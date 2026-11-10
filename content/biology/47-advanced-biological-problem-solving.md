---
title: Advanced Biological Problem Solving
level: exam
---

University entrance examinations require the integration of biological concepts with mathematical calculations, multi-step genetics problems, and analytical data interpretation. Effective problem-solving involves identifying the relevant formula, understanding the biological conditions, substituting values correctly, and interpreting the result.

## Core Problem-Solving Formulas

### 1. Population Genetics — Hardy-Weinberg Equilibrium

The Hardy-Weinberg principle describes the genetic equilibrium of an ideal population in which allele and genotype frequencies remain constant across generations.

**Allele frequency equation:**

$$
p+q=1
$$

**Genotype frequency equation:**

$$
p^2+2pq+q^2=1
$$

Where:

| Symbol | Meaning |
|---|---|
| \(p\) | Frequency of dominant allele \(A\) |
| \(q\) | Frequency of recessive allele \(a\) |
| \(p^2\) | Frequency of homozygous dominant genotype \(AA\) |
| \(2pq\) | Frequency of heterozygous genotype \(Aa\) |
| \(q^2\) | Frequency of homozygous recessive genotype \(aa\) |

**Important calculation patterns:**

If the frequency of a recessive phenotype is given:

$$
q^2=\text{Recessive phenotype frequency}
$$

Therefore:

$$
q=\sqrt{q^2}
$$

Then calculate:

$$
p=1-q
$$

The heterozygous frequency is:

$$
2pq=2(1-q)q
$$

**Example:**

In a population, 16% of individuals show a recessive phenotype. Calculate the percentage of heterozygous individuals.

Given:

$$
q^2=0.16
$$

Taking the square root:

$$
q=\sqrt{0.16}=0.4
$$

Therefore:

$$
p=1-0.4=0.6
$$

Heterozygous frequency:

$$
2pq=2(0.6)(0.4)=0.48
$$

**Answer:**

$$
\boxed{48\%}
$$

**Conditions for Hardy-Weinberg equilibrium:**

- Very large population.
- Random mating.
- No mutation.
- No migration or gene flow.
- No natural selection.

### 2. Genetics — Recombination Frequency and Gene Mapping

Recombination frequency measures the proportion of recombinant offspring produced during genetic crossing over.

$$
\text{RF (\%)}=
\frac{\text{Number of Recombinant Progeny}}
{\text{Total Number of Progeny}}\times100
$$

The relationship between recombination frequency and genetic distance is:

$$
1\%\text{ recombination}=1\text{ cM}
$$

Where:

- **cM** = Centimorgan.
- **Map unit (mu)** = Unit of genetic distance.
- Higher recombination frequency generally indicates greater distance between linked genes.

**Example:**

A test cross produces the following offspring:

| Offspring type | Number |
|---|---:|
| AB | 420 |
| ab | 410 |
| Ab | 85 |
| aB | 85 |

The most frequent classes are parental types, while the less frequent classes are recombinant types.

Total progeny:

$$
420+410+85+85=1000
$$

Recombinant progeny:

$$
85+85=170
$$

Recombination frequency:

$$
RF=\frac{170}{1000}\times100
$$

$$
RF=17\%
$$

Therefore:

$$
\boxed{17\text{ cM}}
$$

**Important:** Recombination frequency cannot exceed 50%. At larger distances, multiple crossing-over events can cause the observed recombination frequency to underestimate the actual map distance.

### 3. Molecular Genetics — DNA Calculations

DNA length can be calculated using the distance between successive base pairs in the double helix.

**Distance between adjacent base pairs:**

$$
0.34\text{ nm}=0.34\times10^{-9}\text{ m}
$$

**Length of double-stranded DNA:**

$$
L=(\text{Number of Base Pairs})\times0.34\text{ nm}
$$

Alternatively:

$$
L=(\text{Number of Base Pairs})\times
(0.34\times10^{-9}\text{ m})
$$

**Example:**

Calculate the length of a DNA molecule containing 5,000 base pairs.

$$
L=5000\times0.34\text{ nm}
$$

$$
L=1700\text{ nm}
$$

$$
\boxed{L=1.7\ \mu\text{m}}
$$

**Additional DNA relationships:**

For a double-stranded DNA molecule containing \(n\) base pairs:

- Total nucleotides:

$$
2n
$$

- Total nitrogenous bases:

$$
2n
$$

- Total phosphodiester bonds in linear double-stranded DNA:

$$
2(n-1)=2n-2
$$

- Total phosphodiester bonds in circular double-stranded DNA:

$$
2n
$$

- Total hydrogen bonds:

$$
H=2N_{AT}+3N_{GC}
$$

Where \(N_{AT}\) and \(N_{GC}\) represent the numbers of A–T and G–C base pairs, respectively.

**Base composition:**

According to Chargaff's rule:

$$
A=T,\qquad G=C
$$

For double-stranded DNA:

$$
A+G=T+C
$$

### 4. Cell Division — Chromosome and DNA Content

Chromosome number and DNA content must be considered separately when solving cell division problems.

**Important notation:**

