# runsForEachTargetApplicationUIConfiguration

**Framework**: XCTest  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether your UI tests run once for each possible combination of orientation, localization, and other appearance settings your app supports.

## Declaration

```swift
class var runsForEachTargetApplicationUIConfiguration: Bool { get }
```

```objc
@property (class, readonly) BOOL runsForEachTargetApplicationUIConfiguration;
```

#### Discussion

The default is `false`. Override this method to return `true` in your UI test case to run the tests once for each UI configuration your app supports. To determine what UI configurations your app supports, the test system examines your project settings, including:

- Appearance (for example, light mode or dark mode)
- Orientation (for example, portrait or landscape)
- Localization (for example, `en_US` or `zh_CN`)

The test system calculates a set of configurations that encompasses all the possible combinations of those supported settings, and provides each configuration to an iteration of your tests when you call [`launch()`](../../XCUIAutomation/xcuiapplication/launch%28%29.md) on [`XCUIApplication`](../../XCUIAutomation/xcuiapplication.md).

## See Also

### Managing Test Case Execution
- [var continueAfterFailure: Bool](./continueafterfailure.md)
  A Boolean value that indicates whether a test method should continue running after a failure occurs.
- [var executionTimeAllowance: TimeInterval](./executiontimeallowance.md)
  The number of seconds, rounded up to the nearest minute, for a test to run before it fails with a timeout error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/runsforeachtargetapplicationuiconfiguration)*