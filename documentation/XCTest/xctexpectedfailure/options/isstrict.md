# isStrict

**Framework**: XCTest  
**Kind**: property

A Boolean value that indicates whether the test reports an error if the expected failure doesn’t occur.

## Declaration

```swift
var isStrict: Bool { get set }
```

#### Discussion

The default is `true`. Set this property to `false` to prevent the test from recording the unfilled expected failure as an issue.

## See Also

- [class func nonStrict() -> XCTExpectedFailure.Options](xctexpectedfailure/options/nonstrict.md)
  Options that specify that an unfulfilled expected failure doesn’t generate a test failure.
- [var isEnabled: Bool](xctexpectedfailure/options/isenabled.md)
  A Boolean value that indicates whether the test checks for the expected failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectedfailure/options/isstrict)*