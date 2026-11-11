---
title: Experimental Physics, Practical Skills and Data Analysis
level: advanced
---

Physics develops through observation, experimentation, mathematical modelling and repeated testing.

An experiment is not merely an activity that produces a numerical answer. It is a systematic investigation designed to test a hypothesis, measure physical quantities and evaluate uncertainty.

This lesson develops the practical skills required to design experiments, operate instruments, analyse measurements and communicate scientific results.

## 1. The Scientific Method

A scientific investigation commonly involves:

1. Identifying a problem or observation.
2. Formulating a research question.
3. Developing a hypothesis.
4. Identifying variables.
5. Designing an experiment.
6. Collecting measurements.
7. Analysing data.
8. Evaluating uncertainty.
9. Drawing conclusions.
10. Repeating or improving the investigation.

A hypothesis should be testable through observation or experiment.

## 2. Variables in an Experiment

Three important categories of variables are:

**Independent variable:**

The quantity deliberately changed by the experimenter.

**Dependent variable:**

The quantity measured as a result of changing the independent variable.

**Controlled variables:**

Other quantities kept constant to ensure a fair investigation.

For example, when investigating how the extension of a spring depends on applied force:
- Independent variable: applied force.
- Dependent variable: extension.
- Controlled variables: spring used, temperature and experimental arrangement.

## 3. Measurement and Instruments

Different physical quantities require suitable instruments.

| Quantity | Common instrument |
|---|---|
| Length | Metre rule |
| Small diameter | Vernier calipers or micrometer screw gauge |
| Time | Stopwatch or electronic timer |
| Mass | Electronic balance |
| Temperature | Thermometer |
| Voltage | Voltmeter |
| Current | Ammeter |
| Resistance | Ohmmeter |
| Pressure | Pressure gauge |
| Frequency | Frequency counter or oscilloscope |

The instrument must have a suitable range and resolution.

## 4. Least Count and Resolution

The least count is the smallest measurement increment an instrument can resolve under its specified scale or design.

For a simple uniformly divided scale:

\[
LC=\frac{\text{Smallest main-scale division}}{\text{Number of subdivisions}}
\]

For digital instruments, resolution is commonly determined by the smallest displayed increment.

A smaller least count generally permits finer measurements, but it does not automatically guarantee greater accuracy.

## 5. Vernier Calipers

Vernier calipers can measure:
- External dimensions.
- Internal dimensions.
- Depth.

A typical reading is:

\[
\text{Reading}=\text{Main scale reading}+\text{Vernier contribution}
\]

The vernier contribution is:

\[
n\times LC
\]

Where n is the coinciding vernier division.

A zero error must be identified and corrected.

## 6. Micrometer Screw Gauge

A micrometer screw gauge measures very small dimensions.

Its pitch is the distance moved by the spindle in one complete rotation.

Least count:

\[
LC=\frac{\text{Pitch}}{\text{Number of circular-scale divisions}}
\]

A reading is obtained from the sleeve scale and circular scale.

The zero correction must be applied where necessary.

## 7. Accuracy and Precision

**Accuracy** describes how close a measured value is to the accepted or reference value.

**Precision** describes how closely repeated measurements agree with one another.

A set of measurements can be:
- Accurate and precise.
- Accurate on average but not precise.
- Precise but inaccurate.
- Neither accurate nor precise.

Precision does not guarantee accuracy.

## 8. Experimental Errors

Errors can be classified into several types.

**Systematic errors:**

Errors that consistently shift measurements in a particular direction or according to a repeatable pattern.

Examples:
- Incorrect calibration.
- Zero error.
- Consistent temperature effects.

**Random errors:**

Unpredictable variations between repeated measurements.

Examples:
- Reaction-time variations.
- Small environmental fluctuations.
- Electronic noise.

**Gross errors:**

Mistakes caused by incorrect reading, recording, calculation or experimental procedure.

Repeated measurements and careful experimental design help reduce errors.

## 9. Absolute, Relative and Percentage Error

Absolute error:

\[
\Delta x=|x_{\mathrm{measured}}-x_{\mathrm{reference}}|
\]

Relative error:

\[
\text{Relative error}=\frac{\Delta x}{|x_{\mathrm{reference}}|}
\]

Percentage error:

\[
\%\text{ error}=\frac{\Delta x}{|x_{\mathrm{reference}}|}\times100
\]

For a measured length of 9.8 cm and reference length of 10.0 cm:

\[
\Delta x=|9.8-10.0|=0.2\text{ cm}
\]

\[
\%\text{ error}=\frac{0.2}{10.0}\times100
\]

\[
\boxed{2\%}
\]

## 10. Repeated Measurements and Mean

When random errors are present, repeated measurements help estimate the central value.

Arithmetic mean:

\[
\bar x=\frac{x_1+x_2+\cdots+x_n}{n}
\]

For measurements:

9.8 cm, 10.1 cm and 10.0 cm:

\[
\bar x=\frac{9.8+10.1+10.0}{3}
\]

\[
\boxed{\bar x=9.97\text{ cm}}
\]

The mean is often a better estimate than a single measurement when the measurements are independent and random errors are appropriately distributed.

## 11. Propagation of Uncertainty

When quantities are combined mathematically, their uncertainties affect the final result.

For independent uncertainties:

**Addition or subtraction:**

Absolute uncertainties are commonly added as a conservative maximum estimate.

For independent random uncertainties, they may instead be combined in quadrature.

**Multiplication or division:**

Fractional uncertainties are combined.

For:

\[
Q=AB
\]

The approximate maximum fractional uncertainty is:

\[
\frac{\Delta Q}{Q}\approx\frac{\Delta A}{A}+\frac{\Delta B}{B}
\]

For:

\[
Q=A^n
\]

\[
\frac{\Delta Q}{Q}\approx|n|\frac{\Delta A}{A}
\]

These are first-order approximations.

## 12. Significant Figures

Significant figures communicate the precision of a reported measurement.

Examples:

- 25.4 has three significant figures.
- 0.0045 has two significant figures.
- 2.500 has four significant figures.

For multiplication and division, the final result is generally reported to the same number of significant figures as the least precise input.

Intermediate calculations should retain additional digits to reduce rounding errors.

## 13. Graphical Analysis

Graphs help identify relationships between physical quantities.

A graph should include:
- A descriptive title.
- Labelled axes.
- Units.
- Appropriate scale.
- Clearly plotted data points.
- A suitable best-fit line or curve.

Independent variables are commonly plotted on the horizontal axis and dependent variables on the vertical axis.

## 14. Gradient and Physical Meaning

The gradient of a straight line is:

\[
m=\frac{\Delta y}{\Delta x}
\]

The physical meaning depends on the quantities represented.

Examples:

**Position-time graph:**

Gradient represents velocity.

**Velocity-time graph:**

Gradient represents acceleration.

**Displacement-time graph for uniform motion:**

Gradient represents constant velocity.

**Current-voltage graph:**

Gradient may represent conductance if current is plotted vertically against voltage.

Always inspect the axis labels before interpreting a gradient.

## 15. Area Under a Graph

The area under a graph can represent an accumulated physical quantity.

Examples:

- Area under a velocity-time graph gives displacement.
- Area under a force-displacement graph gives work.
- Area under a current-time graph gives electric charge.

For electric charge:

\[
Q=\int I\,dt
\]

For constant current:

\[
Q=It
\]

## 16. Linearisation of Experimental Data

Some physical relationships are nonlinear but can be transformed into straight-line relationships.

For example:

\[
y=ax^2
\]

If y is plotted against x², a straight line through the origin is expected, with gradient a.

For exponential relationships:

\[
y=Ae^{kx}
\]

Taking natural logarithms:

\[
\ln y=\ln A+kx
\]

A plot of ln y against x should be linear, with gradient k.

Linearisation makes parameter estimation and comparison easier.

## 17. Important Physics Experiments

### Determination of g Using a Simple Pendulum

For small oscillations:

\[
T=2\pi\sqrt{\frac{L}{g}}
\]

Squaring:

\[
T^2=\frac{4\pi^2}{g}L
\]

Plot T² against L.

Gradient:

\[
m=\frac{4\pi^2}{g}
\]

Therefore:

\[
g=\frac{4\pi^2}{m}
\]

### Verification of Ohm's Law

Connect a resistor, ammeter, voltmeter and variable DC source.

Measure voltage and current for several settings.

Plot V against I.

For an ohmic resistor at constant physical conditions:

\[
V=IR
\]

The gradient of the V-I graph gives resistance.

### Determination of Spring Constant

Hooke's law:

\[
F=kx
\]

Plot force against extension.

The gradient gives the spring constant k.

### Determination of Focal Length

For a thin converging lens:

\[
\frac1f=\frac1v-\frac1u
\]

Using the Cartesian sign convention, measure object distance and image distance.

Calculate focal length for several observations and compare the results.

## 18. Oscilloscope Basics

A cathode-ray oscilloscope or digital oscilloscope displays electrical signals as functions of time.

It can be used to measure:
- Voltage.
- Time period.
- Frequency.
- Phase difference.
- Waveform shape.

Frequency:

\[
f=\frac1T
\]

If a signal completes one cycle in 2 milliseconds:

\[
T=2\times10^{-3}\text{ s}
\]

\[
f=\frac1{2\times10^{-3}}
\]

\[
\boxed{f=500\text{ Hz}}
\]

## 19. Good Experimental Practice

- Use suitable measuring instruments.
- Check calibration and zero error.
- Record measurements with units.
- Repeat measurements where appropriate.
- Keep controlled variables constant.
- Avoid parallax errors when reading scales.
- Record unexpected observations honestly.
- Use graphs and uncertainty analysis.
- Distinguish measured results from assumptions.
- Never modify experimental data merely to match an expected result.

## Common Exam Traps

- Accuracy and precision are different concepts.
- Repeated measurements help reduce random uncertainty but do not automatically remove systematic error.
- A smaller least count does not guarantee accuracy.
- Gradient depends on which quantity is plotted on each axis.
- Area under a graph has a physical interpretation only after identifying its axes.
- Percentage uncertainty and percentage error are related but not identical in every experimental context.
- Always retain units in final results.
- A physical conclusion should be supported by experimental evidence.

## Quiz

1. A student measures a length as 19.6 cm when the accepted value is 20.0 cm. What is the percentage error?

- [ ] 0.4%
- [x] 2%
- [ ] 4%
- [ ] 20%

> Absolute error = 0.4 cm. Percentage error = (0.4/20.0) × 100 = 2%.

2. The gradient of a velocity-time graph represents:

- [ ] Displacement
- [ ] Momentum
- [x] Acceleration
- [ ] Force

> Acceleration is the rate of change of velocity with time, so it is represented by the gradient of a velocity-time graph.

3. In a simple pendulum experiment, a graph of T² against L has gradient m. The acceleration due to gravity is:

- [ ] 2 pi m
- [ ] m divided by 4 pi squared
- [x] 4 pi squared divided by m
- [ ] 4 pi divided by m

> From T² = (4 pi²/g)L, the gradient is 4 pi²/g. Rearranging gives g = 4 pi²/m.