- \(n\) = Haploid chromosome number.
- \(2n\) = Diploid chromosome number.
- \(C\) = DNA content of one haploid unreplicated genome.

**Changes during the cell cycle:**

| Stage | Chromosome Number | DNA Content |
|---|---:|---:|
| G1 phase | 2n | 2C |
| S phase | 2n | 2C → 4C |
| G2 phase | 2n | 4C |
| Metaphase of mitosis | 2n | 4C |
| After mitosis and cytokinesis | 2n per daughter cell | 2C per daughter cell |
| Metaphase I of meiosis | 2n | 4C |
| After meiosis I | n | 2C |
| After meiosis II | n | 1C |

**Critical distinction:**

During S-phase, DNA replication doubles the DNA content, but the chromosome number remains unchanged because each replicated chromosome consists of two sister chromatids.

**Meiosis example:**

A diploid cell has:

$$
2n=24
$$

Its unreplicated DNA content is:

$$
2C=40\text{ pg}
$$

After S-phase:

- Chromosome number = 24.
- DNA content = 80 pg.

After meiosis I:

- Chromosome number = 12 per daughter cell.
- DNA content = 40 pg per daughter cell.

After meiosis II:

- Chromosome number = 12 per daughter cell.
- DNA content = 20 pg per daughter cell.

### 5. Ecology — Energy Transfer and Trophic Levels

The **10% law**, proposed by Raymond Lindeman, states that approximately 10% of the energy available at one trophic level is transferred to the next trophic level.

The remaining energy is used in metabolic activities or lost as heat and through other processes.

**Energy transfer formula:**

$$
E_n=E_1(0.10)^{n-1}
$$

Where:

- \(E_n\) = Energy available at trophic level \(n\).
- \(E_1\) = Energy available at the producer level.
- \(n\) = Trophic level number.

**Example:**

If producers contain 40,000 J of energy:

| Trophic Level | Organism Group | Energy Available |
|---|---|---:|
| T1 | Producers | 40,000 J |
| T2 | Primary consumers | 4,000 J |
| T3 | Secondary consumers | 400 J |
| T4 | Tertiary consumers | 40 J |

Therefore, energy available to tertiary consumers is:

$$
\boxed{40\text{ J}}
$$

### 6. Population Ecology — Growth Rate Calculations

Population growth depends on births, deaths, immigration, and emigration.

**Population change:**

$$
N_{t+1}=N_t+(B+I)-(D+E)
$$

Where:

- \(N_t\) = Initial population.
- \(B\) = Number of births.
- \(I\) = Number of immigrants.
- \(D\) = Number of deaths.
- \(E\) = Number of emigrants.

**Exponential growth:**

Occurs when resources are unlimited and environmental resistance is negligible.

$$
\frac{dN}{dt}=rN
$$

Integrated equation:

$$
N_t=N_0e^{rt}
$$

Where:

- \(N_0\) = Initial population.
- \(N_t\) = Population after time \(t\).
- \(r\) = Intrinsic rate of natural increase.
- \(e\) = Base of natural logarithms.

**Logistic growth:**

Occurs when resources are limited and population growth is restricted by carrying capacity.

$$
\frac{dN}{dt}=rN\left(\frac{K-N}{K}\right)
$$

Where:

- \(K\) = Carrying capacity.
- \(N\) = Current population.
- \(r\) = Intrinsic rate of natural increase.

Maximum population growth rate occurs when:

$$
N=\frac{K}{2}
$$

Therefore:

$$
\left(\frac{dN}{dt}\right)_{\max}=\frac{rK}{4}
$$

## Advanced Problem Patterns

    Problem Framework
            |
    -----------------------------------------------
    |                    |                        |
    v                    v                        v
    Genetics &          Cell Division &           Ecological
    Pedigrees            DNA Calculations          Numericals
    |                    |                        |
    v                    v                        v
    Allele frequencies   Chromosome counts         Energy transfer
    Genotype ratios      DNA content               Population growth
    Map distances        DNA replication           Carrying capacity
    Test crosses         Cell cycle stages         Trophic levels

## Common Exam Traps

- **Allele vs Genotype Frequency**: \(p\) and \(q\) represent allele frequencies, whereas \(p^2\), \(2pq\), and \(q^2\) represent genotype frequencies.
- **Recessive Phenotype Calculation**: If the recessive phenotype frequency is given, it represents \(q^2\), not \(q\). Take the square root before calculating \(p\).
- **Parental vs Recombinant Progeny**: In a linked-gene test cross, the more frequent classes are generally parental, while the less frequent classes are recombinant.
- **Recombination Frequency**: Count both recombinant classes and divide by the total progeny, not by the number of parental progeny.
- **Map Distance**: A recombination frequency of 17% corresponds to an estimated map distance of 17 cM.
- **Maximum Recombination Frequency**: Observed recombination frequency cannot exceed 50%, even when genes are far apart or located on different chromosomes.
- **DNA Length**: Use the number of base pairs, not the total number of individual nucleotides, when calculating double-stranded DNA length.
- **Phosphodiester Bonds**: Linear double-stranded DNA has \(2n-2\) phosphodiester bonds, whereas circular double-stranded DNA has \(2n\).
- **DNA Content vs Chromosome Number**: During S-phase, DNA content doubles from 2C to 4C, but chromosome number remains 2n.
- **Meiosis I vs Meiosis II**: Meiosis I separates homologous chromosomes; meiosis II separates sister chromatids.
- **DNA Content after Meiosis I**: Each daughter cell is haploid but still contains duplicated chromosomes, giving DNA content of 2C.
- **10% Energy Transfer**: The tertiary consumer is at T4, so energy is transferred three times from the producer level.
- **Exponential vs Logistic Growth**: Exponential growth produces a J-shaped curve, while logistic growth produces a sigmoid curve.
- **Carrying Capacity**: At \(N=K\), the net logistic population growth rate becomes zero.

