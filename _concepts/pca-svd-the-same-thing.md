# PCA 与 SVD 的关系是什么？为什么组学里我们其实在用 SVD？

> PCA 找最大方差方向，SVD 给出它的数值解。

## 长答案

设中心化后的数据矩阵为 $X\in\mathbb{R}^{n\times p}$，行是样本，列是特征。PCA 第一主成分要找一个单位向量 $v$，使投影方差最大：
$$
\max_{\|v\|=1}\frac{1}{n-1}\|Xv\|^2
=\max_{\|v\|=1}v^\top\left(\frac{X^\top X}{n-1}\right)v
$$

用拉格朗日乘子：
$$
L(v,\lambda)=v^\top S v-\lambda(v^\top v-1),\qquad S=\frac{X^\top X}{n-1}
$$
求导：
$$
\frac{\partial L}{\partial v}=2Sv-2\lambda v=0
$$
所以：
$$
Sv=\lambda v
$$
PCA 的 loading 是协方差矩阵 $S$ 的特征向量。

SVD（singular value decomposition）把 $X$ 分解为：
$$
X=U\Sigma V^\top
$$
于是：
$$
X^\top X=V\Sigma^\top U^\top U\Sigma V^\top=V\Sigma^2V^\top
$$
因为 $U^\top U=I$。所以 $X^\top X$ 的特征向量就是 $V$，特征值是 $\sigma_k^2$。PCA score 是：
$$
XV=U\Sigma
$$

组学里我们说“跑 PCA”，多数软件实际算的是中心化/缩放矩阵的 SVD，而不是显式构造 $p\times p$ 协方差矩阵。

## 为什么这么设计

SVD 数值上更稳定，也适合 $p\gg n$ 的组学矩阵。RNA-seq 可能 20,000 genes、几十样本；显式求协方差浪费且易病态。scRNA 更夸张，稀疏矩阵上用 truncated SVD 才可行。

为什么 PCA 能看到 batch？因为它只关心最大方差方向，不知道哪个方向是 biological condition。若 batch 解释的方差最大，PC1 就是 batch。

## ⚠️ 容易混淆 / 常见误解

**误解 1**：PCA 是聚类方法。  
为什么是错的：PCA 是线性投影；聚类结构只是投影后的可视化现象。

**误解 2**：PC1 一定是最重要生物信号。  
为什么是错的：PC1 是最大方差，不是最大生物意义。

**误解 3**：PCA 前是否 scaling 无所谓。  
为什么是错的：不 scaling 时高方差特征主导；scaling 后每列方差等权，问题变了。

## 横向连接

- [[_concepts/batch-effects-causes-and-cures]]
- [[_concepts/umap-tsne-what-they-preserve]]
- [[04-scRNAseq/pca-in-singlecell]]
- [[11-3D-genome/ab-compartments-pc1]]
- [[15-multiomics-integration/jive-snmf-shared-individual]]

## 我现在的理解状态

`#待 Peter 确认`

## 参考

- Pearson (1901), *Philosophical Magazine*
- Hotelling (1933), *Journal of Educational Psychology*
- Eckart & Young (1936), *Psychometrika*
- Alter et al. (2000), *PNAS*

