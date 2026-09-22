"""
All lesson and quiz content lives here as plain Python data.

Structure (unchanged from before):
    SUBJECTS[key] = {"name": str, "lessons": [{"id", "title", "content", "quiz"}]}
    quiz item      = {"question": str, "options": [str, ...], "answer": int}  # 0-based

To keep this file short, lessons are built with the L() helper below instead of
repeating the same dict keys 90 times. The resulting data shape is identical.

To add a lesson: append L(next_id, "Title", "<p>...</p>", (question, options, answer), (...))
Lesson ids inside a subject must be consecutive integers starting at 1 — lessons unlock in order.
Each lesson has exactly 2 quiz questions, so scores are reported out of 2.
"""

QUIZ_LENGTH = 2


def L(lesson_id, title, content, *questions):
    """Build one lesson. Each question is a (text, options, answer_index) tuple."""
    return {
        "id": lesson_id,
        "title": title,
        "content": content.strip(),
        "quiz": [{"question": q, "options": list(o), "answer": a} for q, o, a in questions],
    }


def score(lesson, responses):
    """Return (correct, total) for a list of chosen option indices."""
    quiz = lesson["quiz"]
    correct = sum(1 for q, r in zip(quiz, responses) if r == q["answer"])
    return correct, len(quiz)


SUBJECTS = {
    "maths": {
        "name": "Mathematics",
        "lessons": [
            L(1, "Introduction to Algebra", """
                <p>Algebra uses letters such as <b>x</b> and <b>y</b> to stand in for unknown numbers,
                so that one rule can describe many situations at once.</p>
                <p>An equation like <code>x + 5 = 12</code> asks: what number, added to 5, gives 12?
                Subtracting 5 from both sides leaves <code>x = 7</code>.</p>
                <p>The golden rule: whatever you do to one side of an equation you must do to the
                other, so the two sides stay balanced.</p>
            """,
              ("Solve: x + 5 = 12. What is x?", ("5", "6", "7", "17"), 2),
              ("Why must the same operation be applied to both sides of an equation?",
               ("To make the numbers smaller", "To keep both sides equal",
                "To remove the letter x", "It is optional"), 1)),
            L(2, "Linear Equations", """
                <p>A linear equation has variables raised only to the power 1, e.g. <code>3x - 4 = 11</code>.
                Solve it by undoing operations in reverse order: add 4, then divide by 3, giving <code>x = 5</code>.</p>
                <p>When the unknown appears on both sides, gather the x terms on one side first:
                <code>5x - 2 = 3x + 8</code> becomes <code>2x = 10</code>, so <code>x = 5</code>.</p>
                <p>Always check by substituting your answer back into the original equation.</p>
            """,
              ("Solve: 3x - 4 = 11.", ("x = 3", "x = 5", "x = 7", "x = 15"), 1),
              ("Solving 5x - 2 = 3x + 8, the sensible first step is to:",
               ("Divide everything by 5", "Subtract 3x from both sides",
                "Add 2 to only the left side", "Square both sides"), 1)),
            L(3, "Expanding and Factorising", """
                <p>Expanding removes brackets: <code>3(x + 4) = 3x + 12</code>. Every term inside the
                bracket is multiplied by the term outside.</p>
                <p>For two brackets, multiply each term in the first by each term in the second:
                <code>(x + 2)(x + 3) = x&sup2; + 5x + 6</code>.</p>
                <p>Factorising is the reverse: rewrite an expression as a product. For
                <code>x&sup2; + 5x + 6</code> look for two numbers that multiply to 6 and add to 5 &mdash; 2 and 3.</p>
            """,
              ("Expand (x + 2)(x + 3).", ("x&sup2; + 6", "x&sup2; + 5x + 6", "x&sup2; + 5x", "2x + 3"), 1),
              ("To factorise x&sup2; + 7x + 10 you need two numbers that:",
               ("Add to 10 and multiply to 7", "Multiply to 10 and add to 7",
                "Are both equal to 5", "Subtract to give 10"), 1)),
            L(4, "Quadratic Equations", """
                <p>A quadratic has the form <code>ax&sup2; + bx + c = 0</code> and can have two, one, or no
                real solutions.</p>
                <p>If it factorises, use the fact that a product is zero only when a factor is zero:
                <code>(x - 2)(x - 3) = 0</code> gives <code>x = 2</code> or <code>x = 3</code>.</p>
                <p>Otherwise use the formula <code>x = (-b &plusmn; &radic;(b&sup2; - 4ac)) / 2a</code>.
                The part <code>b&sup2; - 4ac</code> is the discriminant: negative means no real roots.</p>
            """,
              ("The solutions of (x - 2)(x - 3) = 0 are:",
               ("x = -2 and x = -3", "x = 2 and x = 3", "x = 6 only", "x = 5"), 1),
              ("If b&sup2; - 4ac is negative, the quadratic has:",
               ("Two real roots", "One repeated root", "No real roots", "Infinitely many roots"), 2)),
            L(5, "Angles and Shapes", """
                <p>Angles on a straight line add to 180&deg;, and angles around a point add to 360&deg;.</p>
                <p>A triangle's three interior angles always total <b>180&deg;</b>; a quadrilateral's total 360&deg;.
                A square has four equal sides and four 90&deg; angles.</p>
                <p>Perimeter is the total distance around a shape; area is the space it covers.</p>
            """,
              ("The interior angles of a triangle add up to:",
               ("90 degrees", "180 degrees", "270 degrees", "360 degrees"), 1),
              ("A triangle has angles of 40&deg; and 75&deg;. The third angle is:",
               ("55 degrees", "65 degrees", "75 degrees", "115 degrees"), 1)),
            L(6, "Triangles and Pythagoras", """
                <p>In a right-angled triangle the longest side, opposite the right angle, is the
                <b>hypotenuse</b>.</p>
                <p>Pythagoras' theorem states <code>a&sup2; + b&sup2; = c&sup2;</code>, where c is the hypotenuse.
                With sides 3 and 4, the hypotenuse is &radic;25 = 5.</p>
                <p>The theorem works only for right-angled triangles, and can also be used backwards to
                test whether a triangle contains a right angle.</p>
            """,
              ("A right-angled triangle has short sides 3 and 4. The hypotenuse is:",
               ("5", "6", "7", "12"), 0),
              ("Pythagoras' theorem can be applied to:",
               ("Any triangle", "Right-angled triangles only",
                "Squares only", "Triangles with equal sides only"), 1)),
            L(7, "Circles", """
                <p>The radius runs from the centre to the edge; the diameter is twice the radius.</p>
                <p>Circumference = <code>2&pi;r</code> and area = <code>&pi;r&sup2;</code>, where &pi; &asymp; 3.14.</p>
                <p>So a circle of radius 5 cm has circumference about 31.4 cm and area about 78.5 cm&sup2;.</p>
            """,
              ("The area of a circle is given by:", ("2&pi;r", "&pi;r&sup2;", "&pi;d", "r&sup2;"), 1),
              ("A circle has diameter 10 cm. Its circumference is roughly:",
               ("15.7 cm", "31.4 cm", "78.5 cm", "100 cm"), 1)),
            L(8, "Fractions, Decimals and Percentages", """
                <p>These are three ways of writing the same idea: 1/4 = 0.25 = 25%.</p>
                <p>To find a percentage of an amount, convert to a decimal and multiply:
                15% of 80 is 0.15 &times; 80 = 12.</p>
                <p>For a percentage increase, multiply by (1 + rate). A 20% rise on 50 gives
                50 &times; 1.2 = 60.</p>
            """,
              ("What is 15% of 80?", ("8", "12", "15", "20"), 1),
              ("Increasing 50 by 20% gives:", ("55", "60", "70", "100"), 1)),
            L(9, "Ratio and Proportion", """
                <p>A ratio compares quantities, e.g. 2:3. To share &pound;50 in the ratio 2:3, note there are
                5 parts, so each part is &pound;10, giving &pound;20 and &pound;30.</p>
                <p>Two quantities are in direct proportion when doubling one doubles the other.</p>
                <p>In inverse proportion their product stays constant: as one doubles, the other halves.</p>
            """,
              ("Sharing 50 in the ratio 2:3 gives:", ("20 and 30", "25 and 25", "10 and 40", "15 and 35"), 0),
              ("In inverse proportion, when one quantity doubles the other:",
               ("Doubles", "Halves", "Stays the same", "Increases by 2"), 1)),
            L(10, "Indices and Standard Form", """
                <p>Indices show repeated multiplication: <code>2&sup5; = 32</code>. Rules:
                <code>a&#8319; &times; a&#7504; = a&#8319;&#8314;&#7504;</code> and <code>a&#8319; &divide; a&#7504; = a&#8319;&#8315;&#7504;</code>.</p>
                <p>Anything to the power 0 equals 1, and a negative index means a reciprocal:
                <code>2&#8315;&sup3; = 1/8</code>.</p>
                <p>Standard form writes numbers as <code>A &times; 10&#8319;</code> with 1 &le; A &lt; 10, so
                4500 becomes <code>4.5 &times; 10&sup3;</code>.</p>
            """,
              ("Write 4500 in standard form.",
               ("45 &times; 10&sup2;", "4.5 &times; 10&sup3;", "4.5 &times; 10&#8308;", "0.45 &times; 10&#8308;"), 1),
              ("What is the value of 2&#8315;&sup3;?", ("-8", "-6", "1/8", "6"), 2)),
            L(11, "Coordinates and Straight Line Graphs", """
                <p>Points are written as (x, y), measured from the origin (0, 0).</p>
                <p>A straight line has equation <code>y = mx + c</code>, where m is the gradient
                (steepness) and c is the y-intercept.</p>
                <p>Gradient = change in y divided by change in x. Parallel lines share the same gradient.</p>
            """,
              ("In y = mx + c, the letter m represents the:",
               ("y-intercept", "Gradient", "x value", "Area under the line"), 1),
              ("The line y = 3x + 2 crosses the y-axis at:",
               ("(0, 2)", "(2, 0)", "(0, 3)", "(3, 2)"), 0)),
            L(12, "Sequences", """
                <p>A sequence is an ordered list of terms. In an <b>arithmetic</b> sequence you add a
                constant difference each time: 3, 7, 11, 15 (difference 4).</p>
                <p>The nth term of that sequence is <code>4n - 1</code>, which lets you jump straight to
                any term.</p>
                <p>In a <b>geometric</b> sequence you multiply by a constant ratio: 2, 6, 18, 54.</p>
            """,
              ("The nth term of 3, 7, 11, 15, ... is:", ("n + 4", "4n - 1", "4n + 3", "3n"), 1),
              ("The sequence 2, 6, 18, 54 is:",
               ("Arithmetic with difference 4", "Geometric with ratio 3",
                "Neither", "Geometric with ratio 2"), 1)),
            L(13, "Averages and Data", """
                <p>The <b>mean</b> is the total divided by how many values there are; the <b>median</b>
                is the middle value when ordered; the <b>mode</b> is the most common value.</p>
                <p>The range (largest minus smallest) measures spread, not average.</p>
                <p>For 2, 3, 3, 8 the mean is 4, the median 3, the mode 3 and the range 6.</p>
            """,
              ("For the data 2, 3, 3, 8 the mean is:", ("3", "4", "5", "6"), 1),
              ("The range of a data set measures:",
               ("The most common value", "The middle value", "The spread", "The total"), 2)),
            L(14, "Introduction to Trigonometry", """
                <p>In a right-angled triangle, the ratios of sides depend only on the angles:
                <code>sin&theta; = opp/hyp</code>, <code>cos&theta; = adj/hyp</code>,
                <code>tan&theta; = opp/adj</code> (remember SOH CAH TOA).</p>
                <p>Use them to find a missing side when you know an angle and one side.</p>
                <p>To find a missing angle, use the inverse functions, e.g. <code>&theta; = tan&#8315;&sup1;(opp/adj)</code>.</p>
            """,
              ("Which ratio equals opposite divided by hypotenuse?",
               ("sin", "cos", "tan", "None"), 0),
              ("To find an angle when you know the opposite and adjacent sides, use:",
               ("sin", "cos", "tan inverse", "Pythagoras"), 2)),
            L(15, "Introduction to Calculus", """
                <p>Calculus studies change. <b>Differentiation</b> finds the gradient of a curve at a
                point &mdash; the instantaneous rate of change.</p>
                <p>The rule for powers: if <code>y = x&#8319;</code> then <code>dy/dx = nx&#8319;&#8315;&sup1;</code>.
                So for <code>y = x&sup3;</code>, <code>dy/dx = 3x&sup2;</code>.</p>
                <p>Where the gradient is zero the curve has a turning point &mdash; a maximum or minimum.</p>
            """,
              ("If y = x&sup3;, then dy/dx is:", ("3x", "x&sup2;", "3x&sup2;", "3x&#8308;"), 2),
              ("At a maximum or minimum point of a curve, the gradient is:",
               ("Zero", "One", "Always positive", "Undefined"), 0)),
        ],
    },
}

