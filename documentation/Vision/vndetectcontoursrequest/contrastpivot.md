# contrastPivot

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The pixel value to use as a pivot for the contrast.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var contrastPivot: NSNumber? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) NSNumber * contrastPivot;
```

## Discussion

Numeric values range from `0.0` to `1.0`. You can also specify `nil` to have the framework automatically detect the value according to image intensity.

The default value is `0.5`, which indicates the pixel center.

## See Also

### Configuring the Request
- [var contrastAdjustment: Float](./contrastadjustment.md)
  The amount by which to adjust the image contrast.
- [var detectsDarkOnLight: Bool](./detectsdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background to aid in detection.
- [var maximumImageDimension: Int](./maximumimagedimension.md)
  The maximum image dimension to use for contour detection.
- [var detectDarkOnLight: Bool](./detectdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectcontoursrequest/contrastpivot)*