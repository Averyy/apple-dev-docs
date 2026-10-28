# invokeTest()

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Invokes the test.

## Declaration

```swift
func invokeTest()
```

```objc
- (void) invokeTest;
```

## Discussion

Invoking a test performs its setup, invocation, and teardown. In general this should not be called directly.

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
- [func record(XCTIssue)](./record%28_%29.md)
  Records an issue during test execution.
- [func recordFailure(withDescription: String, inFile: String, atLine: Int, expected: Bool)](./recordfailure%28withdescription,infile,atline,expected%29.md)
  Records a failure during text execution.
- [class var defaultTestSuite: XCTestSuite](./defaulttestsuite.md)
  A test suite that contains test cases for all of the tests in the class.
- [+ testCaseWithInvocation:](./testcasewithinvocation_.md)
  Creates a test case with an invocation.
- [+ testCaseWithSelector:](./testcasewithselector_.md)
  Creates a test case with a selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/invoketest())*