SUBJECTS["physics"] = {
    "name": "Physics",
    "lessons": [
        L(1, "Introduction to Motion", """
            <p>Motion describes how an object's position changes over time.</p>
            <p><b>Speed</b> is distance divided by time; <b>velocity</b> is speed together with a
            direction, which makes it a vector quantity.</p>
            <p>A car travelling 100 km in 2 hours has an average speed of 50 km/h, even if it sped
            up and slowed down along the way.</p>
        """,
          ("A car travels 100 km in 2 hours. Its average speed is:",
           ("25 km/h", "50 km/h", "100 km/h", "200 km/h"), 1),
          ("What makes velocity different from speed?",
           ("It includes direction", "It is always larger", "It has no units", "There is no difference"), 0)),
        L(2, "Acceleration and Motion Graphs", """
            <p>Acceleration is the rate of change of velocity, measured in m/s&sup2;:
            <code>a = (v - u) / t</code>.</p>
            <p>On a distance-time graph the gradient gives speed; a horizontal line means the object
            is stationary.</p>
            <p>On a velocity-time graph the gradient gives acceleration and the area under the line
            gives the distance travelled.</p>
        """,
          ("The gradient of a velocity-time graph represents:",
           ("Distance", "Speed", "Acceleration", "Force"), 2),
          ("A car goes from 0 to 20 m/s in 4 s. Its acceleration is:",
           ("4 m/s&sup2;", "5 m/s&sup2;", "20 m/s&sup2;", "80 m/s&sup2;"), 1)),
        L(3, "Forces and Newton's Laws", """
            <p>A force is a push or a pull, measured in newtons. Newton's first law: an object stays
            at rest or moves at constant velocity unless a resultant force acts on it (inertia).</p>
            <p>Newton's second law: <code>Force = mass &times; acceleration</code>.</p>
            <p>Newton's third law: every action has an equal and opposite reaction, acting on a
            different object.</p>
        """,
          ("A 5 kg mass accelerates at 3 m/s&sup2;. The resultant force is:",
           ("1.7 N", "8 N", "15 N", "45 N"), 2),
          ("Newton's first law is also called the law of:",
           ("Gravity", "Inertia", "Reaction", "Momentum"), 1)),
        L(4, "Gravity, Mass and Weight", """
            <p>Mass is the amount of matter in an object and does not change with location; weight is
            the force of gravity on that mass.</p>
            <p><code>Weight = mass &times; gravitational field strength</code>. On Earth g &asymp; 10 N/kg,
            so a 60 kg person weighs about 600 N.</p>
            <p>On the Moon g is about one sixth of Earth's, so the same person weighs far less but has
            exactly the same mass.</p>
        """,
          ("The weight of a 60 kg person on Earth (g = 10 N/kg) is about:",
           ("6 N", "60 N", "600 N", "6000 N"), 2),
          ("Taking an object to the Moon changes its:",
           ("Mass only", "Weight only", "Both mass and weight", "Neither"), 1)),
        L(5, "Work, Energy and Power", """
            <p>Work done = force &times; distance moved in the direction of the force, measured in joules.</p>
            <p>Energy is conserved: it transfers between stores such as kinetic
            (<code>&frac12;mv&sup2;</code>) and gravitational potential (<code>mgh</code>).</p>
            <p>Power is the rate of energy transfer: <code>P = E / t</code>, measured in watts.</p>
        """,
          ("Power is best described as:",
           ("Total energy used", "Energy transferred per second", "Force times distance", "Mass times acceleration"), 1),
          ("A force of 20 N moves an object 3 m. Work done is:",
           ("6 J", "23 J", "60 J", "600 J"), 2)),
        L(6, "Momentum", """
            <p>Momentum = mass &times; velocity, measured in kg m/s, and it is a vector.</p>
            <p>In a closed system total momentum before a collision equals total momentum after &mdash;
            the principle of conservation of momentum.</p>
            <p>Crumple zones and airbags increase the time taken to change momentum, which reduces the
            force experienced.</p>
        """,
          ("Momentum is calculated as:",
           ("mass &times; acceleration", "mass &times; velocity", "force &times; time", "&frac12;mv&sup2;"), 1),
          ("Airbags reduce injury because they:",
           ("Increase the force", "Increase the time over which momentum changes",
            "Reduce the mass", "Increase the velocity"), 1)),
        L(7, "Density and Pressure", """
            <p>Density = mass / volume, usually in kg/m&sup3;. Objects less dense than a fluid float in it.</p>
            <p>Pressure = force / area, measured in pascals. A sharp knife has a tiny contact area, so
            a modest force gives a very high pressure.</p>
            <p>In a liquid, pressure increases with depth and acts in all directions.</p>
        """,
          ("Pressure is calculated as:",
           ("Force &times; area", "Force / area", "Area / force", "Mass / volume"), 1),
          ("Pressure in a liquid increases as you go:",
           ("Deeper", "Shallower", "Sideways only", "It stays constant"), 0)),
        L(8, "Heat and Temperature", """
            <p>Temperature measures how hot something is; thermal energy depends on both temperature
            and mass.</p>
            <p>Heat transfers by conduction (through solids), convection (in fluids, driven by density
            differences) and radiation (infrared waves, needing no medium).</p>
            <p>Insulation, such as trapped air in a jumper, slows conduction and convection.</p>
        """,
          ("Energy from the Sun reaches Earth by:",
           ("Conduction", "Convection", "Radiation", "Evaporation"), 2),
          ("Convection currents occur because heated fluid becomes:",
           ("Denser and sinks", "Less dense and rises", "Solid", "Colder"), 1)),
        L(9, "Waves", """
            <p>Waves transfer energy without transferring matter. In <b>transverse</b> waves the
            oscillation is perpendicular to travel (light); in <b>longitudinal</b> waves it is parallel (sound).</p>
            <p>Key terms: amplitude, wavelength, frequency (hertz) and period.</p>
            <p>The wave equation is <code>v = f&lambda;</code>: speed equals frequency times wavelength.</p>
        """,
          ("The wave equation is:",
           ("v = f + &lambda;", "v = f&lambda;", "v = &lambda;/f", "f = v&lambda;"), 1),
          ("Sound waves are:",
           ("Transverse", "Longitudinal", "Electromagnetic", "Stationary"), 1)),
        L(10, "Sound and Hearing", """
            <p>Sound is a longitudinal wave of compressions and rarefactions, so it needs a medium and
            cannot travel through a vacuum.</p>
            <p>Higher frequency is heard as higher pitch; larger amplitude is heard as greater loudness.</p>
            <p>Sound travels faster in solids than in liquids, and faster in liquids than in gases,
            because particles are closer together.</p>
        """,
          ("Sound cannot travel through:",
           ("Water", "Steel", "A vacuum", "Air"), 2),
          ("Increasing the frequency of a sound increases its:",
           ("Loudness", "Pitch", "Speed", "Amplitude"), 1)),
        L(11, "Light and Optics", """
            <p>Light travels in straight lines and reflects so that the angle of incidence equals the
            angle of reflection.</p>
            <p>Refraction is the bending of light when it changes speed entering a new medium, which is
            why a straw looks bent in water.</p>
            <p>Converging lenses bring parallel rays to a focus and are used in cameras and eyes;
            white light can be dispersed into a spectrum by a prism.</p>
        """,
          ("Light bending as it passes from air into glass is called:",
           ("Reflection", "Refraction", "Diffraction", "Dispersion"), 1),
          ("In reflection, the angle of incidence is:",
           ("Always 90&deg;", "Equal to the angle of reflection", "Twice the angle of reflection", "Always zero"), 1)),
        L(12, "Current, Voltage and Resistance", """
            <p>Current is the rate of flow of charge, measured in amperes; voltage is the energy given
            per unit charge, measured in volts.</p>
            <p>Resistance opposes current. Ohm's law states <code>V = IR</code>.</p>
            <p>So a 12 V supply pushing 2 A through a component means the component has a resistance
            of 6 ohms.</p>
        """,
          ("Ohm's law is written as:", ("V = I/R", "V = IR", "I = VR", "R = VI"), 1),
          ("A 12 V supply drives 2 A through a resistor. Its resistance is:",
           ("2 &Omega;", "6 &Omega;", "14 &Omega;", "24 &Omega;"), 1)),
        L(13, "Electrical Circuits", """
            <p>In a <b>series</b> circuit there is one path: current is the same everywhere and the
            supply voltage is shared between components.</p>
            <p>In a <b>parallel</b> circuit there are branches: each branch gets the full supply voltage
            and the currents in the branches add up to the total.</p>
            <p>Adding resistors in series increases total resistance; adding them in parallel decreases it.</p>
        """,
          ("In a series circuit, the current:",
           ("Is the same at every point", "Splits between components",
            "Is zero", "Doubles at each component"), 0),
          ("Components in parallel each receive:",
           ("A share of the supply voltage", "The full supply voltage", "No voltage", "Double the voltage"), 1)),
        L(14, "Magnetism and Electromagnetism", """
            <p>Magnets have north and south poles; like poles repel and unlike poles attract.</p>
            <p>A current in a wire creates a magnetic field around it. Coiling the wire into a solenoid
            around an iron core makes an electromagnet that can be switched on and off.</p>
            <p>A current-carrying wire in a magnetic field experiences a force &mdash; the motor effect.
            Moving a magnet near a coil induces a voltage, which is how generators work.</p>
        """,
          ("Two north poles placed near each other will:",
           ("Attract", "Repel", "Do nothing", "Become south poles"), 1),
          ("Moving a magnet into a coil of wire will:",
           ("Induce a voltage", "Destroy the magnet", "Stop the current", "Have no effect"), 0)),
        L(15, "Atoms and Radioactivity", """
            <p>An atom has a tiny nucleus of protons and neutrons, surrounded by electrons.</p>
            <p>Unstable nuclei decay and emit radiation: alpha (stopped by paper), beta (stopped by thin
            aluminium) and gamma (reduced by thick lead).</p>
            <p>Half-life is the time for half the undecayed nuclei in a sample to decay &mdash; a random
            process that is predictable only on average.</p>
        """,
          ("Which type of radiation is the most penetrating?",
           ("Alpha", "Beta", "Gamma", "They are equal"), 2),
          ("Half-life is the time taken for:",
           ("All nuclei to decay", "Half the undecayed nuclei to decay",
            "The mass to double", "Radiation to stop entirely"), 1)),
    ],
}

