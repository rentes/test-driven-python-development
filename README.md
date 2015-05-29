# test-driven-python-development

This repository contains all the code examples from the book "Test-Driven Python Development". The author has made available a public github repository with the code samples from the book at https://github.com/siddhi/test_driven_python/

This book explores the Test-Driven Development approach to software development, using Python 3.4. It is assumed that the reader has an intermediate understanding of the Python Programming language and its rich set of features, although the author presents a comprehensive description of these features as they are needed throughout the book.

If you're interested, get the book from Amazon: http://amzn.to/1AvKq4H

The code examples were copied (and completed where necessary) from "Test-Driven Python Development" by Miguel Rentes (miguel.rentes@gmail.com).

His blog is at https://rentes.github.io

--------------------

###Table of Contents
[Chapter 1: Getting Started with Test-Driven Development](#Chap1)

[Chapter 2: Red-Green-Refactor - The TDD Cycle](#Chap2)

<div id='Chap1' />
## Getting Started with Test-Driven Development

Chapter 1 introduces the concept of TDD, how it is different from other forms of unit and integration testing, and the Red-Green-Refactor workflow. After that, we write out first test, using Python's already bundled unittest framework. On the final pages, we reorganize the project structure (which is suitable for larger and more complex projects), and update our testing procedure to run again our test suite after the project reorganization.

<div id='Chap2' />
## Red-Green-Refactor - The TDD Cycle

Chapter 2 starts going further into the definition of the TDD as being an explicit requirements translation into a test. Put it simply, in TDD tests are the software requirements. In this way, we can be assured that whenever the implementation is drifting away from the set requirements, the tests will always fail. This is a great advantage of using TDD. Along this chapter we use the assert family of methods to complete our tests, the Arrange-Act-Assert pattern, what brittle tests are and ways to overcome them. Finally we do a few basic refactorings to keep the code simple and DRY.
