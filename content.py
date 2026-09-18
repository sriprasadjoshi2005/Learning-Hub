"""
Learning Hub — structured lesson and quiz content.

Each subject contains 20 lessons progressing from foundations to advanced applications.
Each lesson contains exactly 5 quiz questions: 2 easy, 2 moderate, and 1 difficult.
The quiz answer field is the 0-based index of the correct option.
The difficulty field can be used by the quiz/result templates to display question levels.
"""

QUIZ_REMARKS = {'excellent': 'Excellent work! You have demonstrated a strong understanding of this lesson.', 'good': 'Good work! You understand the main ideas, but reviewing a few concepts will strengthen your mastery.', 'needs_review': 'Keep practising. Review the lesson carefully and retry the quiz to strengthen your understanding.', 'weak': 'This topic needs more attention. Revisit the lesson, work through examples, and try the quiz again.'}

SUBJECTS = {
    "maths": {
        "name": "Mathematics",
        "lessons": [
            {
                "id": 1,
                "title": "Number Systems",
                "content": """
                    <p>This lesson develops <b>Number Systems</b> at the basic foundations level.</p>
                            <p>It covers natural, whole, integer, rational, irrational and real numbers; place value and properties of operations.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Number Systems', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Number Systems?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Number Systems?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Number Systems should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Number Systems?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 2,
                "title": "Arithmetic Operations",
                "content": """
                    <p>This lesson develops <b>Arithmetic Operations</b> at the basic foundations level.</p>
                            <p>It covers order of operations, factors, multiples, divisibility, HCF and LCM, and estimation.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Arithmetic Operations', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Arithmetic Operations?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Arithmetic Operations?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Arithmetic Operations should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Arithmetic Operations?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 3,
                "title": "Fractions, Decimals and Percentages",
                "content": """
                    <p>This lesson develops <b>Fractions, Decimals and Percentages</b> at the basic foundations level.</p>
                            <p>It covers equivalent fractions, decimal conversion, percentage change and real-world percentage calculations.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Fractions, Decimals and Percentages', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Fractions, Decimals and Percentages?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Fractions, Decimals and Percentages?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Fractions, Decimals and Percentages should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Fractions, Decimals and Percentages?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 4,
                "title": "Ratio, Proportion and Variation",
                "content": """
                    <p>This lesson develops <b>Ratio, Proportion and Variation</b> at the basic foundations level.</p>
                            <p>It covers ratios, rates, direct proportion, inverse proportion and scaling.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Ratio, Proportion and Variation', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Ratio, Proportion and Variation?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Ratio, Proportion and Variation?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Ratio, Proportion and Variation should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Ratio, Proportion and Variation?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 5,
                "title": "Algebraic Expressions",
                "content": """
                    <p>This lesson develops <b>Algebraic Expressions</b> at the basic foundations level.</p>
                            <p>It covers variables, constants, coefficients, terms, simplification, expansion and factorisation.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Algebraic Expressions', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Algebraic Expressions?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Algebraic Expressions?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Algebraic Expressions should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Algebraic Expressions?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 6,
                "title": "Linear Equations and Inequalities",
                "content": """
                    <p>This lesson develops <b>Linear Equations and Inequalities</b> at the basic foundations level.</p>
                            <p>It covers solving one-variable equations and inequalities and representing solutions on a number line.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Linear Equations and Inequalities', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Linear Equations and Inequalities?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Linear Equations and Inequalities?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Linear Equations and Inequalities should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Linear Equations and Inequalities?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 7,
                "title": "Polynomials",
                "content": """
                    <p>This lesson develops <b>Polynomials</b> at the basic foundations level.</p>
                            <p>It covers degree, operations, identities, factor theorem and roots.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Polynomials', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Polynomials?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Polynomials?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Polynomials should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Polynomials?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 8,
                "title": "Sequences and Series",
                "content": """
                    <p>This lesson develops <b>Sequences and Series</b> at the intermediate methods level.</p>
                            <p>It covers patterns, arithmetic and geometric progressions, nth terms and sums.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Sequences and Series', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Sequences and Series?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Sequences and Series?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Sequences and Series should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Sequences and Series?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 9,
                "title": "Coordinate Geometry",
                "content": """
                    <p>This lesson develops <b>Coordinate Geometry</b> at the intermediate methods level.</p>
                            <p>It covers Cartesian plane, distance, midpoint, slope and equations of straight lines.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Coordinate Geometry', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Coordinate Geometry?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Coordinate Geometry?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Coordinate Geometry should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Coordinate Geometry?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 10,
                "title": "Plane Geometry",
                "content": """
                    <p>This lesson develops <b>Plane Geometry</b> at the intermediate methods level.</p>
                            <p>It covers points, lines, angles, polygons, congruence, similarity and geometric reasoning.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Plane Geometry', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Plane Geometry?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Plane Geometry?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Plane Geometry should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Plane Geometry?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 11,
                "title": "Triangles and Quadrilaterals",
                "content": """
                    <p>This lesson develops <b>Triangles and Quadrilaterals</b> at the intermediate methods level.</p>
                            <p>It covers triangle properties, congruence, similarity, Pythagoras and quadrilateral properties.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Triangles and Quadrilaterals', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Triangles and Quadrilaterals?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Triangles and Quadrilaterals?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Triangles and Quadrilaterals should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Triangles and Quadrilaterals?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 12,
                "title": "Circles",
                "content": """
                    <p>This lesson develops <b>Circles</b> at the intermediate methods level.</p>
                            <p>It covers radius, diameter, chord, arc, tangent, circumference, area and basic circle theorems.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Circles', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Circles?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Circles?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Circles should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Circles?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 13,
                "title": "Trigonometry Basics",
                "content": """
                    <p>This lesson develops <b>Trigonometry Basics</b> at the intermediate methods level.</p>
                            <p>It covers sine, cosine, tangent, right triangles, angles and standard values.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Trigonometry Basics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Trigonometry Basics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Trigonometry Basics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Trigonometry Basics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Trigonometry Basics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 14,
                "title": "Trigonometric Identities and Equations",
                "content": """
                    <p>This lesson develops <b>Trigonometric Identities and Equations</b> at the intermediate methods level.</p>
                            <p>It covers fundamental identities, transformations and solving basic trigonometric equations.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Trigonometric Identities and Equations', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Trigonometric Identities and Equations?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Trigonometric Identities and Equations?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Trigonometric Identities and Equations should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Trigonometric Identities and Equations?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 15,
                "title": "Exponents and Logarithms",
                "content": """
                    <p>This lesson develops <b>Exponents and Logarithms</b> at the advanced applications and connections level.</p>
                            <p>It covers laws of indices, exponential growth and logarithms as inverse operations.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Exponents and Logarithms', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Exponents and Logarithms?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Exponents and Logarithms?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Exponents and Logarithms should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Exponents and Logarithms?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 16,
                "title": "Functions and Graphs",
                "content": """
                    <p>This lesson develops <b>Functions and Graphs</b> at the advanced applications and connections level.</p>
                            <p>It covers domain, range, notation, transformations, inverse functions and graph interpretation.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Functions and Graphs', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Functions and Graphs?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Functions and Graphs?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Functions and Graphs should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Functions and Graphs?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 17,
                "title": "Limits and Continuity",
                "content": """
                    <p>This lesson develops <b>Limits and Continuity</b> at the advanced applications and connections level.</p>
                            <p>It covers approaching values, one-sided limits, continuity and basic limit laws.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Limits and Continuity', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Limits and Continuity?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Limits and Continuity?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Limits and Continuity should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Limits and Continuity?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 18,
                "title": "Differential Calculus",
                "content": """
                    <p>This lesson develops <b>Differential Calculus</b> at the advanced applications and connections level.</p>
                            <p>It covers derivative as rate of change, differentiation rules, tangent lines and applications.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Differential Calculus', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Differential Calculus?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Differential Calculus?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Differential Calculus should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Differential Calculus?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 19,
                "title": "Integral Calculus",
                "content": """
                    <p>This lesson develops <b>Integral Calculus</b> at the advanced applications and connections level.</p>
                            <p>It covers antiderivatives, definite integrals, area and the fundamental theorem of calculus.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Integral Calculus', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Integral Calculus?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Integral Calculus?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Integral Calculus should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Integral Calculus?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 20,
                "title": "Probability and Statistics",
                "content": """
                    <p>This lesson develops <b>Probability and Statistics</b> at the advanced applications and connections level.</p>
                            <p>It covers data summaries, distributions, probability rules, conditional probability and expected value.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Probability and Statistics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Probability and Statistics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Probability and Statistics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Probability and Statistics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Probability and Statistics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
        ],
    },
    "physics": {
        "name": "Physics",
        "lessons": [
            {
                "id": 1,
                "title": "Units, Dimensions and Measurement",
                "content": """
                    <p>This lesson develops <b>Units, Dimensions and Measurement</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of units, dimensions and measurement.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Units, Dimensions and Measurement', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Units, Dimensions and Measurement?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Units, Dimensions and Measurement?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Units, Dimensions and Measurement should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Units, Dimensions and Measurement?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 2,
                "title": "Scalars and Vectors",
                "content": """
                    <p>This lesson develops <b>Scalars and Vectors</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of scalars and vectors.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Scalars and Vectors', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Scalars and Vectors?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Scalars and Vectors?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Scalars and Vectors should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Scalars and Vectors?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 3,
                "title": "Motion in One Dimension",
                "content": """
                    <p>This lesson develops <b>Motion in One Dimension</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of motion in one dimension.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Motion in One Dimension', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Motion in One Dimension?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Motion in One Dimension?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Motion in One Dimension should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Motion in One Dimension?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 4,
                "title": "Motion in Two Dimensions",
                "content": """
                    <p>This lesson develops <b>Motion in Two Dimensions</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of motion in two dimensions.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Motion in Two Dimensions', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Motion in Two Dimensions?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Motion in Two Dimensions?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Motion in Two Dimensions should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Motion in Two Dimensions?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 5,
                "title": "Newton's Laws of Motion",
                "content": """
                    <p>This lesson develops <b>Newton's Laws of Motion</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of newton's laws of motion.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', "Newton's Laws of Motion", 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': "[Easy] Which approach is most appropriate when first learning Newton's Laws of Motion?", 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': "[Moderate] Which skill is most directly developed by studying Newton's Laws of Motion?", 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': "[Moderate] A strong solution involving Newton's Laws of Motion should usually include:", 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': "[Difficult] What best demonstrates mastery of Newton's Laws of Motion?", 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 6,
                "title": "Work, Energy and Power",
                "content": """
                    <p>This lesson develops <b>Work, Energy and Power</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of work, energy and power.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Work, Energy and Power', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Work, Energy and Power?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Work, Energy and Power?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Work, Energy and Power should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Work, Energy and Power?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 7,
                "title": "Momentum and Collisions",
                "content": """
                    <p>This lesson develops <b>Momentum and Collisions</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of momentum and collisions.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Momentum and Collisions', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Momentum and Collisions?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Momentum and Collisions?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Momentum and Collisions should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Momentum and Collisions?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 8,
                "title": "Circular Motion and Gravitation",
                "content": """
                    <p>This lesson develops <b>Circular Motion and Gravitation</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of circular motion and gravitation.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Circular Motion and Gravitation', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Circular Motion and Gravitation?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Circular Motion and Gravitation?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Circular Motion and Gravitation should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Circular Motion and Gravitation?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 9,
                "title": "Rotational Motion",
                "content": """
                    <p>This lesson develops <b>Rotational Motion</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of rotational motion.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Rotational Motion', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Rotational Motion?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Rotational Motion?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Rotational Motion should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Rotational Motion?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 10,
                "title": "Properties of Matter",
                "content": """
                    <p>This lesson develops <b>Properties of Matter</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of properties of matter.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Properties of Matter', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Properties of Matter?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Properties of Matter?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Properties of Matter should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Properties of Matter?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 11,
                "title": "Oscillations",
                "content": """
                    <p>This lesson develops <b>Oscillations</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of oscillations.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Oscillations', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Oscillations?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Oscillations?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Oscillations should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Oscillations?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 12,
                "title": "Waves and Sound",
                "content": """
                    <p>This lesson develops <b>Waves and Sound</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of waves and sound.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Waves and Sound', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Waves and Sound?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Waves and Sound?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Waves and Sound should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Waves and Sound?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 13,
                "title": "Thermal Physics",
                "content": """
                    <p>This lesson develops <b>Thermal Physics</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of thermal physics.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Thermal Physics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Thermal Physics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Thermal Physics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Thermal Physics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Thermal Physics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 14,
                "title": "Thermodynamics",
                "content": """
                    <p>This lesson develops <b>Thermodynamics</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of thermodynamics.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Thermodynamics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Thermodynamics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Thermodynamics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Thermodynamics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Thermodynamics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 15,
                "title": "Electrostatics",
                "content": """
                    <p>This lesson develops <b>Electrostatics</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of electrostatics.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Electrostatics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Electrostatics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Electrostatics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Electrostatics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Electrostatics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 16,
                "title": "Current Electricity",
                "content": """
                    <p>This lesson develops <b>Current Electricity</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of current electricity.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Current Electricity', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Current Electricity?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Current Electricity?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Current Electricity should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Current Electricity?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 17,
                "title": "Magnetism and Electromagnetic Induction",
                "content": """
                    <p>This lesson develops <b>Magnetism and Electromagnetic Induction</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of magnetism and electromagnetic induction.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Magnetism and Electromagnetic Induction', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Magnetism and Electromagnetic Induction?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Magnetism and Electromagnetic Induction?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Magnetism and Electromagnetic Induction should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Magnetism and Electromagnetic Induction?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 18,
                "title": "Optics",
                "content": """
                    <p>This lesson develops <b>Optics</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of optics.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Optics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Optics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Optics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Optics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Optics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 19,
                "title": "Modern Physics",
                "content": """
                    <p>This lesson develops <b>Modern Physics</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of modern physics.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Modern Physics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Modern Physics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Modern Physics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Modern Physics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Modern Physics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 20,
                "title": "Semiconductors and Electronics",
                "content": """
                    <p>This lesson develops <b>Semiconductors and Electronics</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of semiconductors and electronics.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Semiconductors and Electronics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Semiconductors and Electronics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Semiconductors and Electronics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Semiconductors and Electronics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Semiconductors and Electronics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
        ],
    },
    "chemistry": {
        "name": "Chemistry",
        "lessons": [
            {
                "id": 1,
                "title": "Atoms and the Periodic Table",
                "content": """
                    <p>This lesson develops <b>Atoms and the Periodic Table</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of atoms and the periodic table.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Atoms and the Periodic Table', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Atoms and the Periodic Table?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Atoms and the Periodic Table?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Atoms and the Periodic Table should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Atoms and the Periodic Table?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 2,
                "title": "Mole Concept and Stoichiometry",
                "content": """
                    <p>This lesson develops <b>Mole Concept and Stoichiometry</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of mole concept and stoichiometry.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Mole Concept and Stoichiometry', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Mole Concept and Stoichiometry?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Mole Concept and Stoichiometry?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Mole Concept and Stoichiometry should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Mole Concept and Stoichiometry?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 3,
                "title": "Chemical Bonding",
                "content": """
                    <p>This lesson develops <b>Chemical Bonding</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of chemical bonding.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Chemical Bonding', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Chemical Bonding?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Chemical Bonding?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Chemical Bonding should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Chemical Bonding?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 4,
                "title": "States of Matter",
                "content": """
                    <p>This lesson develops <b>States of Matter</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of states of matter.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'States of Matter', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning States of Matter?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying States of Matter?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving States of Matter should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of States of Matter?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 5,
                "title": "Thermochemistry",
                "content": """
                    <p>This lesson develops <b>Thermochemistry</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of thermochemistry.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Thermochemistry', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Thermochemistry?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Thermochemistry?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Thermochemistry should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Thermochemistry?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 6,
                "title": "Chemical Equilibrium",
                "content": """
                    <p>This lesson develops <b>Chemical Equilibrium</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of chemical equilibrium.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Chemical Equilibrium', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Chemical Equilibrium?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Chemical Equilibrium?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Chemical Equilibrium should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Chemical Equilibrium?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 7,
                "title": "Ionic Equilibrium",
                "content": """
                    <p>This lesson develops <b>Ionic Equilibrium</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of ionic equilibrium.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Ionic Equilibrium', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Ionic Equilibrium?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Ionic Equilibrium?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Ionic Equilibrium should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Ionic Equilibrium?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 8,
                "title": "Redox Reactions",
                "content": """
                    <p>This lesson develops <b>Redox Reactions</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of redox reactions.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Redox Reactions', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Redox Reactions?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Redox Reactions?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Redox Reactions should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Redox Reactions?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 9,
                "title": "Electrochemistry",
                "content": """
                    <p>This lesson develops <b>Electrochemistry</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of electrochemistry.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Electrochemistry', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Electrochemistry?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Electrochemistry?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Electrochemistry should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Electrochemistry?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 10,
                "title": "Chemical Kinetics",
                "content": """
                    <p>This lesson develops <b>Chemical Kinetics</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of chemical kinetics.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Chemical Kinetics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Chemical Kinetics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Chemical Kinetics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Chemical Kinetics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Chemical Kinetics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 11,
                "title": "Solutions",
                "content": """
                    <p>This lesson develops <b>Solutions</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of solutions.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Solutions', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Solutions?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Solutions?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Solutions should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Solutions?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 12,
                "title": "Surface Chemistry",
                "content": """
                    <p>This lesson develops <b>Surface Chemistry</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of surface chemistry.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Surface Chemistry', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Surface Chemistry?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Surface Chemistry?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Surface Chemistry should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Surface Chemistry?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 13,
                "title": "Introduction to Organic Chemistry",
                "content": """
                    <p>This lesson develops <b>Introduction to Organic Chemistry</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of introduction to organic chemistry.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Introduction to Organic Chemistry', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Introduction to Organic Chemistry?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Introduction to Organic Chemistry?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Introduction to Organic Chemistry should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Introduction to Organic Chemistry?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 14,
                "title": "Hydrocarbons",
                "content": """
                    <p>This lesson develops <b>Hydrocarbons</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of hydrocarbons.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Hydrocarbons', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Hydrocarbons?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Hydrocarbons?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Hydrocarbons should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Hydrocarbons?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 15,
                "title": "Functional Groups",
                "content": """
                    <p>This lesson develops <b>Functional Groups</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of functional groups.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Functional Groups', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Functional Groups?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Functional Groups?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Functional Groups should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Functional Groups?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 16,
                "title": "Organic Reactions",
                "content": """
                    <p>This lesson develops <b>Organic Reactions</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of organic reactions.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Organic Reactions', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Organic Reactions?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Organic Reactions?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Organic Reactions should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Organic Reactions?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 17,
                "title": "Polymers",
                "content": """
                    <p>This lesson develops <b>Polymers</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of polymers.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Polymers', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Polymers?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Polymers?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Polymers should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Polymers?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 18,
                "title": "Coordination Chemistry",
                "content": """
                    <p>This lesson develops <b>Coordination Chemistry</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of coordination chemistry.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Coordination Chemistry', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Coordination Chemistry?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Coordination Chemistry?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Coordination Chemistry should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Coordination Chemistry?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 19,
                "title": "Metallurgy and Materials",
                "content": """
                    <p>This lesson develops <b>Metallurgy and Materials</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of metallurgy and materials.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Metallurgy and Materials', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Metallurgy and Materials?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Metallurgy and Materials?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Metallurgy and Materials should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Metallurgy and Materials?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 20,
                "title": "Environmental Chemistry",
                "content": """
                    <p>This lesson develops <b>Environmental Chemistry</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of environmental chemistry.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Environmental Chemistry', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Environmental Chemistry?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Environmental Chemistry?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Environmental Chemistry should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Environmental Chemistry?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
        ],
    },
    "biology": {
        "name": "Biology",
        "lessons": [
            {
                "id": 1,
                "title": "Introduction to Biology and Scientific Method",
                "content": """
                    <p>This lesson develops <b>Introduction to Biology and Scientific Method</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of introduction to biology and scientific method.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Introduction to Biology and Scientific Method', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Introduction to Biology and Scientific Method?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Introduction to Biology and Scientific Method?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Introduction to Biology and Scientific Method should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Introduction to Biology and Scientific Method?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 2,
                "title": "Biological Molecules",
                "content": """
                    <p>This lesson develops <b>Biological Molecules</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of biological molecules.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Biological Molecules', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Biological Molecules?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Biological Molecules?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Biological Molecules should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Biological Molecules?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 3,
                "title": "Cell Structure",
                "content": """
                    <p>This lesson develops <b>Cell Structure</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of cell structure.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Cell Structure', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Cell Structure?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Cell Structure?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Cell Structure should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Cell Structure?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 4,
                "title": "Cell Membrane and Transport",
                "content": """
                    <p>This lesson develops <b>Cell Membrane and Transport</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of cell membrane and transport.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Cell Membrane and Transport', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Cell Membrane and Transport?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Cell Membrane and Transport?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Cell Membrane and Transport should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Cell Membrane and Transport?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 5,
                "title": "Cellular Respiration",
                "content": """
                    <p>This lesson develops <b>Cellular Respiration</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of cellular respiration.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Cellular Respiration', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Cellular Respiration?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Cellular Respiration?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Cellular Respiration should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Cellular Respiration?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 6,
                "title": "Photosynthesis",
                "content": """
                    <p>This lesson develops <b>Photosynthesis</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of photosynthesis.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Photosynthesis', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Photosynthesis?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Photosynthesis?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Photosynthesis should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Photosynthesis?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 7,
                "title": "Cell Division",
                "content": """
                    <p>This lesson develops <b>Cell Division</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of cell division.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Cell Division', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Cell Division?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Cell Division?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Cell Division should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Cell Division?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 8,
                "title": "Genetics",
                "content": """
                    <p>This lesson develops <b>Genetics</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of genetics.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Genetics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Genetics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Genetics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Genetics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Genetics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 9,
                "title": "DNA, RNA and Protein Synthesis",
                "content": """
                    <p>This lesson develops <b>DNA, RNA and Protein Synthesis</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of dna, rna and protein synthesis.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'DNA, RNA and Protein Synthesis', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning DNA, RNA and Protein Synthesis?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying DNA, RNA and Protein Synthesis?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving DNA, RNA and Protein Synthesis should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of DNA, RNA and Protein Synthesis?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 10,
                "title": "Evolution",
                "content": """
                    <p>This lesson develops <b>Evolution</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of evolution.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Evolution', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Evolution?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Evolution?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Evolution should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Evolution?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 11,
                "title": "Classification and Biodiversity",
                "content": """
                    <p>This lesson develops <b>Classification and Biodiversity</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of classification and biodiversity.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Classification and Biodiversity', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Classification and Biodiversity?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Classification and Biodiversity?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Classification and Biodiversity should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Classification and Biodiversity?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 12,
                "title": "Plant Structure and Transport",
                "content": """
                    <p>This lesson develops <b>Plant Structure and Transport</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of plant structure and transport.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Plant Structure and Transport', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Plant Structure and Transport?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Plant Structure and Transport?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Plant Structure and Transport should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Plant Structure and Transport?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 13,
                "title": "Plant Reproduction",
                "content": """
                    <p>This lesson develops <b>Plant Reproduction</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of plant reproduction.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Plant Reproduction', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Plant Reproduction?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Plant Reproduction?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Plant Reproduction should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Plant Reproduction?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 14,
                "title": "Human Digestive System",
                "content": """
                    <p>This lesson develops <b>Human Digestive System</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of human digestive system.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Human Digestive System', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Human Digestive System?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Human Digestive System?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Human Digestive System should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Human Digestive System?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 15,
                "title": "Human Circulatory System",
                "content": """
                    <p>This lesson develops <b>Human Circulatory System</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of human circulatory system.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Human Circulatory System', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Human Circulatory System?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Human Circulatory System?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Human Circulatory System should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Human Circulatory System?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 16,
                "title": "Human Respiratory System",
                "content": """
                    <p>This lesson develops <b>Human Respiratory System</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of human respiratory system.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Human Respiratory System', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Human Respiratory System?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Human Respiratory System?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Human Respiratory System should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Human Respiratory System?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 17,
                "title": "Nervous and Endocrine Systems",
                "content": """
                    <p>This lesson develops <b>Nervous and Endocrine Systems</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of nervous and endocrine systems.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Nervous and Endocrine Systems', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Nervous and Endocrine Systems?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Nervous and Endocrine Systems?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Nervous and Endocrine Systems should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Nervous and Endocrine Systems?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 18,
                "title": "Immune System and Disease",
                "content": """
                    <p>This lesson develops <b>Immune System and Disease</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of immune system and disease.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Immune System and Disease', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Immune System and Disease?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Immune System and Disease?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Immune System and Disease should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Immune System and Disease?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 19,
                "title": "Ecology and Ecosystems",
                "content": """
                    <p>This lesson develops <b>Ecology and Ecosystems</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of ecology and ecosystems.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Ecology and Ecosystems', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Ecology and Ecosystems?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Ecology and Ecosystems?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Ecology and Ecosystems should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Ecology and Ecosystems?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 20,
                "title": "Biotechnology",
                "content": """
                    <p>This lesson develops <b>Biotechnology</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of biotechnology.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Biotechnology', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Biotechnology?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Biotechnology?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Biotechnology should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Biotechnology?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
        ],
    },
    "computer_science": {
        "name": "Computer Science",
        "lessons": [
            {
                "id": 1,
                "title": "Computers and Information",
                "content": """
                    <p>This lesson develops <b>Computers and Information</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of computers and information.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Computers and Information', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Computers and Information?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Computers and Information?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Computers and Information should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Computers and Information?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 2,
                "title": "Binary and Data Representation",
                "content": """
                    <p>This lesson develops <b>Binary and Data Representation</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of binary and data representation.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Binary and Data Representation', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Binary and Data Representation?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Binary and Data Representation?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Binary and Data Representation should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Binary and Data Representation?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 3,
                "title": "Programming Fundamentals",
                "content": """
                    <p>This lesson develops <b>Programming Fundamentals</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of programming fundamentals.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Programming Fundamentals', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Programming Fundamentals?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Programming Fundamentals?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Programming Fundamentals should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Programming Fundamentals?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 4,
                "title": "Variables, Types and Operators",
                "content": """
                    <p>This lesson develops <b>Variables, Types and Operators</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of variables, types and operators.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Variables, Types and Operators', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Variables, Types and Operators?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Variables, Types and Operators?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Variables, Types and Operators should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Variables, Types and Operators?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 5,
                "title": "Conditionals and Loops",
                "content": """
                    <p>This lesson develops <b>Conditionals and Loops</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of conditionals and loops.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Conditionals and Loops', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Conditionals and Loops?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Conditionals and Loops?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Conditionals and Loops should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Conditionals and Loops?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 6,
                "title": "Functions and Modularity",
                "content": """
                    <p>This lesson develops <b>Functions and Modularity</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of functions and modularity.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Functions and Modularity', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Functions and Modularity?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Functions and Modularity?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Functions and Modularity should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Functions and Modularity?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 7,
                "title": "Data Structures",
                "content": """
                    <p>This lesson develops <b>Data Structures</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of data structures.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Data Structures', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Data Structures?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Data Structures?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Data Structures should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Data Structures?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 8,
                "title": "Algorithms and Complexity",
                "content": """
                    <p>This lesson develops <b>Algorithms and Complexity</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of algorithms and complexity.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Algorithms and Complexity', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Algorithms and Complexity?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Algorithms and Complexity?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Algorithms and Complexity should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Algorithms and Complexity?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 9,
                "title": "Object-Oriented Programming",
                "content": """
                    <p>This lesson develops <b>Object-Oriented Programming</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of object-oriented programming.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Object-Oriented Programming', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Object-Oriented Programming?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Object-Oriented Programming?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Object-Oriented Programming should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Object-Oriented Programming?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 10,
                "title": "Recursion",
                "content": """
                    <p>This lesson develops <b>Recursion</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of recursion.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Recursion', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Recursion?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Recursion?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Recursion should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Recursion?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 11,
                "title": "Databases and SQL",
                "content": """
                    <p>This lesson develops <b>Databases and SQL</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of databases and sql.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Databases and SQL', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Databases and SQL?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Databases and SQL?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Databases and SQL should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Databases and SQL?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 12,
                "title": "Computer Networks",
                "content": """
                    <p>This lesson develops <b>Computer Networks</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of computer networks.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Computer Networks', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Computer Networks?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Computer Networks?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Computer Networks should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Computer Networks?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 13,
                "title": "Operating Systems",
                "content": """
                    <p>This lesson develops <b>Operating Systems</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of operating systems.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Operating Systems', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Operating Systems?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Operating Systems?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Operating Systems should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Operating Systems?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 14,
                "title": "Computer Architecture",
                "content": """
                    <p>This lesson develops <b>Computer Architecture</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of computer architecture.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Computer Architecture', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Computer Architecture?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Computer Architecture?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Computer Architecture should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Computer Architecture?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 15,
                "title": "Cybersecurity Fundamentals",
                "content": """
                    <p>This lesson develops <b>Cybersecurity Fundamentals</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of cybersecurity fundamentals.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Cybersecurity Fundamentals', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Cybersecurity Fundamentals?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Cybersecurity Fundamentals?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Cybersecurity Fundamentals should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Cybersecurity Fundamentals?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 16,
                "title": "Web Development",
                "content": """
                    <p>This lesson develops <b>Web Development</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of web development.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Web Development', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Web Development?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Web Development?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Web Development should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Web Development?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 17,
                "title": "Software Engineering and Git",
                "content": """
                    <p>This lesson develops <b>Software Engineering and Git</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of software engineering and git.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Software Engineering and Git', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Software Engineering and Git?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Software Engineering and Git?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Software Engineering and Git should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Software Engineering and Git?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 18,
                "title": "Artificial Intelligence and Machine Learning",
                "content": """
                    <p>This lesson develops <b>Artificial Intelligence and Machine Learning</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of artificial intelligence and machine learning.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Artificial Intelligence and Machine Learning', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Artificial Intelligence and Machine Learning?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Artificial Intelligence and Machine Learning?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Artificial Intelligence and Machine Learning should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Artificial Intelligence and Machine Learning?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 19,
                "title": "Data Science",
                "content": """
                    <p>This lesson develops <b>Data Science</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of data science.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Data Science', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Data Science?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Data Science?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Data Science should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Data Science?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 20,
                "title": "Advanced Algorithms",
                "content": """
                    <p>This lesson develops <b>Advanced Algorithms</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of advanced algorithms.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Advanced Algorithms', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Advanced Algorithms?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Advanced Algorithms?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Advanced Algorithms should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Advanced Algorithms?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
        ],
    },
    "english": {
        "name": "English",
        "lessons": [
            {
                "id": 1,
                "title": "Parts of Speech",
                "content": """
                    <p>This lesson develops <b>Parts of Speech</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of parts of speech.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Parts of Speech', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Parts of Speech?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Parts of Speech?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Parts of Speech should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Parts of Speech?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 2,
                "title": "Sentence Structure",
                "content": """
                    <p>This lesson develops <b>Sentence Structure</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of sentence structure.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Sentence Structure', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Sentence Structure?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Sentence Structure?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Sentence Structure should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Sentence Structure?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 3,
                "title": "Tenses",
                "content": """
                    <p>This lesson develops <b>Tenses</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of tenses.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Tenses', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Tenses?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Tenses?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Tenses should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Tenses?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 4,
                "title": "Subject-Verb Agreement",
                "content": """
                    <p>This lesson develops <b>Subject-Verb Agreement</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of subject-verb agreement.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Subject-Verb Agreement', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Subject-Verb Agreement?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Subject-Verb Agreement?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Subject-Verb Agreement should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Subject-Verb Agreement?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 5,
                "title": "Articles and Determiners",
                "content": """
                    <p>This lesson develops <b>Articles and Determiners</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of articles and determiners.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Articles and Determiners', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Articles and Determiners?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Articles and Determiners?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Articles and Determiners should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Articles and Determiners?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 6,
                "title": "Prepositions and Conjunctions",
                "content": """
                    <p>This lesson develops <b>Prepositions and Conjunctions</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of prepositions and conjunctions.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Prepositions and Conjunctions', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Prepositions and Conjunctions?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Prepositions and Conjunctions?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Prepositions and Conjunctions should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Prepositions and Conjunctions?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 7,
                "title": "Active and Passive Voice",
                "content": """
                    <p>This lesson develops <b>Active and Passive Voice</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of active and passive voice.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Active and Passive Voice', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Active and Passive Voice?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Active and Passive Voice?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Active and Passive Voice should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Active and Passive Voice?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 8,
                "title": "Direct and Indirect Speech",
                "content": """
                    <p>This lesson develops <b>Direct and Indirect Speech</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of direct and indirect speech.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Direct and Indirect Speech', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Direct and Indirect Speech?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Direct and Indirect Speech?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Direct and Indirect Speech should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Direct and Indirect Speech?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 9,
                "title": "Punctuation",
                "content": """
                    <p>This lesson develops <b>Punctuation</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of punctuation.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Punctuation', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Punctuation?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Punctuation?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Punctuation should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Punctuation?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 10,
                "title": "Vocabulary and Word Formation",
                "content": """
                    <p>This lesson develops <b>Vocabulary and Word Formation</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of vocabulary and word formation.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Vocabulary and Word Formation', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Vocabulary and Word Formation?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Vocabulary and Word Formation?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Vocabulary and Word Formation should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Vocabulary and Word Formation?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 11,
                "title": "Reading Comprehension",
                "content": """
                    <p>This lesson develops <b>Reading Comprehension</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of reading comprehension.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Reading Comprehension', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Reading Comprehension?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Reading Comprehension?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Reading Comprehension should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Reading Comprehension?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 12,
                "title": "Paragraph Writing",
                "content": """
                    <p>This lesson develops <b>Paragraph Writing</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of paragraph writing.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Paragraph Writing', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Paragraph Writing?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Paragraph Writing?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Paragraph Writing should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Paragraph Writing?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 13,
                "title": "Essay Writing",
                "content": """
                    <p>This lesson develops <b>Essay Writing</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of essay writing.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Essay Writing', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Essay Writing?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Essay Writing?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Essay Writing should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Essay Writing?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 14,
                "title": "Formal Writing",
                "content": """
                    <p>This lesson develops <b>Formal Writing</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of formal writing.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Formal Writing', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Formal Writing?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Formal Writing?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Formal Writing should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Formal Writing?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 15,
                "title": "Creative Writing",
                "content": """
                    <p>This lesson develops <b>Creative Writing</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of creative writing.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Creative Writing', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Creative Writing?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Creative Writing?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Creative Writing should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Creative Writing?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 16,
                "title": "Argument and Critical Reading",
                "content": """
                    <p>This lesson develops <b>Argument and Critical Reading</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of argument and critical reading.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Argument and Critical Reading', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Argument and Critical Reading?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Argument and Critical Reading?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Argument and Critical Reading should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Argument and Critical Reading?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 17,
                "title": "Rhetoric and Persuasion",
                "content": """
                    <p>This lesson develops <b>Rhetoric and Persuasion</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of rhetoric and persuasion.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Rhetoric and Persuasion', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Rhetoric and Persuasion?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Rhetoric and Persuasion?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Rhetoric and Persuasion should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Rhetoric and Persuasion?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 18,
                "title": "Literary Devices",
                "content": """
                    <p>This lesson develops <b>Literary Devices</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of literary devices.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Literary Devices', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Literary Devices?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Literary Devices?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Literary Devices should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Literary Devices?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 19,
                "title": "Poetry and Prose",
                "content": """
                    <p>This lesson develops <b>Poetry and Prose</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of poetry and prose.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Poetry and Prose', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Poetry and Prose?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Poetry and Prose?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Poetry and Prose should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Poetry and Prose?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 20,
                "title": "Advanced Grammar and Style",
                "content": """
                    <p>This lesson develops <b>Advanced Grammar and Style</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of advanced grammar and style.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Advanced Grammar and Style', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Advanced Grammar and Style?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Advanced Grammar and Style?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Advanced Grammar and Style should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Advanced Grammar and Style?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
        ],
    },
    "economics": {
        "name": "Economics",
        "lessons": [
            {
                "id": 1,
                "title": "Introduction to Economics",
                "content": """
                    <p>This lesson develops <b>Introduction to Economics</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of introduction to economics.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Introduction to Economics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Introduction to Economics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Introduction to Economics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Introduction to Economics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Introduction to Economics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 2,
                "title": "Scarcity and Opportunity Cost",
                "content": """
                    <p>This lesson develops <b>Scarcity and Opportunity Cost</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of scarcity and opportunity cost.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Scarcity and Opportunity Cost', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Scarcity and Opportunity Cost?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Scarcity and Opportunity Cost?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Scarcity and Opportunity Cost should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Scarcity and Opportunity Cost?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 3,
                "title": "Demand",
                "content": """
                    <p>This lesson develops <b>Demand</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of demand.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Demand', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Demand?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Demand?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Demand should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Demand?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 4,
                "title": "Supply",
                "content": """
                    <p>This lesson develops <b>Supply</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of supply.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Supply', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Supply?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Supply?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Supply should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Supply?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 5,
                "title": "Market Equilibrium",
                "content": """
                    <p>This lesson develops <b>Market Equilibrium</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of market equilibrium.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Market Equilibrium', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Market Equilibrium?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Market Equilibrium?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Market Equilibrium should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Market Equilibrium?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 6,
                "title": "Elasticity",
                "content": """
                    <p>This lesson develops <b>Elasticity</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of elasticity.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Elasticity', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Elasticity?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Elasticity?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Elasticity should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Elasticity?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 7,
                "title": "Consumer Behaviour",
                "content": """
                    <p>This lesson develops <b>Consumer Behaviour</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of consumer behaviour.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Consumer Behaviour', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Consumer Behaviour?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Consumer Behaviour?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Consumer Behaviour should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Consumer Behaviour?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 8,
                "title": "Production and Costs",
                "content": """
                    <p>This lesson develops <b>Production and Costs</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of production and costs.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Production and Costs', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Production and Costs?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Production and Costs?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Production and Costs should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Production and Costs?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 9,
                "title": "Market Structures",
                "content": """
                    <p>This lesson develops <b>Market Structures</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of market structures.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Market Structures', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Market Structures?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Market Structures?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Market Structures should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Market Structures?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 10,
                "title": "National Income",
                "content": """
                    <p>This lesson develops <b>National Income</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of national income.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'National Income', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning National Income?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying National Income?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving National Income should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of National Income?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 11,
                "title": "Inflation",
                "content": """
                    <p>This lesson develops <b>Inflation</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of inflation.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Inflation', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Inflation?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Inflation?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Inflation should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Inflation?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 12,
                "title": "Unemployment",
                "content": """
                    <p>This lesson develops <b>Unemployment</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of unemployment.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Unemployment', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Unemployment?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Unemployment?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Unemployment should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Unemployment?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 13,
                "title": "Money and Banking",
                "content": """
                    <p>This lesson develops <b>Money and Banking</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of money and banking.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Money and Banking', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Money and Banking?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Money and Banking?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Money and Banking should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Money and Banking?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 14,
                "title": "Fiscal Policy",
                "content": """
                    <p>This lesson develops <b>Fiscal Policy</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of fiscal policy.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Fiscal Policy', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Fiscal Policy?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Fiscal Policy?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Fiscal Policy should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Fiscal Policy?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 15,
                "title": "Monetary Policy",
                "content": """
                    <p>This lesson develops <b>Monetary Policy</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of monetary policy.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Monetary Policy', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Monetary Policy?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Monetary Policy?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Monetary Policy should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Monetary Policy?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 16,
                "title": "International Trade",
                "content": """
                    <p>This lesson develops <b>International Trade</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of international trade.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'International Trade', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning International Trade?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying International Trade?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving International Trade should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of International Trade?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 17,
                "title": "Exchange Rates",
                "content": """
                    <p>This lesson develops <b>Exchange Rates</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of exchange rates.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Exchange Rates', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Exchange Rates?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Exchange Rates?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Exchange Rates should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Exchange Rates?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 18,
                "title": "Economic Growth and Development",
                "content": """
                    <p>This lesson develops <b>Economic Growth and Development</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of economic growth and development.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Economic Growth and Development', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Economic Growth and Development?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Economic Growth and Development?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Economic Growth and Development should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Economic Growth and Development?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 19,
                "title": "Public Finance",
                "content": """
                    <p>This lesson develops <b>Public Finance</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of public finance.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Public Finance', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Public Finance?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Public Finance?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Public Finance should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Public Finance?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 20,
                "title": "Indian Economy: Foundations",
                "content": """
                    <p>This lesson develops <b>Indian Economy: Foundations</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of indian economy: foundations.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Indian Economy: Foundations', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Indian Economy: Foundations?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Indian Economy: Foundations?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Indian Economy: Foundations should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Indian Economy: Foundations?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
        ],
    },
    "indian_history": {
        "name": "Indian History",
        "lessons": [
            {
                "id": 1,
                "title": "Prehistoric India",
                "content": """
                    <p>This lesson develops <b>Prehistoric India</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of prehistoric india.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Prehistoric India', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Prehistoric India?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Prehistoric India?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Prehistoric India should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Prehistoric India?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 2,
                "title": "Indus Valley Civilization",
                "content": """
                    <p>This lesson develops <b>Indus Valley Civilization</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of indus valley civilization.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Indus Valley Civilization', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Indus Valley Civilization?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Indus Valley Civilization?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Indus Valley Civilization should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Indus Valley Civilization?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 3,
                "title": "Vedic Period",
                "content": """
                    <p>This lesson develops <b>Vedic Period</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of vedic period.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Vedic Period', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Vedic Period?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Vedic Period?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Vedic Period should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Vedic Period?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 4,
                "title": "Mahajanapadas and Buddhism",
                "content": """
                    <p>This lesson develops <b>Mahajanapadas and Buddhism</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of mahajanapadas and buddhism.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Mahajanapadas and Buddhism', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Mahajanapadas and Buddhism?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Mahajanapadas and Buddhism?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Mahajanapadas and Buddhism should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Mahajanapadas and Buddhism?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 5,
                "title": "Mauryan Empire",
                "content": """
                    <p>This lesson develops <b>Mauryan Empire</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of mauryan empire.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Mauryan Empire', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Mauryan Empire?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Mauryan Empire?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Mauryan Empire should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Mauryan Empire?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 6,
                "title": "Post-Mauryan India",
                "content": """
                    <p>This lesson develops <b>Post-Mauryan India</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of post-mauryan india.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Post-Mauryan India', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Post-Mauryan India?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Post-Mauryan India?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Post-Mauryan India should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Post-Mauryan India?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 7,
                "title": "Gupta Empire",
                "content": """
                    <p>This lesson develops <b>Gupta Empire</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of gupta empire.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Gupta Empire', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Gupta Empire?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Gupta Empire?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Gupta Empire should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Gupta Empire?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 8,
                "title": "Early Medieval India",
                "content": """
                    <p>This lesson develops <b>Early Medieval India</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of early medieval india.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Early Medieval India', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Early Medieval India?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Early Medieval India?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Early Medieval India should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Early Medieval India?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 9,
                "title": "Delhi Sultanate",
                "content": """
                    <p>This lesson develops <b>Delhi Sultanate</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of delhi sultanate.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Delhi Sultanate', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Delhi Sultanate?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Delhi Sultanate?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Delhi Sultanate should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Delhi Sultanate?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 10,
                "title": "Mughal Empire",
                "content": """
                    <p>This lesson develops <b>Mughal Empire</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of mughal empire.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Mughal Empire', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Mughal Empire?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Mughal Empire?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Mughal Empire should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Mughal Empire?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 11,
                "title": "Maratha Power",
                "content": """
                    <p>This lesson develops <b>Maratha Power</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of maratha power.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Maratha Power', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Maratha Power?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Maratha Power?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Maratha Power should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Maratha Power?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 12,
                "title": "Regional Kingdoms in Early Modern India",
                "content": """
                    <p>This lesson develops <b>Regional Kingdoms in Early Modern India</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of regional kingdoms in early modern india.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Regional Kingdoms in Early Modern India', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Regional Kingdoms in Early Modern India?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Regional Kingdoms in Early Modern India?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Regional Kingdoms in Early Modern India should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Regional Kingdoms in Early Modern India?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 13,
                "title": "European Trading Companies in India",
                "content": """
                    <p>This lesson develops <b>European Trading Companies in India</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of european trading companies in india.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'European Trading Companies in India', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning European Trading Companies in India?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying European Trading Companies in India?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving European Trading Companies in India should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of European Trading Companies in India?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 14,
                "title": "British Expansion in India",
                "content": """
                    <p>This lesson develops <b>British Expansion in India</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of british expansion in india.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'British Expansion in India', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning British Expansion in India?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying British Expansion in India?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving British Expansion in India should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of British Expansion in India?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 15,
                "title": "Revolt of 1857",
                "content": """
                    <p>This lesson develops <b>Revolt of 1857</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of revolt of 1857.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Revolt of 1857', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Revolt of 1857?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Revolt of 1857?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Revolt of 1857 should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Revolt of 1857?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 16,
                "title": "Socio-Religious Reform Movements",
                "content": """
                    <p>This lesson develops <b>Socio-Religious Reform Movements</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of socio-religious reform movements.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Socio-Religious Reform Movements', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Socio-Religious Reform Movements?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Socio-Religious Reform Movements?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Socio-Religious Reform Movements should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Socio-Religious Reform Movements?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 17,
                "title": "Indian National Congress and Early Nationalism",
                "content": """
                    <p>This lesson develops <b>Indian National Congress and Early Nationalism</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of indian national congress and early nationalism.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Indian National Congress and Early Nationalism', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Indian National Congress and Early Nationalism?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Indian National Congress and Early Nationalism?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Indian National Congress and Early Nationalism should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Indian National Congress and Early Nationalism?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 18,
                "title": "Gandhian Era",
                "content": """
                    <p>This lesson develops <b>Gandhian Era</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of gandhian era.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Gandhian Era', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Gandhian Era?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Gandhian Era?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Gandhian Era should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Gandhian Era?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 19,
                "title": "Indian Independence and Partition",
                "content": """
                    <p>This lesson develops <b>Indian Independence and Partition</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of indian independence and partition.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Indian Independence and Partition', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Indian Independence and Partition?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Indian Independence and Partition?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Indian Independence and Partition should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Indian Independence and Partition?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 20,
                "title": "Post-Independence India",
                "content": """
                    <p>This lesson develops <b>Post-Independence India</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of post-independence india.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Post-Independence India', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Post-Independence India?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Post-Independence India?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Post-Independence India should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Post-Independence India?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
        ],
    },
    "geography": {
        "name": "Geography",
        "lessons": [
            {
                "id": 1,
                "title": "Earth and Its Motions",
                "content": """
                    <p>This lesson develops <b>Earth and Its Motions</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of earth and its motions.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Earth and Its Motions', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Earth and Its Motions?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Earth and Its Motions?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Earth and Its Motions should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Earth and Its Motions?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 2,
                "title": "Latitudes, Longitudes and Time",
                "content": """
                    <p>This lesson develops <b>Latitudes, Longitudes and Time</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of latitudes, longitudes and time.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Latitudes, Longitudes and Time', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Latitudes, Longitudes and Time?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Latitudes, Longitudes and Time?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Latitudes, Longitudes and Time should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Latitudes, Longitudes and Time?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 3,
                "title": "Maps and Scale",
                "content": """
                    <p>This lesson develops <b>Maps and Scale</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of maps and scale.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Maps and Scale', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Maps and Scale?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Maps and Scale?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Maps and Scale should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Maps and Scale?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 4,
                "title": "Rocks and the Rock Cycle",
                "content": """
                    <p>This lesson develops <b>Rocks and the Rock Cycle</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of rocks and the rock cycle.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Rocks and the Rock Cycle', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Rocks and the Rock Cycle?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Rocks and the Rock Cycle?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Rocks and the Rock Cycle should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Rocks and the Rock Cycle?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 5,
                "title": "Plate Tectonics",
                "content": """
                    <p>This lesson develops <b>Plate Tectonics</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of plate tectonics.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Plate Tectonics', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Plate Tectonics?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Plate Tectonics?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Plate Tectonics should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Plate Tectonics?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 6,
                "title": "Landforms",
                "content": """
                    <p>This lesson develops <b>Landforms</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of landforms.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Landforms', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Landforms?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Landforms?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Landforms should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Landforms?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 7,
                "title": "Atmosphere",
                "content": """
                    <p>This lesson develops <b>Atmosphere</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of atmosphere.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Atmosphere', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Atmosphere?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Atmosphere?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Atmosphere should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Atmosphere?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 8,
                "title": "Weather and Climate",
                "content": """
                    <p>This lesson develops <b>Weather and Climate</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of weather and climate.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Weather and Climate', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Weather and Climate?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Weather and Climate?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Weather and Climate should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Weather and Climate?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 9,
                "title": "Oceans and Water Cycle",
                "content": """
                    <p>This lesson develops <b>Oceans and Water Cycle</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of oceans and water cycle.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Oceans and Water Cycle', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Oceans and Water Cycle?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Oceans and Water Cycle?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Oceans and Water Cycle should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Oceans and Water Cycle?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 10,
                "title": "Soils",
                "content": """
                    <p>This lesson develops <b>Soils</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of soils.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Soils', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Soils?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Soils?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Soils should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Soils?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 11,
                "title": "Natural Vegetation and Biomes",
                "content": """
                    <p>This lesson develops <b>Natural Vegetation and Biomes</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of natural vegetation and biomes.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Natural Vegetation and Biomes', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Natural Vegetation and Biomes?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Natural Vegetation and Biomes?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Natural Vegetation and Biomes should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Natural Vegetation and Biomes?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 12,
                "title": "Population Geography",
                "content": """
                    <p>This lesson develops <b>Population Geography</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of population geography.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Population Geography', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Population Geography?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Population Geography?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Population Geography should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Population Geography?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 13,
                "title": "Migration and Urbanization",
                "content": """
                    <p>This lesson develops <b>Migration and Urbanization</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of migration and urbanization.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Migration and Urbanization', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Migration and Urbanization?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Migration and Urbanization?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Migration and Urbanization should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Migration and Urbanization?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 14,
                "title": "Agriculture",
                "content": """
                    <p>This lesson develops <b>Agriculture</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of agriculture.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Agriculture', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Agriculture?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Agriculture?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Agriculture should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Agriculture?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 15,
                "title": "Mineral and Energy Resources",
                "content": """
                    <p>This lesson develops <b>Mineral and Energy Resources</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of mineral and energy resources.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Mineral and Energy Resources', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Mineral and Energy Resources?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Mineral and Energy Resources?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Mineral and Energy Resources should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Mineral and Energy Resources?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 16,
                "title": "Industries",
                "content": """
                    <p>This lesson develops <b>Industries</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of industries.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Industries', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Industries?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Industries?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Industries should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Industries?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 17,
                "title": "Transport and Communication",
                "content": """
                    <p>This lesson develops <b>Transport and Communication</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of transport and communication.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Transport and Communication', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Transport and Communication?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Transport and Communication?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Transport and Communication should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Transport and Communication?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 18,
                "title": "Environmental Geography",
                "content": """
                    <p>This lesson develops <b>Environmental Geography</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of environmental geography.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Environmental Geography', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Environmental Geography?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Environmental Geography?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Environmental Geography should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Environmental Geography?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 19,
                "title": "Disasters and Risk Reduction",
                "content": """
                    <p>This lesson develops <b>Disasters and Risk Reduction</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of disasters and risk reduction.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Disasters and Risk Reduction', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Disasters and Risk Reduction?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Disasters and Risk Reduction?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Disasters and Risk Reduction should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Disasters and Risk Reduction?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 20,
                "title": "India: Physical and Economic Geography",
                "content": """
                    <p>This lesson develops <b>India: Physical and Economic Geography</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of india: physical and economic geography.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'India: Physical and Economic Geography', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning India: Physical and Economic Geography?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying India: Physical and Economic Geography?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving India: Physical and Economic Geography should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of India: Physical and Economic Geography?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
        ],
    },
    "psychology": {
        "name": "Psychology",
        "lessons": [
            {
                "id": 1,
                "title": "Introduction to Psychology",
                "content": """
                    <p>This lesson develops <b>Introduction to Psychology</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of introduction to psychology.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Introduction to Psychology', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Introduction to Psychology?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Introduction to Psychology?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Introduction to Psychology should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Introduction to Psychology?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 2,
                "title": "Research Methods",
                "content": """
                    <p>This lesson develops <b>Research Methods</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of research methods.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Research Methods', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Research Methods?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Research Methods?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Research Methods should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Research Methods?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 3,
                "title": "Biological Bases of Behaviour",
                "content": """
                    <p>This lesson develops <b>Biological Bases of Behaviour</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of biological bases of behaviour.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Biological Bases of Behaviour', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Biological Bases of Behaviour?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Biological Bases of Behaviour?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Biological Bases of Behaviour should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Biological Bases of Behaviour?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 4,
                "title": "Sensation and Perception",
                "content": """
                    <p>This lesson develops <b>Sensation and Perception</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of sensation and perception.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Sensation and Perception', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Sensation and Perception?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Sensation and Perception?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Sensation and Perception should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Sensation and Perception?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 5,
                "title": "Learning",
                "content": """
                    <p>This lesson develops <b>Learning</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of learning.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Learning', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Learning?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Learning?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Learning should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Learning?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 6,
                "title": "Memory",
                "content": """
                    <p>This lesson develops <b>Memory</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of memory.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Memory', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Memory?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Memory?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Memory should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Memory?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 7,
                "title": "Thinking and Problem Solving",
                "content": """
                    <p>This lesson develops <b>Thinking and Problem Solving</b> at the basic foundations level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of thinking and problem solving.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Thinking and Problem Solving', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Thinking and Problem Solving?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Thinking and Problem Solving?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Thinking and Problem Solving should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Thinking and Problem Solving?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 8,
                "title": "Intelligence",
                "content": """
                    <p>This lesson develops <b>Intelligence</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of intelligence.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Intelligence', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Intelligence?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Intelligence?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Intelligence should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Intelligence?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 9,
                "title": "Motivation and Emotion",
                "content": """
                    <p>This lesson develops <b>Motivation and Emotion</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of motivation and emotion.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Motivation and Emotion', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Motivation and Emotion?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Motivation and Emotion?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Motivation and Emotion should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Motivation and Emotion?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 10,
                "title": "Developmental Psychology",
                "content": """
                    <p>This lesson develops <b>Developmental Psychology</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of developmental psychology.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Developmental Psychology', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Developmental Psychology?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Developmental Psychology?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Developmental Psychology should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Developmental Psychology?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 11,
                "title": "Personality",
                "content": """
                    <p>This lesson develops <b>Personality</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of personality.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Personality', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Personality?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Personality?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Personality should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Personality?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 12,
                "title": "Social Psychology",
                "content": """
                    <p>This lesson develops <b>Social Psychology</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of social psychology.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Social Psychology', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Social Psychology?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Social Psychology?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Social Psychology should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Social Psychology?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 13,
                "title": "Attitudes and Persuasion",
                "content": """
                    <p>This lesson develops <b>Attitudes and Persuasion</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of attitudes and persuasion.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Attitudes and Persuasion', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Attitudes and Persuasion?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Attitudes and Persuasion?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Attitudes and Persuasion should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Attitudes and Persuasion?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 14,
                "title": "Stress and Coping",
                "content": """
                    <p>This lesson develops <b>Stress and Coping</b> at the intermediate methods level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of stress and coping.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Stress and Coping', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Stress and Coping?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Stress and Coping?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Stress and Coping should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Stress and Coping?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 15,
                "title": "Psychological Disorders",
                "content": """
                    <p>This lesson develops <b>Psychological Disorders</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of psychological disorders.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Psychological Disorders', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Psychological Disorders?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Psychological Disorders?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Psychological Disorders should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Psychological Disorders?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 16,
                "title": "Therapy and Mental Health",
                "content": """
                    <p>This lesson develops <b>Therapy and Mental Health</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of therapy and mental health.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Therapy and Mental Health', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Therapy and Mental Health?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Therapy and Mental Health?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Therapy and Mental Health should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Therapy and Mental Health?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 17,
                "title": "Cognition and Decision Making",
                "content": """
                    <p>This lesson develops <b>Cognition and Decision Making</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of cognition and decision making.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Cognition and Decision Making', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Cognition and Decision Making?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Cognition and Decision Making?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Cognition and Decision Making should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Cognition and Decision Making?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 18,
                "title": "Language and Communication",
                "content": """
                    <p>This lesson develops <b>Language and Communication</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of language and communication.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Language and Communication', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Language and Communication?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Language and Communication?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Language and Communication should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Language and Communication?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 19,
                "title": "Organizational Psychology",
                "content": """
                    <p>This lesson develops <b>Organizational Psychology</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of organizational psychology.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Organizational Psychology', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Organizational Psychology?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Organizational Psychology?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Organizational Psychology should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Organizational Psychology?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
            {
                "id": 20,
                "title": "Applied Psychology and Everyday Life",
                "content": """
                    <p>This lesson develops <b>Applied Psychology and Everyday Life</b> at the advanced applications and connections level.</p>
                            <p>It covers the key ideas, terminology, examples and problem-solving methods of applied psychology and everyday life.</p>
                            <p>Focus on definitions first, then worked examples, relationships between ideas, and finally
                            applying the concepts to unfamiliar problems. You should be able to explain the main ideas,
                            choose an appropriate method, and check whether your result is reasonable.</p>
                """,
                "quiz": [
                    {'question': '[Easy] What is the main topic studied in this lesson?', 'options': ['Unrelated topic', 'Applied Psychology and Everyday Life', 'A random historical event', 'Computer hardware'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Easy] Which approach is most appropriate when first learning Applied Psychology and Everyday Life?', 'options': ['Memorise answers without understanding', 'Learn definitions and simple examples first', 'Skip examples', 'Start with the hardest problem'], 'answer': 1, 'difficulty': 'easy'},
                    {'question': '[Moderate] Which skill is most directly developed by studying Applied Psychology and Everyday Life?', 'options': ['Choosing and applying relevant concepts', 'Ignoring assumptions', 'Avoiding calculations', 'Guessing without checking'], 'answer': 0, 'difficulty': 'moderate'},
                    {'question': '[Moderate] A strong solution involving Applied Psychology and Everyday Life should usually include:', 'options': ['Only a final answer', 'A relevant method and a check of the result', 'No explanation', 'An unrelated formula'], 'answer': 1, 'difficulty': 'moderate'},
                    {'question': '[Difficult] What best demonstrates mastery of Applied Psychology and Everyday Life?', 'options': ['Repeating one memorised example', 'Applying the ideas to an unfamiliar problem and justifying the method', 'Skipping foundational ideas', 'Selecting an answer at random'], 'answer': 1, 'difficulty': 'difficult'},
                ],
            },
        ],
    },
}
