# XCTExpectedFailure

**Framework**: XCTest  
**Kind**: class

An object that represents an expected test failure.

## Declaration

```swift
class XCTExpectedFailure
```

#### Overview

The test system creates and tracks instances of `XCTExpectedFailure` when you call one of the `XCTExpectFailure` functions. Don’t create or use them directly.

## Topics

### Detailing Expected Failure
- [var failureReason: String?](xctexpectedfailure/failurereason.md)
  An optional string that describes why the test expects a failure.
- [var issue: XCTIssue](xctexpectedfailure/issue.md)
  The issue that fulfills the expected failure.
### Setting Options
- [XCTExpectedFailure.Options](xctexpectedfailure/options.md)
  Options that determine how the test matches the expected failure to an actual test failure, and whether an unfulfilled expected failure results in a test failure.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [XCTExpectedFailure.Options](xctexpectedfailure/options.md)
  Options that determine how the test matches the expected failure to an actual test failure, and whether an unfulfilled expected failure results in a test failure.
- [func XCTExpectFailure(String?, options: XCTExpectedFailure.Options)](xctexpectfailure(_:options:).md)
  Instructs the test to expect a failure in an upcoming assertion, with options to customize expected failure checking and handling.
- [func XCTExpectFailure(String?, enabled: Bool?, strict: Bool?, issueMatcher: ((XCTIssue) -> Bool)?)](xctexpectfailure(_:enabled:strict:issuematcher:).md)
  Instructs the test to expect a failure in an upcoming assertion, with parameters to customize expected failure checking and handling.
- [func XCTExpectFailure<R>(String?, options: XCTExpectedFailure.Options, failingBlock: () throws -> R) rethrows -> R](xctexpectfailure(_:options:failingblock:).md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with options to customize expected failure checking and handling.
- [func XCTExpectFailure<R>(String?, enabled: Bool?, strict: Bool?, failingBlock: () throws -> R, issueMatcher: ((XCTIssue) -> Bool)?) rethrows -> R](xctexpectfailure(_:enabled:strict:failingblock:issuematcher:).md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with parameters to customize expected failure checking and handling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectedfailure)*