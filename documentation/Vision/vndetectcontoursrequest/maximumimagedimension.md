# maximumImageDimension

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The maximum image dimension to use for contour detection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var maximumImageDimension: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger maximumImageDimension;
```

## Discussion

Contour detection is computationally intensive. To improve performance, Vision scales the input image down, while maintaining its aspect ratio, such that its maximum dimension is the value of this property. Vision never scales the image up, so specifying the maximum value ensures that the image processes in its original size and not as a downscaled version.

This property supports values from 64 to [`NSUIntegerMax`](../../ObjectiveC/nsuintegermax.md). The default value is 512.

## See Also

### Configuring the Request
- [var contrastAdjustment: Float](./contrastadjustment.md)
  The amount by which to adjust the image contrast.
- [var contrastPivot: NSNumber?](./contrastpivot.md)
  The pixel value to use as a pivot for the contrast.
- [var detectsDarkOnLight: Bool](./detectsdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background to aid in detection.
- [var detectDarkOnLight: Bool](./detectdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectcontoursrequest/maximumimagedimension)*