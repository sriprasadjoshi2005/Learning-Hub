---
title: Alternating Current and AC Circuits
level: intermediate
---

Alternating current (AC) is an electric current that changes its magnitude and periodically reverses its direction. It is widely used in electrical power generation, transmission, domestic electricity supply and industrial equipment.

Unlike direct current, which flows in one direction, alternating current varies continuously with time.

## 1. Introduction to Alternating Current

An alternating current periodically changes direction.

The voltage supplied by an AC source also changes periodically.

A common form of alternating voltage is sinusoidal:

v(t) = Vm sin(ωt)

Similarly, the current may be written as:

i(t) = Im sin(ωt)

Where:
- Vm = maximum or peak voltage
- Im = maximum or peak current
- ω = angular frequency
- t = time

The SI unit of voltage is the volt (V), and the SI unit of current is the ampere (A).

## 2. Time Period and Frequency

The time period T is the time taken to complete one full cycle.

The frequency f is the number of complete cycles per second.

f = 1/T

The SI unit of frequency is the hertz (Hz).

Angular frequency is:

ω = 2πf

Therefore:

ω = 2π/T

For example, an AC supply with frequency 50 Hz completes 50 cycles every second.

Its time period is:

T = 1/50 = 0.02 s

## 3. Instantaneous Values

The instantaneous value of an alternating quantity is its value at a particular moment.

For sinusoidal voltage:

v = Vm sin(ωt)

For sinusoidal current:

i = Im sin(ωt)

The value changes continuously between positive and negative maximum values.

At:
- ωt = 0: voltage is zero.
- ωt = π/2: voltage is maximum positive.
- ωt = π: voltage is zero.
- ωt = 3π/2: voltage is maximum negative.
- ωt = 2π: one complete cycle is completed.

The same mathematical pattern applies to sinusoidal current.

## 4. Peak Value

The peak value is the maximum magnitude reached by an alternating quantity.

It is also called the amplitude.

For voltage:

Peak voltage = Vm

For current:

Peak current = Im

Peak values are important when determining the maximum electrical stress experienced by components.

## 5. Average Value of AC

The average value is calculated over a specified time interval.

For a complete sinusoidal cycle:

Average voltage = 0

Average current = 0

This occurs because the positive and negative halves cancel.

For a half-cycle, the average value of a sinusoidal current is:

Iaverage = 2Im/π

Similarly:

Vaverage = 2Vm/π

The average over a half-cycle is useful in rectifier analysis.

## 6. Root Mean Square Value

The root mean square (RMS) value is the effective value of an alternating quantity.

It represents the value of direct current that would produce the same average heating effect in a resistor.

For sinusoidal voltage:

Vrms = Vm/√2

For sinusoidal current:

Irms = Im/√2

Therefore:

Vrms ≈ 0.707Vm

Irms ≈ 0.707Im

RMS values are normally used when specifying AC supply voltages and currents.

For example, a domestic AC supply rated at 230 V generally refers to its RMS voltage, not its peak voltage.

Its peak voltage is:

Vm = √2 × 230

Vm ≈ 325 V

## 7. AC Through a Pure Resistor

Consider a resistor R connected to an AC voltage source.

The applied voltage is:

v = Vm sin(ωt)

Using Ohm's law:

i = v/R

Therefore:

i = (Vm/R)sin(ωt)

Since Im = Vm/R:

i = Im sin(ωt)

Voltage and current are in phase.

This means:
- Both reach maximum values simultaneously.
- Both become zero simultaneously.
- Their zero crossings occur at the same times.

The average power consumed is:

P = VrmsIrms

For a pure resistor:

P = Irms²R

## 8. AC Through a Pure Inductor

An inductor opposes changes in current through self-induction.

For a pure inductor:

v = L(di/dt)

If:

v = Vm sin(ωt)

Then the current is:

i = Im sin(ωt - π/2)

Thus, current lags voltage by 90 degrees.

The inductive reactance is:

XL = ωL

Therefore:

XL = 2πfL

Where:
- XL = inductive reactance
- L = inductance
- f = frequency

The SI unit of reactance is the ohm (Ω).

Increasing frequency or inductance increases inductive reactance.

An ideal inductor consumes zero average power over a complete cycle.

It temporarily stores energy in its magnetic field and returns that energy to the source.

## 9. AC Through a Pure Capacitor

A capacitor opposes changes in voltage across it.

For a capacitor:

i = C(dv/dt)

If:

v = Vm sin(ωt)

Then:

i = ωCVm cos(ωt)

Since cos(ωt) = sin(ωt + π/2):

i = Im sin(ωt + π/2)

Thus, current leads voltage by 90 degrees.

The capacitive reactance is:

