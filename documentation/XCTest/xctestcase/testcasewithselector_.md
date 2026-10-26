# testCaseWithSelector:

**Framework**: XCTest  
**Kind**: method  
**Role**: Type Method

Creates a test case with a selector.

## Declaration

```objc
+ (instancetype) testCaseWithSelector:(SEL) selector;
```

#### Return Value

A test case with a selector.

## Parameters

- `selector`: A selector to use when running this test.

## See Also

### Creating Tests Programmatically
- [init(invocation: NSInvocation?)](./init%28invocation%29.md)
  Initializes a test case with an invocation.
- [+ testCaseWithInvocation:](./testcasewithinvocation_.md)
  Creates a test case with an invocation.
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
- [func recordFailure(withDescription: String, inFile: String, atLine: Int, expected: Bool)](./recordfailure%28withdescription,infile,atline,expected%29.md)
  Records a failure during text execution.
- [class var defaultTestSuite: XCTestSuite](./defaulttestsuite.md)
  A test suite that contains test cases for all of the tests in the class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/testcasewithselector:)*