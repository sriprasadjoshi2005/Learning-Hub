---
title: Biotechnology — Principles and Tools
level: advanced
---

Biotechnology uses living organisms, cells, or biological molecules such as enzymes to develop products and processes beneficial to humans. **Recombinant DNA (rDNA) technology** is a form of genetic engineering in which DNA from different sources is combined *in vitro* to create new genetic combinations.

## Key Steps in Recombinant DNA Technology

The production of recombinant DNA and its introduction into a suitable host involve a sequence of major steps:

    Isolation of Genetic Material
                |
                v
       Cutting DNA with
      Restriction Enzymes
                |
                v
     Isolation of Gene of Interest
                |
                v
       Insertion into Vector
         using DNA Ligase
                |
                v
         Recombinant DNA
                |
                v
       Introduction into Host
          (Transformation)
                |
                v
       Selection of Transformants
                |
                v
       Cloning and Gene Expression
                |
                v
       Desired Product Formation

**Major stages:**

1. **Isolation of genetic material**: DNA containing the desired gene is extracted from the source organism.
2. **Cutting DNA at specific sites**: Restriction endonucleases cut both the desired DNA and the vector at suitable recognition sequences.
3. **Amplification of the gene of interest**: PCR can be used to produce multiple copies of the required DNA segment.
4. **Ligation**: DNA ligase joins the desired DNA fragment with the vector, producing recombinant DNA.
5. **Introduction into the host**: Recombinant DNA is transferred into a suitable host cell through transformation or another gene-transfer method.
6. **Selection and expression**: Cells containing recombinant DNA are identified, multiplied, and used to express the desired gene product.

## Major Molecular Tools

### 1. Restriction Endonucleases — Molecular Scissors

Restriction endonucleases are enzymes that recognize specific DNA sequences and cut double-stranded DNA at or near those sequences.

- They recognize specific **palindromic nucleotide sequences**.
- A DNA palindrome reads the same in the 5′ → 3′ direction on both complementary strands.
- They produce either **sticky ends** or **blunt ends**.
- Sticky ends contain short single-stranded overhangs that can pair with complementary sequences.

**Example: EcoRI**

EcoRI recognizes the palindromic sequence:

    5' — G A A T T C — 3'
          ↓
    3' — C T T A A G — 5'

It cuts between G and A on the two strands in a staggered manner, producing complementary sticky ends.

**Naming of EcoRI:**

| Letter | Meaning |
|---|---|
| E | Genus: *Escherichia* |
| co | Species: *coli* |
| R | Strain: RY13 |
| I | First restriction enzyme isolated from that strain |

### 2. Cloning Vectors — Molecular Vehicles

Cloning vectors are DNA molecules used to carry foreign DNA into host cells and facilitate its replication.

Common vectors include plasmids and bacteriophages.

**Essential features of a cloning vector:**

| Component | Function |
|---|---|
| Origin of replication (ori) | Site where replication begins; influences vector copy number |
| Selectable marker | Helps identify cells that have received the vector |
| Cloning site | Contains recognition sites for restriction enzymes where foreign DNA can be inserted |

**Example: pBR322**

pBR322 is a commonly studied plasmid cloning vector containing two selectable marker genes:

- **ampR**: Provides resistance to ampicillin.
- **tetR**: Provides resistance to tetracycline.

Insertion of foreign DNA into one of these marker genes can inactivate it, allowing recombinant and non-recombinant colonies to be distinguished through insertional inactivation.

**Important distinction:**

- A **transformant** is a host cell that has taken up the vector.
- A **recombinant transformant** contains a vector carrying the inserted foreign DNA.
- A **non-recombinant transformant** contains the vector without the desired DNA insert.

### 3. DNA Ligase — Molecular Glue

DNA ligase joins DNA fragments by forming **phosphodiester bonds** between adjacent nucleotides.

- It seals breaks in the sugar-phosphate backbone.
- It joins compatible DNA fragments after restriction enzyme digestion.
- It is essential for producing stable recombinant DNA molecules.

### 4. Host Organisms

Host cells receive recombinant DNA and allow its replication or expression.

Common hosts include:

- *Escherichia coli* — widely used bacterial host.
- Yeast — useful eukaryotic host.
- Plant and animal cells — used for producing specific proteins and other biotechnology products.

An ideal host should be easy to grow, genetically stable, and capable of supporting the replication or expression of the introduced DNA.

## Core Molecular Techniques

### 1. Gel Electrophoresis

Gel electrophoresis separates DNA fragments according to their size using an electric field.

**Principle:**

