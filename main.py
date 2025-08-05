import sys
import requests
import json
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def call_api(access_key, electron_key, github_token, json_data):
    """调用API并传递JSON数据"""
    try:

        api_url = 'http://xg.api.upgrade.toolsetlink.com/v1/electron/github-aciton/upload'

        logger.info(f"Calling API: {api_url}")

        # 构建API请求URL，添加参数
        params = {'electronKey': electron_key, 'githubToken': github_token}

        # 设置请求头
        headers = {
            'X-AccessKey': access_key,
            'Content-Type': 'application/json'
        }

        # 发送请求
        response = requests.post(api_url, params=params, headers=headers, json=json_data)
        response.raise_for_status()  # 如果请求失败，抛出异常

        logger.info(f"API response: {response.text}")
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        sys.exit(1)


def main():
    # 从命令行参数获取输入
    if len(sys.argv) != 7:
        logger.error("Usage: python main.py <source-url> <access-key> <electron-key> <github-token> <version> <prompt-upgrade-content>")
        sys.exit(1)

    source_url = sys.argv[1]
    access_key = sys.argv[2]
    electron_key = sys.argv[3]
    github_token = sys.argv[4]
    version = sys.argv[5]
    prompt_upgrade_content = sys.argv[6]

    # 获取JSON数据
    json_data = {
        "version": version,
        "promptUpgradeContent": prompt_upgrade_content,
        "platforms": {
            "url": source_url,
        }
    }

    # 调用API
    call_api(access_key, electron_key, github_token, json_data)


if __name__ == "__main__":
    main()