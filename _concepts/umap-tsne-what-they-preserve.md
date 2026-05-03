# UMAP 与 t-SNE 各自保留什么、扭曲什么？

> 它们保局部邻域，不保全局距离和簇大小。

## 长答案

t-SNE（t-distributed stochastic neighbor embedding）先在高维空间把点 $j$ 作为点 $i$ 邻居的概率写成：
$$
p_{j|i}=\frac{\exp(-\|x_i-x_j\|^2/2\sigma_i^2)}{\sum_{k\ne i}\exp(-\|x_i-x_k\|^2/2\sigma_i^2)}
$$
再对称化为 $p_{ij}$。低维空间用重尾 t 分布：
$$
q_{ij}=\frac{(1+\|y_i-y_j\|^2)^{-1}}{\sum_{k\ne l}(1+\|y_k-y_l\|^2)^{-1}}
$$
优化目标是：
$$
KL(P\|Q)=\sum_{i\ne j}p_{ij}\log\frac{p_{ij}}{q_{ij}}
$$
因为是 $KL(P\|Q)$，高维里近的点若低维放远会被重罚；高维里远的点低维放近惩罚较弱。所以 t-SNE 强保局部邻域，弱保全局距离。

UMAP（Uniform Manifold Approximation and Projection）先构建 fuzzy kNN graph。高维边权近似：
$$
w_{ij}=\exp\left(-\frac{\max(0,d(x_i,x_j)-\rho_i)}{\sigma_i}\right)
$$
低维边权用一条可调曲线：
$$
\hat w_{ij}=\frac{1}{1+a\|y_i-y_j\|^{2b}}
$$
优化 fuzzy set cross-entropy：
$$
\sum_{ij} w_{ij}\log\frac{w_{ij}}{\hat w_{ij}}+(1-w_{ij})\log\frac{1-w_{ij}}{1-\hat w_{ij}}
$$

UMAP 的图结构让它通常比 t-SNE 更保留一些粗略拓扑，但仍不保证真实全局距离。

## 为什么这么设计

高维组学数据里欧氏距离本身会退化，直接保全局距离很难。t-SNE 和 UMAP 都选择保“谁是谁的邻居”，牺牲簇间距离、簇面积和轴的解释性。这样做适合可视化细胞状态连续谱，但不适合作为统计检验。

为什么不用 PCA？PCA 是线性投影，能保最大方差方向，但非线性流形上的局部结构可能被压扁。UMAP/t-SNE 用局部邻域图换取更清晰的可视化。

## ⚠️ 容易混淆 / 常见误解

**误解 1**：UMAP 上两个簇距离远，生物差异就更大。  
为什么是错的：低维距离受参数、初始化和图优化影响，不是可解释尺度。

**误解 2**：簇面积代表细胞数量或多样性。  
为什么是错的：布局会拉伸或压缩局部密度，面积没有直接统计意义。

**误解 3**：UMAP 可以替代聚类。  
为什么是错的：UMAP 是 visualization，聚类应在原始空间或 PCA/邻接图上定义。

## 横向连接

- [[_concepts/pca-svd-the-same-thing]]
- [[04-scRNAseq/umap-tsne-in-sc]]
- [[04-scRNAseq/leiden-louvain-graph]]
- [[08-ATAC/scatac-tfidf-lsi]]
- [[15-multiomics-integration/mofa-variational]]

## 我现在的理解状态

`#待 Peter 确认`

## 参考

- van der Maaten & Hinton (2008), *Journal of Machine Learning Research*
- McInnes et al. (2018), *arXiv*
- Kobak & Berens (2019), *Nature Communications*

