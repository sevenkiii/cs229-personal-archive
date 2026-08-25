# Problem Set 3

## Problem 1

### (a)

$$
\begin{aligned}
g(x):&=1/(1+\exp(-x))\\
u :&=w^{[1]}_{0,2} + w^{[1]}_{1,2}x^{(i)}_1 + w^{[1]}_{2,2}x^{(i)}_2\\
v :&=w^{[2]}_0 + w^{[2]}_1h_1 + w^{[2]}_2h_2+w^{[2]}_3h_3\\
h_2 &= g(u)\\
o^{(i)} &= g(v)\\
\dfrac{\partial l}{\partial o^{(i)}} &= \dfrac{2(o^{(i)}-y^{(i)})}{m}\\
\dfrac{\partial o^{(i)}}{\partial h_2}&=g(v)(1-g(v))w^{[2]}_2\\
\dfrac{\partial h_2}{\partial w^{[1]}_{1,2}}&=g(u)(1-g(u))x^{(i)}_1\\
\dfrac{\partial l}{\partial w^{[1]}_{1,2}} &= \sum_{i=1}^m\dfrac{\partial l}{\partial o^{(i)}}\dfrac{\partial o^{(i)}}{\partial w^{[2]}_2}\dfrac{\partial w^{[2]}_2}{\partial w^{[1]}_{1,2}}\\
&= \sum_{i=1}^m\dfrac{2(o^{(i)}-y^{(i)})}{m}g(v)(1-g(v))w^{[2]}_2g(u)(1-g(u))x^{(i)}_1\\
&= \frac{2}{m}\sum_{i=1}^m(o^{(i)}-y^{(i)})o^{(i)}(1-o^{(i)})w^{[2]}_2h_2(1-h_2)x^{(i)}_1\\


\end{aligned}
$$

so the update rule is:
$$
w^{[1]}_{1,2}:= w^{[1]}_{1,2} - \alpha \frac{2}{m}\sum_{i=1}^m(o^{(i)}-y^{(i)})o^{(i)}(1-o^{(i)})w^{[2]}_2h_2(1-h_2)x^{(i)}_1
$$


### (b)

we found the blue points in in the triangle formed by the following 3 lines:
$$
x_1 - 0.5 = 0\\
x_2 -0.5 = 0\\
x_1+x_2-4=0
$$
we just need to use the three neurons to show if a point is in the "positive side"(let it be the triangle side) of the three lines, and output if and only if the three indicators all show 1.

### (c)

such a set of weights doesn't exist.

using the linear function, the neural network is equivalent to a linear classifier which can only draw a straight line to classify, but the points can't be classified with 100% accuracy by a line.
$$
W^{[2]}(W^{[1]}x+b^{[1]})+b^{[2]} = W^{[2]}W^{[1]}x+W^{[2]}b^{[1]}+b^{[2]}=Wx+b\\
W = W^{[2]}W^{[1]}, b=W^{[2]}b^{[1]}+b^{[2]}
$$

## Problem 2

### (a)

$$
\begin{aligned}
-D_{\mathrm{KL}}(P||Q) &= -\sum_{x \in \mathcal X} P(x) \log \dfrac{P(x)}{Q(x)}\\
&= \mathbb E_{x\sim P}\left[\log \dfrac{Q(x)}{P(x)}\right]\\
&\le \log \mathbb E_{x\sim P}\left[ \dfrac{Q(x)}{P(x)}\right]\\
&= \log \sum_{x \in \mathcal X}Q(x) = \log 1 = 0\\
D_{\mathrm{KL}}(P||Q) &\ge 0\\

\end{aligned}
$$

and we have
$$
\mathbb E_{x\sim P}\left[\log \dfrac{Q(x)}{P(x)}\right]= \log \mathbb E_{x\sim P}\left[ \dfrac{Q(x)}{P(x)}\right]
$$
if and only if
$$
\dfrac{Q(x)}{P(x)} = \mathrm{Constant}
$$
and due to
$$
\sum_{x\in \mathcal X}P(x) = \sum_{x\in \mathcal X}Q(x) = 1
$$
so
$$
P(x) = Q(x)
$$

### (b)

