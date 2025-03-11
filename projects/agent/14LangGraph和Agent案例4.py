import os
from typing import Annotated

from langchain_community.tools import TavilySearchResults
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.constants import START, END
from langgraph.graph import add_messages, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from typing_extensions import TypedDict

from lc01.langgraph_utils import draw_graph, loop_graph_invoke, loop_graph_invoke_tools


# 状态(state)， 节点（node）， 边(edge)

# 需求：对话的案例：

# 1、定义一个状态 类型
class MyState(TypedDict):  # 在整个流程中， 状态用来保存历史记录
    # messages:状态中保存数据的key， list: 数据类型， add_messages：一个函数，用于更新list数据
    messages: Annotated[list, add_messages]


# 2、定义一个流程图
graph = StateGraph(MyState)

# 3、准备一个node（节点）, 并且把它添加到流程图中
# llm = ChatOpenAI(
#     temperature=1.0,
#     model='gpt-4o',
#     api_key="sk-doD81WgxSoF9A6xYzhgW7GUh5frRwPETI8mDq3ce4UaWnCPF",
#     base_url="https://xiaoai.plus/v1")

# deepseek-v3可以用，但是会出现死循环和空返回值，deepseek-r1不支持

llm = ChatOpenAI(
    model='glm-4-plus',
    temperature=1.0,
    openai_api_key='4afc2ced3f174bc89dd17b3e47d2586d.qqcyAW2zEEqj5rY3',
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)

# 4、添加一个工具节点（互联网搜索的工具）
os.environ["TAVILY_API_KEY"] = "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"
search_tool = TavilySearchResults(max_results=2)
tools = [search_tool]

# 把工具和大模型绑定一下
agent = llm.bind_tools(tools)


def chatbot(state: MyState):
    return {'messages': [agent.invoke(state['messages'])]}


# chatbot 节点函数如何以当前 State 作为输入，并返回一个包含更新后的 messages
# 第一个参数是唯一的节点名称
# 第二个参数是每当节点被使用时将调用的函数或对象
graph.add_node('agent', chatbot)

# 添加一个工具节点
tool_node = ToolNode(tools=tools)
graph.add_node('tools', tool_node)
https://www.yuque.com/damingming-e16aa/xx8pma/vyig1i8ugqnzqmlg
# 根据智能体自动决策是否需要调用工具，
graph.add_conditional_edges('agent', tools_condition)

# 4、设置边
graph.add_edge('tools', 'agent')
# 设置入口节点
graph.set_entry_point('agent')
# 我们正在使用内存中的检查点。它将所有内容都保存在内存中。
# 在生产应用程序中，您可能会将其更改为使用 SqliteSaver 或 PostgresSaver 并连接到您自己的数据库 # pip install langgraph-checkpoint-sqlite
memory_checkpointer = MemorySaver()
# sqlite_checkpointer = SqliteSaver('sqlite:///tset.db')

# 整个graph已经确定
graph = graph.compile(
    checkpointer=memory_checkpointer,
    interrupt_before=['tools']  # 在执行到"tools"节点之前中断，允许外部处理或检查
    # 注意：如果需要，也可以在工具执行后中断
    # interrupt_after=["tools"]  # 取消注释此行可以在"tools"节点执行后中断

)  # 构建一个图对象


# 5、把graph变成一张图
# draw_graph(graph, 'graph2.png')

thread_id = input('请输入一个sessionId:')
config = {"configurable": {"thread_id": thread_id}}

# 执行这个工作流
while True:
    try:
        user_input = input('用户: ')
        if user_input.lower() in ['q', 'exit', 'quit']:
            print('对话结束，拜拜！')
            break
        else:
            # 执行 工作流
            loop_graph_invoke(graph, user_input, config)
            # 查看此时的状态
            now_state = graph.get_state(config)
            # print('此时的状态数据为: ', now_state)

            if 'tools' in now_state.next:  # 判断下一个节点是否为：tool
                # 可以人工介入
                tools_script_message = now_state.values['messages'][-1]  # 状态中存储的最后一个message
                print('Tools Script: ', tools_script_message.tool_calls)

                if input('人工客户输入是否继续工具调用: yes或者no').lower() == 'yes':
                    loop_graph_invoke_tools(graph, None, config)

    except Exception as e:
        print(e)
