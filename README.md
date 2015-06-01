# test-driven-python-development

This repository contains all the code examples from the book "Test-Driven Python Development". The author has made available a public github repository with the code samples from the book at https://github.com/siddhi/test_driven_python/

This book explores the Test-Driven Development approach to software development, using Python 3.4. It is assumed that the reader has an intermediate understanding of the Python Programming language and its rich set of features, although the author presents a comprehensive description of these features as they are needed throughout the book.

If you're interested, get the book from Amazon: http://amzn.to/1AvKq4H

The code examples were copied (and completed where necessary) from "Test-Driven Python Development" by Miguel Rentes (miguel.rentes@gmail.com).

His blog is at https://rentes.github.io

--------------------

###Table of Contents
- [Chapter 1: Getting Started with Test-Driven Development](#Chap1)
- [Chapter 2: Red-Green-Refactor - The TDD Cycle](#Chap2)
- [Chapter 3: Code Smells and Refactoring](#Chap3)
- [Chapter 4: Using Mock Objects to Test Interactions](#Chap4)
- [Chapter 5: Working with Legacy Code](#Chap5)

<div id='Chap1' />
## Getting Started with Test-Driven Development

Chapter 1 introduces the concept of TDD, how it is different from other forms of unit and integration testing, and the Red-Green-Refactor workflow. After that, we write out first test, using Python's already bundled unittest framework. On the final pages, we reorganize the project structure (which is suitable for larger and more complex projects), and update our testing procedure to run again our test suite after the project reorganization.

<div id='Chap2' />
## Red-Green-Refactor - The TDD Cycle

Chapter 2 starts going further into the definition of the TDD as being an explicit requirements translation into a test. Put it simply, in TDD tests are the software requirements. In this way, we can be assured that whenever the implementation is drifting away from the set requirements, the tests will always fail. This is a great advantage of using TDD. Along this chapter we use the assert family of methods to complete our tests, the Arrange-Act-Assert pattern, what brittle tests are and ways to overcome them. Finally we do a few basic refactorings to keep the code simple and DRY.

<div id='Chap3' />
## Code Smells and Refactoring

Chapter 3 looks at some Code Smells we always want to avoid, and also explores refactoring patterns to fix them, step-by-step explaining each one, to easily build a test suite which is correct, simpler to read and that avoids the code smells detected at the start of this chapter. The DRY and Single Responsibility principles are also explained thoroughly along with other patterns, which makes this chapter an excellent read. Test-Driven Development and these Refactoring Principles should always be applied if possible to every software project.

<div id='Chap4' />
## Using Mock Objects to Test Interactions

On Chapter 4 we look at how we can use mock objects to test that interactions between multiple objects occurs as we planned to. We learn how to use the unittest.mock module provided by Python, which is a very powerful mocking framework, and a very easy to use as well, as this Chapter demonstrates. Finally, we see how to use patching for a more advancing mocking and we then put all of the mocking techniques into practice to achieve a more complex mocking example for our stock application. This chapter also makes the important distinction between mocks, stubs, fakes and spies. It's well worth a read, if you haven't used mocking before on your software projects.

<div id='Chap5' />
## Working with Legacy Code

This chapter tells us how to deal with software projects which have no tests. Unfortunately, there are always pieces of code (if not always the whole project) that don't have tests. This chapter provides precious advice on how to change the legacy code to accomodate for Test-Driven Development and take the most out of this practice. We see how to use the Python Interactive shell (IPython) and the Python debugger (pdb) to understand how a legacy code works, and we also explore the functionality of many different techniques to write many more tests, such as: characterization tests, breaking dependencies, separating initialization from execution, using default values for parameters, stubbing local methods, using the Rope refactoring library and the extract method refactoring for this effect.
