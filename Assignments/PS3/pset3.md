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

## Problem 4

### (a)

$$
\begin{aligned}
\ell_{\text{semi-sup}}(\theta^{(t+1)}) &= \sum_i \mathrm{ELBO}(x^{(i)};Q_i^{(t+1)},\theta^{(t+1)}) +\alpha\left(\sum_{i=1}^{\tilde m} \log p(\tilde x^{(i)},\tilde z^{(i)};\theta^{(t+1)})\right)\\
&\ge  \sum_i \mathrm{ELBO}(x^{(i)};Q_i^{(t)},\theta^{(t+1)}) +\alpha\left(\sum_{i=1}^{\tilde m} \log p(\tilde x^{(i)},\tilde z^{(i)};\theta^{(t+1)})\right)\\
&\ge \sum_i \mathrm{ELBO}(x^{(i)};Q_i^{(t)},\theta^{(t)}) +\alpha\left(\sum_{i=1}^{\tilde m} \log p(\tilde x^{(i)},\tilde z^{(i)};\theta^{(t)})\right)\\
&= \ell_{\text{semi-sup}}(\theta^{(t)})
\end{aligned}
$$

the last $\ge$ is because 
$$
\theta^{(t+1)}:=\arg \max_\theta \left[ \sum_i \mathrm{ELBO}(x^{(i)};Q_i^{(t)},\theta) +\alpha\left(\sum_{i=1}^{\tilde m} \log p(\tilde x^{(i)},\tilde z^{(i)};\theta)\right)\right]
$$

### (b)

$$
\begin{aligned}
w_j^{(i)} &= Q_i(z^{(i)}=j)=P(z^{(i)}=j|x^{(i)};\phi,\mu,\Sigma)\\
&= \dfrac{P(x^{(i)}|z^{(i)}=j;\mu,\Sigma)P(z^{(i)}=j;\phi)}{\sum_{u=1}^k P(x^{(i)}|z^{(i)}=u;\mu,\Sigma)P(z^{(i)}=u;\phi)}\\
&= \dfrac{\frac{1}{(2\pi)^{d/2}|\Sigma_j|^{1/2}}\exp\left(-\frac{1}{2}(x^{(i)}-\mu_j)^T\Sigma^{-1}_j(x^{(i)}-\mu_j)\right)\phi_j}{\sum_{u=1}^k \frac{1}{(2\pi)^{d/2}|\Sigma_u|^{1/2}}\exp\left(-\frac{1}{2}(x^{(i)}-\mu_u)^T\Sigma^{-1}_u(x^{(i)}-\mu_u)\right)\phi_u}\\
&= \dfrac{\frac{1}{|\Sigma_j|^{1/2}}\exp\left(-\frac{1}{2}(x^{(i)}-\mu_j)^T\Sigma^{-1}_j(x^{(i)}-\mu_j)\right)\phi_j}{\sum_{u=1}^k \frac{1}{|\Sigma_u|^{1/2}}\exp\left(-\frac{1}{2}(x^{(i)}-\mu_u)^T\Sigma^{-1}_u(x^{(i)}-\mu_u)\right)\phi_u}
\end{aligned}
$$

### (c)

in M-Step, we should maximize:
$$
\ell_{\text{semi-sup}}(\theta^{(t+1)}) = \sum_i^m \sum_{j=1}^k w_j^{(i)} \log \frac{\frac{1}{(2\pi)^{d/2}\vert{}\Sigma_j\vert{}^{1/2}} \exp(-\frac{1}{2}(x^{(i)} - \mu_j)^T \Sigma_j^{-1} (x^{(i)} - \mu_j)) \cdot \phi_j}{w_j^{(i)}}+\alpha\left(\sum_{i=1}^{\tilde m} \log p(\tilde x^{(i)},\tilde z^{(i)};\theta^{(t+1)})\right)
$$
and we know
$$
\begin{aligned}
\alpha\sum_{i=1}^{\tilde m} \log p(\tilde x^{(i)},\tilde z^{(i)};\theta^{(t+1)}) &= \alpha\sum_{i=1}^{\tilde m} \log p(\tilde x^{(i)}|\tilde z^{(i)};\theta^{(t+1)})\phi_{\tilde z^{(i)}}\\
&= \alpha\sum_{i=1}^{\tilde m} \log\phi_{\tilde z^{(i)}}+\log \frac{1}{(2\pi)^{d/2}|\Sigma_{\tilde z^{(i)}}|^{1/2}}\exp\left(-\frac{1}{2}(\tilde x^{(i)}-\mu_{\tilde z^{(i)}})^T\Sigma^{-1}_{\tilde z^{(i)}}(\tilde x^{(i)}-\mu_{\tilde z^{(i)}})\right)\\
&= \alpha\sum_{i=1}^{\tilde m} \log\phi_{\tilde z^{(i)}} +\log \frac{1}{(2\pi)^{d/2}|\Sigma_{\tilde z^{(i)}}|^{1/2}}+\left(-\frac{1}{2}(\tilde x^{(i)}-\mu_{\tilde z^{(i)}})^T\Sigma^{-1}_{\tilde z^{(i)}}(\tilde x^{(i)}-\mu_{\tilde z^{(i)}})\right)
\end{aligned}
$$




