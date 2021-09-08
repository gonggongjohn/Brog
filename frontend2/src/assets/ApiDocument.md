# 第五章 矩阵计算问题

在众多科学与工程学科，如物理、化学工程、统计学、经济学、生物学、信号处理、自动控 制、系统理论、医学和军事工程等中，许多问题都可用数学建模成矩阵方程 $\textbf{Ax} = \textbf{b}$. 根据数据向量 $\textbf{b} \in \mathbb{R}^{m \times 1}$ 和数据矩阵 $A \in \mathbb{R}^{m \times n}$ 的不同，矩阵方程主要有以下三种类型:

**(1) 适定方程组：**方程的个数与未知量的个数相等即 $m = n$，并且 $\textbf{A}$ 满秩可逆，此时 $\textbf{x}$ 有唯一的解。

**(2) 超定方程组：**当上述 $m > n$ 时，并且数据矩阵 $\textbf{A}$ 和数据向量 $\textbf{b}$ 均已知，其中之一或者二者可能存在误差或者干扰。

**(3) 欠定方程组：**当上述 $m < n$ 时，数据矩阵 $\textbf{A}$ 和数据向量 $\textbf{b}$ 均已知，但未知向量 $\textbf{x}$ 可能要求为稀疏向量。

我们这里引进线性方程并给出它的标准形式 $\textbf{Ax} = \textbf{y}$，其中 $\textbf{x} \in \mathbb{R}^n$ 是未知变量，$\textbf{A} \in \mathbb{R}^{m \times n}$ 是参数矩阵，$\textbf{y} \in \mathbb{R}^m$ 是已知向量。线性方程构成了数值线性代数的基础，它们的解法是许多优化方法的关键。事实上，解线性方程组问题 $\textbf{Ax} = \textbf{y}$ 可以被看成**优化问题**，即关于 $x$，最小化 $||\textbf{Ax} − \textbf{y}||^2$。我们描述线性方程组解得集合并且当线性方程组正确解不存在的情况下，讨论求解线性方程组近似解的方法。随后引出最小二乘问题以及它的变体、解的数值敏感性及其解决方法，它们与矩阵分解的关系 (例如QR分解和SVD) 也将被介绍。

![1](image/1.jpg)

图 5.1: 本章导图

## 5.1 线性方程组的直接解法

### 5.1.1 线性方程组问题

在工程问题中，线性方程组描述了变量之间最基本的关系。线性方程在各个科学分支中无处不在，例如弹性力学、电阻网络、曲线拟合等。线性方程构成了线性代数的核心并时常作为 优化问题的约束条件。由于许多优化算法的迭代过程非常依赖线性方程组的解，所以它也是许 多优化算法的基础。下面我们以一个例子来说明，线性方程组如何解决上面的问题。

**例5.1.1.** *(*三点测距问题*)*三角测量是一种确定点位置的方法，给定距离到已知控制点*(*锚点*)*，三边测量可以应用于许多不同的领域，如地理测绘、地震学、导航(例如 *GPS* 系统)等。 在图*5.2*中，三个测距点 $a_1, a_2, a_3 \in \mathbb{R}^2$ 的坐标是已知的，并且从点 $\textbf{x} = (x_1, x_2)^T$ 到测距点的距离为 $d_1, d_2, d_3$，$\textbf{x}$ 的未知坐标与距离测量有关，可以由下面非线性方程组描述

$$
||\textbf{x}−\textbf{a}_1||_2^2 =d_1^2, ||\textbf{x}−\textbf{a}_2||_2^2 =d_2^2, ||\textbf{x}−\textbf{a}_3||_2^2 =d^2_3 \ \ \ (5.1)

$$

![2](image/2.jpg)

图 5.2: 三点测量位置图例。点 $\textbf{x}$ 处，我们测量距三个测距点 $\textbf{a}_1$, $\textbf{a}_2$, $\textbf{a}_3$ 的距离，以便确定 $\textbf{x}$ 的坐标。

