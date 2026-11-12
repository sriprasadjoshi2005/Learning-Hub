---
title: Capacitors and Capacitance
level: intermediate
---

# Capacitors and Capacitance

## Introduction

A capacitor is a passive electrical component that stores energy in an electric field. It consists of two conducting plates separated by an insulating material called a dielectric.

Capacitors are widely used in electronic circuits for filtering, timing, coupling, decoupling, energy storage, signal processing, and power conditioning.

Capacitance describes the ability of a capacitor to store electric charge for a given potential difference.

This lesson explores capacitor construction, capacitance, dielectric materials, series and parallel combinations, stored energy, charging and discharging behaviour, and practical capacitor applications.

## 1. Construction of a Capacitor

A basic capacitor consists of two conducting plates separated by an insulating material.

The insulating material is known as the dielectric.

```text
       Conducting plate
       ────────────────
            Dielectric
       ────────────────
       Conducting plate
```

When a voltage is applied across the plates:
- One plate accumulates positive charge.
- The other plate accumulates an equal magnitude of negative charge.
- An electric field develops between the plates.
- Electrical energy is stored in the electric field.

The dielectric prevents direct conduction between the plates under normal operating conditions.

## 2. Capacitance

Capacitance is defined as the ratio of the magnitude of charge stored on either plate to the potential difference between the plates.

\[
\boxed{C=\frac{Q}{V}}
\]

Where:
- \(C\) = capacitance in farads (F).
- \(Q\) = magnitude of charge in coulombs (C).
- \(V\) = voltage across the capacitor in volts (V).

One farad is the capacitance of a capacitor that stores one coulomb of charge when one volt is applied.

\[
1\text{ F}=1\text{ C/V}
\]

The farad is a large unit, so practical capacitors commonly use smaller units.

| Unit | Equivalent |
|---|---|
| Millifarad | \(1\text{ mF}=10^{-3}\text{ F}\) |
| Microfarad | \(1\ \mu\text{F}=10^{-6}\text{ F}\) |
| Nanofarad | \(1\text{ nF}=10^{-9}\text{ F}\) |
| Picofarad | \(1\text{ pF}=10^{-12}\text{ F}\) |

## 3. Factors Affecting Capacitance

For a parallel-plate capacitor:

\[
\boxed{C=\frac{\varepsilon A}{d}}
\]

Where:
- \(\varepsilon\) = permittivity of the dielectric.
- \(A\) = overlapping plate area.
- \(d\) = distance between the plates.

The permittivity is:

\[
\varepsilon=\varepsilon_0\varepsilon_r
\]

Where:
- \(\varepsilon_0\) = permittivity of free space.
- \(\varepsilon_r\) = relative permittivity of the dielectric.

### 3.1 Plate Area

Capacitance is directly proportional to plate area.

Increasing the overlapping area increases capacitance.

### 3.2 Plate Separation

Capacitance is inversely proportional to plate separation.

Reducing the distance between the plates increases capacitance.

### 3.3 Dielectric Material

A dielectric with a larger relative permittivity produces greater capacitance for the same geometry.

Different materials are selected according to operating voltage, temperature, frequency, size, and reliability requirements.

## 4. Dielectric Materials

A dielectric is an insulating material that becomes polarised when placed in an electric field.

Polarisation reduces the effective electric field inside the material for a given free charge and allows more charge to be stored at a given applied voltage.

Common dielectric materials include:

- Ceramic.
- Aluminium oxide.
- Tantalum oxide.
- Polyester film.
- Polypropylene.
- Mica.
- Paper.
- Air.

### 4.1 Dielectric Strength

Dielectric strength is the maximum electric field that an insulating material can withstand without electrical breakdown.

If the applied field exceeds the material's dielectric strength, the dielectric may conduct, become damaged, or fail permanently.

## 5. Types of Capacitors

### 5.1 Ceramic Capacitors

Ceramic capacitors use ceramic dielectric materials.

Characteristics:
- Small physical size.
- Widely available capacitance values.
- Commonly used for high-frequency bypassing and decoupling.
- Some types exhibit significant capacitance variation with voltage and temperature.

### 5.2 Electrolytic Capacitors

Electrolytic capacitors provide relatively large capacitance values.

Characteristics:
- Commonly used in power-supply filtering.
- Often polarised.
- Require correct terminal orientation.
- May have higher leakage current than many ceramic or film types.

### 5.3 Tantalum Capacitors

Tantalum capacitors provide relatively high capacitance in compact packages.

They are commonly used in portable electronics and power-management circuits.

Their voltage rating and surge-current limitations must be respected.

### 5.4 Film Capacitors

Film capacitors use thin plastic films as dielectrics.

Characteristics:
- Good stability.
- Low dielectric loss in suitable types.
- Useful in filtering, timing, and AC applications.

### 5.5 Variable Capacitors

