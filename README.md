# 多组学学习 Vault

Peter 自用组学方法学 atomic notes。每篇笔记回答一个具体问题，重点放在原理、推导、设计动机、误解和横向连接。

## 在线阅读

https://petemeng.github.io/omics-vault/

## 这个仓库是什么

这是一个面向 Obsidian 和网页双用途的多组学学习库：

- Obsidian 版本保留原始 vault 结构和 `[[双链]]`
- MkDocs 版本自动构建成网页，方便浏览和分享
- 每篇 atomic note 只回答一个问题，避免长文堆叠
- Quiz 用博士资格考风格训练推导、反例和实验设计能力

## 工作规则

- 一篇 atomic note = 一个 `.md` 文件 = 一个具体问题。
- 默认按 `_meta/progress.md` 的顺序继续生成。
- 模板见 `_meta/this-task.md`。
- 所有内部链接使用 Obsidian 双链，路径不带 `.md`。

## 当前内容

Wave 1 已完成：`_concepts/` 跨组学通用概念 10 篇、MOC 和第一份 quiz。

已覆盖的地基概念：

- 负二项 vs 泊松
- GLM 统一框架
- mixed model / random effect
- PCA 与 SVD
- UMAP 与 t-SNE
- 批次效应
- 多重检验
- 组分数据陷阱
- zero inflation
- Bayesian 在组学中的实际价值

下一篇见 `_meta/progress.md`：`00-foundations/sequencing-platforms-error-models`。

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

后续继续从 `_meta/progress.md` 读取下一篇。网页构建时会先运行 `scripts/prepare_mkdocs_source.py`，把 vault 内容同步到 `webdocs/`，再由 MkDocs 构建。
