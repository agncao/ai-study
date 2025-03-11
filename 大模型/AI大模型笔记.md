# 提示词

## 不知道顺利数据怎么办

- 有得大模型会公开友好格式，例如：chatGPT对md格式友好 claude对xml格式友好
- 如果没有公开，只能不断的试了
- 如果底层大模型换了，提示词也要重新优化

# Prompt 的典型构成

- 角色。例如：你是一个JAVA开发工程
- 任务
- 背景
- 例子
- 输入
- 输出

# AI大模型笔记

## Transformer

### 它是干什么的

- 基本组成依然是机器翻译模型里最常见的`seq2seq`网络

- 输入输出都很直观，其核心架构就是中间的网络设计，例如

  我爱你 -> TRANSFORMER网络架构 -> I love you 

### 应用场景

- 应用于翻译，例如：我爱你 -> I love you
- 问答系统
- 图像分类
- 视频分析
- 甚至推荐系统也用上了Tranformer

### 为何不用传统的RNN

- 不能像transformer的attention机制一样能并行处理
- Transformer能轻松捕捉长距依赖

### BERT：一种自然语言解决方案

- 基于Tranformer网络架构
- 需熟悉word2vec RNN网络模型 了解向量如何建构
- 开源项目
- 提供预训练模型，基本任务哪里直接用都行

### 传统的word2vec

传统的向量的问题：

 - 不会根据上下文更新向量。例如 干啥呢 在不同语境有不同语意，训练好了向量永久不变了

### self-attention 是什么

- 比如输入一句话，关注点是哪些词
- 每个词与你输入的整体的关联，得到一个权重
- 目的是语言文字特征提取出来，相当于C V里的卷积层网络
- 缩放点积机制计算方法

### 注意力机制算法

- (K矩阵*Q矩阵)/缩放 输入到SoftMax函数得到一个0-1之间的权重，然后再与V矩阵相乘得到注意力值

​	（1）定义了Q、K、V三个向量

​	（2）嵌入式输入

​	（3）得到Wq、Wk、Wv三个向量的矩阵

​	（4）缩放点积注意力：如果不缩放，原始数据太大的话，比较大的向量值可能会权重无限接近1，比较小的会权重无限接近0

- 多头注意力：像卷积层一样一层一层提取特征

- 将多头Q KV向量 注意力计算结果拼接(concat)一起再经过线性变换得到最终的注意力结果

## Embedding

<img src="/Users/caojm/course/学习笔记/AI/大模型/images/Embedding模型图解.svg" alt="Embedding模型图解" style="zoom:150%;" />

## 常用的数据科学库

### 1. **tiktoken**

- **用途**：`tiktoken` 是一个用于处理 Token 化（tokenization）任务的库，特别是在处理与大语言模型（如 GPT）相关的任务时。
- **常见应用**：它用于将文本转换成模型可以理解的 tokens（词元），并且支持高效的文本编码和解码。通常在处理自然语言处理（NLP）任务时，尤其是对 GPT 系列模型进行文本预处理时会使用这个库。

### 2. **matplotlib**

- **用途**：`matplotlib` 是一个非常流行的 2D 图形绘制库，常用于数据可视化。
- **常见应用**：它可以帮助你创建静态、动态、交互式的图表和图像，如折线图、散点图、条形图等。`matplotlib` 允许你对图表进行高度定制，广泛用于科学计算和数据分析领域。
- **示例**：绘制数据趋势图、统计图表等。

### 3. **plotly**

- **用途**：`plotly` 是一个用于创建交互式图表的库，可以生成 2D 和 3D 图表。
- **常见应用**：与 `matplotlib` 不同，`plotly` 的图表具有高度交互性，可以在网页中进行缩放、拖动等操作，非常适合数据展示和分析。它支持创建更复杂和美观的图形，例如交互式的柱状图、饼图、热图、地图等。
- **示例**：制作交互式的可视化仪表板，展示数据分析结果。

### 4. **scikit-learn**

- **用途**：`scikit-learn` 是一个非常流行的机器学习库，提供了广泛的算法和工具，适用于分类、回归、聚类、降维等任务。
- **常见应用**：它包括许多常用的机器学习模型，如支持向量机（SVM）、决策树、随机森林、KNN、逻辑回归等，同时也提供了数据预处理、特征选择、模型评估等功能。
- **示例**：使用 `scikit-learn` 训练机器学习模型并进行预测、数据分割和评估。

### 5. **numpy**

- **用途**：`numpy` 是 Python 中用于处理大规模数值计算的基础库，特别是对数组和矩阵进行高效操作。
- **常见应用**：它提供了一个强大的 `ndarray` 对象，用于存储和操作多维数组。`numpy` 支持大规模的数学运算，如线性代数、傅里叶变换、随机数生成等，广泛应用于科学计算和数据分析中。
- **示例**：执行矩阵运算、计算统计量、处理大量数据集。

### 6. Pandas 

是 Python 中用于数据处理和分析的非常强大的库，特别适用于结构化数据（如表格数据）。它的主要功能是提供快速、灵活、表达力强的数据结构，特别是 DataFrame 和 Series，来简化数据清洗、探索和分析的工作。

### 主要功能和应用：