Variable capacitors allow capacitance to be adjusted mechanically or electronically.

They are used in tuning circuits and frequency-selection systems.

## 6. Capacitors in Series

When capacitors are connected in series, the same magnitude of charge appears on each capacitor.

The total voltage equals the sum of individual capacitor voltages.

\[
V_T=V_1+V_2+\cdots+V_n
\]

Using:

\[
V=\frac{Q}{C}
\]

For two capacitors:

\[
\frac{Q}{C_T}=\frac{Q}{C_1}+\frac{Q}{C_2}
\]

Cancelling \(Q\):

\[
\boxed{\frac{1}{C_T}=\frac{1}{C_1}+\frac{1}{C_2}}
\]

For two capacitors:

\[
\boxed{C_T=\frac{C_1C_2}{C_1+C_2}}
\]

For \(n\) capacitors:

\[
\boxed{\frac{1}{C_T}=\sum_{i=1}^{n}\frac{1}{C_i}}
\]

The equivalent capacitance is smaller than the smallest individual capacitance.

## 7. Capacitors in Parallel

When capacitors are connected in parallel, the voltage across every capacitor is the same.

The total charge is the sum of individual charges.

\[
Q_T=Q_1+Q_2+\cdots+Q_n
\]

Using:

\[
Q=CV
\]

\[
C_TV=C_1V+C_2V+\cdots+C_nV
\]

Cancelling the common voltage:

\[
\boxed{C_T=C_1+C_2+\cdots+C_n}
\]

The equivalent capacitance is greater than any individual capacitance when multiple positive capacitances are connected in parallel.

## 8. Energy Stored in a Capacitor

A capacitor stores energy in its electric field.

The work required to charge a capacitor is:

\[
dW=V\,dq
\]

Since:

\[
V=\frac{q}{C}
\]

\[
dW=\frac{q}{C}dq
\]

Integrating from zero charge to final charge \(Q\):

\[
W=\int_0^Q\frac{q}{C}dq
\]

\[
W=\frac{1}{C}\left[\frac{q^2}{2}\right]_0^Q
\]

Therefore:

\[
\boxed{W=\frac{Q^2}{2C}}
\]

Using \(Q=CV\):

\[
\boxed{W=\frac12CV^2}
\]

Another form is:

\[
\boxed{W=\frac12QV}
\]

Where energy is measured in joules.

## 9. Current-Voltage Relationship of a Capacitor

The charge-voltage relationship is:

\[
Q=CV
\]

Current is the rate of change of charge:

\[
i=\frac{dQ}{dt}
\]

For a constant capacitance:

\[
\boxed{i=C\frac{dv}{dt}}
\]

This is one of the most important capacitor equations.

It shows that capacitor current depends on the rate of change of voltage.

### 9.1 Important Consequences

- A constant capacitor voltage produces zero ideal current.
- A rapidly changing voltage produces a larger current.
- An ideal capacitor does not allow its voltage to change instantaneously when current is finite.
- Capacitor current can change abruptly under ideal switching conditions.

## 10. Capacitor Behaviour in DC and AC Circuits

### 10.1 DC Steady State

In a DC circuit, after a capacitor has completely charged, its voltage becomes constant.

Therefore:

\[
\frac{dv}{dt}=0
\]

\[
\boxed{i=0}
\]

An ideal capacitor behaves as an open circuit under DC steady-state conditions.

During charging or discharging, however, current flows.

### 10.2 AC Behaviour

In an AC circuit, the capacitor continuously charges and discharges as the applied voltage changes.

Its opposition to AC is called capacitive reactance.

\[
\boxed{X_C=\frac{1}{2\pi fC}}
\]

Where:
- \(X_C\) = capacitive reactance in ohms.
- \(f\) = frequency in hertz.
- \(C\) = capacitance in farads.

As frequency increases, capacitive reactance decreases.

As capacitance increases, capacitive reactance decreases.

The ideal capacitor current leads its voltage by \(90^\circ\) in sinusoidal steady state.

## 11. Worked Numerical Examples

### Example 1: Calculating Capacitance

**Given:**

- Stored charge = 600 μC.
- Applied voltage = 12 V.

**Find:** Capacitance.

**Formula:**

\[
C=\frac{Q}{V}
\]

**Solution:**

\[
C=\frac{600\times10^{-6}}{12}
\]

\[
C=50\times10^{-6}\text{ F}
\]

\[
\boxed{C=50\ \mu\text{F}}
\]

### Example 2: Capacitors in Series

**Given:**

- \(C_1=6\ \mu\text{F}\)
- \(C_2=3\ \mu\text{F}\)

**Find:** Equivalent capacitance.

**Solution:**

\[
C_T=\frac{C_1C_2}{C_1+C_2}
\]

\[
C_T=\frac{6\times3}{6+3}
\]

