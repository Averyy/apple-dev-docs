# testCaseCount

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The number of test cases in the test.

## Declaration

```swift
var testCaseCount: Int { get }
```

```objc
@property (readonly) NSUInteger testCaseCount;
```

## Discussion

Must be overridden by subclasses.

## See Also

### Examining Test Properties
- [var name: String](./name.md)
  The name of the test.
- [var testRun: XCTestRun?](./testrun.md)
  The test run object that executes the test.
- [var testRunClass: AnyClass?](./testrunclass.md)
  The test run subclass to instantiate when the test runs, which records the test’s results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/testcasecount)*