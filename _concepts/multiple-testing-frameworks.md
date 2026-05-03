# 多重检验：Bonferroni / BH / Storey q / IHW 各自假设和取舍？

> 校正目标不同：控制任一假阳性，还是控制假发现比例。

## 长答案

做 $m$ 个检验时，若每个原假设下 $p<\alpha$ 的概率是 $\alpha$，则至少一个假阳性的概率为：
$$
P(V\ge1)=1-P(V=0)=1-(1-\alpha)^m
$$
当 $m=20000,\alpha=0.05$ 时几乎必然有假阳性。

Bonferroni 控制 family-wise error rate（FWER）：
$$
P(V\ge1)\le \sum_{i=1}^m P(p_i\le \alpha/m)=m\cdot\alpha/m=\alpha
$$
推导用 union bound，不要求独立，所以保守。

BH（Benjamini-Hochberg）控制 false discovery rate（FDR）：
$$
FDR=\mathbb{E}\left[\frac{V}{\max(R,1)}\right]
$$
把 p 值排序 $p_{(1)}\le\dots\le p_{(m)}$，找最大 $k$：
$$
p_{(k)}\le \frac{k}{m}q
$$
拒绝前 $k$ 个。直觉是：如果全是 null，期望有 $m\cdot p_{(k)}$ 个假阳性；令它不超过 $kq$，即假发现比例不超过 $q$。

Storey q-value 估计真 null 比例 $\pi_0$，把 $m$ 替换成 $\pi_0m$，提高 power。IHW（independent hypothesis weighting）利用与 null p 值独立的协变量给检验加权，例如 RNA-seq 中 baseMean 高的基因 power 更高。

## 为什么这么设计

Bonferroni 适合“一个假阳性都很贵”的场景；BH 适合组学发现，因为我们接受候选列表中有少量假阳性。Storey 和 IHW 进一步承认：不是每个检验的先验 null 比例和 power 都一样。

为什么不直接按 p<0.05？因为组学的检验数量让单检验错误率失去意义。

## ⚠️ 容易混淆 / 常见误解

**误解 1**：FDR 5% 表示每个基因 5% 概率是假阳性。  
为什么是错的：FDR 是发现集合层面的期望比例，不是单个基因后验概率。

**误解 2**：Bonferroni 比 BH 更“正确”。  
为什么是错的：二者控制目标不同；保守不是自动更科学。

**误解 3**：IHW 是作弊，因为用了额外信息。  
为什么是错的：只要权重协变量在 null 下与 p 值独立，FDR 仍可控制。

## 横向连接

- [[03-bulk-RNAseq/independent-filtering-not-cheating]]
- [[02-GWAS/gwas-power-derivation]]
- [[08-ATAC/differential-accessibility]]
- [[09-methylation/dmr-callers-compared]]
- [[12-proteomics/target-decoy-fdr]]

## 我现在的理解状态

`#待 Peter 确认`

## 参考

- Bonferroni (1936), *Pubblicazioni del R Istituto Superiore*
- Benjamini & Hochberg (1995), *Journal of the Royal Statistical Society B*
- Storey (2002), *Journal of the Royal Statistical Society B*
- Ignatiadis et al. (2016), *Nature Methods*

