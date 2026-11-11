---
title: Measurement, Significant Figures and Experimental Errors
level: foundation
---

Physics depends on measurements. Every experiment involves measuring physical quantities such as length, mass, time, temperature, voltage or current.

However, no physical measurement is perfectly exact. Measuring instruments have limitations, experimental conditions may vary, and observations may contain uncertainty.

Understanding measurement, significant figures and experimental errors is essential for obtaining reliable experimental results and solving numerical problems accurately.

## 1. Measurement and Its Importance

Measurement is the process of comparing an unknown physical quantity with an accepted standard of the same kind.

A measurement consists of:

- A numerical value.
- A unit.
- An associated level of precision or uncertainty.

For example:

\[
L=12.5\ \text{cm}
\]

This indicates that the measured length is approximately 12.5 centimetres.

Measurements are essential because physics uses quantitative observations to develop, test and verify scientific relationships.

## 2. Accuracy and Precision

Accuracy and precision describe different aspects of measurement quality.

**Accuracy:**

Accuracy describes how close a measured value is to the accepted or true value.

**Precision:**

Precision describes how close repeated measurements are to one another.

Consider the accepted value of a length as 10.0 cm.

Three sets of measurements are obtained:

- Set A: 9.9, 10.0, 10.1 cm
- Set B: 8.0, 8.0, 8.1 cm
- Set C: 9.5, 10.5, 9.8 cm

Set A is both accurate and precise.

Set B is precise but not accurate.

Set C is less precise and does not consistently reproduce the accepted value.

### Important distinction

A measurement can be precise without being accurate.

For example, a faulty instrument may consistently show a value 2 cm greater than the true value. Its readings may be highly consistent but systematically incorrect.

## 3. Least Count of Measuring Instruments

The least count is the smallest measurement that an instrument can directly resolve or display.

Examples:

| Instrument | Typical least count |
|---|---:|
| Ordinary metre scale | 1 mm |
| Vernier calipers | 0.1 mm or 0.01 cm |
| Micrometer screw gauge | 0.01 mm |
| Digital stopwatch | 0.01 s |
| Digital balance | Depends on model |

The actual least count depends on the instrument.

### Vernier calipers

Vernier calipers measure small lengths, internal diameters and external diameters.

The least count is:

\[
LC=1\ MSD-1\ VSD
\]

Where:

- MSD = one main scale division.
- VSD = one vernier scale division.

A typical reading is:

\[
\text{Reading}=\text{Main scale reading}
+\text{Vernier coincidence}\times LC
\]

If the main scale reading is 2.3 cm, the 6th vernier division coincides, and the least count is 0.01 cm:

\[
\text{Reading}=2.3+6(0.01)
\]

\[
=2.36\ \text{cm}
\]

### Screw gauge

A screw gauge measures very small thicknesses and diameters.

Its least count is:

\[
LC=\frac{\text{Pitch}}{\text{Number of circular scale divisions}}
\]

Pitch is the distance moved by the screw in one complete rotation.

For example, if the pitch is 1 mm and there are 100 circular scale divisions:

\[
LC=\frac{1}{100}=0.01\ \text{mm}
\]

The measurement is:

\[
\text{Reading}=\text{Pitch scale reading}
+\text{Circular scale reading}\times LC
\]

Zero correction must also be considered where necessary.

## 4. Significant Figures

Significant figures are the meaningful digits in a measured quantity that indicate its precision.

They include all certain digits and the first uncertain digit.

### Rules for counting significant figures

**Rule 1: All non-zero digits are significant.**

Example:

\[
456
\]

There are 3 significant figures.

**Rule 2: Zeros between non-zero digits are significant.**

Example:

\[
1005
\]

There are 4 significant figures.

**Rule 3: Leading zeros are not significant.**

Example:

\[
0.0045
\]

There are 2 significant figures.

**Rule 4: Trailing zeros after a decimal point are significant.**

Example:

\[
2.500
\]

There are 4 significant figures.

**Rule 5: Trailing zeros in a whole number without a decimal point may be ambiguous.**