SUBJECTS["chemistry"] = {
    "name": "Chemistry",
    "lessons": [
        L(1, "States of Matter", """
            <p>Matter exists mainly as solids, liquids and gases, differing in how tightly their
            particles are held together.</p>
            <p>Solids have a fixed shape and volume; liquids take the shape of their container; gases
            expand to fill any space.</p>
            <p>Changes of state are physical, not chemical: melting, boiling, condensing and freezing
            rearrange particles but do not make new substances.</p>
        """,
          ("Which state has a fixed volume but takes the shape of its container?",
           ("Solid", "Liquid", "Gas", "Plasma"), 1),
          ("Melting ice into water is:",
           ("A chemical change", "A physical change", "Combustion", "Oxidation"), 1)),
        L(2, "Atomic Structure", """
            <p>Atoms contain protons (positive) and neutrons (neutral) in the nucleus, with electrons
            (negative) in shells around it.</p>
            <p>The atomic number is the number of protons and defines the element; the mass number is
            protons plus neutrons.</p>
            <p><b>Isotopes</b> are atoms of the same element with different numbers of neutrons, such as
            carbon-12 and carbon-14.</p>
        """,
          ("The atomic number of an element equals its number of:",
           ("Neutrons", "Protons", "Electrons plus neutrons", "Shells"), 1),
          ("Isotopes of an element differ in their number of:",
           ("Protons", "Electrons", "Neutrons", "Shells"), 2)),
        L(3, "The Periodic Table", """
            <p>Elements are arranged in order of atomic number. Vertical <b>groups</b> share chemical
            properties; horizontal <b>periods</b> show gradual change.</p>
            <p>Group 1 alkali metals are highly reactive, group 7 halogens are reactive non-metals, and
            group 0 noble gases are inert because their outer shells are full.</p>
            <p>The group number tells you the number of electrons in the outer shell.</p>
        """,
          ("Elements in the same group have the same number of:",
           ("Protons", "Neutrons", "Outer-shell electrons", "Shells"), 2),
          ("Noble gases are unreactive because their outer shells are:",
           ("Empty", "Full", "Half full", "Missing"), 1)),
        L(4, "Chemical Bonding", """
            <p>Atoms bond to achieve full outer shells. In <b>ionic</b> bonding a metal transfers
            electrons to a non-metal, forming charged ions that attract strongly.</p>
            <p>In <b>covalent</b> bonding two non-metals share pairs of electrons, as in water.</p>
            <p>In <b>metallic</b> bonding positive ions sit in a sea of delocalised electrons, which is
            why metals conduct electricity and can be bent.</p>
        """,
          ("Sodium chloride is held together by:",
           ("Covalent bonds", "Ionic bonds", "Metallic bonds", "No bonds"), 1),
          ("Metals conduct electricity because they contain:",
           ("Shared pairs of electrons", "Delocalised electrons", "Neutrons", "Negative ions"), 1)),
        L(5, "Formulae and Equations", """
            <p>A chemical formula shows the elements present and how many atoms of each:
            <code>H&#8322;O</code> has two hydrogens and one oxygen.</p>
            <p>Equations must be balanced because atoms are never created or destroyed:
            <code>2H&#8322; + O&#8322; &rarr; 2H&#8322;O</code>.</p>
            <p>State symbols (s), (l), (g) and (aq) add useful detail.</p>
        """,
          ("Equations must be balanced because:",
           ("It looks neater", "Atoms are conserved in a reaction",
            "Energy must be equal", "Charges must be zero"), 1),
          ("How many atoms in total are in one molecule of H&#8322;O?",
           ("2", "3", "4", "1"), 1)),
        L(6, "The Mole and Reacting Masses", """
            <p>The mole is the chemist's counting unit: one mole contains 6.02 &times; 10&sup2;&sup3; particles
            (Avogadro's number).</p>
            <p>One mole of a substance has a mass in grams equal to its relative formula mass, so one
            mole of water is 18 g.</p>
            <p><code>moles = mass / relative formula mass</code>, which lets you predict how much product
            a reaction will give.</p>
        """,
          ("Moles are calculated as:",
           ("mass &times; Mr", "mass / Mr", "Mr / mass", "mass + Mr"), 1),
          ("36 g of water (Mr = 18) is how many moles?",
           ("0.5", "1", "2", "18"), 2)),
        L(7, "Acids, Bases and pH", """
            <p>Acids release H&#8314; ions in solution; alkalis release OH&#8315; ions. The pH scale runs
            from 0 (strongly acidic) to 14 (strongly alkaline), with 7 neutral.</p>
            <p>Neutralisation produces a salt and water:
            <code>acid + base &rarr; salt + water</code>.</p>
            <p>Indicators such as litmus or universal indicator show pH by changing colour.</p>
        """,
          ("A solution with pH 2 is:",
           ("Strongly alkaline", "Neutral", "Strongly acidic", "Weakly alkaline"), 2),
          ("Acid + base produces:",
           ("Salt + water", "Hydrogen + oxygen", "Only a gas", "A metal"), 0)),
        L(8, "Types of Chemical Reaction", """
            <p>Common patterns include combustion (burning in oxygen), oxidation (gain of oxygen or loss
            of electrons) and reduction (the opposite).</p>
            <p>In displacement a more reactive element takes the place of a less reactive one; in
            thermal decomposition heat breaks a compound apart.</p>
            <p>Reactions that release heat are exothermic; those that absorb it are endothermic.</p>
        """,
          ("A reaction that releases heat to the surroundings is:",
           ("Endothermic", "Exothermic", "Neutral", "Reversible"), 1),
          ("Heating calcium carbonate to give calcium oxide and carbon dioxide is:",
           ("Displacement", "Thermal decomposition", "Combustion", "Neutralisation"), 1)),
        L(9, "Metals and the Reactivity Series", """
            <p>Metals can be ranked by reactivity: potassium, sodium and calcium are very reactive,
            while gold and platinum are very unreactive.</p>
            <p>A more reactive metal displaces a less reactive one from its compound, e.g. zinc
            displaces copper from copper sulfate.</p>
            <p>Very reactive metals are extracted by electrolysis; less reactive ones can be reduced
            with carbon.</p>
        """,
          ("Which metal is the most reactive?",
           ("Gold", "Copper", "Potassium", "Silver"), 2),
          ("Zinc added to copper sulfate solution will:",
           ("Do nothing", "Displace the copper", "Dissolve the sulfate", "Form a gas only"), 1)),
        L(10, "Electrolysis", """
            <p>Electrolysis uses electricity to break down an ionic compound that is molten or dissolved,
            so its ions are free to move.</p>
            <p>Positive ions (cations) move to the negative cathode; negative ions (anions) move to the
            positive anode.</p>
            <p>It is used to extract aluminium from its ore and to electroplate objects with a thin
            metal layer.</p>
        """,
          ("Positive ions travel towards the:",
           ("Anode", "Cathode", "Battery", "Beaker"), 1),
          ("Electrolysis requires the compound to be:",
           ("Solid", "Molten or dissolved", "A gas", "Unreactive"), 1)),
        L(11, "Rates of Reaction", """
            <p>Reaction rate measures how quickly reactants are used up or products formed.</p>
            <p>Rate increases with higher temperature, higher concentration or pressure, smaller
            particle size (larger surface area) and with a catalyst.</p>
            <p>Collision theory explains this: reactions happen when particles collide often enough and
            with enough energy.</p>
        """,
          ("Which change will slow a reaction down?",
           ("Raising the temperature", "Using a catalyst",
            "Using larger lumps of solid", "Increasing concentration"), 2),
          ("A catalyst speeds up a reaction and is:",
           ("Used up completely", "Unchanged at the end", "Turned into product", "Always a gas"), 1)),
        L(12, "Energy Changes in Reactions", """
            <p>Breaking bonds requires energy; making bonds releases it. The overall balance decides
            whether a reaction is exothermic or endothermic.</p>
            <p>Combustion and neutralisation are exothermic; thermal decomposition and many dissolving
            reactions are endothermic.</p>
            <p>Activation energy is the minimum energy needed for a reaction to begin, and catalysts
            lower it.</p>
        """,
          ("Making chemical bonds:",
           ("Absorbs energy", "Releases energy", "Has no energy change", "Always cools the mixture"), 1),
          ("A catalyst works by lowering the:",
           ("Temperature", "Activation energy", "Concentration", "Mass of product"), 1)),
        L(13, "Introduction to Organic Chemistry", """
            <p>Organic chemistry studies compounds of carbon, which forms four bonds and long chains.</p>
            <p>Alkanes such as methane (CH&#8324;) have only single bonds and are saturated; alkenes such
            as ethene (C&#8322;H&#8324;) contain a double bond and are unsaturated.</p>
            <p>Crude oil is separated by fractional distillation into useful fractions such as petrol
            and diesel.</p>
        """,
          ("Alkenes are described as unsaturated because they contain:",
           ("Only single bonds", "A carbon-carbon double bond", "No carbon", "Extra hydrogen"), 1),
          ("Crude oil is separated into fractions by:",
           ("Filtration", "Fractional distillation", "Electrolysis", "Chromatography"), 1)),
        L(14, "Separating Mixtures", """
            <p>Mixtures are not chemically bonded, so physical methods can separate them.</p>
            <p>Filtration removes insoluble solids; evaporation and crystallisation recover dissolved
            solids; simple distillation separates a solvent from a solution.</p>
            <p>Chromatography separates substances by how strongly they are attracted to the paper
            versus the solvent.</p>
        """,
          ("To recover pure water from salty water you would use:",
           ("Filtration", "Distillation", "Chromatography", "Decanting"), 1),
          ("Chromatography is most useful for separating:",
           ("Sand from water", "Coloured dyes in an ink", "Iron from sulfur", "Oxygen from air"), 1)),
        L(15, "Chemistry and the Environment", """
            <p>The atmosphere is roughly 78% nitrogen and 21% oxygen, with small amounts of carbon
            dioxide and other gases.</p>
            <p>Burning fossil fuels releases carbon dioxide, which traps heat and contributes to global
            warming, plus sulfur dioxide, which causes acid rain.</p>
            <p>Reducing emissions, recycling and using renewable energy limit these effects.</p>
        """,
          ("The most abundant gas in the atmosphere is:",
           ("Oxygen", "Nitrogen", "Carbon dioxide", "Argon"), 1),
          ("Sulfur dioxide from burning fuels mainly causes:",
           ("Acid rain", "Ozone repair", "Global cooling", "Hard water"), 0)),
    ],
}

