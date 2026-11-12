---
title: Maximum Power Transfer Theorem
level: intermediate
---

# Maximum Power Transfer Theorem

## Introduction

Maximum power transfer is an important principle in electrical network theory. It determines the load condition under which a source network delivers the greatest possible power to an external load.

The theorem is particularly useful in communication systems, amplifier design, impedance matching, antenna systems, and signal transmission.

For a DC resistive network, maximum power is transferred when the load resistance equals the Thevenin resistance of the source network.

For AC networks containing complex impedances, maximum average power transfer occurs when the load impedance is the complex conjugate of the source impedance.

This lesson develops the theorem mathematically, derives the maximum-power condition, examines efficiency, and explains practical impedance-matching applications.

## 1. Statement of Maximum Power Transfer Theorem

The maximum power transfer theorem states:

**A linear source network delivers maximum power to a load when the load resistance is equal to the Thevenin resistance of the network as viewed from the load terminals.**

For a DC resistive network:

\[
\boxed{R_L=R_{TH}}
\]

Where:
- \(R_L\) = load resistance.
- \(R_{TH}\) = Thevenin resistance.

This condition produces maximum load power.

## 2. Thevenin Equivalent Representation

Any suitable linear two-terminal source network can be represented using its Thevenin equivalent.

```text
       RTH
  +───/\/\/─────+
  |             |
 (VTH)          RL
  |             |
  +─────────────+
```

The load current is:

\[
I=\frac{V_{TH}}{R_{TH}+R_L}
\]

The load power is:

\[
P_L=I^2R_L
\]

Substituting the current:

\[
\boxed{
P_L=\frac{V_{TH}^2R_L}
{(R_{TH}+R_L)^2}
}
\]

This equation describes the power delivered to the load as a function of load resistance.

## 3. Derivation of Maximum Power Condition

Starting with:

\[
P_L=\frac{V_{TH}^2R_L}
{(R_{TH}+R_L)^2}
\]

Differentiate with respect to \(R_L\).

Using the product and quotient rules:

\[
\frac{dP_L}{dR_L}
=
V_{TH}^2
\frac{(R_{TH}+R_L)^2-2R_L(R_{TH}+R_L)}
{(R_{TH}+R_L)^4}
\]

Factorising:

\[
\frac{dP_L}{dR_L}
=
V_{TH}^2
\frac{(R_{TH}+R_L)(R_{TH}-R_L)}
{(R_{TH}+R_L)^4}
\]

Simplifying:

\[
\frac{dP_L}{dR_L}
=
V_{TH}^2
\frac{R_{TH}-R_L}
{(R_{TH}+R_L)^3}
\]

For maximum or minimum power:

\[
\frac{dP_L}{dR_L}=0
\]

Therefore:

\[
R_{TH}-R_L=0
\]

Hence:

\[
\boxed{R_L=R_{TH}}
\]

This is the maximum power transfer condition for a purely resistive DC network.

## 4. Maximum Power Expression

When:

\[
R_L=R_{TH}
\]

The load current becomes:

\[
I=\frac{V_{TH}}{2R_{TH}}
\]

Maximum load power is:

\[
P_{max}=I^2R_{TH}
\]

Substituting:

\[
P_{max}=
\left(\frac{V_{TH}}{2R_{TH}}\right)^2R_{TH}
\]

Therefore:

\[
\boxed{P_{max}=\frac{V_{TH}^2}{4R_{TH}}}
\]

This equation gives the maximum power available from a Thevenin-equivalent resistive source.

## 5. Efficiency at Maximum Power Transfer

Efficiency is defined as:

\[
\eta=\frac{P_L}{P_{source}}\times100
\]

At maximum power transfer:

\[
R_L=R_{TH}
\]

The same current flows through the internal resistance and load.

Internal power loss:

\[
P_{internal}=I^2R_{TH}
\]

Load power:

\[
P_L=I^2R_L
\]

Since both resistances are equal:

\[
P_{internal}=P_L
\]

