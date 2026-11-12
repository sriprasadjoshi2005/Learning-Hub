---
title: Electric Charge and Current
level: foundation
---

# Electric Charge and Current

Electric charge and electric current are the fundamental physical quantities behind every electronic circuit. Electronic devices operate by controlling the movement and distribution of charged particles, primarily electrons in metallic conductors and electrons and holes in semiconductors.

Understanding electric charge requires examining atomic structure, charge conservation, electrostatic interactions and the movement of charge carriers. Understanding electric current requires connecting the microscopic motion of particles to measurable circuit quantities.

This lesson explores the nature of electric charge, charging mechanisms, Coulomb's law, charge conservation, current direction, conventional current, electron flow, current density and charge-carrier drift. By the end, you will be able to calculate electrostatic forces, determine current from charge movement, analyse charge-carrier flow and distinguish conventional current from electron motion.

## 1. Electric Charge

### 1.1 Atomic Structure and Electric Charge

All ordinary matter consists of atoms containing:

- Protons: Positively charged particles in the nucleus.
- Neutrons: Electrically neutral particles in the nucleus.
- Electrons: Negatively charged particles surrounding the nucleus.

The magnitude of the elementary charge is:

$$e=1.602176634\times10^{-19}\text{ C}$$

Therefore:

$$q_p=+e$$

$$q_e=-e$$

An electrically neutral atom contains equal numbers of protons and electrons.

An atom becomes electrically charged when it gains or loses electrons.

- Losing electrons produces a positive ion.
- Gaining electrons produces a negative ion.

### 1.2 Properties of Electric Charge

Electric charge has several important properties.

**1. Two Types of Charge**

Like charges repel, while unlike charges attract.

**2. Additivity**

The total charge of a system is the algebraic sum of individual charges.

$$Q_{total}=\sum_i q_i$$

**3. Conservation**

Electric charge cannot be created or destroyed in an isolated system. It can be transferred between objects.

**4. Quantization**

Charge exists in discrete multiples of the elementary charge:

$$Q=ne$$

Where $n$ is an integer for an isolated system of ordinary charged particles.

### 1.3 Methods of Charging

Objects can become electrically charged through several mechanisms.

**Charging by Friction**

Rubbing two different materials may transfer electrons from one material to another.

**Charging by Conduction**

A charged object touches another object, allowing charge to transfer through physical contact.

**Charging by Induction**

A nearby charged object redistributes charge in another object without direct contact. Grounding can allow net charge transfer during this process.

## 2. Coulomb's Law

Coulomb's law describes the electrostatic force between two stationary point charges.

The magnitude of the force is:

$$F=k\frac{|q_1q_2|}{r^2}$$

Where:

- $F$ = electrostatic force in newtons.
- $q_1,q_2$ = charges in coulombs.
- $r$ = separation between charges in metres.
- $k$ = Coulomb's constant.

In vacuum:

$$k=\frac{1}{4\pi\varepsilon_0}$$

$$k\approx8.99\times10^9\text{ N m}^2/\text{C}^2$$

The permittivity of free space is:

$$\varepsilon_0\approx8.854\times10^{-12}\text{ F/m}$$

### 2.1 Nature of the Electrostatic Force

- If the charges have the same sign, the force is repulsive.
- If the charges have opposite signs, the force is attractive.

The force acts along the line joining the two charges.

### 2.2 Effect of Distance

Coulomb's force follows an inverse-square relationship.

$$F\propto\frac{1}{r^2}$$

If the distance doubles:

$$F_{new}=\frac{F_{old}}{4}$$

If the distance becomes three times larger:

$$F_{new}=\frac{F_{old}}{9}$$

## 3. Electric Current

### 3.1 Definition of Electric Current

Electric current is the rate of flow of electric charge through a cross-section of a conductor.

$$I=\frac{dQ}{dt}$$

For constant current:

$$I=\frac{Q}{t}$$

The SI unit is the ampere (A).

$$1\text{ A}=1\text{ C/s}$$

A current of 2 A means that 2 coulombs of charge pass through a given cross-section every second.

### 3.2 Conventional Current and Electron Flow

Two directions are commonly used when describing current.

**Conventional Current**

Conventional current is defined as the direction in which positive charge would move.

In a metallic conductor, it is opposite to the average electron drift direction.

**Electron Flow**

Electrons carry negative charge and drift in the direction opposite to conventional current.

Both descriptions are valid, provided the chosen convention is used consistently.

### 3.3 Current in Different Materials

The mobile charge carriers depend on the material.

| Material | Main Charge Carriers |
|---|---|
| Metals | Electrons |
| Intrinsic semiconductors | Electrons and holes |
| Doped semiconductors | Majority and minority carriers |
| Electrolytes | Positive and negative ions |
| Ionized gases | Electrons and ions |

This distinction becomes particularly important when studying semiconductor devices.

## 4. Microscopic View of Electric Current

### 4.1 Drift Velocity

When an electric field is applied across a conductor, charge carriers acquire an average directed velocity called drift velocity.

