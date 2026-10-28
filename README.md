# Python & SQL · Homework

Course assignments covering loops, collections, functions, small games, SQL queries and regression. Each solution stays in its original date folder.

**Status:** learning archive; some answers are unfinished. [Browse every exercise by topic](TOPICS.md).

| Practice | Navigation |
| --- | --- |
| Input, loops, match-case and formatting | [Control flow](TOPICS.md#loops-branching-and-input) |
| Lists, sets, dictionaries and grouping | [Collections](TOPICS.md#lists-sets-and-grouping) |
| Reusable functions and returned values | [Functions](TOPICS.md#functions-and-dictionaries) |
| Quizzes, random games and validation | [Problem solving](TOPICS.md#games-and-problem-solving) |
| SQL filtering and distinct values | [SQL](TOPICS.md#sql-queries) |
| Regression, metrics and plots | [Data science](TOPICS.md#regression-and-visualization) |

## Run a small exercise

Use Python 3.12+ for the mixed coursework syntax. From the repository root:

```bash
python3 '11.2/Lists & Built-in Functions_q1.py'
```

This example uses only the standard library. Other exercises can require interactive input. The graphical slot-machine exercise needs Pygame; the regression exercise imports NumPy, pandas, IPython, matplotlib, seaborn and scikit-learn. There is no shared locked environment. Use a local virtual environment for whichever optional dependencies you need.

The SQL exercises and `ekom__homework_database.db` are retained. Use a disposable database copy when experimenting; scripts may change tables or data.

## Learning and verification

The progression is from input validation and collection operations to functions, grouping, queries and model evaluation. Original comments and answers remain unchanged so they can be reviewed alongside class notes.

No automated test suite is configured. The documentation check found an existing syntax error in [Digital Business Card](11.3/Question%201%20%E2%80%93%20Digital%20Business%20Card.py): its opening function declaration is unfinished. It is preserved as coursework, not presented as runnable. The topic links and representative noninteractive examples are checked separately from answer correctness.

[Related classwork](https://github.com/LOVA-malamud/LOVA_M) · [Python exam](https://github.com/LOVA-malamud/exam_1_ekom)

On 2026-10-28, the list example above ran successfully under Python 3.12.10; it ended with six values totaling 244.
