# Random effect 在 GWAS / scRNA / 重复测量里到底是不是同一件事？

> 是同一思想：把相关性写进协方差。

## 长答案

随机效应（random effect）的核心不是“某因素随机抽样”，而是把观测之间的相关性显式写进模型。标准线性混合模型（linear mixed model, LMM）：
$$
y=X\beta+Zu+\epsilon,\qquad u\sim N(0,G),\quad \epsilon\sim N(0,R)
$$

因此：
$$
\text{Var}(y)=\text{Var}(Zu+\epsilon)=ZGZ^\top+R
$$
这里交叉项为 0，因为假设 $u$ 与 $\epsilon$ 独立。所有应用差异，本质上都在选择 $Z$、$G$、$R$。

GWAS 中，个体间有亲缘相关：
$$
y=X\beta+g+\epsilon,\qquad g\sim N(0,\sigma_g^2K)
$$
所以：
$$
\text{Var}(y)=\sigma_g^2K+\sigma_e^2I
$$
$K$ 是 kinship matrix。它让近亲个体的 residual 允许更相似，避免把群体结构误判成 SNP 效应。

重复测量中，多个时间点来自同一对象。可写：
$$
y_{ij}=x_{ij}^\top\beta+b_i+\epsilon_{ij},\qquad b_i\sim N(0,\sigma_b^2)
$$
同一对象内任意两个观测的协方差为 $\sigma_b^2$。

scRNA 的 donor-level random effect 也是这个逻辑：同一 donor 的细胞不是独立样本。随机截距允许它们共享 donor baseline。

## 为什么这么设计

如果相关性不进模型，标准误会被低估。GWAS 中是假阳性膨胀；scRNA 中是 pseudoreplication；重复测量中是把同一对象内的多个点当成多个独立对象。

为什么不直接加 fixed effect？当 level 很少且关心每个 level，fixed effect 更稳；当 level 多且目标是估计方差结构，random effect 更合适。GWAS 的 kinship 不是普通 categorical batch，无法用成千上万个固定效应优雅表示。

## ⚠️ 容易混淆 / 常见误解

**误解 1**：random effect 只用于随机抽样的因素。  
为什么是错的：实践中它常用于建模相关性与 shrinkage，抽样解释不是唯一理由。

**误解 2**：batch 总该设 random effect。  
为什么是错的：只有 2 个 batch 时方差成分估计很弱，通常 fixed effect 更直接。

**误解 3**：加了 random effect 就解决 confounding。  
为什么是错的：如果 batch 与 condition 完全重合，协方差建模也分不开二者。

## 横向连接

- [[_concepts/glm-unified-view]]
- [[_concepts/batch-effects-causes-and-cures]]
- [[02-GWAS/why-mixed-model-in-gwas]]
- [[04-scRNAseq/pseudoreplication-pseudobulk]]
- [[00-foundations/experimental-design-fundamentals]]

## 我现在的理解状态

`#待 Peter 确认`

## 参考

- Henderson (1950), *Annals of Mathematical Statistics*
- Laird & Ware (1982), *Biometrics*
- Kang et al. (2010), *Nature Genetics*
- Yang et al. (2014), *Nature Genetics*

