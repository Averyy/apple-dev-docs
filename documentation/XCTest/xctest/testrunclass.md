# testRunClass

**Framework**: XCTest  
**Kind**: property

The test run subclass to instantiate when the test runs, which records the test’s results.

## Declaration

```swift
var testRunClass: AnyClass? { get }
```

#### Discussion

Subclasses must override `testRunClass`.

## See Also

- [var name: String](xctest/name.md)
  The name of the test.
- [var testCaseCount: Int](xctest/testcasecount.md)
  The number of test cases in the test.
- [var testRun: XCTestRun?](xctest/testrun.md)
  The test run object that executes the test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/testrunclass)*