# Ipad_project_01

用于在 iPad 上编写小型程序、运行测试，并通过 GitHub 与电脑同步。

## 工具分工

| 工具 | 负责什么 |
| --- | --- |
| Working Copy | Clone、Pull、查看差异、Commit、Push |
| Textastic | 打开项目目录并原地编辑文件 |
| a-Shell | 运行 Python 脚本和测试 |

先使用 Python 标准库，不需要安装第三方依赖。iPad 上的 a-Shell 不是完整的桌面 Linux 环境；新增语言、编译工具或依赖前，先确认设备支持。

## 第一次在 iPad 上使用

1. 在 Working Copy 点击 `+` → Clone repository，输入：

   ```text
   https://github.com/xcy1-cn/Ipad_project_01.git
   ```

2. 在系统“文件”App 的侧边栏中启用 Working Copy。
3. 在 Textastic 选择 `Add External Folder…`，进入 Working Copy，选择这个仓库并打开。以后直接在这里编辑，不要导出副本。
4. 在 a-Shell 执行：

   ```sh
   pickFolder
   ```

   尝试选择同一个仓库文件夹。选择后运行 `pwd` 和 `ls`，确认当前位置包含本 README、`examples` 和 `tests`。若没有进入项目目录，先切换到所选目录再继续。不同 iPadOS 和文件提供器版本的支持情况可能不同。

5. 在项目根目录运行：

   ```sh
   python3 examples/hello.py
   python3 -m unittest discover -s tests -v
   ```

   预期脚本输出 `Hello, iPad!`，测试结果显示 `OK`。

## 每次开发的流程

1. Working Copy 中 Pull，取得最新代码；有未提交修改时先检查并处理。
2. Textastic 编辑并保存文件。
3. a-Shell 在同一目录运行脚本与测试。
4. Working Copy 查看差异，确认包含刚才的修改，再 Commit 和 Push。
5. 换到电脑或另一台设备前先 Push；另一端开始工作前先 Pull。

首次 Push 需要在 Working Copy 配置 GitHub 认证，并确认当前 App 授权支持推送。如果推送失败，保留本地提交，按 App 提示检查授权和远程地址。

## 如果 a-Shell 无法选择 Working Copy 文件夹

不要在两份代码之间来回复制后继续开发。可以改用 a-Shell 的 Documents 下的项目目录作为共同目录：

1. 将项目文件准备到“我的 iPad → a-Shell”下的一个专用文件夹。
2. 使用 Working Copy 的 `Link external directory` 将该目录纳入 Git 管理；链接前确认目录内容与仓库一致，保留已有修改。
3. 在 Textastic 中打开这个外部目录，在 a-Shell 中进入同一个目录。
4. 修改并保存 `examples/hello.py`，确认 Working Copy 能看到差异，再运行脚本，验证三个 App 使用的是同一份文件。

以设备上实际可选的目录和 App 提示为准；若链接功能不可用，先解决目录访问问题。

## 目录

```text
examples/hello.py       第一个可运行的 Python 示例
tests/test_hello.py     标准库 unittest 测试
scratch/README.md      临时练习区说明
```

运行命令时以仓库根目录为当前目录。项目统一使用 UTF-8 编码、LF 换行。不要提交令牌、密码、私钥或真实业务数据；本仓库为公开仓库。

## 官方参考

- [Textastic 与 Working Copy 集成](https://www.textasticapp.com/v10/manual/integration_other_apps/git_client_working_copy.html)
- [Working Copy 用户指南：外部仓库](https://workingcopy.app/manual/external-repos/)
- [a-Shell：命令与文件夹访问](https://github.com/holzschu/a-shell)
