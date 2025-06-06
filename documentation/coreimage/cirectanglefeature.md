# CIRectangleFeature

**Framework**: Coreimage  
**Kind**: cl

Information about a rectangular region detected in a still or video image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIRectangleFeature : CIFeature
```

#### Overview

> **Note**: In macOS 10.13, iOS 11, and tvOS 11 or later, the [`Vision`](https://developer.apple.com/documentation/vision) framework replaces these classes for identifying and analyzing image features. See [`VNDetectRectanglesRequest`](https://developer.apple.com/documentation/vision/vndetectrectanglesrequest).

A detected rectangle feature isn’t necessarily rectangular in the plane of the image; rather, the feature identifies a shape that may be rectangular in space but which appears in perspective in the image — for example, a paper or book on a desk. The properties of a [`CIRectangleFeature`](cirectanglefeature.md) object identify its corners in image coordinates.

For example, you can use rectangle feature detection together with the [`CIPerspectiveCorrection`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/filter/ci/CIPerspectiveCorrection) filter to detect rectangular objects in an image or video and transform them to their original orientation.

To detect rectangles in an image or video, choose the [`CIDetectorTypeRectangle`](cidetectortyperectangle.md) type when initializing a [`CIDetector`](cidetector.md) object, and use the [`CIDetectorAspectRatio`](cidetectoraspectratio.md) and [`CIDetectorFocalLength`](cidetectorfocallength.md) options to specify the approximate shape of rectangular features to search for. The detector returns at most one rectangle feature, the most prominent found in the image.

## Topics

### Locating a Detected Feature
- [var bounds: CGRect](cirectanglefeature/1438024-bounds.md)
  A rectangle indicating the position and extent of the feature in image coordinates.
### Identifying the Corners of a Detected Rectangle
- [var bottomLeft: CGPoint](cirectanglefeature/1437878-bottomleft.md)
  The lower-left corner of the detected rectangle, in image coordinates.
- [var bottomRight: CGPoint](cirectanglefeature/1437888-bottomright.md)
  The lower-right corner of the detected rectangle, in image coordinates.
- [var topLeft: CGPoint](cirectanglefeature/1437951-topleft.md)
  The upper-left corner of the detected rectangle, in image coordinates.
- [var topRight: CGPoint](cirectanglefeature/1438071-topright.md)
  The upper-right corner of the detected rectangle, in image coordinates.

## Relationships

### Inherits From
- [CIFeature](cifeature.md)

## See Also

- [class CIDetector](cidetector.md)
  An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [class CIFeature](cifeature.md)
  The abstract superclass for objects representing notable features detected in an image.
- [class CIFaceFeature](cifacefeature.md)
  Information about a face detected in a still or video image.
- [class CITextFeature](citextfeature.md)
  Information about a region likely to contain text detected in a still or video image.
- [class CIQRCodeFeature](ciqrcodefeature.md)
  Information about a Quick Response code detected in a still or video image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirectanglefeature)*