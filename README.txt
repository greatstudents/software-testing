Author: Jiali Huang
Title: Coverage-based Test Case Selection

Scikit-Learn is a Machine-Learning library for Python.
Git Repository URL for Scikit-Learn: https://github.com/scikit-learn/scikit-learn

Scipy is an open source Python library used by scientists, analysts, and engineers for scientific and technical computing.
Git Repository URL for Scipy: https://github.com/scipy/scipy

NumPy is an extension for Python, adding support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions.
Git Repository URL for Numpy: https://github.com/numpy/numpy

Coverage.py are tools for measuring code coverage of Python programs. It monitors the program, noting which parts of the code have been executed; it then analyzes the source to identify code that could have been executed but was not. Unit test discovery and execution frameworks are used to add tests to existing code, execute those tests, and compile a simple report, without ‘thinking’. 
Coverage.py document webpage: https://coverage.readthedocs.io/en/coverage-4.0.3/


Nose test is a tool for running unit tests, and has a useful plug-in architecture that enables users to extend it in convenient ways; it can be adapted to mimic any unit test discovery framework simply.
Nose document webpage: http://nose.readthedocs.io/en/latest/testing.html

There are many test cases in upper-level components and each test case covers different dependencies’ code. Firstly, we use coverage tool to generate coverage data of upper-level components’ for each test case. Then, we collect diff data that are line changes between different dependencies’ revision. Finally, we match coverage data to diff data. If the test case’s coverage data overlaps the same lines that change between revisions, then the test case needs to be rerun. For the matching part, the diff data and coverage data are parsed to the same format. 

Command to run Coverage plug-in in Nose in Terminal:"nosetests --with-coverage -s -v --cover-erase FILE_NAME"
