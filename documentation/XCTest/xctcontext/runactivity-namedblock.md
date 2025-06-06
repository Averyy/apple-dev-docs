# runActivity(named:block:)

**Framework**: Xctest  
**Kind**: method

Creates and runs an activity with the provided block of code.

## Declaration

```swift
@MainActor
@preconcurrency class func runActivity<Result>(named name: String, block: @MainActor (any XCTActivity) throws -> Result) rethrows -> Result
```

#### Return Value

A [`Result`](https://developer.apple.com/documentation/Swift/Result) object that indicates whether the block of code runs successfully or encounters an error.

#### Discussion

Run a block of code as a named substep in a test. For more information, see [`Grouping Tests into Substeps with Activities`](grouping-tests-into-substeps-with-activities.md).

To save screenshots or other test-result data for later investigation, call the [`add(_:)`](xctactivity/add(_:).md) method on the instance of [`XCTActivity`](xctactivity.md) that the test system passes to your block. For more information, see [`Adding Attachments to Tests, Activities, and Issues`](adding-attachments-to-tests-activities-and-issues.md).

## Parameters

- `name`: A descriptive name for the activity, for display in Xcode’s test results browser.
- `block`: A block of code for the test to execute as the body of the activity.

## See Also

- [Grouping Tests into Substeps with Activities](grouping-tests-into-substeps-with-activities.md)
  Simplify test reports by creating activities that organize substeps within complex test methods.
- [Adding Attachments to Tests, Activities, and Issues](adding-attachments-to-tests-activities-and-issues.md)
  Use attachments to store a test’s output data for later analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctcontext/runactivity(named:block:))*