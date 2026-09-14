# Practical Cleanup Scenarios

This reference is read-only guidance for macOS storage review. It does not authorize deletion, moving files, changing permissions, unloading services, or bypassing macOS privacy prompts.

## Docker Desktop 与虚拟机镜像

- Docker Desktop、Colima、Lima、UTM、Parallels、VMware 和其他虚拟机镜像可能占用大量空间，但它们通常包含用户环境或业务数据。
- 只读报告镜像位置、大小和最后修改时间；不要手工删除 Docker volumes、container layers、虚拟机 `.qcow2`、`.raw`、`.vmdk` 或 `.pvm` 文件。
- 若用户要释放 Docker 空间，应建议先用 Docker Desktop 或 Docker 自带命令查看占用，再由用户确认应用内清理。当前 macOS skill 仍不得执行删除。

## Xcode、Homebrew 与开发缓存

- Xcode DerivedData、Simulator caches、Archives、Homebrew cache、language package caches 可以作为人工判断项展示。
- 当前版本只报告，不执行清理；尤其不要删除正在使用的 Xcode Archives、签名材料、项目目录、`.git` 工作区或课程资料。
- Homebrew 清理可作为人工建议，例如让用户了解 `brew cleanup` 的用途，但不要代运行。

## APFS、Time Machine 与系统卷

- APFS snapshots、Time Machine local snapshots、`/System`、`/Library`、`/private/var/db` 和系统数据卷只做解释，不生成删除命令。
- 不承诺“系统数据”可以被手工删除；优先建议 macOS 储存空间设置、重启、Time Machine 策略或应用内清理。

## 迁移后删除的人工流程

对于明确的旧备份或大安装包，可以给出人工操作路径，但仍保持 read-only：

1. 只读列出源路径、大小和修改时间。
2. 建议用户复制到外置盘、NAS 或其他目标盘。
3. 建议用户校验文件数量、字节数；对少量大文件可校验 `hash`。
4. 只有用户自己确认目标可用后，才由用户在 Finder 中处理源文件。

该流程不得用于照片图库、Messages、微信/聊天数据库、项目源码、同步盘、系统卷或未知应用内部数据。
