# init(forBundlePath:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates a test suite with the bundle at the specified path.

## Declaration

```swift
convenience init(forBundlePath bundlePath: String)
```

```objc
+ (instancetype) testSuiteForBundlePath:(NSString *) bundlePath;
```

## Parameters

- `bundlePath`: A string that represents a file path to a bundle.

## See Also

### Creating Test Suites
- [class var `default`: XCTestSuite](./default.md)
  Creates a suite of test suites that represents all test case methods in the current runtime.
- [init(name: String)](./init%28name%29.md)
  Creates a test suite with the specified name.
- [convenience init(forTestCaseClass: AnyClass)](./init%28fortestcaseclass%29.md)
  Creates a test suite that contains all test methods in the specified class.
- [convenience init(forTestCaseWithName: String)](./init%28fortestcasewithname%29.md)
  Creates a test suite that contains a test case with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestsuite/init(forbundlepath:))*