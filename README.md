# Safe Disk Slimmer macOS

面向 macOS 的安全磁盘瘦身 Codex Skill 骨架。当前阶段是只读与策略设计版：可以指导 Codex 做 macOS 磁盘占用分析和风险分级，但不提供真实删除执行器。

> 正确 skill 名称是 `safe-disk-slimmer-macos`。`safe-dish-slimmer-macos` 是拼写错误，不建议作为目录名或安装名。

## 当前状态

- 默认只读。
- 不读取文件内容。
- 不删除、移动、改名任何文件。
- 不修改系统配置、权限、所有权、启动项、LaunchAgents、LaunchDaemons 或应用配置。
- 不处理 Time Machine、本地快照、APFS 系统卷、`/System`、`/Library`、`/Applications` 或未知系统目录。
- 个人文件、项目文件、课程资料、聊天数据、照片、视频、备份和同步盘只报告。
- 当前没有 macOS 扫描脚本，因此不能承诺自动扫描整机；如需增强，只能先补只读扫描器并完成 macOS 实机验证。

## 为什么与 Windows 版拆开

macOS 的目录结构、缓存语义、符号链接、挂载点、APFS 快照和开发工具缓存都与 Windows 不同。为了避免误用，本包独立于 `safe-disk-slimmer-windows`，不能共用 Windows 的策略文件或 PowerShell 执行器。

## 建议使用方式

在 Codex 中说：“使用 safe-disk-slimmer-macos 只读分析我的 Mac 磁盘占用，先报告，不要删除。”

## 后续实现原则

真正加入 macOS 清理脚本前，必须先满足：

1. 在 macOS 实机上完成只读扫描测试。
2. 明确跳过符号链接、挂载点和 APFS 特殊卷。
3. 删除前生成不可变计划，并要求用户确认 `plan_id`。
4. 删除器必须二次验证路径边界。
5. 任何清理候选都必须是严格白名单，不得根据“大文件”自动删除。

## 本地验证

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

## 许可

MIT
