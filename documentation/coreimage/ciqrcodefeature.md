# CIQRCodeFeature

**Framework**: Core Image  
**Kind**: class

Information about a Quick Response code detected in a still or video image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIQRCodeFeature
```

#### Overview

> **Note**:  In macOS 10.13, iOS 11, and tvOS 11 or later, the [`Vision`](https://developer.apple.com/documentation/Vision) framework replaces these classes for identifying and analyzing image features. See [`VNDetectBarcodesRequest`](https://developer.apple.com/documentation/Vision/VNDetectBarcodesRequest).

A QR code is a two-dimensional barcode using the ISO/IEC 18004:2006 standard. The properties of a [`CIQRCodeFeature`](ciqrcodefeature.md) object identify the corners of the barcode in the image perspective and provide the decoded message.

To detect QR codes in an image or video, choose the [`CIDetectorTypeQRCode`](cidetectortypeqrcode.md) type when initializing a [`CIDetector`](cidetector.md) object.

## Topics

### Locating a Detected Feature
- [var bounds: CGRect](ciqrcodefeature/bounds-swift.property.md)
  A rectangle indicating the position and extent of the feature in image coordinates.
### Decoding a Detected Barcode
- [var messageString: String?](ciqrcodefeature/messagestring.md)
  The string decoded from the detected barcode.
- [var symbolDescriptor: CIQRCodeDescriptor?](ciqrcodefeature/symboldescriptor-swift.property.md)
  An abstract representation of a QR Code symbol.
### Identifying the Corners of a Detected Barcode
- [var bottomLeft: CGPoint](ciqrcodefeature/bottomleft-swift.property.md)
  The lower-left corner of the detected barcode, in image coordinates.
- [var bottomRight: CGPoint](ciqrcodefeature/bottomright-swift.property.md)
  The lower-right corner of the detected barcode, in image coordinates.
- [var topLeft: CGPoint](ciqrcodefeature/topleft-swift.property.md)
  The upper-left corner of the detected barcode, in image coordinates.
- [var topRight: CGPoint](ciqrcodefeature/topright-swift.property.md)
  The upper-right corner of the detected barcode, in image coordinates.

## Relationships

### Inherits From
- [CIFeature](cifeature.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CIDetector](cidetector.md)
  An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [class CIFeature](cifeature.md)
  The abstract superclass for objects representing notable features detected in an image.
- [class CIFaceFeature](cifacefeature.md)
  Information about a face detected in a still or video image.
- [class CIRectangleFeature](cirectanglefeature.md)
  Information about a rectangular region detected in a still or video image.
- [class CITextFeature](citextfeature.md)
  Information about a region likely to contain text detected in a still or video image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodefeature)*