# CIDetector

**Framework**: Core Image  
**Kind**: cl

An image processor that identifies notable features, such as faces and barcodes, in a still image or video.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIDetector : NSObject
```

#### Overview

> **Note**: In macOS 10.13, iOS 11, and tvOS 11 or later, the [`Vision`](https://developer.apple.com/documentation/vision) framework replaces these classes for identifying and analyzing image features. See [`VNRequest`](https://developer.apple.com/documentation/vision/vnrequest).

In macOS 10.13, iOS 11, and tvOS 11 or later, the [`Vision`](https://developer.apple.com/documentation/vision) framework replaces these classes for identifying and analyzing image features. See [`VNRequest`](https://developer.apple.com/documentation/vision/vnrequest).

A [`CIDetector`](cidetector.md) object uses image processing to search for and identify notable features (faces, rectangles, and barcodes) in a still image or video. Detected features are represented by [`CIFeature`](cifeature.md) objects that provide more information about each feature.

This class can maintain many state variables that can impact performance. So for best performance, reuse [`CIDetector`](cidetector.md) instances instead of creating new ones.

## Topics

### Creating a Detector Object
- [init?(ofType: String, context: CIContext?, options: [String : Any]?)](cidetector/1437884-init.md)
  Creates and returns a configured detector.
### Using a Detector Object to Find Features
- [func features(in: CIImage) -> [CIFeature]](cidetector/1438049-features.md)
  Searches for features in an image.
- [func features(in: CIImage, options: [String : Any]?) -> [CIFeature]](cidetector/1438189-features.md)
  Searches for features in an image based on the specified image orientation.
### Constants
- [Detector Types](cidetector/detector_types.md)
  Strings used to declare the detector for which you are interested.
- [Detector Configuration Keys](cidetector/detector_configuration_keys.md)
  Keys used in the options dictionary to configure a detector.
- [Detector Accuracy Options](cidetector/detector_accuracy_options.md)
  Value options used to specify the desired accuracy of the detector.
- [Feature Detection Keys](cidetector/feature_detection_keys.md)
  Keys used in the options dictionary for [`features(in:options:)`](cidetector/1438189-features.md).

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [class CIFeature](cifeature.md)
  The abstract superclass for objects representing notable features detected in an image.
- [class CIFaceFeature](cifacefeature.md)
  Information about a face detected in a still or video image.
- [class CIRectangleFeature](cirectanglefeature.md)
  Information about a rectangular region detected in a still or video image.
- [class CITextFeature](citextfeature.md)
  Information about a region likely to contain text detected in a still or video image.
- [class CIQRCodeFeature](ciqrcodefeature.md)
  Information about a Quick Response code detected in a still or video image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetector)*