1. **DataFrame 和 Series 数据结构**：
   - **DataFrame**：一个二维表格数据结构，类似于数据库中的表或 Excel 中的工作表。它允许按行和列索引数据，并且每列可以有不同的类型（整数、浮动、字符串等）。
   - **Series**：一个一维数据结构，类似于数组或列表，通常用于表示单列数据。
2. **数据清洗和预处理**：
   - **处理缺失数据**：Pandas 提供了便捷的方法来填补或删除缺失值（如 `NaN`）。
   - **数据过滤和选择**：通过索引和条件筛选数据，可以非常容易地选择和过滤出需要的数据。
   - **数据变换**：可以对数据进行归一化、标准化、映射等变换操作。
3. **数据操作**：
   - **合并与连接**：Pandas 支持多种方式合并不同的数据集（例如 `concat`、`merge`），就像数据库中的连接操作。
   - **分组和聚合**：使用 `groupby` 可以将数据按某个或多个列进行分组，然后进行汇总统计（例如计算平均值、最大值、计数等）。
   - **排序**：可以根据一个或多个列对数据进行排序。
4. **数据读取与存储**：
   - **支持多种数据格式**：Pandas 可以读取和写入多种文件格式，如 CSV、Excel、JSON、SQL 等。
   - **快速读取大数据集**：Pandas 提供了高效的读取大数据集的功能，适合处理海量数据。
5. **数据可视化**：
   - Pandas 自带了一些基本的数据可视化功能，虽然它不如 `matplotlib` 或 `plotly` 强大，但可以快速地绘制数据图表（如折线图、条形图等），对数据进行初步可视化。

### 示例代码：

```python
import pandas as pd

# 创建一个 DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# 查看前几行数据
print(df.head())

# 选择一列
print(df['Name'])

# 筛选数据：筛选年龄大于 30 的人
filtered_df = df[df['Age'] > 30]
print(filtered_df)

# 数据分组并计算平均年龄
grouped = df.groupby('City')['Age'].mean()
print(grouped)
```

### 总结：

- **`tiktoken`**：处理文本 Token 化，通常与 NLP 和大模型相关。

- **`matplotlib`**：用于创建静态图表，常用于数据可视化。

- **`plotly`**：用于创建交互式图表，适合展示动态数据和分析结果。

- **`scikit-learn`**：机器学习库，用于构建、训练和评估机器学习模型。

- **`numpy`**：用于高效数值计算和数组操作，是数据分析和科学计算的基础库。

- **`Pandas `** 是一个非常适合数据分析和处理的库，特别是在处理和清理结构化数据时，它提供了高效、简便的操作。它在数据科学、机器学习、金融分析等领域非常常用，几乎是任何数据分析项目的基础工具之一。如果你处理的主要是表格数据或时间序列数据，Pandas 会极大地提高你的效率。

  <mark>如果你正在进行数据清洗、处理和分析，Pandas 是一个非常重要的工具！</mark>

这些库在数据科学、机器学习、自然语言处理等领域中都是非常重要的工具，您可以根据项目的需求选择适合的库

## LCEL

1. 可监听生命周期 r1.with_listen(on_start=fun1, on_end=fun2);

2. 提示词 --> llm ->生成文本 --> 提示词2  --> 评分
   - 创建大预言模型 `ChatOpenAI(model={},api_key={},base_url={},temprature={})`
   - 创建提示词模板 `PromptTemplate.from_template('{}')`
   - 创建链 `chain1= promt1Obj | llm | StrOutputParser()`
   - 创建提示词2：`PromptTemplate.from_template('text_content')`
   - 创建链： `{'text_content':chain1} |promt2Obj |llm | StrOutputParser()`
3. RunnableLambda
4. 给企业做多模态，并不是我们在deepseek看到的能上传图片、也能文本等各种类型的输入。而是根据用户的输入来动态的选择不同的提示词模版，然后根据提示词模板来动态的调用不同方向的大模型任务

Tool and Agent

1. langChain vs Dify 

   用企业最好还是langChain 比较灵活，Dify有收费的

2. VLLM vs Ollama ： 私有化部署

​		企业里用VLLM，个人可以使用Ollam

​		Ollam可视化部署，一个命令就行，做不了太多的个性化定制

​		VLLM灵活性高，可以对大模型做一些修改，比如对模型输入输出做统一的修改

3. 内置Tool

   Tavily搜索

    - 去官网注册一个api key

      ```python
      	# 先创建一个模型对象
        model = ChatOpenAI(model='{}',temprature={},api_key={},base_url={})
        #使用哪个搜索对象
        search_tool = TavilySearchResults(max_results=3)
        # search_tool.invoke('今天的天气怎样') #这个实际中很少用，这个只是工具，只会做简单的搜索，没有大模型推理能力
        
        tools = [search_tool]
        agent = create_react_agent(llm, tools)	#tools必须传，但大模型未必会用上，大模型会自主决策需要用传入的哪些工具
        # resp = agent.invoke({'messages':[HumanMessage(content='湖南的省会是哪个城市')]})	#并没有调用search_tool
          resp = agent.invoke({'messages':[HumanMessage(content='长沙今天的天气怎么样')]})	
          print(resp)
          
          # 会打印出用了哪些工具，在ToolMessages
      ```

      

4. 创建一个Agent `create_react_agent(llm, tools)` 

​		这个是一个langchain graph的一个对象

4. 