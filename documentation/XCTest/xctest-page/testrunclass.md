# testRunClass

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The test run subclass to instantiate when the test runs, which records the test’s results.

## Declaration

```swift
var testRunClass: AnyClass? { get }
```

```objc
@property (readonly, nullable) Class testRunClass;
```

## Discussion

Subclasses must override `testRunClass`.

## See Also

### Examining Test Properties
- [var name: String](./name.md)
  The name of the test.
- [var testCaseCount: Int](./testcasecount.md)
  The number of test cases in the test.
- [var testRun: XCTestRun?](./testrun.md)
  The test run object that executes the test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/testrunclass)*