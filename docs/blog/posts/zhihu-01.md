# 浅谈指数族

> 发布于 2023-02-26

本文参考了 *Generating Functionology* 第 3 章的内容。

## 0. 引入

某天，有人（不是我）问了如下问题（不用考虑任何置换）：

- 如何求第一类、第二类斯特林数的生成函数？
- 如何求大小为 $n$ 的连通标号图的生成函数？
- 如何求大小为 $n$ 的二分图数量的生成函数？

学习指数族（exponential family）可以统一处理这些问题。

## 1. 一些定义

一个 **Card** $C(S,p)$ 是一个二元组：它包含一个有限集 $S\subset\mathbb{N}_+$，以及一个描述 $S$ 的图片（包括图）。它的权值为 $|S|$。当 $S=[n]$ 时，称这个 Card 是标准的。

一个 **Hand** 是一些 Card 的集合。对于给定的 $n$，它们满足：

$$
\sum_i |S_i|=n,\qquad \bigcup_i S_i=[n].
$$

一个 **Deck** 是若干个权值相同的标准 Card 的集合。记 $d_i=|D_i|$，并令 $D(x)$ 表示集合 $\{d_i\}$ 的指数生成函数。一个指数族 $\mathcal{F}$ 包含一列 Deck：

$$
\mathcal{F}=(D_1,D_2,\dots).
$$

记 $h(n,k)$ 为权值为 $n$、且恰好包含 $k$ 个 Card 的 Hand 的数量，令

$$
\mathcal{H}(x,y)=\sum_{n,k\ge 0}h(n,k)\frac{x^n}{n!}y^k.
$$

## 2. 一些性质

指数公式给出：

$$
\mathcal{H}(x,y)=\exp\{yD(x)\}.
$$

为了证明它，先介绍标号计数的基本引理。设 $\mathcal{F}'$ 和 $\mathcal{F}''$ 是两个 Card 互不相同的指数族，令 $\mathcal{F}=\mathcal{F}'\oplus\mathcal{F}''$。则

$$
\mathcal{H}(x,y)=\mathcal{H}'(x,y)\mathcal{H}''(x,y).
$$

事实上，若 $h'(n_1,k_1)$ 和 $h''(n-n_1,k-k_1)$ 分别表示两类 Hand 的数量，则

$$
h(n,k)=\sum_{n_1,k_1\ge0}\binom{n}{n_1}h'(n_1,k_1)h''(n-n_1,k-k_1).
$$

这正对应于生成函数的乘法。

接下来考虑只有一个 $D_i$ 非零的情况。此时 $h(n,k)$ 只可能在 $n=ik$ 时非零。由于所有 Card 都从 $D_i$ 中选择，需要除以 $k!$，因此

$$
h(ik,k)=d_i^k\frac{(ik)!}{(i!)^k}\frac{1}{k!}.
$$

于是

$$
\begin{aligned}
\mathcal{H}_i(x,y)
&=\sum_k h(ik,k)\frac{x^{ik}}{(ik)!}y^k\\
&=\sum_k\frac{d_i^k x^{ik}y^k}{k!(i!)^k}\\
&=\exp\left\{\frac{d_i x^i y}{i!}\right\}.
\end{aligned}
$$

将不同的 $D_i$ 合并，得到

$$
\begin{aligned}
\mathcal{H}(x,y)
&=\prod_{i\ge1}\mathcal{H}_i(x,y)\\
&=\exp\left\{y\sum_{i\ge1}\frac{d_i x^i}{i!}\right\}\\
&=\exp\{yD(x)\}.
\end{aligned}
$$

## 3. 应用

### 第一类斯特林数

大小为 $i$ 的圆排列有 $d_i=(i-1)!$ 个，因此

$$
D(x)=\sum_{i\ge1}\frac{x^i}{i}=\log\frac{1}{1-x}.
$$

从而

$$
\mathcal{H}(x,y)=e^{yD(x)}=\frac{1}{(1-x)^y}.
$$

### 第二类斯特林数

大小为 $i$ 的子集只有一个，因此 $D(x)=e^x-1$，从而

$$
\mathcal{H}(x,y)=e^{y(e^x-1)}.
$$

特别地，

$$
\mathcal{H}(x,1)=e^{e^x-1}
$$

是贝尔数的指数生成函数。

### 连通图个数

如果一个 Hand 表示一个图，那么一个 Deck 就表示一个连通图。显然

$$
\mathcal{H}(x,1)=\sum_{n\ge0}2^{\binom{n}{2}}\frac{x^n}{n!}.
$$

因此，连通图的生成函数满足 $D(x)=\log\mathcal{H}(x,1)$。

### 二分图数量

先考虑黑白两色可以区分的情况。此时

$$
h_n=\sum_{k\ge0}\binom{n}{k}2^{k(n-k)}.
$$

若记相应的生成函数为 $\mathcal{H}_0(x)$，则 $D(x)=\log\mathcal{H}_0(x)$。不考虑颜色时，颜色交换会产生二阶对称性，因此

$$
\mathcal{H}(x)=\exp\left\{\frac{D(x)}{2}\right\}
=\sqrt{\mathcal{H}_0(x)}.
$$

思考：如何计算每个点的度数都为 $2$ 的图的个数？

本文使用 Zhihu On VSCode 创作并发布。

