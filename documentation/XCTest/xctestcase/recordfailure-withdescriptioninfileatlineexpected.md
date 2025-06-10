# recordFailure(withDescription:inFile:atLine:expected:)

**Framework**: XCTest  
**Kind**: method

Records a failure during text execution.

**Availability**:
- Unknown ?+ - Deprecated

## Declaration

```swift
func recordFailure(withDescription description: String, inFile filePath: String, atLine lineNumber: Int, expected: Bool)
```

#### Discussion

All test assertions use this method to record test failures.

## Parameters

- `description`: A description of the failure.
- `filePath`: The file path to the source file where the failure occurred.
- `lineNumber`: The line number in the source file at   where the failure occurred.
- `expected`:   if the failure was the result of a failed assertion,   if it was the result of an uncaught exception.

## See Also

- [init(invocation: NSInvocation?)](xctestcase/init(invocation:).md)
  Initializes a test case with an invocation.
- [init(selector: Selector)](xctestcase/init(selector:).md)
  Initializes a test case with a selector.
- [class var testInvocations: [NSInvocation]](xctestcase/testinvocations.md)
  An array of invocations that represents each test method in the test case.
- [var invocation: NSInvocation?](xctestcase/invocation.md)
  The invocation for running the test.
- [func invokeTest()](xctestcase/invoketest.md)
  Invokes the test.
- [func record(XCTIssue)](xctestcase/record(_:).md)
  Records an issue during test execution.
- [class var defaultTestSuite: XCTestSuite](xctestcase/defaulttestsuite.md)
  A test suite that contains test cases for all of the tests in the class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/recordfailure(withdescription:infile:atline:expected:))*