- DNA carries a net negative charge because of its phosphate backbone.
- When an electric field is applied, DNA moves towards the **positive electrode (anode)**.
- Smaller DNA fragments move faster and travel farther through the agarose gel than larger fragments.

**Procedure:**

1. DNA samples are loaded into wells in an agarose gel.
2. An electric field is applied.
3. DNA fragments migrate towards the anode.
4. Fragments separate according to size.
5. DNA bands are visualized using a suitable staining method.

**Visualization:**

- Ethidium bromide (EtBr) binds to DNA.
- Under ultraviolet (UV) illumination, stained DNA appears as bright orange fluorescent bands.
- Safer alternative DNA stains are also available.

**Elution:** The desired DNA band is cut from the agarose gel and the DNA is extracted from it. This process is called **elution**.

### 2. Polymerase Chain Reaction (PCR)

PCR is an *in vitro* technique used to amplify a specific DNA sequence, producing millions or billions of copies from a small initial quantity of DNA.

**Requirements:**

- Template DNA containing the target sequence.
- Two short DNA primers complementary to sequences flanking the target region.
- Thermostable DNA polymerase.
- Deoxyribonucleotide triphosphates (dNTPs).
- Suitable buffer and magnesium ions.

**Three major stages of PCR:**

| Stage | Approximate Temperature | Process |
|---|---:|---|
| Denaturation | 94–95°C | Double-stranded DNA separates into single strands |
| Annealing | 50–65°C | Primers bind to complementary template sequences |
| Extension | 72°C | DNA polymerase synthesizes new DNA strands |

**PCR cycle:**

    Double-Stranded DNA
             |
             v
       Denaturation
          94–95°C
             |
             v
        Single Strands
             |
             v
         Annealing
          50–65°C
             |
             v
        Primer Binding
             |
             v
         Extension
            72°C
             |
             v
       New DNA Strands
             |
             v
       Repeat the Cycle

**Taq Polymerase:**

- A heat-stable DNA polymerase isolated from the thermophilic bacterium *Thermus aquaticus*.
- Remains active during repeated high-temperature PCR cycles.
- Synthesizes DNA in the 5′ → 3′ direction.
- Has an optimum working temperature around 72°C.

**Amplification principle:**

Under ideal conditions, the amount of target DNA approximately doubles during each cycle.

\[
N = N_0 \times 2^n
\]

Where:

- \(N\) = Final number of DNA copies.
- \(N_0\) = Initial number of DNA molecules.
- \(n\) = Number of PCR cycles.

For example, one initial DNA molecule can theoretically produce:

\[
2^{10}=1024
\]

copies after 10 ideal cycles.

Actual amplification is lower because reaction efficiency decreases over successive cycles.

## Other Important Molecular Tools

### 1. DNA Polymerases

DNA polymerases synthesize new DNA strands using an existing DNA strand as a template.

- They add nucleotides to the 3′-OH end of a growing strand.
- DNA synthesis proceeds in the 5′ → 3′ direction.
- Thermostable DNA polymerases are essential for conventional PCR.

### 2. Competent Host Cells

DNA molecules cannot easily cross the cell membrane of ordinary bacterial cells. Therefore, host cells are made competent to take up foreign DNA.

**Methods of introducing DNA into host cells:**

| Method | Principle |
|---|---|
| Calcium chloride treatment followed by heat shock | Increases bacterial cell competence for DNA uptake |
| Microinjection | Direct injection of DNA into the nucleus of an animal cell |
| Biolistics / Gene gun | DNA-coated particles are shot into target cells |
| Disarmed pathogen vectors | Modified biological vectors deliver foreign DNA into host cells |

### 3. Selection of Recombinant Cells

After transformation, not every host cell necessarily receives recombinant DNA. Selection methods are used to identify the desired cells.

- **Selectable markers** distinguish cells containing vectors from cells without vectors.
- **Insertional inactivation** identifies recombinant vectors when insertion of foreign DNA disrupts a marker gene.
- Screening methods can distinguish recombinant colonies from non-recombinant colonies.

## Common Exam Traps

