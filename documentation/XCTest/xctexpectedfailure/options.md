# XCTExpectedFailure.Options

**Framework**: Xctest  
**Kind**: class

Options that determine how the test matches the expected failure to an actual test failure, and whether an unfulfilled expected failure results in a test failure.

## Declaration

```swift
class Options
```

#### Overview

Create options and provide them to `XCTExpectFailure` functions to tell the test system how to match an expected failure, whether to enable an expected failure during a test, and whether an unfulfilled expected failure generates a test failure.

## Topics

### Matching Failures
- [var issueMatcher: (XCTIssue) -> Bool](xctexpectedfailure/options/issuematcher.md)
  A block of code that determines whether the test issue fulfills the expected failure.
### Specifying Options
- [class func nonStrict() -> XCTExpectedFailure.Options](xctexpectedfailure/options/nonstrict.md)
  Options that specify that an unfulfilled expected failure doesn’t generate a test failure.
- [var isEnabled: Bool](xctexpectedfailure/options/isenabled.md)
  A Boolean value that indicates whether the test checks for the expected failure.
- [var isStrict: Bool](xctexpectedfailure/options/isstrict.md)
  A Boolean value that indicates whether the test reports an error if the expected failure doesn’t occur.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class XCTExpectedFailure](xctexpectedfailure.md)
  An object that represents an expected test failure.
- [func XCTExpectFailure(String?, options: XCTExpectedFailure.Options)](xctexpectfailure(_:options:).md)
  Instructs the test to expect a failure in an upcoming assertion, with options to customize expected failure checking and handling.
- [func XCTExpectFailure(String?, enabled: Bool?, strict: Bool?, issueMatcher: ((XCTIssue) -> Bool)?)](xctexpectfailure(_:enabled:strict:issuematcher:).md)
  Instructs the test to expect a failure in an upcoming assertion, with parameters to customize expected failure checking and handling.
- [func XCTExpectFailure<R>(String?, options: XCTExpectedFailure.Options, failingBlock: () throws -> R) rethrows -> R](xctexpectfailure(_:options:failingblock:).md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with options to customize expected failure checking and handling.
- [func XCTExpectFailure<R>(String?, enabled: Bool?, strict: Bool?, failingBlock: () throws -> R, issueMatcher: ((XCTIssue) -> Bool)?) rethrows -> R](xctexpectfailure(_:enabled:strict:failingblock:issuematcher:).md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with parameters to customize expected failure checking and handling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectedfailure/options)*