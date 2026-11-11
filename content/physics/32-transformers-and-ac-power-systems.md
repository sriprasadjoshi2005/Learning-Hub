---
title: Transformers and AC Power Systems
level: intermediate
---

Transformers are electrical devices that transfer energy between circuits through electromagnetic induction. They are essential for transmitting electricity efficiently over long distances and supplying suitable voltages to electrical equipment.

## 1. Introduction to Transformers

A transformer is a static electrical device that changes the magnitude of an alternating voltage without changing its frequency.

It operates on the principle of mutual electromagnetic induction.

A basic transformer contains:
- Primary winding.
- Secondary winding.
- Magnetic core.

The primary winding is connected to the AC input source.

The secondary winding supplies the output to the connected load.

## 2. Principle of Mutual Induction

When alternating current flows through the primary winding, it produces a changing magnetic flux in the core.

This changing flux links with the secondary winding.

According to Faraday's law, an EMF is induced in the secondary winding.

The energy is transferred through the changing magnetic field rather than through a direct electrical connection between the windings.

## 3. Construction of a Transformer

### Primary Winding

The primary winding receives electrical energy from the AC source.

### Secondary Winding

The secondary winding delivers electrical energy to the output circuit.

### Magnetic Core

The core provides a low-reluctance path for magnetic flux.

Transformer cores are commonly made from laminated magnetic materials.

Lamination reduces eddy-current losses.

## 4. Transformer EMF Equation

For a sinusoidal magnetic flux:

Φ = Φm sin(ωt)

The RMS induced EMF in a winding is:

E = 4.44fNΦm

Where:
- E = RMS induced EMF
- f = frequency
- N = number of turns
- Φm = maximum magnetic flux

For the primary:

E1 = 4.44fN1Φm

For the secondary:

E2 = 4.44fN2Φm

Therefore:

E2/E1 = N2/N1

This is the ideal transformer voltage-turns relationship.

## 5. Step-Up Transformer

A step-up transformer increases the voltage.

For a step-up transformer:

N2 greater than N1

Therefore:

V2 greater than V1

For an ideal transformer, current decreases as voltage increases.

Step-up transformers are used near generating stations for high-voltage power transmission.

## 6. Step-Down Transformer

A step-down transformer decreases the voltage.

For a step-down transformer:

N2 less than N1

Therefore:

V2 less than V1

The secondary current is greater than the primary current in an ideal transformer supplying the same power.

Step-down transformers are used in distribution networks and electrical equipment.

## 7. Current Relationship in an Ideal Transformer

For an ideal transformer:

V1I1 = V2I2

Therefore:

I2/I1 = V1/V2

Combining the voltage and current relationships:

V2/V1 = N2/N1

I2/I1 = N1/N2

The voltage ratio equals the turns ratio, while the current ratio is its reciprocal.

## 8. Transformer Efficiency

Transformer efficiency is the ratio of output power to input power.

η = (Pout/Pin) × 100%

For an ideal transformer:

η = 100%

Real transformers have losses, so their efficiency is below 100%.

## 9. Transformer Losses

### Copper Loss

Copper loss occurs because the windings have electrical resistance.

Pcu = I²R

It increases with the square of winding current.

### Hysteresis Loss

Hysteresis loss occurs because the magnetic domains in the core repeatedly change orientation during alternating magnetisation.

It can be reduced by selecting suitable core materials with a narrow hysteresis loop.

### Eddy Current Loss

Changing magnetic flux induces circulating currents in the conducting core.

These currents generate heat.

Laminating the core reduces eddy-current loss.

### Flux Leakage

Not all magnetic flux produced by the primary winding links with the secondary winding.

This reduces energy transfer.

### Other Losses

Additional losses may occur through winding effects, vibration, sound and dielectric heating.

## 10. Why Transformers Cannot Operate Normally on Steady DC

A transformer requires changing magnetic flux to induce EMF.

A steady DC current produces approximately constant magnetic flux after the initial switching transient.

Therefore:
- No continuous secondary EMF is induced.
- The primary winding may draw excessive current because its inductive reactance is absent under steady DC.
- The winding may overheat and become damaged.

Transformers are designed for AC operation or other appropriately varying waveforms.

## 11. Why High Voltage Is Used for Transmission

Electrical power is transmitted over long distances using high voltages.

The transmitted power is:

P = VI

