# maximumImageDimension

**Framework**: Vision  
**Kind**: property

The maximum image dimension to use for contour detection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var maximumImageDimension: Int
```

#### Discussion

Contour detection is computationally intensive. To improve performance, the framework scales the input image down, while maintaining its aspect ratio, such that its maximum dimension is the value of this property. The framework never scales the image up, so specifying the maximum value ensures that the image processes in its original size and not as a downscaled version.

This minimum value supported is `64`. The default value is `512`.

## See Also

- [var contrastAdjustment: Float](detectcontoursrequest/contrastadjustment.md)
  The amount by which to adjust the image contrast.
- [var contrastPivot: Float?](detectcontoursrequest/contrastpivot.md)
  The pixel value to use as a pivot for the contrast.
- [var detectsDarkOnLight: Bool](detectcontoursrequest/detectsdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background to aid in detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectcontoursrequest/maximumimagedimension)*