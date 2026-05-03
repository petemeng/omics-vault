# 为什么计数数据普遍用负二项而不是泊松？

> 泊松只允许均值等于方差，组学重复通常过离散。

## 长答案

泊松分布（Poisson）描述一个固定强度的独立计数过程：
$$
Y \sim \text{Poisson}(\lambda), \qquad \mathbb{E}(Y)=\lambda,\quad \text{Var}(Y)=\lambda
$$

这个 $\text{Var}(Y)=\mathbb{E}(Y)$ 是它最硬的承诺。测序 sampling noise 如果是唯一来源，泊松很合理；但组学的生物重复不是同一个 $\lambda$ 被重复观测，而是每个样本都有自己的真实强度。

把样本间真实强度写成隐变量：
$$
Y\mid \lambda \sim \text{Poisson}(\lambda), \qquad \lambda \sim \text{Gamma}(r,\theta)
$$

用全期望公式：
$$
\mathbb{E}(Y)=\mathbb{E}_\lambda[\mathbb{E}(Y\mid\lambda)]=\mathbb{E}(\lambda)=r\theta=\mu
$$

用全方差公式：
$$
\text{Var}(Y)=\mathbb{E}[\text{Var}(Y\mid\lambda)]+\text{Var}[\mathbb{E}(Y\mid\lambda)]
=\mathbb{E}(\lambda)+\text{Var}(\lambda)
=r\theta+r\theta^2
$$

令 $\mu=r\theta$，$\alpha=1/r$，则 $\theta=\alpha\mu$，所以：
$$
\text{Var}(Y)=\mu+\alpha\mu^2
$$

这就是负二项分布（negative binomial, NB）在 RNA-seq、ATAC peak count、微生物丰度等计数数据中反复出现的原因：它不是“更复杂的泊松”，而是“泊松采样 + 样本间强度波动”的边缘分布。

## 为什么这么设计

负二项把两个噪声源分开：泊松层处理 reads sampling，Gamma 层处理生物重复之间的真实差异。直接加一个常数方差不够，因为高丰度特征的样本间波动通常随 $\mu^2$ 放大。硬用泊松会低估标准误，尤其把高 count feature 判成假阳性。

## ⚠️ 容易混淆 / 常见误解

**误解 1**：测序深度足够高就能用泊松。  
为什么是错的：深度只降低采样噪声，不消除生物重复间的 $\lambda$ 波动。

**误解 2**：负二项主要用来处理离群值。  
为什么是错的：NB 处理总体 mean-variance 关系；离群值需要 robust 诊断或 Cook's distance。

**误解 3**：dispersion 越小数据越好。  
为什么是错的：dispersion 反映真实异质性，异常小可能说明把技术重复当成了生物重复。

## 横向连接

- [[_concepts/glm-unified-view]]
- [[_concepts/zero-inflation-vs-true-zero]]
- [[03-bulk-RNAseq/why-negative-binomial-not-poisson]]
- [[04-scRNAseq/why-negative-binomial-in-singlecell]]
- [[09-methylation/beta-binomial-for-methylation]]

## 我现在的理解状态

`#待 Peter 确认`

## 参考

- Greenwood & Yule (1920), *Journal of the Royal Statistical Society*
- Robinson et al. (2010), *Bioinformatics*
- Anders & Huber (2010), *Genome Biology*
- Love et al. (2014), *Genome Biology*

