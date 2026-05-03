# 为什么组分数据（compositional data）会让标准统计失效？

> 总和被固定后，变量会凭空产生负相关。

## 长答案

组分数据（compositional data）只观察相对比例：
$$
x_i=\frac{a_i}{\sum_{k=1}^D a_k},\qquad \sum_{i=1}^D x_i=1
$$
真实绝对丰度 $a_i$ 经过 closure operation 后落在 simplex 上。问题是：标准相关和差异分析默认变量在欧氏空间自由变化，但组分数据的总和约束让一个分量增加必然压低其他分量。

最小例子：真实绝对丰度 $A=100,B=100,C=100$。若只让 $A$ 翻倍，变成 $A=200,B=100,C=100$，相对丰度从：
$$
(1/3,1/3,1/3)
$$
变成：
$$
(1/2,1/4,1/4)
$$
标准分析会说 $B,C$ 都下降了，但它们的绝对丰度没有变。

Aitchison 的解法是用 log-ratio，因为组分中可解释的信息是比例之间的比值。CLR（centered log-ratio）：
$$
\text{clr}(x_i)=\log\frac{x_i}{g(x)},\qquad g(x)=\left(\prod_{k=1}^D x_k\right)^{1/D}
$$
推导动机是尺度不变性：若绝对丰度整体乘以 $c$，$a_i'=ca_i$，则 $x_i'=x_i$，可识别信息只能来自 $a_i/a_j$。log-ratio：
$$
\log\frac{a_i}{a_j}=\log\frac{x_i}{x_j}
$$
不受 closure 影响。

## 为什么这么设计

微生物组、代谢物相对峰面积、single-cell cell-type fraction 都有 compositional 结构。log-ratio 方法不是数学洁癖，而是避免把“别的东西变了”误判成“这个东西变了”。

为什么不直接 rarefy 或总量归一化？rarefy 丢信息，总量归一化没有解除总和约束；它们不能恢复绝对丰度。

## ⚠️ 容易混淆 / 常见误解

**误解 1**：相对丰度下降说明绝对丰度下降。  
为什么是错的：其他组分上升也会让它相对下降。

**误解 2**：CLR 后就万事大吉。  
为什么是错的：零值仍需处理；不同 pseudocount 会影响低丰度特征。

**误解 3**：组分问题只存在于微生物组。  
为什么是错的：任何 fixed-sum 或 depth-normalized feature 都可能有这个问题。

## 横向连接

- [[14-microbiome/compositional-transforms]]
- [[14-microbiome/differential-abundance-tools]]
- [[03-bulk-RNAseq/composition-bias-example]]
- [[04-scRNAseq/pseudoreplication-pseudobulk]]
- [[13-metabolomics/metabolomics-missing-value]]

## 我现在的理解状态

`#待 Peter 确认`

## 参考

- Aitchison (1982), *Journal of the Royal Statistical Society B*
- Aitchison (1986), *The Statistical Analysis of Compositional Data*
- Gloor et al. (2017), *Frontiers in Microbiology*
- Quinn et al. (2018), *GigaScience*