SUBJECTS["biology"] = {
    "name": "Biology",
    "lessons": [
        L(1, "Cells: The Basic Unit of Life", """
            <p>All living things are made of cells. Animal cells have a nucleus, cytoplasm, cell
            membrane and mitochondria.</p>
            <p>Plant cells have these too, plus a cellulose cell wall, a permanent vacuole and
            chloroplasts for photosynthesis.</p>
            <p>The nucleus stores DNA and controls the cell; mitochondria release energy through
            respiration.</p>
        """,
          ("Which structure is found in plant cells but not animal cells?",
           ("Nucleus", "Chloroplast", "Cell membrane", "Cytoplasm"), 1),
          ("Most energy release in a cell happens in the:",
           ("Nucleus", "Mitochondria", "Vacuole", "Cell wall"), 1)),
        L(2, "Cell Division", """
            <p><b>Mitosis</b> produces two genetically identical daughter cells and is used for growth,
            repair and asexual reproduction.</p>
            <p><b>Meiosis</b> produces four genetically different gametes with half the normal number of
            chromosomes.</p>
            <p>Fertilisation restores the full chromosome number and, with meiosis, creates variation.</p>
        """,
          ("Mitosis produces cells that are:",
           ("Genetically identical", "Genetically different", "Always gametes", "Half-sized"), 0),
          ("Meiosis is important because it produces:",
           ("Identical body cells", "Gametes with variation", "More mitochondria", "Larger cells"), 1)),
        L(3, "Movement In and Out of Cells", """
            <p><b>Diffusion</b> is the net movement of particles from high to low concentration, and
            needs no energy.</p>
            <p><b>Osmosis</b> is the diffusion of water across a partially permeable membrane, from
            dilute to concentrated solution.</p>
            <p><b>Active transport</b> moves substances against the concentration gradient and requires
            energy from respiration.</p>
        """,
          ("Osmosis is the movement of:",
           ("Any particle down a gradient", "Water across a partially permeable membrane",
            "Glucose using energy", "Gases only"), 1),
          ("Active transport differs from diffusion because it:",
           ("Requires energy", "Is faster", "Only moves water", "Needs no membrane"), 0)),
        L(4, "Enzymes", """
            <p>Enzymes are biological catalysts made of protein that speed up reactions without being
            used up.</p>
            <p>Each enzyme has an active site with a specific shape, fitting only its substrate &mdash;
            the lock-and-key idea.</p>
            <p>Extreme heat or the wrong pH changes the active site's shape, denaturing the enzyme so it
            no longer works.</p>
        """,
          ("Enzymes are specific because of the shape of their:",
           ("Nucleus", "Active site", "Membrane", "Substrate only"), 1),
          ("High temperatures stop enzymes working because they:",
           ("Dissolve", "Denature", "Multiply", "Become substrates"), 1)),
        L(5, "Nutrition and Digestion", """
            <p>A balanced diet supplies carbohydrates, proteins, fats, vitamins, minerals, fibre and water.</p>
            <p>Digestion breaks large insoluble molecules into small soluble ones: amylase digests starch
            to sugars, protease digests proteins to amino acids, lipase digests fats.</p>
            <p>Absorption happens in the small intestine, whose villi give a huge surface area.</p>
        """,
          ("Proteins are digested by:",
           ("Amylase", "Protease", "Lipase", "Bile"), 1),
          ("Villi in the small intestine increase the rate of absorption by increasing:",
           ("Surface area", "Temperature", "Acidity", "Blood pressure"), 0)),
        L(6, "Respiration", """
            <p>Aerobic respiration releases energy using oxygen:
            <code>glucose + oxygen &rarr; carbon dioxide + water</code>.</p>
            <p>Anaerobic respiration happens without oxygen. In muscles it produces lactic acid and far
            less energy; in yeast it produces ethanol and carbon dioxide.</p>
            <p>Respiration occurs continuously in all living cells, not only in animals.</p>
        """,
          ("Aerobic respiration produces:",
           ("Carbon dioxide and water", "Oxygen and glucose", "Lactic acid only", "Ethanol"), 0),
          ("Anaerobic respiration in human muscle produces:",
           ("Ethanol", "Lactic acid", "Oxygen", "Starch"), 1)),
        L(7, "Photosynthesis", """
            <p>Plants make their own food using light energy:
            <code>carbon dioxide + water &rarr; glucose + oxygen</code>.</p>
            <p>It takes place in chloroplasts, which contain the green pigment chlorophyll.</p>
            <p>The rate is limited by light intensity, carbon dioxide concentration and temperature &mdash;
            the limiting factors.</p>
        """,
          ("Photosynthesis takes place in the:",
           ("Mitochondria", "Chloroplasts", "Nucleus", "Vacuole"), 1),
          ("Which is NOT a limiting factor of photosynthesis?",
           ("Light intensity", "Carbon dioxide level", "Temperature", "Oxygen level"), 3)),
        L(8, "The Circulatory System", """
            <p>The heart is a double pump: the right side sends blood to the lungs, the left side to the
            rest of the body.</p>
            <p>Arteries carry blood away from the heart at high pressure; veins return it with valves to
            stop backflow; capillaries allow exchange with tissues.</p>
            <p>Red blood cells carry oxygen using haemoglobin, white blood cells fight infection, and
            platelets help clotting.</p>
        """,
          ("Arteries carry blood:",
           ("Towards the heart", "Away from the heart", "Only to the lungs", "Only when resting"), 1),
          ("Oxygen is transported by:",
           ("Platelets", "Plasma only", "Red blood cells", "White blood cells"), 2)),
        L(9, "Breathing and Gas Exchange", """
            <p>Air travels through the trachea and bronchi into millions of tiny alveoli.</p>
            <p>Alveoli are adapted for exchange: a huge surface area, very thin walls, a moist lining and
            a rich blood supply.</p>
            <p>Oxygen diffuses into the blood while carbon dioxide diffuses out, both moving down their
            concentration gradients.</p>
        """,
          ("Gas exchange in the lungs happens in the:",
           ("Trachea", "Bronchi", "Alveoli", "Diaphragm"), 2),
          ("Alveoli are efficient partly because their walls are:",
           ("Thick and tough", "Very thin", "Dry", "Impermeable"), 1)),
        L(10, "Coordination: Nerves and Hormones", """
            <p>The nervous system gives fast, short-lived responses using electrical impulses along
            neurones.</p>
            <p>A reflex arc (receptor &rarr; sensory neurone &rarr; relay &rarr; motor neurone &rarr; effector)
            bypasses conscious thought for speed.</p>
            <p>Hormones are chemical messengers carried in the blood; insulin, for example, lowers blood
            glucose.</p>
        """,
          ("Reflex actions are fast because they:",
           ("Use hormones", "Do not involve conscious thought",
            "Travel through blood", "Involve only one neurone"), 1),
          ("Insulin is a hormone that:",
           ("Raises blood glucose", "Lowers blood glucose", "Digests fat", "Carries oxygen"), 1)),
        L(11, "Genetics and Inheritance", """
            <p>Genes come in versions called alleles, which may be dominant or recessive.</p>
            <p>An organism's genotype is its alleles; the phenotype is the characteristic you observe.</p>
            <p>A Punnett square predicts offspring: two heterozygous parents (Bb &times; Bb) give a 3:1
            ratio of dominant to recessive phenotypes.</p>
        """,
          ("A recessive characteristic is only shown when the organism has:",
           ("One recessive allele", "Two recessive alleles", "One dominant allele", "No alleles"), 1),
          ("Crossing Bb with Bb gives a phenotype ratio of about:",
           ("1:1", "2:1", "3:1", "4:0"), 2)),
        L(12, "DNA and Protein Synthesis", """
            <p>DNA is a double helix of two strands, with bases pairing A-T and C-G.</p>
            <p>A gene is a section of DNA coding for a sequence of amino acids that folds into a protein.</p>
            <p>Mutations change the base sequence; most have little effect, but some alter the protein
            and therefore the organism.</p>
        """,
          ("In DNA, the base adenine always pairs with:",
           ("Cytosine", "Guanine", "Thymine", "Another adenine"), 2),
          ("A gene codes for:",
           ("A whole organism", "A protein", "A cell membrane", "A chromosome pair"), 1)),
        L(13, "Evolution and Natural Selection", """
            <p>Individuals within a species vary. Those with characteristics best suited to the
            environment are more likely to survive and reproduce.</p>
            <p>They pass on the useful alleles, so over many generations the population changes &mdash;
            evolution by natural selection, proposed by Charles Darwin.</p>
            <p>Antibiotic-resistant bacteria are a modern example of the same process.</p>
        """,
          ("Natural selection acts on:",
           ("Variation between individuals", "Identical individuals", "Only plants", "Learned behaviour"), 0),
          ("Antibiotic resistance spreads because resistant bacteria:",
           ("Choose to change", "Survive and reproduce", "Grow larger", "Stop dividing"), 1)),
        L(14, "Ecosystems and Food Chains", """
            <p>A food chain starts with a producer, usually a plant that captures light energy, followed
            by primary and secondary consumers.</p>
            <p>Only about 10% of energy passes to the next level, which is why chains are short.</p>
            <p>Decomposers recycle nutrients from dead material back into the soil, keeping the carbon
            and nitrogen cycles turning.</p>
        """,
          ("The first organism in a food chain is always a:",
           ("Predator", "Producer", "Decomposer", "Herbivore"), 1),
          ("Roughly how much energy is passed to the next trophic level?",
           ("10%", "50%", "90%", "100%"), 0)),
        L(15, "Health, Disease and Immunity", """
            <p>Communicable diseases are caused by pathogens: bacteria, viruses, fungi and protists.</p>
            <p>The body defends itself with barriers such as skin and stomach acid, and with white blood
            cells that engulf pathogens or produce antibodies.</p>
            <p>Vaccination introduces a harmless form of a pathogen so the immune system can respond
            quickly if the real one arrives. Antibiotics treat bacteria, not viruses.</p>
        """,
          ("Antibiotics are effective against:",
           ("Viruses", "Bacteria", "All pathogens", "Fungi only"), 1),
          ("Vaccination works by:",
           ("Killing all bacteria", "Training the immune system in advance",
            "Replacing white blood cells", "Blocking the skin"), 1)),
    ],
}

