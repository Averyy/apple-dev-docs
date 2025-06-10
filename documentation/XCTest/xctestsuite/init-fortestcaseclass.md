# init(forTestCaseClass:)

**Framework**: XCTest  
**Kind**: init

Creates a test suite that contains all test methods in the specified class.

## Declaration

```swift
convenience init(forTestCaseClass testCaseClass: AnyClass)
```

## Parameters

- `testCaseClass`: A class that contains test cases.

## See Also

- [class var `default`: XCTestSuite](xctestsuite/default.md)
  Creates a suite of test suites that represents all test case methods in the current runtime.
- [init(name: String)](xctestsuite/init(name:).md)
  Creates a test suite with the specified name.
- [convenience init(forBundlePath: String)](xctestsuite/init(forbundlepath:).md)
  Creates a test suite with the bundle at the specified path.
- [convenience init(forTestCaseWithName: String)](xctestsuite/init(fortestcasewithname:).md)
  Creates a test suite that contains a test case with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestsuite/init(fortestcaseclass:))*