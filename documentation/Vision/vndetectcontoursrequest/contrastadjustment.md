# contrastAdjustment

**Framework**: Vision  
**Kind**: property

The amount by which to adjust the image contrast.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var contrastAdjustment: Float { get set }
```

#### Discussion

Contour detection works best with high-contrast images. The default value of this property is `2.0`, which doubles the image contrast to achieve the most accurate results.

This property supports a value range from `0.0` to `3.0`.

## See Also

- [var contrastPivot: NSNumber?](vndetectcontoursrequest/contrastpivot.md)
  The pixel value to use as a pivot for the contrast.
- [var detectsDarkOnLight: Bool](vndetectcontoursrequest/detectsdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background to aid in detection.
- [var maximumImageDimension: Int](vndetectcontoursrequest/maximumimagedimension.md)
  The maximum image dimension to use for contour detection.
- [var detectDarkOnLight: Bool](vndetectcontoursrequest/detectdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectcontoursrequest/contrastadjustment)*