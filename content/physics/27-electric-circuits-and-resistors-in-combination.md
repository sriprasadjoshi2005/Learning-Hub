---
title: Electric Circuits and Resistors in Combination
level: intermediate
---

Electrical circuits provide controlled paths through which electric current flows. Understanding how resistors are connected, how voltage and current are distributed, and how circuit laws operate is essential for analysing electrical systems.

## 1. Electric Circuit

An electric circuit is a closed conducting path through which electric current can flow.

A basic circuit contains:
- An electrical source.
- Conducting wires.
- A load or electrical component.
- A complete path for current.

Common components include batteries, resistors, switches, lamps, capacitors and measuring instruments.

An open circuit has a broken path and ideally carries no current.

A closed circuit has a complete conducting path.

## 2. Circuit Symbols

Electrical circuit diagrams use standard symbols to represent components.

Common symbols include:

- Cell: a pair of unequal parallel lines.
- Battery: multiple cell symbols.
- Resistor: a rectangular or zigzag symbol.
- Switch: a break with a movable contact.
- Ammeter: a circle containing A.
- Voltmeter: a circle containing V.
- Capacitor: two parallel plates.
- Ground: a set of progressively shorter horizontal lines.

Circuit diagrams make complex electrical arrangements easier to understand.

## 3. Resistors in Series

Resistors are connected in series when they are arranged along a single path.

Important characteristics:

- The same current flows through every resistor.
- The total potential difference is the sum of individual voltage drops.
- Equivalent resistance is the sum of individual resistances.

Req = R1 + R2 + R3 + ...

For n identical resistors:

Req = nR

The equivalent resistance is greater than any individual resistance in the series combination.

## 4. Resistors in Parallel

Resistors are connected in parallel when their terminals are connected across the same two nodes.

Important characteristics:

- The same voltage exists across every resistor.
- Total current is the sum of branch currents.
- Equivalent resistance is calculated using reciprocal addition.

1/Req = 1/R1 + 1/R2 + 1/R3 + ...

For two resistors:

Req = R1R2/(R1 + R2)

For n identical resistors:

Req = R/n

The equivalent resistance is smaller than the smallest individual resistance.

## 5. Mixed Series-Parallel Circuits

Many circuits contain both series and parallel connections.

A systematic approach is:

1. Identify clearly connected series and parallel groups.
2. Calculate the equivalent resistance of the simplest groups.
3. Replace each group with its equivalent resistance.
4. Repeat until a single equivalent resistance remains.
5. Use Ohm's law to calculate the total current.
6. Work backwards to determine individual branch currents and voltage drops.

Never assume that resistors are in series simply because they appear next to one another in a diagram. Their connections at circuit nodes determine the relationship.

## 6. Kirchhoff's Current Law

Kirchhoff's Current Law (KCL) is based on conservation of electric charge.

It states that the algebraic sum of currents at any junction is zero.

ΣI = 0

Equivalently:

Total current entering a junction = Total current leaving it.

This law applies to electrical junctions in lumped circuit models.

It is useful for analysing parallel and complex networks.

## 7. Kirchhoff's Voltage Law

Kirchhoff's Voltage Law (KVL) is based on conservation of energy.

It states that the algebraic sum of potential differences around any closed circuit loop is zero.

ΣV = 0

For a simple loop containing a battery and resistors:

ε - IR1 - IR2 - ... = 0

The signs of voltage rises and drops depend on the chosen direction of traversal.

## 8. Applying Kirchhoff's Laws

A systematic method for solving multi-loop circuits:

1. Assign current variables to branches.
2. Choose a direction for each assumed current.
3. Apply KCL at relevant junctions.
4. Select independent closed loops.
5. Apply KVL to each loop.
6. Solve the simultaneous equations.
7. Interpret negative current values as currents flowing opposite to the assumed direction.

The choice of current direction is arbitrary at the beginning.

## 9. Wheatstone Bridge

A Wheatstone bridge is a circuit used to measure an unknown resistance by balancing two branches of a bridge network.

For a balanced bridge:

P/Q = R/S

Where P, Q, R and S are the four arm resistances, arranged so that P and Q form one branch and R and S form the other branch.