$$
\begin{aligned}
&{ }   D_{\mathrm{KL}}(P(X)||Q(X))+D_{\mathrm{KL}}(P(Y|X)||Q(Y|X)) \\
&= \sum_{x}P(x)\log \dfrac{P(x)}{Q(x)} + \sum_x P(x)\left(\sum_yP(y|x)\log \dfrac{P(x,y)/P(x)}{Q(x,y)/Q(x)}\right)\\
&= \sum_{x}P(x)\log \dfrac{P(x)}{Q(x)} + \sum_x P(x)\left(\sum_yP(y|x)\left[\log \dfrac{P(x,y)}{Q(x,y)} - \log\dfrac{P(x)}{Q(x)}\right]\right)\\
&= \sum_{x}P(x)\log \dfrac{P(x)}{Q(x)} + \sum_x P(x)\sum_yP(y|x)\log \dfrac{P(x,y)}{Q(x,y)} - \sum_x P(x)\log\dfrac{P(x)}{Q(x)}\sum_yP(y|x)\\
&=  \sum_x P(x)\sum_yP(y|x)\log \dfrac{P(x,y)}{Q(x,y)} \\
&=\sum_x\sum_yP(x,y)\log \dfrac{P(x,y)}{Q(x,y)} = D_{\mathrm{KL}}(P(X,Y)||Q(X,Y))
\end{aligned}
$$

### (c)

$$
\begin{aligned}
\arg \min_\theta D_{\mathrm{KL}}(\hat P || P_\theta) &= \arg \min_\theta \sum_x \hat P(x) \log \dfrac{\hat P(x)}{P_\theta(x)}\\
&=\arg \min_\theta \sum_x \hat P(x) \log {\hat P(x)}-\sum_x\hat P(x)\log{P_\theta(x)}\\
&=\arg \min_\theta -\sum_x\hat P(x)\log{P_\theta(x)}\\
&=\arg \max_\theta \sum_x\hat P(x)\log{P_\theta(x)}\\
&=\arg \max_\theta \sum_x\frac{1}{m}\sum_{i=1}^m 1\{x^{(i)}=x\}\log{P_\theta(x)}\\
&=\arg \max_\theta \sum_{i=1}^m \log{P_\theta(x^{(i)})}\\
\end{aligned}
$$

## Problem 3

### (a)

