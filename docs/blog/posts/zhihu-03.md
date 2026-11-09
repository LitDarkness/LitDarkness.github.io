# 区间长度 4 与整系数多项式的根分布的限制问题

> 发布于 2025-12-16 17:29（北京），编辑于 2025-12-16 21:29（北京）

我们将证明如下命题：对于任意给定的实数区间 $I$，如果 $|I|<4$，则只有有限个不可约、首一的整系数多项式，其所有根都完全落在区间 $I$ 内。这个结论通常被认为是 Fekete 定理的一个特例。

## 1. 预备知识

### 1.1 切比雪夫多项式

第一类切比雪夫多项式 $T_n(x)$ 由递推关系定义：

$$
T_0(x)=1,\qquad T_1(x)=x,\qquad
T_{n+1}(x)=2xT_n(x)-T_{n-1}(x).
$$

也可以通过三角函数定义：

$$
T_n(x)=\cos(n\arccos x).
$$

切比雪夫多项式在这个证明中至关重要的性质有两个：

1. 在区间 $[-1,1]$ 上有界：
   $\max_{x\in[-1,1]}|T_n(x)|=1$
2. 当 $n\ge1$ 时，$T_n(x)$ 的最高次项系数是 $2^{n-1}$。若定义首一多项式
   $\widetilde T_n(x)=2^{-(n-1)}T_n(x)$
   那么在所有 $n$ 次首一多项式中，$\widetilde T_n$ 在 $[-1,1]$ 上的最大绝对值是最小的，为 $2^{-(n-1)}$。

### 1.2 结式

设有两个单变量多项式

$$
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,\qquad a_n\ne0,
$$

$$
g(x)=b_mx^m+b_{m-1}x^{m-1}+\cdots+b_1x+b_0,\qquad b_m\ne0.
$$

Sylvester 矩阵 $\operatorname{Syl}(f,g)$ 是一个 $(n+m)\times(n+m)$ 的矩阵。它的前 $m$ 行由 $f(x)$ 的系数组成，每次向右移动一位；后 $n$ 行由 $g(x)$ 的系数组成，每次向右移动一位：

$$
\operatorname{Syl}(f,g)=
\begin{pmatrix}
a_n&a_{n-1}&\cdots&a_0&0&\cdots&0\\
0&a_n&a_{n-1}&\cdots&a_0&\cdots&0\\
\vdots&\vdots&\ddots&\ddots&\ddots&\ddots&\vdots\\
0&\cdots&0&a_n&a_{n-1}&\cdots&a_0\\
b_m&b_{m-1}&\cdots&b_0&0&\cdots&0\\
0&b_m&b_{m-1}&\cdots&b_0&\cdots&0\\
\vdots&\vdots&\ddots&\ddots&\ddots&\ddots&\vdots\\
0&\cdots&0&b_m&b_{m-1}&\cdots&b_0
\end{pmatrix}.
$$

Sylvester 行列式通常被称为这两个多项式的结式，记为 $\operatorname{Res}(f,g)$：

$$
\operatorname{Res}(f,g)=\det\operatorname{Syl}(f,g).
$$

若 $f$ 的根为 $\alpha_1,\dots,\alpha_n$，则

$$
\operatorname{Res}(f,g)=a_n^m\prod_{i=1}^n g(\alpha_i).
$$

此外，结式和多项式的判别式 $\Delta(f)$ 满足：

