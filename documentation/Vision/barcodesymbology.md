# BarcodeSymbology

**Framework**: Vision  
**Kind**: enum

The barcode symbologies that the framework detects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum BarcodeSymbology
```

## Topics

### Getting the symbologies
- [BarcodeSymbology.aztec](barcodesymbology/aztec.md)
- [BarcodeSymbology.codabar](barcodesymbology/codabar.md)
- [BarcodeSymbology.code128](barcodesymbology/code128.md)
- [BarcodeSymbology.code39](barcodesymbology/code39.md)
- [BarcodeSymbology.code39Checksum](barcodesymbology/code39checksum.md)
- [BarcodeSymbology.code39FullASCII](barcodesymbology/code39fullascii.md)
- [BarcodeSymbology.code39FullASCIIChecksum](barcodesymbology/code39fullasciichecksum.md)
- [BarcodeSymbology.code93](barcodesymbology/code93.md)
- [BarcodeSymbology.code93i](barcodesymbology/code93i.md)
- [BarcodeSymbology.dataMatrix](barcodesymbology/datamatrix.md)
- [BarcodeSymbology.ean13](barcodesymbology/ean13.md)
- [BarcodeSymbology.ean8](barcodesymbology/ean8.md)
- [BarcodeSymbology.gs1DataBar](barcodesymbology/gs1databar.md)
- [BarcodeSymbology.gs1DataBarExpanded](barcodesymbology/gs1databarexpanded.md)
- [BarcodeSymbology.gs1DataBarLimited](barcodesymbology/gs1databarlimited.md)
- [BarcodeSymbology.i2of5](barcodesymbology/i2of5.md)
- [BarcodeSymbology.i2of5Checksum](barcodesymbology/i2of5checksum.md)
- [BarcodeSymbology.itf14](barcodesymbology/itf14.md)
- [BarcodeSymbology.microPDF417](barcodesymbology/micropdf417.md)
- [BarcodeSymbology.microQR](barcodesymbology/microqr.md)
- [BarcodeSymbology.msiPlessey](barcodesymbology/msiplessey.md)
- [BarcodeSymbology.pdf417](barcodesymbology/pdf417.md)
- [BarcodeSymbology.qr](barcodesymbology/qr.md)
- [BarcodeSymbology.upce](barcodesymbology/upce.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var symbologies: [BarcodeSymbology]](detectbarcodesrequest/symbologies.md)
  The barcode symbologies that the request detects in an image.
- [var supportedSymbologies: [BarcodeSymbology]](detectbarcodesrequest/supportedsymbologies.md)
  The collection of barcode symbologies that the request can recognize.
- [var coalescesCompositeSymbologies: Bool](detectbarcodesrequest/coalescescompositesymbologies.md)
  A Boolean value that indicates whether the request coalesces multiple codes into one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/barcodesymbology)*