SUBJECTS["computer_science"] = {
    "name": "Computer Science",
    "lessons": [
        L(1, "How Computers Store Data", """
            <p>Computers store everything as <b>binary</b> &mdash; sequences of 0s and 1s called bits,
            because circuits reliably represent just two states.</p>
            <p>8 bits make 1 <b>byte</b>, which can hold a value from 0 to 255 or a single character.</p>
            <p>Photos, music and this lesson are all ultimately patterns of bits interpreted according
            to a file format.</p>
        """,
          ("How many bits make up one byte?", ("4", "8", "16", "32"), 1),
          ("A single byte can represent values from:", ("0 to 8", "0 to 100", "0 to 255", "0 to 1024"), 2)),
        L(2, "Number Systems", """
            <p>Denary (base 10) uses digits 0-9; binary (base 2) uses 0-1; hexadecimal (base 16) uses
            0-9 then A-F.</p>
            <p>In binary, place values double: 1011 is 8 + 0 + 2 + 1 = 11 in denary.</p>
            <p>Hex is popular with programmers because one hex digit represents exactly four bits, making
            long binary strings readable.</p>
        """,
          ("The binary number 1011 equals which denary value?", ("7", "9", "11", "13"), 2),
          ("One hexadecimal digit represents how many bits?", ("2", "4", "8", "16"), 1)),
        L(3, "Hardware and the CPU", """
            <p>The CPU fetches, decodes and executes instructions in a continuous cycle.</p>
            <p>Key parts are the control unit, the arithmetic logic unit (ALU) and registers; cache is
            small fast memory close to the CPU.</p>
            <p>RAM is volatile working memory, lost when power goes; secondary storage such as an SSD
            keeps data permanently.</p>
        """,
          ("The repeating cycle a CPU performs is:",
           ("Save-load-print", "Fetch-decode-execute", "Read-write-delete", "Input-output"), 1),
          ("RAM is described as volatile because it:",
           ("Is very fast", "Loses its contents without power", "Cannot be upgraded", "Stores programs forever"), 1)),
        L(4, "Software and Operating Systems", """
            <p>System software runs the machine; application software does jobs for the user.</p>
            <p>An operating system manages memory, processes, files, devices and user accounts, hiding
            hardware complexity behind a consistent interface.</p>
            <p>Utility programs handle housekeeping such as backup, compression and virus scanning.</p>
        """,
          ("Which is an example of application software?",
           ("Windows", "A word processor", "A device driver", "The BIOS"), 1),
          ("A key job of an operating system is:",
           ("Writing your documents", "Managing memory and processes",
            "Designing hardware", "Compiling all code"), 1)),
        L(5, "Introduction to Algorithms", """
            <p>An algorithm is a precise step-by-step set of instructions for solving a problem.</p>
            <p>To find the largest number in a list, assume the first is largest, then compare it with
            each remaining number, updating whenever a bigger one appears.</p>
            <p>Good algorithms are unambiguous, finite (they stop) and correct. They can be planned with
            pseudocode or flowcharts before coding.</p>
        """,
          ("An algorithm is best described as:",
           ("A programming language", "A step-by-step set of instructions",
            "A type of hardware", "A file format"), 1),
          ("Which is NOT a property of a good algorithm?",
           ("It terminates", "It is unambiguous", "It runs forever", "It gives a correct result"), 2)),
        L(6, "Searching Algorithms", """
            <p>A <b>linear search</b> checks each item in turn. It works on any list but is slow for
            large data.</p>
            <p>A <b>binary search</b> repeatedly halves a <i>sorted</i> list, discarding the half that
            cannot contain the target.</p>
            <p>Binary search finds an item among a million sorted records in about 20 comparisons.</p>
        """,
          ("Binary search requires the data to be:",
           ("Sorted", "Unsorted", "Numeric only", "Stored in a file"), 0),
          ("Linear search works by:",
           ("Halving the list", "Checking items one by one", "Sorting first", "Guessing randomly"), 1)),
        L(7, "Sorting Algorithms", """
            <p><b>Bubble sort</b> repeatedly compares neighbouring items and swaps them if out of order;
            simple but slow.</p>
            <p><b>Insertion sort</b> builds a sorted section by inserting each new item into place, and
            is efficient on nearly sorted data.</p>
            <p><b>Merge sort</b> splits the list in half, sorts each half and merges them; it is much
            faster on large lists.</p>
        """,
          ("Bubble sort works by:",
           ("Splitting the list in half", "Swapping adjacent items that are out of order",
            "Inserting into a new list", "Counting occurrences"), 1),
          ("Which sort uses a divide-and-conquer approach?",
           ("Bubble sort", "Insertion sort", "Merge sort", "Linear sort"), 2)),
        L(8, "Programming Basics", """
            <p>A variable is a named store whose value can change; a constant cannot.</p>
            <p>Common data types are integer, real/float, Boolean, character and string. Choosing the
            right type saves memory and prevents errors.</p>
            <p>Programs follow three basic constructs: sequence, selection and iteration.</p>
        """,
          ("A Boolean variable can hold:",
           ("Any whole number", "True or False", "A line of text", "A decimal"), 1),
          ("The three basic programming constructs are:",
           ("Input, output, storage", "Sequence, selection, iteration",
            "Compile, run, debug", "Variables, constants, arrays"), 1)),
        L(9, "Selection and Iteration", """
            <p>Selection chooses a path: <code>if score &gt;= 50: print("Pass")</code>, optionally with
            elif and else branches.</p>
            <p>A <b>for</b> loop repeats a set number of times; a <b>while</b> loop repeats until a
            condition becomes false.</p>
            <p>A while loop whose condition never becomes false creates an infinite loop.</p>
        """,
          ("Which loop should you use when the number of repetitions is known in advance?",
           ("while loop", "for loop", "if statement", "recursive call"), 1),
          ("An infinite loop happens when:",
           ("The condition never becomes false", "The code has no loop",
            "You use a for loop", "A variable is a string"), 0)),
        L(10, "Functions and Decomposition", """
            <p>Decomposition breaks a large problem into smaller sub-problems, each solved by a function.</p>
            <p>Functions take parameters and usually return a value, so the same code can be reused with
            different inputs.</p>
            <p>Local variables exist only inside a function; global variables are visible throughout the
            program and are best used sparingly.</p>
        """,
          ("The main benefit of using functions is:",
           ("Programs run without errors", "Code can be reused and is easier to maintain",
            "Less memory is always used", "No variables are needed"), 1),
          ("A local variable can be accessed:",
           ("Anywhere in the program", "Only inside its function", "Only by the OS", "Only once"), 1)),
        L(11, "Data Structures", """
            <p>An array or list stores many values under one name, accessed by index starting at 0.</p>
            <p>A record (or dictionary) groups related fields of different types, such as a student's
            name, age and grade.</p>
            <p>A stack is last-in-first-out; a queue is first-in-first-out, used for printer jobs and
            scheduling.</p>
        """,
          ("A stack operates on which principle?",
           ("First in, first out", "Last in, first out", "Random access", "Sorted order"), 1),
          ("In most languages, the first element of an array has index:",
           ("0", "1", "-1", "It varies randomly"), 0)),
        L(12, "Databases and SQL", """
            <p>A relational database stores data in tables of records and fields, linked by keys.</p>
            <p>A primary key uniquely identifies each record; a foreign key refers to a primary key in
            another table, avoiding duplicated data.</p>
            <p>SQL queries the data, e.g.
            <code>SELECT name FROM students WHERE grade &gt; 70;</code></p>
        """,
          ("A primary key is used to:",
           ("Encrypt the table", "Uniquely identify each record",
            "Sort the database", "Link to the internet"), 1),
          ("Which SQL keyword filters which rows are returned?",
           ("SELECT", "FROM", "WHERE", "ORDER"), 2)),
        L(13, "Networks and the Internet", """
            <p>A LAN covers a small area such as a school; a WAN, like the internet, spans large
            distances.</p>
            <p>Devices follow protocols: TCP/IP for transferring data, HTTP/HTTPS for web pages.</p>
            <p>Data is split into packets that travel independently and are reassembled at the
            destination; DNS translates domain names into IP addresses.</p>
        """,
          ("Data sent across the internet is broken into:",
           ("Files", "Packets", "Pixels", "Bytes only"), 1),
          ("DNS is responsible for:",
           ("Encrypting data", "Converting domain names into IP addresses",
            "Storing web pages", "Blocking viruses"), 1)),
        L(14, "Cybersecurity", """
            <p>Threats include malware, phishing emails, brute-force attacks and social engineering that
            targets people rather than systems.</p>
            <p>Defences include strong unique passwords, two-factor authentication, firewalls, software
            updates and regular backups.</p>
            <p>Encryption scrambles data so that intercepting it is useless without the key.</p>
        """,
          ("Phishing is an attack that mainly targets:",
           ("Network cables", "People, by tricking them into revealing information",
            "Hard drives", "Printers"), 1),
          ("Encryption protects data by:",
           ("Deleting it", "Making it unreadable without the key",
            "Compressing it", "Backing it up"), 1)),
        L(15, "Efficiency and Big-O", """
            <p>Two correct algorithms can differ hugely in speed, so we compare how work grows with
            input size n.</p>
            <p>Big-O notation captures this: O(1) is constant, O(log n) very efficient (binary search),
            O(n) linear, and O(n&sup2;) slow for large n (bubble sort).</p>
            <p>There is often a trade-off between time taken and memory used.</p>
        """,
          ("Binary search has a time complexity of:",
           ("O(1)", "O(log n)", "O(n)", "O(n&sup2;)"), 1),
          ("An O(n&sup2;) algorithm becomes a problem when:",
           ("The input is tiny", "The input grows large", "Memory is cheap", "The data is sorted"), 1)),
    ],
}

