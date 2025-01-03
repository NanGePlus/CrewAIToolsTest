# 核心功能:在CrewAI中定义Agent和Task，并通过Crew来管理这些Agent和Task的执行流程
# 导入相关的依赖包
from crewai import Agent, Crew, Process, Task
# CrewBase是一个装饰器，标记一个类为CrewAI项目。agent、task和crew装饰器用于定义agent、task和crew
from crewai.project import CrewBase, agent, crew, task
# 导入官方提供的工具包
from crewai_tools import DOCXSearchTool




# 初始化工具 自定义大模型
docx_tool = DOCXSearchTool(
    config=dict(
        llm=dict(
            provider="openai",
            config=dict(
                base_url="https://yunwu.ai/v1",
                api_key="sk-ux4NQ9lOgCwqJMrJjjungDRDwZjlGqCnaln9n5aAnwQv8FEc",
                model="gpt-4o-mini"
            ),
        ),
        embedder=dict(
            provider="openai",
            config=dict(
                api_base="https://yunwu.ai/v1",
                api_key="sk-ux4NQ9lOgCwqJMrJjjungDRDwZjlGqCnaln9n5aAnwQv8FEc",
                model="text-embedding-3-small"
            ),
        ),
    )
)


# 定义了一个CrewtestprojectCrew类并应用了@CrewBase装饰器初始化项目
# 这个类代表一个完整的CrewAI项目
@CrewBase
class CrewtestprojectCrew():
	# agents_config和tasks_config分别指向agent和task的配置文件，存放在config目录下
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self, llm):
		# Agent使用的大模型
		self.llm = llm

	# 通过@agent装饰器定义一个函数researcher，返回一个Agent实例
	# 该代理读取agents_config中的researcher配置
	# 参数verbose=True用于输出调试信息
	# tools=[MyCustomTool()] 表示代理可以加载自定义工具，但此处为注释，需根据需求自行加载。
	@agent
	def health_data_extractor(self) -> Agent:
		return Agent(
			config=self.agents_config['health_data_extractor'],
			verbose=True,
			llm=self.llm,
			tools=[docx_tool]
		)

	@agent
	def health_advisor(self) -> Agent:
		return Agent(
			config=self.agents_config['health_advisor'],
			verbose=True,
			llm=self.llm
		)

	# 通过@task装饰器定义research_task，返回一个Task实例
	# 配置文件为tasks.yaml中的research_task部分
	@task
	def extract_health_data_task(self) -> Task:
		return Task(
			config=self.tasks_config['extract_health_data_task'],
			tools=[docx_tool]
		)

	@task
	def generate_health_advice_task(self) -> Task:
		return Task(
			config=self.tasks_config['generate_health_advice_task'],
		)



	# Crew类将agent和task组合成一个执行队列，并根据指定的执行流程进行任务调度
	# 通过@crew装饰器定义crew，创建一个Crew实例
	# agents=self.agents和tasks=self.tasks分别自动获取@agent和@task装饰器生成的agent和task
	# process=Process.sequential指定agent执行顺序为顺序执行模式
	# process=Process.hierarchical指定agent执行顺序为层次化执行
	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True
		)