For example, 1500 may represent 2, 3 or 4 significant figures depending on how it was measured.

Scientific notation removes this ambiguity:

\[
1.5\times10^3
\]

has 2 significant figures.

\[
1.500\times10^3
\]

has 4 significant figures.

## 5. Rounding Off

Rounding reduces the number of digits while retaining an appropriate level of precision.

Common rules:

- If the first discarded digit is less than 5, retain the preceding digit.
- If it is greater than 5, increase the preceding digit by 1.
- If it is exactly 5, a rounding convention must be specified. Many elementary problems use rounding upward; some scientific standards use round-to-even.

Examples using the common elementary convention:

\[
3.14159\approx3.14
\]

to 3 significant figures.

\[
7.268\approx7.27
\]

to 3 significant figures.

## 6. Significant Figures in Calculations

Different mathematical operations use different rules.

### Multiplication and division

The result should generally contain the same number of significant figures as the quantity with the fewest significant figures.

Example:

\[
2.5\times3.42=8.55
\]

The first quantity has 2 significant figures.

Therefore:

\[
8.55\approx8.6
\]

### Addition and subtraction

The result should generally have the same number of decimal places as the quantity with the fewest decimal places.

Example:

\[
12.35+4.2=16.55
\]

Since 4.2 has one decimal place:

\[
16.55\approx16.6
\]

Do not confuse decimal-place rules with significant-figure rules.

## 7. Types of Experimental Errors

An experimental error is the difference between a measured value and the true or accepted value.

Errors are commonly classified into systematic errors, random errors and gross errors.

### Systematic errors

Systematic errors shift measurements consistently in one direction.

Causes include:

- Incorrect instrument calibration.
- Zero error.
- Faulty experimental procedures.
- Consistent environmental effects.
- Parallax caused by a fixed observational arrangement.

Systematic errors may often be identified and corrected through calibration and improved experimental design.

### Random errors

Random errors cause unpredictable variations between repeated measurements.

Possible causes include:

- Small changes in environmental conditions.
- Variations in reaction time.
- Fluctuations in instrument readings.
- Limitations in observational judgement.

Repeated measurements and statistical analysis can help reduce their influence.

### Gross errors

Gross errors result from major mistakes.

Examples include:

- Recording an incorrect value.
- Reading the wrong scale.
- Using the wrong unit.
- Incorrectly setting up the apparatus.

Careful procedures and independent checks help prevent gross errors.

## 8. Absolute, Relative and Percentage Errors

Suppose the true or accepted value is \(x\), and the measured value is \(x_m\).

### Absolute error

Absolute error is the magnitude of the difference between the measured and accepted values.

\[
\Delta x=|x_m-x|
\]

For repeated measurements, the mean value is:

\[
\bar{x}=\frac{x_1+x_2+\cdots+x_n}{n}
\]

The absolute deviation of an individual reading is:

\[
\Delta x_i=|x_i-\bar{x}|
\]

The mean absolute error is:

\[
\Delta\bar{x}=
\frac{\sum_{i=1}^{n}|x_i-\bar{x}|}{n}
\]

### Relative error

Relative error is the ratio of absolute error to the magnitude of the measured or accepted reference value.

\[
\text{Relative error}=\frac{\Delta x}{|x|}
\]

### Percentage error

\[
\text{Percentage error}=
\frac{\Delta x}{|x|}\times100
\]

Example:

A measured length is 9.8 cm, while the accepted value is 10.0 cm.

Absolute error:

\[
\Delta x=|9.8-10.0|=0.2\ \text{cm}
\]

Percentage error:

\[
\frac{0.2}{10.0}\times100=2\%
\]

## 9. Propagation of Errors

When physical quantities are calculated using measured values, their uncertainties affect the final result.

### Addition and subtraction

If:

\[
z=x+y
\]

or:

\[
z=x-y
\]

The maximum absolute uncertainty is:

\[
\Delta z=\Delta x+\Delta y
\]

### Multiplication and division