SUBJECTS["english"] = {
    "name": "English",
    "lessons": [
        L(1, "Parts of Speech", """
            <p>Every word in a sentence does a job. Nouns name things, verbs express actions or states,
            and adjectives describe nouns.</p>
            <p>Adverbs modify verbs, adjectives or other adverbs, often telling us how, when or where.</p>
            <p>Pronouns replace nouns, prepositions show relationships (in, under, before) and
            conjunctions join ideas.</p>
        """,
          ("In &quot;She ran quickly&quot;, the word &quot;quickly&quot; is:",
           ("An adjective", "An adverb", "A noun", "A preposition"), 1),
          ("A word that joins two clauses together is a:",
           ("Pronoun", "Conjunction", "Preposition", "Determiner"), 1)),
        L(2, "Sentence Structure", """
            <p>A clause needs a subject and a verb. A main clause makes sense alone; a subordinate
            clause does not.</p>
            <p>Simple sentences have one clause, compound sentences join two main clauses with and, but
            or so, and complex sentences add a subordinate clause.</p>
            <p>Varying sentence length controls pace: short sentences create tension, longer ones build
            description.</p>
        """,
          ("&quot;Although it was raining, we walked home&quot; is a:",
           ("Simple sentence", "Compound sentence", "Complex sentence", "Fragment"), 2),
          ("A subordinate clause is one that:",
           ("Can stand alone", "Cannot stand alone as a sentence",
            "Contains no verb", "Must start a sentence"), 1)),
        L(3, "Punctuation", """
            <p>Full stops end sentences; commas separate items in a list, mark clauses and follow
            introductory phrases.</p>
            <p>Apostrophes show omission (don't) or possession (the dog's bowl; the dogs' bowls for
            plurals).</p>
            <p>Semicolons link two closely related main clauses, while colons introduce a list,
            explanation or quotation.</p>
        """,
          ("Which sentence uses the apostrophe correctly?",
           ("The dog's are barking", "The dogs' bowls were empty",
            "Its' a fine day", "The cat lost it's collar"), 1),
          ("A semicolon is best used to:",
           ("Introduce a list", "Join two closely related main clauses",
            "Show possession", "End a question"), 1)),
        L(4, "Verb Tenses", """
            <p>Tense places an action in time: past, present or future.</p>
            <p>Simple tenses state a fact (she walks), continuous tenses show ongoing action (she is
            walking), and perfect tenses link to another time (she has walked).</p>
            <p>Consistency matters: shifting tense mid-paragraph without reason confuses the reader.</p>
        """,
          ("&quot;She has finished her homework&quot; is in the:",
           ("Past simple", "Present perfect", "Future continuous", "Past continuous"), 1),
          ("Unnecessary changes of tense within a paragraph usually:",
           ("Add style", "Confuse the reader", "Are required", "Improve accuracy"), 1)),
        L(5, "Active and Passive Voice", """
            <p>In the active voice the subject performs the action: "The chef cooked the meal."</p>
            <p>In the passive voice the subject receives it: "The meal was cooked by the chef." The doer
            can even be left out.</p>
            <p>Active writing is usually clearer and more direct; passive suits formal, scientific or
            deliberately impersonal writing.</p>
        """,
          ("Which sentence is in the passive voice?",
           ("The dog chased the ball", "The ball was chased by the dog",
            "The dog is fast", "Chase the ball!"), 1),
          ("The passive voice is often chosen when the writer wants to:",
           ("Be as direct as possible", "Emphasise the action rather than the doer",
            "Shorten every sentence", "Avoid all verbs"), 1)),
        L(6, "Vocabulary and Word Building", """
            <p>Prefixes change meaning at the start of a word (unhappy, rewrite); suffixes usually change
            word class (happiness, quickly).</p>
            <p>Synonyms have similar meanings but different shades: "said", "muttered" and "declared"
            are not interchangeable.</p>
            <p>Register matters &mdash; choose formal vocabulary for essays and letters, informal for
            dialogue and personal writing.</p>
        """,
          ("Adding the prefix &quot;un-&quot; to a word usually:",
           ("Reverses its meaning", "Makes it plural", "Changes the tense", "Makes it a verb"), 0),
          ("Choosing &quot;muttered&quot; instead of &quot;said&quot; mainly affects:",
           ("Grammar", "Tone and precision of meaning", "Tense", "Sentence length"), 1)),
        L(7, "Paragraphs and Cohesion", """
            <p>A paragraph develops one main idea, usually opening with a topic sentence.</p>
            <p>Start a new paragraph when time, place, topic or speaker changes.</p>
            <p>Connectives such as however, therefore, in addition and consequently signal how ideas
            relate and keep writing cohesive.</p>
        """,
          ("The sentence that introduces a paragraph's main idea is the:",
           ("Conclusion", "Topic sentence", "Quotation", "Connective"), 1),
          ("Which connective signals contrast?",
           ("Furthermore", "However", "Similarly", "Therefore"), 1)),
        L(8, "Descriptive Writing", """
            <p>Strong description appeals to several senses, not only sight, and favours precise nouns
            and verbs over piles of adjectives.</p>
            <p>"Show, don't tell": instead of "he was nervous", write "his hands would not stay still".</p>
            <p>Zooming from a wide view to a small detail gives description shape and stops it drifting.</p>
        """,
          ("&quot;Show, don't tell&quot; advises a writer to:",
           ("Explain feelings directly", "Reveal feelings through detail and action",
            "Use more adjectives", "Write shorter sentences"), 1),
          ("Effective description usually appeals to:",
           ("Sight only", "Several senses", "Sound only", "No senses"), 1)),
        L(9, "Persuasive Writing", """
            <p>Persuasion works by combining credibility, emotion and logic.</p>
            <p>Useful techniques include rhetorical questions, the rule of three, direct address, facts
            and statistics, and anecdote.</p>
            <p>Structure matters: a clear line of argument, counter-argument acknowledged and answered,
            and a memorable closing call to action.</p>
        """,
          ("&quot;Are we really going to ignore this?&quot; is an example of:",
           ("A statistic", "A rhetorical question", "An anecdote", "Alliteration"), 1),
          ("Addressing the opposing view in a persuasive piece usually:",
           ("Weakens the argument", "Strengthens it by showing balance",
            "Is never allowed", "Replaces evidence"), 1)),
        L(10, "Formal Letters and Emails", """
            <p>Formal writing needs a clear purpose stated early, standard English and a polite,
            impersonal tone.</p>
            <p>Conventions include a greeting, organised paragraphs and a suitable sign-off: "Yours
            sincerely" when you know the name, "Yours faithfully" when you do not.</p>
            <p>Avoid contractions, slang and emojis; keep sentences clear rather than long.</p>
        """,
          ("If a formal letter begins &quot;Dear Sir or Madam&quot;, it should end:",
           ("Yours sincerely", "Yours faithfully", "Best wishes", "Cheers"), 1),
          ("Which is inappropriate in a formal email?",
           ("Clear paragraphs", "Slang and contractions", "A polite greeting", "Standard spelling"), 1)),
        L(11, "Reading Comprehension and Inference", """
            <p>Explicit information is stated directly; implicit meaning must be inferred from clues.</p>
            <p>Inference means drawing a supported conclusion &mdash; a character who "avoided her eyes"
            may be hiding something.</p>
            <p>In analysis, use the point-evidence-explanation pattern: make a claim, quote briefly, then
            explain how the language supports it.</p>
        """,
          ("Inference means:",
           ("Repeating what the text says", "Drawing a conclusion from clues in the text",
            "Guessing with no evidence", "Summarising the plot"), 1),
          ("In PEE, the E that follows the evidence stands for:",
           ("Example", "Explanation", "Emphasis", "Ending"), 1)),
        L(12, "Figurative Language", """
            <p>A simile compares using like or as; a metaphor says one thing <i>is</i> another.</p>
            <p>Personification gives human qualities to non-human things; hyperbole exaggerates for
            effect.</p>
            <p>Sound devices such as alliteration, assonance and onomatopoeia shape how a line feels
            when read aloud.</p>
        """,
          ("&quot;The wind whispered through the trees&quot; is an example of:",
           ("Simile", "Personification", "Hyperbole", "Onomatopoeia"), 1),
          ("The difference between a simile and a metaphor is that a simile:",
           ("Uses like or as", "Is always shorter", "Describes sound", "Cannot be used in poetry"), 0)),
        L(13, "Analysing Poetry", """
            <p>Read for meaning first, then consider form: stanzas, line length, rhyme scheme and rhythm.</p>
            <p>Enjambment runs a sentence over a line break to create flow or surprise; caesura is a
            pause within a line.</p>
            <p>Strong analysis links technique to effect &mdash; not just "the poet uses a metaphor" but
            what that metaphor makes the reader feel or understand.</p>
        """,
          ("Enjambment is when:",
           ("A line ends with a full stop", "A sentence continues over a line break",
            "Two words rhyme", "A stanza repeats"), 1),
          ("Good poetry analysis always connects a technique to its:",
           ("Length", "Effect on the reader", "Publication date", "Rhyme only"), 1)),
        L(14, "Narrative and Prose Technique", """
            <p>Point of view shapes everything: first person is intimate but limited, third person
            omniscient sees all.</p>
            <p>Structure can be reordered with flashbacks, foreshadowing and cliffhangers to control
            tension.</p>
            <p>Characters are built through action, dialogue and reaction rather than lists of traits;
            setting can mirror mood.</p>
        """,
          ("A story told using &quot;I&quot; is written in:",
           ("Third person", "First person", "Second person", "Omniscient narration"), 1),
          ("Hinting at events to come later in a story is called:",
           ("Flashback", "Foreshadowing", "Exposition", "Resolution"), 1)),
        L(15, "Drama and Shakespeare", """
            <p>Drama is written to be performed, so meaning comes from dialogue, stage directions and
            performance choices.</p>
            <p>A soliloquy lets a character voice private thoughts alone on stage; an aside is a remark
            only the audience hears.</p>
            <p>Shakespeare often wrote in iambic pentameter &mdash; ten syllables with five stressed
            beats &mdash; and used prose for lower-status or comic characters.</p>
        """,
          ("A soliloquy is a speech delivered:",
           ("To another character", "Alone, revealing private thoughts",
            "By the narrator", "By the whole cast"), 1),
          ("Iambic pentameter contains how many syllables per line?",
           ("Five", "Eight", "Ten", "Twelve"), 2)),
    ],
}
