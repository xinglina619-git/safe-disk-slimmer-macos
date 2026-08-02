# Safe Disk Slimmer macOS

A macOS-oriented safety skeleton for a disk-slimming Codex skill. This package is currently read-only and policy-design only: it can guide Codex through macOS storage analysis and risk classification, but it does not include a real deletion executor.

> The correct skill name is `safe-disk-slimmer-macos`. `safe-dish-slimmer-macos` is a typo and should not be used as the directory or installation name.

## Current status

- Read-only by default.
- File contents are not read.
- No file is deleted, moved, or renamed.
- No system configuration, permissions, ownership, startup items, LaunchAgents, LaunchDaemons, or app settings are changed.
- Time Machine, local snapshots, APFS system volumes, `/System`, `/Library`, `/Applications`, and unknown system directories are not cleaned.
- Personal files, projects, course materials, chats, photos, videos, backups, and sync folders are report-only.
- There is currently no macOS scanning script, so this package must not promise automated full-machine scanning. The next efficiency improvement should be a read-only scanner verified on a real macOS machine.

## Why this is separate from Windows

macOS has different directory semantics, cache behavior, symlinks, mount points, APFS snapshots, and developer tool caches. To avoid misuse, this package is separate from `safe-disk-slimmer-windows` and must not share Windows policy files or PowerShell executors.

## Suggested usage

Ask Codex: “Use safe-disk-slimmer-macos to analyze my Mac storage in read-only mode, report first, and do not delete.”

## Future implementation rules

Before any real macOS cleanup script is added:

1. Read-only scanning must be tested on a real macOS machine.
2. Symlinks, mount points, and APFS special volumes must be skipped.
3. Cleanup must use an immutable plan and exact `plan_id` confirmation.
4. The executor must re-check path boundaries independently.
5. Cleanup candidates must be strict whitelist entries; large files must never be deleted automatically.

## Local validation

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

## License

MIT
