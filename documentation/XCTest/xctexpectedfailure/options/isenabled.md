# isEnabled

**Framework**: XCTest  
**Kind**: property

A Boolean value that indicates whether the test checks for the expected failure.

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

The default is `true`. Set this property to `false` to disable the expected failure check.

## See Also

- [class func nonStrict() -> XCTExpectedFailure.Options](xctexpectedfailure/options/nonstrict.md)
  Options that specify that an unfulfilled expected failure doesn’t generate a test failure.
- [var isStrict: Bool](xctexpectedfailure/options/isstrict.md)
  A Boolean value that indicates whether the test reports an error if the expected failure doesn’t occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectedfailure/options/isenabled)*