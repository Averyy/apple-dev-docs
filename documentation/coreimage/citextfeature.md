# CITextFeature

**Framework**: Core Image  
**Kind**: class

Information about a text that was detected in a still or video image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CITextFeature
```

#### Overview

> **Note**: In macOS 10.13, iOS 11, and tvOS 11 or later, the Vision framework replaces these classes for identifying and analyzing image features. See [`VNRecognizeTextRequest`](https://developer.apple.com/documentation/Vision/VNRecognizeTextRequest))

A detected text feature is not necessarily rectangular in the plane of the image; rather, the feature identifies a shape that may be rectangular in space (for example a text on a sign) but which appears as a four-sided polygon in the image. The properties of a `CITextFeature` object identify its four corners in image coordinates.

To detect text in an image or video, choose the [`CIDetectorTypeText`](cidetectortypetext.md) type when initializing a [`CIDetector`](cidetector.md) object, and use the `CIDetectorImageOrientation` option to specify the desired orientation for finding upright text.

## Topics

### Locating a Detected Feature
- [var bounds: CGRect](citextfeature/bounds.md)
  A rectangle that indicates the position and extent of the text feature in image coordinates.
### Locating Features Within a Detected Region
- [var subFeatures: [Any]?](citextfeature/subfeatures.md)
  An array containing additional features detected within the feature.
### Identifying the Corners of a Detected Text Region
- [var bottomLeft: CGPoint](citextfeature/bottomleft.md)
  The image coordinate of the lower-left corner of the detected text.
- [var bottomRight: CGPoint](citextfeature/bottomright.md)
  The image coordinate of the lower-right corner of the detected text.
- [var topLeft: CGPoint](citextfeature/topleft.md)
  The image coordinate of the upper-left corner of the detected text.
- [var topRight: CGPoint](citextfeature/topright.md)
  The image coordinate of the upper-right corner of the detected text.

## Relationships

### Inherits From
- [CIFeature](cifeature.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CIDetector](cidetector.md)
  An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [class CIFeature](cifeature.md)
  The abstract superclass for objects representing notable features detected in an image.
- [class CIFaceFeature](cifacefeature.md)
  Information about a face detected in a still or video image.
- [class CIRectangleFeature](cirectanglefeature.md)
  Information about a rectangular region detected in a still or video image.
- [class CIQRCodeFeature](ciqrcodefeature.md)
  Information about a Quick Response code detected in a still or video image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citextfeature)*