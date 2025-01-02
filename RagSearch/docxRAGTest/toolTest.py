from crewai_tools import DOCXSearchTool



# 自定义大模型配置
tool = DOCXSearchTool(
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


# 运行工具，调用工具解析文件并检索内容
result = tool.run(
    docx='健康档案.docx',
    search_query="张三九的基本信息"
)
print("result:",result)



