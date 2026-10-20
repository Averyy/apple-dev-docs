# detectsDarkOnLight

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the request detects a dark object on a light background to aid in detection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
var detectsDarkOnLight: Bool
```

#### Discussion

The default value is `true`.

## See Also

### Configuring a request
- [var contrastAdjustment: Float](./contrastadjustment.md)
  The amount by which to adjust the image contrast.
- [var contrastPivot: Float?](./contrastpivot.md)
  The pixel value to use as a pivot for the contrast.
- [var maximumImageDimension: Int](./maximumimagedimension.md)
  The maximum image dimension to use for contour detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectcontoursrequest/detectsdarkonlight)*