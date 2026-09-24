QUIZ_LENGTH = 2


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


SUBJECTS = {
    "maths": {
        "name": "Mathematics",
        "lessons": [
            L(1, "Introduction to Algebra", """
                <p>Algebra uses letters such as <b>x</b> and <b>y</b> to stand in for unknown or
                variable numbers, so that one general rule can describe many different situations at
                once instead of writing out every case by hand.</p>
                <p>An equation like <code>x + 5 = 12</code> asks: what number, added to 5, gives 12?
                Subtracting 5 from both sides leaves <code>x = 7</code>. Multi-step equations combine
                several operations, e.g. <code>2(x + 3) = 16</code>: divide both sides by 2 to get
                <code>x + 3 = 8</code>, then subtract 3 to get <code>x = 5</code>.</p>
                <p>The golden rule: whatever you do to one side of an equation you must do to the
                other, so the two sides stay balanced &mdash; like keeping a set of scales level.</p>
                <p>An <b>inequality</b> such as <code>x + 5 &gt; 12</code> is solved the same way but
                gives a range of answers (<code>x &gt; 7</code>) rather than a single value. Dividing
                or multiplying both sides by a negative number flips the inequality sign.</p>
                <p>Always check a solution by substituting it back into the original equation &mdash;
                if both sides don't match, an arithmetic slip has crept in somewhere.</p>
            """,
              ("Solve: 2(x + 3) = 16.", ("5", "6", "7", "8"), 0),
              ("Solve: x/3 - 2 = 5.", ("18", "21", "24", "15"), 1)),
            L(2, "Linear Equations", """
                <p>A linear equation has variables raised only to the power 1, e.g. <code>3x - 4 = 11</code>.
                Solve it by undoing operations in reverse order: add 4, then divide by 3, giving <code>x = 5</code>.</p>
                <p>When the unknown appears on both sides, gather the x terms on one side first:
                <code>5x - 2 = 3x + 8</code> becomes <code>2x = 10</code>, so <code>x = 5</code>.</p>
                <p>Equations with brackets or fractions need an extra step before the usual undoing
                process: expand any brackets first, and clear fractions by multiplying every term by
                the denominator, e.g. <code>(x + 1)/2 = 5</code> becomes <code>x + 1 = 10</code>.</p>
                <p>Linear equations can also model real situations: "I think of a number, double it and
                add 7 to get 19" translates to <code>2x + 7 = 19</code>, giving <code>x = 6</code>.
                Turning words into equations correctly is often the hardest part.</p>
                <p>Always check by substituting your answer back into the original equation.</p>
            """,
              ("Solve: 4x + 7 = 2x + 19.", ("4", "5", "6", "7"), 2),
              ("Solve: (x + 1)/2 = 5.", ("8", "9", "10", "11"), 1)),
            L(3, "Expanding and Factorising", """
                <p>Expanding removes brackets: <code>3(x + 4) = 3x + 12</code>. Every term inside the
                bracket is multiplied by the term outside.</p>
                <p>For two brackets, multiply each term in the first by each term in the second (often
                remembered as FOIL &mdash; First, Outer, Inner, Last):
                <code>(x + 2)(x + 3) = x&sup2; + 5x + 6</code>. With negative or larger coefficients the
                same method still applies, e.g. <code>(2x - 1)(x + 4) = 2x&sup2; + 7x - 4</code>.</p>
                <p>Factorising is the reverse: rewrite an expression as a product. For
                <code>x&sup2; + 5x + 6</code> look for two numbers that multiply to 6 and add to 5 &mdash; 2 and 3.</p>
                <p>A special and very common case is the <b>difference of two squares</b>:
                <code>a&sup2; - b&sup2; = (a - b)(a + b)</code>, so <code>x&sup2; - 9</code> factorises
                instantly to <code>(x - 3)(x + 3)</code> with no middle term to search for.</p>
                <p>Factorising is useful beyond neatness: it is the key step for solving quadratic
                equations and for simplifying algebraic fractions.</p>
            """,
              ("Expand (2x - 1)(x + 4).",
               ("2x&sup2; + 7x - 4", "2x&sup2; + 8x - 4", "2x&sup2; - 7x - 4", "3x&sup2; + 7x - 4"), 0),
              ("Factorise x&sup2; - 9.",
               ("(x - 3)(x + 3)", "(x - 9)(x + 1)", "(x + 3)&sup2;", "(x - 3)&sup2;"), 0)),
            L(4, "Quadratic Equations", """
                <p>A quadratic has the form <code>ax&sup2; + bx + c = 0</code> and can have two, one, or no
                real solutions.</p>
                <p>If it factorises, use the fact that a product is zero only when a factor is zero:
                <code>(x - 2)(x - 3) = 0</code> gives <code>x = 2</code> or <code>x = 3</code>.</p>
                <p>Otherwise use the formula <code>x = (-b &plusmn; &radic;(b&sup2; - 4ac)) / 2a</code>.
                The part <code>b&sup2; - 4ac</code> is the discriminant: negative means no real roots,
                zero means one repeated root, and positive means two distinct real roots.</p>
                <p>Completing the square, <code>a(x + p)&sup2; + q</code>, is a third method that also
                reveals the turning point of the graph directly, which is useful when a question asks
                for the minimum or maximum value rather than just the roots.</p>
                <p>The graph of a quadratic is always a symmetrical curve called a <b>parabola</b>; its
                roots are where the curve crosses the x-axis, which is exactly what solving the
                equation finds.</p>
            """,
              ("Solve x&sup2; - 5x + 6 = 0.",
               ("x = 1 and x = 6", "x = 2 and x = 3", "x = -2 and x = -3", "x = 6 only"), 1),
              ("For 2x&sup2; + 3x - 5 = 0, the discriminant b&sup2; - 4ac equals:",
               ("49", "-31", "9", "29"), 0)),
            L(5, "Angles and Shapes", """
                <p>Angles on a straight line add to 180&deg;, and angles around a point add to 360&deg;.</p>
                <p>A triangle's three interior angles always total <b>180&deg;</b>; a quadrilateral's total 360&deg;.
                A square has four equal sides and four 90&deg; angles.</p>
                <p>Perimeter is the total distance around a shape; area is the space it covers.</p>
                <p>For any polygon with n sides, the interior angles sum to <code>(n - 2) &times; 180&deg;</code>,
                so a hexagon's six interior angles total 720&deg;. Exterior angles of any convex polygon
                always add up to exactly 360&deg;, regardless of how many sides it has.</p>
                <p>These angle facts combine in multi-step problems: if one angle of a triangle is 90&deg;
                and a second is described in terms of the third, the 180&deg; total lets you set up and
                solve an equation to find them.</p>
            """,
              ("The sum of the interior angles of a hexagon is:",
               ("540 degrees", "600 degrees", "720 degrees", "900 degrees"), 2),
              ("A triangle has one angle of 90&deg; and another of x&deg;. If the third angle is 2x&deg;, what is x?",
               ("20", "30", "40", "45"), 1)),
            L(6, "Triangles and Pythagoras", """
                <p>In a right-angled triangle the longest side, opposite the right angle, is the
                <b>hypotenuse</b>.</p>
                <p>Pythagoras' theorem states <code>a&sup2; + b&sup2; = c&sup2;</code>, where c is the hypotenuse.
                With sides 3 and 4, the hypotenuse is &radic;25 = 5.</p>
                <p>The theorem works only for right-angled triangles, and can also be used backwards to
                test whether a triangle contains a right angle: if the two shorter sides squared and
                added exactly equal the longest side squared, the triangle must be right-angled.</p>
                <p>It also rearranges to find a shorter side when the hypotenuse is known:
                <code>a = &radic;(c&sup2; - b&sup2;)</code>. This is exactly the situation in problems
                like a ladder leaning against a wall, where the ladder is the hypotenuse.</p>
                <p>Pythagorean triples &mdash; whole-number solutions such as (3, 4, 5), (5, 12, 13) and
                (8, 15, 17) &mdash; are worth recognising, since they often appear directly in questions.</p>
            """,
              ("A ladder 13 m long leans against a wall with its foot 5 m from the wall. How high up the wall does it reach?",
               ("10 m", "11 m", "12 m", "13 m"), 2),
              ("A triangle has sides 5, 12 and 13. Is it right-angled, and if so, which side is the hypotenuse?",
               ("Yes, 13 is the hypotenuse", "Yes, 12 is the hypotenuse", "No, it is not right-angled", "Yes, 5 is the hypotenuse"), 0)),
            L(7, "Circles", """
                <p>The radius runs from the centre to the edge; the diameter is twice the radius.</p>
                <p>Circumference = <code>2&pi;r</code> and area = <code>&pi;r&sup2;</code>, where &pi; &asymp; 3.14.</p>
                <p>So a circle of radius 5 cm has circumference about 31.4 cm and area about 78.5 cm&sup2;.</p>
                <p>These formulas also work in reverse: if you are given the area or circumference, you
                can rearrange to find the radius, e.g. <code>r = &radic;(Area / &pi;)</code>.</p>
                <p>A <b>sector</b> is a "slice" of a circle between two radii; its area is a fraction of
                the whole circle's area, found using <code>(angle / 360&deg;) &times; &pi;r&sup2;</code>,
                and an <b>arc</b> is the curved edge of that slice.</p>
            """,
              ("A circle has area 154 cm&sup2; (use &pi; &asymp; 22/7). Its radius is approximately:",
               ("5 cm", "6 cm", "7 cm", "8 cm"), 2),
              ("A circle has circumference 44 cm (&pi; &asymp; 22/7). Its diameter is:",
               ("7 cm", "14 cm", "21 cm", "28 cm"), 1)),
            L(8, "Fractions, Decimals and Percentages", """
                <p>These are three ways of writing the same idea: 1/4 = 0.25 = 25%.</p>
                <p>To find a percentage of an amount, convert to a decimal and multiply:
                15% of 80 is 0.15 &times; 80 = 12.</p>
                <p>For a percentage increase, multiply by (1 + rate). A 20% rise on 50 gives
                50 &times; 1.2 = 60.</p>
                <p>Working backwards from a final amount to an original value is a common trap: if a
                price after a 20% increase is &pound;72, you must divide by 1.2 (not subtract 20%) to
                recover the original &pound;60.</p>
                <p>Successive percentage changes do not simply add up: decreasing by 10% and then
                increasing by 10% does <i>not</i> return to the original value, because the second
                change is applied to a smaller starting amount (0.9 &times; 1.1 = 0.99, a 1% net fall).</p>
            """,
              ("A price is increased by 20% to &pound;72. What was the original price?",
               ("&pound;54", "&pound;57.60", "&pound;60", "&pound;62"), 2),
              ("A quantity decreases by 10% and then increases by 10%. Compared with the original, it is:",
               ("Unchanged", "1% less", "1% more", "10% less"), 1)),
            L(9, "Ratio and Proportion", """
                <p>A ratio compares quantities, e.g. 2:3. To share &pound;50 in the ratio 2:3, note there are
                5 parts, so each part is &pound;10, giving &pound;20 and &pound;30.</p>
                <p>Two quantities are in direct proportion when doubling one doubles the other.</p>
                <p>In inverse proportion their product stays constant: as one doubles, the other halves.</p>
                <p>Ratios also scale recipes and mixtures: if flour and sugar are used in ratio 5:2, the
                same ratio must be kept however much is made &mdash; find the multiplier from one known
                quantity, then apply it to the other.</p>
                <p>For inverse proportion problems, first find the constant of proportionality
                <code>k</code> from the given pair of values using <code>y = k/x</code>, then use it to
                find any other missing value.</p>
            """,
              ("A recipe uses flour and sugar in the ratio 5:2. If 250 g of sugar is used, how much flour is needed?",
               ("500 g", "600 g", "625 g", "700 g"), 2),
              ("y is inversely proportional to x. When x = 4, y = 15. What is y when x = 10?",
               ("4", "6", "24", "37.5"), 1)),
            L(10, "Indices and Standard Form", """
                <p>Indices show repeated multiplication: <code>2&sup5; = 32</code>. Rules:
                <code>a&#8319; &times; a&#7504; = a&#8319;&#8314;&#7504;</code> and <code>a&#8319; &divide; a&#7504; = a&#8319;&#8315;&#7504;</code>.</p>
                <p>Anything to the power 0 equals 1, and a negative index means a reciprocal:
                <code>2&#8315;&sup3; = 1/8</code>.</p>
                <p>Standard form writes numbers as <code>A &times; 10&#8319;</code> with 1 &le; A &lt; 10, so
                4500 becomes <code>4.5 &times; 10&sup3;</code>.</p>
                <p>A power raised to another power multiplies the indices: <code>(a&#8319;)&#7504; = a&#8319;&#7504;</code>,
                so <code>(2x&sup3;)&sup2; = 4x&#8310;</code> &mdash; remember to square the numerical
                coefficient too, not just the index.</p>
                <p>When multiplying or dividing numbers in standard form, combine the two "A" parts and
                add or subtract the powers of 10 separately, then adjust back into standard form if the
                result falls outside the 1 &le; A &lt; 10 range.</p>
            """,
              ("Simplify (2x&sup3;)&sup2;.", ("2x&#8310;", "4x&#8309;", "4x&#8310;", "2x&#8309;"), 2),
              ("Calculate (3 &times; 10&#8308;) &times; (2 &times; 10&#8315;&sup2;), giving the answer in standard form.",
               ("6 &times; 10&sup2;", "6 &times; 10&#8310;", "6 &times; 10&#8315;&#8312;", "6 &times; 10&sup3;"), 0)),
            L(11, "Coordinates and Straight Line Graphs", """
                <p>Points are written as (x, y), measured from the origin (0, 0).</p>
                <p>A straight line has equation <code>y = mx + c</code>, where m is the gradient
                (steepness) and c is the y-intercept.</p>
                <p>Gradient = change in y divided by change in x. Parallel lines share the same gradient.</p>
                <p>Given any two points on a line, the gradient can be calculated directly:
                <code>m = (y&#8322; - y&#8321;) / (x&#8322; - x&#8321;)</code>. Once the gradient and one
                point are known, substituting into <code>y = mx + c</code> finds the missing
                y-intercept, which then gives the full equation of the line.</p>
                <p>Lines that are <b>perpendicular</b> to each other have gradients that multiply to
                give -1; for example a line with gradient 2 is perpendicular to one with gradient -&frac12;.</p>
            """,
              ("Find the gradient of the line joining (1, 2) and (5, 10).",
               ("1", "2", "3", "4"), 1),
              ("A line has gradient 2 and passes through (3, 7). Its equation is:",
               ("y = 2x + 1", "y = 2x + 4", "y = 2x - 1", "y = 2x + 7"), 0)),
            L(12, "Sequences", """
                <p>A sequence is an ordered list of terms. In an <b>arithmetic</b> sequence you add a
                constant difference each time: 3, 7, 11, 15 (difference 4).</p>
                <p>The nth term of that sequence is <code>4n - 1</code>, which lets you jump straight to
                any term.</p>
                <p>In a <b>geometric</b> sequence you multiply by a constant ratio: 2, 6, 18, 54.</p>
                <p>Not all sequences are linear: a quadratic sequence has an nth term containing
                <code>n&sup2;</code>, such as <code>2n&sup2; + 1</code>, and its term-to-term
                differences themselves form an arithmetic sequence &mdash; a useful check when finding
                the rule from a list of numbers.</p>
                <p>For a geometric sequence with first term a and common ratio r, the nth term is
                <code>ar&#8319;&#8315;&sup1;</code>, letting you find distant terms without listing every
                one in between.</p>
            """,
              ("The nth term of a sequence is 2n&sup2; + 1. What is the 4th term?",
               ("17", "33", "9", "32"), 1),
              ("A geometric sequence starts 5, 15, 45, ... What is the 5th term?",
               ("135", "225", "405", "675"), 2)),
            L(13, "Averages and Data", """
                <p>The <b>mean</b> is the total divided by how many values there are; the <b>median</b>
                is the middle value when ordered; the <b>mode</b> is the most common value.</p>
                <p>The range (largest minus smallest) measures spread, not average.</p>
                <p>For 2, 3, 3, 8 the mean is 4, the median 3, the mode 3 and the range 6.</p>
                <p>The mean is pulled about strongly by extreme values (outliers), while the median is
                far more resistant to them, since it only depends on which value sits in the middle
                position once the data is ordered.</p>
                <p>These ideas combine in "missing value" problems: if you know the mean of a data set
                and all but one value, the total (mean &times; number of values) lets you calculate the
                missing figure by subtraction.</p>
            """,
              ("A set of 5 numbers has a mean of 12. Four of them are 10, 11, 13 and 14. What is the fifth?",
               ("10", "11", "12", "14"), 2),
              ("For the data 4, 4, 5, 7, 8, 20 the mean is:",
               ("6", "7", "8", "9"), 2)),
            L(14, "Introduction to Trigonometry", """
                <p>In a right-angled triangle, the ratios of sides depend only on the angles:
                <code>sin&theta; = opp/hyp</code>, <code>cos&theta; = adj/hyp</code>,
                <code>tan&theta; = opp/adj</code> (remember SOH CAH TOA).</p>
                <p>Use them to find a missing side when you know an angle and one side.</p>
                <p>To find a missing angle, use the inverse functions, e.g. <code>&theta; = tan&#8315;&sup1;(opp/adj)</code>.</p>
                <p>Choosing the correct ratio starts with labelling the triangle correctly relative to
                the angle being used: the side opposite the angle, the side adjacent to it, and the
                hypotenuse opposite the right angle. Picking the wrong pair of sides is the most common
                mistake.</p>
                <p>These ratios also rearrange to find the hypotenuse or another side, e.g. from
                <code>cos&theta; = adj/hyp</code>, <code>hyp = adj / cos&theta;</code>, which is exactly
                the situation for a ladder leaning at a known angle against a wall.</p>
            """,
              ("A ladder leans against a wall, making 60&deg; with the ground, with its foot 4 m from the wall. How long is the ladder (cos 60&deg; = 0.5)?",
               ("4 m", "6 m", "8 m", "9.2 m"), 2),
              ("In a right triangle, the opposite side is 7 and the hypotenuse is 25. The angle &theta; is closest to:",
               ("16&deg;", "28&deg;", "35&deg;", "74&deg;"), 0)),
            L(15, "Introduction to Calculus", """
                <p>Calculus studies change. <b>Differentiation</b> finds the gradient of a curve at a
                point &mdash; the instantaneous rate of change.</p>
                <p>The rule for powers: if <code>y = x&#8319;</code> then <code>dy/dx = nx&#8319;&#8315;&sup1;</code>.
                So for <code>y = x&sup3;</code>, <code>dy/dx = 3x&sup2;</code>.</p>
                <p>Where the gradient is zero the curve has a turning point &mdash; a maximum or minimum.</p>
                <p>Each term of a longer expression is differentiated separately using the same power
                rule, and any constant term disappears entirely, since a constant does not change the
                gradient: for <code>y = 4x&sup3; - 2x</code>, <code>dy/dx = 12x&sup2; - 2</code>.</p>
                <p>To find a turning point, set the derivative equal to zero and solve for x; this gives
                the x-coordinate where the curve momentarily stops rising or falling before changing
                direction.</p>
            """,
              ("If y = 4x&sup3; - 2x, find dy/dx.",
               ("12x&sup2; - 2", "4x&sup2; - 2", "12x - 2", "12x&sup2;"), 0),
              ("Find the x-coordinate of the turning point of y = x&sup2; - 6x + 5.",
               ("2", "3", "5", "6"), 1)),

        L(16, "Sets, Relations and Functions", """
            <p>A <b>set</b> is a collection of distinct objects, and notation such as <code>A &cup; B</code> means every element in either set while <code>A &cap; B</code> means elements common to both. The complement of a set contains elements in the chosen universal set that are not in it.</p>
            <p>A <b>relation</b> pairs elements from one set with elements of another. A <b>function</b> is a special relation in which every input has exactly one output. The input set is the domain and the possible outputs form the codomain.</p>
            <p>Function composition combines rules: <code>(f &compfn; g)(x) = f(g(x))</code>. For example, if <code>g(x)=2x+1</code> and <code>f(x)=x&sup2;</code>, then <code>f(g(x))=(2x+1)&sup2;</code>.</p>
            <p>When a function is one-to-one on its domain, an inverse can be defined. The inverse reverses the mapping, so <code>f<sup>&minus;1</sup>(f(x))=x</code> for valid inputs.</p>
        """,
          ("Let A = {1,2,3,4} and B = {3,4,5,6}. How many elements are in A &cup; B?", ("4", "5", "6", "8"), 2),
          ("If f(x)=3x-2 and g(x)=x&sup2;+1, what is (g &compfn; f)(2)?", ("10", "17", "25", "37"), 1)),
        L(17, "Polynomials and Remainder Theorem", """
            <p>A polynomial is an expression such as <code>2x&sup3;-5x&sup2;+x-7</code>, where powers of x are non-negative integers. Its degree is the highest power with a non-zero coefficient.</p>
            <p>Polynomial division extends ordinary long division. If a polynomial <code>P(x)</code> is divided by <code>x-a</code>, the remainder is <code>P(a)</code>; this is the <b>remainder theorem</b>.</p>
            <p>The factor theorem follows immediately: <code>x-a</code> is a factor of <code>P(x)</code> exactly when <code>P(a)=0</code>. This gives a systematic way to test possible roots and factor higher-degree polynomials.</p>
            <p>For example, if a cubic has a known root, division by the corresponding linear factor reduces the problem to a quadratic, which can then be solved using factorisation or the quadratic formula.</p>
        """,
          ("For P(x)=2x&sup3;-3x&sup2;-11x+6, what is the remainder when P(x) is divided by x-2?", ("0", "2", "6", "12"), 0),
          ("If P(3)=0, which statement must be true?", ("x+3 is a factor", "x-3 is a factor", "3x is a factor", "P has no other roots"), 1)),
        L(18, "Sequences and Series", """
            <p>An arithmetic sequence changes by a constant difference <code>d</code>, giving <code>a<sub>n</sub>=a<sub>1</sub>+(n-1)d</code>. A geometric sequence multiplies by a constant ratio <code>r</code>, giving <code>a<sub>n</sub>=a<sub>1</sub>r<sup>n-1</sup></code>.</p>
            <p>The sum of the first n arithmetic terms is <code>S<sub>n</sub>=n/2[2a<sub>1</sub>+(n-1)d]</code>. For a finite geometric series, <code>S<sub>n</sub>=a<sub>1>(r<sup>n</sup>-1)/(r-1)</code> when <code>r &ne; 1</code>.</p>
            <p>An infinite geometric series converges only when <code>|r|&lt;1</code>, in which case <code>S=a<sub>1</sub>/(1-r)</code>. If <code>|r|&ge;1</code>, the terms do not approach zero and the infinite sum does not converge.</p>
            <p>Sequences can model repeated growth, depreciation, compound processes and recursive algorithms, making the distinction between additive and multiplicative change practically important.</p>
        """,
          ("An arithmetic sequence has a<sub>5</sub>=17 and a<sub>12</sub>=45. What is its first term?", ("1", "3", "5", "7"), 1),
          ("For the infinite series 12+6+3+1.5+..., what is its sum?", ("18", "20", "24", "30"), 2)),
        L(19, "Coordinate Geometry and Circles", """
            <p>The distance between <code>(x<sub>1</sub>,y<sub>1</sub>)</code> and <code>(x<sub>2</sub>,y<sub>2</sub>)</code> is <code>&radic;[(x<sub>2</sub>-x<sub>1</sub>)&sup2;+(y<sub>2</sub>-y<sub>1</sub>)&sup2;]</code>. The midpoint is obtained by averaging the two x-coordinates and the two y-coordinates.</p>
            <p>A circle with centre <code>(h,k)</code> and radius r has equation <code>(x-h)&sup2;+(y-k)&sup2;=r&sup2;</code>. Expanding it gives a general quadratic form in x and y.</p>
            <p>The gradient of a line perpendicular to another non-vertical line is the negative reciprocal of its gradient. This lets coordinate geometry convert geometric perpendicularity into an algebraic condition.</p>
            <p>Intersection problems combine equations. Substituting a line into a circle can produce a quadratic whose discriminant indicates whether the line misses the circle, touches it once, or cuts it twice.</p>
        """,
          ("What is the distance between (-2,3) and (4,-5)?", ("8", "10", "12", "14"), 1),
          ("For the circle (x-2)&sup2;+(y+1)&sup2;=25, which point lies on the circle?", ("(2,3)", "(5,3)", "(7,-1)", "(0,1)"), 0)),
        L(20, "Vectors", """
            <p>A vector has both magnitude and direction, unlike a scalar, which has magnitude only. In two dimensions a vector can be represented by components such as <code>(3,4)</code>.</p>
            <p>Vectors add component-by-component and a scalar multiple changes the magnitude and possibly reverses the direction. The magnitude of <code>(a,b)</code> is <code>&radic;(a&sup2;+b&sup2;)</code>.</p>
            <p>The <b>dot product</b> of <code>a=(a<sub>1</sub>,a<sub>2</sub>)</code> and <code>b=(b<sub>1</sub>,b<sub>2</sub>)</code> is <code>a&middot;b=a<sub>1</sub>b<sub>1</sub>+a<sub>2</sub>b<sub>2</sub></code>. If the dot product is zero, the vectors are perpendicular.</p>
            <p>Vectors provide a compact language for displacement, velocity, force and navigation because direction and magnitude can be manipulated independently and then recombined.</p>
        """,
          ("If a=(3,4) and b=(-2,5), what is a&middot;b?", ("10", "14", "20", "26"), 1),
          ("A vector has components (5,12). Its magnitude is:", ("11", "12", "13", "17"), 2)),
        L(21, "Permutations and Combinations", """
            <p>Counting methods avoid listing every possibility. A permutation counts arrangements where order matters, while a combination counts selections where order does not matter.</p>
            <p>The number of ways to arrange n distinct objects is <code>n!</code>. Choosing r objects from n without regard to order gives <code>C(n,r)=n!/[r!(n-r)!]</code>.</p>
            <p>For example, selecting a president and secretary from a group is an ordered choice because the roles differ. Selecting two committee members is an unordered choice.</p>
            <p>These ideas form the basis of probability calculations when outcomes are equally likely and are especially useful for counting possible passwords, schedules, teams and experimental outcomes.</p>
        """,
          ("How many distinct 4-letter arrangements can be formed from A, B, C, D, E without repetition?", ("20", "60", "100", "120"), 1),
          ("A committee of 3 is chosen from 8 students. How many different committees are possible?", ("24", "48", "56", "336"), 2)),
        L(22, "Probability and Conditional Probability", """
            <p>For equally likely outcomes, probability is <code>P(A)=number of favourable outcomes/total outcomes</code>. Complementary events satisfy <code>P(A<sup>c</sup>)=1-P(A)</code>.</p>
            <p>For two events, <code>P(A &cap; B)=P(A)P(B|A)</code>. Conditional probability changes the sample space after information about another event is known.</p>
            <p>Two events are independent when knowing that one occurred does not change the probability of the other, so <code>P(A &cap; B)=P(A)P(B)</code>.</p>
            <p>Careful probability reasoning prevents the common error of treating dependent draws as independent. Sampling without replacement changes later probabilities because the composition of the population has changed.</p>
        """,
          ("A bag contains 5 red and 3 blue balls. Two are drawn without replacement. What is the probability both are red?", ("5/16", "5/14", "25/64", "1/2"), 0),
          ("If P(A)=0.6, P(B|A)=0.5 and P(B)=0.4, what is P(A &cap; B)?", ("0.2", "0.24", "0.30", "0.50"), 2)),
        L(23, "Statistics and Standard Deviation", """
            <p>The mean uses every value but can be strongly affected by extreme observations. The median is the middle ordered value and is often more resistant to outliers.</p>
            <p>Variance measures the average squared distance from the mean, while standard deviation is its square root and therefore has the same units as the original data.</p>
            <p>A dataset with values tightly clustered around the mean has a smaller standard deviation than a dataset spread widely around the same mean.</p>
            <p>When comparing data, always consider the centre and spread together. Two groups can have the same mean but very different variability, which can change the interpretation of reliability or consistency.</p>
        """,
          ("For the data 2,4,4,6,9, what is the mean?", ("4", "5", "6", "7"), 1),
          ("If every value in a dataset is multiplied by 3, the standard deviation is multiplied by:", ("1/3", "1", "3", "9"), 2)),
        L(24, "Logarithms and Exponentials", """
            <p>A logarithm reverses exponentiation: <code>log<sub>b</sub>(x)=y</code> means <code>b<sup>y</sup>=x</code>. Logarithms are defined for positive arguments when working over the real numbers.</p>
            <p>Important laws include <code>log(ab)=log a+log b</code>, <code>log(a/b)=log a-log b</code>, and <code>log(a<sup>k</sup>)=k log a</code>. These convert multiplication into addition and powers into multiplication.</p>
            <p>The natural exponential function <code>e<sup>x</sup></code> is its own derivative and is central to continuous growth and decay. Exponential models are often written as <code>Ae<sup>kt</sup></code>.</p>
            <p>Logarithms are useful for solving equations where the unknown appears in an exponent, estimating orders of magnitude, and describing scales such as sound intensity and acidity.</p>
        """,
          ("Solve 2<sup>x</sup>=32.", ("3", "4", "5", "6"), 2),
          ("If log<sub>10</sub>(x)=2.7, x is closest to:", ("50", "100", "500", "1000"), 2)),
        L(25, "Matrices and Linear Systems", """
            <p>A matrix is a rectangular arrangement of numbers. Matrix addition is performed entry-by-entry, while matrix multiplication combines rows of the first matrix with columns of the second.</p>
            <p>A system such as <code>2x+y=7</code> and <code>x-y=2</code> can be represented as <code>AX=b</code>. Row operations can transform the augmented matrix into a form that reveals the solution.</p>
            <p>A square matrix has a determinant. For a 2&times;2 matrix <code>[[a,b],[c,d]]</code>, the determinant is <code>ad-bc</code>. A zero determinant means the matrix has no inverse.</p>
            <p>Matrix methods scale naturally to many simultaneous equations and appear in computer graphics, control systems, data analysis and engineering models.</p>
        """,
          ("Solve the system 2x+y=7 and x-y=2. What is (x,y)?", ("(2,3)", "(3,1)", "(4,-1)", "(1,5)"), 1),
          ("What is the determinant of [[3,2],[5,4]]?", ("-2", "2", "12", "22"), 0)),
        L(26, "Complex Numbers", """
            <p>The imaginary unit satisfies <code>i&sup2;=-1</code>. A complex number has the form <code>a+bi</code>, where a is the real part and b is the imaginary part.</p>
            <p>Addition combines real and imaginary parts separately. Multiplication uses <code>i&sup2;=-1</code>, so products that initially look like fourth-degree algebra can be simplified back into the form <code>a+bi</code>.</p>
            <p>The complex conjugate of <code>a+bi</code> is <code>a-bi</code>. Multiplying a number by its conjugate gives <code>a&sup2;+b&sup2;</code>, which is real and is useful for division.</p>
            <p>The modulus <code>|a+bi|=&radic;(a&sup2;+b&sup2;)</code> gives the distance of the complex number from the origin in the complex plane.</p>
        """,
          ("Simplify (3+2i)(1-4i).", ("-5-10i", "11-10i", "11+10i", "3-8i"), 1),
          ("What is the modulus of -5+12i?", ("7", "12", "13", "17"), 2)),
        L(27, "Limits and Continuity", """
            <p>A limit describes the value a function approaches as the input approaches a point. It can exist even when the function is not defined at that exact point.</p>
            <p>For polynomial functions, direct substitution usually evaluates the limit. Indeterminate forms such as <code>0/0</code> may require factorisation, cancellation or other algebraic techniques.</p>
            <p>A function is continuous at x=a when its value exists, its limit exists, and the limit equals the function value. A removable hole violates the first condition at the point but can often be repaired by redefining the value.</p>
            <p>Limits are the foundation of derivatives because a derivative measures the limiting rate of change as the interval between two points approaches zero.</p>
        """,
          ("Evaluate lim<sub>x&rarr;2</sub> (x&sup2;-4)/(x-2).", ("2", "4", "6", "8"), 2),
          ("If a function approaches 7 from both sides of x=3 but is defined there as 2, which statement is correct?", ("The limit is 2", "The limit is 3", "The limit is 7 but the function is discontinuous at 3", "No limit exists"), 2)),
        L(28, "Differentiation and Applications", """
            <p>The derivative gives the instantaneous rate of change. For <code>f(x)=x<sup>n</sup></code>, the power rule gives <code>f'(x)=nx<sup>n-1</sup></code>.</p>
            <p>The product rule handles <code>uv</code>, the quotient rule handles <code>u/v</code>, and the chain rule handles a function nested inside another function.</p>
            <p>A stationary point occurs where the derivative is zero or undefined. The sign of the derivative on either side can reveal whether the function is increasing or decreasing and whether a stationary point is a local maximum or minimum.</p>
            <p>Derivatives also model velocity from position, marginal change in economics, optimisation in engineering and sensitivity of a system to small input changes.</p>
        """,
          ("If f(x)=3x&sup4;-5x&sup2;+2, what is f'(2)?", ("76", "86", "96", "106"), 1),
          ("For f(x)=x&sup3;-3x, the stationary points occur at:", ("x=0 only", "x=&plusmn;1", "x=&plusmn;&radic;3", "x=3"), 1)),
        L(29, "Integration and Area", """
            <p>Integration reverses differentiation in the sense captured by the fundamental theorem of calculus. An indefinite integral includes a constant because many functions have the same derivative.</p>
            <p>For powers, <code>&int;x<sup>n</sup>dx=x<sup>n+1</sup>/(n+1)+C</code> for <code>n&ne;-1</code>. Definite integrals evaluate an antiderivative at two limits and represent signed accumulated change.</p>
            <p>The area between a curve and the x-axis is positive where the curve is above the axis and negative where it is below. For geometric area, intervals and signs must therefore be interpreted carefully.</p>
            <p>Integration can also recover displacement from velocity and total quantity from a rate, making it the natural tool for accumulation problems.</p>
        """,
          ("Evaluate &int;<sub>0</sub><sup>2</sup> (3x&sup2;+1) dx.", ("8", "10", "12", "14"), 2),
          ("If velocity is v(t)=6t-4 m/s, what displacement occurs from t=1 to t=4?", ("24 m", "30 m", "33 m", "36 m"), 2)),
        L(30, "Differential Equations and Mathematical Modelling", """
            <p>A differential equation relates a function to one or more of its derivatives. It describes how a quantity changes rather than giving only its final value.</p>
            <p>For example, <code>dy/dt=ky</code> models continuous proportional growth or decay. Its solution has exponential form <code>y=Ce<sup>kt</sup></code>, where an initial condition determines C.</p>
            <p>More complicated models can include forcing terms, damping, feedback or nonlinear interactions. The equation alone may have many mathematical solutions, so initial or boundary conditions are essential for selecting the physically relevant one.</p>
            <p>Differential equations are used to model circuits, population dynamics, heat flow, mechanical motion and many other systems in which present behaviour depends on rates of change.</p>
        """,
          ("The model dy/dt=0.2y has y(0)=50. What is y(5)?", ("50e", "50e<sup>0.2</sup>", "50e<sup>1</sup>", "10e"), 2),
          ("A first-order model predicts a quantity decreases at a rate proportional to its current value. Which functional form is appropriate?", ("Linear", "Quadratic only", "Exponential decay", "Constant only"), 2)),
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
            <p>Average speed over a journey with several stages is always <b>total distance divided by
            total time</b>, not the average of the individual speeds &mdash; a journey that is faster
            for a short stage and slower for a long stage is weighted towards the slower speed.</p>
            <p>Because velocity includes direction, two objects can have the same speed but different
            velocities (e.g. moving north versus south), and a change in direction alone, even at
            constant speed, counts as a change in velocity.</p>
        """,
          ("A cyclist travels 30 km at 15 km/h, then returns the same 30 km at 10 km/h. What is the average speed for the whole 60 km journey?",
           ("12 km/h", "12.5 km/h", "15 km/h", "25 km/h"), 0),
          ("Two cars both travel at 20 m/s, one heading north and one heading south. Their velocities are:",
           ("Identical", "Equal in magnitude but different in direction", "Different speeds", "Not vectors"), 1)),
        L(2, "Acceleration and Motion Graphs", """
            <p>Acceleration is the rate of change of velocity, measured in m/s&sup2;:
            <code>a = (v - u) / t</code>.</p>
            <p>On a distance-time graph the gradient gives speed; a horizontal line means the object
            is stationary.</p>
            <p>On a velocity-time graph the gradient gives acceleration and the area under the line
            gives the distance travelled.</p>
            <p>A curved distance-time graph means the speed is changing: the steeper the curve becomes,
            the faster the object is moving at that instant. Similarly a curved velocity-time graph
            shows changing (non-uniform) acceleration.</p>
            <p>A velocity-time graph sloping downward toward zero shows deceleration; if it then stays
            flat at zero, the object has stopped, and any negative gradient below the axis represents
            motion in the reverse direction.</p>
        """,
          ("A car accelerates uniformly from 5 m/s to 25 m/s in 8 s. What is its acceleration?",
           ("2 m/s&sup2;", "2.5 m/s&sup2;", "3 m/s&sup2;", "4 m/s&sup2;"), 1),
          ("On a velocity-time graph, a straight line from (0 s, 10 m/s) to (5 s, 0 m/s) represents an object that is:",
           ("Accelerating at 2 m/s&sup2;", "Decelerating at 2 m/s&sup2;", "Stationary", "Moving at a constant 10 m/s"), 1)),
        L(3, "Forces and Newton's Laws", """
            <p>A force is a push or a pull, measured in newtons. Newton's first law: an object stays
            at rest or moves at constant velocity unless a resultant force acts on it (inertia).</p>
            <p>Newton's second law: <code>Force = mass &times; acceleration</code>.</p>
            <p>Newton's third law: every action has an equal and opposite reaction, acting on a
            different object.</p>
            <p>A <b>resultant force</b> is the single overall force found by combining every force
            acting on an object; if forces are balanced the resultant is zero and the object's velocity
            does not change, however large the individual forces are.</p>
            <p>Newton's second law rearranges easily to find any one quantity from the other two:
            <code>a = F / m</code> or <code>m = F / a</code>, which is essential for braking and
            acceleration calculations.</p>
        """,
          ("A resultant force of 24 N acts on an object, giving it an acceleration of 3 m/s&sup2;. What is the object's mass?",
           ("6 kg", "8 kg", "21 kg", "72 kg"), 1),
          ("A 1000 kg car decelerates from 20 m/s to rest in 5 s. What braking force is needed?",
           ("200 N", "800 N", "4000 N", "5000 N"), 2)),
        L(4, "Gravity, Mass and Weight", """
            <p>Mass is the amount of matter in an object and does not change with location; weight is
            the force of gravity on that mass.</p>
            <p><code>Weight = mass &times; gravitational field strength</code>. On Earth g &asymp; 10 N/kg,
            so a 60 kg person weighs about 600 N.</p>
            <p>On the Moon g is about one sixth of Earth's, so the same person weighs far less but has
            exactly the same mass.</p>
            <p>Weight acts through an object's <b>centre of mass</b> and, unlike mass, is measured with
            a newtonmeter (spring balance) rather than a mass balance, since it depends on the local
            gravitational field.</p>
            <p>Because mass is unaffected by location, a mass calculated from a weight measured on
            Earth is exactly the same value anywhere else in the universe &mdash; only the weight
            changes when g changes.</p>
        """,
          ("An astronaut has a mass of 80 kg. On the Moon (g = 1.6 N/kg) their weight is:",
           ("80 N", "128 N", "480 N", "800 N"), 1),
          ("A person weighs 750 N on Earth (g = 10 N/kg). Their mass on Mars (g = 3.7 N/kg) would be:",
           ("75 kg", "277.5 kg", "20.3 kg", "750 kg"), 0)),
        L(5, "Work, Energy and Power", """
            <p>Work done = force &times; distance moved in the direction of the force, measured in joules.</p>
            <p>Energy is conserved: it transfers between stores such as kinetic
            (<code>&frac12;mv&sup2;</code>) and gravitational potential (<code>mgh</code>).</p>
            <p>Power is the rate of energy transfer: <code>P = E / t</code>, measured in watts.</p>
            <p>Because energy is conserved, gravitational potential energy lost as an object falls
            converts (ignoring air resistance) entirely into kinetic energy gained, which is how the
            speed of a falling object can be calculated without using the equations of motion directly.</p>
            <p>Combining these ideas lets you connect work, energy and power in a single multi-step
            problem: work done gives energy transferred, and energy transferred divided by time gives
            power delivered.</p>
        """,
          ("A crane lifts a 500 kg load 10 m in 20 s (g = 10 N/kg). What power does it develop?",
           ("250 W", "2500 W", "5000 W", "50000 W"), 1),
          ("A 2 kg ball is dropped and falls freely. Its speed just before hitting the ground after falling 5 m (g = 10 N/kg) is:",
           ("5 m/s", "10 m/s", "20 m/s", "50 m/s"), 1)),
        L(6, "Momentum", """
            <p>Momentum = mass &times; velocity, measured in kg m/s, and it is a vector.</p>
            <p>In a closed system total momentum before a collision equals total momentum after &mdash;
            the principle of conservation of momentum.</p>
            <p>Crumple zones and airbags increase the time taken to change momentum, which reduces the
            force experienced.</p>
            <p>In a collision where two objects stick together (a "perfectly inelastic" collision), the
            combined mass moves off with a single shared velocity, found by dividing the total momentum
            before the collision by the total mass afterwards.</p>
            <p>Force and momentum are linked by <code>F = &Delta;p / &Delta;t</code>, the change in
            momentum divided by the time taken for that change &mdash; the formal explanation for why
            spreading out an impact over more time reduces the force involved.</p>
        """,
          ("A 2 kg trolley moving at 3 m/s collides and sticks to a stationary 1 kg trolley. What is their combined velocity after the collision?",
           ("1 m/s", "1.5 m/s", "2 m/s", "3 m/s"), 2),
          ("A 0.5 kg ball hits a wall at 8 m/s and rebounds at 8 m/s. What is the magnitude of the change in momentum?",
           ("0", "4 kg m/s", "8 kg m/s", "16 kg m/s"), 2)),
        L(7, "Density and Pressure", """
            <p>Density = mass / volume, usually in kg/m&sup3;. Objects less dense than a fluid float in it.</p>
            <p>Pressure = force / area, measured in pascals. A sharp knife has a tiny contact area, so
            a modest force gives a very high pressure.</p>
            <p>In a liquid, pressure increases with depth and acts in all directions.</p>
            <p>Density explains floating and sinking directly: an object floats when it displaces a
            weight of fluid equal to its own weight before it is fully submerged, which is only
            possible if its average density is less than that of the fluid.</p>
            <p>Pressure in a liquid at depth h is given by <code>P = &rho;gh</code>, where &rho; is the
            liquid's density &mdash; this is why deep-sea vessels must be built to withstand enormous
            pressures compared with the surface.</p>
        """,
          ("A block has a mass of 540 g and a volume of 200 cm&sup3;. Its density is:",
           ("0.37 g/cm&sup3;", "2.7 g/cm&sup3;", "27 g/cm&sup3;", "108 g/cm&sup3;"), 1),
          ("A force of 300 N acts on an area of 0.05 m&sup2;. The pressure is:",
           ("15 Pa", "60 Pa", "600 Pa", "6000 Pa"), 3)),
        L(8, "Heat and Temperature", """
            <p>Temperature measures how hot something is; thermal energy depends on both temperature
            and mass.</p>
            <p>Heat transfers by conduction (through solids), convection (in fluids, driven by density
            differences) and radiation (infrared waves, needing no medium).</p>
            <p>Insulation, such as trapped air in a jumper, slows conduction and convection.</p>
            <p>Because thermal energy depends on mass as well as temperature, two objects at the exact
            same temperature can store very different amounts of thermal energy if their masses (or
            specific heat capacities) differ &mdash; a large mass at a given temperature holds more
            energy than a small one at that same temperature.</p>
            <p>A vacuum flask combines several strategies at once: an evacuated gap between its walls
            almost eliminates conduction and convection, while a silvered (reflective) inner surface
            reduces heat loss by radiation too.</p>
        """,
          ("Two identical mugs contain water at the same temperature, but one has twice the mass of water. Which has more thermal energy?",
           ("The lighter one", "The heavier one", "Both are equal", "Cannot be determined"), 1),
          ("A vacuum flask reduces heat loss by preventing:",
           ("Conduction and convection only", "Radiation only", "Conduction, convection and radiation", "Evaporation only"), 2)),
        L(9, "Waves", """
            <p>Waves transfer energy without transferring matter. In <b>transverse</b> waves the
            oscillation is perpendicular to travel (light); in <b>longitudinal</b> waves it is parallel (sound).</p>
            <p>Key terms: amplitude, wavelength, frequency (hertz) and period.</p>
            <p>The wave equation is <code>v = f&lambda;</code>: speed equals frequency times wavelength.</p>
            <p>Frequency and period are reciprocals of one another, <code>T = 1/f</code>, so a wave with
            a higher frequency has a shorter period between successive wave crests passing a fixed
            point.</p>
            <p>The wave equation can be rearranged to find any one quantity from the other two, which is
            how the frequency of a sound can be calculated from its measured speed and wavelength, or
            vice versa.</p>
        """,
          ("A wave has a frequency of 50 Hz and a wavelength of 4 m. Its speed is:",
           ("12.5 m/s", "54 m/s", "200 m/s", "400 m/s"), 2),
          ("A sound wave travels at 340 m/s and has a wavelength of 0.85 m. Its frequency is:",
           ("200 Hz", "289 Hz", "400 Hz", "850 Hz"), 2)),
        L(10, "Sound and Hearing", """
            <p>Sound is a longitudinal wave of compressions and rarefactions, so it needs a medium and
            cannot travel through a vacuum.</p>
            <p>Higher frequency is heard as higher pitch; larger amplitude is heard as greater loudness.</p>
            <p>Sound travels faster in solids than in liquids, and faster in liquids than in gases,
            because particles are closer together.</p>
            <p>An echo is simply a reflected sound wave; timing how long an echo takes to return, and
            knowing the speed of sound, lets you calculate the distance to the reflecting surface &mdash;
            remembering that the sound travels there <i>and back</i> in that time.</p>
            <p>Ultrasound uses frequencies above the range of human hearing (above about 20,000 Hz) and
            is used in medical scanning and sonar because it reflects strongly off boundaries between
            different materials.</p>
        """,
          ("Sound travels faster in steel than in air mainly because in steel the particles are:",
           ("Further apart", "Closer together, transmitting vibrations more quickly", "Not vibrating", "Charged"), 1),
          ("A person hears an echo 0.5 s after shouting at a cliff. If sound travels at 340 m/s, how far away is the cliff?",
           ("85 m", "170 m", "340 m", "680 m"), 0)),
        L(11, "Light and Optics", """
            <p>Light travels in straight lines and reflects so that the angle of incidence equals the
            angle of reflection.</p>
            <p>Refraction is the bending of light when it changes speed entering a new medium, which is
            why a straw looks bent in water.</p>
            <p>Converging lenses bring parallel rays to a focus and are used in cameras and eyes;
            white light can be dispersed into a spectrum by a prism.</p>
            <p>Both angle of incidence and angle of reflection are always measured from the
            <b>normal</b>, an imaginary line at right angles to the surface &mdash; not from the surface
            itself, which is a common source of errors.</p>
            <p>Dispersion happens because different colours of light (different wavelengths) refract by
            slightly different amounts in the same material, so white light entering a prism spreads
            into its full spectrum of colours rather than staying as a single beam.</p>
        """,
          ("A ray of light hits a mirror at an angle of 35&deg; to the mirror's surface. The angle of reflection, measured from the normal, is:",
           ("35&deg;", "45&deg;", "55&deg;", "90&deg;"), 2),
          ("White light passing through a prism separates into a spectrum because:",
           ("Different colours have different speeds in air", "Different colours refract by different amounts in the glass", "The prism absorbs some colours", "Light reflects off the prism"), 1)),
        L(12, "Current, Voltage and Resistance", """
            <p>Current is the rate of flow of charge, measured in amperes; voltage is the energy given
            per unit charge, measured in volts.</p>
            <p>Resistance opposes current. Ohm's law states <code>V = IR</code>.</p>
            <p>So a 12 V supply pushing 2 A through a component means the component has a resistance
            of 6 ohms.</p>
            <p>Ohm's law rearranges to find any of the three quantities given the other two:
            <code>I = V/R</code> or <code>R = V/I</code>, and these forms are used constantly when
            analysing circuits.</p>
            <p>A resistor that obeys Ohm's law has a constant resistance regardless of the current
            flowing through it (an "ohmic" conductor); components like filament lamps and diodes do not
            behave this way, since their resistance changes with current or temperature.</p>
        """,
          ("A component has a resistance of 15 &Omega; and a current of 0.4 A flows through it. The voltage across it is:",
           ("0.027 V", "6 V", "15.4 V", "37.5 V"), 1),
          ("A 6 V battery drives current through two identical resistors in series, each 4 &Omega;. What current flows?",
           ("0.5 A", "0.75 A", "1.5 A", "24 A"), 1)),
        L(13, "Electrical Circuits", """
            <p>In a <b>series</b> circuit there is one path: current is the same everywhere and the
            supply voltage is shared between components.</p>
            <p>In a <b>parallel</b> circuit there are branches: each branch gets the full supply voltage
            and the currents in the branches add up to the total.</p>
            <p>Adding resistors in series increases total resistance; adding them in parallel decreases it.</p>
            <p>Total resistance in series is simply the sum of the individual resistances,
            <code>R_total = R1 + R2 + ...</code>, but in parallel the reciprocals add:
            <code>1/R_total = 1/R1 + 1/R2 + ...</code>, which always gives a total smaller than the
            smallest individual resistor.</p>
            <p>These rules let you predict circuit behaviour without a meter: for example, since
            parallel branches share the same voltage, two identical bulbs in parallel across a battery
            are each as bright as if connected alone, unlike in series where the voltage &mdash; and
            therefore the brightness &mdash; is shared between them.</p>
        """,
          ("Two 6 &Omega; resistors are connected in parallel. Their combined resistance is:",
           ("3 &Omega;", "6 &Omega;", "12 &Omega;", "36 &Omega;"), 0),
          ("In a circuit with a 12 V battery and two identical bulbs in parallel, each bulb has a voltage across it of:",
           ("6 V", "12 V", "24 V", "0 V"), 1)),
        L(14, "Magnetism and Electromagnetism", """
            <p>Magnets have north and south poles; like poles repel and unlike poles attract.</p>
            <p>A current in a wire creates a magnetic field around it. Coiling the wire into a solenoid
            around an iron core makes an electromagnet that can be switched on and off.</p>
            <p>A current-carrying wire in a magnetic field experiences a force &mdash; the motor effect.
            Moving a magnet near a coil induces a voltage, which is how generators work.</p>
            <p>The strength of an electromagnet increases with a larger current, more turns of wire in
            the coil, and the presence of an iron core, which concentrates the magnetic field far more
            strongly than an air-filled coil.</p>
            <p>The size of an induced voltage in a generator increases with a faster relative motion
            between magnet and coil, a stronger magnet, and more turns on the coil &mdash; the same
            factors that strengthen an electromagnet also strengthen electromagnetic induction.</p>
        """,
          ("To increase the strength of an electromagnet, you could:",
           ("Reduce the number of coil turns", "Increase the current or number of turns", "Remove the iron core", "Use AC only"), 1),
          ("A generator produces a bigger induced voltage when:",
           ("The magnet moves faster", "The coil is removed", "The current is reduced", "The wire is thicker only"), 0)),
        L(15, "Atoms and Radioactivity", """
            <p>An atom has a tiny nucleus of protons and neutrons, surrounded by electrons.</p>
            <p>Unstable nuclei decay and emit radiation: alpha (stopped by paper), beta (stopped by thin
            aluminium) and gamma (reduced by thick lead).</p>
            <p>Half-life is the time for half the undecayed nuclei in a sample to decay &mdash; a random
            process that is predictable only on average.</p>
            <p>Half-life calculations repeat the same halving step for each half-life that passes: after
            n half-lives, the remaining amount is the original amount divided by <code>2&#8319;</code>.</p>
            <p>There is a trade-off between penetration and ionising power: alpha particles are the most
            strongly ionising (easily stopped, but very damaging to living cells at close range) while
            gamma rays are the most penetrating but the least ionising per unit of radiation.</p>
        """,
          ("A radioactive isotope has a half-life of 6 hours. Starting with 80 g, how much remains after 18 hours?",
           ("5 g", "10 g", "20 g", "40 g"), 1),
          ("Alpha particles are the least penetrating but the most:",
           ("Fast-moving", "Ionising", "Charge-neutral", "Able to pass through lead"), 1)),

        L(16, "Kinematics Graphs", """
            <p>Motion can be represented by displacement-time, velocity-time and acceleration-time graphs. The gradient of a displacement-time graph gives velocity, while the gradient of a velocity-time graph gives acceleration.</p>
            <p>The area under a velocity-time graph represents displacement. The area under an acceleration-time graph represents the change in velocity.</p>
            <p>A horizontal velocity-time line means constant velocity even though the object may be moving. A horizontal displacement-time line means the object is stationary because its displacement is not changing.</p>
            <p>Graph interpretation is powerful because it separates what a quantity is from how rapidly it changes and allows motion to be analysed without relying only on equations.</p>
        """,
          ("A velocity-time graph is a horizontal line at 8 m/s for 12 s. What displacement occurs?", ("20 m", "48 m", "96 m", "120 m"), 2),
          ("On a displacement-time graph, a curve becomes progressively steeper with time. What does this indicate?", ("Constant zero velocity", "Increasing speed in the positive direction", "Constant negative acceleration only", "Zero displacement"), 1)),
        L(17, "Projectile Motion", """
            <p>Projectile motion combines horizontal and vertical motion under gravity. Ignoring air resistance, horizontal acceleration is zero while vertical acceleration is approximately <code>g</code> downward.</p>
            <p>The horizontal and vertical components can be analysed independently. If an object is launched with speed u at angle &theta;, its initial components are <code>u cos&theta;</code> horizontally and <code>u sin&theta;</code> vertically.</p>
            <p>For launch and landing at the same height, the time of flight is <code>2u sin&theta;/g</code> and the range is <code>u&sup2;sin(2&theta;)/g</code>. These formulas depend on the assumptions of uniform gravity and negligible air resistance.</p>
            <p>The trajectory is parabolic because horizontal displacement changes linearly with time while vertical displacement changes quadratically.</p>
        """,
          ("A projectile is launched at 20 m/s at 30&deg;. Taking g=10 m/s&sup2;, its initial vertical velocity is:", ("5 m/s", "10 m/s", "17.3 m/s", "20 m/s"), 1),
          ("For the same launch speed and level landing, which launch angle gives the greatest ideal range?", ("30&deg;", "45&deg;", "60&deg;", "90&deg;"), 1)),
        L(18, "Circular Motion", """
            <p>Uniform circular motion has constant speed but changing velocity because the direction changes continuously. The inward acceleration is called centripetal acceleration and has magnitude <code>a=v&sup2;/r</code>.</p>
            <p>The corresponding centripetal force is <code>F=mv&sup2;/r</code>. It is not a new type of force; it is the name given to the net inward force responsible for circular motion.</p>
            <p>Angular speed <code>&omega;</code> relates to linear speed through <code>v=&omega;r</code>. One complete revolution corresponds to <code>2&pi;</code> radians.</p>
            <p>Increasing speed strongly increases the required inward force because force depends on the square of speed. Doubling speed at fixed radius requires four times the centripetal force.</p>
        """,
          ("A 2 kg object moves at 6 m/s around a circle of radius 3 m. What centripetal force is required?", ("12 N", "18 N", "24 N", "36 N"), 2),
          ("If the speed of an object in circular motion doubles while radius and mass remain fixed, centripetal acceleration becomes:", ("2 times", "3 times", "4 times", "8 times"), 2)),
        L(19, "Torque and Rotational Equilibrium", """
            <p>Torque measures the turning effect of a force. Its magnitude is <code>&tau;=rF sin&theta;</code>, where r is the distance from the pivot and &theta; is the angle between the lever arm and force.</p>
            <p>A force applied perpendicular to a long lever arm produces more torque than the same force applied close to the pivot or at a smaller angle.</p>
            <p>For rotational equilibrium, the net clockwise torque equals the net anticlockwise torque. This is the rotational analogue of zero net force for translational equilibrium.</p>
            <p>Torque explains why door handles are placed far from hinges and why a spanner is easier to use when its handle is longer.</p>
        """,
          ("A 30 N force acts perpendicular to a lever 0.4 m from its pivot. What torque is produced?", ("7.5 N m", "12 N m", "30 N m", "75 N m"), 1),
          ("A 20 N force acts at 30&deg; to a 0.5 m lever arm. What torque magnitude results?", ("2.5 N m", "5 N m", "8.66 N m", "10 N m"), 1)),
        L(20, "Rotational Dynamics and Moment of Inertia", """
            <p>Rotational motion has analogues of mass, force and momentum. Moment of inertia <code>I</code> measures resistance to angular acceleration and depends on both mass and how far that mass is distributed from the axis.</p>
            <p>Rotational dynamics follows <code>&tau;=I&alpha;</code>, where &alpha; is angular acceleration. The same torque produces less angular acceleration for an object with larger moment of inertia.</p>
            <p>Angular momentum is <code>L=I&omega;</code>. If external torque is negligible, angular momentum is conserved, so a spinning system can increase angular speed when its moment of inertia decreases.</p>
            <p>This principle appears in rotating machinery, gyroscopes and the motion of a skater pulling their arms inward while spinning.</p>
        """,
          ("If a wheel has moment of inertia 4 kg m&sup2; and experiences a torque of 12 N m, its angular acceleration is:", ("0.33 rad/s&sup2;", "3 rad/s&sup2;", "8 rad/s&sup2;", "48 rad/s&sup2;"), 1),
          ("A rotating person reduces their moment of inertia to one-half with negligible external torque. Their angular speed becomes:", ("Half as large", "Unchanged", "Twice as large", "Four times as large"), 2)),
        L(21, "Gravitation and Orbital Motion", """
            <p>Newton's law of gravitation states <code>F=GMm/r&sup2;</code>. The force decreases with the square of separation between the centres of the two masses.</p>
            <p>An orbit occurs because gravity continuously changes the direction of an object's velocity while the object has enough tangential motion to keep falling around the attracting body rather than directly into it.</p>
            <p>For a circular orbit, gravitational force provides centripetal force, giving <code>v=&radic;(GM/r)</code>. Larger orbital radii therefore correspond to lower circular orbital speeds.</p>
            <p>Orbital period also increases with radius. This explains why distant planets take much longer to complete an orbit than planets closer to their star.</p>
        """,
          ("If the distance between two masses doubles, their gravitational force becomes:", ("Twice as large", "Half as large", "One-quarter as large", "Four times as large"), 2),
          ("For a circular orbit around the same central mass, increasing orbital radius by a factor of 4 changes circular orbital speed by a factor of:", ("4", "2", "1/2", "1/4"), 2)),
        L(22, "Fluid Mechanics and Buoyancy", """
            <p>Pressure in a stationary fluid increases with depth according to <code>P=P<sub>0</sub>+&rho;gh</code>. The increase depends on density, gravitational field strength and depth.</p>
            <p>Archimedes' principle states that an immersed object experiences an upward buoyant force equal to the weight of the fluid displaced.</p>
            <p>An object floats when buoyant force balances its weight. For a floating object, the fraction of its volume submerged is related to the ratio of object density to fluid density.</p>
            <p>Hydraulic systems exploit pressure transmission through fluids. A pressure applied to one piston can create a larger force on a larger piston because force equals pressure times area.</p>
        """,
          ("What pressure increase occurs 5 m below the surface of water if &rho;=1000 kg/m&sup3; and g=10 m/s&sup2;?", ("5 kPa", "10 kPa", "50 kPa", "100 kPa"), 2),
          ("An object has density 600 kg/m&sup3; and floats in water of density 1000 kg/m&sup3;. Approximately what fraction of its volume is submerged?", ("0.4", "0.6", "1.0", "1.67"), 1)),
        L(23, "Thermodynamics and Internal Energy", """
            <p>Temperature measures the average microscopic kinetic energy of particles, while internal energy includes microscopic kinetic and potential contributions.</p>
            <p>The first law of thermodynamics expresses energy conservation as <code>&Delta;U=Q-W</code> when W is work done by the system. Heating can therefore increase internal energy, while expansion work can decrease it.</p>
            <p>Specific heat capacity is the energy needed to raise the temperature of 1 kg of a substance by 1 K: <code>Q=mc&Delta;T</code>.</p>
            <p>During a phase change, energy can enter or leave without changing temperature because it changes the microscopic arrangement of particles rather than simply increasing their average kinetic energy.</p>
        """,
          ("How much energy is required to heat 2 kg of a material with c=500 J/kg K by 20 K?", ("5 kJ", "10 kJ", "20 kJ", "40 kJ"), 2),
          ("During boiling at constant pressure, supplied energy mainly goes into:", ("Increasing temperature only", "Changing phase by overcoming intermolecular attractions", "Reducing mass", "Creating gravitational potential energy"), 1)),
        L(24, "Gas Laws", """
            <p>For an ideal gas, pressure, volume, temperature and amount are related by <code>PV=nRT</code>. Temperature in this equation must be measured on an absolute scale such as kelvin.</p>
            <p>At constant temperature, increasing volume reduces pressure so that <code>PV</code> remains constant. At constant volume, pressure is proportional to absolute temperature.</p>
            <p>Real gases approach ideal behaviour when particles are relatively far apart and intermolecular interactions are less important, such as at low pressure and sufficiently high temperature.</p>
            <p>Gas-law reasoning is useful for engines, refrigeration, pressure vessels, weather processes and laboratory measurements.</p>
        """,
          ("A gas occupies 2 L at 300 K. If pressure remains constant and temperature rises to 450 K, what is its new volume?", ("1.33 L", "2 L", "3 L", "4.5 L"), 2),
          ("At fixed volume, the absolute temperature of a gas doubles. Its ideal-gas pressure becomes:", ("Half", "Unchanged", "Double", "Four times"), 2)),
        L(25, "Electrostatics and Electric Fields", """
            <p>Electric charge exists in positive and negative forms. Like charges repel and unlike charges attract. Charge is conserved, so it can be transferred but not created or destroyed in ordinary processes.</p>
            <p>Coulomb's law gives the force between point charges as <code>F=k|q<sub>1</sub>q<sub>2</sub>|/r&sup2;</code>. The inverse-square dependence means doubling separation reduces force to one-quarter.</p>
            <p>An electric field is force per unit positive test charge: <code>E=F/q</code>. Around an isolated point charge its magnitude is <code>E=kQ/r&sup2;</code>.</p>
            <p>Electric potential is energy per unit charge. A positive charge naturally moves toward lower electric potential when only electric forces do work, while negative charges behave oppositely in terms of force direction.</p>
        """,
          ("Two point charges are separated by 3 m. If their separation is reduced to 1 m with charges unchanged, Coulomb force becomes:", ("One-third", "Three times", "Six times", "Nine times"), 3),
          ("An electric field has magnitude 2000 N/C. What force acts on a 3 &times; 10<sup>-6</sup> C charge placed in it?", ("0.00067 N", "0.003 N", "0.006 N", "6000 N"), 2)),
        L(26, "Electromagnetic Induction", """
            <p>Faraday's law states that an induced emf is produced when magnetic flux through a circuit changes. Its magnitude depends on the rate of change of flux linkage.</p>
            <p>Lenz's law gives the direction: the induced current acts to oppose the change in magnetic flux that produced it. This is a consequence of energy conservation.</p>
            <p>Changing the magnetic field, changing the area of a loop, or moving a magnet relative to a coil can all change magnetic flux and induce an emf.</p>
            <p>Generators convert mechanical motion into electrical energy using induction. Transformers also rely on changing magnetic flux to transfer energy between coils, although they require alternating current for continuous operation.</p>
        """,
          ("A coil has 200 turns and its magnetic flux changes by 0.03 Wb in 0.2 s. What is the magnitude of average induced emf?", ("3 V", "15 V", "30 V", "300 V"), 2),
          ("Lenz's law determines the induced current direction so that it:", ("Always increases the flux change", "Opposes the change in magnetic flux producing it", "Always flows clockwise", "Always flows anticlockwise"), 1)),
        L(27, "Alternating Current and Transformers", """
            <p>Alternating current changes direction periodically. For a sinusoidal source, the root-mean-square value gives the equivalent DC value for resistive heating.</p>
            <p>An ideal transformer follows <code>V<sub>s</sub>/V<sub>p</sub>=N<sub>s</sub>/N<sub>p</sub></code>. Increasing secondary turns produces a step-up transformer, while fewer secondary turns produce a step-down transformer.</p>
            <p>For an ideal transformer, input and output power are approximately equal, so increasing voltage reduces current in the same proportion, neglecting losses.</p>
            <p>High-voltage transmission reduces resistive losses because power can be transmitted at lower current for the same delivered power, while power loss in a line is approximately <code>I&sup2;R</code>.</p>
        """,
          ("An ideal transformer has 500 primary turns and 2000 secondary turns. If the primary voltage is 120 V, the secondary voltage is:", ("30 V", "120 V", "240 V", "480 V"), 3),
          ("For the same transmitted power, reducing line current to one-half changes resistive power loss I&sup2;R to:", ("One-half", "One-quarter", "Double", "Four times"), 1)),
        L(28, "Wave Interference and Diffraction", """
            <p>When waves overlap, their displacements add according to the principle of superposition. Constructive interference occurs when waves reinforce, while destructive interference occurs when they cancel.</p>
            <p>For coherent sources, stable interference patterns can be produced because their phase relationship remains fixed. Path difference determines whether reinforcement or cancellation occurs.</p>
            <p>Diffraction is the spreading of waves around obstacles and through openings. It becomes especially noticeable when the obstacle or aperture size is comparable to the wavelength.</p>
            <p>Interference and diffraction occur for water, sound, light and matter waves, showing that they are general wave phenomena rather than properties of one particular type of wave.</p>
        """,
          ("Two coherent waves arrive in phase at a point with equal amplitude. The resulting amplitude is:", ("Zero", "Half of one wave", "Equal to one wave", "Twice the amplitude of one wave"), 3),
          ("Diffraction through a single slit becomes more pronounced when the slit width is:", ("Much larger than wavelength", "Comparable to wavelength", "Exactly zero", "Independent of wavelength"), 1)),
        L(29, "Quantum Physics", """
            <p>Quantum physics describes microscopic systems whose behaviour cannot always be explained by classical trajectories. Energy exchange can occur in discrete amounts called quanta.</p>
            <p>Photons have energy <code>E=hf</code>. Increasing frequency therefore increases photon energy, while increasing intensity at fixed frequency mainly increases the number of photons arriving per unit time.</p>
            <p>Wave-particle duality means particles such as electrons have associated wavelengths described by de Broglie's relation <code>&lambda;=h/p</code>. Smaller momentum corresponds to a longer wavelength.</p>
            <p>Quantum ideas underpin lasers, semiconductors, electron microscopes, atomic spectra and modern electronic devices.</p>
        """,
          ("A photon has frequency 6 &times; 10<sup>14</sup> Hz. Taking h=6.63 &times; 10<sup>-34</sup> J s, its energy is closest to:", ("3.98 &times; 10<sup>-19</sup> J", "9.95 &times; 10<sup>-20</sup> J", "1.11 &times; 10<sup>-47</sup> J", "4.42 &times; 10<sup>-9</sup> J"), 0),
          ("If an electron's momentum doubles, its de Broglie wavelength becomes:", ("Twice as large", "Half as large", "Four times as large", "Unchanged"), 1)),
        L(30, "Relativity and Modern Physics", """
            <p>Special relativity states that the laws of physics are the same in all inertial frames and that the speed of light in vacuum is invariant. These assumptions lead to time dilation and length contraction at very high relative speeds.</p>
            <p>Mass and energy are related by <code>E=mc&sup2;</code>, showing that even a small mass corresponds to a very large energy equivalent because c is enormous.</p>
            <p>Relativistic effects are negligible at ordinary speeds but become important for particles in accelerators and for precision technologies such as satellite navigation.</p>
            <p>Modern physics combines relativity and quantum theory with classical models where appropriate, using each framework within the regime where its assumptions apply.</p>
        """,
          ("The rest-energy equivalent of 1 gram of mass is closest to:", ("9 &times; 10<sup>7</sup> J", "9 &times; 10<sup>10</sup> J", "9 &times; 10<sup>13</sup> J", "9 &times; 10<sup>16</sup> J"), 2),
          ("According to special relativity, an object moving very close to light speed relative to an observer experiences, in the observer's frame, time that:", ("Runs faster", "Runs slower", "Stops permanently", "Is always identical to the observer's time"), 1)),
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
            <p>The number of distinct values n bits can represent is always <code>2&#8319;</code>, so
            doubling the number of bits available squares the range of values that can be stored, not
            just doubles it.</p>
            <p>File size can be estimated by multiplying the number of stored items by the bytes needed
            per item &mdash; for example an image's file size is roughly its pixel count multiplied by
            the bytes used to store each pixel's colour.</p>
        """,
          ("How many different values can be represented using 10 bits?",
           ("10", "100", "1024", "2048"), 2),
          ("A 5-megapixel image using 3 bytes per pixel (RGB) needs approximately how much storage?",
           ("1.5 MB", "5 MB", "15 MB", "50 MB"), 2)),
        L(2, "Number Systems", """
            <p>Denary (base 10) uses digits 0-9; binary (base 2) uses 0-1; hexadecimal (base 16) uses
            0-9 then A-F.</p>
            <p>In binary, place values double: 1011 is 8 + 0 + 2 + 1 = 11 in denary.</p>
            <p>Hex is popular with programmers because one hex digit represents exactly four bits, making
            long binary strings readable.</p>
            <p>Converting denary to binary repeatedly checks the largest remaining place value (128, 64,
            32, 16, 8, 4, 2, 1 for a byte) and records a 1 or 0 depending on whether that value can be
            subtracted &mdash; effectively building the number place by place.</p>
            <p>Because one hex digit maps exactly to four bits, converting hex to binary (or back) can
            be done digit by digit without needing to work with the whole number at once, which is why
            programmers often use hex as shorthand for binary.</p>
        """,
          ("Convert the denary number 45 into binary.",
           ("101101", "110101", "101011", "111001"), 0),
          ("Convert the hexadecimal number 2F into denary.",
           ("31", "37", "47", "79"), 2)),
        L(3, "Hardware and the CPU", """
            <p>The CPU fetches, decodes and executes instructions in a continuous cycle.</p>
            <p>Key parts are the control unit, the arithmetic logic unit (ALU) and registers; cache is
            small fast memory close to the CPU.</p>
            <p>RAM is volatile working memory, lost when power goes; secondary storage such as an SSD
            keeps data permanently.</p>
            <p>The <b>program counter</b> register keeps track of the memory address of the next
            instruction to be fetched, while the <b>accumulator</b> holds the results of calculations
            the ALU is currently working on.</p>
            <p>Cache sits between the CPU and RAM, storing frequently used data closer to the processor;
            since accessing cache is much faster than accessing RAM, a larger cache combined with a
            higher clock speed generally improves performance on instruction-heavy tasks.</p>
        """,
          ("Which factor would generally increase CPU performance the most for typical instruction-heavy tasks?",
           ("A slower clock speed", "More cache and a higher clock speed", "Less RAM", "Removing the ALU"), 1),
          ("During the fetch-decode-execute cycle, the address of the next instruction is normally held in the:",
           ("Program counter", "Accumulator", "Cache", "Hard disk"), 0)),
        L(4, "Software and Operating Systems", """
            <p>System software runs the machine; application software does jobs for the user.</p>
            <p>An operating system manages memory, processes, files, devices and user accounts, hiding
            hardware complexity behind a consistent interface.</p>
            <p>Utility programs handle housekeeping such as backup, compression and virus scanning.</p>
            <p><b>Process management</b> is one of the OS's central jobs: with only one (or a few) CPU
            cores but many programs wanting to run, the OS decides which process gets CPU time next and
            for how long, switching between them so quickly it appears they all run at once.</p>
            <p><b>Virtual memory</b> lets the OS treat part of secondary storage as an extension of RAM,
            allowing programs to use more memory than is physically installed, at the cost of being
            slower than true RAM access.</p>
        """,
          ("An OS uses virtual memory mainly to:",
           ("Make RAM permanent", "Let programs use more memory than physically exists by using disk space", "Speed up the CPU clock", "Compress files"), 1),
          ("Which task is handled by the operating system's process management?",
           ("Formatting a document", "Deciding which program gets CPU time next", "Designing an app's icon", "Writing source code"), 1)),
        L(5, "Introduction to Algorithms", """
            <p>An algorithm is a precise step-by-step set of instructions for solving a problem.</p>
            <p>To find the largest number in a list, assume the first is largest, then compare it with
            each remaining number, updating whenever a bigger one appears.</p>
            <p>Good algorithms are unambiguous, finite (they stop) and correct. They can be planned with
            pseudocode or flowcharts before coding.</p>
            <p>"Correct" and "efficient" are different properties: an algorithm can always give the
            right answer yet still be a poor choice if it takes far longer, or uses far more memory,
            than an alternative approach solving the same problem.</p>
            <p>Tracing an algorithm by hand &mdash; working through it step by step with a specific
            example, tracking how variables change &mdash; is the most reliable way to check it does
            what you expect before trusting it with real data.</p>
        """,
          ("An algorithm sets max = list[0], then compares max with each remaining item, updating max if a larger value is found. For the list [3, 9, 4, 9, 2], what is max at the end?",
           ("3", "4", "9", "2"), 2),
          ("Which best describes an algorithm that is correct but not efficient?",
           ("It never finishes", "It gives wrong answers sometimes", "It gives the right answer but takes excessive time or resources", "It cannot be written in pseudocode"), 2)),
        L(6, "Searching Algorithms", """
            <p>A <b>linear search</b> checks each item in turn. It works on any list but is slow for
            large data.</p>
            <p>A <b>binary search</b> repeatedly halves a <i>sorted</i> list, discarding the half that
            cannot contain the target.</p>
            <p>Binary search finds an item among a million sorted records in about 20 comparisons.</p>
            <p>Each step of a binary search compares the target with the middle item: if the target is
            smaller, the entire upper half of the list is discarded in one move; if larger, the lower
            half is discarded &mdash; this halving is what makes it so much faster than checking items
            one at a time.</p>
            <p>The number of comparisons binary search needs in the worst case grows only with the
            logarithm of the list size, so even a huge increase in data size adds relatively few extra
            comparisons.</p>
        """,
          ("Searching for 23 in the sorted list [2, 5, 9, 12, 23, 31, 40, 55] using binary search, which value is checked first?",
           ("2", "12", "23", "40"), 1),
          ("For a sorted list of 1 million items, roughly how many comparisons does binary search need in the worst case?",
           ("About 20", "About 1000", "About 500", "About 1,000,000"), 0)),
        L(7, "Sorting Algorithms", """
            <p><b>Bubble sort</b> repeatedly compares neighbouring items and swaps them if out of order;
            simple but slow.</p>
            <p><b>Insertion sort</b> builds a sorted section by inserting each new item into place, and
            is efficient on nearly sorted data.</p>
            <p><b>Merge sort</b> splits the list in half, sorts each half and merges them; it is much
            faster on large lists.</p>
            <p>A single pass of bubble sort moves through the list comparing each adjacent pair once,
            swapping them if they are in the wrong order; after one full pass the largest unsorted value
            has "bubbled" to the end, but the rest of the list may still be unsorted and need further
            passes.</p>
            <p>Merge sort's advantage over bubble sort grows dramatically as lists get larger, because
            its time complexity increases much more slowly with input size &mdash; the difference is
            barely noticeable on small lists but becomes enormous on lists of millions of items.</p>
        """,
          ("After one full pass of bubble sort on [5, 1, 4, 2], the list becomes:",
           ("[1, 4, 2, 5]", "[1, 2, 4, 5]", "[5, 4, 2, 1]", "[1, 5, 4, 2]"), 0),
          ("Merge sort is generally preferred over bubble sort for very large lists because:",
           ("It uses less code", "Its time complexity grows much more slowly as the list gets bigger", "It doesn't need a computer", "It only works on numbers"), 1)),
        L(8, "Programming Basics", """
            <p>A variable is a named store whose value can change; a constant cannot.</p>
            <p>Common data types are integer, real/float, Boolean, character and string. Choosing the
            right type saves memory and prevents errors.</p>
            <p>Programs follow three basic constructs: sequence, selection and iteration.</p>
            <p>Storing a numeric value like age as a string rather than an integer is a common bug
            source: arithmetic operations such as adding 1 will not behave as expected on a string
            without first converting it to a numeric type, and comparisons may sort lexically ("10"
            before "9") rather than numerically.</p>
            <p>Integer division (often written <code>//</code>) divides and discards any remainder,
            which is different from normal division and is often the source of off-by-one style errors
            if a programmer forgets it truncates rather than rounds.</p>
        """,
          ("A program stores a person's age as a string instead of an integer. What problem could this cause?",
           ("No problem at all", "Arithmetic like age + 1 won't work correctly without conversion", "The string uses less memory", "It automatically becomes a float"), 1),
          ("Given x = 7 and y = 2, what is the result of x // y (integer division) in most languages?",
           ("3", "3.5", "4", "14"), 0)),
        L(9, "Selection and Iteration", """
            <p>Selection chooses a path: <code>if score &gt;= 50: print("Pass")</code>, optionally with
            elif and else branches.</p>
            <p>A <b>for</b> loop repeats a set number of times; a <b>while</b> loop repeats until a
            condition becomes false.</p>
            <p>A while loop whose condition never becomes false creates an infinite loop.</p>
            <p>Tracing a loop by hand &mdash; writing down the value of every variable after each
            iteration &mdash; is the surest way to predict its final result, especially when the range
            of a for loop or the update inside a while loop is not immediately obvious.</p>
            <p>A while loop's condition is checked <i>before</i> each iteration, including the very
            first one, so if the starting condition is already false the loop body never runs at all.</p>
        """,
          ("total = 0; for i in range(1, 5): total = total + i. What is the value of total after the loop?",
           ("4", "9", "10", "15"), 2),
          ("count = 10; while count > 0: count = count - 3. How many times does the loop body execute?",
           ("3", "4", "5", "10"), 1)),
        L(10, "Functions and Decomposition", """
            <p>Decomposition breaks a large problem into smaller sub-problems, each solved by a function.</p>
            <p>Functions take parameters and usually return a value, so the same code can be reused with
            different inputs.</p>
            <p>Local variables exist only inside a function; global variables are visible throughout the
            program and are best used sparingly.</p>
            <p>Functions can be nested inside one another's calls: the innermost function call is
            evaluated first, and its returned value is then passed into the outer function, exactly as
            in ordinary mathematical function notation like f(f(x)).</p>
            <p>Passing data between functions with parameters and return values, rather than relying on
            global variables, keeps each function self-contained and much easier to test, reuse and
            debug independently of the rest of the program.</p>
        """,
          ("A function is defined as: def square(n): return n * n. What does square(square(3)) return?",
           ("9", "18", "27", "81"), 3),
          ("A variable declared inside a function but needed in another function should best be:",
           ("Made global everywhere", "Passed as a parameter or returned as a value", "Deleted after use", "Renamed randomly"), 1)),
        L(11, "Data Structures", """
            <p>An array or list stores many values under one name, accessed by index starting at 0.</p>
            <p>A record (or dictionary) groups related fields of different types, such as a student's
            name, age and grade.</p>
            <p>A stack is last-in-first-out; a queue is first-in-first-out, used for printer jobs and
            scheduling.</p>
            <p>Because arrays are indexed from 0, an array holding n elements has valid indices from 0
            to n - 1; trying to access index n is a common "off-by-one" error that goes beyond the end
            of the array.</p>
            <p>Tracing stack and queue operations by hand &mdash; writing down the contents after each
            push/pop or enqueue/dequeue &mdash; makes their very different orderings clear: a stack
            always removes the most recently added item, while a queue always removes the item that has
            been waiting longest.</p>
        """,
          ("Items A, B, C are pushed onto a stack in that order, then two items are popped. Which item remains on the stack?",
           ("A", "B", "C", "None"), 0),
          ("In an array indexed from 0, an array has 8 elements. What is the index of the last element?",
           ("6", "7", "8", "9"), 1)),
        L(12, "Databases and SQL", """
            <p>A relational database stores data in tables of records and fields, linked by keys.</p>
            <p>A primary key uniquely identifies each record; a foreign key refers to a primary key in
            another table, avoiding duplicated data.</p>
            <p>SQL queries the data, e.g.
            <code>SELECT name FROM students WHERE grade &gt; 70;</code></p>
            <p>SQL statements follow a fixed clause order: <code>SELECT</code> the columns wanted,
            <code>FROM</code> the table, <code>WHERE</code> to filter rows, and <code>ORDER BY</code> to
            sort the result &mdash; writing clauses in the wrong order causes a syntax error.</p>
            <p>Splitting data across linked tables (such as Customers and Orders) rather than repeating
            customer details in every order avoids duplication and keeps the database consistent if a
            customer's details change; the link is made through a foreign key matching a primary key.</p>
        """,
          ("Which SQL statement would return only students with a grade above 80, sorted by name?",
           ("SELECT * FROM students ORDER BY name WHERE grade &gt; 80",
            "SELECT * FROM students WHERE grade &gt; 80 ORDER BY name",
            "SELECT students WHERE grade &gt; 80",
            "ORDER BY name SELECT * FROM students"), 1),
          ("A table Orders stores a CustomerID that matches the primary key in a Customers table. CustomerID in Orders is an example of a:",
           ("Primary key", "Foreign key", "Composite key", "Candidate key"), 1)),
        L(13, "Networks and the Internet", """
            <p>A LAN covers a small area such as a school; a WAN, like the internet, spans large
            distances.</p>
            <p>Devices follow protocols: TCP/IP for transferring data, HTTP/HTTPS for web pages.</p>
            <p>Data is split into packets that travel independently and are reassembled at the
            destination; DNS translates domain names into IP addresses.</p>
            <p>HTTPS adds encryption on top of the standard HTTP protocol, so data such as passwords or
            payment details cannot easily be read if intercepted in transit &mdash; this is why secure
            websites use HTTPS rather than plain HTTP.</p>
            <p>Splitting a message into packets, each labelled with its destination and position in the
            sequence, allows packets to take different routes across a busy network and still be
            reassembled correctly, making the network more resilient if part of it is congested or down.</p>
        """,
          ("A web page requests data from a server. Which protocol is typically used to transfer that page securely?",
           ("HTTP", "HTTPS", "SMTP", "DNS"), 1),
          ("Breaking a file into packets before sending it across a network mainly allows:",
           ("Packets to travel via different routes and be reassembled, improving reliability", "The file to be permanently deleted", "Only one device to use the network", "Data to be sent without an IP address"), 0)),
        L(14, "Cybersecurity", """
            <p>Threats include malware, phishing emails, brute-force attacks and social engineering that
            targets people rather than systems.</p>
            <p>Defences include strong unique passwords, two-factor authentication, firewalls, software
            updates and regular backups.</p>
            <p>Encryption scrambles data so that intercepting it is useless without the key.</p>
            <p>Two-factor authentication combines something the user knows (a password) with something
            they have (a code sent to a phone) or are (a fingerprint), so a stolen password alone is not
            enough for an attacker to log in.</p>
            <p>A brute-force attack differs from phishing in method, not goal: phishing tricks a person
            into handing over credentials, while brute force relies purely on a computer systematically
            trying enormous numbers of password combinations until one succeeds.</p>
        """,
          ("A company requires a password plus a code sent to your phone to log in. This is an example of:",
           ("Encryption", "Two-factor authentication", "A firewall", "A virus scan"), 1),
          ("A brute-force attack works by:",
           ("Tricking a user into revealing their password", "Systematically trying many possible passwords until one works", "Encrypting the user's files for ransom", "Intercepting network packets"), 1)),
        L(15, "Efficiency and Big-O", """
            <p>Two correct algorithms can differ hugely in speed, so we compare how work grows with
            input size n.</p>
            <p>Big-O notation captures this: O(1) is constant, O(log n) very efficient (binary search),
            O(n) linear, and O(n&sup2;) slow for large n (bubble sort).</p>
            <p>There is often a trade-off between time taken and memory used.</p>
            <p>An algorithm whose run time roughly doubles whenever the input size doubles has time
            complexity O(n) &mdash; a straight-line relationship between input size and work done; an
            algorithm whose run time increases by a factor of four when input doubles is O(n&sup2;)
            instead.</p>
            <p>For an O(n&sup2;) algorithm, increasing the input size by a factor of 100 increases the
            run time by a factor of 100&sup2; = 10,000, which is why algorithms with poor time
            complexity become impractical surprisingly quickly as data grows.</p>
        """,
          ("An algorithm's run time roughly doubles every time the input size doubles. Its time complexity is best described as:",
           ("O(1)", "O(log n)", "O(n)", "O(n&sup2;)"), 2),
          ("If an O(n&sup2;) algorithm takes 1 second for n = 1000, roughly how long would it take for n = 10,000 (100 times more input)?",
           ("About 10 seconds", "About 100 seconds", "About 1000 seconds", "Still about 1 second"), 1)),

        L(16, "Recursion and Recursive Algorithms", """
            <p>Recursion solves a problem by having a function call itself on a smaller instance of the same problem. A correct recursive algorithm needs a <b>base case</b> that stops further calls.</p>
            <p>For example, factorial can be defined as <code>n!=n(n-1)!</code> with <code>0!=1</code>. Each call reduces n until the base case is reached.</p>
            <p>Recursive calls use stack memory. Deep recursion can therefore consume significant memory and may cause a stack overflow if the base case is missing or the problem is reduced too slowly.</p>
            <p>Recursion is particularly natural for tree traversal, divide-and-conquer algorithms and problems that have self-similar structure.</p>
        """,
          ("What does a correct recursive factorial function need to prevent infinite calls?", ("A global variable", "A base case", "A network connection", "A sorting algorithm"), 1),
          ("If factorial(4) recursively calls factorial(3), factorial(2), factorial(1), and factorial(0), how many factorial function calls occur including factorial(4)?", ("3", "4", "5", "6"), 2)),
        L(17, "Trees and Binary Search Trees", """
            <p>A tree is a hierarchical data structure made of nodes connected by edges. The top node is the root, and nodes with no children are leaves.</p>
            <p>In a binary tree, each node has at most two children. A binary search tree maintains the ordering rule that values in the left subtree are smaller and values in the right subtree are larger, under the usual distinct-key assumption.</p>
            <p>An in-order traversal of a binary search tree visits keys in sorted order. Pre-order and post-order traversals are useful for different structural operations.</p>
            <p>Performance depends strongly on tree shape. A balanced search tree can support operations in roughly logarithmic time, while a highly skewed tree can degrade toward linear-time behaviour.</p>
        """,
          ("In a binary search tree containing distinct keys, an in-order traversal produces keys in:", ("Reverse insertion order", "Sorted ascending order", "Random order", "Level order only"), 1),
          ("A binary search tree containing n keys becomes completely skewed like a linked list. Search can then degrade to approximately:", ("O(1)", "O(log n)", "O(n)", "O(n&sup2;)"), 2)),
        L(18, "Heaps and Priority Queues", """
            <p>A heap is a complete binary tree satisfying a heap-order property. In a max-heap, every parent is at least as large as its children; in a min-heap, every parent is at most as large as its children.</p>
            <p>A heap is commonly stored in an array. With zero-based indexing, the children of index i are at <code>2i+1</code> and <code>2i+2</code> when those indices exist.</p>
            <p>Insertion and removal of the highest-priority item require restoring the heap property, typically in O(log n) time. Looking at the root gives the highest-priority item in O(1).</p>
            <p>Priority queues use heaps for scheduling, graph algorithms and event processing where the next item is selected according to priority rather than arrival time alone.</p>
        """,
          ("In a zero-based heap array, the children of index 4 are at indices:", ("5 and 6", "7 and 8", "8 and 9", "9 and 10"), 2),
          ("Which operation on a binary heap normally has O(log n) time in the worst case?", ("Read the root", "Insert an element", "Check the number of elements", "Access index 0"), 1)),
        L(19, "Graphs and Graph Representations", """
            <p>A graph consists of vertices and edges. Edges may be directed or undirected and may carry weights representing distance, cost, time or another quantity.</p>
            <p>An adjacency matrix stores whether or how strongly every pair of vertices is connected and uses O(V&sup2;) space. An adjacency list stores neighbours and is usually more space-efficient for sparse graphs.</p>
            <p>The degree of an undirected vertex is the number of incident edges. In a directed graph, in-degree counts incoming edges and out-degree counts outgoing edges.</p>
            <p>Graph representations affect algorithm performance, so choosing between a matrix and list depends on graph density and on whether the application needs fast edge lookup or efficient neighbour iteration.</p>
        """,
          ("A graph has 100 vertices and only 120 edges. Which representation is usually more space-efficient?", ("Adjacency matrix", "Adjacency list", "A full 100&times;100 table", "Both always use identical space"), 1),
          ("In a directed graph, a vertex has 3 incoming edges and 5 outgoing edges. Its total directed degree count is:", ("2", "5", "8", "15"), 2)),
        L(20, "Breadth-First and Depth-First Search", """
            <p>Breadth-first search (BFS) explores a graph layer by layer and is naturally implemented with a queue. In an unweighted graph, BFS can find the minimum number of edges from a source to reachable vertices.</p>
            <p>Depth-first search (DFS) explores as far as possible before backtracking and can be implemented with recursion or an explicit stack.</p>
            <p>Both BFS and DFS run in O(V+E) time when an adjacency-list representation is used, because each reachable vertex and edge is processed a bounded number of times.</p>
            <p>BFS is useful for shortest paths in unweighted networks, while DFS is useful for connectivity, cycle detection, topological reasoning and exploring hierarchical structures.</p>
        """,
          ("Which data structure naturally supports BFS traversal order?", ("Stack", "Queue", "Heap only", "Hash table"), 1),
          ("For an adjacency-list graph with V vertices and E edges, BFS has time complexity approximately:", ("O(V&sup2;E)", "O(V+E)", "O(log V)", "O(E&sup2;)"), 1)),
        L(21, "Shortest Paths", """
            <p>Shortest-path algorithms find minimum-cost routes from one vertex to another. The correct algorithm depends on whether edge weights can be negative and whether all-pairs distances are required.</p>
            <p>Dijkstra's algorithm repeatedly selects the unsettled vertex with the smallest tentative distance and relaxes its outgoing edges. It assumes edge weights are non-negative.</p>
            <p>Bellman-Ford can handle negative edge weights and can also detect reachable negative cycles. A negative cycle makes a finite shortest distance undefined for paths that can exploit the cycle repeatedly.</p>
            <p>For all-pairs shortest paths on smaller dense graphs, dynamic-programming approaches such as Floyd-Warshall can be appropriate.</p>
        """,
          ("Which condition is required for standard Dijkstra's algorithm to guarantee correct shortest paths?", ("All edges must have equal weight", "All edge weights must be non-negative", "The graph must be a tree", "There must be no vertices of degree 1"), 1),
          ("Which algorithm can detect a reachable negative-weight cycle while computing single-source shortest paths?", ("Binary search", "Bellman-Ford", "Merge sort", "Depth-first traversal only"), 1)),
        L(22, "Minimum Spanning Trees", """
            <p>A spanning tree connects every vertex of a connected undirected graph using exactly V-1 edges and contains no cycles. A minimum spanning tree (MST) has the smallest possible total edge weight among all spanning trees.</p>
            <p>Kruskal's algorithm sorts edges by weight and repeatedly adds the next edge that does not create a cycle. A disjoint-set structure can efficiently test whether two vertices are already connected.</p>
            <p>Prim's algorithm grows one tree outward by repeatedly choosing the cheapest edge that connects the current tree to a new vertex.</p>
            <p>MSTs are useful for infrastructure planning because they minimise total connection cost while keeping every required location connected, although an MST is not generally a shortest path between arbitrary pairs.</p>
        """,
          ("A spanning tree of a connected graph with 12 vertices must contain exactly how many edges?", ("10", "11", "12", "24"), 1),
          ("Kruskal's algorithm rejects an edge mainly when adding it would:", ("Increase the number of vertices", "Create a cycle", "Make the graph directed", "Reduce every edge weight"), 1)),
        L(23, "Hash Tables and Hash Functions", """
            <p>A hash table maps keys to positions using a hash function. The goal is to distribute keys across the table so that insert, search and delete are fast on average.</p>
            <p>A <b>collision</b> occurs when two different keys produce the same table index. Common collision strategies include separate chaining and open addressing.</p>
            <p>The load factor measures how full the table is. As the load factor rises, collisions usually become more frequent, so tables often resize before performance degrades severely.</p>
            <p>A good hash function should distribute typical inputs evenly and should be deterministic: the same key must produce the same hash value for the same table configuration.</p>
        """,
          ("Two different keys produce the same hash-table index. This situation is called a:", ("Recursion", "Collision", "Deadlock", "Traversal"), 1),
          ("If a hash table has 700 stored items and 1000 slots, its load factor is:", ("0.07", "0.3", "0.7", "7"), 2)),
        L(24, "Dynamic Programming", """
            <p>Dynamic programming solves problems with overlapping subproblems by storing solutions to smaller states instead of recomputing them repeatedly.</p>
            <p>A problem is suitable for dynamic programming when it has optimal substructure and overlapping subproblems. Solutions can be stored using memoisation from the top down or tabulation from the bottom up.</p>
            <p>The Fibonacci recurrence is a simple example: naive recursion repeatedly computes the same values, while memoisation reduces the number of calculations to linear in n.</p>
            <p>More advanced applications include shortest paths, sequence alignment, knapsack problems and resource allocation, where carefully defining the state is often the hardest conceptual step.</p>
        """,
          ("The main reason memoisation speeds up naive recursive Fibonacci is that it:", ("Sorts the input first", "Stores previously computed subproblem results", "Uses more recursive calls", "Removes the base case"), 1),
          ("A dynamic-programming solution changes a repeated O(2<sup>n</sup>) recurrence to O(n). For n=30, approximately how many times larger is 2<sup>n</sup> than n?", ("About 2", "About 30", "About 36 million", "About 1 billion"), 2)),
        L(25, "Greedy Algorithms", """
            <p>A greedy algorithm makes the best-looking local choice at each step. Greedy methods can be extremely efficient, but they are correct only for problems whose structure guarantees that local choices lead to a global optimum.</p>
            <p>Examples include Kruskal's and Prim's minimum-spanning-tree algorithms and certain interval-scheduling problems. The proof of correctness usually relies on an exchange argument or another structural property.</p>
            <p>A greedy strategy can fail for problems such as general coin change, where taking the largest available denomination first is not always optimal for an arbitrary set of denominations.</p>
            <p>Therefore, an attractive local rule is not enough. The algorithm must be supported by a correctness argument specific to the problem.</p>
        """,
          ("A greedy algorithm is guaranteed to be correct for a problem only when:", ("The local choice is intuitively large", "The problem has a property that makes the local choice safe", "The input is always sorted", "It uses recursion"), 1),
          ("For coin denominations {1,3,4} and target 6, choosing the largest coin first gives 4+1+1. The optimal solution uses:", ("2 coins", "3 coins", "4 coins", "6 coins"), 0)),
        L(26, "Object-Oriented Programming", """
            <p>Object-oriented programming organises software around objects that combine data and behaviour. A class defines the structure and operations that instances can use.</p>
            <p><b>Encapsulation</b> controls access to internal state, <b>inheritance</b> allows a class to reuse or extend another class, and <b>polymorphism</b> lets a common interface refer to objects with different implementations.</p>
            <p>Composition builds complex objects from other objects and is often preferable when a strict parent-child relationship is not conceptually appropriate.</p>
            <p>Good object-oriented design aims for clear responsibilities and low coupling, so changing one component does not force unrelated parts of the program to change.</p>
        """,
          ("A class defines a method draw(), and Circle and Square provide different implementations. Calling draw() through a common Shape reference demonstrates:", ("Encapsulation only", "Polymorphism", "Compilation", "Hashing"), 1),
          ("A Car object contains an Engine object as one of its components. This relationship is primarily an example of:", ("Composition", "Recursion", "Sorting", "Overloading only"), 0)),
        L(27, "Concurrency and Processes", """
            <p>A process is an executing program with its own address space and resources. Threads are execution paths within a process and can share the process's memory.</p>
            <p>Concurrency allows multiple tasks to make progress during overlapping periods. Parallelism is stronger: tasks actually execute simultaneously on multiple processing resources.</p>
            <p>Shared mutable data creates race conditions when the final result depends on the timing of operations. Synchronisation mechanisms such as locks can protect critical sections.</p>
            <p>Too much locking can reduce performance or cause deadlock if processes wait indefinitely for resources held by one another. Correct concurrent design therefore requires both safety and progress considerations.</p>
        """,
          ("Two threads increment the same shared counter without synchronisation. The final count may be wrong because of a:", ("Syntax error", "Race condition", "Compilation directive", "Cache hit"), 1),
          ("Which situation is most closely associated with deadlock?", ("Two tasks repeatedly finish early", "Tasks wait indefinitely for resources held by one another", "A program has no variables", "A loop executes once"), 1)),
        L(28, "Operating Systems and Memory Management", """
            <p>An operating system manages CPU time, memory, files, devices and processes. Virtual memory gives processes the illusion of a larger continuous address space by mapping virtual addresses to physical memory and, when necessary, secondary storage.</p>
            <p>Paging divides virtual memory into fixed-size pages and physical memory into frames. A page fault occurs when a needed page is not currently in physical memory and must be fetched.</p>
            <p>Frequent page faults can lead to <b>thrashing</b>, where the system spends more time moving pages than executing useful work.</p>
            <p>Memory protection prevents one process from arbitrarily accessing another process's private memory, improving reliability and security.</p>
        """,
          ("A page fault occurs when:", ("A CPU instruction is always invalid", "A required virtual-memory page is not currently in physical memory", "A hard disk has no files", "A process terminates normally"), 1),
          ("Thrashing is characterised by:", ("Very few memory transfers and high useful CPU work", "Excessive paging that leaves little time for useful computation", "Only network traffic", "A faster CPU clock"), 1)),
        L(29, "Compilers, Interpreters and Language Processing", """
            <p>A compiler translates source code into another form, often machine code or an intermediate representation, before execution. An interpreter executes source or an intermediate form through a runtime process.</p>
            <p>Language processing commonly includes lexical analysis, parsing, semantic checks, intermediate representation and optimisation before code generation.</p>
            <p>A parser checks whether tokens follow the grammar of the language and often builds a syntax tree. Semantic analysis then checks meaning-related constraints such as type compatibility.</p>
            <p>Modern systems frequently combine approaches: a language may compile to bytecode, execute it in a virtual machine and use just-in-time compilation to optimise frequently executed code at runtime.</p>
        """,
          ("Which compiler stage primarily determines whether tokens form a valid grammatical structure?", ("Lexical analysis", "Parsing", "Linking only", "Disk formatting"), 1),
          ("A just-in-time compiler typically improves performance by:", ("Deleting source code", "Compiling frequently executed code during program execution", "Removing all memory", "Disabling the CPU"), 1)),
        L(30, "Artificial Intelligence and Machine Learning Foundations", """
            <p>Artificial intelligence includes methods for building systems that perform tasks associated with perception, reasoning, decision-making or language. Machine learning is a subset in which models learn patterns from data rather than being programmed with every rule explicitly.</p>
            <p>In supervised learning, a model learns from labelled examples. In unsupervised learning, it searches for structure without target labels. Reinforcement learning uses rewards and penalties to learn actions through interaction with an environment.</p>
            <p>A model that performs extremely well on training data but poorly on unseen data may be <b>overfitting</b>. Techniques such as regularisation, validation and appropriate dataset splitting help measure and improve generalisation.</p>
            <p>Machine learning systems depend on data quality, feature representation, evaluation design and computational resources. A high training score alone does not establish that a model will perform reliably in real-world conditions.</p>
        """,
          ("A model has 99% training accuracy but 62% accuracy on unseen validation data. This pattern most strongly suggests:", ("Underfitting", "Overfitting", "Perfect generalisation", "No relationship to data"), 1),
          ("Which learning setting uses labelled input-output examples to learn a mapping?", ("Supervised learning", "Unsupervised learning", "Random search only", "Packet switching"), 0)),
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
            <p>Common symbols follow logical shapes: a battery is shown as long and short parallel
            lines, a resistor as a zigzag or rectangle, a switch as a break in the line, and a bulb as a
            circle with a cross inside it.</p>
            <p>If any part of the loop is broken &mdash; a switch left open, a wire disconnected, or a
            component failed &mdash; no current can flow anywhere in that loop, even in parts that
            appear undamaged.</p>
        """,
          ("In a circuit diagram, a component symbol shown as a zigzag line normally represents a:",
           ("Battery", "Resistor", "Capacitor", "Switch"), 1),
          ("Which of these is NOT essential for current to flow in a basic circuit?",
           ("A closed loop", "A source of potential difference", "A load or component", "A microcontroller"), 3)),
        L(2, "Voltage, Current and Resistance", """
            <p>Voltage is the electrical "push" that drives charge around a circuit, measured in volts.</p>
            <p>Current is the rate of flow of charge, measured in amperes; resistance opposes that flow,
            measured in ohms.</p>
            <p>Ohm's law ties the three together: <code>V = I &times; R</code>. Doubling the resistance
            while keeping voltage fixed halves the current.</p>
            <p>These three quantities can always be rearranged to find whichever one is unknown:
            <code>I = V/R</code> or <code>R = V/I</code>, and it helps to picture voltage as the cause,
            resistance as the obstacle, and current as the resulting effect.</p>
            <p>A useful way to remember the relationship is the "Ohm's law triangle": cover the quantity
            you want to find, and the triangle shows whether to multiply or divide the other two.</p>
        """,
          ("A component has 4 A flowing through it when 2 V is applied. Its resistance is:",
           ("0.5 &Omega;", "2 &Omega;", "6 &Omega;", "8 &Omega;"), 0),
          ("If the resistance of a component doubles while the current through it stays constant, the voltage across it must:",
           ("Halve", "Stay the same", "Double", "Become zero"), 2)),
        L(3, "Series and Parallel Circuits", """
            <p>In a <b>series</b> circuit there is one path: current is the same everywhere and the
            supply voltage is shared between components.</p>
            <p>In a <b>parallel</b> circuit there are branches: each branch gets the full supply voltage
            and the currents in the branches add up to the total.</p>
            <p>If one bulb fails in a series circuit the whole loop breaks; in a parallel circuit the
            other branches keep working.</p>
            <p>Because each branch of a parallel circuit is connected directly across the supply,
            identical bulbs in parallel are each just as bright as a single bulb connected alone &mdash;
            adding more parallel branches does not dim the existing ones, though it does draw more total
            current from the supply.</p>
            <p>In series, the supply voltage is shared between the components in proportion to their
            resistance, so a voltmeter placed across identical resistors in series will read an equal
            fraction of the total supply voltage across each one.</p>
        """,
          ("Three identical bulbs are connected in parallel across a 6 V battery. Compared with a single bulb on its own, each bulb in this circuit will be:",
           ("Dimmer, because voltage is shared", "The same brightness, because each gets the full 6 V", "Brighter, because current adds up", "Off, because parallel circuits don't work"), 1),
          ("Two identical resistors are connected in series across a battery. If a voltmeter reads 3 V across one resistor, the battery's voltage is:",
           ("1.5 V", "3 V", "6 V", "9 V"), 2)),
        L(4, "Resistors and Resistor Networks", """
            <p>A resistor limits current flow and is often used to protect other components or set a
            precise voltage or current.</p>
            <p>Resistors in series add directly: <code>R_total = R1 + R2</code>. Resistors in parallel
            combine so the total is always less than the smallest individual resistor.</p>
            <p>Colour bands printed on a resistor's body encode its resistance value and tolerance.</p>
            <p>For two resistors in parallel there is a shortcut formula,
            <code>R_total = (R1 &times; R2) / (R1 + R2)</code>, which gives the same result as adding
            the reciprocals but is often quicker for just two resistors.</p>
            <p>Reading colour bands relies on a fixed digit-colour code (black=0, brown=1, red=2, and so
            on): the first two bands give significant digits, the third gives a multiplier, and a fourth
            band shows the tolerance (how accurate the stated value is).</p>
        """,
          ("A 4 &Omega; and a 12 &Omega; resistor are connected in parallel. Their combined resistance is closest to:",
           ("3 &Omega;", "8 &Omega;", "12 &Omega;", "16 &Omega;"), 0),
          ("A resistor has colour bands red-red-orange, where red = 2 and orange means &times;1000. Its resistance is:",
           ("22 &Omega;", "220 &Omega;", "2200 &Omega;", "22000 &Omega;"), 3)),
        L(5, "Capacitors", """
            <p>A capacitor stores electrical charge on two conductive plates separated by an insulator,
            measured in farads.</p>
            <p>It charges up when connected to a supply and discharges when the supply is removed,
            smoothing out voltage changes.</p>
            <p>Capacitors are used for smoothing power supplies, timing circuits and filtering unwanted
            signal noise.</p>
            <p>Charging (and discharging) is not instant: it happens through whatever resistance is in
            the circuit, so a larger resistor in series with the capacitor slows the process down,
            giving a longer charging time for the same capacitor.</p>
            <p>In a power supply, after a rectifier converts AC to a bumpy DC output, a smoothing
            capacitor charges near each peak and slowly discharges between peaks, reducing the "ripple"
            and producing a much steadier DC voltage.</p>
        """,
          ("A capacitor is charged through a resistor. Increasing the resistance will:",
           ("Make it charge faster", "Make it charge more slowly", "Not affect charging time", "Discharge it instantly"), 1),
          ("In a smoothing circuit after a rectifier, a capacitor mainly reduces:",
           ("The average voltage to zero", "Ripple in the DC output", "The current to zero", "The frequency of the AC input"), 1)),
        L(6, "Diodes and Rectification", """
            <p>A diode allows current to flow in only one direction, acting like a one-way valve for
            electricity.</p>
            <p>A light-emitting diode (LED) also gives off light when current passes through it in the
            correct direction, and needs a resistor in series to limit current.</p>
            <p>Rectification uses diodes to convert alternating current (AC), which reverses direction,
            into direct current (DC), which flows one way.</p>
            <p>An LED's series resistor protects it from too much current: without it, the very low
            resistance of the LED itself would let a large current flow and quickly destroy it, since
            LEDs (unlike ordinary resistors) do not limit current in proportion to voltage in a simple
            way.</p>
            <p>A single diode rectifier only makes use of half of each AC cycle, blocking the other
            half entirely; a bridge rectifier of four diodes redirects both halves of the cycle in the
            same direction, giving a smoother, more efficient DC output before any smoothing capacitor
            is even added.</p>
        """,
          ("An LED requires a series resistor mainly to:",
           ("Increase the light output", "Limit the current and prevent damage", "Reverse the current direction", "Store charge"), 1),
          ("A bridge rectifier made of four diodes is used to convert AC into DC. Compared with using a single diode, a bridge rectifier:",
           ("Blocks all current", "Uses both halves of the AC cycle, giving a smoother output", "Only works with DC input", "Removes the need for a capacitor entirely"), 1)),
        L(7, "Transistors as Switches", """
            <p>A transistor is a semiconductor device that can act as an electronic switch or an
            amplifier.</p>
            <p>A small current or voltage at the base (or gate) controls a much larger current flowing
            between the other two terminals.</p>
            <p>This lets a low-power signal, such as from a sensor, switch a high-power output like a
            motor or lamp.</p>
            <p>Whether the transistor is "on" or "off" depends on the voltage or current reaching its
            base: below a certain threshold it stays off (no current flows through the main path), and
            above that threshold it switches fully on, behaving almost like a closed switch.</p>
            <p>In a light-sensing circuit, an LDR and fixed resistor set the voltage reaching the
            transistor's base; because an LDR's resistance rises in the dark, that darkness-driven
            voltage change is what switches the transistor, and therefore a connected lamp, on or off.</p>
        """,
          ("In a simple transistor switching circuit, a small base current controls a much larger current flowing between the collector and emitter. This is an example of:",
           ("Rectification", "Amplification or switching action", "Capacitance", "Insulation"), 1),
          ("A light sensor circuit uses a transistor to switch on a lamp in the dark. As light falls, the LDR's resistance rises, which:",
           ("Decreases the voltage at the base, turning the transistor off", "Increases the voltage at the base, turning the transistor on", "Has no effect on the transistor", "Destroys the transistor"), 1)),
        L(8, "Logic Gates", """
            <p>Logic gates perform simple decisions on digital signals that are either HIGH (1) or LOW
            (0).</p>
            <p>An <b>AND</b> gate outputs 1 only when all its inputs are 1; an <b>OR</b> gate outputs 1
            when at least one input is 1; a <b>NOT</b> gate simply inverts its input.</p>
            <p>Combining a handful of basic gates can build circuits that add numbers or make complex
            decisions.</p>
            <p>When gates are chained together, the output of one becomes the input of the next, so a
            circuit must be evaluated in order: work out the result of the first gate using the given
            inputs, then feed that result into the following gate to find the final output.</p>
            <p>Tracing backwards from a required output is just as useful as tracing forwards: to make
            an OR gate followed by a NOT gate output 1 overall, the OR gate itself must output 0, which
            is only possible when every one of its inputs is 0.</p>
        """,
          ("A circuit has inputs A and B combined first by an AND gate, and that output is then fed into a NOT gate. If A = 1 and B = 1, the final output is:",
           ("0", "1", "Depends on B", "Undefined"), 0),
          ("Which combination of inputs makes a 2-input OR gate followed by a NOT gate output 1?",
           ("A = 0, B = 0", "A = 1, B = 0", "A = 0, B = 1", "A = 1, B = 1"), 0)),
        L(9, "Boolean Algebra and Truth Tables", """
            <p>Boolean algebra describes logic using only two values, true and false (1 and 0), and
            operators such as AND, OR and NOT.</p>
            <p>A truth table lists every possible combination of inputs alongside the resulting output,
            making a gate's behaviour easy to check.</p>
            <p>Combining gates, such as AND followed by NOT (a NAND gate), can build any other logic
            function.</p>
            <p>The number of rows a complete truth table needs is always <code>2&#8319;</code>, where n
            is the number of inputs, since every input can independently be either 0 or 1 and every
            combination must be listed exactly once.</p>
            <p>NAND (AND then NOT) and NOR (OR then NOT) gates are especially important because either
            one, used repeatedly, is enough on its own to build any other logic gate &mdash; a property
            that real digital chips take advantage of.</p>
        """,
          ("For a 3-input AND gate, how many rows does its complete truth table have?",
           ("3", "6", "8", "9"), 2),
          ("A NOR gate is equivalent to which combination of gates?",
           ("AND then NOT", "OR then NOT", "NOT then AND", "XOR then NOT"), 1)),
        L(10, "Digital vs Analogue Signals", """
            <p>An <b>analogue</b> signal varies smoothly and continuously, like the volume from a
            microphone.</p>
            <p>A <b>digital</b> signal has only discrete levels, usually just HIGH and LOW, making it
            more resistant to noise and easier to process.</p>
            <p>An analogue-to-digital converter (ADC) samples an analogue signal at intervals and
            represents each sample as a binary number.</p>
            <p>An ADC's resolution depends on how many bits it uses per sample: an n-bit ADC can
            represent <code>2&#8319;</code> distinct voltage levels, so more bits give a finer, more
            accurate digital approximation of the original analogue signal.</p>
            <p>Digital signals resist noise well because a receiving circuit only needs to decide
            whether a signal is closer to HIGH or LOW; small variations in voltage caused by
            interference rarely change that decision, unlike an analogue signal where any such variation
            directly distorts the information carried.</p>
        """,
          ("An 8-bit ADC can represent how many distinct voltage levels?",
           ("8", "16", "128", "256"), 3),
          ("A key reason digital signals are more resistant to noise than analogue signals is that:",
           ("Digital signals travel faster", "Small variations don't change whether a signal reads as a 0 or 1", "Digital signals use higher voltages always", "Analogue signals cannot be amplified"), 1)),
        L(11, "Sensors and Input Devices", """
            <p>Sensors convert a physical quantity, such as light, temperature or pressure, into an
            electrical signal a circuit can process.</p>
            <p>A light-dependent resistor (LDR) lowers its resistance as light increases; a thermistor's
            resistance changes with temperature.</p>
            <p>These are often used with a voltage divider so their changing resistance produces a
            changing voltage a circuit can read.</p>
            <p>In a voltage-divider circuit, the voltage across each resistor is a fraction of the
            supply voltage set by the ratio of resistances, so as one resistor's resistance falls, the
            voltage across the <i>other</i>, fixed resistor rises correspondingly.</p>
            <p>Most temperature sensors used in simple circuits are <b>NTC</b> (negative temperature
            coefficient) thermistors, whose resistance falls as temperature rises &mdash; the opposite
            relationship to an ordinary metal conductor, whose resistance typically rises with
            temperature.</p>
        """,
          ("In a voltage-divider circuit with an LDR on top and a fixed resistor on the bottom, as light level increases (LDR resistance falls), the voltage across the fixed resistor:",
           ("Increases", "Decreases", "Stays the same", "Becomes zero"), 0),
          ("A thermistor is used to trigger a cooling fan when temperature rises. As temperature increases, a typical (NTC) thermistor's resistance:",
           ("Increases", "Decreases", "Stays constant", "Becomes infinite"), 1)),
        L(12, "Output Devices and Actuators", """
            <p>Output devices convert an electrical signal into a useful physical effect: LEDs produce
            light, buzzers produce sound, and motors produce movement.</p>
            <p>A relay uses a small control current to switch a separate, often much higher-power,
            circuit on or off, keeping the two electrically isolated.</p>
            <p>Motors and other high-current outputs are usually driven through a transistor or relay
            rather than directly from a microcontroller pin.</p>
            <p>A microcontroller pin can typically only supply a very small current, far less than most
            motors need to run, so connecting a motor directly to a pin risks damaging the
            microcontroller; the transistor or relay instead uses the pin's small signal to control a
            separate, adequately rated power supply for the motor.</p>
            <p>A relay's key advantage over a transistor in many designs is electrical isolation: the
            control circuit and the switched circuit are not directly connected, which is valuable when
            switching mains-voltage or otherwise higher-risk circuits from low-voltage electronics.</p>
        """,
          ("A microcontroller pin can only supply a small current, but a project needs to switch on a 2 A motor. The best approach is to:",
           ("Connect the motor directly to the pin", "Use a transistor or relay driven by the pin to switch the motor's separate power supply", "Increase the pin's voltage", "Remove the motor's power supply"), 1),
          ("A relay is chosen over a transistor in some designs mainly because a relay:",
           ("Is always faster switching", "Provides electrical isolation between control and load circuits", "Cannot handle AC", "Needs no power to switch"), 1)),
        L(13, "Power Supplies and Batteries", """
            <p>Batteries store chemical energy and release it as direct current (DC) at a roughly
            constant voltage until they run low.</p>
            <p>Connecting cells in series increases total voltage; connecting them in parallel increases
            available current (capacity) while keeping voltage the same.</p>
            <p>Mains electricity is alternating current (AC) and must usually be transformed and
            rectified before it can power DC circuits and electronics.</p>
            <p>The total EMF of cells connected in series is simply the sum of the individual cell
            voltages, so four 1.5 V cells in series provide 6 V &mdash; this is exactly how multi-cell
            battery packs reach higher voltages than a single cell could supply.</p>
            <p>Connecting identical cells in parallel instead keeps the voltage the same as a single
            cell, but the combined capacity (often measured in mAh, milliamp-hours) adds up, allowing
            the combination to supply current for longer before running down.</p>
        """,
          ("Four 1.5 V cells are connected in series. The total EMF supplied is:",
           ("1.5 V", "3 V", "4.5 V", "6 V"), 3),
          ("Two identical batteries rated 1.5 V, 2000 mAh are connected in parallel. The combined arrangement provides:",
           ("3 V, 2000 mAh", "1.5 V, 4000 mAh", "1.5 V, 2000 mAh", "3 V, 4000 mAh"), 1)),
        L(14, "Printed Circuit Boards and Prototyping", """
            <p>A breadboard lets components be connected temporarily without soldering, ideal for
            testing and prototyping a design.</p>
            <p>A printed circuit board (PCB) has copper tracks etched onto an insulating board, giving a
            permanent, compact and reliable connection between components.</p>
            <p>Moving from breadboard to PCB usually happens once a design has been tested and is ready
            for a final, durable version.</p>
            <p>Breadboard connections rely on spring contacts that can work loose with vibration or
            movement, which makes a breadboard unsuitable for a final product that must survive being
            moved, dropped or used in a vehicle; a soldered PCB provides permanent, mechanically robust
            connections instead.</p>
            <p>A stray blob of solder bridging two tracks that should not be connected creates an
            unintended <b>short circuit</b>, which can cause components to behave unpredictably or be
            damaged, and is one of the most common faults to check for when a finished PCB does not work.</p>
        """,
          ("A student's breadboard prototype works, but the final product needs to survive vibration in a moving vehicle. The best next step is usually to:",
           ("Leave it on the breadboard", "Transfer the design to a soldered PCB", "Add more breadboard wires", "Remove all resistors"), 1),
          ("On a PCB, two copper tracks that should not be electrically connected but are joined by a stray blob of solder create a:",
           ("Open circuit", "Short circuit", "Perfect connection", "Capacitor"), 1)),
        L(15, "Microcontrollers and Embedded Systems", """
            <p>A microcontroller is a small computer on a single chip, containing a processor, memory
            and input/output pins, used to control a specific device.</p>
            <p>An embedded system is any computer system built into a larger product, such as a washing
            machine or a car, rather than a general-purpose computer.</p>
            <p>Microcontrollers are typically programmed once and then repeatedly read sensors, make
            decisions, and drive outputs in a continuous loop.</p>
            <p>A system that reads a sensor and uses that reading to decide how to control an output is
            called a <b>closed-loop</b> (feedback) control system, since the output's effect on the
            environment is continuously fed back in through the sensor to adjust future behaviour &mdash;
            unlike an open-loop system, which simply runs a fixed sequence regardless of conditions.</p>
            <p>Compared with a general-purpose computer, a microcontroller is usually far cheaper,
            smaller and less powerful, but is optimised and dedicated to running one specific repeated
            task extremely reliably, often for years without needing attention.</p>
        """,
          ("A microcontroller-based plant-watering system reads a soil moisture sensor and turns on a pump when the soil is dry. This is an example of:",
           ("Open-loop control with no feedback", "A closed-loop control system using sensor feedback", "A purely analogue system", "A system with no output device"), 1),
          ("Compared with a general-purpose desktop computer, a microcontroller used in an embedded system is typically:",
           ("More powerful but less specialised", "Smaller, cheaper, and dedicated to a specific repeated task", "Incapable of running any program", "Only usable with a keyboard and monitor"), 1)),

    L(16, "Operational Amplifiers", """
        <p>An operational amplifier, or op-amp, is a high-gain differential amplifier with two inputs and an output. In ideal analysis, input current is treated as zero and negative feedback forces the input voltages to be approximately equal in linear operation.</p>
        <p>Inverting and non-inverting amplifier configurations use resistors to set predictable voltage gains. For an inverting amplifier, the ideal gain is <code>A<sub>v</sub>=-R<sub>f</sub>/R<sub>in</sub></code>.</p>
        <p>The output cannot exceed the available supply rails, so a real op-amp saturates if the required output voltage is too large. Real devices also have finite bandwidth, input offset and limited slew rate.</p>
        <p>Op-amps are used for amplification, buffering, filtering, comparison and signal conditioning before data is processed or converted.</p>
    """,
      ("An ideal inverting op-amp has R<sub>in</sub>=10 k&Omega; and R<sub>f</sub>=50 k&Omega;. For an input of 0.2 V, the output is:", ("+1 V", "-1 V", "+5 V", "-5 V"), 1),
      ("The ideal op-amp assumption that input current is approximately zero implies that:", ("Input terminals behave like short circuits for current", "The output current is always zero", "No voltage can appear at the output", "The power supply is unnecessary"), 0)),
    L(17, "Analog-to-Digital Conversion", """
        <p>An ADC converts a continuous analogue voltage into a digital code. An n-bit ideal ADC provides <code>2<sup>n</sup></code> possible codes across its input range.</p>
        <p>Quantisation divides the analogue range into discrete levels. The quantisation step becomes smaller as the number of bits increases, reducing quantisation error under the same input range.</p>
        <p>The sampling rate must be high enough to capture changes in the input. According to the Nyquist criterion, a band-limited signal with maximum frequency f<sub>max</sub> requires a sampling frequency greater than 2f<sub>max</sub> to avoid ideal aliasing.</p>
        <p>Practical ADC systems also have reference-voltage limits, nonlinearity, noise and finite acquisition time, so resolution is only one part of conversion quality.</p>
    """,
      ("An ideal 10-bit ADC has how many possible output codes?", ("512", "1000", "1024", "2048"), 2),
      ("A signal contains frequencies up to 8 kHz. Ignoring practical margins, the minimum sampling frequency required by the Nyquist criterion is:", ("4 kHz", "8 kHz", "12 kHz", "16 kHz"), 3)),
    L(18, "Digital-to-Analog Conversion", """
        <p>A DAC converts a digital code into an analogue voltage or current. Common architectures include binary-weighted resistor networks and R-2R ladders.</p>
        <p>For an ideal n-bit unipolar DAC with reference V<sub>ref</sub>, the output has discrete levels. The smallest change between adjacent ideal codes is approximately V<sub>ref</sub>/(2<sup>n</sup>-1) when the full-scale code corresponds to V<sub>ref</sub>.</p>
        <p>DAC performance depends on resolution, monotonicity, settling time, offset, gain error and linearity. A higher resolution does not automatically eliminate dynamic errors.</p>
        <p>DACs are used to generate control voltages, audio signals, waveforms and analogue actuator commands from digital systems.</p>
    """,
      ("An ideal 8-bit DAC spans 0 to 5 V with code 255 at 5 V. Approximately what voltage corresponds to code 128?", ("0.98 V", "2.51 V", "3.14 V", "5 V"), 1),
      ("Increasing DAC resolution from 8 bits to 10 bits increases the number of discrete output codes by a factor of:", ("2", "4", "8", "10"), 1)),
    L(19, "Filters and Frequency Response", """
        <p>A filter changes the amplitude and sometimes phase of signals according to frequency. A low-pass filter passes lower frequencies and attenuates higher ones, while a high-pass filter does the opposite.</p>
        <p>A first-order RC low-pass filter has cutoff frequency <code>f<sub>c</sub>=1/(2&pi;RC)</code>. At the cutoff frequency, the magnitude is approximately 0.707 of the passband value for an ideal first-order filter.</p>
        <p>Filters can be implemented with passive components or active circuits such as op-amp filters. Higher-order filters generally provide steeper attenuation outside the passband.</p>
        <p>Real signal chains use filters to reduce noise, prevent aliasing before ADC conversion and isolate frequency bands of interest.</p>
    """,
      ("For an RC low-pass filter with R=10 k&Omega; and C=10 nF, the cutoff frequency is closest to:", ("159 Hz", "1.59 kHz", "15.9 kHz", "159 kHz"), 1),
      ("A low-pass filter is most appropriate for removing:", ("A slowly varying signal", "High-frequency noise from a slowly varying measurement", "All DC content", "Every frequency equally"), 1)),
    L(20, "Diode Applications and Voltage Regulation", """
        <p>Diodes conduct strongly in one direction and block current in the other under normal operation. Beyond simple rectification, diodes can protect circuits, clamp voltages and regulate voltage.</p>
        <p>A Zener diode is designed to operate in reverse breakdown over a specified region, allowing it to maintain an approximately constant voltage when used with an appropriate current-limiting resistor.</p>
        <p>Flyback diodes are placed across inductive loads such as relay coils to provide a safe path for stored magnetic energy when the driving current is switched off.</p>
        <p>LEDs emit light when forward biased and require current limiting. Different semiconductor materials produce different forward voltages and wavelengths.</p>
    """,
      ("A relay coil is switched off suddenly. Why is a flyback diode placed across the coil?", ("To increase the coil resistance permanently", "To provide a path for the inductive current and limit the voltage spike", "To reverse the battery polarity", "To eliminate magnetic fields"), 1),
      ("A Zener regulator is supplied through a resistor mainly to:", ("Increase breakdown voltage indefinitely", "Limit current so the Zener can operate safely in its regulation region", "Remove the load", "Make the diode conduct only forward"), 1)),
    L(21, "BJT Transistors", """
        <p>A bipolar junction transistor has three terminals: emitter, base and collector. In active operation, a small base current controls a larger collector current, giving current amplification.</p>
        <p>For a simplified common-emitter model, <code>I<sub>C</sub>&asymp;&beta;I<sub>B</sub></code>. Real transistors depart from this ideal relation, especially near cutoff and saturation.</p>
        <p>In switching applications, the transistor is driven between cutoff and saturation. In amplifier applications it is biased in a region where changes in input produce controlled changes in collector current.</p>
        <p>Biasing establishes a suitable operating point so that an amplifier can handle an input signal without excessive clipping or distortion.</p>
    """,
      ("A BJT has &beta;=100 and base current 40 &micro;A in its active region. The approximate collector current is:", ("0.04 mA", "0.4 mA", "4 mA", "40 mA"), 2),
      ("A transistor used as a digital switch is normally driven between:", ("Active and active only", "Cutoff and saturation", "Breakdown and avalanche only", "Two reverse-bias states"), 1)),
    L(22, "MOSFETs and CMOS Logic", """
        <p>A MOSFET controls current using an electric field at an insulated gate. Because the gate is insulated, steady-state gate current is ideally near zero, although charging and discharging the gate capacitance still requires transient current.</p>
        <p>Enhancement-mode MOSFETs are commonly used as switches. An NMOS conducts when the gate-to-source voltage exceeds its threshold by an appropriate amount, while PMOS operation uses the complementary polarity.</p>
        <p>CMOS logic combines NMOS and PMOS devices so that ideally one network pulls the output high while the other pulls it low. Static power consumption is therefore low except for leakage and switching-related effects.</p>
        <p>Switching speed is influenced by capacitance, transistor drive strength and load. Faster transitions generally require charging and discharging capacitive loads more rapidly.</p>
    """,
      ("The very small steady-state gate current of an ideal MOSFET is mainly due to the gate being:", ("Directly shorted to the channel", "Insulated from the channel by a dielectric", "Made of a perfect conductor to ground", "Connected only through a resistor"), 1),
      ("A CMOS inverter output is pulled high when the:", ("NMOS network alone is conducting strongly", "PMOS pull-up network provides the active path while NMOS is off", "Both transistors must always be fully on", "Power supply is disconnected"), 1)),
    L(23, "Digital Counters and Registers", """
        <p>A register stores a group of binary bits using flip-flops. Counters are sequential circuits that move through a defined sequence of states on clock edges.</p>
        <p>A binary counter can represent 2<sup>n</sup> states with n flip-flops before repeating. The state sequence can be used to divide clock frequency because a selected bit toggles at a predictable fraction of the input frequency.</p>
        <p>Registers can be parallel-in/parallel-out, serial-in/serial-out or other configurations depending on how data enters and leaves the circuit.</p>
        <p>Setup and hold timing constraints matter because flip-flops must sample stable input data around the active clock edge to avoid unreliable behaviour.</p>
    """,
      ("How many distinct states can an ideal 4-bit binary counter represent before repeating?", ("4", "8", "16", "32"), 2),
      ("A 16 MHz clock drives a binary divider where one output toggles at f/2<sup>4</sup>. What is that output frequency?", ("1 MHz", "2 MHz", "4 MHz", "8 MHz"), 1)),
    L(24, "Timers, PWM and Motor Control", """
        <p>Pulse-width modulation represents an analogue-like control level using a digital signal that switches rapidly between high and low states. The <b>duty cycle</b> is the fraction of one period for which the signal is high.</p>
        <p>For an ideal 0 to V supply, the average voltage of a sufficiently fast PWM waveform is approximately <code>V<sub>avg</sub>=D V</code>, where D is the duty cycle expressed as a fraction.</p>
        <p>PWM is widely used for LED brightness, DC motor speed control and power conversion. Motors do not instantly respond to each pulse because their mechanical inertia and electrical inductance smooth the effect.</p>
        <p>A timer peripheral can generate precise PWM waveforms without the CPU manually toggling a pin at every edge, leaving processor time for other tasks.</p>
    """,
      ("A 12 V PWM signal has a duty cycle of 25%. Its ideal average voltage is approximately:", ("1.5 V", "3 V", "6 V", "9 V"), 1),
      ("Increasing PWM frequency while keeping duty cycle constant generally changes the ideal average voltage by:", ("Doubling it", "Halving it", "Leaving it approximately unchanged", "Making it zero"), 2)),
    L(25, "Serial Communication Protocols", """
        <p>Serial communication sends bits sequentially rather than presenting an entire word on separate wires. UART, SPI and I2C are common embedded interfaces with different trade-offs.</p>
        <p>UART is commonly asynchronous and uses agreed baud rates and framing bits. SPI typically uses a clock and separate data lines and can communicate at high speed over short distances.</p>
        <p>I2C uses two main lines, SDA and SCL, and supports multiple addressed devices on a shared bus. Devices use pull-up resistors because the common bus lines are typically driven in an open-drain/open-collector style.</p>
        <p>Protocol selection depends on speed, wiring, number of devices, distance, addressing needs and software complexity.</p>
    """,
      ("Which interface normally uses SDA and SCL as its two main bus signals?", ("UART", "SPI", "I2C", "USB audio only"), 2),
      ("A UART link is configured for 9600 baud. Ignoring framing overhead, approximately how many bits can be transmitted in 0.5 s?", ("480", "960", "4800", "9600"), 2)),
    L(26, "Embedded C and Real-Time Systems", """
        <p>Embedded software often interacts directly with hardware registers, interrupts, timers and memory-mapped peripherals. C is widely used because it offers low-level control with relatively small runtime overhead.</p>
        <p>An interrupt allows hardware or software events to request CPU attention without continuously polling. The interrupt service routine should normally be short and deterministic, with lengthy work deferred to the main program or a task system.</p>
        <p>A real-time system is concerned not only with producing the correct result but also with producing it within specified timing constraints. Missing a deadline can be a functional failure in a hard real-time system.</p>
        <p>Careful use of volatile variables, atomic operations and concurrency control is important when data can change asynchronously or be shared between interrupt handlers and normal code.</p>
    """,
      ("Why might a hardware register accessed by both normal code and an interrupt handler be declared volatile in C?", ("To force it into a graphics card", "To prevent the compiler from assuming its value never changes unexpectedly", "To encrypt the register", "To make it constant forever"), 1),
      ("A hard real-time control task has a 5 ms deadline but sometimes completes in 7 ms. The key problem is:", ("Numerical precision only", "A missed timing deadline", "Excessive screen resolution", "Too few variables"), 1)),
    L(27, "Signal Conditioning and Instrumentation", """
        <p>Sensor outputs often need amplification, filtering, level shifting and protection before conversion by an ADC. The goal is to preserve useful information while reducing noise and preventing the interface from exceeding safe limits.</p>
        <p>Instrumentation amplifiers are designed for accurate amplification of small differential signals while rejecting common-mode voltage. Their performance is described using parameters such as gain, input impedance and common-mode rejection ratio.</p>
        <p>Grounding, shielding and cable routing can strongly affect low-level measurements because electromagnetic interference can be comparable to the signal being measured.</p>
        <p>A complete measurement chain therefore includes the sensor, analogue conditioning, ADC, digital processing and calibration rather than treating the sensor output as an ideal number.</p>
    """,
      ("A differential sensor produces 2.01 V and 2.00 V on two leads while both have a large common 1 V interference component. A high CMRR amplifier is useful mainly because it:", ("Amplifies only the common-mode signal", "Rejects common-mode voltage while amplifying the differential signal", "Removes the sensor completely", "Converts the signal directly to binary without an ADC"), 1),
      ("If an ADC input must never exceed 3.3 V but a sensor can output 0 to 5 V, a suitable interface should primarily:", ("Connect it directly", "Use appropriate scaling or protection so the ADC input remains within its allowed range", "Increase ADC voltage indefinitely", "Remove all filtering"), 1)),
    L(28, "Control Systems and Feedback", """
        <p>An open-loop system applies a control action without measuring the result. A closed-loop system measures an output and uses the difference between desired and measured values to adjust control.</p>
        <p>A simple feedback controller may use proportional action, where the control signal is related to the error. Integral action accumulates error over time, while derivative action responds to the rate of change of error.</p>
        <p>Feedback can improve accuracy and reject disturbances, but poor controller tuning can produce overshoot, oscillation or instability.</p>
        <p>Embedded controllers combine sensors, computation and actuators to regulate temperature, speed, position, pressure and many other physical variables.</p>
    """,
      ("A temperature controller increases heater power when measured temperature falls below the setpoint. This is an example of:", ("Open-loop control only", "Closed-loop feedback control", "No control system", "Purely mechanical storage"), 1),
      ("A controller that accumulates error over time is using which action?", ("Proportional", "Integral", "Derivative", "Sampling only"), 1)),
    L(29, "RF and Wireless Communication", """
        <p>Radio communication uses electromagnetic waves to carry information through space. A transmitter generates and modulates a carrier, while a receiver filters, demodulates and processes the received signal.</p>
        <p>Amplitude modulation varies carrier amplitude, while frequency modulation varies carrier frequency. Digital systems can use modulation schemes such as PSK, FSK and QAM to represent symbols.</p>
        <p>Free-space received power generally decreases strongly with distance because the wave spreads over a larger area. Antennas, frequency, bandwidth and propagation conditions all affect link performance.</p>
        <p>Noise and interference limit reliable communication. Signal-to-noise ratio, bandwidth and modulation choices therefore have to be considered together rather than optimising only one parameter.</p>
    """,
      ("In frequency modulation, the information signal primarily changes the carrier's:", ("Amplitude", "Frequency", "Mass", "Propagation speed in vacuum"), 1),
      ("If received signal power is 100 mW and noise power is 1 mW, the signal-to-noise ratio in linear form is:", ("0.01", "1", "10", "100"), 3)),
    L(30, "Embedded System Design and IoT Architecture", """
        <p>An embedded IoT system commonly contains sensors, a microcontroller, communication hardware, software and a power source. Data may be processed locally or transmitted to another device or cloud service.</p>
        <p>Edge processing can reduce latency and communication bandwidth by extracting useful information near the sensor. Cloud processing can provide large-scale storage, analytics and remote access.</p>
        <p>Reliable systems must consider power consumption, communication loss, security, firmware updates, sensor calibration and failure handling. A device that works only under ideal conditions is not a complete engineering solution.</p>
        <p>Security should be designed from the beginning using authenticated communication, protected credentials, least-privilege access and secure update mechanisms rather than added after deployment.</p>
    """,
      ("A battery-powered sensor node sends raw data continuously to a cloud server even though only one-minute averages are needed. Which change can most directly reduce communication energy?", ("Increase transmission frequency", "Compute one-minute averages locally and transmit only summaries", "Disable all sensing", "Increase packet size without processing"), 1),
      ("An IoT device receives firmware updates. Which mechanism most directly helps prevent an attacker from installing an unauthorised firmware image?", ("Unsigned updates", "Cryptographic verification of signed firmware", "Disabling version numbers", "Using a longer sensor cable"), 1)),
    ],
}
