# 批次效应有几种来源？校正手段如何对应？

> 批次不是一种问题，而是一组非目标系统差异。

## 长答案

批次效应（batch effect）可以写成一个最小模型：
$$
y_{ij}=\mu+\beta x_i+\gamma b_i+\epsilon_{ij}
$$
$x_i$ 是目标生物因素，$b_i$ 是批次因素。危险发生在 $x$ 与 $b$ 相关时。若完全混杂，例如所有 treatment 都在 batch 1，所有 control 都在 batch 2，则设计矩阵 $[x,b]$ 的两列线性相关，$\beta$ 与 $\gamma$ 不可辨识。

数学上，如果 $b=x$，模型变成：
$$
y_i=\mu+(\beta+\gamma)x_i+\epsilon_i
$$
数据只能估计 $\beta+\gamma$，不能分开估计 $\beta$ 与 $\gamma$。这不是算法不够强，而是信息论上没有足够信息。

批次来源至少有四类：样本来源批次（采样中心、时间、组织缺血）、实验批次（提取、建库、上机 lane）、测量批次（仪器漂移、试剂 lot）、计算批次（参考版本、流程参数）。对应手段也不同：设计阶段用 randomization/blocking；建模阶段加入 covariate 或 random effect；矩阵阶段用 ComBat、removeBatchEffect、Harmony 等；质控阶段剔除不可解释异常。

## 为什么这么设计

最好的批次处理是设计，而不是校正。随机化让 $x$ 与 $b$ 近似独立；blocking 让每个 batch 都包含所有条件。后期校正只适合“批次与条件未完全混杂”的情况。

为什么不用一个通用算法清洗？因为不同批次形态不同。加性 location shift 可用线性模型；均值-方差同时变可用 empirical Bayes；scRNA 的细胞组成差异会被整合算法误删，不能当普通 batch。

## ⚠️ 容易混淆 / 常见误解

**误解 1**：PCA 上 batch 分开，校正后混在一起就成功。  
为什么是错的：如果真实生物差异也被抹掉，图好看但结论坏了。

**误解 2**：batch correction 应该在差异分析前默认做。  
为什么是错的：计数模型更适合把 batch 放进 design，而不是先改 counts。

**误解 3**：完全混杂可以用 ComBat 救。  
为什么是错的：完全混杂时目标效应与批次效应不可辨识。

## 横向连接

- [[_concepts/mixed-models-everywhere]]
- [[_concepts/pca-svd-the-same-thing]]
- [[00-foundations/experimental-design-fundamentals]]
- [[03-bulk-RNAseq/pc1-batch-rescue]]
- [[15-multiomics-integration/cross-omics-batch]]

## 我现在的理解状态

`#待 Peter 确认`

## 参考

- Johnson et al. (2007), *Biostatistics*
- Leek et al. (2010), *Nature Reviews Genetics*
- Risso et al. (2014), *Nature Biotechnology*
- Haghverdi et al. (2018), *Nature Biotechnology*

