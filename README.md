# UpgradeLink Action Electron

**UpgradeLink** - [全端支持，一站式应用升级分发平台及解决方案](http://upgrade.toolsetlink.com/)

## 项目简介
此项目为开源的 Electron 项目，用于快速接入 UpgradeLink 服务。通过在 GitHub Action 中引入此模块，可自动将生成的版本文件和升级任务配置到 UpgradeLink 系统，无需额外手动操作。

## 接入方式
```yaml
  upgradeLink-upload:
    needs:  publish-electron  # 依赖于publish-electron作业完成
    permissions:
      contents: write 
    runs-on: ubuntu-latest
    steps:
      - name: Send a request to UpgradeLink
        uses: toolsetlink/upgradelink-action-electron@v1.0.1
        with:
          source-url: 'https://github.com/toolsetlink/electron-demo/releases/download/${{ needs.publish-electron.outputs.appVersion }}'
          access-key: ${{ secrets.UPGRADE_LINK_ACCESS_KEY }}  # ACCESS_KEY  密钥key
          electron-key: ${{ secrets.UPGRADE_LINK_ELECTRON_KEY }}    # ELECTRON_KEY electron 应用唯一标识
          github-token: ${{ secrets.GITHUB_TOKEN }}
          version: ${{ needs.publish-electron.outputs.appVersion }}
          prompt-upgrade-content: '提示升级内容'
```


## 完整案例参考
[electron-demo 示例项目](http://upgrade.toolsetlink.com/)  
（可查看实际部署效果及完整 GitHub Action 配置）


### 配置说明
- **source-url**：需指向包含 Electron 应用版本信息地址前缀 例子：https://github.com/toolsetlink/electron-demo/releases/download/1.3.0
- **access-key**：在 UpgradeLink 平台创建应用后生成的访问密钥，用于身份验证
- **electron-key**：Electron 应用在 UpgradeLink 平台的唯一标识，与应用配置绑定
- **github-token**：GITHUB TOKEN
- **version**：版本名
- **prompt-upgrade-content**：提示升级内容


### 最佳实践
1. 在 GitHub 仓库的 **Settings > Secrets** 中配置 `UPGRADE_LINK_ACCESS_KEY` 和 `UPGRADE_LINK_ELECTRON_KEY`，避免明文暴露密钥
2. 确保 `publish-electron` 作业已正确生成并上传版本文件
3. 可通过监听 `release` 事件触发此 Action，实现版本发布与升级配置的自动化流程
