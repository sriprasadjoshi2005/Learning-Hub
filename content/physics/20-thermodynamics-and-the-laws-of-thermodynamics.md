---
title: Thermodynamics and the Laws of Thermodynamics
level: intermediate
---

Thermodynamics studies heat, work, temperature, and internal energy, together with the transformations between these quantities.

It provides the theoretical foundation for engines, refrigerators, power plants, chemical processes, and many natural phenomena.

The laws of thermodynamics describe energy conservation, the direction of spontaneous processes, and the limits of energy conversion.

## 1. Thermodynamic Systems

A thermodynamic system is the part of the physical world selected for study.

Everything outside the system is called its surroundings.

The boundary separates the system from its surroundings.

Types of systems:

**Open system:** Exchanges both matter and energy with its surroundings.

**Closed system:** Exchanges energy but not matter.

**Isolated system:** Exchanges neither matter nor energy.

Examples:
- Boiling water in an uncovered pot: approximately an open system.
- Gas in a sealed piston-cylinder: a closed system.
- An ideal perfectly insulated sealed container: an isolated system.

## 2. Thermodynamic State Variables

A thermodynamic state is described by measurable properties called state variables.

Important variables include:
- Pressure (P).
- Volume (V).
- Temperature (T).
- Internal energy (U).
- Entropy (S).

State variables depend on the current equilibrium state, not on the path used to reach it.

Heat and work are different: they describe energy transfer during a process rather than properties stored as state variables.

## 3. Internal Energy

Internal energy is the total microscopic energy associated with the particles of a system.

It includes contributions from:
- Molecular kinetic energy.
- Molecular potential energy.
- Rotational and vibrational energy.
- Intermolecular interactions.

For an ideal gas, internal energy depends only on temperature.

For a monatomic ideal gas:

\[
U=\frac{3}{2}nRT
\]

A change in internal energy is a change in the system's microscopic energy.

## 4. Thermodynamic Work

When a gas expands or compresses against an external pressure, work is transferred.

For a quasistatic process:

\[
W_{\text{by}}=\int_{V_1}^{V_2}P\,dV
\]

Here W_by is the work done by the system.

For constant pressure:

\[
W_{\text{by}}=P(V_2-V_1)
\]

Expansion gives positive work by the gas.

Compression gives negative work by the gas.

The area under a pressure-volume graph represents the work done by the system.

## 5. First Law of Thermodynamics

The first law expresses conservation of energy in thermodynamic processes.

Using the convention that W_by is work done by the system:

\[
\Delta U=Q-W_{\text{by}}
\]

Where:
- delta U = change in internal energy
- Q = heat supplied to the system
- W_by = work done by the system

If heat enters the system, Q is positive.

If the system does work on its surroundings, W_by is positive.

The first law does not determine whether a process will occur spontaneously. It only accounts for energy conservation.

## 6. Thermodynamic Processes

### Isothermal Process

An isothermal process occurs at constant temperature.

\[
\Delta T=0
\]

For an ideal gas:

\[
\Delta U=0
\]

Therefore:

\[
Q=W_{\text{by}}
\]

For reversible isothermal expansion of an ideal gas:

\[
W_{\text{by}}=nRT\ln\left(\frac{V_2}{V_1}\right)
\]

### Adiabatic Process

An adiabatic process occurs without heat transfer.

\[
Q=0
\]

Therefore:

\[
\Delta U=-W_{\text{by}}
\]

For a reversible adiabatic ideal-gas process:

\[
PV^\gamma=\text{constant}
\]

Where gamma is the ratio of heat capacities:

\[
\gamma=\frac{C_P}{C_V}
\]

### Isobaric Process

An isobaric process occurs at constant pressure.

\[
W_{\text{by}}=P\Delta V
\]

### Isochoric Process

An isochoric process occurs at constant volume.

\[
\Delta V=0
\]

Therefore:

\[
W_{\text{by}}=0
\]

The first law becomes:

\[
\Delta U=Q
\]

## 7. Heat Capacities of Gases

The molar heat capacity at constant volume is:

\[
C_V=\frac{1}{n}\left(\frac{Q}{\Delta T}\right)_V
\]

The molar heat capacity at constant pressure is:

\[
C_P=\frac{1}{n}\left(\frac{Q}{\Delta T}\right)_P
\]

For an ideal gas:

\[
C_P-C_V=R
\]

This is Mayer's relation.

For a monatomic ideal gas:

\[
C_V=\frac{3}{2}R
\]

\[
C_P=\frac{5}{2}R
\]

## 8. Second Law of Thermodynamics

The second law establishes the preferred direction of natural processes.

It can be expressed in several equivalent ways.

**Clausius statement:** Heat does not spontaneously flow from a colder body to a hotter body without external work.

**Kelvin-Planck statement:** No cyclic heat engine can convert all the heat absorbed from a single reservoir completely into work.

The second law explains why real energy conversions have limitations.

## 9. Entropy

Entropy is a thermodynamic state function associated with the distribution of energy and the number of accessible microscopic arrangements.

