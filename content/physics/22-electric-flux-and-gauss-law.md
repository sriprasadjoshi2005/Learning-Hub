---
title: Electric Flux and Gauss's Law
level: intermediate
---

Electric flux and Gauss's law provide a powerful mathematical framework for studying electric fields, particularly when charges are distributed symmetrically. These concepts simplify the calculation of electric fields produced by spherical, cylindrical and planar charge distributions.

## 1. Electric Flux

Electric flux measures how much electric field passes through a given surface.

For a uniform electric field passing through a flat surface:

ΦE = EA cos θ

Where:
- ΦE = electric flux
- E = magnitude of the electric field
- A = surface area
- θ = angle between the electric field and the surface normal

The surface normal is an imaginary line perpendicular to the surface.

The SI unit of electric flux is N m²/C.

Electric flux is a scalar quantity.

## 2. Understanding the Angle in Electric Flux

The angle in the electric flux equation is measured between the electric field and the normal to the surface, not between the field and the surface itself.

Three important cases:

### Field Perpendicular to the Surface

The field is parallel to the surface normal.

θ = 0 degrees

ΦE = EA

Flux is maximum and positive.

### Field Parallel to the Surface

The field is perpendicular to the surface normal.

θ = 90 degrees

ΦE = 0

No electric flux passes through the surface in this orientation.

### Field Opposite to the Surface Normal

θ = 180 degrees

ΦE = -EA

Flux is maximum in magnitude but negative.

## 3. Electric Flux Through an Arbitrary Surface

For a non-uniform electric field or curved surface, electric flux is calculated using integration.

dΦE = E · dA

Total flux:

ΦE = ∫ E · dA

Here dA is a small area vector directed perpendicular to the surface.

For a closed surface, the integral is written as:

ΦE = ∮ E · dA

The symbol ∮ indicates integration over a closed surface.

## 4. Open and Closed Surfaces

An open surface has a boundary and does not completely enclose a region of space.

Examples include:
- A flat sheet.
- An open cylinder.
- A curved hemispherical surface without its base.

A closed surface completely encloses a volume.

Examples include:
- A sphere.
- A cube.
- A closed cylinder.

Gauss's law is applied to closed surfaces, also called Gaussian surfaces.

## 5. Gaussian Surface

A Gaussian surface is an imaginary closed surface selected to simplify the calculation of electric flux.

It does not need to be a physical object.

The choice of Gaussian surface depends on the symmetry of the charge distribution.

Common choices:

- Spherical Gaussian surface for spherical symmetry.
- Cylindrical Gaussian surface for cylindrical symmetry.
- Pillbox-shaped Gaussian surface for planar symmetry.

A suitable Gaussian surface makes the electric field constant over certain portions of the surface or makes the flux through some portions zero.

## 6. Gauss's Law

Gauss's law states that the total electric flux through any closed surface is equal to the net charge enclosed divided by the permittivity of free space.

ΦE = Qenclosed / ε0

In integral form:

∮ E · dA = Qenclosed / ε0

Where:
- Qenclosed = net charge enclosed by the Gaussian surface
- ε0 = permittivity of free space

Gauss's law is one of Maxwell's fundamental equations.

## 7. Important Interpretations of Gauss's Law

### Enclosed Charge Determines Net Flux

The total electric flux through a closed surface depends only on the net charge enclosed by it.

It does not depend on:
- The shape of the Gaussian surface.
- The size of the Gaussian surface.
- The position of charges outside the surface.

### External Charges

Charges outside a Gaussian surface may produce electric fields on the surface, but their net contribution to the total flux through that closed surface is zero.

### Zero Enclosed Charge

If the net enclosed charge is zero:

ΦE = 0

This does not necessarily mean that the electric field is zero everywhere on the surface.

Positive and negative flux contributions may cancel.

## 8. Electric Field Due to an Infinite Straight Line Charge

Consider an infinitely long straight wire with uniform linear charge density λ.

Linear charge density is:

λ = Q / L

Choose a cylindrical Gaussian surface of radius r and length L around the wire.

By symmetry:
- The electric field is radial.
- Its magnitude is constant on the curved surface.
- The flux through the flat end faces is zero.

Using Gauss's law:

E × 2πrL = λL / ε0

Therefore:

E = λ / (2πε0r)

The electric field decreases inversely with distance from the line charge.

## 9. Electric Field Due to an Infinite Plane Sheet

Consider an infinitely large non-conducting plane sheet with uniform surface charge density σ.

Surface charge density is:

σ = Q / A

