# XCTExpectFailure(_:enabled:strict:failingBlock:issueMatcher:)

**Framework**: Xctest  
**Kind**: func

Instructs the test to expect a failure in an assertion in the provided block of code, with parameters to customize expected failure checking and handling.

## Declaration

```swift
func XCTExpectFailure<R>(_ failureReason: String? = nil, enabled: Bool? = nil, strict: Bool? = nil, failingBlock: () throws -> R, issueMatcher: ((XCTIssue) -> Bool)? = nil) rethrows -> R
```

#### Return Value

If the `failingBlock` you provide returns a value or throws an error, the function returns that value or rethrows the error.

## Parameters

- `failureReason`: An optional string that describes why the test expects a failure.
- `enabled`: A Boolean value that indicates whether the test checks for the expected failure.
- `strict`: A Boolean value that indicates whether the test reports an error if the expected failure doesn’t occur.
- `failingBlock`: A block of test code and assertions where the test expects a failure.
- `issueMatcher`: A block of code that determines whether the test issue fulfills the expected failure.

## See Also

- [class XCTExpectedFailure](xctexpectedfailure.md)
  An object that represents an expected test failure.
- [XCTExpectedFailure.Options](xctexpectedfailure/options.md)
  Options that determine how the test matches the expected failure to an actual test failure, and whether an unfulfilled expected failure results in a test failure.
- [func XCTExpectFailure(String?, options: XCTExpectedFailure.Options)](xctexpectfailure(_:options:).md)
  Instructs the test to expect a failure in an upcoming assertion, with options to customize expected failure checking and handling.
- [func XCTExpectFailure(String?, enabled: Bool?, strict: Bool?, issueMatcher: ((XCTIssue) -> Bool)?)](xctexpectfailure(_:enabled:strict:issuematcher:).md)
  Instructs the test to expect a failure in an upcoming assertion, with parameters to customize expected failure checking and handling.
- [func XCTExpectFailure<R>(String?, options: XCTExpectedFailure.Options, failingBlock: () throws -> R) rethrows -> R](xctexpectfailure(_:options:failingblock:).md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with options to customize expected failure checking and handling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectfailure(_:enabled:strict:failingblock:issuematcher:))*