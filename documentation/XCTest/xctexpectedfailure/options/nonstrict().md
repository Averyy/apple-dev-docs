# nonStrict()

**Framework**: XCTest  
**Kind**: method  
**Role**: Type Method

Options that specify that an unfulfilled expected failure doesn’t generate a test failure.

## Declaration

```swift
class func nonStrict() -> XCTExpectedFailure.Options
```

```objc
+ (XCTExpectedFailureOptions *) nonStrictOptions;
```

#### Return Value

Returns an options instance that specifies that an unfulfilled expected failure doesn’t generate a test failure.

## See Also

### Specifying Options
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the test checks for the expected failure.
- [var isStrict: Bool](./isstrict.md)
  A Boolean value that indicates whether the test reports an error if the expected failure doesn’t occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctexpectedfailure/options/nonstrict())*