Therefore, total power supplied to the two resistances is divided equally.

\[
\boxed{\eta=50\%}
\]

This means half the power is delivered to the load and half is dissipated in the source's internal resistance.

## 6. Maximum Power and Maximum Efficiency

Maximum power transfer does not mean maximum efficiency.

These are different objectives.

| Condition | Result |
|---|---|
| \(R_L=R_{TH}\) | Maximum load power |
| \(R_L\gg R_{TH}\) | High efficiency but lower load power |
| \(R_L\ll R_{TH}\) | Low load voltage and low load power |

In practical power-delivery systems, efficiency is often more important than obtaining maximum power from a source.

For this reason, power systems generally use low source resistance and loads much larger than the source resistance.

## 7. Maximum Power Transfer in AC Circuits

In AC circuits, resistance alone is not sufficient to describe the source and load.

The source and load may contain resistance and reactance.

The source impedance is:

\[
Z_{TH}=R_{TH}+jX_{TH}
\]

The load impedance is:

\[
Z_L=R_L+jX_L
\]

For maximum average power transfer:

\[
\boxed{Z_L=Z_{TH}^{*}}
\]

The asterisk represents the complex conjugate.

Therefore:

\[
\boxed{R_L=R_{TH}}
\]

And:

\[
\boxed{X_L=-X_{TH}}
\]

The load resistance must equal the source resistance, while the load reactance must cancel the source reactance.

This condition is known as conjugate impedance matching.

## 8. Impedance Matching

Impedance matching is the process of adjusting the load impedance to obtain a desired power-transfer condition.

It is commonly used in:

- Radio-frequency circuits.
- Antenna systems.
- Transmission lines.
- Audio equipment.
- Communication transmitters and receivers.
- High-frequency amplifier stages.

A matching network may use inductors, capacitors, or transformers to transform one impedance into another.

## 9. Worked Numerical Examples

### Example 1: Maximum Power Delivered to a Load

**Given:**

- Thevenin voltage = 20 V.
- Thevenin resistance = 5 Ω.

**Find:** Load resistance for maximum power and maximum power.

**Solution:**

Maximum power condition:

\[
R_L=R_{TH}
\]

\[
\boxed{R_L=5\ \Omega}
\]

Maximum power:

\[
P_{max}=\frac{V_{TH}^2}{4R_{TH}}
\]

\[
P_{max}=\frac{20^2}{4\times5}
\]

\[
P_{max}=\frac{400}{20}
\]

\[
\boxed{P_{max}=20\text{ W}}
\]

### Example 2: Load Power for Different Resistances

**Given:**

- Thevenin voltage = 12 V.
- Thevenin resistance = 4 Ω.

Calculate load power for:

1. \(R_L=2\ \Omega\)
2. \(R_L=4\ \Omega\)
3. \(R_L=8\ \Omega\)

**Solution:**

General expression:

\[
P_L=\frac{V_{TH}^2R_L}
{(R_{TH}+R_L)^2}
\]

For \(R_L=2\ \Omega\):

\[
P_L=\frac{144\times2}{(4+2)^2}
\]

\[
\boxed{P_L=8\text{ W}}
\]

For \(R_L=4\ \Omega\):

\[
P_L=\frac{144\times4}{(4+4)^2}
\]

\[
\boxed{P_L=9\text{ W}}
\]

For \(R_L=8\ \Omega\):

\[
P_L=\frac{144\times8}{(4+8)^2}
\]

\[
\boxed{P_L=8\text{ W}}
\]

The maximum power is 9 W when the load resistance equals the Thevenin resistance.

### Example 3: Efficiency at Maximum Power Transfer

**Given:**

- Source resistance = 10 Ω.
- Load resistance = 10 Ω.
- Current = 2 A.

**Find:** Load power, internal power loss, and efficiency.

**Solution:**

Load power:

\[
P_L=I^2R_L
\]

\[
P_L=2^2\times10
\]