- **Restriction Endonuclease vs Exonuclease**: Endonucleases cut DNA at internal sites, whereas exonucleases remove nucleotides from DNA ends.
- **Sticky Ends vs Blunt Ends**: Sticky ends contain single-stranded overhangs; blunt ends have no overhangs.
- **EcoRI Recognition Site**: EcoRI recognizes \(5'\text{-GAATTC-}3'\), not \(5'\text{-AAGCTT-}3'\) (recognized by HindIII).
- **DNA Movement in Gel Electrophoresis**: DNA moves towards the positive anode because its phosphate backbone is negatively charged.
- **DNA Fragment Size**: Smaller fragments travel farther through agarose gel under the same conditions.
- **Elution**: Extraction of the desired DNA fragment from an agarose gel is called elution.
- **PCR Temperature Sequence**: Denaturation → Annealing → Extension. The exact annealing temperature depends on primer properties.
- **Taq Polymerase**: Isolated from *Thermus aquaticus*; it is thermostable and functions optimally around 72°C.
- **DNA Ligase**: Joins DNA fragments by forming phosphodiester bonds; restriction enzymes perform the cutting.
- **ori vs Selectable Marker**: ori controls replication, while selectable markers help identify cells carrying the vector.
- **Transformant vs Recombinant**: A transformant has taken up a vector; it is recombinant only if the vector contains the foreign DNA insert.

## Quiz

1. Which restriction endonuclease recognizes the palindromic DNA sequence \(5'\text{-GAATTC-}3'\) and produces sticky ends?

- [ ] HindIII
- [x] EcoRI
- [ ] BamHI
- [ ] PstI

> EcoRI recognizes the palindromic sequence \(5'\text{-GAATTC-}3'\) and cuts between G and A on the complementary strands, producing sticky ends.

2. During agarose gel electrophoresis, in which direction do negatively charged DNA fragments migrate?

- [ ] Towards the negative cathode
- [x] Towards the positive anode
- [ ] Towards the loading wells
- [ ] They remain stationary

> DNA has a negatively charged phosphate backbone and therefore migrates towards the positive electrode, called the anode.

3. Which component of a cloning vector is primarily responsible for initiating DNA replication and influencing its copy number?

- [ ] Selectable marker
- [ ] Cloning site
- [x] Origin of replication (ori)
- [ ] DNA ligase

> The origin of replication (ori) is the sequence where replication begins. It also influences the number of copies of the vector maintained inside the host cell.

4. A researcher inserts foreign DNA into the tetracycline-resistance gene of pBR322. Which phenomenon can help distinguish recombinant colonies from non-recombinant colonies?

- [ ] DNA denaturation
- [ ] Elution
- [x] Insertional inactivation
- [ ] DNA amplification

> Insertion of foreign DNA disrupts the tetracycline-resistance gene, making recombinant cells tetracycline-sensitive. This allows them to be distinguished from non-recombinant cells using appropriate antibiotic selection.

5. Which enzyme is used to join a foreign DNA fragment with a plasmid vector during recombinant DNA formation?

- [ ] Restriction endonuclease
- [x] DNA ligase
- [ ] Helicase
- [ ] RNA polymerase

> DNA ligase joins compatible DNA fragments by forming phosphodiester bonds between adjacent nucleotides in the sugar-phosphate backbone.

6. What is the correct sequence of temperature-dependent stages in a conventional PCR cycle?

- [ ] Annealing → Extension → Denaturation
- [x] Denaturation → Annealing → Extension
- [ ] Extension → Denaturation → Annealing
- [ ] Denaturation → Extension → Annealing

> PCR begins with denaturation to separate DNA strands, followed by primer annealing and extension by DNA polymerase.

7. Which enzyme is commonly used in PCR because it can withstand repeated high-temperature denaturation steps?

- [ ] DNA Polymerase I from *E. coli*
- [x] Taq Polymerase from *Thermus aquaticus*
- [ ] Reverse transcriptase from retroviruses
- [ ] RNA polymerase from *E. coli*

> Taq Polymerase is obtained from the thermophilic bacterium *Thermus aquaticus*. Its thermostability allows it to remain functional during repeated PCR cycles.

8. A DNA sample produces several bands after agarose gel electrophoresis. Which fragments will generally travel the greatest distance from the wells?

- [ ] The largest DNA fragments
- [ ] Fragments with the highest molecular mass
- [x] The smallest DNA fragments
- [ ] All fragments travel the same distance

> Smaller DNA fragments move more easily through the pores of the agarose gel and therefore travel farther than larger fragments under the same conditions.

9. A desired DNA band is identified under UV illumination and cut out of an agarose gel. What is the process of extracting DNA from this gel fragment called?

- [ ] Transformation
- [ ] Denaturation
- [x] Elution
- [ ] Annealing

> Elution is the process of recovering the desired DNA fragment from the excised agarose gel piece for subsequent use in recombinant DNA technology.

10. Under ideal conditions, how many DNA copies can theoretically be produced from one initial DNA molecule after 10 PCR cycles?

- [ ] 100
- [ ] 512
- [x] 1024
- [ ] 2048

> The number of copies doubles in every ideal PCR cycle. Therefore, \(N=1\times 2^{10}=1024\) DNA molecules after 10 cycles.
