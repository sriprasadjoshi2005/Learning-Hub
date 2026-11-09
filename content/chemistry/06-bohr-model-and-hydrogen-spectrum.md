---
title: Bohr Model and the Hydrogen Spectrum
level: foundation
---

Bohr's model (1913) explained why hydrogen emits only certain wavelengths. Its postulates:

- Electrons move in fixed circular orbits without radiating energy.
- Angular momentum is quantised: $mvr = n\hbar$ with $n = 1, 2, 3, \dots$
- Light is emitted or absorbed only when an electron jumps between orbits, with $\Delta E = h\nu$.

For a hydrogen-like species (one electron, nuclear charge $Z$):

$$E_n = -13.6\,\frac{Z^2}{n^2}\ \text{eV} \qquad r_n = 0.529\,\frac{n^2}{Z}\ \text{\AA}$$

Energy is negative because the electron is bound; it rises toward zero as $n \to \infty$. The ionisation energy from the ground state is therefore $13.6\,Z^2$ eV.

## Spectral series

When an electron falls from level $n_2$ to $n_1$, the wavenumber of the emitted light is

$$\frac{1}{\lambda} = R\,Z^2\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right), \qquad R = 1.097\times10^{7}\ \text{m}^{-1}.$$

| Series | Ends at $n_1$ | Region |
|---|---|---|
| Lyman | 1 | Ultraviolet |
| Balmer | 2 | Visible |
| Paschen | 3 | Infrared |

Within a series the **longest** wavelength is the jump between adjacent levels ($n_2 = n_1+1$); the **shortest** is the series limit ($n_2 = \infty$).

## Counting lines

An atom excited to level $n$ can return to the ground state by many routes. In a large sample, every possible jump occurs, so the number of distinct lines is $\dfrac{n(n-1)}{2}$.

## Limits of the model

Bohr's model works only for one-electron species. It cannot explain multi-electron spectra, fine structure, or the Zeeman effect, and it conflicts with the uncertainty principle, since it assigns an electron an exact orbit. These failures led to the quantum mechanical model.

## Quiz

1. What is the wavelength of the longest-wavelength line in the Balmer series of hydrogen? ($R=1.097\times10^7$ m$^{-1}$)
   - [ ] 486 nm
   - [ ] 365 nm
   - [ ] 122 nm
   - [x] 656 nm
   > The longest Balmer line is $n=3\to2$: $1/\lambda = 1.097\times10^7(1/4-1/9)=1.524\times10^6$ m$^{-1}$, so $\lambda=656$ nm. 486 nm is $4\to2$, 365 nm is the series limit, and 122 nm belongs to the Lyman series.

2. What is the energy needed to remove the electron from a ground-state $\mathrm{He^+}$ ion?
   - [ ] 13.6 eV
   - [ ] 27.2 eV
   - [x] 54.4 eV
   - [ ] 108.8 eV
   > $E_1 = -13.6\,Z^2/n^2 = -13.6\times4 = -54.4$ eV for $Z=2$, $n=1$. The ionisation energy is the magnitude, 54.4 eV.

3. A sample of hydrogen atoms is excited to the $n=5$ level. What is the maximum number of different spectral lines that can be emitted as the atoms return to $n=1$?
   - [ ] 4
   - [x] 10
   - [ ] 6
   - [ ] 15
   > $n(n-1)/2 = 5\times4/2 = 10$. The four lines of the Lyman series alone ($5\to1$, $4\to1$, $3\to1$, $2\to1$) are just a part of this, because transitions between excited levels also count.