for $\mu$:
$$
\begin{aligned}
\nabla_{\mu_l}\ell_{\text{semi-sup}}(\theta) &= \sum_{i=1}^m w_l^{(i)} (\Sigma^{-1}_l x^{(i)} -\Sigma^{-1}_l\mu_l) + \nabla_{\mu_l}\alpha\left(\sum_{i=1}^{\tilde m} \log p(\tilde x^{(i)}|\tilde z^{(i)};\theta)\phi_{\tilde z^{(i)}}\right)\\
&= \sum_{i=1}^m w_l^{(i)} (\Sigma^{-1}_l x^{(i)} -\Sigma^{-1}_l\mu_l) + \alpha \sum_{i=1}^{\tilde m} 1\{\tilde z^{(i)}=l\}(\Sigma^{-1}_l x^{(i)} -\Sigma^{-1}_l\mu_l)
\end{aligned}
$$
set it to zero:
$$
\begin{aligned}
\sum_{i=1}^m w_l^{(i)} \Sigma^{-1}_l x^{(i)} + \alpha \sum_{i=1}^{\tilde m} 1\{\tilde z^{(i)}=l\}\Sigma^{-1}_l x^{(i)} &= \sum_{i=1}^m w_l^{(i)}\Sigma^{-1}_l\mu_l +\alpha \sum_{i=1}^{\tilde m} 1\{\tilde z^{(i)}=l\}\Sigma^{-1}_l\mu_l\\
&= \mu_l\left(\sum_{i=1}^m w_l^{(i)}\Sigma^{-1}_l +\alpha \sum_{i=1}^{\tilde m} 1\{\tilde z^{(i)}=l\}\Sigma^{-1}_l\right)\\
\mu_l &= \dfrac{\sum_{i=1}^m w_l^{(i)} \Sigma^{-1}_l x^{(i)} + \alpha \sum_{i=1}^{\tilde m} 1\{\tilde z^{(i)}=l\}\Sigma^{-1}_l \tilde x^{(i)}}{\sum_{i=1}^m w_l^{(i)}\Sigma^{-1}_l +\alpha \sum_{i=1}^{\tilde m} 1\{\tilde z^{(i)}=l\}\Sigma^{-1}_l}\\
&= \dfrac{\sum_{i=1}^m w_l^{(i)}  x^{(i)} + \alpha \sum_{i=1}^{\tilde m} 1\{\tilde z^{(i)}=l\} \tilde x^{(i)}}{\sum_{i=1}^m w_l^{(i)} +\alpha \sum_{i=1}^{\tilde m} 1\{\tilde z^{(i)}=l\}}
\end{aligned}
$$


for $\phi$, find those related, we should maximize
$$
\begin{aligned}
\sum_{i=1}^m\sum_{j=1}^k w_j^{(i)}\log \phi_j + \alpha\sum_{i=1}^{\tilde m}\sum_{j=1}^k1\{\tilde z^{(i)}=j\} \log\phi_{j}
\end{aligned}
$$
subject to
$$
\sum_{j=1}^k \phi_j = 1
$$
construct Langrange:
$$
\mathcal L (\phi,\lambda) = \sum_{i=1}^m\sum_{j=1}^k w_j^{(i)}\log \phi_j + \alpha\sum_{i=1}^{\tilde m}\sum_{j=1}^k1\{\tilde z^{(i)}=j\} \log\phi_{j} + \lambda\left(\sum_{j=1}^k \phi_j-1\right)
$$

$$
\begin{aligned}
\dfrac{\partial}{\partial\phi_j}\mathcal L (\phi,\lambda) = \sum_{i=1}^m\frac{w_j^{(i)}}{\phi_j}  +\alpha\sum_{i=1}^{\tilde m} \dfrac{1\{\tilde z^{(i)}=j\}}{\phi_{j}}+ \lambda
\end{aligned}
$$

set to zero:
$$
\begin{aligned}
\phi_j = \dfrac{1}{\lambda}\left(\sum_{i=1}^m{w_j^{(i)}}  +\alpha\sum_{i=1}^{\tilde m} {1\{\tilde z^{(i)}=j\}}\right)
\end{aligned}
$$
by $\sum_j \phi_j = 1$:
$$
\begin{aligned}
\lambda = (m+\alpha\tilde m)
\end{aligned}
$$
we have
$$
\phi_j = \dfrac{1}{m+\alpha\tilde m}\left(\sum_{i=1}^m{w_j^{(i)}}  +\alpha\sum_{i=1}^{\tilde m} {1\{\tilde z^{(i)}=j\}}\right)
$$


