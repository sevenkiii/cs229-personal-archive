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

## Prb. 2

### (a)

(0,1) including all training set

after MLE, we have

(in the intercept term all x give 1.)
$$
\begin{aligned}
\dfrac{\partial}{\partial\theta_j}\ell(\theta) = \sum_{i=1}^m(y^{(i)}-g(\theta^Tx^{(i)}))x_j^{(i)}&=0\\
\sum_{i=1}^my^{(i)}x_0^{(i)} &= \sum_{i=1}^mg(\theta^Tx^{(i)})x_0^{(i)}\\
\sum_{i=1}^my^{(i)}&=\sum_{i=1}^mg(\theta^Tx^{(i)})\\
\frac{\sum_{i\in I_{a,b}}\mathbb{I}\{y^{(i)}=1\}}{\vert{}\{i\in I_{a,b}\}\vert{}}&=\frac{\sum_{i\in I_{a,b}}P(y^{(i)}=1\vert{}x^{(i)};\theta)}{\vert{}\{i\in I_{a,b}\}\vert{}}
\end{aligned}
$$

### (b)

~~both yes.~~

~~in fact, the assumption of GLM holds, and Bernoulli is in Exponential Family, so when the property holds, the model just fit the Bernoulli distribution exactly, leading to perfect accuracy. The converse is also true, as perfect accuracy leads to MLE, MLE leads to fit the Bernoulli exactly.~~

**both NO**

when $(a,b) = (0.5,1)$, all predictions are "1". however
$$
\frac{\sum_{i\in I_{a,b}}\mathbb{I}\{y^{(i)}=1\}}{\vert{}\{i\in I_{a,b}\}\vert{}}=\frac{\sum_{i\in I_{a,b}}P(y^{(i)}=1\vert{}x^{(i)};\theta)}{\vert{}\{i\in I_{a,b}\}\vert{}}<1
$$
that is, perfect accuracy can't be achieved.

In the same way, the converse, though achieves perfect accuracy, we have  

$$
\frac{\sum_{i\in I_{a,b}}P(y^{(i)}=1\vert{}x^{(i)};\theta)}{\vert{}\{i\in I_{a,b}\}\vert{}}<1=\frac{\sum_{i\in I_{a,b}}\mathbb{I}\{y^{(i)}=1\}}{\vert{}\{i\in I_{a,b}\}\vert{}}
$$

so the converse is wrong.

// 原来 perfect accuracy 是全对的意思啊......

### (c)

including regularization can lead to lower Var and higher Bias. That is, it will not MLE, leading to not fitting the Bernoulli exactly. (Or, it modifies the loss function so that the likelihood won't be maximized, give way to L2 norm.) therefore, there will be some error on model calibration. 
$$
\begin{aligned}
\dfrac{\partial}{\partial\theta_j}\ell(\theta) = \lambda\theta_j+\sum_{i=1}^m(y^{(i)}-g(\theta^Tx^{(i)}))x_j^{(i)} &=0\\
\lambda\theta_j+\sum_{i=1}^my^{(i)}x_0^{(i)} &= \sum_{i=1}^mg(\theta^Tx^{(i)})x_0^{(i)}\\
\lambda\theta_j+\sum_{i=1}^my^{(i)}&=\sum_{i=1}^mg(\theta^Tx^{(i)})\\
\lambda\theta_j+\sum_{i\in I_{a,b}}\mathbb{I}\{y^{(i)}=1\}&=\sum_{i\in I_{a,b}}P(y^{(i)}=1\vert{}x^{(i)};\theta)
\end{aligned}
$$


## Prb. 3

### (a)

$$
\begin{aligned}
\theta_{\mathrm{MAP}} &= \arg \max_\theta p(\theta | x,y)\\
&=\arg \max_\theta \dfrac{p(x,y|\theta)p(\theta)}{p(x,y)}\\
&=\arg \max_\theta \dfrac{p(y|x,\theta)p(x|\theta)p(\theta)}{p(x,y)}\\
&=\arg \max_\theta \dfrac{p(y|x,\theta)p(x)p(\theta)}{p(x,y)}\\
&=\arg \max_\theta p(y|x,\theta)p(\theta)
\end{aligned}
$$

### (b)

$$
\begin{aligned}
\theta_{\mathrm{MAP}}&=\arg \max_\theta p(y|x,\theta)p(\theta)\\
&= \arg \max_\theta p(y|x,\theta)\dfrac{1}{(2\pi)^{d/2}|\eta^2I|^{1/2}}\exp\left(-\frac{1}{2}\theta^T(\eta^2I)^{-1}\theta\right)\\
&= \arg \max_\theta p(y|x,\theta)\dfrac{1}{(2\pi)^{d/2}\eta^{d}}\exp\left(-\frac{1}{2\eta^2}\theta^T\theta\right)\\
&= \arg \max_\theta p(y|x,\theta)\exp\left(-\frac{1}{2\eta^2}||\theta||_2^2\right)\\
&= \arg \min_\theta -\log p(y|x,\theta) +\frac{1}{2\eta^2}||\theta||_2^2\\
\lambda &= \dfrac{1}{2\eta^2}
\end{aligned}
$$

### (c)

$$
\begin{aligned}
\theta_{\mathrm{MAP}}&= \arg \min_\theta -\log p(y|x,\theta) +\frac{1}{2\eta^2}||\theta||_2^2\\
&= \arg \min_\theta -\log \left(\frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\dfrac{(y-\theta^Tx)^2}{2\sigma^2}\right)\right) +\frac{1}{2\eta^2}||\theta||_2^2\\
&= \arg \min_\theta \dfrac{(y-\theta^Tx)^2}{2\sigma^2}-\log \frac{1}{\sqrt{2\pi}\sigma} +\frac{1}{2\eta^2}||\theta||_2^2\\
&= \arg \min_\theta \dfrac{(y-\theta^Tx)^2}{2\sigma^2} +\frac{||\theta||_2^2}{2\eta^2}
\end{aligned}
$$

