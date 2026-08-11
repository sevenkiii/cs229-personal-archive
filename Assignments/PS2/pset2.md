# Problem Set 2

note the // is something written after correct the mistakes.

## Prb.1

### (a)

A converged quickly but B not.

### (b)

below, $y \in \{0,1\}$

dataset B is linearly separable.

thus $g(\theta^Tx)$ go higher as theta gets bigger, which lead to lower loss.

There is not a point where loss get the min value. it go far away.

why A can converge? Suppose we have a y=1 but wrongly classify to h<0.5, the other points are classified correctly. Consider the loss:

$\log h(x^{(i)}) = \log g(\theta^Tx^{(i)})$

when $\theta \to \infty$, other point loss=0, but this point loss = infinity

so there exists a minimum point.

// key point: very wrong separation's loss >> very correct separation's reward

### (c)

// actually changing learning rate can't solve the problem definitely.

// lower learning rate <=> lower difference

ii iv v yes.

i iii no.

### (d)

not vulnerable. the hinge loss can go to zero.

B is linearly separable. and geometric margin don't change when we just change $||\theta||$

## Prb. 4

$$
z^TKz = \sum z_iz_jK_d(x^{(i)},x^{(j)})\ge 0  \ \ \ \text{for }d=1,2
$$

### (a)

yes
$$
z^TKz = \sum z_iz_j[K_1(x^{(i)},x^{(j)})+K_2(x^{(i)},x^{(j)})] =z^TK_1z + z^TK_2z\ge 0
$$

### (b)

no
$$
z^TKz = \sum z_iz_j[K_1(x^{(i)},x^{(j)})-K_2(x^{(i)},x^{(j)})] =z^TK_1z - z^TK_2z
$$
let $K_2=2K_1$ (by c we knew we can do that),we have
$$
z^TKz= -z^TK_1z\le 0
$$

### (c)

yes

$z^TKz = az^TK_1z\ge 0$

### (d)

no

$z^TKz = -az^TK_1z\le 0$

### (e)

yes

since $K_1,K_2$ are kernels. we can found $\phi_1,\phi_2$ corresponding to them.
$$
K_{ij} = K_{1ij}K_{2ij}
$$

$$
\begin{aligned}
z^TKz&=\sum_{i=1}^n\sum_{j=1}^n z_iz_jK_{1ij}K_{2ij}\\
&=\sum_{i=1}^n\sum_{j=1}^n z_iz_j\phi_1(x^{(i)})^T\phi_1(x^{(j)})\phi_2(x^{(i)})^T\phi_2(x^{(j)})\\
&= \sum_{i=1}^n\sum_{j=1}^n z_iz_j\left(\sum_{u=1}^{d_1}\phi_1(x^{(i)})_u\phi_1(x^{(j)})_u\right)\left(\sum_{v=1}^{d_2}\phi_2(x^{(i)})_v\phi_2(x^{(j)})_v\right)\\
&= \sum_{u=1}^{d_1}\sum_{v=1}^{d_2}\sum_{i=1}^nz_i\phi_1(x^{(i)})_u\phi_2(x^{(i)})_v\sum_{j=1}^n z_j\phi_1(x^{(j)})_u\phi_2(x^{(j)})_v\\
&= \sum_{u=1}^{d_1}\sum_{v=1}^{d_2}\left(\sum_{i=1}^nz_i\phi_1(x^{(i)})_u\phi_2(x^{(i)})_v\right)^2\ge 0
\end{aligned}
$$

### (f)

yes
$$
\begin{aligned}
z^TKz &= \sum_{i=1}^n\sum_{j=1}^n z_iz_jf(x^{(i)})f(x^{(j)})\\
&=\sum_{i=1}^nz_if(x^{(i)})\sum_{j=1}^n z_jf(x^{(j)})\\
&=\left(\sum_{i=1}^nz_if(x^{(i)})\right)^2\ge0
\end{aligned}
$$

### (g)

yes

for each set of $x^{(i)}$, $K_3$ is PSD

replace $x^{(i)}$ by $\phi(x^{(i)})$ , it is still PSD, but now it turns into $K$, so $K$ is PSD.

### (h)

yes
$$
\begin{aligned}
z^TKz&= \sum_{i=1}^n\sum_{j=1}^n z_iz_j\sum_{u=0}^sa_uK_{1ij}^u\\
&=\sum_{u=0}^sa_u\sum_{i=1}^n\sum_{j=1}^n z_iz_jK_{1ij}^u
\end{aligned}
$$
by (e) we can know that for any positive integer u we have $K(x,z) = K_1^u(x,z)$ is a kernel, so we can know that
$$
\sum_{i=1}^n\sum_{j=1}^n z_iz_jK_{1ij}^u\ge0
$$
for u=0, we know that $\sum_{i=1}^n\sum_{j=1}^n z_iz_j = (\sum_{i=1}^nz_i)^2\ge0$

since $a_u>0$, $z^TKz\ge 0$