\[
\boxed{P_L=40\text{ W}}
\]

Internal power loss:

\[
P_{internal}=I^2R_{TH}
\]

\[
P_{internal}=2^2\times10
\]

\[
\boxed{P_{internal}=40\text{ W}}
\]

Efficiency:

\[
\eta=\frac{40}{40+40}\times100
\]

\[
\boxed{\eta=50\%}
\]

### Example 4: Maximum Power in an AC Circuit

**Given:**

Source impedance:

\[
Z_{TH}=4+j3\ \Omega
\]

**Find:** Load impedance for maximum average power transfer.

**Solution:**

The load impedance must be the complex conjugate:

\[
Z_L=Z_{TH}^{*}
\]

Therefore:

\[
\boxed{Z_L=4-j3\ \Omega}
\]

The load resistance is 4 Ω and the load reactance is -3 Ω.

The negative reactance represents a capacitive load.

## 10. Practical Applications

### 10.1 Antenna Matching

Antennas are designed to operate with specific impedances.

Matching the antenna impedance to the transmission system improves power transfer and reduces reflections.

### 10.2 Audio Amplifiers

Impedance matching may be used in particular audio stages to transfer signals effectively.

However, modern audio power amplifiers commonly use low-output-impedance designs rather than strict maximum-power matching.

### 10.3 Communication Systems

RF transmitters and receivers frequently use matching networks to maximise power transfer and control signal reflections.

### 10.4 Transformer Matching

A transformer can be used to make a load appear as a different resistance to the source.

For an ideal transformer:

\[
\boxed{R_{in}=\left(\frac{N_1}{N_2}\right)^2R_L}
\]

Where:
- \(N_1\) = primary turns.
- \(N_2\) = secondary turns.
- \(R_L\) = load resistance.

## 11. Important Observations

- Maximum power transfer occurs when load resistance equals source resistance in a DC resistive network.
- Maximum average AC power transfer requires complex-conjugate impedance matching.
- Maximum power transfer occurs at 50% efficiency for the simple resistive Thevenin model.
- Maximum power and maximum efficiency are different objectives.
- The theorem is particularly important in signal and communication systems.

## 12. Common Exam Traps

1. **Using the wrong resistance condition:** Maximum DC power requires \(R_L=R_{TH}\).

2. **Assuming maximum efficiency occurs at maximum power:** Maximum power transfer in the resistive model has 50% efficiency.

3. **Ignoring reactance in AC circuits:** AC maximum power transfer requires conjugate matching.

4. **Using the source voltage directly as the load voltage:** The load voltage is reduced by the internal resistance.

5. **Confusing source resistance with load resistance:** The maximum-power condition requires equality between them, not addition or subtraction.

6. **Forgetting that maximum power depends on source voltage:** The maximum available power is proportional to the square of the Thevenin voltage.

## Quiz

1. A Thevenin source has a voltage of 24 V and an internal resistance of 6 Ω. What load resistance receives maximum power?

   - [ ] 12 Ω
   - [ ] 3 Ω
   - [x] 6 Ω
   - [ ] 24 Ω

   > Maximum DC power transfer occurs when the load resistance equals the Thevenin resistance. Therefore, \(R_L=6\ \Omega\).

2. What is the efficiency of a simple resistive source network at the maximum power transfer condition?

   - [ ] 25%
   - [x] 50%
   - [ ] 75%
   - [ ] 100%

   > At maximum power transfer, the source resistance and load resistance are equal. Both dissipate equal power, so half the total power reaches the load.

3. A source has impedance \(Z_{TH}=6+j4\ \Omega\). Which load impedance produces maximum average power transfer?

   - [ ] \(6+j4\ \Omega\)
   - [ ] \(4-j6\ \Omega\)
   - [x] \(6-j4\ \Omega\)
   - [ ] \(6+j8\ \Omega\)

   > Maximum average AC power transfer requires the load impedance to be the complex conjugate of the source impedance. The resistance remains 6 Ω and the reactance changes sign.