In a metal, electrons drift opposite to the applied electric field.

Although their drift speed may be relatively small, electrical signals in circuits propagate through electromagnetic interactions much faster than individual electrons drift.

### 4.2 Current Density

Current density describes current flowing per unit cross-sectional area.

$$J=\frac{I}{A}$$

Where:

- $J$ = current density in A/m².
- $I$ = current in amperes.
- $A$ = cross-sectional area in m².

For a uniform current distribution:

$$I=JA$$

Current density is a vector quantity whose direction follows conventional current.

### 4.3 Current and Charge Carrier Density

For a conductor containing mobile charge carriers:

$$I=nqAv_d$$

Where:

- $n$ = number of charge carriers per unit volume in m$^{-3}$.
- $q$ = magnitude of charge per carrier in coulombs.
- $A$ = cross-sectional area in m².
- $v_d$ = magnitude of drift velocity in m/s.

For electron conduction, the conventional current direction is opposite to electron drift.

This relationship connects microscopic charge motion to measurable current.

### 4.4 Current in Terms of Charge Flow

If $N$ electrons cross a conductor's cross-section in time $t$, the magnitude of transferred charge is:

$$Q=Ne$$

Therefore:

$$I=\frac{Ne}{t}$$

This expression is useful when analysing the number of charge carriers involved in electronic conduction.

## 5. Types of Electric Current

### 5.1 Direct Current

Direct current (DC) maintains one direction of conventional current flow.

Its magnitude may be constant or vary with time while retaining the same direction.

Examples:

- Battery-powered circuits.
- DC power supplies.
- Many electronic control circuits.

For ideal constant DC:

$$i(t)=I_0$$

### 5.2 Alternating Current

Alternating current (AC) periodically reverses its direction.

A sinusoidal AC current can be represented as:

$$i(t)=I_m\sin(2\pi ft+\phi)$$

Where:

- $I_m$ = peak current.
- $f$ = frequency.
- $\phi$ = phase angle.

For a sinusoidal current:

$$I_{rms}=\frac{I_m}{\sqrt{2}}$$

RMS current is particularly useful because it represents the equivalent DC heating effect in a resistor.

### 5.3 Pulsating Direct Current

Pulsating DC flows in one direction but varies in magnitude.

It is commonly produced by rectifier circuits before filtering.

## 6. Mathematical Derivations and Numerical Examples

### Example 1: Coulomb's Law

**Given:**

Two point charges are separated by 0.20 m in vacuum.

- $q_1=+4\ \mu\text{C}$
- $q_2=-6\ \mu\text{C}$
- $r=0.20\text{ m}$

Determine the magnitude and nature of the electrostatic force.

**Formula:**

$$F=k\frac{|q_1q_2|}{r^2}$$

**Solution:**

1. Convert charges:

   $$q_1=4\times10^{-6}\text{ C}$$

   $$q_2=6\times10^{-6}\text{ C}$$

2. Substitute:

   $$F=8.99\times10^9\frac{(4\times10^{-6})(6\times10^{-6})}{(0.20)^2}$$

3. Multiply the charges:

   $$|q_1q_2|=24\times10^{-12}\text{ C}^2$$

4. Square the distance:

   $$r^2=0.04\text{ m}^2$$

5. Calculate:

   $$F=\frac{8.99\times10^9\times24\times10^{-12}}{0.04}$$

   $$F=5.394\text{ N}$$

**Final Answer:**

The electrostatic force has a magnitude of approximately **5.39 N** and is **attractive**, because the charges have opposite signs.

### Example 2: Current from Electron Flow

**Given:**

An electronic conductor carries $3.0\times10^{19}$ electrons through a cross-section in 2 seconds.

Determine the magnitude of the conventional current.

**Formula:**

$$I=\frac{Ne}{t}$$

**Solution:**

1. Number of electrons:

   $$N=3.0\times10^{19}$$

2. Elementary charge:

   $$e=1.602\times10^{-19}\text{ C}$$

3. Time:

   $$t=2\text{ s}$$

4. Calculate transferred charge:

   $$Q=Ne$$

   $$Q=(3.0\times10^{19})(1.602\times10^{-19})$$

   $$Q=4.806\text{ C}$$

5. Calculate current:

   $$I=\frac{4.806}{2}$$

   $$I=2.403\text{ A}$$

**Final Answer:**

The magnitude of conventional current is approximately **2.40 A**. Its direction is opposite to the average electron drift direction.

### Example 3: Drift Velocity in a Metallic Conductor

**Given:**

A copper conductor carries 5 A.

- Cross-sectional area, $A=1.0\text{ mm}^2$
- Free-electron density, $n=8.5\times10^{28}\text{ m}^{-3}$
- Electron charge magnitude, $e=1.602\times10^{-19}\text{ C}$

Determine the magnitude of electron drift velocity.

**Formula:**

$$I=neAv_d$$

Rearranging:

$$v_d=\frac{I}{neA}$$

