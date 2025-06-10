# Grouping Tests into Substeps with Activities

**Framework**: XCTest

Simplify test reports by creating activities that organize substeps within complex test methods.

#### Overview

Use activities to break longer test methods, such as UI tests and integration tests, into smaller named substeps.

Each activity wraps a block of code, giving the code a name. You can nest and call activities within other activities. Xcode test reports organize results by activity name, making test reports for complex, multistep tests easier to understand.

For long test methods, especially in UI tests that contain lots of steps, simplify your test methods by refactoring them into utility methods or substeps with activities.

##### Organize Long Test Methods Into Substeps

Identify the substeps that you want to group into named activities. For example, you might break down a login UI test into three substeps: opening the login window, entering a password, and closing the login window. Then, create named activities for each substep you identify.

Activities run against the current testing context, represented by [`XCTContext`](xctcontext.md). To run a block of code as an activity, call the [`runActivityNamed:block:`](xctcontext/runactivitynamed:block:.md) class method on `XCTContext`, passing your test code as the block to execute.

##### Build Utility Methods From Common Test Substeps

Convert common test substeps into self-contained utility methods for reuse in multiple tests with activities. For example, if you have three UI tests that each require the user to be logged in, extract the login process into a utility method that wraps the process inside an activity called `Login`, and call the utility method from within each test method. The login activity appears in the Xcode test report for each test method that calls it.

If the login fails, the login activity adds a screenshot as an attachment for later investigation. For more information, see [`Adding Attachments to Tests, Activities, and Issues`](adding-attachments-to-tests-activities-and-issues.md).

You can use `XCTContext` anywhere within your test target, not just within test methods on an [`XCTestCase`](xctestcase.md) subclass. This enables you to define activities in your own utility code, such as in custom methods on subclasses of [`XCUIApplication`](https://developer.apple.com/documentation/XCUIAutomation/XCUIApplication) or [`XCUIElement`](https://developer.apple.com/documentation/XCUIAutomation/XCUIElement).

## See Also

- [class XCTContext](xctcontext.md)
  A proxy for the current testing context.
- [protocol XCTActivity](xctactivity.md)
  A named substep of a test method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/grouping-tests-into-substeps-with-activities)*