\[
C_T=\frac{18}{9}
\]

\[
\boxed{C_T=2\ \mu\text{F}}
\]

### Example 3: Capacitors in Parallel

**Given:**

- \(C_1=4\ \mu\text{F}\)
- \(C_2=8\ \mu\text{F}\)
- \(C_3=12\ \mu\text{F}\)

**Find:** Equivalent capacitance.

**Solution:**

\[
C_T=4+8+12
\]

\[
\boxed{C_T=24\ \mu\text{F}}
\]

### Example 4: Energy Stored in a Capacitor

**Given:**

- Capacitance = 100 μF.
- Voltage = 20 V.

**Find:** Stored energy.

**Formula:**

\[
W=\frac12CV^2
\]

**Solution:**

\[
W=\frac12(100\times10^{-6})(20)^2
\]

\[
W=0.5\times100\times10^{-6}\times400
\]

\[
\boxed{W=0.02\text{ J}}
\]

### Example 5: Capacitive Reactance

**Given:**

- Frequency = 50 Hz.
- Capacitance = 100 μF.

**Find:** Capacitive reactance.

**Formula:**

\[
X_C=\frac{1}{2\pi fC}
\]

**Solution:**

\[
X_C=\frac{1}{2\pi(50)(100\times10^{-6})}
\]

\[
\boxed{X_C\approx31.83\ \Omega}
\]

## 12. Practical Applications

Capacitors are used in:

- Power-supply smoothing.
- Noise filtering.
- Signal coupling.
- Signal decoupling.
- Timing circuits.
- Oscillator circuits.
- Energy-storage systems.
- Camera flashes.
- Motor-starting circuits.
- Radio-frequency tuning.

### 12.1 Decoupling

A decoupling capacitor is placed near an integrated circuit's supply pins to provide local transient current and reduce supply-voltage disturbances.

### 12.2 Coupling

A coupling capacitor allows changing signals to pass between circuit stages while blocking steady DC components.

### 12.3 Filtering

Capacitors can attenuate or pass different frequency components depending on their reactance and circuit arrangement.

## 13. Important Comparisons and Observations

| Property | Series capacitors | Parallel capacitors |
|---|---|---|
| Common quantity | Charge | Voltage |
| Equivalent capacitance | Reciprocal sum | Direct sum |
| Equivalent value | Smaller than smallest capacitor | Larger than largest capacitor |
| Voltage distribution | Depends on capacitance | Equal |
| Charge distribution | Equal magnitude | Depends on capacitance |

Additional observations:

- Capacitance depends on plate geometry and dielectric material.
- A capacitor stores energy in an electric field.
- Capacitor current depends on the rate of change of voltage.
- Capacitive reactance decreases as frequency increases.
- Real capacitors have leakage, equivalent series resistance, and parasitic inductance.

## 14. Common Exam Traps

1. **Confusing series and parallel rules:** Series capacitors combine using reciprocal addition; parallel capacitors combine by direct addition.

2. **Forgetting unit conversion:** Microfarads must be converted to farads when calculating reactance using SI units.

3. **Using resistance instead of reactance:** Capacitors oppose AC through capacitive reactance.

4. **Incorrect energy formula:** The correct expression is \(W=\frac12CV^2\), not \(CV^2\).

5. **Assuming a capacitor always blocks current:** It blocks ideal steady DC after charging but allows current during voltage changes.

6. **Ignoring polarity:** Polarised capacitors must be connected with the correct polarity.

7. **Confusing current and voltage phase:** In an ideal capacitor, current leads voltage by \(90^\circ\).

## Quiz

1. A capacitor stores 400 μC of charge at a voltage of 20 V. What is its capacitance?

   - [ ] 10 μF
   - [x] 20 μF
   - [ ] 40 μF
   - [ ] 80 μF

   > Capacitance is \(C=Q/V=(400\times10^{-6})/20=20\times10^{-6}\) F, or 20 μF.

2. What happens to the capacitive reactance when the frequency of an AC supply increases while capacitance remains constant?

   - [ ] It increases.
   - [ ] It remains unchanged.
   - [x] It decreases.
   - [ ] It becomes infinite.

   > Capacitive reactance is \(X_C=1/(2\pi fC)\). It is inversely proportional to frequency, so increasing frequency reduces reactance.

3. Two identical capacitors are connected in series across a fixed DC voltage. Compared with connecting the same capacitors in parallel, what happens to their equivalent capacitance?

   - [ ] It becomes four times larger.
   - [ ] It remains unchanged.
   - [x] It becomes one-quarter of the parallel equivalent capacitance.
   - [ ] It becomes twice the parallel equivalent capacitance.

   > For two identical capacitors of capacitance C, the series equivalent is C/2, whereas the parallel equivalent is 2C. Their ratio is (C/2)/(2C)=1/4.