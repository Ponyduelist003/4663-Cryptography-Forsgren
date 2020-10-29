## CMPS 4663 Cryptography Assignment 7 - Primality Lit Review
### Griffin Forsgren

### Algorithm 1 - Lucas-Lehmer Test
The Lucas-Lehmer Test is a deterministic test specifically used for Mersenne numbers, which is a number that can be written as 2<sup>n</sup> - 1 for some positive integer n. Specifically, Mersenne numbers can only be prime when the integer n is prime, thus giving us 2<sup>p</sup> - 1 for some prime number p. The Lucas-Lehmer test draws particular attention to the recurrence equation s<sub>n</sub> = s<sup>2</sup><sub>n-1</sub> - 2(mod M<sub>p</sub>) with s<sub>0</sub> = 4. As it turns out, M<sub>p</sub> is prime if and only if s<sub>p-2</sub> = 0 (mod M<sub>p</sub>)

Reference: https://mathworld.wolfram.com/Lucas-LehmerTest.html

### Algorithm 2 - Rabin-Miller Test
The Rabin-Miller Test is a compositeness test which takes an odd integer n, which we let be equal to 2<sup>r</sup>s + 1 with s being an odd number. We can then choose some integer a such that 1 <= a <= n - 1, and if a<sup>s</sup> is congruent to 1(mod n) or a<sup>2js</sup> is congruent to -1(mod n) for some j such that 0 <= j <= r - 1, then n passes. If n is prime, it will pass for all possible values of a. 

Reference: https://mathworld.wolfram.com/Rabin-MillerStrongPseudoprimeTest.html

### Algorithm 3 - Lucas Primality Certificate
The Lucas Primality test is a certification test that says, for any integer n, if there exists a where 1 < a < n such that a<sup>n - 1</sup> is congruent to 1 (mod n) and for every prime factor q of n - 1 it holds that a<sup>(n - 1)/q</sup> is not congruent to 1 (mod n), then n is prime. Otherwise, n is either 1, 2, or composite. 

Reference: https://en.wikipedia.org/wiki/Lucas_primality_test

### Algorithm 4 - AKS Primality Test
AKS is a Deterministic Probability test with the following algorithm. First, check if your number is a perfect power, or a number n such that n = a<sup>b</sup> for positive integers a and b. If so, it is composite. Then, find the smallest r coprime to n such that ord<sub>r</sub>(n) > (log<sub>2</sub>n)<sup>2</sup>. Then, for all a where 2 <= a <= min(r, n - 1), check that a does not divide n. If it does, n is composite. If n <= r, n is prime. For a from 1 to 

Reference: https://en.wikipedia.org/wiki/AKS_primality_test