now consider the training examples.
$$
\begin{aligned}
\theta_{\mathrm{MAP}}&= \arg \min_\theta \dfrac{(\vec{y}-X\theta)^T(\vec{y}-X\theta)}{2\sigma^2} +\frac{\theta^T\theta}{2\eta^2}\\
\ell(\theta):&=\dfrac{(\vec{y}-X\theta)^T(\vec{y}-X\theta)}{2\sigma^2} +\frac{\theta^T\theta}{2\eta^2}\\
\grad_\theta\ell(\theta)&=\dfrac{1}{2\sigma^2}\grad_\theta\left(\vec{y}^T\vec{y} -\theta^TX^T\vec{y}-\vec{y}^TX\theta+\theta^TX^TX\theta\right) + \dfrac{\theta}{\eta^2}\\

&=\dfrac{1}{2\sigma^2}\grad_\theta\left( -2\theta^TX^T\vec{y}+\theta^TX^TX\theta\right) + \dfrac{\theta}{\eta^2}\\
&=\dfrac{-2X^T\vec{y} + 2X^TX\theta }{2\sigma^2}+ \dfrac{\theta}{\eta^2}\\
&=\dfrac{ X^TX\theta -X^T\vec{y}}{\sigma^2}+ \dfrac{\theta}{\eta^2}
\end{aligned}
$$
set grad to zero:
$$
\begin{aligned}
\dfrac{ X^TX\theta -X^T\vec{y}}{\sigma^2}+ \dfrac{\theta}{\eta^2}&=0\\
(X^TX\theta -X^T\vec{y}) + \dfrac{\sigma^2\theta}{\eta^2} &= 0\\
(X^TX +\dfrac{\sigma^2}{\eta^2}I) \theta &= X^T\vec{y}\\
\theta_{\mathrm{MAP}} &= \left(X^TX +\dfrac{\sigma^2}{\eta^2}I\right)^{-1}X^T\vec{y}
\end{aligned}
$$

### (d)

$$
\begin{aligned}
\theta_{\mathrm{MAP}}&=\arg \max_\theta p(y|x,\theta)p(\theta)\\
&=\arg \max_\theta p(y|x,\theta)\prod_j \dfrac{1}{2b}\exp({-\frac{|\theta_j|}{b}})\\
&=\arg \max_\theta \log p(y|x,\theta) + \sum_j -\frac{|\theta_j|}{b}+\log \frac{1}{2b}\\
&=\arg \min_\theta -\log p(y|x,\theta) +\dfrac{1}{b}||\theta||_1\\
&=\arg \min_\theta \dfrac{(y-\theta^Tx)^2}{2\sigma^2} +\dfrac{1}{b}||\theta||_1\\
&=\arg \min_\theta \ (y-\theta^Tx)^2 +\dfrac{2\sigma^2}{b}||\theta||_1\\
\end{aligned}
$$

in matrix form we have
$$
J(\theta) = ||X\theta-\vec{y}||_2^2 +\dfrac{2\sigma^2}{b}||\theta||_1\\
\gamma = \dfrac{2\sigma^2}{b}\\
\theta_{\mathrm{MAP}} = \arg \min_\theta J(\theta)
$$

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

## Prb. 5

### (a)

i.

note $\langle x,z\rangle = x^Tz$

assume that
$$
\theta^{(i)}=\sum_{j=1}^i\lambda_j \phi(x^{(j)})
$$

$$
\begin{aligned}
\theta^{(i+1)}:&=\sum_{j=1}^i\lambda_j\phi(x^{(j)}) + \alpha\left(y^{(i+1)}-g\left(\sum_{j=1}^i\lambda_j\phi(x^{(j)})^T\phi(x^{(i+1)})\right)\right)\phi(x^{(i+1)})\\
&=\sum_{j=1}^i\lambda_j\phi(x^{(j)}) + \alpha\left(y^{(i+1)}-g\left(\sum_{j=1}^i\lambda_jK(x^{(j)},x^{(i+1)})\right)\right)\phi(x^{(i+1)})\\
\end{aligned}
$$

by induction we know the assumption is correct, and 
$$
\lambda_{i+1} = \alpha\left(y^{(i+1)}-g\left(\sum_{j=1}^i\lambda_jK(x^{(j)},x^{(i+1)})\right)\right)
$$
we can use lambda to represent theta implicitly. $\theta^{(i)}=\sum_{j=1}^i\lambda_j\phi(x_j)$, specifically $\theta^{(0)}=0$ with all the lambda is initial zero.

ii.

$$
\begin{aligned}
h_{\theta^{(i)}}(x^{(i+1)}) &= g(\theta^{(i)^T}\phi(x^{(i+1)}))\\
&= g\left(\sum_{j=1}^i\lambda_j \phi(x^{(j)})^T\phi(x^{(i+1)})\right)\\
&= g\left(\sum_{j=1}^i\lambda_j K(x^{(j)},x^{(i+1)})\right)

\end{aligned}
$$
iii. has been shown above.

### (c)

dot product kernel.

using dot product as a kernel gives a $\phi(x)=x$, so the perceptron can only give a linear decision boundary.

//note: the code in util.py mistakes `y == 0` as `y == -1`
