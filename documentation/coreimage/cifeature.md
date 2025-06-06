# CIFeature

**Framework**: Coreimage  
**Kind**: cl

The abstract superclass for objects representing notable features detected in an image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIFeature : NSObject
```

#### Overview

> **Note**: In macOS 10.13, iOS 11, and tvOS 11 or later, the [`Vision`](https://developer.apple.com/documentation/vision) framework replaces these classes for identifying and analyzing image features. See [`VNObservation`](https://developer.apple.com/documentation/vision/vnobservation).

A [`CIFeature`](cifeature.md) object represents a portion of an image that a detector believes matches its criteria. Subclasses of `CIFeature` typically hold additional information specific to the detector that discovered the feature.

## Topics

### Feature Properties
- [var bounds: CGRect](cifeature/1437782-bounds.md)
  The rectangle that holds discovered feature.
- [var type: String](cifeature/1438092-type.md)
  The type of feature that was discovered.
### Feature Types
- [let CIFeatureTypeFace: String](cifeaturetypeface.md)
  The discovered feature is a person’s face.
- [let CIFeatureTypeRectangle: String](cifeaturetyperectangle.md)
  The discovered feature is a rectangular object, though it might appear in perspective in the image.
- [let CIFeatureTypeQRCode: String](cifeaturetypeqrcode.md)
  The discovered feature is a Quick Response code (2D barcode).
- [let CIFeatureTypeText: String](cifeaturetypetext.md)
  The discovered feature is a region likely to contain upright text.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [class CIDetector](cidetector.md)
  An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [class CIFaceFeature](cifacefeature.md)
  Information about a face detected in a still or video image.
- [class CIRectangleFeature](cirectanglefeature.md)
  Information about a rectangular region detected in a still or video image.
- [class CITextFeature](citextfeature.md)
  Information about a region likely to contain text detected in a still or video image.
- [class CIQRCodeFeature](ciqrcodefeature.md)
  Information about a Quick Response code detected in a still or video image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifeature)*