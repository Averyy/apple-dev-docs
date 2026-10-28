# isStrict

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the test reports an error if the expected failure doesn’t occur.

## Declaration

```swift
var isStrict: Bool { get set }
```

```objc
@property (getter=isStrict) BOOL strict;
```

## Discussion

The default is `true`. Set this property to `false` to prevent the test from recording the unfilled expected failure as an issue.

## See Also

### Specifying Options
- [class func nonStrict() -> XCTExpectedFailure.Options](./nonstrict%28%29.md)
  Options that specify that an unfulfilled expected failure doesn’t generate a test failure.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the test checks for the expected failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectedfailure/options/isstrict)*