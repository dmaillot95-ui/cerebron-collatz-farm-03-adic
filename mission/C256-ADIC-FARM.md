# C256 — ADIC FARM

Objective: determine whether balanced/mechanical exponent words can satisfy simultaneously the real first-return window and the 2-adic/3-adic endpoint congruence constraints for arbitrarily large lengths.

Accelerated odd Collatz:
T(x_i)=(3x_i+1)/2^{a_i}, a_i=v2(3x_i+1)>=1.
For a finite word a_0,...,a_{n-1}, A_k=sum_{i<k}a_i and
x_k=(3^k x_0+C_k)/2^{A_k}, C_0=0, C_{k+1}=3C_k+2^{A_k}.

Known checkpoint:
- every finite positive valuation word is locally realizable by infinitely many positive odd finite trajectories;
- pure symbolic transition graph is complete;
- multiplier-only contraction is insufficient;
- for a fixed word, if the real feasible interval I_W(X) has width c_W X+O(1) with c_W>0, then its intersection with one fixed 2-adic cylinder is eventually nonempty for large X;
- therefore the next lock is joint REAL + 2-ADIC + 3-ADIC compatibility, not 2-adic compatibility alone.

Tasks:
1. derive exact 2-adic cylinder for x_0 induced by the valuation word;
2. derive exact endpoint congruence modulo 3^n and any stronger 3-adic restrictions;
3. combine both via CRT where coprime moduli apply, but do not confuse local CRT solvability with a valid Collatz episode;
4. couple these congruences to the real first-return interval and exact positivity/oddness conditions;
5. test whether balanced/Sturmian words force normalized adic residue rates away from zero, or whether arbitrarily long compatible families exist;
6. search for a rigorous contradiction or a rigorous no-go theorem against this route;
7. distinguish PROVED / REFUTED / HOLD / EXPERIMENTAL.

No agent may claim CYCLES CLOSED without a complete arbitrary-N contradiction.
