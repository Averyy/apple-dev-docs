# XCTExpectFailure(_:options:)

**Framework**: XCTest  
**Kind**: func

Instructs the test to expect a failure in an upcoming assertion, with options to customize expected failure checking and handling.

## Declaration

```swift
func XCTExpectFailure(_ failureReason: String? = nil, options: XCTExpectedFailure.Options = .init())
```

## Parameters

- `failureReason`: An optional string that describes why the test expects a failure.
- `options`: Options that determine how the test matches the expected failure to an actual test failure, and whether an unfulfilled expected failure results in a test failure.

## See Also

- [class XCTExpectedFailure](xctexpectedfailure.md)
  An object that represents an expected test failure.
- [XCTExpectedFailure.Options](xctexpectedfailure/options.md)
  Options that determine how the test matches the expected failure to an actual test failure, and whether an unfulfilled expected failure results in a test failure.
- [func XCTExpectFailure(String?, enabled: Bool?, strict: Bool?, issueMatcher: ((XCTIssue) -> Bool)?)](xctexpectfailure(_:enabled:strict:issuematcher:).md)
  Instructs the test to expect a failure in an upcoming assertion, with parameters to customize expected failure checking and handling.
- [func XCTExpectFailure<R>(String?, options: XCTExpectedFailure.Options, failingBlock: () throws -> R) rethrows -> R](xctexpectfailure(_:options:failingblock:).md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with options to customize expected failure checking and handling.
- [func XCTExpectFailure<R>(String?, enabled: Bool?, strict: Bool?, failingBlock: () throws -> R, issueMatcher: ((XCTIssue) -> Bool)?) rethrows -> R](xctexpectfailure(_:enabled:strict:failingblock:issuematcher:).md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with parameters to customize expected failure checking and handling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectfailure(_:options:))*