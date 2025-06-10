# init(selector:)

**Framework**: XCTest  
**Kind**: init

Initializes a test case with a selector.

## Declaration

```swift
init(selector: Selector)
```

## Parameters

- `selector`: A selector to use when running this test.

## See Also

- [init(invocation: NSInvocation?)](xctestcase/init(invocation:).md)
  Initializes a test case with an invocation.
- [class var testInvocations: [NSInvocation]](xctestcase/testinvocations.md)
  An array of invocations that represents each test method in the test case.
- [var invocation: NSInvocation?](xctestcase/invocation.md)
  The invocation for running the test.
- [func invokeTest()](xctestcase/invoketest.md)
  Invokes the test.
- [func record(XCTIssue)](xctestcase/record(_:).md)
  Records an issue during test execution.
- [func recordFailure(withDescription: String, inFile: String, atLine: Int, expected: Bool)](xctestcase/recordfailure(withdescription:infile:atline:expected:).md)
  Records a failure during text execution.
- [class var defaultTestSuite: XCTestSuite](xctestcase/defaulttestsuite.md)
  A test suite that contains test cases for all of the tests in the class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/init(selector:))*