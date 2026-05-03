# Zero inflation 真的存在吗？真零 vs 假零如何区分？

> 多出来的零只有超过抽样模型预期时才叫 inflation。

## 长答案

零值有两种来源。真零（true zero）表示目标分子或物种确实不存在；假零（sampling zero/dropout）表示存在但没被采到。Zero inflation 指观测到的零比基准分布预期更多。

以负二项为基准，若 $Y\sim\text{NegBin}(\mu,\alpha)$，常用参数化下：
$$
P(Y=0)=\left(\frac{1}{1+\alpha\mu}\right)^{1/\alpha}
$$
推导来自 NB PMF：
$$
P(Y=y)=\frac{\Gamma(y+1/\alpha)}{\Gamma(1/\alpha)y!}
\left(\frac{1}{1+\alpha\mu}\right)^{1/\alpha}
\left(\frac{\alpha\mu}{1+\alpha\mu}\right)^y
$$
令 $y=0$，最后一项为 1，组合系数也为 1。

零膨胀负二项（zero-inflated negative binomial, ZINB）加入一个结构零过程：
$$
P(Y=0)=\pi+(1-\pi)P_{\text{NB}}(0)
$$
$$
P(Y=y>0)=(1-\pi)P_{\text{NB}}(y)
$$
$\pi$ 是额外零概率。

关键问题是：NB 自身已经能产生很多零，尤其在 $\mu$ 小、dispersion 大时。因此“零很多”不等于 zero inflation。

## 为什么这么设计

ZINB 的设计动机是区分“不可表达/不存在”与“可表达但抽样没捕获”。但如果 NB 已能解释零比例，再加 $\pi$ 会过拟合，把低表达和技术深度差异误拆成 dropout 机制。

真零与假零的区分依赖外部信息：测序深度、spike-in、同一 feature 在相似细胞中的表达、蛋白/原位验证、绝对定量。单靠一个零无法判断。

## ⚠️ 容易混淆 / 常见误解

**误解 1**：scRNA-seq 必须用 ZINB。  
为什么是错的：UMI 数据中很多零可由 NB/Poisson sampling 解释；是否 inflation 要检验。

**误解 2**：真零比假零更“生物学”。  
为什么是错的：假零也可由低捕获率、细胞大小、RNA content 等生物-技术混合因素产生。

**误解 3**：加 zero inflation 总是更保守。  
为什么是错的：多余参数可能吸收真实差异，降低 power，也可能制造不可解释的 latent structure。

## 横向连接

- [[_concepts/poisson-vs-negative-binomial]]
- [[04-scRNAseq/dropout-truth-in-sc]]
- [[04-scRNAseq/why-negative-binomial-in-singlecell]]
- [[13-metabolomics/metabolomics-missing-value]]
- [[14-microbiome/differential-abundance-tools]]

## 我现在的理解状态

`#待 Peter 确认`

## 参考

- Lambert (1992), *Technometrics*
- Pierson & Yau (2015), *Genome Biology*
- Svensson (2020), *Nature Biotechnology*
- Choudhary & Satija (2022), *Genome Biology*

