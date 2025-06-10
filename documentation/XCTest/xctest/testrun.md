# testRun

**Framework**: XCTest  
**Kind**: property

The test run object that executes the test.

## Declaration

```swift
var testRun: XCTestRun? { get }
```

#### Discussion

An instance of [`testRunClass`](xctest/testrunclass.md), or `nil` if the test hasn’t run.

## See Also

- [var name: String](xctest/name.md)
  The name of the test.
- [var testCaseCount: Int](xctest/testcasecount.md)
  The number of test cases in the test.
- [var testRunClass: AnyClass?](xctest/testrunclass.md)
  The test run subclass to instantiate when the test runs, which records the test’s results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/testrun)*