# 1、介绍
## 1.1 主要内容                                                 
本期系列相关视频为大家测试CrewAI官方提供的Tools，按照发布的先后顺序:                          
**(第一期)[2025.01.02]RAG搜索(1)**               
主要内容:针对官方提供的CSV、DOCX、PDF、TXT文件内容检索工具进行RAG应用。提供工具demo测试和Crew应用测试                                              

## 1.2 CrewAI框架           
CrewAI是一个用于构建多Agent协作应用的框架，它能够让多个具有不同角色和目标的Agent共同协作，完成复杂的任务                          
该工具可以将任务分解，分配给不同的Agent，借助它们的特定技能和工具，完成各自负责的子任务，最终实现整体任务目标              
官网:https://www.crewai.com/                                          
GitHub:https://github.com/crewAIInc/crewAI                                           
关于CrewAI更多的应用，大家请查看我的主页，有关于CrewAI基础及高阶应用分享                


# 2、前期准备工作
## 2.1 开发环境搭建:anaconda、pycharm
anaconda:提供python虚拟环境，官网下载对应系统版本的安装包安装即可                                      
pycharm:提供集成开发环境，官网下载社区版本安装包安装即可                                               
**可参考如下视频:**                      
集成开发环境搭建Anaconda+PyCharm                                                          
https://www.bilibili.com/video/BV1q9HxeEEtT/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                             
https://youtu.be/myVgyitFzrA          

## 2.2 大模型相关配置
(1)GPT大模型使用方案(第三方代理方式)                               
(2)非GPT大模型(阿里通义千问、讯飞星火、智谱等大模型)使用方案(OneAPI方式)                         
(3)本地开源大模型使用方案(Ollama方式)                                             
**可参考如下视频:**                                   
提供一种LLM集成解决方案，一份代码支持快速同时支持gpt大模型、国产大模型(通义千问、文心一言、百度千帆、讯飞星火等)、本地开源大模型(Ollama)                       
https://www.bilibili.com/video/BV12PCmYZEDt/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                 
https://youtu.be/CgZsdK43tcY           


# 3、项目初始化
## 3.1 下载源码
GitHub或Gitee中下载工程文件到本地，下载地址如下：                
https://github.com/NanGePlus/CrewAIToolsTest                                                                                
https://gitee.com/NanGePlus/CrewAIToolsTest                                                       

## 3.2 构建项目
使用pycharm构建一个项目，为项目配置虚拟python环境                       
项目名称：CrewAIToolsTest                                                   
虚拟环境名称保持与项目名称一致                                       

## 3.3 将相关代码拷贝到项目工程中           
将下载的代码文件夹中的文件全部拷贝到新建的项目根目录下                      

## 3.4 安装项目依赖          
打开命令行终端在项目根目录下执行如下命令安装依赖包                                            
pip install -r requirements.txt                     
每个软件包后面都指定了本次视频测试中固定的版本号,建议先使用要求的对应版本进行本项目测试，避免因版本升级造成的代码不兼容。测试通过后，可进行升级测试                      


# 4、项目测试          
运行脚本分别测试CSV、DOCX、PDF、TXT文件内容RAG                   
运行脚本前根据自己实际情况调整大模型相关参数                 
**(1).env环境变量参数调整**                    
GPT大模型配置参数(代理方式):                                  
OPENAI_BASE_URL=https://yunwu.ai/v1                          
OPENAI_API_KEY=sk-ux4NQ9lOgCwqJMrJjjungDRDwZjlGqCnaln9n5aAnwQv8FEc                               
OPENAI_CHAT_MODEL=gpt-4o-mini                           
**(2)tools中指定模型配置**                      
GPT大模型配置参数(代理方式):          
tool = CSVSearchTool(                
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