Choose a cylindrical pillbox Gaussian surface crossing the sheet.

Electric flux passes through the two flat faces.

Using Gauss's law:

2EA = σA / ε0

Therefore:

E = σ / (2ε0)

The electric field is independent of the distance from an ideal infinite plane sheet.

For a positively charged sheet, the field points away from the sheet on both sides.

For a negatively charged sheet, the field points towards the sheet.

## 10. Electric Field Near a Conducting Surface

For a conductor in electrostatic equilibrium, the electric field immediately outside its surface is perpendicular to the surface.

The magnitude is:

E = σ / ε0

Where σ is the local surface charge density.

Inside the conducting material:

E = 0

This result applies to an ideal conductor in electrostatic equilibrium.

## 11. Electric Field Due to a Uniformly Charged Spherical Shell

Consider a thin spherical shell with total charge Q and radius R.

### Outside the Shell

For r greater than R, choose a spherical Gaussian surface of radius r.

By symmetry:

E × 4πr² = Q / ε0

Therefore:

E = kQ / r²

The field behaves as if all the charge were concentrated at the centre.

### Inside the Shell

For r less than R, the Gaussian surface encloses no charge.

Therefore:

E = 0

This result is important in electrostatics.

## 12. Electric Field Due to a Uniformly Charged Solid Sphere

Consider a non-conducting solid sphere of radius R with uniformly distributed total charge Q.

### Outside the Sphere

For r greater than or equal to R:

E = kQ / r²

### Inside the Sphere

For r less than R, the enclosed charge is proportional to the volume enclosed.

Qenclosed = Q(r³ / R³)

Applying Gauss's law:

E × 4πr² = Qr³ / (ε0R³)

Therefore:

E = kQr / R³

The electric field inside the uniformly charged solid sphere increases linearly with distance from the centre.

At the centre:

E = 0

At the surface, the field reaches kQ/R².

## 13. Applications of Gauss's Law

Gauss's law is useful in:

- Calculating electric fields for highly symmetric charge distributions.
- Understanding the electric field inside and outside conductors.
- Analysing charged spherical shells.
- Studying long charged wires and plane sheets.
- Deriving relationships between electric charge and electric fields.
- Understanding electrostatic shielding.

Gauss's law is always valid, but it is especially useful for calculating electric fields when sufficient symmetry exists.

## 14. Numerical Applications

**Example 1: Electric flux**

A uniform electric field of 200 N/C passes through a flat surface of area 0.5 m². The field makes an angle of 60 degrees with the surface normal.

ΦE = EA cos θ

ΦE = 200 × 0.5 × cos 60 degrees

ΦE = 50 N m²/C

**Example 2: Flux through a closed surface**

A closed surface encloses a charge of 4 μC.

ΦE = Q / ε0

ΦE = (4 × 10^-6) / (8.854 × 10^-12)

ΦE ≈ 4.52 × 10^5 N m²/C

## Common Exam Traps

- Electric flux is a scalar quantity, not a vector.
- The angle in EA cos θ is measured from the surface normal.
- Zero electric flux does not necessarily mean zero electric field.
- Gauss's law uses net enclosed charge, not all charges in the universe.
- Charges outside a closed Gaussian surface do not change its net flux.
- The electric field of an infinite line charge varies as 1/r.
- The electric field of an infinite plane sheet is independent of distance.
- The electric field inside a uniformly charged thin spherical shell is zero.
- The electric field inside a uniformly charged solid non-conducting sphere varies linearly with distance from its centre.
- Gauss's law is valid for all closed surfaces, but symmetry determines whether it is convenient for calculating the electric field.

## Quiz

1. The electric flux through a flat surface is maximum when the electric field makes which angle with the surface normal?

- [ ] 90 degrees
- [x] 0 degrees
- [ ] 45 degrees
- [ ] 180 degrees

> Flux is ΦE = EA cos θ. Its maximum positive value occurs when cos θ = 1.

2. The electric field due to an infinitely long straight line charge varies with distance r as:

- [ ] 1/r²
- [x] 1/r
- [ ] r²
- [ ] Constant

> Gauss's law gives E = λ/(2πε0r), so the field is inversely proportional to r.

3. The electric field inside a uniformly charged thin spherical shell is:

- [ ] Maximum at the centre
- [ ] Proportional to distance from the centre
- [x] Zero everywhere inside
- [ ] Inversely proportional to the square of distance

> A Gaussian surface inside the shell encloses no charge. By spherical symmetry and Gauss's law, the electric field is zero.