# XCTExpectedFailure.Options

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

Options that determine how the test matches the expected failure to an actual test failure, and whether an unfulfilled expected failure results in a test failure.

## Declaration

```swift
class Options
```

```objc
@interface XCTExpectedFailureOptions : NSObject
```

## Overview

Create options and provide them to `XCTExpectFailure` functions to tell the test system how to match an expected failure, whether to enable an expected failure during a test, and whether an unfulfilled expected failure generates a test failure.

## Topics

### Matching Failures
- [var issueMatcher: (XCTIssue) -> Bool](./options/issuematcher.md)
  A block of code that determines whether the test issue fulfills the expected failure.
### Specifying Options
- [class func nonStrict() -> XCTExpectedFailure.Options](./options/nonstrict%28%29.md)
  Options that specify that an unfulfilled expected failure doesn’t generate a test failure.
- [var isEnabled: Bool](./options/isenabled.md)
  A Boolean value that indicates whether the test checks for the expected failure.
- [var isStrict: Bool](./options/isstrict.md)
  A Boolean value that indicates whether the test reports an error if the expected failure doesn’t occur.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Expected Failures
- [class XCTExpectedFailure](../xctexpectedfailure.md)
  An object that represents an expected test failure.
- [func XCTExpectFailure(String?, options: XCTExpectedFailure.Options)](../xctexpectfailure%28_,options%29.md)
  Instructs the test to expect a failure in an upcoming assertion, with options to customize expected failure checking and handling.
- [func XCTExpectFailure(String?, enabled: Bool?, strict: Bool?, issueMatcher: ((XCTIssue) -> Bool)?)](../xctexpectfailure%28_,enabled,strict,issuematcher%29.md)
  Instructs the test to expect a failure in an upcoming assertion, with parameters to customize expected failure checking and handling.
- [func XCTExpectFailure<R>(String?, options: XCTExpectedFailure.Options, failingBlock: () throws -> R) rethrows -> R](../xctexpectfailure%28_,options,failingblock%29.md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with options to customize expected failure checking and handling.
- [func XCTExpectFailure<R>(String?, enabled: Bool?, strict: Bool?, failingBlock: () throws -> R, issueMatcher: ((XCTIssue) -> Bool)?) rethrows -> R](../xctexpectfailure%28_,enabled,strict,failingblock,issuematcher%29.md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with parameters to customize expected failure checking and handling.
- [XCTExpectFailure](../xctexpectfailure.md)
  Instructs the test to expect a failure in an upcoming assertion.
- [XCTExpectFailureInBlock](../xctexpectfailureinblock.md)
  Instructs the test to expect a failure in an assertion in the provided block of code.
- [XCTExpectFailureWithOptions](../xctexpectfailurewithoptions.md)
  Instructs the test to expect a failure in an upcoming assertion, with options to customize expected failure checking and handling.
- [XCTExpectFailureWithOptionsInBlock](../xctexpectfailurewithoptionsinblock.md)
  Instructs the test to expect a failure in an assertion in the provided block of code, with options to customize expected failure checking and handling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectedfailure/options)*