通过第一个方程减去另外两个方程，我们获得了两个 $\textbf{x}$ 的线性方程组。

$$
2(\textbf{a}_2 − \textbf{a}_1 )^T \textbf{x} = d_1^2 − d_2^2 + ||\textbf{a}_2 ||_2^2 − ||\textbf{a}_1 ||_2^2 \\
2(\textbf{a}_3 − \textbf{a}_1 )^T \textbf{x} = d_1^2 − d_3^2 + ||\textbf{a}_3 ||_2^2 − ||\textbf{a}_1 ||_2^2

$$

也就是说，原始非线性方程组(5.1)的每个解也可以看作线性方程组的解。使用方程组标准形式 $\textbf{Ax} = \textbf{y}$ *(*标准形式的定义在下一小节给出*)* 可以描述为:

$$
A = \begin{bmatrix}
2(\textbf{a}_2 - \textbf{a}_1)^T \\
2(\textbf{a}_3 - \textbf{a}_1)^T
\end{bmatrix},
\textbf{y} = \begin{bmatrix}
d_1^2 - d_2^2 + ||\textbf{a}_2||_2^2 - ||\textbf{a}_1||_2^2 \\
d_1^2 - d_3^2 + ||\textbf{a}_3||_2^2 - ||\textbf{a}_1||_2^2
\end{bmatrix},
\ \ \ (5.2)

$$

上述问题的解，将在后面详细讨论。

我们先回顾线性方程组中的一般概念。

含 $n$ 个未知量 $x_1,x_2,\cdots,x_n$，$m$个方程的线性方程组的一般形式为