for $\Sigma$, we have
$$
\begin{aligned}
t(l,x^{(i)})&:=\frac{1}{(2\pi)^{d/2}\vert{}\Sigma_l\vert{}^{1/2}} \exp\left(-\frac{1}{2}(x^{(i)} - \mu_l)^T \Sigma_l^{-1} (x^{(i)} - \mu_l)\right) \cdot \phi_l\\
\nabla_{\Sigma_l}\ell_{\text{semi-sup}}(\theta) &=\sum_{i=1}^m  w_l^{(i)} \left( -\dfrac{1}{2}\Sigma_l^{-1}  +\frac{1}{2}\Sigma_l^{-1}(x^{(i)} - \mu_l)(x^{(i)} - \mu_l)^T\Sigma_l^{-1}\right) + \alpha \sum_{i=1}^{\tilde m}  1\{\tilde z^{(i)}=l\} \left( -\dfrac{1}{2}\Sigma_l^{-1}  +\frac{1}{2}\Sigma_l^{-1}(\tilde x^{(i)} - \mu_l)(\tilde x^{(i)} - \mu_l)^T\Sigma_l^{-1}\right)
\end{aligned}
$$
set to zero:
$$
\begin{aligned}
\sum_{i=1}^m  w_l^{(i)}  + \alpha \sum_{i=1}^{\tilde m}  1\{\tilde z^{(i)}=l\} 
&=
\sum_{i=1}^m  w_l^{(i)} \left(  (x^{(i)} - \mu_l)(x^{(i)} - \mu_l)^T\Sigma_l^{-1}\right) + \alpha \sum_{i=1}^{\tilde m}  1\{\tilde z^{(i)}=l\} \left(  (\tilde x^{(i)} - \mu_l)(\tilde x^{(i)} - \mu_l)^T\Sigma_l^{-1}\right)\\

\left(\sum_{i=1}^m  w_l^{(i)}  + \alpha \sum_{i=1}^{\tilde m}  1\{\tilde z^{(i)}=l\}\right)\Sigma_l 
&=
\sum_{i=1}^m  w_l^{(i)} \left(  (x^{(i)} - \mu_l)(x^{(i)} - \mu_l)^T\right) + \alpha \sum_{i=1}^{\tilde m}  1\{\tilde z^{(i)}=l\} \left(  (\tilde x^{(i)} - \mu_l)(\tilde x^{(i)} - \mu_l)^T\right)\\
\Sigma_l &= \dfrac{\sum_{i=1}^m  w_l^{(i)} \left(  (x^{(i)} - \mu_l)(x^{(i)} - \mu_l)^T\right) + \alpha \sum_{i=1}^{\tilde m}  1\{\tilde z^{(i)}=l\} \left(  (\tilde x^{(i)} - \mu_l)(\tilde x^{(i)} - \mu_l)^T\right)}{\sum_{i=1}^m  w_l^{(i)}  + \alpha \sum_{i=1}^{\tilde m}  1\{\tilde z^{(i)}=l\}}
\end{aligned}
$$
in conclusion:
$$
\begin{aligned}
\mu_l^{(t+1)} &= \dfrac{\sum_{i=1}^m w_l^{(i)}  x^{(i)} + \alpha \sum_{i=1}^{\tilde m} 1\{\tilde z^{(i)}=l\} \tilde x^{(i)}}{\sum_{i=1}^m w_l^{(i)} +\alpha \sum_{i=1}^{\tilde m} 1\{\tilde z^{(i)}=l\}}\\
\Sigma_l^{(t+1)} &= \dfrac{\sum_{i=1}^m  w_l^{(i)} \left(  (x^{(i)} - \mu_l)(x^{(i)} - \mu_l)^T\right) + \alpha \sum_{i=1}^{\tilde m}  1\{\tilde z^{(i)}=l\} \left(  (\tilde x^{(i)} - \mu_l)(\tilde x^{(i)} - \mu_l)^T\right)}{\sum_{i=1}^m  w_l^{(i)}  + \alpha \sum_{i=1}^{\tilde m}  1\{\tilde z^{(i)}=l\}}\\
\phi_j^{(t+1)} &= \dfrac{1}{m+\alpha\tilde m}\left(\sum_{i=1}^m{w_j^{(i)}}  +\alpha\sum_{i=1}^{\tilde m} {1\{\tilde z^{(i)}=j\}}\right)
\end{aligned}
$$

### (f)

i. unsupervised takes about 150 iterations to converge, which is slower than semi-supervised that takes about 25 iterations to converge.

ii. unsupervised is very unstable, in different random initializations the assignments change a lot, while semi-supervised is very stable, the assignments don't change at all.

iii. 

unsupervised: low quality. it could split the high-variance distribution into two distributions or mix up two low-variance distributions.   
semi-supervised: high qualily. it figured out the three low-variance distributions and the the high-variance distribution correctly.

## Problem 5

original: $512\times 512 \times 24 = 6,291,456\ \mathrm{ bits}$

compressed(approximately): $512\times 512\times 4 = 1,048,576\ \mathrm{bits}$

Compression Factor is approximately $\dfrac{1}{6}$