If:

\[
z=xy
\]

or:

\[
z=\frac{x}{y}
\]

The maximum relative uncertainty is approximately:

\[
\frac{\Delta z}{|z|}
=
\frac{\Delta x}{|x|}
+
\frac{\Delta y}{|y|}
\]

### Powers

If:

\[
z=x^n
\]

Then:

\[
\frac{\Delta z}{|z|}
\approx |n|\frac{\Delta x}{|x|}
\]

These are commonly used maximum-uncertainty rules for small independent measurement uncertainties.

For statistically independent random uncertainties, uncertainty propagation may instead use quadrature rather than direct addition.

### Example: Area of a rectangle

Suppose:

\[
l=10.0\pm0.1\ \text{cm}
\]

\[
b=5.0\pm0.1\ \text{cm}
\]

Area:

\[
A=lb=50.0\ \text{cm}^2
\]

Maximum relative uncertainty:

\[
\frac{\Delta A}{A}
=
\frac{0.1}{10.0}+\frac{0.1}{5.0}
\]

\[
=0.01+0.02=0.03
\]

Therefore:

\[
\Delta A=50.0\times0.03=1.5\ \text{cm}^2
\]

Result:

\[
A=50.0\pm1.5\ \text{cm}^2
\]

## 10. Graphical Representation of Experimental Data

Graphs help identify relationships between physical quantities.

Important features include:

- Independent variable: The variable deliberately changed or controlled.
- Dependent variable: The variable measured in response.
- Horizontal axis: Usually represents the independent variable.
- Vertical axis: Usually represents the dependent variable.
- Gradient: Indicates the rate of change.
- Intercept: Indicates the value when the independent variable is zero.

For a straight-line relationship:

\[
y=mx+c
\]

where:

- \(m\) is the gradient.
- \(c\) is the vertical intercept.

The gradient is:

\[
m=\frac{\Delta y}{\Delta x}
\]

For example, a displacement-time graph has a gradient equal to velocity.

A velocity-time graph has a gradient equal to acceleration.

The area under a velocity-time graph represents displacement.

## 11. Reliability and Reproducibility

Reliable experimental results require more than a single measurement.

Good experimental practice includes:

- Repeating measurements.
- Using calibrated instruments.
- Recording units consistently.
- Controlling relevant variables.
- Avoiding parallax errors.
- Reporting uncertainty.
- Identifying anomalous readings.
- Using appropriate statistical methods.

Reproducibility means that other investigators can obtain compatible results when following the same experimental method under comparable conditions.

## Common Exam Traps

- Accuracy and precision are different concepts.
- A smaller least count generally permits finer measurement resolution but does not guarantee accuracy.
- Leading zeros are not significant figures.
- Trailing zeros after a decimal point are significant.
- Multiplication and division use significant-figure rules; addition and subtraction use decimal-place rules.
- Systematic errors do not necessarily disappear when measurements are repeated.
- Random errors can often be reduced through repeated measurements.
- For products and quotients, relative uncertainties add when calculating maximum uncertainty.
- The gradient of a graph must be interpreted using the physical quantities on its axes.

## Quiz

1. Which statement correctly describes precision?

- [ ] Closeness of a measurement to the accepted value
- [x] Closeness of repeated measurements to one another
- [ ] The smallest unit available in the SI system
- [ ] The absence of all systematic errors

> Precision describes the consistency of repeated measurements. Accuracy describes closeness to the accepted value.

2. How many significant figures are present in 0.004050?

- [ ] 3
- [x] 4
- [ ] 5
- [ ] 6

> The leading zeros are not significant. The digits 4, 0, 5 and the final 0 are significant because the zero between non-zero digits and the trailing decimal zero are retained.

3. A quantity is measured as 48.0 units, while its accepted value is 50.0 units. What is the percentage error?

- [ ] 2%
- [ ] 3%
- [x] 4%
- [ ] 5%

> Absolute error = |48.0 - 50.0| = 2.0. Percentage error = (2.0/50.0) × 100 = 4%.