$$
\left\{
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\
\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m
\end{aligned}
\right.
\ \ \ (5.3)

$$

若记

$$
\textbf{A} = (a_{ij})^{m \times n}, \textbf{x} = (x_1, x_2, \cdots, x_n)^T, \textbf{b} = (b_1, b_2, \cdots, b_m)^T
\ \ \ (5.4)

$$

则方程组(5.3)可表为如下的矩阵形式:

$$
\textbf{Ax} = \textbf{b}
\ \ \ (5.5)

$$

当 $\textbf{b} = \textbf{0}$ 时，方程组(5.5)所对应的齐次线性方程组为

$$
\textbf{Ax} = \textbf{0}
\ \ \ (5.6)

$$

**定义 5.1.1.** 矩阵 $\textbf{A} = (a_{ij})^{m \times n}$，称为方程组(5.5) 的**系数矩阵**，而矩阵 $\tilde{A} = (\textbf{A}, \textbf{b})$ 称为它的**增广矩阵**。方程组(5.6)称为方程组(5.5) 的**导出组**。

**定义 5.1.2.** 给定方程组

$$
\bar{A} \textbf{x} = \bar{b}
\ \ \ (5.7)

$$

其中 $\bar{A} = (\bar{a}_{ij})^{m \times n}$，$\textbf{x} = (x_1, x_2, \cdots, x_n)^T$，$\bar{b} = (\bar{b}_1, \bar{b}_2, \cdots, \bar{b}_m)^T$。当 $\textbf{x}^0 = (x_1^0, x_2^0, \cdots, x_n^0)^T$ 是方程组(5.7) 的解向量时，若它也是方程组(5.5) 的解向量，则称方程组(5.5) 与方程组(5.7)是 **同解方程组**。

**定理 5.1.1.** 对方程组(5.5)的系数矩阵 $\textbf{A}$ 及右端作相同的行初等变换，所得到的新方程组与原方程组同解。

**定义 5.1.3.** 设 $\eta_1, \eta_2, \cdots, \eta_t$ 是齐次线性方程组(5.6)的解向量组，如果 $\eta_1, \eta_2, \cdots, \eta_n$ 线性无关，且方程组(5.6)的任意解向量 $\eta$ 都可由 $\eta_1, \eta_2, \cdots, \eta_t$ 线性表出，则称解向量组 $\eta_1, \eta_2, \cdots, \eta_t$ 为方程组(5.6)的一个 **基础解系**。

**定理 5.1.2.** 设齐次线性方程组(5.6)的系数矩阵 $\textbf{A}$ 的秩为 $r$，此时

(*1*) 方程组(5.6)有非零解的必要充分条件是 $r < n$。
(*2*) 若 $r < n$，则方程组(5.6)一定有基础解系。基础解系不是唯一的，但任两个基础解系必等价，且每一个基础解系所含解向量的个数都等于 $n − r$。
(*3*) 若 $r < n$，设 $\eta_1, \eta_2, \cdots, \eta_{n−r}$ 是方程组(5.6) 的一个基础解系，则它的一般解为

$$
\eta = \lambda_1 \eta_1 +\lambda_2 \eta_2 + \cdots + \lambda_{n - r} \eta_{n - r}, \ \ \ (5.8)

$$

其中 $\lambda_i(i = 1, 2, \cdots, n − r)$ 是数域 $\mathbb{K}$ 中的任意常数*.*

**定理5.1.3.** 方程组(5.5)有解的必要充分条件是: $\rank (A) = \rank (\tilde{A})$. 矩阵 $\tilde{A}$ 为它的**增广矩阵**.

**定理5.1.4.** 设 $\rank (A) = \rank (\tilde{A}) = r$, $\gamma_0$ 是非齐次方程组(5.5)的一个解向量 *(*常称为**特解** *)*，$\eta_1, \eta_2, \cdots, \eta_{n−r}$ 是其导出组(5.6)的一个基础解系，则方程组(5.5)的解向量均可表为：

$$
\gamma = \gamma_0 + \eta = \gamma_0 + \lambda_1 \eta_1+\lambda_2 \eta_2 + \cdots + \lambda_{n-r} \eta_{n - r},

$$

其中 $\lambda_i(i = 1, 2, \cdots, n − r)$ 是数域 $\mathbb{K}$ 中的任意常数（这种形式的解向量常称为一般解）.

对增广矩阵 $\tilde{A}$ 进行初等行变换将其化为阶梯型矩阵，写出相应的阶梯型方程组.

（1）若 $r = n$, 则阶梯型方程组形如：

$$
\left\{
\begin{aligned}
c_{11}x_1 + c_{12}x_2 + \cdots + c_{1n}x_n = d_1 \\
c_{22}x_2 + \cdots + c_{2n}x_n = d_2 \\
\cdots \cdots \cdots \cdots \\
c_{nn}x_n = d_n
\end{aligned}
\right.
\ \ \ (5.9)

$$

其中 $c_{ii} \neq 0(i = 1,2, \cdots, n)$.依次由第 $n$ 个，第 $n−1$ 个，$\cdots$,第一个方程组可解得$x_n,x_{n−1}, \cdots, x_1$，由此即得方程组(5.3) 的唯一解 $x_1, x_2, \cdots, x_n$.

（2）若 $r < n$, 则阶梯型方程组可表为:

$$
\left\{
\begin{aligned}
c_{11}x_1 +c_{12}x_2 + \cdots+c_{1r}x_r = d_1 − c_{1,r+1}x_{r+1} − \cdots − c_{1n}x_n \\
c_{22}x_2 + \cdots + c_{2r}x_r = d_2 − c_{2,r+1}x_{r+1} − \cdots − c_{2n}x_n \\
\cdots \cdots \cdots \cdots \\
c_{rr}x_r = d_r − c_{r,r+1}x_{r+1} − \cdots − c_{rn}x_n
\end{aligned}
\right.

$$

其中 $c_{ii} \neq 0(i = 1,2, \cdots,r)$.此时方程组(5.3)有无穷多组解.若令 $x_{r+1} = x_{r+2} = \cdots = x_n = 0$, 则可由方程组(5.10) 求得一个特解 $\gamma_0 = (\delta_1, \delta_2, \cdots, \delta_r, 0, 0, \cdots, 0)$，再由其导出组的一个基础解系 $\eta_1, \eta_2, \cdots, \eta_{n−r}$，可得方程组(5.3)的一般解.
