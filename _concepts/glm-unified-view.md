# GLM 把线性回归 / 逻辑回归 / 泊松 / 负二项统一成什么框架？

> GLM 统一的是“均值如何由线性预测子决定”。

## 长答案

广义线性模型（generalized linear model, GLM）把三件事拆开：随机分布、线性预测子、链接函数。

第一，响应变量 $Y$ 来自指数族或近似指数族：
$$
p(y\mid\theta,\phi)=\exp\left(\frac{y\theta-b(\theta)}{a(\phi)}+c(y,\phi)\right)
$$

关键性质来自对 log partition function $b(\theta)$ 求导。因为概率和为 1：
$$
\int p(y\mid\theta,\phi)dy=1
$$
对 $\theta$ 求导：
$$
\mathbb{E}\left[\frac{Y-b'(\theta)}{a(\phi)}\right]=0
$$
所以：
$$
\mathbb{E}(Y)=b'(\theta)
$$
再求一次导数得到：
$$
\text{Var}(Y)=a(\phi)b''(\theta)
$$

第二，协变量只通过线性预测子进入：
$$
\eta_i=x_i^\top\beta
$$

第三，链接函数（link function）把均值和线性预测子连接：
$$
g(\mu_i)=\eta_i
$$

于是线性回归是 $Y\sim N(\mu,\sigma^2)$、$g(\mu)=\mu$；逻辑回归是 $Y\sim \text{Bernoulli}(p)$、$g(p)=\log\frac{p}{1-p}$；泊松回归是 $Y\sim \text{Poisson}(\mu)$、$g(\mu)=\log\mu$；RNA-seq NB GLM 是 $Y\sim\text{NegBin}(\mu,\alpha)$、$g(\mu)=\log\mu$。

## 为什么这么设计

GLM 的设计动机是保留线性模型的可解释性，同时让响应变量遵守自己的取值空间。计数不能用普通线性回归直接拟合，因为预测值可能为负；二分类不能用线性回归，因为概率会越界。链接函数把无界的 $x^\top\beta$ 映射到合法均值空间。

为什么不是先 transform 再线性回归？因为 transform 后的误差结构通常变了。例如 $\log(Y+1)$ 让低 count 的伪计数影响很大，也不能自然处理 library size offset。GLM 直接建模原始尺度上的均值和方差。

## ⚠️ 容易混淆 / 常见误解

**误解 1**：GLM 就是“非正态数据的线性回归”。  
为什么是错的：核心不是非正态，而是均值、方差、链接函数三者绑定。

**误解 2**：log link 等于把 $Y$ 取 log。  
为什么是错的：log link 是 $\log\mu=x^\top\beta$，不是 $\log Y=x^\top\beta+\epsilon$。

**误解 3**：负二项不属于 GLM。  
为什么是错的：固定 dispersion 时 NB 可作为 GLM；实际软件还会额外估计 dispersion。

## 横向连接

- [[_concepts/poisson-vs-negative-binomial]]
- [[_concepts/mixed-models-everywhere]]
- [[03-bulk-RNAseq/wald-vs-lrt]]
- [[04-scRNAseq/sctransform-pearson-residual]]
- [[14-microbiome/differential-abundance-tools]]

## 我现在的理解状态

`#待 Peter 确认`

## 参考

- Nelder & Wedderburn (1972), *Journal of the Royal Statistical Society Series A*
- McCullagh & Nelder (1989), *Generalized Linear Models*
- Dobson & Barnett (2018), *An Introduction to Generalized Linear Models*

