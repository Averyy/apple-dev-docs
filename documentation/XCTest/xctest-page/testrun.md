# testRun

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The test run object that executes the test.

## Declaration

```swift
var testRun: XCTestRun? { get }
```

```objc
@property (readonly, nullable) XCTestRun * testRun;
```

## Discussion

An instance of [`testRunClass`](./testrunclass.md), or `nil` if the test hasn’t run.

## See Also

### Examining Test Properties
- [var name: String](./name.md)
  The name of the test.
- [var testCaseCount: Int](./testcasecount.md)
  The number of test cases in the test.
- [var testRunClass: AnyClass?](./testrunclass.md)
  The test run subclass to instantiate when the test runs, which records the test’s results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/testrun)*