XC = 1/(ωC)

Therefore:

XC = 1/(2πfC)

Increasing frequency or capacitance decreases capacitive reactance.

An ideal capacitor consumes zero average power over a complete cycle.

It stores energy in its electric field and returns that energy to the source.

## 10. Phase Difference

The phase difference describes how much one alternating quantity is shifted relative to another.

For a pure resistor:

Phase difference = 0 degrees.

For a pure inductor:

Current lags voltage by 90 degrees.

For a pure capacitor:

Current leads voltage by 90 degrees.

These relationships are fundamental to AC circuit analysis.

## 11. Series RL Circuit

A series RL circuit contains a resistor and an inductor connected to an AC source.

The inductive reactance is:

XL = ωL

The impedance is:

Z = sqrt(R² + XL²)

Current:

I = V/Z

The phase angle is:

tan φ = XL/R

Current lags voltage by angle φ.

The impedance is measured in ohms.

## 12. Series RC Circuit

A series RC circuit contains a resistor and capacitor.

The capacitive reactance is:

XC = 1/(ωC)

The impedance is:

Z = sqrt(R² + XC²)

Current:

I = V/Z

The phase angle magnitude is:

tan φ = XC/R

Current leads the supply voltage.

## 13. Series RLC Circuit

A series RLC circuit contains a resistor, inductor and capacitor.

Its net reactance is:

X = XL - XC

The impedance is:

Z = sqrt(R² + (XL - XC)²)

Current:

I = V/Z

The phase angle is:

tan φ = (XL - XC)/R

Three cases are possible:

- XL greater than XC: circuit is inductive and current lags voltage.
- XC greater than XL: circuit is capacitive and current leads voltage.
- XL equals XC: circuit is purely resistive at resonance.

## 14. Resonance in a Series RLC Circuit

Resonance occurs when inductive reactance equals capacitive reactance.

XL = XC

ωL = 1/(ωC)

Therefore:

ω0 = 1/sqrt(LC)

Resonant frequency:

f0 = 1/(2πsqrt(LC))

At resonance:
- Net reactance is zero.
- Impedance is minimum and equals R.
- Current is maximum.
- Voltage and current are in phase.
- Power factor is one.

Resonance is used in radio tuning, filters and frequency-selective circuits.

## 15. Quality Factor

The quality factor Q describes the sharpness of resonance.

For an ideal series RLC circuit:

Q = ω0L/R

Equivalently:

Q = 1/(ω0CR)

A higher quality factor indicates a sharper resonance and a narrower bandwidth.

## 16. Numerical Applications

**Example 1: RMS voltage**

An AC source has peak voltage 325 V.

Vrms = Vm/√2

Vrms = 325/1.414

Vrms ≈ 230 V

**Example 2: Inductive reactance**

An inductor of 0.2 H is connected to a 50 Hz supply.

XL = 2πfL

XL = 2 × 3.1416 × 50 × 0.2

XL ≈ 62.83 Ω

**Example 3: Capacitive reactance**

A capacitor of 100 μF is connected to a 50 Hz supply.

XC = 1/(2πfC)

XC = 1/(2 × 3.1416 × 50 × 100 × 10^-6)

XC ≈ 31.83 Ω

## Common Exam Traps

- RMS value is not the same as peak value.
- For a sinusoidal AC signal, RMS value is peak value divided by √2.
- The average of a complete sinusoidal cycle is zero.
- In a pure resistor, voltage and current are in phase.
- In a pure inductor, current lags voltage by 90 degrees.
- In a pure capacitor, current leads voltage by 90 degrees.
- Inductive reactance increases with frequency.
- Capacitive reactance decreases with frequency.
- At series resonance, impedance is minimum and current is maximum.
- Reactance and resistance are both measured in ohms, but they represent different effects.

## Quiz

1. The RMS value of a sinusoidal alternating voltage with peak value Vm is:

- [ ] Vm
- [x] Vm/√2
- [ ] √2Vm
- [ ] Vm/2

> For a sinusoidal signal, RMS voltage is Vm/√2, approximately 0.707 times the peak voltage.

2. In a pure inductive AC circuit, current:

- [ ] Leads voltage by 90 degrees
- [x] Lags voltage by 90 degrees
- [ ] Is always in phase with voltage
- [ ] Lags voltage by 180 degrees

> An ideal inductor produces a phase difference of 90 degrees, with current lagging voltage.

3. At resonance in a series RLC circuit:

- [ ] Impedance is maximum
- [ ] Current is minimum
- [x] Inductive and capacitive reactances are equal
- [ ] Net reactance is maximum

> Resonance occurs when XL = XC, making the net reactance zero and impedance equal to resistance.