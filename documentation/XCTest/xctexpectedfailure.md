# XCTExpectedFailure

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An object that represents an expected test failure.

## Declaration

```swift
class XCTExpectedFailure
```

```objc
@interface XCTExpectedFailure : NSObject
```

#### Overview

The test system creates and tracks instances of `XCTExpectedFailure` when you call one of the `XCTExpectFailure` functions. Don’t create or use them directly.

## Topics

### Detailing Expected Failure
- [var failureReason: String?](./xctexpectedfailure/failurereason.md)
  An optional string that describes why the test expects a failure.
- [var issue: XCTIssue](./xctexpectedfailure/issue.md)
  The issue that fulfills the expected failure.
### Setting Options
- [XCTExpectedFailure.Options](./xctexpectedfailure/options.md)
  Options that determine how the test matches the expected failure to an actual test failure, and whether an unfulfilled expected failure results in a test failure.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Expected Failures
- [XCTExpectedFailure.Options](./xctexpectedfailure/options.md)
  Options that determine how the test matches the expected failure to an actual test failure, and whether an unfulfilled expected failure results in a test failure.
- [func XCTExpectFailure(String?, options: XCTExpectedFailure.Options)](./xctexpectfailure%28_,options%29.md)
  Instructs the test to expect a failure in an upcoming assertion, with options to customize expected failure checking and handling.
- [func XCTExpectFailure(String?, enabled: Bool?, strict: Bool?, issueMatcher: ((XCTIssue) -> Bool)?)](./xctexpectfailure%28_,enabled,strict,issuematcher%29.md)
  Instructs the test to expect a failure in an upcoming assertion, with parameters to customize expected failure checking and handling.
- [func XCTExpectFailure<R>(String?, options: XCTExpectedFailure.Options, failingBlock: () throws -> R) rethrows -> R](./xctexpectfailure%28_,options,failingblock%29.md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with options to customize expected failure checking and handling.
- [func XCTExpectFailure<R>(String?, enabled: Bool?, strict: Bool?, failingBlock: () throws -> R, issueMatcher: ((XCTIssue) -> Bool)?) rethrows -> R](./xctexpectfailure%28_,enabled,strict,failingblock,issuematcher%29.md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with parameters to customize expected failure checking and handling.
- [XCTExpectFailure](./xctexpectfailure.md)
  Instructs the test to expect a failure in an upcoming assertion.
- [XCTExpectFailureInBlock](./xctexpectfailureinblock.md)
  Instructs the test to expect a failure in an assertion in the provided block of code.
- [XCTExpectFailureWithOptions](./xctexpectfailurewithoptions.md)
  Instructs the test to expect a failure in an upcoming assertion, with options to customize expected failure checking and handling.
- [XCTExpectFailureWithOptionsInBlock](./xctexpectfailurewithoptionsinblock.md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with options to customize expected failure checking and handling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectedfailure)*