At balance:
- No current flows through the galvanometer.
- The potentials at the galvanometer terminals are equal.

Wheatstone bridges are used in precision resistance measurement and sensor circuits.

## 10. Meter Bridge

A meter bridge is a practical application of the Wheatstone bridge principle.

It consists of:
- A uniform wire of length 1 m.
- Two resistance gaps.
- A galvanometer.
- A jockey making contact at a selected point.

At balance, if the unknown resistance X is in the left gap and known resistance R is in the right gap, with balancing length l measured from the left end:

X/R = l/(100 - l)

Therefore:

X = Rl/(100 - l)

This assumes a uniform bridge wire and correct connections.

## 11. Potentiometer

A potentiometer measures potential difference or EMF by comparing it with the potential drop along a uniform wire.

Its principle is that the potential drop along a uniform wire carrying constant current is proportional to its length.

V ∝ l

For two cells:

ε1/ε2 = l1/l2

Where l1 and l2 are their respective balancing lengths.

A potentiometer uses a null method, so at balance it draws no current from the source being measured.

This makes it more accurate than an ordinary voltmeter for comparing EMFs.

## 12. Comparing EMF and Internal Resistance

A potentiometer can also be used to determine the internal resistance of a cell.

Let:
- l1 = balancing length for EMF when the cell is not supplying current.
- l2 = balancing length for terminal voltage when the cell supplies current through an external resistance R.

Then:

ε/V = l1/l2

For a cell with internal resistance r:

r = R(l1/l2 - 1)

This method avoids drawing current from the cell during the EMF measurement.

## 13. Electrical Measuring Instruments

### Ammeter

An ammeter measures current.

It is connected in series with the circuit.

An ideal ammeter has zero resistance so that it does not significantly alter the current.

### Voltmeter

A voltmeter measures potential difference.

It is connected in parallel across the component.

An ideal voltmeter has infinite resistance so that it draws no current.

### Galvanometer

A galvanometer detects small electric currents.

It can be converted into:
- An ammeter by connecting a low-resistance shunt in parallel.
- A voltmeter by connecting a high resistance in series.

## 14. Numerical Applications

**Example 1: Series resistors**

Three resistors of 2 Ω, 3 Ω and 5 Ω are connected in series.

Req = 2 + 3 + 5

Req = 10 Ω

**Example 2: Parallel resistors**

Two resistors of 6 Ω and 3 Ω are connected in parallel.

Req = (6 × 3)/(6 + 3)

Req = 2 Ω

**Example 3: Wheatstone bridge**

A balanced bridge has P = 2 Ω, Q = 4 Ω and R = 3 Ω. Find S.

P/Q = R/S

2/4 = 3/S

S = 6 Ω

## Common Exam Traps

- Series resistors carry the same current.
- Parallel resistors have the same potential difference.
- Equivalent series resistance is greater than each individual resistance.
- Equivalent parallel resistance is smaller than the smallest individual resistance.
- KCL follows conservation of charge.
- KVL follows conservation of energy.
- Negative calculated current indicates an opposite direction, not an invalid result.
- An ammeter is connected in series.
- A voltmeter is connected in parallel.
- A balanced Wheatstone bridge has zero galvanometer current.
- A potentiometer uses a null method and can compare EMFs accurately.

## Quiz

1. Three resistors of 2 Ω, 4 Ω and 6 Ω are connected in series. Their equivalent resistance is:

- [ ] 2 Ω
- [ ] 6 Ω
- [x] 12 Ω
- [ ] 24 Ω

> Series resistances add directly: 2 + 4 + 6 = 12 Ω.

2. Kirchhoff's Current Law is based on the conservation of:

- [ ] Energy
- [x] Electric charge
- [ ] Momentum
- [ ] Mass

> KCL states that the total current entering a junction equals the total current leaving it, reflecting charge conservation.

3. An ideal voltmeter should have:

- [ ] Zero resistance
- [ ] Very low resistance
- [x] Infinite resistance
- [ ] The same resistance as the circuit

> An ideal voltmeter draws no current from the circuit, which requires infinite resistance.