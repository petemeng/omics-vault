# 组学里什么时候 Bayesian 真的有用而不是炫技？

> 当需要共享信息、表达不确定性或引入先验时。

## 长答案

Bayesian 的核心是把未知量当随机变量：
$$
p(\theta\mid y)=\frac{p(y\mid\theta)p(\theta)}{p(y)}
$$
其中证据项：
$$
p(y)=\int p(y\mid\theta)p(\theta)d\theta
$$
推导只是条件概率：
$$
p(\theta,y)=p(y\mid\theta)p(\theta)=p(\theta\mid y)p(y)
$$
移项即 Bayes theorem。

组学里 Bayesian 真有用的第一类场景是 shrinkage。假设每个基因效应 $\beta_g$ 来自共同先验：
$$
\beta_g\sim N(0,\tau^2),\qquad \hat\beta_g\mid\beta_g\sim N(\beta_g,s_g^2)
$$
后验均值为：
$$
\mathbb{E}(\beta_g\mid\hat\beta_g)=
\frac{\tau^2}{\tau^2+s_g^2}\hat\beta_g
$$
推导来自两个正态密度相乘：后验 precision 是先验 precision 与似然 precision 之和，
$$
\frac{1}{v}=\frac{1}{\tau^2}+\frac{1}{s_g^2},\qquad
\frac{m}{v}=\frac{\hat\beta_g}{s_g^2}
$$
所以 $m=\frac{\tau^2}{\tau^2+s_g^2}\hat\beta_g$。低信息基因 $s_g^2$ 大，shrink 更多。

第二类是 latent variable model，如 scVI、MOFA，把不可观测的 cell state、batch、factor 写入生成模型。第三类是层次模型，如 eQTL、甲基化、蛋白组缺失值中共享方差信息。第四类是需要输出完整不确定性，而不是单个点估计。

## 为什么这么设计

组学特征多、重复少。每个基因单独估计会不稳定；完全 pooled 又抹掉差异。Bayesian hierarchical model 提供 partial pooling：相似问题共享信息，但不强迫完全相同。

什么时候是炫技？当普通 GLM 已经回答问题，而 Bayesian 模型只增加不可诊断的先验、复杂采样和难解释 latent factor。Bayesian 不是更高级的 p 值替代品。

## ⚠️ 容易混淆 / 常见误解

**误解 1**：Bayesian 结果更主观，所以不适合科学。  
为什么是错的：频率学方法也有隐含正则化和模型假设；Bayesian 只是把先验显式化。

**误解 2**：posterior probability 就等于真实概率。  
为什么是错的：它是在模型和先验条件下的条件概率，模型错时后验也错。

**误解 3**：变分推断的 ELBO 高就代表生物解释好。  
为什么是错的：ELBO 是拟合目标，不保证 latent factor 可解释或因果。

## 横向连接

- [[03-bulk-RNAseq/lfc-shrinkage-priors]]
- [[15-multiomics-integration/mofa-variational]]
- [[15-multiomics-integration/scvi-totalvi-multivi]]
- [[09-methylation/beta-binomial-for-methylation]]
- [[02-GWAS/fine-mapping-methods]]

## 我现在的理解状态

`#待 Peter 确认`

## 参考

- Efron & Morris (1973), *Journal of the American Statistical Association*
- Stephens (2016), *Biostatistics*
- Lopez et al. (2018), *Nature Methods*
- Argelaguet et al. (2020), *Genome Biology*