## Quiz

1. In a population under Hardy-Weinberg equilibrium, 9% of individuals exhibit a recessive phenotype. What percentage of the population is expected to be heterozygous?

- [ ] 9%
- [ ] 21%
- [x] 42%
- [ ] 49%

> The recessive phenotype frequency is \(q^2=0.09\). Therefore, \(q=0.3\) and \(p=1-0.3=0.7\). The heterozygous frequency is \(2pq=2(0.7)(0.3)=0.42\), or 42%.

2. A test cross produces 600 offspring, of which 90 belong to one recombinant class and 90 belong to the other recombinant class. What is the estimated genetic distance between the two genes?

- [ ] 15 cM
- [x] 30 cM
- [ ] 45 cM
- [ ] 60 cM

> Total recombinant progeny = \(90+90=180\). Therefore, \(RF=(180/600)\times100=30\%\). The estimated map distance is 30 cM.

3. A linear double-stranded DNA molecule contains 2,500 base pairs. What is its approximate length?

- [ ] 425 nm
- [x] 850 nm
- [ ] 1,250 nm
- [ ] 1,700 nm

> The distance between adjacent base pairs is 0.34 nm. Therefore, DNA length \(=2500\times0.34=850\text{ nm}\).

4. A linear double-stranded DNA molecule contains 1,000 base pairs. How many phosphodiester bonds are present in its two strands combined?

- [ ] 999
- [ ] 1,000
- [ ] 1,998
- [x] 1,998? 

> For linear double-stranded DNA, each strand contains \(n-1\) phosphodiester bonds. Therefore, the total is \(2(n-1)=2(1000-1)=1998\) bonds.

5. A diploid cell has 2n = 16 chromosomes and an unreplicated DNA content of 24 pg. What will be its chromosome number and DNA content per cell immediately after S-phase?

- [ ] 32 chromosomes; 48 pg
- [x] 16 chromosomes; 48 pg
- [ ] 16 chromosomes; 24 pg
- [ ] 8 chromosomes; 48 pg

> During S-phase, DNA replication doubles the DNA content from 24 pg to 48 pg. However, chromosome number remains 16 because each chromosome now consists of two sister chromatids.

6. A mammalian cell has 2n = 20 chromosomes and 60 pg of DNA before replication. What will be the chromosome number and DNA content in each cell after completion of meiosis I?

- [ ] 20 chromosomes; 60 pg
- [ ] 10 chromosomes; 60 pg
- [x] 10 chromosomes; 30 pg
- [ ] 20 chromosomes; 30 pg

> DNA content doubles to 120 pg during S-phase. Meiosis I separates homologous chromosomes and divides the replicated DNA between two cells. Each daughter cell therefore contains 10 chromosomes and 60 pg of DNA. 

7. Producers in an ecosystem contain 80,000 J of energy. According to the 10% law, how much energy will be available to secondary consumers?

- [ ] 8,000 J
- [x] 800 J
- [ ] 80 J
- [ ] 8 J

> Producers are T1, primary consumers are T2, and secondary consumers are T3. Energy is transferred twice: \(80,000\times0.1\times0.1=800\text{ J}\).

8. A population of 500 individuals experiences 80 births, 30 deaths, 20 immigrants, and 10 emigrants during a particular period. What is its final population?

- [ ] 520
- [ ] 540
- [x] 560
- [ ] 580

> Final population \(=500+(80+20)-(30+10)=500+100-40=560\) individuals.

9. A population has a carrying capacity of 1,000 individuals and an intrinsic growth rate of 0.2 per unit time. According to the logistic growth model, what is the maximum population growth rate?

- [ ] 25 individuals per unit time
- [ ] 40 individuals per unit time
- [x] 50 individuals per unit time
- [ ] 200 individuals per unit time

> Maximum logistic growth occurs at \(N=K/2\). The maximum growth rate is \(rK/4=(0.2\times1000)/4=50\) individuals per unit time.

10. In a Hardy-Weinberg population, the frequency of the dominant allele is 0.8. What is the expected frequency of heterozygous individuals?

- [ ] 0.04
- [ ] 0.16
- [x] 0.32
- [ ] 0.64

> Given \(p=0.8\), the recessive allele frequency is \(q=1-0.8=0.2\). The heterozygous frequency is \(2pq=2(0.8)(0.2)=0.32\), or 32%.
``