**Solution:**

1. Convert cross-sectional area:

   $$A=1.0\times10^{-6}\text{ m}^2$$

2. Substitute:

   $$v_d=\frac{5}{(8.5\times10^{28})(1.602\times10^{-19})(1.0\times10^{-6})}$$

3. Calculate the denominator:

   $$neA=1.3617\times10^4$$

4. Determine drift velocity:

   $$v_d=\frac{5}{1.3617\times10^4}$$

   $$v_d\approx3.67\times10^{-4}\text{ m/s}$$

**Final Answer:**

The magnitude of electron drift velocity is approximately **0.367 mm/s**.

The average electron drift direction is opposite to conventional current.

## 7. Practical Applications

### 7.1 Electrostatic Protection

Electronic manufacturing environments use electrostatic discharge (ESD) protection to prevent static charge from damaging sensitive semiconductor components.

Grounding straps, conductive work surfaces and antistatic packaging help control unwanted charge accumulation.

### 7.2 Semiconductor Devices

Diodes and transistors operate through controlled movement of electrons and holes.

Understanding charge-carrier behaviour is essential for analysing PN junctions and transistor operation.

### 7.3 Battery-Powered Circuits

Battery current depends on the connected load and available voltage.

Current calculations are used to estimate battery operating time and select suitable conductors and protection devices.

### 7.4 Current Measurement

Ammeters and current sensors measure charge flow through a circuit.

An ammeter is generally connected in series with the circuit branch being measured.

### 7.5 Electrostatic Sensors

Capacitive touchscreens and proximity sensors use changes in electric charge distribution and capacitance to detect objects or human touch.

## 8. Important Comparisons and Observations

### 8.1 Conventional Current and Electron Flow

| Characteristic | Conventional Current | Electron Flow |
|---|---|---|
| Direction | Positive-charge direction | Electron drift direction |
| Charge convention | Positive | Negative |
| In metallic conductors | Direction of current | Opposite to current |
| Circuit analysis | Standard engineering convention | Useful for microscopic explanations |

### 8.2 DC and AC

| Characteristic | DC | AC |
|---|---|---|
| Direction | Does not periodically reverse | Periodically reverses |
| Frequency | Zero for constant DC | Nonzero for periodic AC |
| Common source | Battery | Alternator or inverter |
| Common application | Electronic circuits | Power distribution and AC systems |

### 8.3 Important Observations

1. Electric charge is conserved.
2. Current is the rate of charge transfer.
3. Conventional current direction is opposite to electron drift in metals.
4. Current density depends on both current and conductor cross-sectional area.
5. Drift velocity is not the same as the propagation speed of an electrical signal.
6. Different materials contain different charge carriers.
7. AC and DC describe current behaviour, not simply whether its magnitude is constant.

## 9. Common Exam Traps

- **Confusing electron flow with conventional current:** In metals, they have opposite directions.
- **Forgetting the inverse-square relationship:** Doubling the separation between two point charges reduces Coulomb force to one-quarter.
- **Ignoring charge signs:** Signs determine attraction or repulsion, while absolute values are used to calculate force magnitude.
- **Confusing drift velocity with signal propagation:** Individual electrons drift relatively slowly even though electrical signals propagate much faster.
- **Using the wrong area units:** Convert mm² into m² before calculating current density or drift velocity.
- **Confusing current density and current:** Current is measured in amperes, while current density is measured in A/m².
- **Assuming all charge carriers are electrons:** Semiconductor conduction involves both electrons and holes.

## Quiz

1. Two point charges of $+3\ \mu\text{C}$ and $-8\ \mu\text{C}$ are separated by 0.30 m in vacuum. What is the approximate electrostatic force magnitude?

   - [ ] 0.80 N
   - [x] 2.40 N
   - [ ] 7.19 N
   - [ ] 24.0 N

   > Using Coulomb's law, $F=k|q_1q_2|/r^2$. Substituting gives $F=(8.99\times10^9)(24\times10^{-12})/(0.09)\approx2.40\text{ N}$. The force is attractive because the charges have opposite signs.

2. In a metallic conductor, electrons drift from the negative terminal toward the positive terminal of a DC source. What is the direction of conventional current?

   - [ ] In the same direction as electron drift.
   - [x] Opposite to electron drift.
   - [ ] Perpendicular to electron drift.
   - [ ] Conventional current has no defined direction.

   > Conventional current is defined as the direction of positive charge movement. Since electrons are negatively charged, their drift direction is opposite to conventional current.

3. A conductor carries a constant current of 4 A. Its cross-sectional area is reduced to half while the current remains unchanged. Assuming uniform current distribution, what happens to its current density?

   - [ ] It becomes half.
   - [ ] It remains unchanged.
   - [x] It doubles.
   - [ ] It becomes four times larger.

   > Current density is $J=I/A$. If the current remains constant while the cross-sectional area becomes $A/2$, the new density is $J'=I/(A/2)=2I/A=2J$. Therefore, current density doubles.
