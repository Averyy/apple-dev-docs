# XCTExpectFailureWithOptions

**Framework**: XCTest  
**Kind**: func  
**Role**: Function

Instructs the test to expect a failure in an upcoming assertion, with options to customize expected failure checking and handling.

## Declaration

```c
extern void XCTExpectFailureWithOptions(NSString *failureReason, XCTExpectedFailureOptions *options);
```

## See Also

### Expected Failures
- [class XCTExpectedFailure](./xctexpectedfailure.md)
  An object that represents an expected test failure.
- [XCTExpectedFailure.Options](./xctexpectedfailure/options.md)
  Options that determine how the test matches the expected failure to an actual test failure, and whether an unfulfilled expected failure results in a test failure.
- [XCTExpectFailure](./xctexpectfailure.md)
  Instructs the test to expect a failure in an upcoming assertion.
- [XCTExpectFailureInBlock](./xctexpectfailureinblock.md)
  Instructs the test to expect a failure in an assertion in the provided block of code.
- [XCTExpectFailureWithOptionsInBlock](./xctexpectfailurewithoptionsinblock.md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with options to customize expected failure checking and handling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectfailurewithoptions)*