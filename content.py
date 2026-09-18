"""
All lesson and quiz content lives here as plain Python data.
To add a new lesson: append a dict with the same shape to a subject's "lessons" list.
Lesson ids inside a subject must be consecutive integers starting at 1 — lessons unlock in order.
Each quiz question's "answer" is the index (0-based) of the correct option.
"""

SUBJECTS = {
    "maths": {
        "name": "Mathematics",
        "lessons": [
            {
                "id": 1,
                "title": "Introduction to Algebra",
                "content": """
                    <p>Algebra is the branch of maths that uses letters (like <b>x</b> and <b>y</b>)
                    to stand in for unknown numbers.</p>
                    <p>An equation such as <code>x + 5 = 12</code> asks: what number, added to 5,
                    gives 12? Here, <code>x = 7</code>.</p>
                    <p>The core idea: whatever you do to one side of an equation, you must do to
                    the other side, to keep it balanced.</p>
                """,
                "quiz": [
                    {
                        "question": "What does 'x' usually represent in algebra?",
                        "options": ["A fixed number", "An unknown value", "A unit of measurement", "A type of graph"],
                        "answer": 1,
                    },
                    {
                        "question": "Solve: x + 5 = 12. What is x?",
                        "options": ["5", "6", "7", "17"],
                        "answer": 2,
                    },
                    {
                        "question": "To keep an equation balanced, what must you do?",
                        "options": [
                            "Nothing, just guess the answer",
                            "Apply the same operation to both sides",
                            "Only change the left side",
                            "Only change the right side",
                        ],
                        "answer": 1,
                    },
                ],
            },
            {
                "id": 2,
                "title": "Basic Geometry: Angles and Shapes",
                "content": """
                    <p>Geometry studies shapes, sizes, and the space they take up.</p>
                    <p>A triangle's three interior angles always add up to <b>180 degrees</b>.
                    A square has four equal sides and four 90-degree angles.</p>
                    <p>The perimeter of a shape is the total length around its edges; the area is
                    the amount of space it covers.</p>
                """,
                "quiz": [
                    {
                        "question": "The interior angles of a triangle add up to:",
                        "options": ["90 degrees", "180 degrees", "270 degrees", "360 degrees"],
                        "answer": 1,
                    },
                    {
                        "question": "How many sides does a square have?",
                        "options": ["3", "4", "5", "6"],
                        "answer": 1,
                    },
                    {
                        "question": "The distance around the outside of a shape is called its:",
                        "options": ["Area", "Volume", "Perimeter", "Diameter"],
                        "answer": 2,
                    },
                ],
            },
        ],
    },
    "physics": {
        "name": "Physics",
        "lessons": [
            {
                "id": 1,
                "title": "Introduction to Motion",
                "content": """
                    <p>Motion describes how an object's position changes over time.</p>
                    <p><b>Speed</b> is how fast something moves, calculated as distance divided
                    by time. <b>Velocity</b> is speed with a direction.</p>
                    <p>If a car travels 100 km in 2 hours, its average speed is 50 km/h.</p>
                """,
                "quiz": [
                    {
                        "question": "Speed is calculated as:",
                        "options": ["Time divided by distance", "Distance divided by time", "Distance times time", "Mass divided by time"],
                        "answer": 1,
                    },
                    {
                        "question": "What makes velocity different from speed?",
                        "options": ["Velocity includes direction", "Velocity is always faster", "Velocity has no units", "There is no difference"],
                        "answer": 0,
                    },
                    {
                        "question": "A car travels 100 km in 2 hours. Its average speed is:",
                        "options": ["25 km/h", "50 km/h", "100 km/h", "200 km/h"],
                        "answer": 1,
                    },
                ],
            },
            {
                "id": 2,
                "title": "Forces and Newton's Laws",
                "content": """
                    <p>A force is a push or a pull. Newton's first law says an object at rest
                    stays at rest, and an object in motion stays in motion, unless a force
                    acts on it.</p>
                    <p>Newton's second law: <code>Force = mass &times; acceleration</code>.</p>
                    <p>Newton's third law: every action has an equal and opposite reaction.</p>
                """,
                "quiz": [
                    {
                        "question": "Newton's first law is also known as the law of:",
                        "options": ["Gravity", "Inertia", "Reaction", "Energy"],
                        "answer": 1,
                    },
                    {
                        "question": "Newton's second law is written as:",
                        "options": ["F = m / a", "F = m + a", "F = m x a", "F = a / m"],
                        "answer": 2,
                    },
                    {
                        "question": "Newton's third law states that every action has:",
                        "options": ["No reaction", "A smaller reaction", "An equal and opposite reaction", "A delayed reaction"],
                        "answer": 2,
                    },
                ],
            },
        ],
    },
    "computer_science": {
        "name": "Computer Science",
        "lessons": [
            {
                "id": 1,
                "title": "How Computers Store Data",
                "content": """
                    <p>Computers store all data as <b>binary</b> — sequences of 0s and 1s,
                    called bits.</p>
                    <p>8 bits make up 1 <b>byte</b>. A byte can represent a number from 0 to 255,
                    or one character of text.</p>
                    <p>Everything from photos to videos to this lesson is ultimately stored as
                    patterns of bits.</p>
                """,
                "quiz": [
                    {
                        "question": "Computers store data using:",
                        "options": ["Decimal digits (0-9)", "Binary digits (0-1)", "Letters only", "Roman numerals"],
                        "answer": 1,
                    },
                    {
                        "question": "How many bits make up one byte?",
                        "options": ["4", "8", "16", "32"],
                        "answer": 1,
                    },
                    {
                        "question": "A single bit can be:",
                        "options": ["0 or 1", "Any number 0-9", "A letter", "A whole byte"],
                        "answer": 0,
                    },
                ],
            },
            {
                "id": 2,
                "title": "Introduction to Algorithms",
                "content": """
                    <p>An algorithm is a step-by-step set of instructions for solving a problem
                    or completing a task.</p>
                    <p>A simple example: to find the largest number in a list, start by
                    assuming the first number is the largest, then compare it to each other
                    number, updating your answer whenever you find a bigger one.</p>
                    <p>Good algorithms are precise, finite (they eventually stop), and produce
                    a correct result.</p>
                """,
                "quiz": [
                    {
                        "question": "An algorithm is best described as:",
                        "options": [
                            "A programming language",
                            "A step-by-step set of instructions",
                            "A type of computer hardware",
                            "A file format",
                        ],
                        "answer": 1,
                    },
                    {
                        "question": "A good algorithm should eventually:",
                        "options": ["Run forever", "Stop and produce a result", "Use no memory", "Ignore the input"],
                        "answer": 1,
                    },
                    {
                        "question": "To find the largest number in a list, you should:",
                        "options": [
                            "Guess randomly",
                            "Sort the list alphabetically",
                            "Compare each number and keep track of the biggest so far",
                            "Only look at the last number",
                        ],
                        "answer": 2,
                    },
                ],
            },
        ],
    },
}
