def L(lesson_id, title, content, *questions):
    return {
        "id": lesson_id,
        "title": title,
        "content": content.strip(),
        "quiz": [{"question": q, "options": list(o), "answer": a} for q, o, a in questions],
    }


def score(lesson, responses):
    quiz = lesson["quiz"]
    correct = sum(1 for q, r in zip(quiz, responses) if r == q["answer"])
    return correct, len(quiz)


SUBJECTS = {}

SUBJECTS["maths"] = {
    "name": "Mathematics",
    "lessons": [
        L(1, "Introduction to Algebra", """
            <p><b>Basic:</b> Algebra uses letters such as <b>x</b> and <b>y</b> to stand in for unknown numbers,
            so that one rule can describe many situations at once. Think of x as a box you have not opened yet &mdash;
            the equation tells you what must be inside.</p>
            <p>An equation like <code>x + 5 = 12</code> asks: what number, added to 5, gives 12?
            Subtracting 5 from both sides leaves <code>x = 7</code>. The golden rule: whatever you do to one side
            of an equation you must do to the other, so the two sides stay balanced &mdash; like a see-saw that
            must stay level.</p>
            <p><b>Intermediate:</b> Algebra lets you model real situations. If a taxi charges a &pound;3 call-out fee
            plus &pound;2 per mile, the total cost is <code>C = 3 + 2m</code>. If you only have &pound;15, you can solve
            <code>3 + 2m = 15</code> to find the furthest you can travel: <code>m = 6</code> miles, before you even
            get in the car.</p>
            <p>Negative numbers and brackets follow the same balancing rule. Solving <code>-2x + 7 = 1</code> gives
            <code>-2x = -6</code>, so <code>x = 3</code> &mdash; dividing by a negative does not flip the answer's
            sign rule, but does flip an inequality's direction, which trips up many learners.</p>
            <p><b>Pre-advanced:</b> Not every equation has exactly one solution. <code>x + 3 = x + 3</code> is true
            for every value of x (infinitely many solutions), while <code>x + 3 = x + 5</code> is never true
            (no solution). Recognising these cases &mdash; rather than panicking when the letters cancel out &mdash;
            is a hallmark of algebraic fluency used throughout science and engineering, from balancing chemical
            equations to pricing spreadsheets.</p>
        """,
          ("Solve: x + 5 = 12. What is x?", ("5", "6", "7", "17"), 2),
          ("Why must the same operation be applied to both sides of an equation?",
           ("To make the numbers smaller", "To keep both sides equal",
            "To remove the letter x", "It is optional"), 1),
          ("A taxi costs 3 + 2m pounds for m miles. With 15 pounds, the furthest you can travel is:",
           ("4 miles", "5 miles", "6 miles", "7.5 miles"), 2),
          ("Solving -2x + 7 = 1 gives x equal to:",
           ("-3", "3", "4", "-4"), 1),
          ("Which equation has infinitely many solutions for x?",
           ("x + 3 = x + 5", "2x = 10", "x + 3 = x + 3", "x - 1 = 0"), 2)),
        L(2, "Linear Equations", """
            <p><b>Basic:</b> A linear equation has variables raised only to the power 1, e.g. <code>3x - 4 = 11</code>.
            Solve it by undoing operations in reverse order: add 4, then divide by 3, giving <code>x = 5</code>.</p>
            <p>When the unknown appears on both sides, gather the x terms on one side first:
            <code>5x - 2 = 3x + 8</code> becomes <code>2x = 10</code>, so <code>x = 5</code>. Always check by
            substituting your answer back into the original equation &mdash; a 10-second habit that catches most
            arithmetic slips.</p>
            <p><b>Intermediate:</b> Linear equations model anything that changes at a constant rate. A phone plan
            costing &pound;20 a month plus 5p per text means the monthly bill is <code>B = 20 + 0.05t</code>. Two
            competing plans can be compared by setting their expressions equal to find the "break-even" number of
            texts where both cost the same.</p>
            <p>Equations with fractions, like <code>(x + 1)/3 = 4</code>, are solved by clearing the denominator
            first: multiply both sides by 3 to get <code>x + 1 = 12</code>, so <code>x = 11</code>.</p>
            <p><b>Pre-advanced:</b> Simultaneous linear equations describe two conditions that must hold at once,
            such as two ingredients whose total weight and total cost are both fixed. Elimination (adding or
            subtracting equations to cancel a variable) and substitution (rearranging one equation and plugging it
            into the other) are the two standard tools, and both scale up to systems with many variables used in
            real spreadsheets, GPS positioning and economic modelling.</p>
        """,
          ("Solve: 3x - 4 = 11.", ("x = 3", "x = 5", "x = 7", "x = 15"), 1),
          ("Solving 5x - 2 = 3x + 8, the sensible first step is to:",
           ("Divide everything by 5", "Subtract 3x from both sides",
            "Add 2 to only the left side", "Square both sides"), 1),
          ("Solve (x + 1)/3 = 4.", ("x = 3", "x = 9", "x = 11", "x = 13"), 2),
          ("Plan A costs 20 + 0.05t and Plan B costs 10 + 0.10t. The plans cost the same when t equals:",
           ("100", "150", "200", "250"), 2),
          ("Solving the pair 2x + y = 7 and x - y = 2 by elimination, x equals:",
           ("1", "2", "3", "4"), 2)),
        L(3, "Expanding and Factorising", """
            <p><b>Basic:</b> Expanding removes brackets: <code>3(x + 4) = 3x + 12</code>. Every term inside the
            bracket is multiplied by the term outside, like handing three friends the same bag of snacks and
            multiplying the count.</p>
            <p>For two brackets, multiply each term in the first by each term in the second (sometimes called
            FOIL &mdash; First, Outer, Inner, Last): <code>(x + 2)(x + 3) = x&sup2; + 5x + 6</code>.</p>
            <p><b>Intermediate:</b> Factorising is the reverse: rewrite an expression as a product. For
            <code>x&sup2; + 5x + 6</code> look for two numbers that multiply to 6 and add to 5 &mdash; 2 and 3, giving
            <code>(x + 2)(x + 3)</code>. Spotting a common factor first, e.g. <code>6x&sup2; + 9x = 3x(2x + 3)</code>,
            keeps later numbers smaller and easier to work with.</p>
            <p>The "difference of two squares" pattern, <code>a&sup2; - b&sup2; = (a + b)(a - b)</code>, is worth
            memorising: it turns <code>x&sup2; - 25</code> instantly into <code>(x + 5)(x - 5)</code> without any
            trial and error.</p>
            <p><b>Pre-advanced:</b> When the coefficient of x&sup2; is not 1, e.g. <code>2x&sup2; + 7x + 3</code>,
            factorising needs a product-sum approach: find two numbers multiplying to <code>2 &times; 3 = 6</code>
            and summing to 7 (that's 1 and 6), split the middle term, then factor by grouping to get
            <code>(2x + 1)(x + 3)</code>. This same grouping technique underlies solving cubic and higher-degree
            polynomials in later study.</p>
        """,
          ("Expand (x + 2)(x + 3).", ("x&sup2; + 6", "x&sup2; + 5x + 6", "x&sup2; + 5x", "2x + 3"), 1),
          ("To factorise x&sup2; + 7x + 10 you need two numbers that:",
           ("Add to 10 and multiply to 7", "Multiply to 10 and add to 7",
            "Are both equal to 5", "Subtract to give 10"), 1),
          ("Factorise x&sup2; - 25 using difference of two squares.",
           ("(x - 5)&sup2;", "(x + 5)(x - 5)", "(x + 25)(x - 1)", "Cannot be factorised"), 1),
          ("Factorise 2x&sup2; + 7x + 3.",
           ("(2x + 1)(x + 3)", "(2x + 3)(x + 1)", "(x + 1)(x + 3)", "(2x + 7)(x + 1)"), 0)),
        L(4, "Quadratic Equations", """
            <p><b>Basic:</b> A quadratic has the form <code>ax&sup2; + bx + c = 0</code> and can have two, one, or no
            real solutions &mdash; think of it as the equation for the path of a thrown ball, which can hit the
            ground at two points, graze it at one, or (if thrown from underground) never reach it.</p>
            <p>If it factorises, use the fact that a product is zero only when a factor is zero:
            <code>(x - 2)(x - 3) = 0</code> gives <code>x = 2</code> or <code>x = 3</code>.</p>
            <p><b>Intermediate:</b> Otherwise use the quadratic formula
            <code>x = (-b &plusmn; &radic;(b&sup2; - 4ac)) / 2a</code>. The part <code>b&sup2; - 4ac</code> is the
            discriminant: positive means two distinct real roots, zero means one repeated root, negative means no
            real roots. A ball thrown so its path never crosses the ground corresponds to a negative discriminant.</p>
            <p>Completing the square, <code>x&sup2; + 6x + 5 = (x + 3)&sup2; - 4</code>, reveals the vertex of the
            parabola directly: here the minimum value is -4, occurring at <code>x = -3</code>, useful for finding
            maximum profit or minimum material cost problems without calculus.</p>
            <p><b>Pre-advanced:</b> When the discriminant is negative, the roots exist but are complex numbers
            involving <code>&radic;-1 = i</code>. Engineers use these "imaginary" roots constantly when analysing
            oscillating systems such as bridges and alternating current circuits, even though the physical
            displacement is always a real number.</p>
        """,
          ("The solutions of (x - 2)(x - 3) = 0 are:",
           ("x = -2 and x = -3", "x = 2 and x = 3", "x = 6 only", "x = 5"), 1),
          ("If b&sup2; - 4ac is negative, the quadratic has:",
           ("Two real roots", "One repeated root", "No real roots", "Infinitely many roots"), 2),
          ("Completing the square, x&sup2; + 6x + 5 can be written as:",
           ("(x + 3)&sup2; - 4", "(x + 3)&sup2; + 4", "(x + 6)&sup2; - 5", "(x + 5)&sup2; - 3"), 0),
          ("Using the quadratic formula, the solutions of x&sup2; - 5x + 6 = 0 are:",
           ("x = 1, x = 6", "x = 2, x = 3", "x = -2, x = -3", "x = 6, x = -1"), 1),
          ("A quadratic with discriminant exactly zero has:",
           ("No real roots", "Two distinct real roots", "One repeated real root", "Three roots"), 2)),
        L(5, "Angles and Shapes", """
            <p><b>Basic:</b> Angles on a straight line add to 180&deg;, and angles around a point add to 360&deg;.
            A triangle's three interior angles always total 180&deg;; a quadrilateral's total 360&deg;.</p>
            <p>A square has four equal sides and four 90&deg; angles. Perimeter is the total distance around a
            shape (useful for fencing a garden); area is the space it covers (useful for buying turf or carpet).</p>
            <p><b>Intermediate:</b> Regular polygons follow a formula: the sum of interior angles is
            <code>(n - 2) &times; 180&deg;</code> for n sides, so a regular hexagon's angles sum to 720&deg; and each
            angle is 120&deg; &mdash; exactly why honeycomb cells tile perfectly with no gaps.</p>
            <p>Exterior angles of any convex polygon always sum to 360&deg;, regardless of how many sides it has,
            which is a quick sanity check when a geometry problem gives you a messy shape.</p>
            <p><b>Pre-advanced:</b> Circle theorems extend this thinking: the angle at the centre of a circle is
            twice the angle at the circumference subtended by the same arc, and angles in the same segment are
            equal. Architects use these relationships when designing arches and domes so that structural loads are
            distributed symmetrically.</p>
        """,
          ("The interior angles of a triangle add up to:",
           ("90 degrees", "180 degrees", "270 degrees", "360 degrees"), 1),
          ("A triangle has angles of 40&deg; and 75&deg;. The third angle is:",
           ("55 degrees", "65 degrees", "75 degrees", "115 degrees"), 1),
          ("The sum of interior angles of a regular hexagon is:",
           ("360 degrees", "540 degrees", "720 degrees", "900 degrees"), 2),
          ("The exterior angles of any convex polygon always sum to:",
           ("180 degrees", "270 degrees", "360 degrees", "It depends on the number of sides"), 2)),
        L(6, "Triangles and Pythagoras", """
            <p><b>Basic:</b> In a right-angled triangle the longest side, opposite the right angle, is the
            <b>hypotenuse</b>. Pythagoras' theorem states <code>a&sup2; + b&sup2; = c&sup2;</code>, where c is the
            hypotenuse. With sides 3 and 4, the hypotenuse is &radic;25 = 5 &mdash; the famous "3-4-5 triangle"
            builders have used for centuries to check a corner is truly square.</p>
            <p>The theorem works only for right-angled triangles, and can also be used backwards to test whether
            a triangle contains a right angle at all.</p>
            <p><b>Intermediate:</b> Pythagoras extends into three dimensions: the longest diagonal of a box with
            sides a, b and c is <code>&radic;(a&sup2; + b&sup2; + c&sup2;)</code>, which is how removal companies work
            out whether a wardrobe will fit diagonally through a doorway.</p>
            <p><b>Pre-advanced:</b> Combined with trigonometry, Pythagoras underlies the distance formula on a
            coordinate grid, <code>d = &radic;((x&#8322;-x&#8321;)&sup2; + (y&#8322;-y&#8321;)&sup2;)</code>, which GPS
            systems use millions of times per second to calculate how far apart two satellites' signals place you.</p>
        """,
          ("A right-angled triangle has short sides 3 and 4. The hypotenuse is:",
           ("5", "6", "7", "12"), 0),
          ("Pythagoras' theorem can be applied to:",
           ("Any triangle", "Right-angled triangles only",
            "Squares only", "Triangles with equal sides only"), 1),
          ("The longest diagonal of a box with sides 2, 3 and 6 is:",
           ("6", "7", "8", "11"), 1),
          ("The distance between points (1, 2) and (4, 6) on a grid is:",
           ("3", "4", "5", "7"), 2)),
        L(7, "Circles", """
            <p><b>Basic:</b> The radius runs from the centre to the edge; the diameter is twice the radius.
            Circumference = <code>2&pi;r</code> and area = <code>&pi;r&sup2;</code>, where &pi; &asymp; 3.14.</p>
            <p>So a circle of radius 5 cm has circumference about 31.4 cm and area about 78.5 cm&sup2;.</p>
            <p><b>Intermediate:</b> A sector is a "slice" of a circle. Its arc length is a fraction of the
            circumference and its area is the same fraction of the total area: a 90&deg; sector of a circle with
            radius 8 cm has area <code>(90/360) &times; &pi; &times; 8&sup2; &asymp; 50.3 cm&sup2;</code> &mdash; exactly
            a quarter of a pizza, in pizza-slicing terms.</p>
            <p><b>Pre-advanced:</b> Radians offer a more natural angle unit for circles: one radian is the angle
            subtended when the arc length equals the radius, so a full turn is <code>2&pi;</code> radians. Formulas
            such as arc length <code>= r&theta;</code> only work directly when &theta; is in radians, which is why
            radians dominate physics and engineering rather than degrees.</p>
        """,
          ("The area of a circle is given by:", ("2&pi;r", "&pi;r&sup2;", "&pi;d", "r&sup2;"), 1),
          ("A circle has diameter 10 cm. Its circumference is roughly:",
           ("15.7 cm", "31.4 cm", "78.5 cm", "100 cm"), 1),
          ("The area of a 90 degree sector of a circle with radius 8 cm is closest to:",
           ("25.1 cm2", "50.3 cm2", "100.5 cm2", "201.1 cm2"), 1),
          ("One full turn in radians is:",
           ("&pi;", "2&pi;", "&pi;/2", "360"), 1)),
        L(8, "Fractions, Decimals and Percentages", """
            <p><b>Basic:</b> These are three ways of writing the same idea: 1/4 = 0.25 = 25%. To find a percentage
            of an amount, convert to a decimal and multiply: 15% of 80 is 0.15 &times; 80 = 12.</p>
            <p>For a percentage increase, multiply by (1 + rate). A 20% rise on 50 gives 50 &times; 1.2 = 60.</p>
            <p><b>Intermediate:</b> Repeated percentage change compounds rather than adds. A price rising 10% then
            falling 10% does <b>not</b> return to the original: <code>100 &times; 1.1 &times; 0.9 = 99</code>, a common
            trap in sale-pricing adverts.</p>
            <p>Reverse percentage problems ask you to find the original value: if a jacket costs &pound;72 after a 20%
            discount, the original price P satisfies <code>0.8P = 72</code>, so <code>P = &pound;90</code>.</p>
            <p><b>Pre-advanced:</b> Compound interest, <code>A = P(1 + r)&#8319;</code>, is the same idea repeated n
            times: &pound;1000 saved at 5% annual interest for 10 years grows to about &pound;1628.89, noticeably more
            than the &pound;1500 simple interest would give, because each year's interest itself earns interest.</p>
        """,
          ("What is 15% of 80?", ("8", "12", "15", "20"), 1),
          ("Increasing 50 by 20% gives:", ("55", "60", "70", "100"), 1),
          ("A price rises 10% then falls 10%. Compared to the original price, the final price is:",
           ("Exactly the same", "1% lower", "1% higher", "10% lower"), 1),
          ("A jacket costs 72 pounds after a 20% discount. The original price was:",
           ("80 pounds", "86.40 pounds", "90 pounds", "92 pounds"), 2),
          ("1000 pounds invested at 5% compound interest for 2 years grows to:",
           ("1050.00 pounds", "1100.00 pounds", "1102.50 pounds", "1150.00 pounds"), 2)),
        L(9, "Ratio and Proportion", """
            <p><b>Basic:</b> A ratio compares quantities, e.g. 2:3. To share &pound;50 in the ratio 2:3, note there
            are 5 parts, so each part is &pound;10, giving &pound;20 and &pound;30.</p>
            <p>Two quantities are in direct proportion when doubling one doubles the other &mdash; like the amount
            of flour and the number of cakes a recipe makes.</p>
            <p><b>Intermediate:</b> In inverse proportion their product stays constant: as one doubles, the other
            halves, which is exactly how more workers finishing a job faster works &mdash; 4 painters take 6 hours,
            so 8 painters (double the workers) take 3 hours (half the time), assuming equal pace.</p>
            <p>Map and model scales are ratios too: a 1:25000 map means 1 cm on paper represents 25000 cm
            (250 m) in reality, so a 6 cm gap on the map is a 1.5 km walk.</p>
            <p><b>Pre-advanced:</b> Combined ratio problems chain several proportions together, such as converting
            currency then splitting a bill, or mixing paint in a ratio and then scaling the recipe up for a bigger
            wall &mdash; the key skill is finding one common "unit" that links every quantity in the chain.</p>
        """,
          ("Sharing 50 in the ratio 2:3 gives:", ("20 and 30", "25 and 25", "10 and 40", "15 and 35"), 0),
          ("In inverse proportion, when one quantity doubles the other:",
           ("Doubles", "Halves", "Stays the same", "Increases by 2"), 1),
          ("4 painters take 6 hours to paint a wall. Assuming equal pace, 8 painters take:",
           ("2 hours", "3 hours", "4 hours", "12 hours"), 1),
          ("On a 1:25000 map, a distance of 6 cm represents in real life:",
           ("150 m", "1500 m", "1.5 km", "Both B and C are correct"), 3)),
        L(10, "Indices and Standard Form", """
            <p><b>Basic:</b> Indices show repeated multiplication: <code>2&#8309; = 32</code>. Rules:
            <code>a&#8319; &times; a&#7504; = a&#8319;&#8314;&#7504;</code> and
            <code>a&#8319; &divide; a&#7504; = a&#8319;&#8315;&#7504;</code>.</p>
            <p>Anything to the power 0 equals 1, and a negative index means a reciprocal:
            <code>2&#8315;&sup3; = 1/8</code>.</p>
            <p><b>Intermediate:</b> Standard form writes numbers as <code>A &times; 10&#8319;</code> with
            1 &le; A &lt; 10, so 4500 becomes <code>4.5 &times; 10&sup3;</code>. Scientists use it constantly: the
            mass of an electron is about <code>9.1 &times; 10&#8315;&sup3;&sup1; kg</code>, a number that would be
            unmanageable written out in full.</p>
            <p>Fractional indices link to roots: <code>a^(1/2) = &radic;a</code> and <code>a^(1/3) = &#8731;a</code>,
            so <code>27^(1/3) = 3</code> because <code>3&sup3; = 27</code>.</p>
            <p><b>Pre-advanced:</b> Combined index laws let you simplify expressions like
            <code>(8x&#8310;)^(2/3) = 4x&#8308;</code> in one line rather than working the cube root and square
            separately, a skill essential for simplifying scientific formulae such as those for orbital period or
            radioactive decay.</p>
        """,
          ("Write 4500 in standard form.",
           ("45 &times; 10&sup2;", "4.5 &times; 10&sup3;", "4.5 &times; 10&#8308;", "0.45 &times; 10&#8308;"), 1),
          ("What is the value of 2&#8315;&sup3;?", ("-8", "-6", "1/8", "6"), 2),
          ("What is 27^(1/3)?", ("3", "9", "13.5", "1/3"), 0),
          ("Simplify (8x&#8310;)^(2/3).", ("2x&sup2;", "4x&#8308;", "4x&sup2;", "8x&#8308;"), 1)),
        L(11, "Coordinates and Straight Line Graphs", """
            <p><b>Basic:</b> Points are written as (x, y), measured from the origin (0, 0). A straight line has
            equation <code>y = mx + c</code>, where m is the gradient (steepness) and c is the y-intercept.</p>
            <p>Gradient = change in y divided by change in x. Parallel lines share the same gradient.</p>
            <p><b>Intermediate:</b> Two lines are perpendicular exactly when the product of their gradients is
            <code>-1</code>, so a line with gradient 2 meets a perpendicular line with gradient <code>-1/2</code> at
            a right angle &mdash; a fact used to design road junctions and to reflect light rays in optics diagrams.</p>
            <p>The midpoint of two points is the average of their coordinates:
            <code>((x&#8321;+x&#8322;)/2, (y&#8321;+y&#8322;)/2)</code>.</p>
            <p><b>Pre-advanced:</b> The equation of a line through two points can be built directly from the
            gradient formula, and finding where two lines cross means solving them as simultaneous equations
            &mdash; the same technique used to find the break-even point between cost and revenue graphs in
            business planning.</p>
        """,
          ("In y = mx + c, the letter m represents the:",
           ("y-intercept", "Gradient", "x value", "Area under the line"), 1),
          ("The line y = 3x + 2 crosses the y-axis at:",
           ("(0, 2)", "(2, 0)", "(0, 3)", "(3, 2)"), 0),
          ("A line with gradient 2 is perpendicular to a line with gradient:",
           ("2", "-2", "1/2", "-1/2"), 3),
          ("The midpoint of (2, 4) and (6, 10) is:",
           ("(4, 7)", "(8, 14)", "(3, 6)", "(4, 6)"), 0)),
        L(12, "Sequences", """
            <p><b>Basic:</b> A sequence is an ordered list of terms. In an <b>arithmetic</b> sequence you add a
            constant difference each time: 3, 7, 11, 15 (difference 4).</p>
            <p>The nth term of that sequence is <code>4n - 1</code>, which lets you jump straight to any term
            without listing them all.</p>
            <p><b>Intermediate:</b> In a <b>geometric</b> sequence you multiply by a constant ratio: 2, 6, 18, 54
            (ratio 3), with nth term <code>2 &times; 3&#8319;&#8315;&sup1;</code>. Compound interest and viral
            social-media sharing both follow geometric growth.</p>
            <p>The sum of the first n terms of an arithmetic sequence is
            <code>S&#8319; = n/2 &times; (2a + (n-1)d)</code>, which famously let a young Gauss add 1 to 100 in
            seconds by pairing numbers from opposite ends.</p>
            <p><b>Pre-advanced:</b> The Fibonacci sequence (1, 1, 2, 3, 5, 8, ...), where each term is the sum of
            the previous two, appears in sunflower seed spirals, pinecones and nautilus shells, and its ratio of
            consecutive terms converges towards the golden ratio &phi; &asymp; 1.618, a number long prized in art
            and architecture.</p>
        """,
          ("The nth term of 3, 7, 11, 15, ... is:", ("n + 4", "4n - 1", "4n + 3", "3n"), 1),
          ("The sequence 2, 6, 18, 54 is:",
           ("Arithmetic with difference 4", "Geometric with ratio 3",
            "Neither", "Geometric with ratio 2"), 1),
          ("The sum of the first 10 terms of 3, 7, 11, 15, ... is:",
           ("165", "195", "210", "225"), 1),
          ("In the Fibonacci sequence 1, 1, 2, 3, 5, 8, ..., the next term after 8 is:",
           ("11", "12", "13", "16"), 2)),
        L(13, "Averages and Data", """
            <p><b>Basic:</b> The <b>mean</b> is the total divided by how many values there are; the <b>median</b>
            is the middle value when ordered; the <b>mode</b> is the most common value.</p>
            <p>The range (largest minus smallest) measures spread, not average. For 2, 3, 3, 8 the mean is 4, the
            median 3, the mode 3 and the range 6.</p>
            <p><b>Intermediate:</b> The mean is sensitive to outliers: if a billionaire walks into a small caf&eacute;,
            the mean customer wealth rockets even though the median (the "typical" customer) barely moves &mdash;
            which is why news reports on income often quote the median rather than the mean.</p>
            <p>Grouped frequency tables let you estimate a mean for continuous data using midpoints of each class
            interval, useful whenever raw data (like exact ages or exact times) is impractical to record.</p>
            <p><b>Pre-advanced:</b> Standard deviation measures how tightly data clusters around the mean. Two
            classes can have identical mean test scores of 65% yet very different standard deviations &mdash; one
            class uniformly scoring around 65%, the other split between students scoring near 40% and near 90% &mdash;
            information the mean alone completely hides.</p>
        """,
          ("For the data 2, 3, 3, 8 the mean is:", ("3", "4", "5", "6"), 1),
          ("The range of a data set measures:",
           ("The most common value", "The middle value", "The spread", "The total"), 2),
          ("Which average is least affected by one extremely large outlier?",
           ("Mean", "Median", "Range", "Total"), 1),
          ("Two data sets have the same mean but different standard deviations. This tells you the sets differ in:",
           ("Their total", "How spread out the values are", "Their mode", "Their sample size"), 1)),
        L(14, "Introduction to Trigonometry", """
            <p><b>Basic:</b> In a right-angled triangle, the ratios of sides depend only on the angles:
            <code>sin&theta; = opp/hyp</code>, <code>cos&theta; = adj/hyp</code>,
            <code>tan&theta; = opp/adj</code> (remember SOH CAH TOA).</p>
            <p>Use them to find a missing side when you know an angle and one side, or a missing angle using the
            inverse functions, e.g. <code>&theta; = tan&#8315;&sup1;(opp/adj)</code>.</p>
            <p><b>Intermediate:</b> Beyond right-angled triangles, the sine rule
            <code>a/sinA = b/sinB = c/sinC</code> and cosine rule <code>c&sup2; = a&sup2; + b&sup2; - 2ab cosC</code>
            solve any triangle, which is exactly how surveyors calculate the height of a mountain from two ground
            measurements without ever climbing it.</p>
            <p>Angles of elevation and depression turn everyday problems &mdash; the angle up to a kite, or down
            from a clifftop to a boat &mdash; into simple right-angled triangle calculations.</p>
            <p><b>Pre-advanced:</b> Extending sin, cos and tan beyond 90&deg; using the unit circle reveals a
            repeating wave pattern; this periodicity is exactly why trigonometric functions model sound waves,
            AC electricity, tides and the length of daylight through the year.</p>
        """,
          ("Which ratio equals opposite divided by hypotenuse?",
           ("sin", "cos", "tan", "None"), 0),
          ("To find an angle when you know the opposite and adjacent sides, use:",
           ("sin", "cos", "tan inverse", "Pythagoras"), 2),
          ("The sine rule states that in any triangle:",
           ("a/sinA = b/sinB = c/sinC", "a + b = c", "sinA + sinB = sinC", "a2 = b2 + c2"), 0),
          ("Which real-world phenomenon is naturally modelled by a repeating sine wave?",
           ("A car braking to a stop", "Alternating current in a wall socket",
            "A ball rolling down a fixed slope", "Compound interest growth"), 1)),
        L(15, "Introduction to Calculus", """
            <p><b>Basic:</b> Calculus studies change. <b>Differentiation</b> finds the gradient of a curve at a
            point &mdash; the instantaneous rate of change, such as a car's speed at one exact moment rather than
            its average speed over a whole journey.</p>
            <p>The rule for powers: if <code>y = x&#8319;</code> then <code>dy/dx = nx&#8319;&#8315;&sup1;</code>.
            So for <code>y = x&sup3;</code>, <code>dy/dx = 3x&sup2;</code>.</p>
            <p><b>Intermediate:</b> Where the gradient is zero the curve has a turning point &mdash; a maximum or
            minimum. A company modelling profit as <code>P = -2x&sup2; + 40x - 50</code> can differentiate,
            set the result to zero, and find the exact production level x that maximises profit, rather than
            guessing.</p>
            <p><b>Integration</b> reverses differentiation and finds the area under a curve: it is how the total
            distance travelled is recovered from a velocity-time graph, even when the speed is constantly
            changing.</p>
            <p><b>Pre-advanced:</b> The second derivative tells you whether a turning point is a maximum or a
            minimum: a negative second derivative means the curve bends downward (a maximum, like the peak of a
            profit curve), while a positive one means it bends upward (a minimum, like the lowest point of a cost
            curve) &mdash; removing the need to sketch the graph to check.</p>
        """,
          ("If y = x&sup3;, then dy/dx is:", ("3x", "x&sup2;", "3x&sup2;", "3x&#8308;"), 2),
          ("At a maximum or minimum point of a curve, the gradient is:",
           ("Zero", "One", "Always positive", "Undefined"), 0),
          ("For P = -2x2 + 40x - 50, the value of x that maximises P is:",
           ("5", "10", "15", "20"), 1),
          ("A negative second derivative at a turning point indicates:",
           ("A minimum", "A maximum", "No turning point", "An inflection point"), 1),
          ("Integration is best described as the reverse process of:",
           ("Simplifying fractions", "Differentiation", "Factorising", "Solving simultaneous equations"), 1)),
        L(16, "Probability", """
            <p><b>Basic:</b> Probability measures how likely an event is, from 0 (impossible) to 1 (certain).
            Rolling a fair six-sided die, the probability of getting a 4 is <code>1/6</code>, since each of the six
            equally likely outcomes has the same chance.</p>
            <p>The probability of an event <b>not</b> happening is <code>1 - P(event)</code>: if there's a 30%
            chance of rain, there's a 70% chance it stays dry.</p>
            <p><b>Intermediate:</b> For independent events (where one outcome does not affect the other), multiply
            the probabilities: the chance of flipping two heads in a row is <code>1/2 &times; 1/2 = 1/4</code>.</p>
            <p>Tree diagrams organise multi-step probability problems, such as drawing two balls from a bag without
            replacement, where the second draw's probabilities change because one ball is already gone &mdash;
            this is a dependent event.</p>
            <p><b>Pre-advanced:</b> Conditional probability, written <code>P(A|B)</code>, asks how likely A is
            <i>given</i> that B has already happened. It is the backbone of real diagnostic reasoning: even a
            99%-accurate medical test can give mostly false positives for a rare disease, because the tiny group of
            genuinely sick people is vastly outnumbered by healthy people who are still occasionally flagged &mdash;
            a surprising result formalised by Bayes' theorem.</p>
        """,
          ("The probability of rolling a 4 on a fair six-sided die is:",
           ("1/2", "1/4", "1/6", "1/3"), 2),
          ("If there is a 30% chance of rain, the chance it stays dry is:",
           ("30%", "50%", "70%", "100%"), 2),
          ("The probability of flipping two heads in a row on a fair coin is:",
           ("1/2", "1/3", "1/4", "1/8"), 2),
          ("Drawing two balls from a bag without replacement is an example of:",
           ("Independent events", "Dependent events", "Impossible events", "Certain events"), 1),
          ("A rare-disease test being mostly wrong on positive results despite being 99% accurate is best explained by:",
           ("The test being broken", "Conditional probability and the disease being rare",
            "Rounding errors", "The test having no false positives"), 1)),
        L(17, "Vectors", """
            <p><b>Basic:</b> A vector has both magnitude (size) and direction, unlike a scalar which has size only.
            Speed is a scalar (30 mph); velocity is a vector (30 mph north). Vectors are often written as column
            pairs, e.g. <code>(3, 4)</code> meaning 3 units across and 4 units up.</p>
            <p>Vectors add "tip to tail": travelling <code>(3, 4)</code> then <code>(1, -2)</code> ends up at
            <code>(4, 2)</code> overall, exactly like following two legs of a journey on a map.</p>
            <p><b>Intermediate:</b> The magnitude of a vector <code>(x, y)</code> is found with Pythagoras,
            <code>&radic;(x&sup2; + y&sup2;)</code>, so <code>(3, 4)</code> has magnitude 5. Multiplying a vector by a
            scalar stretches or shrinks it without changing its direction (or reverses it if the scalar is
            negative).</p>
            <p>Vectors describe forces acting on a bridge, wind affecting a plane's true path, or a game
            character's movement on screen &mdash; anywhere direction matters as much as amount.</p>
            <p><b>Pre-advanced:</b> Two vectors are parallel exactly when one is a scalar multiple of the other,
            which is how engineers check that a support strut is aligned correctly, and the resultant of several
            forces acting on an object is simply the vector sum of them all &mdash; the same idea behind why a boat
            crossing a river drifts downstream even while aiming straight across.</p>
        """,
          ("Which of these is a vector quantity?", ("Speed", "Mass", "Velocity", "Temperature"), 2),
          ("Adding the vectors (3, 4) and (1, -2) gives:",
           ("(4, 2)", "(2, 6)", "(4, -2)", "(3, -8)"), 0),
          ("The magnitude of the vector (3, 4) is:",
           ("5", "7", "12", "25"), 0),
          ("Two vectors are parallel when one is:",
           ("Perpendicular to the other", "A scalar multiple of the other",
            "Equal in magnitude only", "Always pointing north"), 1)),
    ],
}

