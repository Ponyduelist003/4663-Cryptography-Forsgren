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
AKS is a Deterministic Probability test with the following algorithm. First, check if your number is a perfect power, or a number n such that n = a<sup>b</sup> for positive integers a and b. If so, it is composite. Then, find the smallest r coprime to n such that ord<sub>r</sub>(n) > (log<sub>2</sub>n)<sup>2</sup>. Then, for all a where 2 <= a <= min(r, n - 1), check that a does not divide n. If it does, n is composite. If n <= r, n is prime. For a from 1 to ![equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/66e8f8e1f842f93eeafb29da46bd297fd6accdbc), if for any such a it holds that (X + a)<sup>n</sup> != X<sup>n</sup> + a (mod X<sup>r</sup> - 1, n), n is composite. Otherwise, it is prime. 

Reference: https://en.wikipedia.org/wiki/AKS_primality_test

### Algorithm 5 - Solovay-Strassen Primality Test
Solovay-Strassen is a compositeness primality test which makes use of the Jacobi Symbol, an operation on a/n with some odd n and a < n where for each factor p<sub>k</sub> of n, we raise the Legendre symbol of a and p<sub>k</sub> (0 if a = 0 (mod p<sub>k</sub>), 1 if it isn't but a = x<sup>2</sup> (mod p<sub>k</sub>) for some integer x, and -1 if neither of the previous two conditions hold) to the power of p<sub>k</sub> present in n, and then multiply all the results. If a<sup>(n-1)/2</sup> is not congruent to the Jacobi Symbol of a and n (mod n) then n is composite and a is a witness. If not, n may be prime.

References: https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test

https://en.wikipedia.org/wiki/Jacobi_symbol

### Algorithm 6 - Bailie-PSW test 
Bailie-PSW is a probabilistic test where, after checking for small prime factors and determining a number to be a strong probable prime, we then find the first D in the sequence 5, -7, 9, -11, 13, -15,... for which the Jacobi Symbol of D/n is 1. Let P = 1 and Q = (1 - D)/4. We then perform a Lucas Psuedoprime test, factoring n + 1 into the form d * 2<sup>s</sup> for some odd number d. If we can find that U<sub>d</sub> = 0 (mod n) or that V<sub>d * 2<sup>r</sup></sub> = 0 (mod n) for the Lucas Sequence explained in references, then n is a Strong Lucas Pseudoprime and passes the test. 

References: https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test

https://en.wikipedia.org/wiki/Lucas_pseudoprime

https://en.wikipedia.org/wiki/Lucas_sequence

### Algorithm 7 -
