# Running tests and interpreting results

**Framework**: Xcode

Determine whether your project’s code behaves as you expect by running tests and understanding the results.

#### Overview

At different points in the software development workflow you’ll want to run subsets of your tests:

- While making changes to a particular function or type, running just the tests relevant to that unit gives you the fastest feedback about the state of your changes.
- When your change is ready for code review or integration, running all of the tests for the affected target can uncover any unexpected regressions.
- Finally, Xcode Cloud can run a complete set of tests with multiple configurations on a schedule, providing greater confidence in the correctness of your code while managing the increased execution time required for completing so many tests.

#### Run Tests From a Test Plan

To run all the tests in the active test plan, you have two options: you can run them in Xcode (choose Product > Test), or you can run the `xcodebuild` command in Terminal:

```zsh
% xcodebuild test -scheme SampleApp
```

Configure which tests the test runner runs when you perform this action by editing the test plan for your Xcode target’s scheme. For more information, see [`Customizing the build schemes for a project`](customizing-the-build-schemes-for-a-project.md). If your build scheme includes more than one test plan, choose Product > Test Plan to select a test plan to run. View the active plan under the Test navigator, choose View > Navigators > Tests. When you select a different test plan or a different build scheme, the Test navigator updates to display that plan. Expand the outline view for the plan to see the targets, suites, test functions, and parameterized test cases it includes. Items you disable or mark to be skipped appear dimmed.

#### Interpret Test Results

After your test run, Xcode displays a status icon in the Test navigator next to the test plan and next to each item in its outline view.

