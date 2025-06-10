# Improving code assessment by organizing tests into test plans

**Framework**: Xcode

Control the information you receive from your tests at different stages in the software engineering process by creating and configuring test plans.

#### Overview

A mature project benefits from many tests that cover a variety of scenarios. Tests can verify code behavior or measure performance; they can test different products, or the same product on different targets or configurations. They can be long-running UI tests that exercise complex workflows or small unit tests that exercise individual functions, as described in [`Testing`](testing.md).

Control the information you receive from your tests at different stages in the software engineering process by organizing these tests into test plans, and configuring how Xcode executes the test plans. For example, you can create a test plan to run only the unit tests for a module while developing and debugging that module, and a second test plan to run all unit, integration, and UI tests before submitting your app to the App Store.

![A graph that demonstrates the components of an Xcode project that Xcode uses to determine the test activities: the test plan, scheme, test target, and product target.](https://docs-assets.developer.apple.com/published/fb97d06a00af6ecfbd44b2bb7f03d5d6/organizing-tests-hero%402x.png)

With [`Swift Testing`](https://developer.apple.com/documentation/Testing), you can declare and add , annotations that identify tests that share common characteristics, to your tests.

You might add tags to specify:

- priority level (critical, normal, low)
- kind (unit, integration, performance)
- cadence (presubmission, daily, prerelease)
- functional area
- dependancies

In Xcode 16 and later, you can use tags in your test plans to specify which tests to include. For more information about declaring tags and adding tags to test, see [`Adding tags to tests`](https://developer.apple.com/documentation/Testing/AddingTags). For more information about migrating your existing unit test to Swift Testing, see [`Migrating a test from XCTest`](https://developer.apple.com/documentation/Testing/MigratingFromXCTest).

> **Note**: Tags aren’t a replacement for test suites. Suites impose hierarchical structure on test functions at the source level, while tags help you associate tests from different files, suites, and targets.

##### Create Schemes to Associate Test Targets with Products

A scheme instructs Xcode to use specific targets when you invoke the building, testing, running, analyzing, profiling, and archiving actions, shown in the figure below. In the test action for a scheme, include the target for the product under test along with the test targets that contain tests relevant to that product.

![A graph that demonstrates that an Xcode scheme associates the product target, test targets, and test plans to define the behavior of the test action.](https://docs-assets.developer.apple.com/published/5560df6f4b4819787683711587780c35/organizing-tests-scheme%402x.png)

For information on creating Xcode schemes and assigning targets to schemes, see [`Customizing the build schemes for a project`](customizing-the-build-schemes-for-a-project.md).

If your product has multiple targets — like an iOS app that contains a static library and a widget extension — create a scheme for each of the individual targets in addition to an “umbrella” scheme that builds the whole product suitable for release. Developers on your team can use the more specific scheme when working on tasks in each target, running only the tests relevant to that target to get faster feedback. When they are ready to integrate their changes, developers can get better assurance that they have not introduced regressions by running the complete collection of tests in the umbrella scheme.

##### Create Test Plans to Organize the Tests for a Scheme

A  is a document in your Xcode project that describes which tests Xcode should run when a developer invokes the test action, shown in the figure below, and the configurations Xcode uses to run the tests.

![A graph that demonstrates that a test plan defines which test suites and functions Xcode should run in the test action.](https://docs-assets.developer.apple.com/published/e0d2c677e6d19db8eb5dab4a06e54fd6/organizing-tests-test-plan%402x.png)

You can create multiple test plans for the same scheme and use any of them when running tests from Xcode or in Terminal. You must choose one test plan as the default plan for the scheme; Xcode uses this plan to run tests when none is explicitly specified. Xcode creates a default test plan that includes all of the tests from the test targets built by your scheme.

![A screenshot of the scheme editor in Xcode that shows an automatically created Test plan.](https://docs-assets.developer.apple.com/published/dbb23f1f5938ea8c7140b6059164d254/organizing-tests-autocreated-test-plan%402x.png)

To edit this test plan, choose Product > Scheme > Edit Test Plan. Xcode prompts you for a location to save the test plan.

To create additional test plans:

1. Choose Product > Test Plan > New Test Plan.
2. Enter a name for the new test plan.
3. Choose a location to save the test plan.
4. Click Create.

To select the default test plan for the current scheme:

1. Choose Product > Test Plan > Manage Test Plans.
2. Select the radio button in the Default column next to the desired test plan.

![A screenshot of the scheme editor in Xcode with the Test pane shown. The pane include one automatically created Test plan.](https://docs-assets.developer.apple.com/published/cb09ef07db9a79c120f1dc5d9f1baf4c/organizing-tests-new-test-plan%402x.png)

##### Include or Exclude Tests From a Test Plan

Specify the test targets to use, along with any tags Xcode should use to determine which tests to include or exclude from a test plan:

1. Select the test plan in the Project navigator.
2. In the Tests pane, click Choose Targets to add test targets to the test plan.
3. To include tests annotated with a tag, click the Include Tags text field and type the symbol name of one or more tags. Select Any Tag from the filter button to include a test when it matches any the tags you enter, and All Tags to include it only when it matches all of the tags.
4. To exclude tests annotated with a tag, enter the symbol name of one or more tags to exclude in the Exclude Tags field. Select Any Tag from the filter button to exclude a test when it matches any the tags you enter, and All Tags to exclude it only when it matches all of the tags.

![A screenshot of the Include Tags and Exclude Tags fields in the Test Plan editor in Xcode. The Include Tags field contains tags for formatting and unit. The Exclude Tags field contains tags for stress and release. The filter button in the Exclude Tags field is expanded to show options for Any Tag and All Tags.](https://docs-assets.developer.apple.com/published/4fde76520a0d32738f8185a02142528f/organizing-tests-test-plan-exclude-tags%402x.png)

To include all your tests in the test plan, leave the Include Tags and  Exclude Tags fields empty.

##### Choose the Test Suites and Functions to Run in a Test Plan

To further filter the tests that Xcode runs for a given test plan, select the checkbox in the Included column next to an item in the test plan’s outline view. You can select or deselect any item that matches the conditions from the Include Tags and Exclude Tags fields. The items represent targets, suites, functions, and specific input parameters passed to parameterized test functions. Xcode displays the symbol names for tags under the Tags column next to the suites and functions they annotate. Hold the pointer over an item to display a right arrow button. Click the button to display the source code for that item in the Source editor.

If you exclude a test function or test case from a test plan, Xcode skips over the test function or test case and doesn’t provide feedback on their status. The only effect an excluded test function has on the outcome of the test action is if the test contains a build error, in which case the whole test action fails.

Swift Testing and XCTest support ways to modify the effect a test has on the outcome of a test action while still running it. In Swift Testing you use traits to control the runtime conditions under which test should run, see [`Enabling and disabling tests`](https://developer.apple.com/documentation/Testing/EnablingAndDisabling) and [`Known issues`](https://developer.apple.com/documentation/Testing/known-issues) to indicate tests you expect to fail. To skip a test because the execution platform or configuration is inappropriate for the test in XCTest, use [`XCTSkipIf(_:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTSkipIf(_:_:file:line:)) or [`XCTSkipUnless(_:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTSkipUnless(_:_:file:line:)). To indicate that a test is expected to fail in XCTest, use [`XCTExpectFailure(_:options:)`](https://developer.apple.com/documentation/XCTest/XCTExpectFailure(_:options:)).

##### Adjust Configurations for Test Plans

Each test plan contains one or more configurations that tell Xcode how to set up the runtime environment for the tests. In the Configurations tab of the test plan editor, shown in the figure below, you can set environment variables, enable additional checks such as the address sanitizer and memory management guards, and choose different localization settings for the code.

![A screenshot of Xcode, showing the test plan configuration editor.](https://docs-assets.developer.apple.com/published/cbdf4697b741d31cb64de2281186a857/organizing-tests-configurations%402x.png)

The values you can specify in a test plan configuration are:

For more information on the address sanitizer, thread sanitizer, undefined behavior sanitizer, and main thread checker, see [`Diagnosing memory, thread, and crash issues early`](diagnosing-memory-thread-and-crash-issues-early.md).

To create additional test plan configurations, click the Add button. Xcode runs the tests specified in a test plan once for each of that plan’s configurations.

##### Add a Test Plan to a Scheme

You can associate a test plan with more than one scheme, to get the same test suites and functions included with the same configurations in multiple schemes. To add an existing test plan to a scheme, do the following:

1. Choose Product > Test Plan > Manage Test Plans.
2. Click the Add button below the list of test plans.
3. Choose Add existing Test Plan.
4. Select the test plan you want to add to the scheme.

##### Run the Tests Specified in a Test Plan in Xcode

When Xcode runs the test action, it executes the tests in the active test plan once for each configuration in the test plan. To set the active test plan and run the tests specified in that plan, do the following:

1. Choose Product > Test Plan.
2. Select the test plan you want to run.
3. Choose Product > Test.

For information about interpreting the results of tests in Xcode, see [`Running tests and interpreting results`](running-tests-and-interpreting-results.md).

##### Run Tests From the Command Line

To run tests using a specific test plan from the command-line, you must explicitly name the test plan to use. To discover the test plans for `SampleApp`, run the following:

```zsh
% xcodebuild -scheme SampleApp -showTestPlans
```

To run the tests specified in the “Performance Tests” test plan, run the following:

```zsh
% xcodebuild -scheme SampleApp test -testPlan Performance\ Tests
```

To run the tests in the “Performance Tests” test plan, using only the configuration called “My Config”, run the following:

```zsh
% xcodebuild -scheme SampleApp test -testPlan Performance\ Tests --only-test-configuration My\ Config
```

To run the tests in the “Performance Tests” test plan, using all configurations except “My Config”, run the following:

```zsh
% xcodebuild -scheme SampleApp test -testPlan Performance\ Tests --skip-test-configuration My\ Config
```

## See Also

- [Adding tests to your Xcode project](adding-tests-to-your-xcode-project.md)
  Include test targets that build code to test the logic in your functions, check for integration issues, automate UI workflows, and measure performance.
- [Updating your existing codebase to accommodate unit tests](updating-your-existing-codebase-to-accommodate-unit-tests.md)
  Remove coupling between components to increase test coverage and reliability.
- [Determining how much code your tests cover](determining-how-much-code-your-tests-cover.md)
  Use code coverage to focus new test development on areas that lack adequate testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/organizing-tests-to-improve-feedback)*