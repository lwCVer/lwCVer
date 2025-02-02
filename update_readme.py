import requests
import os

def get_total_stars(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    repos = response.json()
    total_stars = sum(repo['stargazers_count'] for repo in repos)
    return total_stars

def update_readme(total_stars):
    with open("README.md", "r") as file:
        content = file.read()

    # 替换总 Star 数的占位符
    new_content = content.replace("<!-- TOTAL_STARS -->", str(total_stars))

    with open("README.md", "w") as file:
        file.write(new_content)

if __name__ == "__main__":
    username = "lwCVer"  # 替换为你的 GitHub 用户名
    total_stars = get_total_stars(username)
    update_readme(total_stars)