SUBJECTS["physics"] = {
    "name": "Physics",
    "lessons": [
        L(1, "Introduction to Motion", """
            <p><b>Basic:</b> Motion describes how an object's position changes over time. <b>Speed</b> is distance
            divided by time; <b>velocity</b> is speed together with a direction, which makes it a vector
            quantity.</p>
            <p>A car travelling 100 km in 2 hours has an average speed of 50 km/h, even if it sped up and slowed
            down along the way &mdash; the average hides the detail of the journey.</p>
            <p><b>Intermediate:</b> Distance is how far you have travelled in total; displacement is how far you
            end up from where you started, in a straight line. A runner completing one lap of a 400 m track has
            travelled 400 m but has a displacement of zero, since they finish where they began.</p>
            <p>Relative velocity matters whenever two things move at once: two cars each doing 60 km/h towards each
            other close the gap between them at a combined 120 km/h, which is why head-on collisions are so much
            more dangerous than rear-end ones at the same individual speeds.</p>
            <p><b>Pre-advanced:</b> Instantaneous speed &mdash; the reading on a speedometer at one exact instant
            &mdash; is the limit of average speed as the time interval shrinks towards zero, which is precisely the
            idea differentiation captures in calculus: speed is the derivative of position with respect to time.</p>
        """,
          ("A car travels 100 km in 2 hours. Its average speed is:",
           ("25 km/h", "50 km/h", "100 km/h", "200 km/h"), 1),
          ("What makes velocity different from speed?",
           ("It includes direction", "It is always larger", "It has no units", "There is no difference"), 0),
          ("A runner completes one full lap of a 400 m track. Their displacement is:",
           ("400 m", "200 m", "0 m", "800 m"), 2),
          ("Two cars each travelling at 60 km/h move directly towards each other. The rate at which the gap between them closes is:",
           ("60 km/h", "90 km/h", "120 km/h", "30 km/h"), 2)),
        L(2, "Acceleration and Motion Graphs", """
            <p><b>Basic:</b> Acceleration is the rate of change of velocity, measured in m/s&sup2;:
            <code>a = (v - u) / t</code>. On a distance-time graph the gradient gives speed; a horizontal line
            means the object is stationary.</p>
            <p>On a velocity-time graph the gradient gives acceleration and the area under the line gives the
            distance travelled.</p>
            <p><b>Intermediate:</b> A curved distance-time graph means changing speed &mdash; steepening means
            speeding up, flattening means slowing down. A straight-line velocity-time graph means constant
            acceleration, exactly like a ball rolling down a smooth ramp under gravity.</p>
            <p>The suvat equations connect motion variables when acceleration is constant, e.g.
            <code>v&sup2; = u&sup2; + 2as</code>, letting you find a final speed without ever needing to know the
            time taken &mdash; handy for questions about braking distance.</p>
            <p><b>Pre-advanced:</b> A car's stopping distance is the sum of thinking distance (constant speed during
            reaction time) and braking distance (deceleration under the brakes); doubling the speed roughly
            quadruples the braking distance because braking distance depends on velocity squared, which is why
            speed limits near schools are so much lower than on motorways.</p>
        """,
          ("The gradient of a velocity-time graph represents:",
           ("Distance", "Speed", "Acceleration", "Force"), 2),
          ("A car goes from 0 to 20 m/s in 4 s. Its acceleration is:",
           ("4 m/s2", "5 m/s2", "20 m/s2", "80 m/s2"), 1),
          ("A car braking from 30 m/s to rest has roughly this many times the braking distance of one braking from 15 m/s to rest, assuming equal deceleration:",
           ("2", "3", "4", "8"), 2),
          ("On a velocity-time graph, the area under the line represents:",
           ("Acceleration", "Distance travelled", "Force", "Average speed only"), 1)),
        L(3, "Forces and Newton's Laws", """
            <p><b>Basic:</b> A force is a push or a pull, measured in newtons. Newton's first law: an object stays
            at rest or moves at constant velocity unless a resultant force acts on it (inertia).</p>
            <p>Newton's second law: <code>Force = mass &times; acceleration</code>. Newton's third law: every
            action has an equal and opposite reaction, acting on a different object.</p>
            <p><b>Intermediate:</b> A resultant force is what remains after all forces on an object are combined,
            accounting for direction. A tug-of-war team pulling with 500 N against another pulling 480 N produces a
            resultant force of 20 N, enough to slowly move the rope even though both teams are pulling hard.</p>
            <p>Newton's third law pairs always act on different objects, which is exactly why rockets work in the
            vacuum of space: the rocket pushes exhaust gas backward, and the gas pushes the rocket forward, with no
            air needed to "push against".</p>
            <p><b>Pre-advanced:</b> Free-body diagrams isolate one object and show every force acting on it as an
            arrow; resolving forces at an angle into horizontal and vertical components (using sin and cos) lets
            engineers calculate whether a ladder leaning against a wall will slip, by comparing the resolved
            frictional force to the resolved weight component along the ground.</p>
        """,
          ("A 5 kg mass accelerates at 3 m/s2. The resultant force is:",
           ("1.7 N", "8 N", "15 N", "45 N"), 2),
          ("Newton's first law is also called the law of:",
           ("Gravity", "Inertia", "Reaction", "Momentum"), 1),
          ("Two tug-of-war teams pull with 500 N and 480 N in opposite directions. The resultant force is:",
           ("980 N towards the stronger team", "20 N towards the stronger team",
            "0 N, the rope does not move", "480 N towards the weaker team"), 1),
          ("A rocket accelerates in the vacuum of space because:",
           ("It pushes against the air", "Exhaust gas pushed backward pushes the rocket forward",
            "Gravity pulls it upward", "There is no force acting on it"), 1)),
        L(4, "Gravity, Mass and Weight", """
            <p><b>Basic:</b> Mass is the amount of matter in an object and does not change with location; weight
            is the force of gravity on that mass.</p>
            <p><code>Weight = mass &times; gravitational field strength</code>. On Earth g &asymp; 10 N/kg, so a
            60 kg person weighs about 600 N.</p>
            <p><b>Intermediate:</b> On the Moon g is about one sixth of Earth's, so the same person weighs far less
            (about 100 N) but has exactly the same mass of 60 kg &mdash; an astronaut does not become "lighter" in
            matter, only in the pull felt on them.</p>
            <p>Newton's law of gravitation shows gravitational force weakens with the square of distance: doubling
            the distance between two masses cuts the gravitational force to a quarter, which is why astronauts in
            low orbit still feel almost full Earth gravity but appear "weightless" only because they are in
            continuous free fall around the planet.</p>
            <p><b>Pre-advanced:</b> Because g varies slightly across Earth's surface (higher at the poles than the
            equator due to Earth's shape and rotation), extremely precise weighing scales are calibrated to their
            location, even though everyday bathroom scales never need this correction.</p>
        """,
          ("The weight of a 60 kg person on Earth (g = 10 N/kg) is about:",
           ("6 N", "60 N", "600 N", "6000 N"), 2),
          ("Taking an object to the Moon changes its:",
           ("Mass only", "Weight only", "Both mass and weight", "Neither"), 1),
          ("Doubling the distance between two masses changes the gravitational force between them to:",
           ("Half", "A quarter", "Double", "The same"), 1),
          ("Astronauts in low orbit appear weightless mainly because they are:",
           ("Far beyond Earth's gravity", "In continuous free fall around the Earth",
            "Not affected by mass", "In a vacuum with no gravity at all"), 1)),
        L(5, "Work, Energy and Power", """
            <p><b>Basic:</b> Work done = force &times; distance moved in the direction of the force, measured in
            joules. Energy is conserved: it transfers between stores such as kinetic
            (<code>&frac12;mv&sup2;</code>) and gravitational potential (<code>mgh</code>).</p>
            <p>Power is the rate of energy transfer: <code>P = E / t</code>, measured in watts.</p>
            <p><b>Intermediate:</b> A roller coaster converts gravitational potential energy at the top of the
            first hill almost entirely into kinetic energy at the bottom, then back again on the next rise &mdash;
            friction and air resistance are the only reason it cannot climb back to quite the same height.</p>
            <p>Efficiency compares useful output energy to total input energy, expressed as a percentage: a
            lightbulb converting 60 J of electrical energy into 12 J of light and 48 J of wasted heat is only 20%
            efficient.</p>
            <p><b>Pre-advanced:</b> Because kinetic energy depends on velocity <i>squared</i>, doubling a car's
            speed quadruples its kinetic energy, which is why the same braking force takes four times the distance
            to stop a car travelling twice as fast &mdash; a direct real-world consequence of the energy equation,
            not just a rule to memorise.</p>
        """,
          ("Power is best described as:",
           ("Total energy used", "Energy transferred per second", "Force times distance", "Mass times acceleration"), 1),
          ("A force of 20 N moves an object 3 m. Work done is:",
           ("6 J", "23 J", "60 J", "600 J"), 2),
          ("A lightbulb takes in 60 J of electrical energy and outputs 12 J of light. Its efficiency is:",
           ("12%", "20%", "48%", "60%"), 1),
          ("If a car's speed doubles, its kinetic energy becomes:",
           ("The same", "Double", "Triple", "Four times as much"), 3)),
        L(6, "Momentum", """
            <p><b>Basic:</b> Momentum = mass &times; velocity, measured in kg m/s, and it is a vector. In a closed
            system total momentum before a collision equals total momentum after &mdash; the principle of
            conservation of momentum.</p>
            <p>Crumple zones and airbags increase the time taken to change momentum, which reduces the force
            experienced, since <code>F = &Delta;p / &Delta;t</code>.</p>
            <p><b>Intermediate:</b> In an explosion (like a firework or a gun firing), momentum before is zero, so
            the fragments must fly apart with equal and opposite total momentum &mdash; the recoil felt on a rifle
            is exactly this principle in action.</p>
            <p>Collisions can be elastic (kinetic energy is also conserved, like billiard balls) or inelastic
            (kinetic energy is lost to heat and sound, like a car crash), but momentum is conserved in both
            cases.</p>
            <p><b>Pre-advanced:</b> Impulse, <code>J = F&Delta;t</code>, equals the change in momentum an object
            experiences. This is why a boxer "rolling with the punch" reduces injury: extending the contact time
            over which the punch's momentum is absorbed lowers the peak force felt, even though the total impulse
            delivered is unchanged.</p>
        """,
          ("Momentum is calculated as:",
           ("mass x acceleration", "mass x velocity", "force x time", "half m v squared"), 1),
          ("Airbags reduce injury because they:",
           ("Increase the force", "Increase the time over which momentum changes",
            "Reduce the mass", "Increase the velocity"), 1),
          ("A firework explodes from rest into fragments. The total momentum of all the fragments immediately after is:",
           ("Equal to the momentum just before, which is zero", "Always positive", "Always negative", "Undefined"), 0),
          ("Which quantity is conserved in both elastic and inelastic collisions?",
           ("Kinetic energy", "Momentum", "Both kinetic energy and momentum", "Neither"), 1)),
        L(7, "Density and Pressure", """
            <p><b>Basic:</b> Density = mass / volume, usually in kg/m&sup3;. Objects less dense than a fluid float
            in it. Pressure = force / area, measured in pascals.</p>
            <p>A sharp knife has a tiny contact area, so a modest force gives a very high pressure, which is why a
            blunt knife (larger contact area, same force) struggles to cut at all.</p>
            <p><b>Intermediate:</b> In a liquid, pressure increases with depth (<code>P = &rho;gh</code>) and acts
            in all directions equally at a given depth, which is why a deep-sea submersible needs a far stronger
            hull than a surface boat, and why your ears "pop" diving to the bottom of a swimming pool.</p>
            <p>An object floats when the upthrust from displaced fluid equals its weight (Archimedes' principle)
            &mdash; a steel ship floats not because steel is light, but because its hollow shape displaces enough
            water to generate sufficient upthrust.</p>
            <p><b>Pre-advanced:</b> Pascal's principle states that pressure applied to an enclosed fluid is
            transmitted equally throughout it, which is the working principle behind hydraulic car jacks: a small
            force on a narrow piston creates enough pressure to lift a car's full weight on a much wider piston, at
            the cost of having to push the small piston a much greater distance.</p>
        """,
          ("Pressure is calculated as:",
           ("Force x area", "Force / area", "Area / force", "Mass / volume"), 1),
          ("Pressure in a liquid increases as you go:",
           ("Deeper", "Shallower", "Sideways only", "It stays constant"), 0),
          ("A steel ship floats mainly because:",
           ("Steel is less dense than water", "It displaces enough water to create sufficient upthrust",
            "It has no weight in water", "Its engines push it up"), 1),
          ("A hydraulic jack lifts a heavy car with a small applied force mainly because:",
           ("Pressure is transmitted equally through the enclosed fluid to a wider piston",
            "The fluid loses mass", "Gravity is weaker inside the jack", "The car becomes lighter"), 0)),
        L(8, "Heat and Temperature", """
            <p><b>Basic:</b> Temperature measures how hot something is; thermal energy depends on both temperature
            and mass. Heat transfers by conduction (through solids), convection (in fluids, driven by density
            differences) and radiation (infrared waves, needing no medium).</p>
            <p>Insulation, such as trapped air in a jumper, slows conduction and convection.</p>
            <p><b>Intermediate:</b> Specific heat capacity is the energy needed to raise 1 kg of a substance by
            1&deg;C. Water has an unusually high specific heat capacity, which is why coastal regions have milder
            climates than inland areas at the same latitude &mdash; the sea absorbs and releases huge amounts of
            heat with only small temperature swings.</p>
            <p>During a change of state, temperature stays constant even while energy (latent heat) is still being
            added or removed, which is why ice at 0&deg;C stays at 0&deg;C throughout melting rather than warming
            up immediately.</p>
            <p><b>Pre-advanced:</b> Dark, matte surfaces are both better absorbers and better emitters of infrared
            radiation than light, shiny ones, which is why a matte black car interior gets far hotter in the sun
            than a white one, and why vacuum flasks use a shiny inner lining to minimise radiative heat loss.</p>
        """,
          ("Energy from the Sun reaches Earth by:",
           ("Conduction", "Convection", "Radiation", "Evaporation"), 2),
          ("Convection currents occur because heated fluid becomes:",
           ("Denser and sinks", "Less dense and rises", "Solid", "Colder"), 1),
          ("Water's unusually high specific heat capacity helps explain why coastal climates are:",
           ("More extreme than inland climates", "Milder than inland climates at the same latitude",
            "Always colder", "Unaffected by the sea"), 1),
          ("While ice melts at 0 degrees Celsius, its temperature:",
           ("Rises steadily", "Falls", "Stays constant until melting is complete", "Increases then decreases"), 2)),
        L(9, "Waves", """
            <p><b>Basic:</b> Waves transfer energy without transferring matter. In <b>transverse</b> waves the
            oscillation is perpendicular to travel (light); in <b>longitudinal</b> waves it is parallel (sound).</p>
            <p>Key terms: amplitude, wavelength, frequency (hertz) and period. The wave equation is
            <code>v = f&lambda;</code>: speed equals frequency times wavelength.</p>
            <p><b>Intermediate:</b> Amplitude relates to the energy a wave carries (louder sound, brighter light),
            while frequency relates to pitch or colour &mdash; two completely independent properties, so a loud
            low note and a quiet high note are entirely possible.</p>
            <p>Waves reflect, refract (change speed and bend at a boundary) and diffract (spread out through gaps
            or around obstacles); diffraction is most noticeable when the gap is close to the wavelength in size,
            which is why you can hear someone around a corner but rarely see them.</p>
            <p><b>Pre-advanced:</b> The Doppler effect explains why an ambulance siren sounds higher-pitched
            approaching and lower-pitched departing: the wavelength is compressed ahead of the moving source and
            stretched behind it, and the same principle applied to light from distant galaxies (redshift) provides
            key evidence that the universe is expanding.</p>
        """,
          ("The wave equation is:",
           ("v = f + lambda", "v = f lambda", "v = lambda / f", "f = v lambda"), 1),
          ("Sound waves are:",
           ("Transverse", "Longitudinal", "Electromagnetic", "Stationary"), 1),
          ("Diffraction of a wave through a gap is most noticeable when the gap size is:",
           ("Much larger than the wavelength", "Much smaller than the wavelength",
            "Close to the wavelength in size", "Diffraction does not depend on gap size"), 2),
          ("An ambulance siren sounds higher pitched as it approaches because:",
           ("It is playing a different note", "The wavelength ahead of it is compressed, raising frequency",
            "The amplitude increases", "Sound speeds up as it approaches"), 1)),
        L(10, "Sound and Hearing", """
            <p><b>Basic:</b> Sound is a longitudinal wave of compressions and rarefactions, so it needs a medium
            and cannot travel through a vacuum. Higher frequency is heard as higher pitch; larger amplitude is
            heard as greater loudness.</p>
            <p>Sound travels faster in solids than in liquids, and faster in liquids than in gases, because
            particles are closer together and transmit vibrations more readily.</p>
            <p><b>Intermediate:</b> The human ear typically hears frequencies from about 20 Hz to 20,000 Hz; sound
            above this range (ultrasound) is used in medical scanning and by bats for echolocation, while sound
            below it (infrasound) can travel huge distances and is produced by elephants and some seismic events.</p>
            <p>Echo timing (time taken for a reflected sound to return) is used in sonar to measure the depth of
            the seabed: <code>distance = (speed &times; time) / 2</code>, dividing by two because the sound
            travels down and back.</p>
            <p><b>Pre-advanced:</b> Resonance occurs when a periodic force matches an object's natural frequency,
            dramatically amplifying oscillation &mdash; the mechanism opera singers rely on (in myth, at least) to
            shatter a wine glass, and a real engineering hazard that caused the Tacoma Narrows Bridge to oscillate
            itself apart in 1940.</p>
        """,
          ("Sound cannot travel through:",
           ("Water", "Steel", "A vacuum", "Air"), 2),
          ("Increasing the frequency of a sound increases its:",
           ("Loudness", "Pitch", "Speed", "Amplitude"), 1),
          ("Sonar measures seabed depth from echo timing using distance equals:",
           ("speed x time", "speed x time / 2", "time / speed", "speed / time"), 1),
          ("A structure oscillating violently because a driving force matches its natural frequency is an example of:",
           ("Diffraction", "Refraction", "Resonance", "The Doppler effect"), 2)),
        L(11, "Light and Optics", """
            <p><b>Basic:</b> Light travels in straight lines and reflects so that the angle of incidence equals the
            angle of reflection. Refraction is the bending of light when it changes speed entering a new medium,
            which is why a straw looks bent in water.</p>
            <p>Converging lenses bring parallel rays to a focus and are used in cameras and eyes; white light can
            be dispersed into a spectrum by a prism.</p>
            <p><b>Intermediate:</b> The refractive index of a material measures how much it slows and bends light;
            diamond's very high refractive index is exactly why cut diamonds sparkle so intensely &mdash; light
            entering is bent sharply and bounces internally before escaping.</p>
            <p>Total internal reflection happens when light hits a boundary at an angle beyond the "critical
            angle" and cannot exit at all, instead reflecting entirely back inside &mdash; the principle that
            allows optical fibres to carry internet data as light pulses over huge distances with minimal loss.</p>
            <p><b>Pre-advanced:</b> A converging lens forms a real, inverted image when an object is beyond the
            focal length, but a virtual, upright, magnified image when the object sits inside the focal length
            &mdash; exactly the difference between how a camera lens and a magnifying glass are used, despite being
            the same basic shape of glass.</p>
        """,
          ("Light bending as it passes from air into glass is called:",
           ("Reflection", "Refraction", "Diffraction", "Dispersion"), 1),
          ("In reflection, the angle of incidence is:",
           ("Always 90 degrees", "Equal to the angle of reflection", "Twice the angle of reflection", "Always zero"), 1),
          ("Optical fibres transmit light over long distances using the principle of:",
           ("Dispersion", "Diffraction", "Total internal reflection", "The Doppler effect"), 2),
          ("A magnifying glass produces an upright, magnified image when the object is placed:",
           ("Beyond the focal length", "Exactly at the focal length",
            "Inside the focal length", "Anywhere at all"), 2)),
        L(12, "Current, Voltage and Resistance", """
            <p><b>Basic:</b> Current is the rate of flow of charge, measured in amperes; voltage is the energy
            given per unit charge, measured in volts. Resistance opposes current. Ohm's law states
            <code>V = IR</code>.</p>
            <p>So a 12 V supply pushing 2 A through a component means the component has a resistance of 6
            ohms.</p>
            <p><b>Intermediate:</b> Resistance in a wire increases with length, decreases with cross-sectional
            area, and depends on the material (resistivity) &mdash; exactly why thick, short cables are used for
            heavy-current appliances, and thin, long wires make good heating elements because their resistance
            converts electrical energy efficiently to heat.</p>
            <p>Most conductors' resistance rises with temperature as vibrating atoms increasingly obstruct electron
            flow, while some materials become superconductors (zero resistance) when cooled close to absolute
            zero, allowing current to flow indefinitely with no energy loss.</p>
            <p><b>Pre-advanced:</b> Power dissipated by a resistor can be written three equivalent ways:
            <code>P = IV</code>, <code>P = I&sup2;R</code> or <code>P = V&sup2;/R</code>, and choosing the right
            version for the information given (often <code>I&sup2;R</code> when current is fixed by a series
            circuit) avoids unnecessary extra calculation steps.</p>
        """,
          ("Ohm's law is written as:", ("V = I/R", "V = IR", "I = VR", "R = VI"), 1),
          ("A 12 V supply drives 2 A through a resistor. Its resistance is:",
           ("2 ohms", "6 ohms", "14 ohms", "24 ohms"), 1),
          ("A longer wire of the same material and cross-section has:",
           ("Lower resistance", "Higher resistance", "The same resistance", "No resistance"), 1),
          ("A resistor carries a current of 3 A and has resistance 4 ohms. The power dissipated is:",
           ("12 W", "16 W", "24 W", "36 W"), 3)),
        L(13, "Electrical Circuits", """
            <p><b>Basic:</b> In a <b>series</b> circuit there is one path: current is the same everywhere and the
            supply voltage is shared between components.</p>
            <p>In a <b>parallel</b> circuit there are branches: each branch gets the full supply voltage and the
            currents in the branches add up to the total.</p>
            <p><b>Intermediate:</b> Adding resistors in series increases total resistance
            (<code>R = R&#8321; + R&#8322;</code>); adding them in parallel decreases it, since extra branches give
            charge more routes to flow through, described by
            <code>1/R = 1/R&#8321; + 1/R&#8322;</code>.</p>
            <p>This is exactly why household wiring uses parallel circuits: each appliance gets the full mains
            voltage and can be switched independently, so a fault or off-switch on one lamp does not cut power to
            the rest of the house, unlike old-style series Christmas tree lights.</p>
            <p><b>Pre-advanced:</b> A voltmeter (very high resistance) is connected in parallel to measure voltage
            without disturbing the circuit's current, while an ammeter (very low resistance) is connected in series
            to measure current without significantly affecting the voltage &mdash; getting either one the wrong
            way round noticeably distorts the reading or can damage the meter.</p>
        """,
          ("In a series circuit, the current:",
           ("Is the same at every point", "Splits between components",
            "Is zero", "Doubles at each component"), 0),
          ("Components in parallel each receive:",
           ("A share of the supply voltage", "The full supply voltage", "No voltage", "Double the voltage"), 1),
          ("Household wiring uses parallel circuits mainly because:",
           ("It uses less wire", "Each appliance gets full voltage and can be switched independently",
            "It reduces total current", "Parallel circuits are always safer from fire"), 1),
          ("A voltmeter should be connected in a circuit:",
           ("In series, with low resistance", "In parallel, with very high resistance",
            "In series, with very high resistance", "In parallel, with low resistance"), 1)),
        L(14, "Magnetism and Electromagnetism", """
            <p><b>Basic:</b> Magnets have north and south poles; like poles repel and unlike poles attract.
            A current in a wire creates a magnetic field around it.</p>
            <p>Coiling the wire into a solenoid around an iron core makes an electromagnet that can be switched on
            and off, unlike a permanent magnet.</p>
            <p><b>Intermediate:</b> A current-carrying wire in a magnetic field experiences a force &mdash; the
            motor effect &mdash; and reversing either the current direction or the field direction reverses the
            force, which is the basic working principle of every electric motor, from a hairdryer to an electric
            car.</p>
            <p>Moving a magnet near a coil induces a voltage (electromagnetic induction), and the faster the
            relative movement, the greater the induced voltage &mdash; exactly how a bicycle dynamo lights a lamp
            more brightly the faster you pedal.</p>
            <p><b>Pre-advanced:</b> Generators and motors are essentially the same device run in reverse: a
            generator converts mechanical movement into electrical current via induction, while a motor converts
            electrical current into mechanical movement via the motor effect, which is why regenerative braking in
            electric vehicles can recharge the battery by running the drive motor as a generator while
            decelerating.</p>
        """,
          ("Two north poles placed near each other will:",
           ("Attract", "Repel", "Do nothing", "Become south poles"), 1),
          ("Moving a magnet into a coil of wire will:",
           ("Induce a voltage", "Destroy the magnet", "Stop the current", "Have no effect"), 0),
          ("Pedalling a bicycle dynamo faster makes the lamp brighter because:",
           ("The magnet gets stronger", "Faster relative movement induces a greater voltage",
            "The wire gets thicker", "Resistance decreases with speed"), 1),
          ("Regenerative braking in an electric car works by:",
           ("Using the motor as a generator to recharge the battery", "Reversing gravity",
            "Disconnecting the battery entirely", "Increasing tyre friction only"), 0)),
        L(15, "Atoms and Radioactivity", """
            <p><b>Basic:</b> An atom has a tiny nucleus of protons and neutrons, surrounded by electrons. Unstable
            nuclei decay and emit radiation: alpha (stopped by paper), beta (stopped by thin aluminium) and gamma
            (reduced by thick lead).</p>
            <p>Half-life is the time for half the undecayed nuclei in a sample to decay &mdash; a random process
            that is predictable only on average.</p>
            <p><b>Intermediate:</b> Because decay is random for any single nucleus but statistically predictable
            for huge numbers of them, a sample with a 10-day half-life still has one quarter of its original
            activity left after 20 days (two half-lives), and one eighth after 30 days (three half-lives) &mdash;
            exponential, not linear, decline.</p>
            <p>Carbon dating uses the known half-life of carbon-14 (about 5,730 years) to estimate the age of
            once-living material, comparing the remaining carbon-14 to the stable carbon-12 it started with.</p>
            <p><b>Pre-advanced:</b> Nuclear fission (splitting large unstable nuclei, used in power stations) and
            nuclear fusion (joining light nuclei, the process powering the Sun) both release energy because the
            resulting nuclei have slightly less mass than the starting materials, with that "missing" mass
            converted directly to energy according to <code>E = mc&sup2;</code>.</p>
        """,
          ("Which type of radiation is the most penetrating?",
           ("Alpha", "Beta", "Gamma", "They are equal"), 2),
          ("Half-life is the time taken for:",
           ("All nuclei to decay", "Half the undecayed nuclei to decay",
            "The mass to double", "Radiation to stop entirely"), 1),
          ("A sample with a 10-day half-life will have this fraction of its original activity left after 30 days:",
           ("1/2", "1/3", "1/6", "1/8"), 3),
          ("Nuclear fission and fusion both release energy mainly because:",
           ("Protons are destroyed", "The products have slightly less mass, converted to energy via E=mc2",
            "Electrons are gained", "The nucleus gets heavier"), 1)),
        L(16, "Energy Resources", """
            <p><b>Basic:</b> Energy resources are grouped as renewable (replenished naturally, such as solar, wind,
            hydroelectric and geothermal) or non-renewable (finite, such as coal, oil, gas and nuclear fuel).</p>
            <p>A power station's job, whatever the fuel, is usually the same: generate heat, boil water into
            steam, and spin a turbine connected to a generator &mdash; only the heat source changes.</p>
            <p><b>Intermediate:</b> Renewables avoid ongoing fuel costs and carbon dioxide emissions during
            operation, but many are intermittent (solar produces nothing at night, wind depends on weather),
            creating a real engineering challenge in matching supply to constantly changing demand.</p>
            <p>Energy storage &mdash; batteries, or pumping water uphill in a reservoir during low demand to
            release it through a turbine later &mdash; helps smooth out this mismatch between when energy is
            generated and when it is needed.</p>
            <p><b>Pre-advanced:</b> Comparing energy resources fairly means weighing more than just running
            efficiency: build cost, land use, waste disposal (nuclear), habitat disruption (large hydro dams) and
            lifecycle carbon emissions (manufacturing solar panels or wind turbines is not itself carbon-free) all
            factor into genuinely sustainable energy policy.</p>
        """,
          ("Which of these is a renewable energy resource?",
           ("Coal", "Natural gas", "Wind", "Oil"), 2),
          ("A major challenge with solar and wind power is that they are:",
           ("Too expensive to build at all", "Intermittent and depend on weather or time of day",
            "Illegal in most countries", "Unable to generate any electricity"), 1),
          ("Pumped-storage hydroelectric schemes mainly help the grid by:",
           ("Generating power with zero cost ever", "Storing energy to release later when demand is high",
            "Removing the need for any other power stations", "Preventing all blackouts permanently"), 1)),
    ],
}

