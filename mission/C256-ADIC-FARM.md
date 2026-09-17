# CEREBRON OMEGA — COLLATZ 3-ADIC FARM — CHECKPOINT 2026-09-17

MISSION: exploit exact 3-adic constraints in the H-factorized binary-run system. Do not restart; do not treat finite search as proof.

Exact state:
- 3^{u}t-1=4^{r}h, with h odd, h≡5 mod6.
- Address: h≡-4^{-r} (mod 3^u).
- ord_{3^u}(4)=3^{u-1}; for fixed h, r≡rho_u(h) (mod 3^{u-1}).
- Lifting: rho_{u+1}=rho_u+k_u3^{u-1}, where k_u is determined by Q_u(h)=(h4^{rho_u}+1)/3^u modulo 3.
- H-COUPLING between adjacent runs and H-LOG exact identity are active constraints.
- Example exception: h=5,r=2 survives through u=4; then at u=5 the admissible class jumps strongly.

Primary target: prove a collective small-h exception budget. Quantify when small h forces large r, and when exceptional v3(h4^r+1) can delay that cost. Seek a theorem over the full cycle, not isolated pairs.

Mandatory: h=5,11,17,23,29; u=1.. relevant lifts; exceptional valuations; compatibility with the next run via H-COUPLING.

Do not assume 'large u => large h'. Search for counterexamples first.

ARITHMETIC COMPRESSION: SYMBOLIC REDUCTION BEFORE MULTIPLICATION. Reuse rho_u, Q_u, modular powers and lifted residues; never brute-force r when a lifted congruence exists; filter modulo 3^u before big integers. Report COST BEFORE / TRANSFORMATION / COST AFTER / EQUIVALENCE CHECK / SAVED MULTIPLICATIONS.

Output: VERIFIED LEMMAS / EXCEPTIONS / COUNTEREXAMPLES / COLLECTIVE BOUND CANDIDATE / RESIDUAL / NEXTLOCK / STATUS.