---
title: Chemical Kinetics and Reaction Rates
level: intermediate
---

# Lesson 29: Chemical Kinetics and Reaction Rates

Chemical kinetics studies the rates of chemical reactions and the factors that influence them. While thermodynamics predicts whether a reaction is energetically favourable, kinetics explains how quickly it proceeds. Reaction-rate studies are important in industrial production, combustion, drug stability, atmospheric chemistry, and biological processes.

## 1. Introduction to Chemical Kinetics

Chemical kinetics investigates:
- How fast reactants are consumed.
- How fast products are formed.
- How concentration affects reaction rate.
- How temperature influences reaction speed.
- How catalysts change reaction pathways.

A thermodynamically favourable reaction may still be extremely slow.

## 2. Rate of a Chemical Reaction

For a general reaction:

\[
aA+bB\rightarrow cC+dD
\]

The rate of reaction can be expressed using concentration changes.

\[
\boxed{
r=-\frac{1}{a}\frac{d[A]}{dt}
=-\frac{1}{b}\frac{d[B]}{dt}
=\frac{1}{c}\frac{d[C]}{dt}
=\frac{1}{d}\frac{d[D]}{dt}
}
\]

Reactant concentrations decrease, while product concentrations increase.

The negative sign ensures that the reaction rate is expressed as a positive quantity.

### 2.1 Average Rate

The average rate over a time interval is:

\[
\text{Average rate}=-\frac{\Delta[A]}{\Delta t}
\]

For a product:

\[
\text{Average rate}=\frac{\Delta[C]}{\Delta t}
\]

### 2.2 Instantaneous Rate

The instantaneous rate is the rate at a particular moment.

It is obtained from the slope of the concentration-time curve at that point.

## 3. Factors Affecting Reaction Rate

### 3.1 Concentration

Increasing reactant concentration generally increases reaction rate because particles collide more frequently.

### 3.2 Pressure

For gaseous reactants, increasing pressure by reducing volume generally increases concentration and may increase reaction rate.

### 3.3 Temperature

Increasing temperature usually increases reaction rate because:
- Particles move faster.
- Collision frequency may increase.
- A larger fraction of molecules has sufficient energy to react.

### 3.4 Surface Area

A finely divided solid generally reacts faster than a large solid piece because more surface is available for contact with other reactants.

### 3.5 Catalyst

A catalyst increases reaction rate by providing an alternative reaction pathway with a lower activation energy.

### 3.6 Nature of Reactants

Different substances react at different rates because of differences in:
- Bond strengths.
- Molecular structures.
- Physical states.
- Reaction mechanisms.

## 4. Rate Law

A rate law expresses the dependence of reaction rate on reactant concentrations.

For:

\[
aA+bB\rightarrow\text{Products}
\]

A possible experimentally determined rate law is:

\[
\boxed{r=k[A]^m[B]^n}
\]

Where:
- k = rate constant.
- m = order with respect to A.
- n = order with respect to B.

The overall reaction order is:

\[
\boxed{\text{Overall order}=m+n}
\]

Reaction orders are determined experimentally and cannot generally be obtained directly from the balanced overall equation.

## 5. Order of Reaction

### 5.1 Zero-Order Reaction

For a zero-order reaction:

\[
r=k
\]

The rate is independent of reactant concentration.

The integrated rate equation is:

\[
\boxed{[A]_t=[A]_0-kt}
\]

A plot of concentration against time is a straight line.

Its slope is -k.

### 5.2 First-Order Reaction

For a first-order reaction:

\[
r=k[A]
\]

The integrated rate equation is:

\[
\boxed{\ln\frac{[A]_0}{[A]_t}=kt}
\]

Using common logarithms:

\[
\boxed{\log\frac{[A]_0}{[A]_t}=\frac{kt}{2.303}}
\]

A plot of \(\ln[A]\) against time is a straight line with slope -k.

### 5.3 Second-Order Reaction

For a second-order reaction involving one reactant:

\[
r=k[A]^2
\]

The integrated rate equation is:

\[
\boxed{\frac{1}{[A]_t}=\frac{1}{[A]_0}+kt}
\]

A plot of \(1/[A]\) against time is a straight line with slope k.

## 6. Units of the Rate Constant

The units of k depend on the overall reaction order.

| Reaction order | Units of k |
|---|---|
| Zero | mol L⁻¹ s⁻¹ |
| First | s⁻¹ |
| Second | L mol⁻¹ s⁻¹ |
| Third | L² mol⁻² s⁻¹ |

For a general reaction of order n:

\[
\boxed{[k]=(\text{concentration})^{1-n}(\text{time})^{-1}}
\]

## 7. Half-Life of a Reaction

Half-life is the time required for the concentration of a reactant to decrease to half its initial value.

### 7.1 Zero-Order Reaction

\[
\boxed{t_{1/2}=\frac{[A]_0}{2k}}
\]

### 7.2 First-Order Reaction

\[
\boxed{t_{1/2}=\frac{0.693}{k}}
\]

The half-life of a first-order reaction is independent of initial concentration.

### 7.3 Second-Order Reaction

For a second-order reaction involving one reactant:

\[
\boxed{t_{1/2}=\frac{1}{k[A]_0}}
\]

## 8. Determination of Reaction Order

Reaction order can be determined using experimental concentration and rate measurements.

### 8.1 Initial Rate Method

The initial rate is measured at different initial concentrations.

For:

\[
r=k[A]^m[B]^n
\]

Comparing experiments in which only one concentration changes helps determine the corresponding order.

### 8.2 Integrated Rate Method

Experimental concentration-time data are compared with integrated rate equations.

- Linear [A] versus time suggests zero order.
- Linear ln[A] versus time suggests first order.
- Linear 1/[A] versus time suggests second order.

## 9. Pseudo-First-Order Reactions

A reaction may involve more than one reactant but behave as a first-order reaction when one reactant is present in large excess.

Example: hydrolysis of an ester in a large excess of water.

The water concentration changes negligibly during the reaction and is incorporated into the observed rate constant.

## 10. Common Exam Traps

- Reaction rate and reaction order are different concepts.
- Reaction orders must generally be determined experimentally.
- Overall reaction order is the sum of the exponents in the rate law.
- The balanced equation does not usually provide the rate law.
- First-order half-life is independent of initial concentration.
- The units of the rate constant depend on reaction order.
- Reactant disappearance rates must be divided by their stoichiometric coefficients when defining the overall reaction rate.

## 11. Applications of Chemical Kinetics

- Designing industrial reactors.
- Predicting food spoilage.
- Understanding drug decomposition.
- Controlling combustion.
- Studying atmospheric reactions.
- Optimising chemical manufacturing.
- Investigating enzyme-catalysed reactions.

## Quiz

1. What does the reaction rate measure?
   - [ ] Only the final amount of product
   - [x] The change in concentration per unit time
   - [ ] The equilibrium constant
   - [ ] The total heat released

   > Reaction rate measures how quickly reactant concentrations decrease or product concentrations increase with time.

2. What is the overall order of a reaction with rate law \(r=k[A]^2[B]\)?
   - [ ] First order
   - [ ] Second order
   - [x] Third order
   - [ ] Fourth order

   > The overall order is the sum of the concentration exponents: 2 + 1 = 3.

3. What is the half-life expression for a first-order reaction?
   - [ ] \([A]_0/2k\)
   - [x] \(0.693/k\)
   - [ ] \(1/k[A]_0\)
   - [ ] \(2k/[A]_0\)

   > The integrated first-order rate equation gives a half-life of \(0.693/k\), independent of initial concentration.