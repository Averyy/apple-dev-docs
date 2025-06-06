# CIQRCodeFeature

**Framework**: Core Image  
**Kind**: cl

Information about a Quick Response code detected in a still or video image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIQRCodeFeature : CIFeature
```

#### Overview

> **Note**: In macOS 10.13, iOS 11, and tvOS 11 or later, the [`Vision`](https://developer.apple.com/documentation/vision) framework replaces these classes for identifying and analyzing image features. See [`VNDetectBarcodesRequest`](https://developer.apple.com/documentation/vision/vndetectbarcodesrequest).

In macOS 10.13, iOS 11, and tvOS 11 or later, the [`Vision`](https://developer.apple.com/documentation/vision) framework replaces these classes for identifying and analyzing image features. See [`VNDetectBarcodesRequest`](https://developer.apple.com/documentation/vision/vndetectbarcodesrequest).

A QR code is a two-dimensional barcode using the ISO/IEC 18004:2006 standard. The properties of a [`CIQRCodeFeature`](ciqrcodefeature.md) object identify the corners of the barcode in the image perspective and provide the decoded message.

To detect QR codes in an image or video, choose the [`CIDetectorTypeQRCode`](cidetectortypeqrcode.md) type when initializing a [`CIDetector`](cidetector.md) object.

## Topics

### Locating a Detected Feature
- [var bounds: CGRect](ciqrcodefeature/1438153-bounds.md)
  A rectangle indicating the position and extent of the feature in image coordinates.
### Decoding a Detected Barcode
- [var messageString: String?](ciqrcodefeature/1438035-messagestring.md)
  The string decoded from the detected barcode.
- [var symbolDescriptor: CIQRCodeDescriptor?](ciqrcodefeature/2875553-symboldescriptor.md)
  An abstract representation of a QR Code symbol.
### Identifying the Corners of a Detected Barcode
- [var bottomLeft: CGPoint](ciqrcodefeature/1437985-bottomleft.md)
  The lower-left corner of the detected barcode, in image coordinates.
- [var bottomRight: CGPoint](ciqrcodefeature/1438245-bottomright.md)
  The lower-right corner of the detected barcode, in image coordinates.
- [var topLeft: CGPoint](ciqrcodefeature/1437780-topleft.md)
  The upper-left corner of the detected barcode, in image coordinates.
- [var topRight: CGPoint](ciqrcodefeature/1437896-topright.md)
  The upper-right corner of the detected barcode, in image coordinates.

## Relationships

### Inherits From
- [CIFeature](cifeature.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

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