SUBJECTS["computer_science"] = {
    "name": "Computer Science",
    "lessons": [
        L(1, "How Computers Store Data", """
            <p><b>Basic:</b> Computers store everything as <b>binary</b> &mdash; sequences of 0s and 1s called
            bits, because circuits reliably represent just two states: on and off.</p>
            <p>8 bits make 1 <b>byte</b>, which can hold a value from 0 to 255 or a single character.</p>
            <p><b>Intermediate:</b> Text is stored using a character encoding that maps each symbol to a number:
            ASCII covers 128 basic characters in 7 bits, while Unicode (UTF-8) extends this to represent virtually
            every writing system and emoji on Earth, using more bytes for less common characters.</p>
            <p>Photos, music and this lesson are all ultimately patterns of bits interpreted according to a file
            format &mdash; the same 1,000,000 bits could be a tiny image or ten seconds of low-quality audio,
            depending entirely on how the software agrees to read them.</p>
            <p><b>Pre-advanced:</b> Storage capacity multiplies fast: a kilobyte is roughly 1,000 bytes, a
            megabyte roughly a million, a gigabyte roughly a billion. A basic text file might be a few kilobytes,
            while a single high-resolution photo can be several megabytes &mdash; explaining why photo and video
            storage, not text, dominates most people's phone storage.</p>
        """,
          ("How many bits make up one byte?", ("4", "8", "16", "32"), 1),
          ("A single byte can represent values from:", ("0 to 8", "0 to 100", "0 to 255", "0 to 1024"), 2),
          ("Compared to ASCII, Unicode (UTF-8) is designed mainly to:",
           ("Use fewer bits for every character", "Represent a much wider range of world characters and symbols",
            "Replace binary with decimal", "Only work for English text"), 1),
          ("Roughly how many bytes are in one megabyte?",
           ("A thousand", "A million", "A billion", "A trillion"), 1)),
        L(2, "Number Systems", """
            <p><b>Basic:</b> Denary (base 10) uses digits 0-9; binary (base 2) uses 0-1; hexadecimal (base 16)
            uses 0-9 then A-F.</p>
            <p>In binary, place values double: 1011 is 8 + 0 + 2 + 1 = 11 in denary.</p>
            <p><b>Intermediate:</b> Hex is popular with programmers because one hex digit represents exactly four
            bits, making long binary strings readable: the byte <code>11110000</code> is simply <code>F0</code> in
            hex, far easier to read, type and remember than sixteen raw digits.</p>
            <p>Colours on screen are commonly written in hex, like <code>#FF5733</code>, where each pair of hex
            digits gives the red, green and blue brightness from 00 to FF (0 to 255).</p>
            <p><b>Pre-advanced:</b> Converting denary to binary repeatedly divides by 2 and records the
            remainders in reverse order; converting binary to denary sums the place values where a 1 appears.
            Signed binary numbers (representing negatives) commonly use two's complement, where flipping every bit
            and adding 1 lets ordinary binary addition circuits handle subtraction with no extra hardware.</p>
        """,
          ("The binary number 1011 equals which denary value?", ("7", "9", "11", "13"), 2),
          ("One hexadecimal digit represents how many bits?", ("2", "4", "8", "16"), 1),
          ("The hex colour code FF5733 represents values for which three channels?",
           ("File, folder, format", "Red, green, blue", "Height, width, depth", "Font, frame, fill"), 1),
          ("Two's complement is mainly used to:",
           ("Speed up text encoding", "Represent negative numbers using ordinary binary addition circuits",
            "Store images more efficiently", "Convert hex to denary"), 1)),
        L(3, "Hardware and the CPU", """
            <p><b>Basic:</b> The CPU fetches, decodes and executes instructions in a continuous cycle. Key parts
            are the control unit, the arithmetic logic unit (ALU) and registers; cache is small fast memory close
            to the CPU.</p>
            <p>RAM is volatile working memory, lost when power goes; secondary storage such as an SSD keeps data
            permanently.</p>
            <p><b>Intermediate:</b> Clock speed (measured in GHz) tells you how many fetch-decode-execute cycles
            the CPU can attempt per second, but it is not the whole story: modern CPUs also have multiple cores
            that run instructions in parallel, so a 4-core 3 GHz chip can often outperform a single-core 5 GHz
            chip on tasks that split neatly across cores, like video editing.</p>
            <p>Cache memory exists because RAM, while fast, is still far slower than the CPU itself; storing
            recently or frequently used data in tiny, extremely fast cache reduces how often the CPU must wait on
            slower RAM.</p>
            <p><b>Pre-advanced:</b> The von Neumann bottleneck describes the fundamental limit that a CPU and
            memory share a single bus, so no matter how fast the CPU gets, it can only fetch data as fast as that
            shared connection allows &mdash; a key reason cache hierarchies and multiple cores, rather than raw
            clock speed alone, have driven most performance gains in the last two decades.</p>
        """,
          ("The repeating cycle a CPU performs is:",
           ("Save-load-print", "Fetch-decode-execute", "Read-write-delete", "Input-output"), 1),
          ("RAM is described as volatile because it:",
           ("Is very fast", "Loses its contents without power", "Cannot be upgraded", "Stores programs forever"), 1),
          ("A 4-core 3 GHz processor can outperform a single-core 5 GHz processor mainly when tasks:",
           ("Cannot be split across cores", "Split neatly to run in parallel across multiple cores",
            "Use no memory at all", "Run only one instruction ever"), 1),
          ("Cache memory improves performance mainly by:",
           ("Replacing RAM entirely", "Storing frequently used data closer to the CPU than RAM",
            "Increasing hard disk space", "Making the CPU clock faster"), 1)),
        L(4, "Software and Operating Systems", """
            <p><b>Basic:</b> System software runs the machine; application software does jobs for the user. An
            operating system manages memory, processes, files, devices and user accounts, hiding hardware
            complexity behind a consistent interface.</p>
            <p>Utility programs handle housekeeping such as backup, compression and virus scanning.</p>
            <p><b>Intermediate:</b> Multitasking on a single-core CPU is actually an illusion created by rapid
            task-switching, giving each running program a tiny time slice in turn, so quickly that it appears as
            if everything runs simultaneously &mdash; the same trick your phone uses to run music, messaging and a
            game "at once" on limited cores.</p>
            <p>Device drivers translate general operating-system commands into the specific instructions a
            particular printer, graphics card or mouse understands, which is why installing new hardware often
            means installing its matching driver software first.</p>
            <p><b>Pre-advanced:</b> Virtual memory lets an operating system present programs with more memory than
            physically exists, by temporarily moving less-used data from RAM to disk storage; this expands what a
            computer can run at once but is much slower than true RAM, which is exactly the sluggish feeling you
            get when a computer is "thrashing" under too many open programs.</p>
        """,
          ("Which is an example of application software?",
           ("Windows", "A word processor", "A device driver", "The BIOS"), 1),
          ("A key job of an operating system is:",
           ("Writing your documents", "Managing memory and processes",
            "Designing hardware", "Compiling all code"), 1),
          ("Apparent multitasking on a single-core CPU is actually achieved by:",
           ("Running two CPUs at once", "Rapidly switching between tasks in tiny time slices",
            "Disabling background programs", "Doubling the clock speed"), 1),
          ("Virtual memory allows a computer to run more programs than RAM alone permits by:",
           ("Deleting unused programs permanently", "Temporarily moving less-used data to disk storage",
            "Increasing the CPU's clock speed", "Compressing all running code"), 1)),
        L(5, "Introduction to Algorithms", """
            <p><b>Basic:</b> An algorithm is a precise step-by-step set of instructions for solving a problem. To
            find the largest number in a list, assume the first is largest, then compare it with each remaining
            number, updating whenever a bigger one appears.</p>
            <p>Good algorithms are unambiguous, finite (they stop) and correct. They can be planned with
            pseudocode or flowcharts before coding.</p>
            <p><b>Intermediate:</b> The same problem can often be solved by more than one algorithm, and the
            "best" choice depends on context: finding a friend's number in an unsorted phone contact list by eye
            is a linear search, while looking a word up in a paper dictionary (which is already sorted) is closer
            to a binary search &mdash; you naturally jump to roughly the right section rather than reading every
            page.</p>
            <p>Abstraction &mdash; hiding unnecessary detail to focus on what matters &mdash; and decomposition
            &mdash; breaking a big problem into smaller ones &mdash; are the two core thinking skills behind
            writing any useful algorithm, whether by a human or eventually turned into code.</p>
            <p><b>Pre-advanced:</b> Some problems have no known efficient algorithm at all: the travelling
            salesperson problem (finding the shortest route visiting several cities once) becomes computationally
            explosive as more cities are added, which is why real logistics companies use approximate, "good
            enough" algorithms rather than guaranteeing the perfect route.</p>
        """,
          ("An algorithm is best described as:",
           ("A programming language", "A step-by-step set of instructions",
            "A type of hardware", "A file format"), 1),
          ("Which is NOT a property of a good algorithm?",
           ("It terminates", "It is unambiguous", "It runs forever", "It gives a correct result"), 2),
          ("Breaking a large problem into smaller, more manageable sub-problems is called:",
           ("Abstraction", "Decomposition", "Iteration", "Compilation"), 1),
          ("The travelling salesperson problem is notable in computer science because:",
           ("It has a simple one-line solution", "No known algorithm solves it perfectly in reasonable time as cities increase",
            "It cannot be solved approximately", "It only applies to sorting"), 1)),
        L(6, "Searching Algorithms", """
            <p><b>Basic:</b> A <b>linear search</b> checks each item in turn. It works on any list but is slow
            for large data. A <b>binary search</b> repeatedly halves a <i>sorted</i> list, discarding the half
            that cannot contain the target.</p>
            <p>Binary search finds an item among a million sorted records in about 20 comparisons.</p>
            <p><b>Intermediate:</b> Linear search takes, on average, about n/2 comparisons for a list of n items,
            and up to n in the worst case (the item is last, or missing entirely) &mdash; its performance is said
            to be O(n).</p>
            <p>Binary search's advantage grows dramatically with size: doubling the list size adds only one extra
            comparison step on average, which is exactly why every well-designed search engine, database index
            and even the game "guess my number between 1 and 100" relies on repeatedly halving the possibilities
            rather than checking one at a time.</p>
            <p><b>Pre-advanced:</b> Binary search's requirement that data already be sorted is not free: sorting
            itself costs time, so a list only searched once might genuinely be faster with a plain linear search,
            while a list searched thousands of times easily justifies sorting it first &mdash; a real trade-off
            professional developers weigh, not an automatic "binary search always wins" rule.</p>
        """,
          ("Binary search requires the data to be:",
           ("Sorted", "Unsorted", "Numeric only", "Stored in a file"), 0),
          ("Linear search works by:",
           ("Halving the list", "Checking items one by one", "Sorting first", "Guessing randomly"), 1),
          ("Roughly how many comparisons does binary search need for a sorted list of one million items?",
           ("About 20", "About 1,000", "About 500,000", "About 1,000,000"), 0),
          ("Binary search is not automatically the best choice when:",
           ("The list is searched extremely often", "The list is very large",
            "The list is searched only once and must be sorted first just for that search", "The list never changes"), 2)),
        L(7, "Sorting Algorithms", """
            <p><b>Basic:</b> <b>Bubble sort</b> repeatedly compares neighbouring items and swaps them if out of
            order; simple but slow. <b>Insertion sort</b> builds a sorted section by inserting each new item into
            place, and is efficient on nearly sorted data.</p>
            <p><b>Merge sort</b> splits the list in half, sorts each half and merges them; it is much faster on
            large lists.</p>
            <p><b>Intermediate:</b> Bubble sort's worst-case performance is O(n&sup2;): sorting a list twice as
            long takes roughly four times as long, which becomes painfully slow on large datasets &mdash; sorting
            a million-item list this way could take an impractically long time on ordinary hardware.</p>
            <p>Merge sort's divide-and-conquer approach achieves O(n log n), noticeably better at scale: doubling
            the list barely more than doubles the work, which is why production software (database engines,
            spreadsheet "sort" buttons) never uses bubble sort in practice.</p>
            <p><b>Pre-advanced:</b> Real-world sorting libraries often use hybrid algorithms &mdash; for example
            switching to insertion sort for very small sublists inside an otherwise merge-sort or quicksort
            process &mdash; because insertion sort's simplicity actually beats fancier algorithms' overhead once a
            list is small enough, showing that "best" always depends on the actual data size and shape.</p>
        """,
          ("Bubble sort works by:",
           ("Splitting the list in half", "Swapping adjacent items that are out of order",
            "Inserting into a new list", "Counting occurrences"), 1),
          ("Which sort uses a divide-and-conquer approach?",
           ("Bubble sort", "Insertion sort", "Merge sort", "Linear sort"), 2),
          ("Bubble sort's worst-case time complexity is described as:",
           ("O(1)", "O(log n)", "O(n)", "O(n squared)"), 3),
          ("Merge sort is generally preferred over bubble sort for large datasets because:",
           ("It always uses less memory", "Its time complexity O(n log n) scales far better than O(n squared)",
            "It never needs to compare values", "It works without a computer"), 1)),
        L(8, "Programming Basics", """
            <p><b>Basic:</b> A variable is a named store whose value can change; a constant cannot. Common data
            types are integer, real/float, Boolean, character and string.</p>
            <p>Choosing the right type saves memory and prevents errors. Programs follow three basic constructs:
            sequence, selection and iteration.</p>
            <p><b>Intermediate:</b> Type mismatches are a classic source of bugs: adding the string "5" to the
            string "3" in many languages gives "53" (joining text) rather than 8 (adding numbers), which is why
            careful type conversion matters when reading user input, which typically arrives as text even when it
            looks numeric.</p>
            <p>Meaningful variable names (<code>studentAverage</code> rather than <code>x</code>) cost nothing at
            runtime but save enormous time when a program is read, debugged or extended months later by someone
            else &mdash; or by the original author, who often forgets their own logic surprisingly fast.</p>
            <p><b>Pre-advanced:</b> Scope determines where a variable can be accessed and how long it exists:
            variables declared inside a function typically vanish once that function finishes, while global
            variables persist for the whole program's run &mdash; overusing global variables makes large programs
            unpredictable, since any part of the code might silently change a value another part relies on.</p>
        """,
          ("A Boolean variable can hold:",
           ("Any whole number", "True or False", "A line of text", "A decimal"), 1),
          ("The three basic programming constructs are:",
           ("Input, output, storage", "Sequence, selection, iteration",
            "Compile, run, debug", "Variables, constants, arrays"), 1),
          ("Adding the text values 5 and 3 as strings typically produces:",
           ("8", "53", "An error every time", "15"), 1),
          ("Overusing global variables in a large program is risky mainly because:",
           ("They use no memory", "Any part of the program can unexpectedly change them",
            "They cannot store numbers", "They only work in loops"), 1)),
        L(9, "Selection and Iteration", """
            <p><b>Basic:</b> Selection chooses a path: <code>if score &gt;= 50: print("Pass")</code>, optionally
            with elif and else branches. A <b>for</b> loop repeats a set number of times; a <b>while</b> loop
            repeats until a condition becomes false.</p>
            <p>A while loop whose condition never becomes false creates an infinite loop.</p>
            <p><b>Intermediate:</b> Nested selection and iteration let simple building blocks solve much richer
            problems: a program checking every student's grade and printing a personalised message uses a for
            loop to visit each student, with an if/elif/else inside to decide what to print for that particular
            student.</p>
            <p>Loop counters and accumulator variables (like a running total that increases each pass through a
            loop) are a common pattern &mdash; and a common bug source when a counter starts at the wrong number
            or updates in the wrong place, causing an "off-by-one" error.</p>
            <p><b>Pre-advanced:</b> Choosing for versus while is a design decision, not just syntax: use a for
            loop whenever the number of repeats is genuinely known in advance (looping through every item in a
            fixed list), and a while loop whenever repetition depends on a condition that can only be checked at
            runtime, such as reading input until the user types "quit".</p>
        """,
          ("Which loop should you use when the number of repetitions is known in advance?",
           ("while loop", "for loop", "if statement", "recursive call"), 1),
          ("An infinite loop happens when:",
           ("The condition never becomes false", "The code has no loop",
            "You use a for loop", "A variable is a string"), 0),
          ("An off-by-one error most commonly arises from:",
           ("A loop counter starting or updating incorrectly", "Using the wrong data type",
            "Forgetting to name a variable", "Using an if statement instead of a loop"), 0),
          ("Reading user input repeatedly until they type quit is best suited to:",
           ("A for loop with a fixed count", "A while loop with a condition checked at runtime",
            "A single if statement", "No loop at all"), 1)),
        L(10, "Functions and Decomposition", """
            <p><b>Basic:</b> Decomposition breaks a large problem into smaller sub-problems, each solved by a
            function. Functions take parameters and usually return a value, so the same code can be reused with
            different inputs.</p>
            <p>Local variables exist only inside a function; global variables are visible throughout the program
            and are best used sparingly.</p>
            <p><b>Intermediate:</b> A function written to calculate a triangle's area, for example, can be reused
            anywhere in a program &mdash; or in a future program &mdash; without rewriting the calculation, which
            is the core productivity gain behind reusable code libraries used by virtually every software
            project.</p>
            <p>Parameters let a function behave differently each time it is called without changing its internal
            code: a single <code>greet(name)</code> function can politely greet any name passed to it.</p>
            <p><b>Pre-advanced:</b> Recursion is a function calling itself to solve a smaller version of the same
            problem, with a "base case" that stops the recursion &mdash; calculating a factorial as
            <code>n! = n &times; (n-1)!</code> down to the base case <code>0! = 1</code> is a classic example, and
            while elegant, recursion without a correct base case causes the same crash as an infinite loop.</p>
        """,
          ("The main benefit of using functions is:",
           ("Programs run without errors", "Code can be reused and is easier to maintain",
            "Less memory is always used", "No variables are needed"), 1),
          ("A local variable can be accessed:",
           ("Anywhere in the program", "Only inside its function", "Only by the OS", "Only once"), 1),
          ("A recursive function must include a base case mainly to:",
           ("Make the code shorter", "Stop the function from calling itself forever",
            "Increase its speed", "Allow it to take parameters"), 1),
          ("Passing different arguments into the same function each time it's called allows it to:",
           ("Change its own source code", "Behave differently without rewriting its internal logic",
            "Run without a return value", "Avoid using parameters"), 1)),
        L(11, "Data Structures", """
            <p><b>Basic:</b> An array or list stores many values under one name, accessed by index starting at 0.
            A record (or dictionary) groups related fields of different types, such as a student's name, age and
            grade.</p>
            <p>A stack is last-in-first-out; a queue is first-in-first-out, used for printer jobs and
            scheduling.</p>
            <p><b>Intermediate:</b> The choice of data structure has real performance consequences: an array gives
            instant access to any element by index, but inserting into the middle means shifting every element
            after it, while a linked list inserts quickly anywhere but must be walked step by step to reach a
            specific position.</p>
            <p>A stack's "undo" behaviour in a text editor is a direct real-world use: the most recent edit is the
            first one undone, exactly matching last-in-first-out order; a printer queue instead processes
            documents in the order they were sent, matching first-in-first-out order.</p>
            <p><b>Pre-advanced:</b> Trees generalise lists into branching structures, and binary search trees keep
            data ordered so that searching, inserting and deleting can all be done in roughly O(log n) time on
            average &mdash; combining the fast lookup of binary search with the flexible insertion a plain sorted
            array cannot offer without expensive shifting.</p>
        """,
          ("A stack operates on which principle?",
           ("First in, first out", "Last in, first out", "Random access", "Sorted order"), 1),
          ("In most languages, the first element of an array has index:",
           ("0", "1", "-1", "It varies randomly"), 0),
          ("An 'undo' feature in a text editor typically behaves like a:",
           ("Queue", "Stack", "Array only", "Record"), 1),
          ("A key advantage of a binary search tree over a plain sorted array is:",
           ("It uses no memory", "Insertion and deletion are typically faster on average without full shifting",
            "It cannot be searched", "It stores only numbers"), 1)),
        L(12, "Databases and SQL", """
            <p><b>Basic:</b> A relational database stores data in tables of records and fields, linked by keys. A
            primary key uniquely identifies each record; a foreign key refers to a primary key in another table,
            avoiding duplicated data.</p>
            <p>SQL queries the data, e.g. <code>SELECT name FROM students WHERE grade &gt; 70;</code></p>
            <p><b>Intermediate:</b> Splitting data across linked tables (normalisation) avoids storing the same
            information twice: rather than repeating a customer's full address on every single order they place,
            an orders table stores only a customer ID that links back to one customer table &mdash; so updating an
            address once updates it everywhere it matters.</p>
            <p>JOIN clauses combine data from multiple tables in a single query, which is how a report can list
            "customer name" and "order total" together even though those facts live in two entirely separate
            tables.</p>
            <p><b>Pre-advanced:</b> Without careful design, databases risk anomalies: deleting the only order from
            a customer accidentally losing all record that the customer ever existed (a deletion anomaly), or
            updating a repeated piece of data in one row but not another, creating silent inconsistency &mdash;
            exactly the problems normalisation is designed to prevent.</p>
        """,
          ("A primary key is used to:",
           ("Encrypt the table", "Uniquely identify each record",
            "Sort the database", "Link to the internet"), 1),
          ("Which SQL keyword filters which rows are returned?",
           ("SELECT", "FROM", "WHERE", "ORDER"), 2),
          ("Storing a customer's address only once in a customer table, linked by ID from an orders table, is an example of:",
           ("Encryption", "Normalisation", "A foreign key violation", "Compression"), 1),
          ("A SQL JOIN is primarily used to:",
           ("Delete rows from a table", "Combine related data from multiple tables in one query",
            "Encrypt sensitive fields", "Create a new database"), 1)),
        L(13, "Networks and the Internet", """
            <p><b>Basic:</b> A LAN covers a small area such as a school; a WAN, like the internet, spans large
            distances. Devices follow protocols: TCP/IP for transferring data, HTTP/HTTPS for web pages.</p>
            <p>Data is split into packets that travel independently and are reassembled at the destination; DNS
            translates domain names into IP addresses.</p>
            <p><b>Intermediate:</b> Splitting data into packets means a single web page's data might travel
            across several different physical routes simultaneously and arrive out of order, with TCP responsible
            for reordering and re-requesting any lost packets before handing a complete, correct file to the
            browser &mdash; robustness the earliest circuit-switched phone networks never needed to solve.</p>
            <p>HTTPS adds encryption (via TLS) on top of ordinary HTTP, so that data intercepted in transit &mdash;
            such as a password on public café Wi-Fi &mdash; is unreadable without the correct decryption key.</p>
            <p><b>Pre-advanced:</b> The internet's layered protocol design (application, transport, internet, link)
            means each layer only needs to solve one job and can be swapped independently &mdash; Wi-Fi can replace
            Ethernet at the link layer without the application layer (a web browser) ever needing to know or
            care, which is exactly why the same websites work identically whether you connect by cable or Wi-Fi.</p>
        """,
          ("Data sent across the internet is broken into:",
           ("Files", "Packets", "Pixels", "Bytes only"), 1),
          ("DNS is responsible for:",
           ("Encrypting data", "Converting domain names into IP addresses",
            "Storing web pages", "Blocking viruses"), 1),
          ("HTTPS improves on plain HTTP mainly by adding:",
           ("Faster loading speed only", "Encryption so intercepted data cannot easily be read",
            "More colourful web pages", "Unlimited bandwidth"), 1),
          ("Because internet protocols are layered, Wi-Fi can replace a cabled connection without:",
           ("Changing how websites behave at all for the user", "Any packets being sent",
            "DNS being needed", "TCP being needed"), 0)),
        L(14, "Cybersecurity", """
            <p><b>Basic:</b> Threats include malware, phishing emails, brute-force attacks and social engineering
            that targets people rather than systems. Defences include strong unique passwords, two-factor
            authentication, firewalls, software updates and regular backups.</p>
            <p>Encryption scrambles data so that intercepting it is useless without the key.</p>
            <p><b>Intermediate:</b> Two-factor authentication defeats most password theft because a stolen
            password alone is no longer enough &mdash; the attacker also needs a second factor, typically a code
            sent to a device only the real owner holds, drastically reducing the value of a leaked password
            database to criminals.</p>
            <p>Regular software updates matter because many attacks exploit already-known vulnerabilities that a
            patch has already fixed; delaying updates effectively leaves a door unlocked that the manufacturer has
            already told the world how to close.</p>
            <p><b>Pre-advanced:</b> Ransomware encrypts a victim's own files and demands payment for the
            decryption key, which is precisely why offline or immutable backups (not just backups permanently
            connected to the same network) are considered essential: a backup drive that is always plugged in and
            reachable can itself be encrypted by the same attack, defeating its entire purpose.</p>
        """,
          ("Phishing is an attack that mainly targets:",
           ("Network cables", "People, by tricking them into revealing information",
            "Hard drives", "Printers"), 1),
          ("Encryption protects data by:",
           ("Deleting it", "Making it unreadable without the key",
            "Compressing it", "Backing it up"), 1),
          ("Two-factor authentication significantly improves security mainly because:",
           ("It removes the need for passwords entirely", "A stolen password alone is no longer enough to log in",
            "It encrypts all internet traffic", "It blocks all malware automatically"), 1),
          ("Ransomware is particularly dangerous to backups that are:",
           ("Kept completely offline", "Always connected and reachable from the infected network",
            "Stored on paper", "Encrypted separately"), 1)),
        L(15, "Efficiency and Big-O", """
            <p><b>Basic:</b> Two correct algorithms can differ hugely in speed, so we compare how work grows with
            input size n. Big-O notation captures this: O(1) is constant, O(log n) very efficient (binary search),
            O(n) linear, and O(n&sup2;) slow for large n (bubble sort).</p>
            <p>There is often a trade-off between time taken and memory used.</p>
            <p><b>Intermediate:</b> Big-O describes worst-case growth trends, not exact runtimes: an O(n) algorithm
            is not automatically faster than an O(n&sup2;) one for every possible n, but as n grows large enough,
            the O(n) algorithm always eventually wins &mdash; which is exactly why Big-O matters most for choosing
            algorithms that will handle genuinely large, real-world datasets.</p>
            <p>Space complexity uses the same notation to describe memory use rather than time: a solution that
            trades extra memory (like a lookup table computed once) for much faster repeated lookups is a
            deliberate and common time-space trade-off, not a flaw.</p>
            <p><b>Pre-advanced:</b> Some problems are provably intractable at large scale &mdash; certain
            algorithms have exponential complexity O(2&#8319;), where each extra input item doubles the work
            required, meaning even a modest increase in input size can push runtime from seconds to longer than
            the age of the universe, which is precisely why algorithm design, not just faster hardware, is central
            to solving large real-world problems.</p>
        """,
          ("Binary search has a time complexity of:",
           ("O(1)", "O(log n)", "O(n)", "O(n squared)"), 1),
          ("An O(n squared) algorithm becomes a problem when:",
           ("The input is tiny", "The input grows large", "Memory is cheap", "The data is sorted"), 1),
          ("Big-O notation is most useful for describing:",
           ("The exact runtime in seconds", "How an algorithm's workload grows as input size increases",
            "The programming language used", "The colour of the output"), 1),
          ("An algorithm with O(2 to the power n) complexity is considered problematic mainly because:",
           ("It uses no memory at all", "Runtime can explode dramatically with only modest increases in input size",
            "It only works on sorted data", "It cannot be written in most languages"), 1)),
        L(16, "Artificial Intelligence Basics", """
            <p><b>Basic:</b> Artificial intelligence broadly means getting computers to perform tasks that would
            normally need human intelligence, such as recognising images, understanding language or playing
            games.</p>
            <p><b>Machine learning</b> is a major approach to AI where, instead of a programmer writing exact
            rules, a system learns patterns from example data &mdash; like teaching a program to recognise cats by
            showing it thousands of labelled photos rather than describing "whiskers" and "pointy ears" in code.</p>
            <p><b>Intermediate:</b> Supervised learning trains on labelled examples (photos already tagged "cat"
            or "not cat") to predict labels for new, unseen data; unsupervised learning instead looks for hidden
            structure in unlabelled data, such as automatically grouping customers with similar shopping habits
            without ever being told what the groups should be.</p>
            <p>A neural network is loosely inspired by connected brain cells: layers of simple mathematical units
            pass signals forward, each connection carrying an adjustable "weight" that training gradually tunes
            so the network's output better matches the correct answer.</p>
            <p><b>Pre-advanced:</b> A model trained too closely to its exact training examples can "overfit",
            performing brilliantly on data it has already seen but poorly on new data &mdash; much like a student
            who memorises past exam answers word-for-word rather than understanding the underlying method, and
            then struggles the moment the questions are phrased differently.</p>
        """,
          ("Machine learning differs from traditional programming mainly because it:",
           ("Requires no computer at all", "Learns patterns from example data rather than following fixed hard-coded rules",
            "Only works with images", "Always runs faster"), 1),
          ("Training a model on data that is already labelled with the correct answer is called:",
           ("Unsupervised learning", "Supervised learning", "Overfitting", "Encryption"), 1),
          ("A model that performs very well on training data but poorly on new, unseen data is said to be:",
           ("Underfitting", "Overfitting", "Compressed", "Encrypted"), 1),
          ("Grouping customers by similar shopping habits without being told the groups in advance is an example of:",
           ("Supervised learning", "Unsupervised learning", "Binary search", "Encryption"), 1)),
    ],
}
