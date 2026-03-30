from github import Github
import requests

# ========== 替换成你自己的信息 ==========
GITHUB_TOKEN = NinVa6269 — repo

REPO_NAME = "Mary1238699/NinVa6269"
PUSHPLUS_TOKEN = 9d3d5d7ae86145958c00072b3bdfbed1
# ========================================

def main():
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
        
        issue = repo.create_issue(
            title="苹果消息来了🍎",
            body="微信或群里发消息，第一时间提醒"
        )
        print(f"✅ Issue 创建成功：{issue.html_url}")

        push_url = "https://www.pushplus.plus/api/send"
        data = {
            "token": PUSHPLUS_TOKEN,
            "title": "苹果消息来了🍎",
            "content": "有人发消息啦，快去查看微信"
        }
        res = requests.post(push_url, json=data)
        print(f"✅ 微信推送状态：{res.status_code}")

    except Exception as e:
        print(f"❌ 错误：{str(e)}")

if __name__ == "__main__":
    main()
