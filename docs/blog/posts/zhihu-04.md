# 罗素公理系统的几个见解

> 发布于 2026-01-05 11:26（北京），编辑于 2026-01-05 11:27（北京）

（PS：本篇除了作为复习离散数学考试之外，没有任何意义，只是在重复造轮子罢了。）

在《数学原理》（*Principia Mathematica*）的公理体系中，看似直观的代数性质往往需要极高成本的句法构造。本文展示如何在该系统中构造两个非平凡命题的证明：析取结合律与分配律，并尝试总结使用罗素公理系统时的一些规律。

## 1. 预备知识：公理与基础工具

原始符号仅限于 $\neg$（非）与 $\vee$（析取）。定义蕴含：

$$
P \to Q \overset{\mathrm{def}}{=} \neg P \vee Q.
$$

定义合取：

$$
P \wedge Q \overset{\mathrm{def}}{=} \neg(\neg P \vee \neg Q).
$$

公理组如下：

- **Ax. 1：** $\vdash (P \vee P) \to P$。
- **Ax. 2：** $\vdash Q \to (P \vee Q)$。
- **Ax. 3：** $\vdash (P \vee Q) \to (Q \vee P)$。
- **Ax. 4：** $\vdash (Q \to R) \to ((P \vee Q) \to (P \vee R))$。

推理规则只有一条：

- **MP：** 若 $\vdash P$ 且 $\vdash P \to Q$，则 $\vdash Q$。

为避免重复造轮子，下面假设两个基础定理已经证毕：

- **Th. 1（传递律）：**

  $$
  \vdash (Q \to R) \to ((P \to Q) \to (P \to R)).
  $$

- **Th. 2（逆否律）：**

  $$
  \vdash (P \to Q) \to (\neg Q \to \neg P).
  $$

## 2. 命题一：析取结合律

目标命题是：

$$
\vdash P \vee (Q \vee R) \to (P \vee Q) \vee R.
$$

困难在于括号层级的“左移”。在只有公理 4 的情况下，不能直接移动括号，因此我们分别证明 $P$ 与 $Q \vee R$ 都能推出目标，再把两个结论合并起来。

### 2.1 构造引理 A

利用 Ax. 2，可以逐步扩大析取范围：

$$
\vdash P \to (P \vee Q),
$$

$$
\vdash (P \vee Q) \to ((P \vee Q) \vee R).
$$

由传递律得到引理 A：

$$
\vdash P \to ((P \vee Q) \vee R).
$$

### 2.2 构造引理 B

接下来证明右侧部分 $Q \vee R$ 可以推出同一个目标。由交换律与 Ax. 2，可得：

$$
\vdash Q \to (P \vee Q).
$$

在两边析取添加 $R$，并使用 MP：

$$
\vdash (R \vee Q) \to (R \vee (P \vee Q)).
$$

再利用 Ax. 3 两次交换析取项：

$$
\vdash (Q \vee R) \to (R \vee Q),
$$

$$
\vdash (R \vee (P \vee Q)) \to ((P \vee Q) \vee R).
$$

连续使用传递律，得到引理 B：

$$
\vdash (Q \vee R) \to ((P \vee Q) \vee R).
$$

### 2.3 综合与消去

记

$$
S=Q \vee R,\qquad T=(P \vee Q) \vee R.
$$

引理 B 给出 $S\to T$。由 Ax. 4 将其扩展到 $P\vee S$：

$$
\vdash (S \to T) \to ((P \vee S) \to (P \vee T)).
$$

因此有

$$
\vdash (P \vee (Q \vee R)) \to (P \vee T).
$$

剩下的工作是消去右侧多余的 $P$。由引理 A、Ax. 4、Ax. 3 和 Ax. 1，依次得到：

$$
\vdash (P \to T) \to ((T \vee P) \to (T \vee T)),
$$

$$
\vdash (P \vee T) \to (T \vee P),\qquad
\vdash (T \vee T) \to T.
$$

再次使用传递律，得到 $\vdash(P\vee T)\to T$。与前面的结论连接，便得到：

$$
\boxed{\vdash P \vee (Q \vee R) \to (P \vee Q) \vee R}.
$$

证毕。

## 3. 命题二：分配律（半边）

结合律的困难在于结构调整，分配律的困难在于定义展开与逆否变换。下面证明一个方向：

$$
\vdash P \vee (Q \wedge R) \to (P \vee Q) \wedge (P \vee R).
$$

根据合取的定义，这个命题等价于：

$$
\vdash P \vee \neg(\neg Q \vee \neg R)
\to \neg(\neg(P \vee Q) \vee \neg(P \vee R)).
$$

### 3.1 策略分析

令 $A=P\vee(Q\wedge R)$、$B=P\vee Q$、$C=P\vee R$。要证明 $A\to B\wedge C$，只需分别证明 $A\to B$ 与 $A\to C$，再使用合取引入引理。

### 3.2 子命题证明

先证明 $A\to B$。展开 $Q\wedge R$ 后，只需证明：

$$
\neg(\neg Q\vee\neg R)\to Q.
$$

由 Ax. 2 有

$$
\vdash \neg Q\to(\neg Q\vee\neg R).
$$

使用逆否律和双重否定消去，可得

$$
\neg(\neg Q\vee\neg R)\to Q.
$$

再由 Ax. 4 将 $P$ 加到析取式左侧，得到

$$
\vdash (P\vee(Q\wedge R))\to(P\vee Q).
$$

交换 $Q$ 与 $R$ 后可以完全类似地证明第二个子命题：

$$
\vdash (P\vee(Q\wedge R))\to(P\vee R).
$$

### 3.3 合并

现在已经有

$$
A\to B,\qquad A\to C.
$$

由逆否律，这两个结论分别给出 $\neg B\to\neg A$ 与 $\neg C\to\neg A$。将它们合并，得到

$$
\neg B\vee\neg C\to\neg A.
$$

再次使用逆否律并消去双重否定，即得

$$
A\to\neg(\neg B\vee\neg C),
$$

也就是

$$
\boxed{\vdash (P\vee(Q\wedge R))\to((P\vee Q)\wedge(P\vee R))}.
$$

证毕。

## 4. 规律

这两个证明可以总结出几条经验：

1. 对于 $A\vee B\to C$ 形式的命题，可以把前件拆成两个子命题，分别证明后再合并。
2. 对于 $A\to B\wedge C$ 形式的命题，可以把后件拆开，分别证明 $A\to B$ 和 $A\to C$。
3. 多使用逆否命题的变换，并尝试从结论出发逆向寻找需要证明的中间命题。
4. 如果已知 $A$、$B$，想证明 $A\wedge B$，直接处理可能需要先使用结合律。可以引入一个真命题 $W$，把 $A$ 与 $B$ 分别改写为 $A\to A\vee\neg W$ 和 $B\to B\vee\neg W$，再转化为前面已经处理过的形式。

