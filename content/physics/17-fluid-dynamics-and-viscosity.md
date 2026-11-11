---
title: Fluid Dynamics and Viscosity
level: intermediate
---

Fluid dynamics studies fluids in motion. It explains how liquids and gases flow through pipes, channels, vessels, and around moving objects.

Important concepts include streamline flow, continuity, Bernoulli's principle, viscosity, terminal velocity, and the resistance experienced by moving fluids.

## 1. Fluid Flow

Fluid flow describes the movement of liquid or gas particles.

Two broad types of flow are:

**Steady flow:** Fluid properties at a fixed point do not change with time.

**Unsteady flow:** Fluid properties at a fixed point change with time.

Steady flow is a useful idealisation in many fluid mechanics problems.

## 2. Streamline Flow

In streamline or laminar flow, fluid particles follow smooth paths called streamlines.

A streamline represents the direction of fluid velocity at each point.

Two streamlines cannot intersect in a steady flow because the fluid cannot have two different velocity directions at the same point.

At relatively low flow speeds, fluids are more likely to exhibit laminar behaviour.

## 3. Turbulent Flow

Turbulent flow involves irregular fluid motion, fluctuations, and mixing.

Characteristics include:
- Random variations in velocity.
- Formation of eddies and vortices.
- Increased mixing.
- Greater energy dissipation.

Turbulence is common at high flow speeds or under conditions that promote instability.

## 4. Equation of Continuity

The continuity equation expresses conservation of mass in fluid flow.

For steady incompressible flow:

\[
A_1v_1=A_2v_2
\]

Where:
- A = cross-sectional area
- v = fluid speed

If a pipe becomes narrower, the fluid speed increases.

For compressible flow, the general mass-flow relation is:

\[
\rho_1A_1v_1=\rho_2A_2v_2
\]

The mass flow rate is:

\[
\dot m=\rho Av
\]

Its SI unit is kg/s.

## 5. Bernoulli's Principle

Bernoulli's principle states that, for ideal steady flow along a streamline, the total mechanical energy per unit volume remains constant.

\[
P+\frac{1}{2}\rho v^2+\rho gh=\text{constant}
\]

Where:
- P = pressure energy per unit volume
- (1/2)rho v² = kinetic energy per unit volume
- rho gh = gravitational potential energy per unit volume

Between two points:

\[
P_1+\frac{1}{2}\rho v_1^2+\rho gh_1
=
P_2+\frac{1}{2}\rho v_2^2+\rho gh_2
\]

The equation assumes idealised conditions such as negligible viscosity and steady flow.

## 6. Interpretation of Bernoulli's Equation

When the height remains constant:

\[
P+\frac{1}{2}\rho v^2=\text{constant}
\]

For ideal flow, a higher fluid speed corresponds to lower static pressure along the streamline.

This relationship is important in the operation of:
- Venturimeters.
- Atomisers.
- Carburettors.
- Certain aerodynamic systems.

The complete aerodynamic behaviour of aircraft wings is more complex than a simple Bernoulli explanation.

## 7. Torricelli's Theorem

Torricelli's theorem gives the speed of efflux of an ideal liquid through a small opening at depth h below its free surface.

\[
v=\sqrt{2gh}
\]

This is equivalent to the speed acquired by an object falling freely through height h.

The theorem assumes ideal flow and a sufficiently large container compared with the outlet.

## 8. Viscosity

Viscosity is the internal resistance of a fluid to relative motion between adjacent layers.

It is analogous to internal friction.

The coefficient of dynamic viscosity is represented by eta.

For Newtonian fluids:

\[
F=\eta A\frac{dv}{dy}
\]

For a uniform velocity gradient:

\[
F=\eta A\frac{\Delta v}{\Delta y}
\]

The SI unit of dynamic viscosity is Pa s.

Examples:
- Honey has relatively high viscosity.
- Water has relatively low viscosity.
- Air also has viscosity, although it is less noticeable in everyday situations.

## 9. Newtonian and Non-Newtonian Fluids

A Newtonian fluid has a linear relationship between shear stress and velocity gradient at a given temperature and pressure.

Examples include water and air under ordinary conditions.

Non-Newtonian fluids do not follow this simple linear relationship.

Examples include:
- Toothpaste.
- Ketchup.
- Cornstarch suspensions.
- Some polymer solutions.

Their apparent viscosity may change with applied shear.

## 10. Temperature and Viscosity

