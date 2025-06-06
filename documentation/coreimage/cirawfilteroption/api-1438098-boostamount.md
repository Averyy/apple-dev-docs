# boostAmount

**Framework**: Core Image  
**Kind**: structdata

A key for the amount of boost to apply to an image. The associated value is a floating-point value packaged as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object. The value must be in the range of `0...1`. A value of `0` indicates no boost, that is, a linear response. The default value is `1`, which indicates full boost.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.5+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
static let boostAmount: CIRAWFilterOption
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438098-boostamount)*