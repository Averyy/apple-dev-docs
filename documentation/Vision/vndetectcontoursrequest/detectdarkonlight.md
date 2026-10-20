# detectDarkOnLight

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the request detects a dark object on a light background.

**Availability**:
- iOS 14.0+ - Deprecated in 14.0
- iPadOS 14.0+ - Deprecated in 14.0
- Mac Catalyst 14.0+ - Deprecated in 14.0
- macOS 11.0+ - Deprecated in 11.0
- tvOS 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`detectsDarkOnLight`](./detectsdarkonlight.md) instead.

## Declaration

```swift
var detectDarkOnLight: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL detectDarkOnLight;
```

#### Discussion

The default value is [`true`](../../Swift/true.md).

## See Also

### Configuring the Request
- [var contrastAdjustment: Float](./contrastadjustment.md)
  The amount by which to adjust the image contrast.
- [var contrastPivot: NSNumber?](./contrastpivot.md)
  The pixel value to use as a pivot for the contrast.
- [var detectsDarkOnLight: Bool](./detectsdarkonlight.md)
  A Boolean value that indicates whether the request detects a dark object on a light background to aid in detection.
- [var maximumImageDimension: Int](./maximumimagedimension.md)
  The maximum image dimension to use for contour detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectcontoursrequest/detectdarkonlight)*