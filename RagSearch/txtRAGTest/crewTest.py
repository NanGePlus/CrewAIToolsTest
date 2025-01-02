import os
from dotenv import load_dotenv
from crewai import LLM as ChatOpenAI
from crew import CrewtestprojectCrew




# 从 .env 文件加载环境变量
load_dotenv()


def runCrew(query, txt_path, llm):
    inputs = {
        "query": query,
        "txt_path": txt_path,
    }
    # 传入llm，指定crew中的Agent使用什么大模型
    result = CrewtestprojectCrew(llm).crew().kickoff(inputs=inputs)
    # 将返回的数据转成string类型
    formatted_response = str(result)
    print(f"LLM最终回复结果: {formatted_response}")


if __name__ == '__main__':
    llm = ChatOpenAI(
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY"),
        model=os.getenv("OPENAI_CHAT_MODEL")
    )
    query = "张三九的健康档案信息及建议"
    txt_path = "健康档案.txt"
    runCrew(query, txt_path, llm)