For a fixed power:

I = P/V

Therefore, increasing voltage reduces current.

The resistive power loss in transmission lines is:

Ploss = I²R

Reducing current significantly reduces power loss.

For example, if current is reduced to one-tenth while line resistance remains unchanged, resistive power loss becomes one-hundredth.

## 12. AC Power Distribution System

A simplified electrical power system contains:

1. Generating station.
2. Step-up transformer.
3. High-voltage transmission lines.
4. Receiving substation.
5. Step-down transformers.
6. Local distribution network.
7. Consumers.

The voltage is increased for efficient transmission and reduced before electricity reaches most consumers.

## 13. Three-Phase AC Supply

A three-phase electrical system consists of three sinusoidal voltages with equal frequency and magnitude, separated by 120 electrical degrees.

The three phases can be represented as:

Va = Vm sin(ωt)

Vb = Vm sin(ωt - 120 degrees)

Vc = Vm sin(ωt - 240 degrees)

Three-phase systems are widely used in industrial power distribution and electric motors.

Advantages include:
- Efficient transmission of power.
- Nearly constant total power under balanced conditions.
- Effective operation of three-phase motors.
- Reduced conductor material for certain transmission arrangements.

## 14. Star and Delta Connections

### Star Connection

In a star connection, one end of each phase winding is joined at a common neutral point.

For a balanced star system:

VL = √3 Vph

IL = Iph

Where:
- VL = line voltage
- Vph = phase voltage
- IL = line current
- Iph = phase current

### Delta Connection

In a delta connection, the three phase windings form a closed loop.

For a balanced delta system:

VL = Vph

IL = √3 Iph

These relationships assume a balanced three-phase system.

## 15. Power in a Three-Phase System

For a balanced three-phase system, real power is:

P = √3 VLIL cos φ

Where:
- VL = line voltage
- IL = line current
- cos φ = power factor

The power factor describes the phase relationship between voltage and current.

A higher power factor generally reduces current required to transmit a given amount of real power at a fixed voltage.

## 16. Numerical Applications

**Example 1: Transformer turns ratio**

A transformer has 500 turns in its primary winding and 100 turns in its secondary winding. The primary voltage is 230 V.

V2/V1 = N2/N1

V2/230 = 100/500

V2 = 46 V

It is a step-down transformer.

**Example 2: Ideal transformer current**

An ideal transformer receives 1000 W at 200 V.

Primary current:

I1 = P/V1

I1 = 1000/200

I1 = 5 A

If the output voltage is 50 V:

I2 = P/V2

I2 = 1000/50

I2 = 20 A

**Example 3: Transformer efficiency**

A transformer receives 1000 W and delivers 950 W.

η = (950/1000) × 100%

η = 95%

## Common Exam Traps

- A transformer works on mutual induction.
- A normal transformer requires changing magnetic flux.
- The secondary voltage is proportional to its number of turns.
- A step-up transformer increases voltage and decreases current for ideal power transfer.
- A step-down transformer decreases voltage and increases current for ideal power transfer.
- Transformer frequency remains unchanged.
- Core lamination reduces eddy-current losses.
- Copper losses are proportional to I²R.
- Transformers cannot operate normally from a steady DC supply.
- High-voltage transmission reduces current and line losses.
- In a balanced star connection, line voltage is √3 times phase voltage.
- In a balanced delta connection, line current is √3 times phase current.

## Quiz

1. A transformer has 1000 primary turns and 200 secondary turns. If its primary voltage is 250 V, its ideal secondary voltage is:

- [ ] 250 V
- [ ] 100 V
- [x] 50 V
- [ ] 1250 V

> V2/V1 = N2/N1 = 200/1000. Therefore V2 = 250 × 0.2 = 50 V.

2. Laminating a transformer core primarily reduces:

- [ ] Copper losses
- [x] Eddy-current losses
- [ ] Flux linkage
- [ ] The number of turns

> Thin insulated laminations interrupt large circulating current paths in the core and reduce eddy-current heating.

3. Why is electricity transmitted at high voltage?

- [ ] To increase the resistance of transmission lines
- [ ] To eliminate all electrical losses
- [x] To reduce current and resistive power losses for a given transmitted power
- [ ] To increase the frequency of AC

> For fixed power, increasing voltage reduces current. Since transmission loss is I²R, this reduces energy wasted as heat.