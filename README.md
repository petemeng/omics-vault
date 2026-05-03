# 多组学学习 Vault

Peter 自用组学方法学 atomic notes。每篇笔记回答一个具体问题，重点放在原理、推导、设计动机、误解和横向连接。

网页版地址：

https://petemeng.github.io/omics-vault/

## 工作规则

- 一篇 atomic note = 一个 `.md` 文件 = 一个具体问题。
- 默认按 `_meta/progress.md` 的顺序继续生成。
- 模板见 `_meta/this-task.md`。
- 所有内部链接使用 Obsidian 双链，路径不带 `.md`。

## 本地预览

```powershell
$env:PYTHONIOENCODING='utf-8'; python scripts/prepare_mkdocs_source.py
$env:PYTHONIOENCODING='utf-8'; python -m mkdocs serve
```

构建静态网页：

```powershell
$env:PYTHONIOENCODING='utf-8'; python scripts/prepare_mkdocs_source.py
$env:PYTHONIOENCODING='utf-8'; python -m mkdocs build --strict
```

## 当前状态

Wave 1 `_concepts/` 已开始生成。后续继续从 `_meta/progress.md` 读取下一篇。
