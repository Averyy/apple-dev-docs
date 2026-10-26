# testSuiteWithName:

**Framework**: XCTest  
**Kind**: method  
**Role**: Type Method

Creates a test suite with the specified name.

## Declaration

```objc
+ (instancetype) testSuiteWithName:(NSString *) name;
```

## Parameters

- `name`: The name of the test.

## See Also

### Creating Test Suites
- [class var `default`: XCTestSuite](./default.md)
  Creates a suite of test suites that represents all test case methods in the current runtime.
- [init(name: String)](./init%28name%29.md)
  Creates a test suite with the specified name.
- [convenience init(forBundlePath: String)](./init%28forbundlepath%29.md)
  Creates a test suite with the bundle at the specified path.
- [convenience init(forTestCaseClass: AnyClass)](./init%28fortestcaseclass%29.md)
  Creates a test suite that contains all test methods in the specified class.
- [convenience init(forTestCaseWithName: String)](./init%28fortestcasewithname%29.md)
  Creates a test suite that contains a test case with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestsuite/testsuitewithname:)*