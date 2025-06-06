# displayScale

**Framework**: UIKit  
**Kind**: property

The display scale of the trait collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var displayScale: CGFloat { get }
```

#### Discussion

A value of `1.0` indicates a non-Retina display and a value of `2.0` indicates a Retina display. The default display scale for a trait collection is `0.0` (indicating unspecified).

## See Also

- [var displayGamut: UIDisplayGamut](uitraitcollection/displaygamut.md)
  The gamut of the current display.
- [enum UIDisplayGamut](uidisplaygamut.md)
  Constants that indicate the gamut of the current display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/displayscale)*