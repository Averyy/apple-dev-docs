# contrastAdjustment

**Framework**: Vision  
**Kind**: property

The amount by which to adjust the image contrast.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var contrastAdjustment: Float
```

#### Discussion

Contour detection works best with high-contrast images. The default value of this property is `2.0`, which doubles the image contrast to achieve the most accurate results.

This property supports a value range from `0.0` to `3.0`.

## See Also

- [var contrastPivot: Float?](detectcontoursrequest/contrastpivot.md)
  The pixel value to use as a pivot for the contrast.
- [var detectsDarkOnLight: Bool](detectcontoursrequest/detectsdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background to aid in detection.
- [var maximumImageDimension: Int](detectcontoursrequest/maximumimagedimension.md)
  The maximum image dimension to use for contour detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectcontoursrequest/contrastadjustment)*