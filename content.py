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

SUBJECTS["electronics"] = {
    "name": "Electronics",
    "lessons": [
        L(1, "Introduction to Circuits", """
            <p>An electronic circuit is a closed loop that lets electric charge flow from a power
            source, through components, and back again.</p>
            <p>Every circuit needs a source of energy (such as a battery), a path for current
            (conductors), and a load that does something useful, such as a bulb or motor.</p>
            <p>Circuit diagrams use standard symbols so that any engineer, anywhere, can read the same
            circuit the same way.</p>
        """,
          ("A complete electronic circuit must always have:",
           ("A closed loop for current to flow", "At least ten components",
            "Only alternating current", "A microcontroller"), 0),
          ("Circuit diagrams use standard symbols mainly so that:",
           ("Circuits look more colourful", "Anyone can read and build the same circuit",
            "Components are cheaper", "Current flows faster"), 1)),
        L(2, "Voltage, Current and Resistance", """
            <p>Voltage is the electrical "push" that drives charge around a circuit, measured in volts.</p>
            <p>Current is the rate of flow of charge, measured in amperes; resistance opposes that flow,
            measured in ohms.</p>
            <p>Ohm's law ties the three together: <code>V = I &times; R</code>. Doubling the resistance
            while keeping voltage fixed halves the current.</p>
        """,
          ("Which quantity is measured in amperes?", ("Voltage", "Current", "Resistance", "Power"), 1),
          ("A 9 V supply drives current through a 3 &Omega; resistor. The current is:",
           ("1 A", "3 A", "6 A", "27 A"), 1)),
        L(3, "Series and Parallel Circuits", """
            <p>In a <b>series</b> circuit components are connected end to end in a single loop, so the
            same current flows through each one.</p>
            <p>In a <b>parallel</b> circuit components are connected across separate branches, so each
            branch sees the full supply voltage.</p>
            <p>If one bulb fails in a series circuit the whole loop breaks; in a parallel circuit the
            other branches keep working.</p>
        """,
          ("If one bulb breaks in a series circuit, the other bulbs:",
           ("Get brighter", "Stop working too", "Are unaffected", "Explode"), 1),
          ("In a parallel circuit, each branch receives:",
           ("A fraction of the supply voltage", "The full supply voltage",
            "No voltage", "Double the supply voltage"), 1)),
        L(4, "Resistors and Resistor Networks", """
            <p>A resistor limits current flow and is often used to protect other components or set a
            precise voltage or current.</p>
            <p>Resistors in series add directly: <code>R_total = R1 + R2</code>. Resistors in parallel
            combine so the total is always less than the smallest individual resistor.</p>
            <p>Colour bands printed on a resistor's body encode its resistance value and tolerance.</p>
        """,
          ("Two 10 &Omega; resistors connected in series give a total resistance of:",
           ("5 &Omega;", "10 &Omega;", "20 &Omega;", "100 &Omega;"), 2),
          ("Combining resistors in parallel always gives a total resistance that is:",
           ("Greater than any single resistor", "Equal to the largest resistor",
            "Less than the smallest resistor", "Always zero"), 2)),
        L(5, "Capacitors", """
            <p>A capacitor stores electrical charge on two conductive plates separated by an insulator,
            measured in farads.</p>
            <p>It charges up when connected to a supply and discharges when the supply is removed,
            smoothing out voltage changes.</p>
            <p>Capacitors are used for smoothing power supplies, timing circuits and filtering unwanted
            signal noise.</p>
        """,
          ("A capacitor mainly works by:",
           ("Converting current to light", "Storing charge on two plates",
            "Amplifying a signal", "Switching current on and off"), 1),
          ("A common use for a capacitor in a power supply is:",
           ("Smoothing voltage fluctuations", "Increasing resistance",
            "Generating a magnetic field", "Storing programs"), 0)),
        L(6, "Diodes and Rectification", """
            <p>A diode allows current to flow in only one direction, acting like a one-way valve for
            electricity.</p>
            <p>A light-emitting diode (LED) also gives off light when current passes through it in the
            correct direction, and needs a resistor in series to limit current.</p>
            <p>Rectification uses diodes to convert alternating current (AC), which reverses direction,
            into direct current (DC), which flows one way.</p>
        """,
          ("A diode allows current to flow:",
           ("In both directions equally", "In one direction only",
            "Only when cold", "Only in AC circuits"), 1),
          ("Rectification is the process of converting:",
           ("DC to AC", "AC to DC", "Voltage to resistance", "Light to current"), 1)),
        L(7, "Transistors as Switches", """
            <p>A transistor is a semiconductor device that can act as an electronic switch or an
            amplifier.</p>
            <p>A small current or voltage at the base (or gate) controls a much larger current flowing
            between the other two terminals.</p>
            <p>This lets a low-power signal, such as from a sensor, switch a high-power output like a
            motor or lamp.</p>
        """,
          ("A transistor used as a switch is controlled by:",
           ("A small current or voltage at its base/gate", "Removing all resistors",
            "Connecting it to AC only", "Heating it up"), 0),
          ("A key use of transistors in circuits is to:",
           ("Store large amounts of charge", "Switch or amplify a signal",
            "Convert AC to DC directly", "Measure resistance"), 1)),
        L(8, "Logic Gates", """
            <p>Logic gates perform simple decisions on digital signals that are either HIGH (1) or LOW
            (0).</p>
            <p>An <b>AND</b> gate outputs 1 only when all its inputs are 1; an <b>OR</b> gate outputs 1
            when at least one input is 1; a <b>NOT</b> gate simply inverts its input.</p>
            <p>Combining a handful of basic gates can build circuits that add numbers or make complex
            decisions.</p>
        """,
          ("An AND gate outputs 1 when:",
           ("At least one input is 1", "All inputs are 1", "All inputs are 0", "It is never 1"), 1),
          ("A NOT gate takes one input and:",
           ("Doubles it", "Leaves it unchanged", "Inverts it", "Ignores it"), 2)),
        L(9, "Boolean Algebra and Truth Tables", """
            <p>Boolean algebra describes logic using only two values, true and false (1 and 0), and
            operators such as AND, OR and NOT.</p>
            <p>A truth table lists every possible combination of inputs alongside the resulting output,
            making a gate's behaviour easy to check.</p>
            <p>Combining gates, such as AND followed by NOT (a NAND gate), can build any other logic
            function.</p>
        """,
          ("A truth table shows:",
           ("The voltage of a circuit", "Every input combination and its output",
            "The resistance of a gate", "The cost of components"), 1),
          ("Combining an AND gate with a NOT gate on its output creates a:",
           ("NOR gate", "NAND gate", "XOR gate", "Buffer"), 1)),
        L(10, "Digital vs Analogue Signals", """
            <p>An <b>analogue</b> signal varies smoothly and continuously, like the volume from a
            microphone.</p>
            <p>A <b>digital</b> signal has only discrete levels, usually just HIGH and LOW, making it
            more resistant to noise and easier to process.</p>
            <p>An analogue-to-digital converter (ADC) samples an analogue signal at intervals and
            represents each sample as a binary number.</p>
        """,
          ("A digital signal differs from an analogue signal because it:",
           ("Varies smoothly", "Has only discrete levels", "Cannot be measured", "Is always louder"), 1),
          ("An ADC is used to:",
           ("Convert digital signals to analogue", "Convert analogue signals to digital",
            "Amplify a signal", "Store charge"), 1)),
        L(11, "Sensors and Input Devices", """
            <p>Sensors convert a physical quantity, such as light, temperature or pressure, into an
            electrical signal a circuit can process.</p>
            <p>A light-dependent resistor (LDR) lowers its resistance as light increases; a thermistor's
            resistance changes with temperature.</p>
            <p>These are often used with a voltage divider so their changing resistance produces a
            changing voltage a circuit can read.</p>
        """,
          ("A light-dependent resistor (LDR) changes its:",
           ("Voltage output directly", "Resistance with light level",
            "Colour with temperature", "Current with sound"), 1),
          ("Sensors are useful in circuits because they:",
           ("Store energy for later", "Convert physical quantities into electrical signals",
            "Always produce digital output", "Increase supply voltage"), 1)),
        L(12, "Output Devices and Actuators", """
            <p>Output devices convert an electrical signal into a useful physical effect: LEDs produce
            light, buzzers produce sound, and motors produce movement.</p>
            <p>A relay uses a small control current to switch a separate, often much higher-power,
            circuit on or off, keeping the two electrically isolated.</p>
            <p>Motors and other high-current outputs are usually driven through a transistor or relay
            rather than directly from a microcontroller pin.</p>
        """,
          ("A relay is useful because it allows a small current to:",
           ("Directly power a motor with no other components", "Switch a separate, higher-power circuit",
            "Store charge for later use", "Convert AC into light"), 1),
          ("Which of these is an output device?", ("Thermistor", "LDR", "Buzzer", "Push switch"), 2)),
        L(13, "Power Supplies and Batteries", """
            <p>Batteries store chemical energy and release it as direct current (DC) at a roughly
            constant voltage until they run low.</p>
            <p>Connecting cells in series increases total voltage; connecting them in parallel increases
            available current (capacity) while keeping voltage the same.</p>
            <p>Mains electricity is alternating current (AC) and must usually be transformed and
            rectified before it can power DC circuits and electronics.</p>
        """,
          ("Connecting two identical cells in series mainly increases the circuit's:",
           ("Resistance", "Total voltage", "Total current capacity", "Frequency"), 1),
          ("Mains electricity supplied to homes is normally:",
           ("Direct current (DC)", "Alternating current (AC)", "Static electricity", "Always 9 V"), 1)),
        L(14, "Printed Circuit Boards and Prototyping", """
            <p>A breadboard lets components be connected temporarily without soldering, ideal for
            testing and prototyping a design.</p>
            <p>A printed circuit board (PCB) has copper tracks etched onto an insulating board, giving a
            permanent, compact and reliable connection between components.</p>
            <p>Moving from breadboard to PCB usually happens once a design has been tested and is ready
            for a final, durable version.</p>
        """,
          ("A breadboard is mainly used for:",
           ("Permanent soldered circuits", "Temporary prototyping and testing",
            "Generating mains electricity", "Storing programs"), 1),
          ("Copper tracks on a PCB serve the same purpose as:",
           ("Wires connecting components", "Batteries", "Resistors", "Sensors"), 0)),
        L(15, "Microcontrollers and Embedded Systems", """
            <p>A microcontroller is a small computer on a single chip, containing a processor, memory
            and input/output pins, used to control a specific device.</p>
            <p>An embedded system is any computer system built into a larger product, such as a washing
            machine or a car, rather than a general-purpose computer.</p>
            <p>Microcontrollers are typically programmed once and then repeatedly read sensors, make
            decisions, and drive outputs in a continuous loop.</p>
        """,
          ("A microcontroller is best described as:",
           ("A type of resistor", "A small computer on a single chip",
            "A kind of battery", "A logic gate only"), 1),
          ("An embedded system is a computer system that is:",
           ("Only found in desktop PCs", "Built into a larger product to control it",
            "Never connected to sensors", "Always analogue"), 1)),
    ],
}
