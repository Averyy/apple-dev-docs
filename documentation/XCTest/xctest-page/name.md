# name

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The name of the test.

## Declaration

```swift
var name: String { get }
```

```objc
@property (copy, readonly) NSString * name;
```

## Discussion

Must be overridden by subclasses.

## See Also

### Examining Test Properties
- [var testCaseCount: Int](./testcasecount.md)
  The number of test cases in the test.
- [var testRun: XCTestRun?](./testrun.md)
  The test run object that executes the test.
- [var testRunClass: AnyClass?](./testrunclass.md)
  The test run subclass to instantiate when the test runs, which records the test’s results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/name)*