### Algorithm 1 - Lucas-Lehmer Test
The Lucas-Lehmer Test is a test specifically used for Mersenne numbers, which is a number that can be written as 2<sup>n</sup> - 1 for some positive integer n. Specifically, Mersenne numbers can only be prime when the integer n is prime, thus giving us 2<sup>p</sup> - 1 for some prime number p. The Lucas-Lehmer test draws particular attention to the recurrence equation s<sub>n</sub> = s<sup>2</sup><sub>n-1</sub> - 2(mod M<sub>p</sub>) with s<sub>0</sub> = 4. As it turns out, M<sub>p</sub> is prime if and only if s<sub>p-2</sub> = 0 (mod M<sub>p</sub>)

Reference: https://mathworld.wolfram.com/Lucas-LehmerTest.html

### Algorithm 2 - 
