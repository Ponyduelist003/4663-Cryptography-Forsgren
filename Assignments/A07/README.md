## CMPS 4663 Cryptography Assignment 7 - Primality Lit Review
### Griffin Forsgren

### Algorithm 1 - Lucas-Lehmer Test
The Lucas-Lehmer Test is a deterministic test specifically used for Mersenne numbers, which is a number that can be written as 2<sup>n</sup> - 1 for some positive integer n. Specifically, Mersenne numbers can only be prime when the integer n is prime, thus giving us 2<sup>p</sup> - 1 for some prime number p. The Lucas-Lehmer test draws particular attention to the recurrence equation s<sub>n</sub> = s<sup>2</sup><sub>n-1</sub> - 2(mod M<sub>p</sub>) with s<sub>0</sub> = 4. As it turns out, M<sub>p</sub> is prime if and only if s<sub>p-2</sub> = 0 (mod M<sub>p</sub>)

Reference: https://mathworld.wolfram.com/Lucas-LehmerTest.html

### Algorithm 2 - Rabin-Miller Test
The Rabin-Miller Test is a compositeness test which takes an odd integer n, which we let be equal to 2<sup>r</sup>s + 1 with s being an odd number. We can then choose some integer a such that 1 <= a <= n - 1, and if a<sup>s</sup> is congruent to 1(mod n) or a<sup>2js</sup> is congruent to -1(mod n) for some j such that 0 <= j <= r - 1, then n passes. If n is prime, it will pass for all possible values of a. 

Reference: https://mathworld.wolfram.com/Rabin-MillerStrongPseudoprimeTest.html
