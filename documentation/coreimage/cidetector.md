# CIDetector

**Framework**: Core Image  
**Kind**: class

An image processor that identifies notable features, such as faces and barcodes, in a still image or video.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIDetector
```

#### Overview

> **Note**:  In macOS 10.13, iOS 11, and tvOS 11 or later, the [`Vision`](https://developer.apple.com/documentation/Vision) framework replaces these classes for identifying and analyzing image features. See [`VNRequest`](https://developer.apple.com/documentation/Vision/VNRequest).

A `CIDetector` object uses image processing to search for and identify notable features (faces, rectangles, and barcodes) in a still image or video. Detected features are represented by [`CIFeature`](cifeature.md) objects that provide more information about each feature.

This class can maintain many state variables that can impact performance. So for best performance, reuse `CIDetector` instances instead of creating new ones.

## Topics

### Creating a Detector Object
- [init?(ofType: String, context: CIContext?, options: [String : Any]?)](cidetector/init(oftype:context:options:).md)
  Creates and returns a configured detector.
### Using a Detector Object to Find Features
- [func features(in: CIImage) -> [CIFeature]](cidetector/features(in:).md)
  Searches for features in an image.
- [func features(in: CIImage, options: [String : Any]?) -> [CIFeature]](cidetector/features(in:options:).md)
  Searches for features in an image based on the specified image orientation.
### Constants
- [Detector Types](detector-types.md)
  Strings used to declare the detector for which you are interested.
- [Detector Configuration Keys](detector-configuration-keys.md)
  Keys used in the options dictionary to configure a detector.
- [Detector Accuracy Options](detector-accuracy-options.md)
  Value options used to specify the desired accuracy of the detector.
- [Feature Detection Keys](feature-detection-keys.md)
  Keys used in the options dictionary for [`features(in:options:)`](cidetector/features(in:options:).md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CIFeature](cifeature.md)
  The abstract superclass for objects representing notable features detected in an image.
- [class CIFaceFeature](cifacefeature.md)
  Information about a face detected in a still or video image.
- [class CIRectangleFeature](cirectanglefeature.md)
  Information about a rectangular region detected in a still or video image.
- [class CITextFeature](citextfeature.md)
  Information about a text that was detected in a still or video image.
- [class CIQRCodeFeature](ciqrcodefeature.md)
  Information about a Quick Response code detected in a still or video image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetector)*