# default

**Framework**: XCTest  
**Kind**: property  
**Role**: Type Property

Creates a suite of test suites that represents all test case methods in the current runtime.

## Declaration

```swift
class var `default`: XCTestSuite { get }
```

```objc
@property (class, readonly) XCTestSuite * defaultTestSuite;
```

## See Also

### Creating Test Suites
- [init(name: String)](./init%28name%29.md)
  Creates a test suite with the specified name.
- [convenience init(forBundlePath: String)](./init%28forbundlepath%29.md)
  Creates a test suite with the bundle at the specified path.
- [convenience init(forTestCaseClass: AnyClass)](./init%28fortestcaseclass%29.md)
  Creates a test suite that contains all test methods in the specified class.
- [convenience init(forTestCaseWithName: String)](./init%28fortestcasewithname%29.md)
  Creates a test suite that contains a test case with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestsuite/default)*