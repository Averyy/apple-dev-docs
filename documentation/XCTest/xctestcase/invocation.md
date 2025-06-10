# invocation

**Framework**: XCTest  
**Kind**: property

The invocation for running the test.

## Declaration

```swift
var invocation: NSInvocation? { get set }
```

## See Also

- [init(invocation: NSInvocation?)](xctestcase/init(invocation:).md)
  Initializes a test case with an invocation.
- [init(selector: Selector)](xctestcase/init(selector:).md)
  Initializes a test case with a selector.
- [class var testInvocations: [NSInvocation]](xctestcase/testinvocations.md)
  An array of invocations that represents each test method in the test case.
- [func invokeTest()](xctestcase/invoketest.md)
  Invokes the test.
- [func record(XCTIssue)](xctestcase/record(_:).md)
  Records an issue during test execution.
- [func recordFailure(withDescription: String, inFile: String, atLine: Int, expected: Bool)](xctestcase/recordfailure(withdescription:infile:atline:expected:).md)
  Records a failure during text execution.
- [class var defaultTestSuite: XCTestSuite](xctestcase/defaulttestsuite.md)
  A test suite that contains test cases for all of the tests in the class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/invocation)*