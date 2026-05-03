# 跨组学通用概念 MOC

> 这些笔记是后续所有组学章节的共同地基：分布、模型、降维、批次、多重检验、组分约束、零值和 Bayesian。

## 计数与分布

- [[_concepts/poisson-vs-negative-binomial]] — 为什么计数数据普遍用负二项而不是泊松？
- [[_concepts/zero-inflation-vs-true-zero]] — Zero inflation 真的存在吗？真零 vs 假零如何区分？

## 模型框架

- [[_concepts/glm-unified-view]] — GLM 把线性回归 / 逻辑回归 / 泊松 / 负二项统一成什么框架？
- [[_concepts/mixed-models-everywhere]] — Random effect 在 GWAS / scRNA / 重复测量里到底是不是同一件事？
- [[_concepts/bayesian-vs-frequentist-omics]] — 组学里什么时候 Bayesian 真的有用而不是炫技？

## 降维与可视化

- [[_concepts/pca-svd-the-same-thing]] — PCA 与 SVD 的关系是什么？为什么组学里我们其实在用 SVD？
- [[_concepts/umap-tsne-what-they-preserve]] — UMAP 与 t-SNE 各自保留什么、扭曲什么？

## 统计推断与数据结构

- [[_concepts/batch-effects-causes-and-cures]] — 批次效应有几种来源？校正手段如何对应？
- [[_concepts/multiple-testing-frameworks]] — 多重检验：Bonferroni / BH / Storey q / IHW 各自假设和取舍？
- [[_concepts/compositional-data-trap]] — 为什么组分数据会让标准统计失效？

## 推荐阅读路径

1. 先读 [[_concepts/glm-unified-view]] 和 [[_concepts/poisson-vs-negative-binomial]]，建立计数模型框架。
2. 再读 [[_concepts/mixed-models-everywhere]]、[[_concepts/batch-effects-causes-and-cures]] 和 [[_concepts/multiple-testing-frameworks]]，理解为什么组学推断容易假阳性。
3. 然后读 [[_concepts/pca-svd-the-same-thing]] 和 [[_concepts/umap-tsne-what-they-preserve]]，避免过度解释降维图。
4. 最后读 [[_concepts/compositional-data-trap]]、[[_concepts/zero-inflation-vs-true-zero]] 和 [[_concepts/bayesian-vs-frequentist-omics]]，为微生物组、单细胞和多组学整合做准备。

