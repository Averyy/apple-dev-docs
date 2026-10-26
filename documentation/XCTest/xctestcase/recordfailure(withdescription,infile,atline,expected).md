# recordFailure(withDescription:inFile:atLine:expected:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Records a failure during text execution.

> **Deprecated**: Use [`record(_:)`](./record%28_%29.md) instead.

## Declaration

```swift
func recordFailure(withDescription description: String, inFile filePath: String, atLine lineNumber: Int, expected: Bool)
```

```objc
- (void) recordFailureWithDescription:(NSString *) description inFile:(NSString *) filePath atLine:(NSUInteger) lineNumber expected:(BOOL) expected;
```

#### Discussion

All test assertions use this method to record test failures.

## Parameters

- `description`: A description of the failure.
- `filePath`: The file path to the source file where the failure occurred.
- `lineNumber`: The line number in the source file at `filePath` where the failure occurred.
- `expected`: [`true`](../../Swift/true.md) if the failure was the result of a failed assertion, [`false`](../../Swift/false.md) if it was the result of an uncaught exception.

## See Also

### Creating Tests Programmatically
- [init(invocation: NSInvocation?)](./init%28invocation%29.md)
  Initializes a test case with an invocation.
- [init(selector: Selector)](./init%28selector%29.md)
  Initializes a test case with a selector.
- [class var testInvocations: [NSInvocation]](./testinvocations.md)
  An array of invocations that represents each test method in the test case.
- [var invocation: NSInvocation?](./invocation.md)
  The invocation for running the test.
- [func invokeTest()](./invoketest%28%29.md)
  Invokes the test.
- [func record(XCTIssue)](./record%28_%29.md)
  Records an issue during test execution.
- [class var defaultTestSuite: XCTestSuite](./defaulttestsuite.md)
  A test suite that contains test cases for all of the tests in the class.
- [+ testCaseWithInvocation:](./testcasewithinvocation_.md)
  Creates a test case with an invocation.
- [+ testCaseWithSelector:](./testcasewithselector_.md)
  Creates a test case with a selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/recordfailure(withdescription:infile:atline:expected:))*