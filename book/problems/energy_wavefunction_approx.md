Below is a **markdown** version of the explanation, including mathematical typesetting with LaTeX syntax in code blocks.

---

# Why a Trial Wavefunction Close in Energy is An Accurate Approximation to the True Ground-State Wavefunction

(Adapted from ChatGPT's explanation.)

Assume we have:

- A nondegenerate ground state \(\lvert \psi_0 \rangle\) of a Hamiltonian \(H\) with energy \(E_0\).
- A complete orthonormal set of eigenstates \(\{\lvert \psi_n \rangle\}\) of \(H\), with eigenvalues \(E_n\) such that:
  \[
    H \lvert \psi_n \rangle = E_n \lvert \psi_n \rangle,
    \quad E_0 < E_1 \le E_2 \le \cdots
  \]
- A normalized trial wavefunction \(\lvert \psi_{\mathrm{trial}} \rangle\) with energy expectation \(E_{\mathrm{trial}}\):
  \[
    E_{\mathrm{trial}} = \langle \psi_{\mathrm{trial}} \lvert H \rvert \psi_{\mathrm{trial}} \rangle.
  \]

The variational principle states:
\[
  E_{\mathrm{trial}} \;\ge\; E_0.
\]

We will show that if \(E_{\mathrm{trial}}\) is very close to \(E_0\), then \(\lvert \psi_{\mathrm{trial}} \rangle\) must be very close to \(\lvert \psi_0 \rangle\) in the \(L^2\) (norm) sense.

---

## 1. Expansion in the Energy Eigenbasis

Any normalized \(\lvert \psi_{\mathrm{trial}} \rangle\) can be expanded in the basis \(\{\lvert \psi_n \rangle\}\) as

\[
\lvert \psi_{\mathrm{trial}} \rangle
= c_0 \lvert \psi_0 \rangle
  + c_1 \lvert \psi_1 \rangle
  + c_2 \lvert \psi_2 \rangle
  + \dots
\]

where the coefficients satisfy

\[
\sum_{n=0}^{\infty} |c_n|^2 = 1.
\]

---

## 2. The Variational Principle

From the variational principle, we know:

\[
E_{\mathrm{trial}}
= \langle \psi_{\mathrm{trial}} \lvert H \rvert \psi_{\mathrm{trial}} \rangle
\;\ge\; E_0.
\]

Define \(\epsilon = E_{\mathrm{trial}} - E_0 \ge 0\). Our goal is to relate \(\epsilon\) to the overlap \(|c_0|^2\) with the ground state.

---

## 3. Expressing \(E_{\mathrm{trial}}\) in the Eigenbasis

We can write:

\[
E_{\mathrm{trial}}
= \sum_{n=0}^\infty |c_n|^2 \, E_n
= |c_0|^2 E_0 + |c_1|^2 E_1 + |c_2|^2 E_2 + \cdots.
\]

Then,

\[
E_{\mathrm{trial}} - E_0
= \sum_{n=0}^\infty |c_n|^2 E_n \;-\; E_0
= |c_0|^2 E_0 + \sum_{n=1}^\infty |c_n|^2 E_n - E_0.
\]

Since \(\sum_{n=0}^\infty |c_n|^2 = 1\), we have:

\[
1 - |c_0|^2 = \sum_{n=1}^\infty |c_n|^2.
\]

Thus,

\[
E_{\mathrm{trial}} - E_0
= \sum_{n=1}^\infty |c_n|^2 (E_n - E_0)
\;\equiv\; \epsilon.
\]

---

## 4. Bounding the Overlap with the Ground State

Because \(E_n \ge E_1\) for all \(n \ge 1\) and \(E_1 > E_0\) (nondegenerate ground state implies a gap),

\[
E_n - E_0 \;\ge\; E_1 - E_0 > 0,
\quad \text{for all } n \ge 1.
\]

\[
\epsilon
= \sum_{n=1}^\infty |c_n|^2 (E_n - E_0)
\;\ge\; (E_1 - E_0) \sum_{n=1}^\infty |c_n|^2
= (E_1 - E_0) \bigl(1 - |c_0|^2\bigr).
\]

So

\[
1 - |c_0|^2
\;\le\; \frac{\epsilon}{E_1 - E_0}.
\]

Hence, if \(\epsilon\) is very small, then \(1 - |c_0|^2\) must also be small, implying \(|c_0|^2\) (the overlap squared with \(\lvert \psi_0 \rangle\)) is very close to 1.

---

## 5. Closeness in Norm

Since \(|c_0|^2 \to 1\), the sum of all \(|c_n|^2\) for \(n \ge 1\) goes to 0. Therefore,

\[
\|\psi_{\mathrm{trial}} - \psi_0\|^2
= 2 \bigl[1 - \Re\langle \psi_0 \mid \psi_{\mathrm{trial}} \rangle \bigr]
\]

is small because \(\langle \psi_0 \mid \psi_{\mathrm{trial}} \rangle = c_0^*\approx 1\). Concretely,

\[
\|\psi_{\mathrm{trial}} - \psi_0\|^2
= \bigl\|c_0 \lvert \psi_0 \rangle + \sum_{n=1}^\infty c_n \lvert \psi_n \rangle - \psi_0 \bigr\|^2
= \|\,(c_0 - 1)\,\psi_0 + \sum_{n=1}^\infty c_n \psi_n\|^2.
\]

\[
\text{As } |c_0|^2 \to 1 \quad (\text{i.e. } c_0 \to 1\ \text{up to a global phase}),
\quad \sum_{n=1}^\infty |c_n|^2 \to 0,
\]


so the norm difference goes to 0.

Thus, **closeness in energy** (\(E_{\mathrm{trial}} \approx E_0\)) **implies closeness in wavefunction** (\(\lvert \psi_{\mathrm{trial}} \rangle \approx \lvert \psi_0 \rangle\)) when the ground state is nondegenerate.

---

## Summary

1. **Expand** \(\lvert \psi_{\mathrm{trial}} \rangle\) in the eigenbasis.
2. **Use** the variational principle: \(E_{\mathrm{trial}} \ge E_0\).
3. **Relate** the energy gap \(\epsilon = E_{\mathrm{trial}} - E_0\) to \(\lvert c_0 \rvert^2\).
4. **Show** that a small \(\epsilon\) forces \(\lvert c_0 \rvert^2\approx 1\).
5. **Conclude** \(\lvert \psi_{\mathrm{trial}} \rangle\) is close in norm to \(\lvert \psi_0 \rangle\).

Hence, **getting an energy close to the exact ground-state energy ensures your trial wavefunction is also close (in the \(L^2\) sense) to the true ground-state wavefunction**, provided there is a nonzero energy gap between the ground state and the first excited state.