$$
a_n^{2n-2}\prod_{i<j}(\alpha_i-\alpha_j)^2
=\Delta(f)
=\frac{(-1)^{n(n-1)/2}}{a_n}\operatorname{Res}(f,f').
$$

### 1.3 Hadamard 不等式

假设 $A=(a_{ij})$ 是实数矩阵。Hadamard 不等式指出，行列式的绝对值小于等于各列向量欧几里得范数的乘积：

$$
|\det(A)|\le\prod_{j=1}^n\|C_j\|_2.
$$

其中 $C_j$ 是矩阵的第 $j$ 列向量：

$$
C_j=(a_{1j},a_{2j},\dots,a_{nj})^{\mathsf T}.
$$

### 1.4 Minkowski 定理及其线性形式

Minkowski 第一定理（齐次形式）表述如下：对于 $\mathbb{R}^n$ 中的中心对称凸体 $K$，若

$$
\operatorname{Vol}(K)>2^n\det(\Lambda),
$$

则 $K$ 中存在非零格点。

## 2. 论证思路与初步结论

不妨设 $I=[a,b]$，并记 $|I|=b-a<4$。一方面，$\operatorname{Res}(f,g)$ 是整数；另一方面，如果 $f$ 是首一的整系数不可约多项式，那么

$$
\operatorname{Res}(f,g)=\prod_{i=1}^n g(\alpha_i).
$$

如果我们能选取一个整系数多项式 $g$，使得

$$
\max_{x\in I}|g(x)|<1,
$$

并且通常情况下 $f$ 与 $g$ 没有公共根，那么 $\operatorname{Res}(f,g)$ 就是一个绝对值小于 $1$ 的非零整数，矛盾。或者，如果能够对 $\operatorname{Res}(f,f')$ 做类似估计，也能完成证明。

为了方便下面的论证，先证明：满足 $\deg f<N$，并且所有根都为实数且落在 $I$ 中的多项式只有有限个。事实上，所有根的取值都在 $I$ 中，由韦达定理可知系数都落在一个有界集合中；又由于 $f$ 是整系数多项式，所以满足条件的多项式只有有限个。

## 3. 方法一：估计范德蒙德行列式

定义区间 $I$ 上的 $n$ 阶最大范德蒙德值：

$$
V_n^{\max}(I)
=\max_{x_1,\dots,x_n\in I}\prod_{i<j}|x_i-x_j|.
$$

记范德蒙德行列式为

$$
V_n(x_1,\dots,x_n)=
\begin{vmatrix}
1&x_1&x_1^2&\cdots&x_1^{n-1}\\
1&x_2&x_2^2&\cdots&x_2^{n-1}\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&x_n&x_n^2&\cdots&x_n^{n-1}
\end{vmatrix}.
$$

我们要证明：

$$
\limsup_{n\to\infty}
\left(V_n^{\max}(I)\right)^{\frac{2}{n(n-1)}}
\le\frac{b-a}{4}.
$$

令

$$
x_i=\frac{b-a}{2}t_i+\frac{a+b}{2},
$$

把 $I$ 映射到 $[-1,1]$。于是

$$
V_n(x)=\left(\frac{b-a}{2}\right)^{\binom{n}{2}}V_n(t).
$$

因此只需证明在 $[-1,1]$ 上，相应的极限上界为 $1/2$。

由于范德蒙德行列式的值在列变换下只差一个固定的行列式因子，我们可以用首一的归一化切比雪夫多项式基底

$$
P_0(t)=1,\qquad P_k(t)=2^{-(k-1)}T_k(t)\quad(k\ge1)
$$

替换基底 $\{1,t,\dots,t^{n-1}\}$。根据切比雪夫多项式的性质，对于所有 $t\in[-1,1]$，

$$
|P_k(t)|\le2^{-(k-1)}.
$$

构造矩阵 $A=(P_{j-1}(t_i))$，则 $|V_n(t)|$ 与 $|\det A|$ 相等。利用 Hadamard 不等式，第 $j$ 列（对应 $k=j-1$）的模长满足

$$
\sqrt{\sum_{i=1}^n|P_k(t_i)|^2}
\le\sqrt n\,2^{-(j-2)}
\qquad(j\ge2).
$$

对于 $j=1$，由于 $P_0=1$，对应的列向量模长为 $\sqrt n$。因此

$$
|V_n(t)|
\le n^{n/2}\prod_{k=1}^{n-1}2^{-(k-1)}
=n^{n/2}2^{-\frac{(n-1)(n-2)}{2}}.
$$

从而

$$
\limsup_{n\to\infty}|V_n(t)|^{\frac{2}{n(n-1)}}
\le\lim_{n\to\infty}
\left(
n^{\frac{1}{n-1}}
2^{-\frac{(n-1)(n-2)}{n(n-1)}}
\right)
=\frac12.
$$

回到原来的极限表达式，得到

$$
\limsup_{n\to\infty}
\left(V_n^{\max}(I)\right)^{\frac{2}{n(n-1)}}
\le\frac{b-a}{4}<1.
$$

因此，对于充分大的 $n$，由判别式公式可以得到

$$
0\le\Delta(f)
=a_n^{2n-2}\prod_{i<j}(\alpha_i-\alpha_j)^2<1.
$$

但 $\Delta(f)$ 可以写成一个元素全为整数的行列式，所以 $\Delta(f)\in\mathbb{Z}$。又因为 $f$ 不可约，故 $f$ 没有重根，从而 $\Delta(f)\ne0$，矛盾。结合次数小于 $n$ 的多项式只有有限个，命题得证。

## 4. 方法二：构造辅助多项式

我们将证明如下引理：

> **引理：** 若 $|I|<4$，则对于充分大的度数 $d$，存在非零整系数多项式 $Q(x)$，使得它在 $I$ 上的绝对值恒小于 $1$。

一旦证明了该引理，设 $f(x)$ 为任意满足条件的不可约多项式。若 $\deg f$ 足够大（大于 $Q$ 的度数），则 $f$ 与 $Q$ 互质。考虑它们的结式：

$$
|\operatorname{Res}(f,Q)|
=\left|\prod_{i=1}^nQ(\alpha_i)\right|.
$$

由于 $\alpha_i\in I$，且在 $I$ 上 $|Q(x)|<1$，故乘积的绝对值小于 $1$。但 $\operatorname{Res}(f,Q)$ 是整系数多项式的结式，必为整数；非零整数的绝对值不可能小于 $1$，于是得到矛盾。这说明 $f$ 的次数不能任意大。

下面证明这个引理。

### 4.1 构造凸体

考虑 $\mathbb{R}^{d+1}$，坐标对应多项式

$$
Q(x)=a_dx^d+\cdots+a_0
$$

的系数。定义集合

$$
S_{\lambda,I}
=\left\{
(a_d,\dots,a_0)\in\mathbb{R}^{d+1}
\;\middle|\;
\forall x\in I,\ |Q(x)|\le\lambda
\right\}.
$$

这是一个中心对称凸体。我们需要证明：当 $\lambda\in(0,1)$ 时，对于充分大的 $d$，这个集合包含非零整数点。根据 Minkowski 定理，只需证明

$$
\operatorname{Vol}(S_{\lambda,I})>2^{d+1}.
$$

### 4.2 体积估计

为了计算体积，建立一个从多项式系数空间到函数值空间的线性映射。先将区间 $I=[a,b]$ 仿射变换到 $[-1,1]$：

$$
x=\frac{b-a}{2}t+\frac{a+b}{2}.
$$

定义线性映射

$$
\varphi:\mathbb{R}^{d+1}\to\mathbb{R}^{d+1},
\qquad
Q(x)\longmapsto
\frac{1}{\lambda}
Q\left(\frac{b-a}{2}t+\frac{a+b}{2}\right).
$$

映射 $\varphi$ 的行列式包含两部分：

1. 系数缩放 $1/\lambda$ 在 $d+1$ 维空间贡献 $(1/\lambda)^{d+1}$。
2. 变量代换 $x\mapsto t$ 从 $x^k$ 到 $t^k$ 产生 $\left(\frac{b-a}{2}\right)^k$ 的因子。

因此

$$
|\det\varphi|
=\lambda^{-(d+1)}
\left(\frac{b-a}{2}\right)^{\frac{d(d+1)}{2}}.
$$

体积关系为

$$
\operatorname{Vol}(S_{\lambda,I})
=\lambda^{d+1}
\left(\frac{2}{b-a}\right)^{\frac{d(d+1)}{2}}
\operatorname{Vol}(S_{1,[-1,1]}).
$$

为了估计 $\operatorname{Vol}(S_{1,[-1,1]})$，考虑切比雪夫多项式基底 $\{T_0,\dots,T_d\}$。由于 $|T_k(t)|\le1$，由这些多项式作为基底张成的交叉多胞形完全包含在 $S_{1,[-1,1]}$ 内，从而得到：

$$
\operatorname{Vol}(S_{1,[-1,1]})
\ge
\frac{2^{d+1}}{(d+1)!}\,2^{\frac{d(d-1)}{2}}.
$$

代入之前的计算结果：

$$
\operatorname{Vol}(S_{\lambda,I})
\ge
\lambda^{d+1}
\left(\frac{2}{b-a}\right)^{\frac{d(d+1)}{2}}
\frac{2^{d+1}}{(d+1)!}\,2^{\frac{d(d-1)}{2}}.
$$

整理后：

$$
\operatorname{Vol}(S_{\lambda,I})
\ge
\lambda^{d+1}\cdot2^{d+1}\cdot
\frac{1}{(d+1)!}\cdot
\frac{2^{d^2}}{(b-a)^{\frac{d(d+1)}{2}}}.
$$

由于 $b-a<4$，通过对数估计可以证明，当 $d\to\infty$ 时，

$$
\lim_{d\to\infty}
\frac{\operatorname{Vol}(S_{\lambda,I})}{2^{d+1}}
=+\infty.
$$

因此，对于充分大的 $d$，满足 Minkowski 定理的使用条件，引理得证。

## 5. 总结

无论是通过直接估计判别式（方法一），还是利用几何数论构造辅助多项式（方法二），证明的核心都归结于区间长度与 $4$ 的比较。事实上，可以证明 $4$ 是最优常数，并且它与数学中的一些其他深刻理论有关。


