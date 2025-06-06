# Adding tests to your Xcode project

**Framework**: Xcode

Include test targets that build code to test the logic in your functions, check for integration issues, automate UI workflows, and measure performance.

#### Overview

When creating a new project in Xcode 16 and later, choose a Testing System from the pop-up menu in the options dialog and let Xcode configure your project with test bundles.

Xcode includes two testing frameworks:

The options for testing system are Swift Test with XCTest UI Tests and XCTests for Unit and UI Tests. After making a selection, Xcode adds two types of test targets to your project, one for your unit tests with a name ending in “Tests” and one for your UI tests with a name ending in “UITests”. You’ll find the matching name for each of these targets in the Project navigator, along with a template file you can use to start writing your first tests. Your testing system choice impacts the primary framework Xcode includes in the file template for unit tests. Previous versions of Xcode included these targets when you enabled the Include Tests option when creating a new project and included file templates that use XCTest.

##### Add a New Testing Target

If you need to add testing to additional targets or have an existing target you want to add tests to:

1. Chose File > New > Target.
2. Type “Test” in the template filter.
3. Select Unit Testing Bundle or UI Testing Bundle.
4. Click Next.
5. Fill out the options.
6. Click Finish.

> **Note**: Swift Testing and XCTest can build from the same test target and coexist inside the same test bundle. If your project already contains a test bundle with unit tests written using XCTest, you don’t need to add a new Unit Testing Bundle to your project to start writing unit test with Swift Testing. You can add additional files to the target using Swift Testing and consider converting your old tests as time allows.

##### Write a Unit Test

To write a test, select a test file from your test target, and choose a type or function to write a unit test for. If you need to add a new test file to your target,  choose File > New > New File From Template, then select Swift Testing Unit Test or XCTest Unit Test to add a test file with the appropriate structure. The test function that implements the unit test has the following three steps, in order:

1.  — Create any objects or data structures that the code path you’re exercising uses. Replace complex dependencies with “stubs” that are easy to configure to ensure that tests run quickly and are deterministic. Adopting dependency injection and protocol-oriented programming ensures that relationships between objects in your app are sufficiently flexible to enable substitution of real implementations for stubs.
2.  — Call the method or function that you’re testing, using parameters and properties that you configure in the Arrange phase.
3.  — Use [`Expectations and confirmations`](https://developer.apple.com/documentation/Testing/Expectations) in Swift Testing or Test Assertions in [`XCTest`](https://developer.apple.com/documentation/XCTest) to compare the behavior of the code you exercise in the Act phase with your expectations of what should happen. Any expectation whose condition is false causes a test to fail.

In Swift Testing, Test functions are just ordinary Swift functions that you add the the `Test` attribute to. They can be global functions or methods in a type. You can optionally identify suites, types that contain test functions, by marking them with the `Suite` attribute. You can mark them async or throws, or isolate them to a global actor.

For tests you create with XCTest, create a subclass of [`XCTestCase`](https://developer.apple.com/documentation/XCTest/XCTestCase) to contain test methods. Add a method to your `XCTestCase` subclass that takes no arguments and returns `Void`, giving the method a name that begins with the word “`test`”.

Cover multiple paths and test for each scenario. For example, if a function receives an optional parameter, test the parameter as `nil` and test a non-`nil` value. Identify the boundary cases and logical branches in your code, and write a unit test to cover each combination of these cases. To test multiple paths through a function or method in your project using Swift Testing, implement parameterized test functions. For more information, see [`Implementing parameterized tests`](https://developer.apple.com/documentation/Testing/ParameterizedTesting). In XCTest, each unit test should assert the expected behavior of a single path through a method or function in your project. To cover multiple paths, write one test for each scenario.

For more information on defining tests using Swift Testing, see [`Defining test functions`](https://developer.apple.com/documentation/Testing/DefiningTests). For more information on defining tests using XCTest, see [`Defining Test Cases and Test Methods`](https://developer.apple.com/documentation/XCTest/defining-test-cases-and-test-methods).

> **Note**: The Swift access control model prevents an external entity from accessing anything declared as internal. To access items declared as internal from your test code, compile the module your test code needs to access with [`Enable Testability`](build-settings-reference#Enable-Testability.md) and add the `@testable` attribute to the import statement for the module. For more information, see [`Access Control`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/accesscontrol/#Access-Levels-for-Unit-Test-Targets).

##### Write an Integration Test

Integration tests look very similar to unit tests, use the same APIs, and follow the same Arrange-Act-Assert pattern. The difference between a unit test and an integration test is one of scale. While a unit test covers a very small part of your app’s logic, an integration test examines the behavior of a larger subsystem, or combination of classes and functions. In the Arrange step of an integration test, widen the scope of real project code that’s under test, using fewer stub objects.

Rather than trying to cover every different condition or boundary case as with unit tests, use integration tests to assert that components work together to achieve app goals in important situations. Examples include testing that a value received from a controller is stored in the model correctly, and that an error produced by a network request gets passed to and presented by the user interface.

##### Write a Ui Test

UI tests work in a different way from unit and integration tests. The XCTest UI Test template for new files contains the common starting points for UI tests. You implement the UI tests for your app using XCTest in a subclass of [`XCTestCase`](https://developer.apple.com/documentation/XCTest/XCTestCase). Rather than executing your app’s code directly, they use the app’s user-interface controls to determine whether the user can complete a specific task using the app.

Create UI tests to verify that the app can accomplish a tasks in response to user interactions, and that bugs haven’t been introduced that break the behavior of UI controls. UI tests that replicate real user activities provide confidence that the app can be used for its intended task. A UI test for a document-based app might verify that the user can create a new document, edit its content, then delete the document.

To create a UI test in a method on an `XCTestCase` subclass, record your interaction with the app using the Record UI Test feature in Xcode. Design UI tests to replicate the most critical workflows that would affect users if they broke, and to replay reported bugs to avoid regressions.

![Image showing the Record UI Tests button in Xcode.](https://docs-assets.developer.apple.com/published/af3223bfb6cc09fe1d5ff0a0d0ca9912/adding-tests-to-your-xcode-project-ui-record%402x.png)

When recording a workflow that exercises the functionality you’re testing, use the test assertion functions to ensure that the final state of the UI is what you’d expect, given the actions performed during the recorded interaction.

```swift
class MyUITests: XCTestCase {
    let app = XCUIApplication()

    // MARK: - Setup and Teardown
        
    override func setUp() {
        super.setUp()
        // In UI tests, it's prudent to stop the test immediately if a failure occurs.
        continueAfterFailure = false
        // UI tests must launch the app that they test. Do this in setup to ensure that it the app launches for each test method.
        XCUIApplication().launch()
    }

    override func tearDown() {
        // Put teardown code here. The test runner calls this method after the invocation of each test method in the class.
        super.tearDown()
    }
    
    func testAddition() {
        // Perform UI actions to accomplish a task.
        // Check the expected state UI value.
        if let value = app.<ui_type>[<ui_identifier>].value as? String {
            XCTAssertTrue(value = /* … */, "The function didn't return the expected result")
        }        
    }
}
```

Where UI tests imitate complex workflows with multiple distinct steps, use [`XCTActivity`](https://developer.apple.com/documentation/XCTest/XCTActivity) to organize and name the shared steps. Create helper methods to share implementations of activities that you use in multiple tests.

##### Write a Performance Test

Write performance tests to gather information on time taken, memory used, or data written, during the execution of a region of code. XCTest runs your code multiple times, measuring the requested metrics. You can set a baseline expectation for the metric, and if the measured value is significantly worse than the baseline, XCTest reports a test failure.

To test time taken by your code, call [`measure(_:)`](https://developer.apple.com/documentation/XCTest/XCTestCase/measure(_:)) inside your test method, and run your app’s code inside the block argument to `measure(_:)`. To measure performance using other metrics, including memory use and amount of data written to disk, call [`measure(metrics:block:)`](https://developer.apple.com/documentation/XCTest/XCTestCase/measure(metrics:block:)).

```swift
class PerformanceTests : XCTestCase {
    func testCodeIsFastEnough() {
        self.measure() {
          // Place performance-sensitive code here.
        }
    }
}
```

## See Also

- [Updating your existing codebase to accommodate unit tests](updating-your-existing-codebase-to-accommodate-unit-tests.md)
  Remove coupling between components to increase test coverage and reliability.
- [Determining how much code your tests cover](determining-how-much-code-your-tests-cover.md)
  Use code coverage to focus new test development on areas that lack adequate testing.
- [Improving code assessment by organizing tests into test plans](organizing-tests-to-improve-feedback.md)
  Control the information you receive from your tests at different stages in the software engineering process by creating and configuring test plans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/adding-tests-to-your-xcode-project)*