For most liquids, viscosity decreases as temperature increases.

For most gases, viscosity increases as temperature increases.

The microscopic mechanisms responsible for this behaviour differ between liquids and gases.

## 11. Stokes' Law

For a small sphere moving slowly through a viscous fluid under laminar conditions, the viscous drag is:

\[
F=6\pi\eta rv
\]

Where:
- eta = dynamic viscosity
- r = sphere radius
- v = relative speed

Stokes' law applies under low-Reynolds-number conditions and is not valid for every flow situation.

## 12. Terminal Velocity

A falling object in a fluid may eventually reach a constant speed called terminal velocity.

At terminal velocity, the net force is zero.

For a small sphere falling through a fluid under Stokes' law:

\[
mg-F_B-F_D=0
\]

Where:
- mg = weight
- FB = buoyant force
- FD = viscous drag

For a sphere of density rho_s in a fluid of density rho_f:

\[
v_t=\frac{2r^2g(\rho_s-\rho_f)}{9\eta}
\]

This expression assumes Stokes' law is valid.

## 13. Reynolds Number

The Reynolds number is a dimensionless quantity used to compare inertial effects with viscous effects in fluid flow.

\[
Re=\frac{\rho vL}{\eta}
\]

Where:
- rho = fluid density
- v = characteristic speed
- L = characteristic length
- eta = dynamic viscosity

Low Reynolds numbers generally indicate viscous-dominated flow, while high Reynolds numbers indicate stronger inertial effects and greater likelihood of turbulence.

The transition depends on geometry, disturbances, and flow conditions; there is no universal threshold for every system.

## 14. Worked Numerical Examples

**Example 1: Continuity equation**

Water flows through a pipe with an area of 0.04 m² at 2 m/s. It enters a narrower section with an area of 0.01 m². Find the new speed.

\[
A_1v_1=A_2v_2
\]

\[
0.04\times2=0.01v_2
\]

\[
v_2=\frac{0.08}{0.01}
\]

\[
\boxed{v_2=8\,m/s}
\]

**Example 2: Bernoulli's equation**

At the same height, water moves from a region with speed 2 m/s to a region with speed 4 m/s. If the initial pressure is 100000 Pa and density is 1000 kg/m³, calculate the final pressure.

\[
P_1+\frac{1}{2}\rho v_1^2
=
P_2+\frac{1}{2}\rho v_2^2
\]

\[
P_2=P_1+\frac{1}{2}\rho(v_1^2-v_2^2)
\]

\[
P_2=100000+500(4-16)
\]

\[
\boxed{P_2=94000\,Pa}
\]

**Example 3: Reynolds number**

A fluid has density 1000 kg/m³, speed 2 m/s, characteristic length 0.01 m, and viscosity 0.001 Pa s.

\[
Re=\frac{\rho vL}{\eta}
\]

\[
Re=\frac{1000\times2\times0.01}{0.001}
\]

\[
\boxed{Re=20000}
\]

## 15. Applications

- Water distribution systems.
- Blood circulation.
- Aerodynamic design.
- Aircraft and vehicle engineering.
- Industrial pipelines.
- Lubrication systems.
- Weather and atmospheric modelling.

## Common Exam Traps

- Continuity represents conservation of mass.
- For incompressible flow, a smaller cross-sectional area means higher flow speed.
- Bernoulli's equation includes pressure, kinetic, and gravitational potential energy per unit volume.
- Bernoulli's principle has assumptions and cannot be applied indiscriminately to every flow.
- Viscosity is a property of a fluid, not simply its density.
- Stokes' law is valid only under suitable low-Reynolds-number conditions.
- Terminal velocity occurs when the resultant force becomes zero.

## Quiz

1. For steady incompressible flow, if the pipe area becomes half its original value, the flow speed becomes:

- [ ] Half
- [ ] One-fourth
- [x] Twice
- [ ] Unchanged

> From Av = constant, halving the area requires the speed to double.

2. The SI unit of dynamic viscosity is:

- [ ] N/m
- [x] Pa s
- [ ] kg/m³
- [ ] J/s

> Dynamic viscosity is measured in pascal-seconds.

3. At terminal velocity, the resultant force on a falling object is:

- [ ] Equal to its weight
- [ ] Maximum
- [x] Zero
- [ ] Always upward

> Terminal velocity occurs when weight, buoyancy, and drag balance so that acceleration becomes zero.