$$
\begin{aligned}
\mathbb E_{y\sim p(y;\theta)}[\nabla_{\theta'}\log p(y;\theta')|_{\theta'=\theta}] &= \mathbb E_{y\sim p(y;\theta)}\left[\dfrac{1}{p(y;\theta)} \nabla_{\theta'}p(y;\theta')|_{\theta'=\theta}\right]\\
&= \int_{-\infty}^{\infty} p(y;\theta)\dfrac{1}{p(y;\theta)}\nabla_{\theta'}p(y;\theta')|_{\theta'=\theta} dy \\
&= \int_{-\infty}^{\infty}\nabla_{\theta'}p(y;\theta')|_{\theta'=\theta} dy\\
&= \left[\nabla_{\theta'}\int_{-\infty}^{\infty}p(y;\theta') dy \right]|_{\theta'=\theta}\\
&= \left[\nabla_{\theta'}1 \right]|_{\theta'=\theta} =0
\end{aligned}
$$

### (b)

$$
\begin{aligned}
f(y,\theta)&:=\nabla_{\theta'}\log p(y;\theta')|_{\theta' = \theta}\\
\mathcal I(\theta) &= \mathrm{Cov}_{y\sim p(y;\theta)} [f(y,\theta)]\\
&= \mathbb E_{y\sim p(y;\theta)} [(f(y,\theta)-\mu)(f(y,\theta)-\mu)^T]\\
\mu &= \mathbb E_{y\sim p(y;\theta)}[\nabla_{\theta'}\log p(y;\theta')|_{\theta'=\theta}] = 0\\
\mathcal I(\theta) &= \mathbb E_{y\sim p(y;\theta)} [f(y,\theta)f(y,\theta)^T]\\
&=\mathbb E_{y\sim p(y;\theta)} [\nabla_{\theta'}\log p(y;\theta')\nabla_{\theta'}\log p(y;\theta')^T|_{\theta' = \theta}]
\end{aligned}
$$

### (c)

$$
\begin{aligned}
\mathbb E_{y\sim p(y;\theta)}[-\nabla^2_{\theta'}\log p(y;\theta')|_{\theta' = \theta}] &= \mathbb E_{y\sim p(y;\theta)}\left[-\nabla_{\theta'}{(\nabla_{\theta'}\log p(y;\theta'))^T}|_{\theta' = \theta}\right]\\
&= \mathbb E_{y\sim p(y;\theta)}\left[-\nabla_{\theta'}{\dfrac{\nabla_{\theta'} p(y;\theta')^T}{p(y;\theta')}}|_{\theta' = \theta}\right]\\
&= \mathbb E_{y\sim p(y;\theta)}\left[-{\dfrac{p(y;\theta')\nabla_{\theta'}^2 p(y;\theta') - \nabla_{\theta'}p(y;\theta')\nabla_{\theta'} p(y;\theta')^T}{p^2(y;\theta')}}|_{\theta' = \theta}\right]\\
&= \mathbb E_{y\sim p(y;\theta)}\left[-{\dfrac{p(y;\theta')\nabla_{\theta'}^2 p(y;\theta') }{p^2(y;\theta')}}|_{\theta' = \theta}\right] + \mathbb E_{y\sim p(y;\theta)}\left[ \dfrac{\nabla_{\theta'}p(y;\theta')\nabla_{\theta'} p(y;\theta')^T}{p^2(y;\theta')}|_{\theta' = \theta}\right]\\
\end{aligned}
$$

now we have
$$
\begin{aligned}
\mathbb E_{y\sim p(y;\theta)}\left[-{\dfrac{p(y;\theta')\nabla_{\theta'}^2 p(y;\theta') }{p^2(y;\theta')}}|_{\theta' = \theta}\right] &= -\int_{-\infty}^{\infty} p(y;\theta){\dfrac{p(y;\theta')\nabla_{\theta'}^2 p(y;\theta') }{p^2(y;\theta')}}|_{\theta' = \theta} dy\\
&=-\int_{-\infty}^{\infty} {{\nabla_{\theta'}^2 p(y;\theta') }}|_{\theta' = \theta} dy\\
&=-\nabla_{\theta'}^2\int_{-\infty}^{\infty} {{ p(y;\theta') }} dy|_{\theta' = \theta}\\
&= -\nabla_{\theta'}^21|_{\theta' = \theta} =0
\end{aligned}
$$
and
$$
\nabla_{\theta'}\log p(y;\theta')\nabla_{\theta'}\log p(y;\theta')^T = \dfrac{\nabla_{\theta'}p(y;\theta')}{p(y;\theta')}\times\dfrac{\nabla_{\theta'}p(y;\theta') ^T}{p(y;\theta')}\\
\mathbb E_{y\sim p(y;\theta)}\left[ \dfrac{\nabla_{\theta'}p(y;\theta')\nabla_{\theta'} p(y;\theta')^T}{p^2(y;\theta')}|_{\theta' = \theta}\right] = \mathbb E_{y\sim p(y;\theta)}\left[\nabla_{\theta'}\log p(y;\theta')\nabla_{\theta'}\log p(y;\theta')^T|_{\theta' = \theta}\right]
$$
so
$$
\begin{aligned}
\mathbb E_{y\sim p(y;\theta)}[-\nabla^2_{\theta'}\log p(y;\theta')|_{\theta' = \theta}]
&= \mathbb E_{y\sim p(y;\theta)}\left[-{\dfrac{p(y;\theta')\nabla_{\theta'}^2 p(y;\theta') }{p^2(y;\theta')}}|_{\theta' = \theta}\right] + \mathbb E_{y\sim p(y;\theta)}\left[ \dfrac{\nabla_{\theta'}p(y;\theta')\nabla_{\theta'} p(y;\theta')^T}{p^2(y;\theta')}|_{\theta' = \theta}\right]\\
&= 0 + \mathbb E_{y\sim p(y;\theta)}\left[\nabla_{\theta'}\log p(y;\theta')\nabla_{\theta'}\log p(y;\theta')^T|_{\theta' = \theta}\right]\\
&= \mathcal I(\theta)

\end{aligned}
$$

### (d)

$$
\begin{aligned}
D_{\mathrm{KL}}(p_\theta||p_{\tilde\theta}) &\approx D_{\mathrm{KL}}(p_\theta||p_{\theta})
 + (\tilde\theta-\theta)^T\nabla_{\theta'}D_{\mathrm{KL}}(p_\theta||p_{\theta'})|_{\theta'=\theta} + \dfrac{1}{2}(\tilde\theta-\theta)^T (\nabla^2_{\theta'}D_{\mathrm{KL}}(p_\theta||p_{\theta'})|_{\theta'=\theta}) (\tilde\theta-\theta)\\
&= (\tilde\theta-\theta)^T\nabla_{\theta'}D_{\mathrm{KL}}(p_\theta||p_{\theta'})|_{\theta'=\theta} + \dfrac{1}{2}(\tilde\theta-\theta)^T (\nabla^2_{\theta'}D_{\mathrm{KL}}(p_\theta||p_{\theta'})|_{\theta'=\theta}) (\tilde\theta-\theta)\\

\end{aligned}
$$

$$
\begin{aligned}
D_{\mathrm{KL}}(p_\theta||p_{\tilde\theta}) &= \int_{-\infty}^{\infty} p(y;\theta)\log p(y;\theta)dy - \int_{-\infty}^{\infty} p(y;\theta)\log p(y;\tilde\theta)dy\\
\nabla_{\theta'}D_{\mathrm{KL}}(p_\theta||p_{\theta'}) &= - \int_{-\infty}^{\infty} p(y;\theta)\dfrac{\nabla_{\theta'}p(y;\theta')}{p(y;\theta')}dy\\
\nabla_{\theta'}D_{\mathrm{KL}}(p_\theta||p_{\theta'})|_{\theta'=\theta} &= - \int_{-\infty}^{\infty} \nabla_{\theta'}p(y;\theta')dy|_{\theta'=\theta}\\
&=- \nabla_{\theta'}\int_{-\infty}^{\infty} p(y;\theta')dy|_{\theta'=\theta} = - \nabla_{\theta'}1|_{\theta'=\theta} = 0\\
\end{aligned}
$$

so, we have:
$$
D_{\mathrm{KL}}(p_\theta||p_{\tilde\theta}) \approx  \dfrac{1}{2}(\tilde\theta-\theta)^T (\nabla^2_{\theta'}D_{\mathrm{KL}}(p_\theta||p_{\theta'})|_{\theta'=\theta}) (\tilde\theta-\theta)
$$
let's get $\mathcal I(\theta)$:
$$
\begin{aligned}
\nabla^2_{\theta'}D_{\mathrm{KL}}(p_\theta||p_{\theta'})|_{\theta'=\theta} &= - \nabla^2_{\theta'}\int_{-\infty}^{\infty} p(y;\theta)\log p(y;\theta')dy |_{\theta'=\theta}\\
&= - \int_{-\infty}^{\infty} p(y;\theta) \nabla_{\theta'}\dfrac{\nabla_{\theta'}p(y;\theta')^T}{p(y;\theta')}dy |_{\theta'=\theta}\\
&= - \int_{-\infty}^{\infty} p(y;\theta) {\dfrac{p(y;\theta')\nabla_{\theta'}^2 p(y;\theta') - \nabla_{\theta'}p(y;\theta')\nabla_{\theta'} p(y;\theta')^T}{p^2(y;\theta')}}dy |_{\theta'=\theta}\\
&= - \int_{-\infty}^{\infty} \nabla_{\theta'}^2 p(y;\theta')dy |_{\theta'=\theta} + \int_{-\infty}^{\infty} {\dfrac{\nabla_{\theta'}p(y;\theta')\nabla_{\theta'} p(y;\theta')^T|_{\theta'=\theta}}{p(y;\theta)}}dy \\
&= \int_{-\infty}^{\infty} {\dfrac{\nabla_{\theta'}p(y;\theta')\nabla_{\theta'} p(y;\theta')^T|_{\theta'=\theta}}{p(y;\theta)}}dy 
\end{aligned}
$$
and we have:
$$
\begin{aligned}
\mathcal I(\theta)&=\mathbb E_{y\sim p(y;\theta)}\left[\nabla_{\theta'}\log p(y;\theta')\nabla_{\theta'}\log p(y;\theta')^T|_{\theta' = \theta}\right]\\
&= \mathbb E_{y\sim p(y;\theta)}\left[\dfrac{\nabla_{\theta'}p(y;\theta')}{p(y;\theta')} \dfrac{\nabla_{\theta'}p(y;\theta')^T}{p(y;\theta')}|_{\theta' = \theta}\right]\\
&= \int_{-\infty}^{\infty} p(y;\theta)\dfrac{\nabla_{\theta'}p(y;\theta')}{p(y;\theta')} \dfrac{\nabla_{\theta'}p(y;\theta')^T}{p(y;\theta')}|_{\theta' = \theta}dy\\
&= \int_{-\infty}^{\infty}  \dfrac{\nabla_{\theta'}p(y;\theta')\nabla_{\theta'}p(y;\theta')^T|_{\theta' = \theta}}{p(y;\theta)}dy = \nabla^2_{\theta'}D_{\mathrm{KL}}(p_\theta||p_{\theta'})|_{\theta'=\theta}
\end{aligned}
$$
so
$$
D_{\mathrm{KL}}(p_\theta||p_{\tilde\theta}) \approx  \dfrac{1}{2}(\tilde\theta-\theta)^T (\nabla^2_{\theta'}D_{\mathrm{KL}}(p_\theta||p_{\theta'})|_{\theta'=\theta}) (\tilde\theta-\theta) = \dfrac{1}{2}d^T\mathcal I(\theta)d
$$

### (e)

after approximation we have our problem:
$$
d^* = \arg \max_d \ell(\theta) + d^T\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}\\
\text{subject to }\dfrac{1}{2}d^T\mathcal I(\theta)d = c
$$
construct a Lagrangian：
$$
\mathcal L(d,\lambda) =\ell(\theta) + d^T\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta} -\lambda\left(\dfrac{1}{2}d^T\mathcal I(\theta)d - c\right)
$$
we have
$$
\nabla_d\mathcal L(d,\lambda) = \nabla_{\theta'}\ell(\theta')|_{\theta' = \theta} -\lambda \mathcal I(\theta)d\\
\nabla_\lambda\mathcal L(d,\lambda) = \left(c-\dfrac{1}{2}d^T\mathcal I(\theta)d\right)
$$
set to zero
$$
\begin{aligned}
\nabla_d\mathcal L(d,\lambda) = \nabla_{\theta'}\ell(\theta')|_{\theta' = \theta} -\lambda \mathcal I(\theta)d &= 0\\
\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta} &=\lambda \mathcal I(\theta)d\\
d&= \dfrac{\mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}}{\lambda }\\
\tilde d(\lambda) &= \dfrac{\mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}}{\lambda }
\end{aligned}
$$
plug into (b).

$$
\begin{aligned}
\nabla_\lambda\mathcal L(d,\lambda) = c-\dfrac{1}{2}d^T\mathcal I(\theta)d &= 0\\
\dfrac{1}{2}\dfrac{(\mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta})}{\lambda }^T\mathcal I(\theta)\dfrac{\mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}}{\lambda } &= c\\
\dfrac{(\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta} )^T\mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}}{ 2c} &= \lambda^2\\
\sqrt{\dfrac{(\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta} )^T\mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}}{ 2c}} &= \lambda
\end{aligned}
$$
plug into (a).
$$
\begin{aligned}
d&= \mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}\sqrt{\dfrac{2c}{   (\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta} )^T\mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}}}\\

\end{aligned}
$$
finally we have
$$
d^* = \mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}\sqrt{\dfrac{2c}{   (\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta} )^T\mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}}}
$$

### (f)

the Newton's Method:
$$
\theta := \theta - H^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}
$$
natural gradient:
$$
\begin{aligned}
\theta &:= \theta + \dfrac{\mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}}{\lambda }\\
&=\theta + \dfrac{\mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}}{\lambda }
\end{aligned}
$$
where
$$
\begin{aligned}
\mathcal I(\theta) =  \mathbb E_{y\sim p(y;\theta)}[-\nabla^2_{\theta'}\log p(y;\theta')|_{\theta' = \theta}]
\end{aligned}
$$
for a GLM
$$
\begin{aligned}
p(y;\theta') = b(y)\exp\left(\eta^TT(y)-a(\eta)\right)\\
\log p(y;\theta') = (\theta'^Txy - a(\theta'^Tx)) +\log b(y)\\
\nabla_{\theta'} \log p(y;\theta') = (y - a'(\theta'^Tx))x \\
\nabla_{\theta'}^2 \log p(y;\theta') = -a''(\theta'^Tx)xx^T 
\end{aligned}
$$
so
$$
\begin{aligned}
\mathcal I(\theta) &=  \mathbb E_{y\sim p(y;\theta)}[-\nabla^2_{\theta'}\log p(y;\theta')|_{\theta' = \theta}]\\
&= \mathbb E_{y\sim p(y;\theta)}[a''(\theta'^Tx)xx^T |_{\theta' = \theta}]\\
&= a''(\theta'^Tx)xx^T |_{\theta' = \theta} = - H
\end{aligned}
$$

$$
\begin{aligned}
\theta &:= \theta + \dfrac{\mathcal I(\theta)^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}}{\lambda }\\
&= \theta - \dfrac{ H^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}}{\lambda }
\end{aligned}
$$

compare with newton's method:
$$
\theta := \theta - H^{-1}\nabla_{\theta'}\ell(\theta')|_{\theta' = \theta}
$$
 they have the same update direction.

## Problem 4.

