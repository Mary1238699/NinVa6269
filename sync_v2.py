from github import Github
import requests

# ========== 这里填你自己的信息 ==========
GITHUB_TOKEN = "NinVa6269 — repo"
PUSHPLUS_TOKEN = "9d3d5d7ae86145958c00072b3bdfbed1"
# ======================================

def main():
    try:
        # 连接 GitHub
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo("NinVa6269/NinVa6269")
        
        # 创建 Issue（触发提醒）
        issue = repo.create_issue(
            title="苹果消息来了🍎",
            body="有人发消息啦，快去查看微信"
        )
        print(f"✅ Issue 创建成功：{issue.html_url}")

        # 推送微信提醒
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
