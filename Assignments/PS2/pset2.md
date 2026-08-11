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