![The source editor display the implementation for a test with a  red-filled rounded diamond-shaped icon that contains an ex in the gutter and a debug message to the right.](https://docs-assets.developer.apple.com/published/dc36b2f29f8b96e6e1ee73d80b3df898/running-tests-and-interpreting-results-debug-message%402x.png)

The possible states are:

| Test status icon | Description |
| --- | --- |
| ![A green-filled rounded diamond-shaped icon that contains a checkmark.](https://docs-assets.developer.apple.com/published/11f29cc8ad9fe67b2a9ec70164a80b5a/check-green%402x.png) | The test passed. |
| ![A red-filled rounded diamond-shaped icon that contains an ex.](https://docs-assets.developer.apple.com/published/fe768de15f27d9032d048dcaf9d8da79/close-red%402x.png) | The test failed. The failure may also be due to a test that should fail but didn’t. |
| ![A gray-filled rounded diamond-shaped icon that contains an ex.](https://docs-assets.developer.apple.com/published/6d4688e170964c35740f942e5dbfd1c9/close-gray%402x.png) | The test failed with some expected failures, but there were no unexpected failures. |
| ![A gray-filled rounded diamond-shaped icon that contains an arrow that starts at the left corner and goes up toward the top curve of the diamond before curving downward to the right corner.](https://docs-assets.developer.apple.com/published/2f59b7b065262f0a8aaaa36dbf07a8e2/arrow-gray%402x.png) | Xcode skipped a test. |
| ![A green-filled rounded diamond-shaped icon that contains a minus sign.](https://docs-assets.developer.apple.com/published/193175cebe13c7a77a1f21e04779e51f/minus-green%402x.png) | A green icon with a minus sign (–) indicates that a test had a mixed outcome: some test functions or parameterized test cases passed, while others failed with expected failures or were skipped. |
| ![A red-filled rounded diamond-shaped icon that contains a minus sign.](https://docs-assets.developer.apple.com/published/b409cc9b3f6b06a0a04448c20713c663/minus-red%402x.png) | A red icon with a minus sign (–) indicates that the test had a mixed outcome; some of the test functions or parameterized test cases failed while others failed with expected failures or were skipped. |

> **Note**: Swift Testing and XCTest support ways to identify a test to skip or a test you expect to fail due to known issue. The status icon Xcode displays reflects this, as indicated in the table above. To learn about marking known issues and enabling tests using Swift Testing, see [`Known issues`](https://developer.apple.com/documentation/Testing/known-issues) and [`Enabling and disabling tests`](https://developer.apple.com/documentation/Testing/EnablingAndDisabling). To identify test functions you expect to fail using XCTest, call  [`XCTExpectFailure(_:options:)`](https://developer.apple.com/documentation/XCTest/XCTExpectFailure(_:options:)). To skip a test function, call [`XCTSkipIf(_:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTSkipIf(_:_:file:line:)) or [`XCTSkipUnless(_:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTSkipUnless(_:_:file:line:)), which raise instances of [`XCTSkip`](https://developer.apple.com/documentation/XCTest/XCTSkip-swift.struct).

Click to select an item in the Test navigator to display the implementation of a test in the source editor and access additional details for specific test failures or skipped tests. The same status icon appears in the gutter alongside the test implementation to help you locate the failure in the source editor. Click the diamond icon next to the debug message to expand it and review what the debug message reveals about the conditions that led to the failure.

![The source editor display the implementation for a test with a  red-filled rounded diamond-shaped icon that contains an ex in the gutter and an expanded debug message to the right. The debug message includes a Show button at the bottom-right.](https://docs-assets.developer.apple.com/published/bdc061abf215f6cb7552a8a02a2b2535/running-tests-and-interpreting-results-debug-message-expanded%402x.png)

Tests functions you write with Swift Testing capture the state of variables you use in expressions that you pass to expectation macros and input parameters the test runner passes to a test function. Inspect those values to further understand the cause of the failure, click the Show button at the bottom of the debug message and expand the Results and Arguments regions to view the state of expectation expressions and input parameters.

![The source editor display the implementation for a test with a  red-filled rounded diamond-shaped icon that contains an ex in the gutter and a debug message to the right. Results for the test function is expanded to show values for two structs used in the expect macro expression: video.metadata and expectedMetadata. The results show that the property value for duration inside the video.metadata struct is 0.0 seconds while the value inside expectedMetadata is 90.0 seconds. Other properties of the the two structs, such as resolution, are equivalent. ](https://docs-assets.developer.apple.com/published/04ae3564e5f6722f26d05102cc8d850a/running-tests-and-interpreting-results-debug-expanded-gap-results%402x.png)

![The source editor display the implementation for a test with a  red-filled rounded diamond-shaped icon that contains an ex in the gutter and a debug message to the right. Arguments for the parameterized function is expanded to show the current videoName argument is Scotland Coast. The debug messages associated with the failure for this argument indicates that the video in the video library with that name is nil. ](https://docs-assets.developer.apple.com/published/9f87ab79e25af670ec24c01b030f588b/running-tests-and-interpreting-results-debug-expanded-gap-arguments%402x.png)

#### Access Additional Information in the Test Report

Each test run produces a test report. Locate these reports in Xcode in the Report navigator by choosing View > Navigators > Reports, then select the Test action under your build scheme name.

The top level of a test report provides you with a high level summary of the test you’ve run. It highlights important patterns failure information, screenshots, and more to help you determine where to start your investigations.

Further information can be found under the additional sections of the report:

When you run tests with `xcodebuild` in Terminal, the command outputs an Xcode Test Results (`.xcresults`) bundle that contains session results, code coverage (if enabled), and other logs. You can open this file in Xcode to view or share it with other members of your development team.

#### Run a Single Test Function

Navigate to the Swift file that contains the test function you want to run in Xcode. Move the pointer over the diamond icon alongside the function declaration in the editor gutter, and click the gray play icon:

![A screenshot of the Xcode source editor. The icon for running a specific test function is visible in the source editor gutter.](https://docs-assets.developer.apple.com/published/3c522d61adec57b23c2e22c2201490c4/running-tests-and-interpreting-results-single-test-from-source%402x.png)

Alternatively, locate the test function in the Xcode Test navigator by moving the pointer over the test function name and click the play icon.

![A screenshot of the Xcode Test navigator. The icon for running a specific test function is visible.](https://docs-assets.developer.apple.com/published/895f805e861694317f09829a6e8e4641/running-tests-and-interpreting-results-single-test-from-navigator%402x.png)

Xcode runs the selected test function and updates the icon to indicate the outcome.

To run a single test function in Terminal, run `xcodebuild` by giving the test function’s identifier as the parameter to the `-only-testing` option. The identifier for a test function has the form `test_target/test_type/test_function`.

```zsh
% xcodebuild test -scheme SampleApp -only-testing SampleAppTests/SampleAppTests/testEmptyArrayWhenNoOverlappingNotes
```

#### Run a Parameterized Test Function with a Specific Input

Clicking the play icon next to the parameterized test function runs all test cases for that test. To select a specific test case to run, click the expansion arrow before the test function name in the Test navigator, move the pointer over the diamond icon alongside the specific test case, then click the gray play icon.

![A screenshot of the Xcode Test navigator. The icon for running a specific test case under a parameterized function is visible.](https://docs-assets.developer.apple.com/published/a1fc5f0551ec5219a56bb5bea7ff3d4f/running-tests-and-interpreting-results-parameterized-input%402x.png)

When you pass one or more collections to a `@Test` macro that supports parameterization, the macro generates a test case for each element or element pair. Each test case represents a unique set of input parameters that the test runner passes to the test function. If the test fails for one or more inputs, the corresponding diagnostics indicate which inputs to examine. Selecting the specific test case runs the test function with just the input for that case which is useful when debugging. For more information on implementing parameterized tests, see [`Implementing parameterized tests`](https://developer.apple.com/documentation/Testing/ParameterizedTesting).

#### Run a Group of the Test Functions

To run test functions defined under a common type or suite, move the pointer over the diamond icon alongside the type’s declaration in the editor gutter, and click the gray play icon. In Swift Testing, a  is any type that includes the definition for one or more test functions.

![A screenshot of Xcode display a test suite in the source editor. The icon for running the test functions in that type is visible.](https://docs-assets.developer.apple.com/published/0e33879583f08c6edaa55551aaa2185f/running-tests-and-interpreting-results-group-of-test-from-source%402x.png)

Alternatively, to run a group of test functions from the Xcode Test navigator, move the pointer over a plan, target, or suite listed in the navigator, then click the gray play icon:

![A screenshot of the Xcode Test navigator. The icon for running tests in a specific test case is visible.](https://docs-assets.developer.apple.com/published/eab75b8eb8e646fc9ca1b209194e7343/running-tests-and-interpreting-results-group-of-test-from-navigator%402x.png)

You can nest test suites and optionally annotate them with the `@Suite` macro to provide additional information about the test functions they contain. For more information, see [`Organizing test functions with suite types`](https://developer.apple.com/documentation/Testing/OrganizingTests).

In XCTest, you implement all of your test functions on a subclass of [`XCTestCase`](https://developer.apple.com/documentation/XCTest/XCTestCase). For more information, see [`Defining Test Cases and Test Methods`](https://developer.apple.com/documentation/XCTest/defining-test-cases-and-test-methods).

Xcode runs the test functions the selected item contains and updates the icon to indicate the outcome.

To run the test functions in a test case in Terminal, run `xcodebuild` by giving the suite’s identifier as the parameter to the `-only-testing` option. The identifier for a suite has the form `test_target/test_suite`.

```zsh
% xcodebuild test -scheme SampleApp -only-testing SampleAppTests/SampleAppTests
```

#### View and Run Tests By Tag

In Swift Testing, you can use the  [`tags(_:)`](https://developer.apple.com/documentation/Testing/Trait/tags(_:)) trait to annotate a group of related tests. These additional groups can be identified in the outline view under the Tags section of the Test navigator. Click the tag icon at the top of the Test navigator to view test functions organized by their tags. For more information about declaring tags and adding tags to tests, see [`Adding tags to tests`](https://developer.apple.com/documentation/Testing/AddingTags).

To run all of the test functions associated with a tag or a single test function under the tag group, move the pointer over the tag or test function, then click the gray play icon.

#### Run Testing Repeatedly to Determine Reliability

Control-click the diamond icon next to a test function or test suite type and select “Run  Repeatedly”. In the panel that appears, choose when to stop running the test. Options include:

Choose the maximum number of times to repeat the test, whether to pause execution if the test fails, and whether to restart the test runner for each repetition. Finally, click Run to repeatedly run the test.

![A screenshot of the Xcode panel for running the same test repeatedly.](https://docs-assets.developer.apple.com/published/ffc9bd90d0a1893e7afb7178caaff4b8/running-tests-and-interpreting-results-repeating-tests%402x.png)

To repeatedly run tests in Terminal, specify the number of repetitions with the `-test-repetitions` option, optionally specifying whether the tests should repeat until success or failure, and whether to restart the test runner for each repetition:

```zsh
% xcodebuild test -scheme SampleApp -only-testing SampleAppTests/SampleAppTests/testEmptyArrayWhenNoOverlappingNotes -run-tests-until-failure -test-iterations 20
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/running-tests-and-interpreting-results)*