For a reversible process:

\[
dS=\frac{\delta Q_{\text{rev}}}{T}
\]

For a reversible finite-temperature change:

\[
\Delta S=\int\frac{\delta Q_{\text{rev}}}{T}
\]

For an isolated system:

\[
\Delta S_{\text{total}}\geq0
\]

Entropy remains constant for an ideal reversible process and increases for an irreversible process.

Entropy is measured in J/K.

The second law is often expressed through the principle that the total entropy of an isolated system cannot decrease.

## 10. Heat Engines

A heat engine operates in a cycle and converts part of the heat absorbed from a hot reservoir into work.

It:
1. Absorbs heat QH.
2. Performs work W.
3. Rejects heat QC to a colder reservoir.

Energy conservation gives:

\[
W=Q_H-Q_C
\]

Thermal efficiency is:

\[
\eta=\frac{W}{Q_H}
\]

Therefore:

\[
\eta=1-\frac{Q_C}{Q_H}
\]

A real heat engine cannot convert all absorbed heat into useful work.

## 11. Carnot Engine

A Carnot engine is an ideal reversible heat engine operating between two thermal reservoirs.

Its maximum possible efficiency is:

\[
\eta_C=1-\frac{T_C}{T_H}
\]

Where temperatures are measured in kelvin.

No engine operating between the same two reservoirs can be more efficient than a Carnot engine.

Real engines have lower efficiencies because of irreversibilities.

## 12. Refrigerators and Heat Pumps

A refrigerator uses external work to transfer heat from a colder region to a warmer region.

Its coefficient of performance is:

\[
COP_R=\frac{Q_C}{W}
\]

A heat pump is designed to provide heating.

\[
COP_{HP}=\frac{Q_H}{W}
\]

Since:

\[
Q_H=Q_C+W
\]

For the same operating cycle:

\[
COP_{HP}=COP_R+1
\]

The coefficient of performance is not the same as thermal efficiency.

## 13. Third Law of Thermodynamics

The third law states that the entropy of a perfect crystal approaches zero as its temperature approaches absolute zero.

\[
S\rightarrow0\quad\text{as}\quad T\rightarrow0\,K
\]

It also implies that absolute zero cannot be reached through a finite sequence of ideal thermodynamic processes.

The third law provides an important reference for absolute entropy measurements.

## 14. Worked Numerical Examples

**Example 1: First law**

A system absorbs 500 J of heat and performs 200 J of work.

\[
\Delta U=Q-W
\]

\[
\Delta U=500-200
\]

\[
\boxed{\Delta U=300\,J}
\]

The internal energy increases by 300 J.

**Example 2: Work at constant pressure**

A gas expands from 0.02 m³ to 0.05 m³ against a constant pressure of 100000 Pa.

\[
W=P\Delta V
\]

\[
W=100000(0.05-0.02)
\]

\[
\boxed{W=3000\,J}
\]

**Example 3: Heat engine efficiency**

An engine absorbs 2000 J of heat and rejects 1200 J.

\[
W=Q_H-Q_C
\]

\[
W=2000-1200=800\,J
\]

\[
\eta=\frac{800}{2000}\times100\%
\]

\[
\boxed{\eta=40\%}
\]

**Example 4: Carnot efficiency**

A Carnot engine operates between 600 K and 300 K.

\[
\eta_C=1-\frac{T_C}{T_H}
\]

\[
\eta_C=1-\frac{300}{600}
\]

\[
\boxed{\eta_C=0.5=50\%}
\]

## 15. Applications

- Steam and internal combustion engines.
- Refrigerators and air conditioners.
- Thermal power stations.
- Heat pumps.
- Industrial energy systems.
- Chemical and biological processes.
- Energy efficiency analysis.

## Common Exam Traps

- Heat and work are modes of energy transfer, not state variables.
- The sign convention must be consistent when using the first law.
- An isothermal ideal-gas process has no change in internal energy.
- An adiabatic process has zero heat transfer, not necessarily zero temperature change.
- An isochoric process involves zero boundary work.
- Entropy is not simply disorder; it is a thermodynamic state function with a precise statistical and physical meaning.
- Carnot efficiency requires absolute temperatures.
- A refrigerator transfers heat from cold to hot by consuming work.

## Quiz

1. A system receives 600 J of heat and performs 250 J of work. Its change in internal energy is:

- [ ] 850 J
- [x] 350 J
- [ ] -350 J
- [ ] 250 J

> Using delta U = Q - W, the change is 600 - 250 = 350 J.

2. In an isochoric process, the work done by a gas is:

- [x] Zero
- [ ] Equal to its internal energy
- [ ] Always positive
- [ ] Always negative

> At constant volume, delta V is zero. Therefore, boundary work P delta V is zero.

3. The maximum theoretical efficiency of a heat engine operating between 500 K and 300 K is:

- [ ] 20%
- [ ] 30%
- [x] 40%
- [ ] 60%

> Carnot efficiency = 1 - 300/500 = 0.4, or 40%.