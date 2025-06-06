# CIDetectorAspectRatio

**Framework**: Core Image  
**Kind**: data

An option specifying the aspect ratio (width divided by height) of rectangles to search for.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorAspectRatio: String
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object whose value is a positive floating-point number. Use this option with the [`CIDetectorTypeRectangle`](cidetectortyperectangle.md) detector type to fine-tune the accuracy of the detector. For example, to more accurately find a business card (3.5 x 2 inches) in an image, specify an aspect ratio of `1.75` (3.5 / 2).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectoraspectratio)*