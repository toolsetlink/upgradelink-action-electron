# test_integration.py
import pytest
import requests
from main import main, call_api
import sys
import os



@pytest.mark.integration
def test_call_api_real():
    # 准备测试数据
    test_data = {
            "version": "1.3.1",
            "promptUpgradeContent": "See the assets to download this version and install.",
            "releaseDate": "2025-05-29T08:44:05.705Z",
            "platforms": {
                "url": "https://github.com/toolsetlink/electron-demo/releases/download/1.3.1"
            }
        }

    # 调用真实API
    result = call_api( 'U7xY6cjxX7RoW8HwUYE9RQ',  'kPUtUMDIjBhS48q5771pow','github', test_data)

    # 验证响应
    assert result.status_code == 200
    print(f"实际API响应: {result.text}")
