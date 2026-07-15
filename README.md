# web2rss

> 输入网址输出 rss

- [x] 支持私有化部署

- [x] 支持 AI

- [x] 支持 rss 源代理

- [x] local router (pull) -> remote router -> save local

- [x] local router (push) -> remote router -> save remote

- [x] fetch (error) -> proxy

## 在线体验

[web2rss](https://web2rss.cc/)

## 使用

**直接运行**

- 下载项目

- 命令行 pip install -f ./requirements.txt

- 复制 `.env.example` 为 `.env` 并填写配置参数

- 命令行 python3 ./app.py

- 打开浏览器

**docker 运行**

- 下载项目

- 命令行 docker build -t web2rss .

- 命令行 docker run -p 3390:3390 --env-file .env web2rss

- 打开浏览器

## 配置说明

复制 `.env.example` 为 `.env`，修改以下参数：

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `GPT_API_KEY` | AI API 密钥 | `sk-xxx` |
| `GPT_API_URL` | AI API 端点地址 | `https://openai.com/v1/chat/completions` |
| `GPT_MODEL` | AI 模型名称 | `gpt-4o-mini` |
| `PROXY_URL` | 代理地址 | `https://localhost:8080/proxy` |
| `REMOTE_URL` | 远程路由地址 | `https://raw.githubusercontent.com/weekend-project-space/web2rss/main` |
| `LOCAL_REPO_PATH` | 本地仓库路径 | `.` |
