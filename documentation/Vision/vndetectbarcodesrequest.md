# VNDetectBarcodesRequest

**Framework**: Vision  
**Kind**: class

A request that detects barcodes in an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectBarcodesRequest
```

#### Overview

This request returns an array of [`VNBarcodeObservation`](vnbarcodeobservation.md) objects, one for each barcode it detects.

## Topics

### Specifying Symbologies
- [func supportedSymbologies() throws -> [VNBarcodeSymbology]](vndetectbarcodesrequest/supportedsymbologies.md)
  Returns the barcode symbologies that the request supports.
- [var symbologies: [VNBarcodeSymbology]](vndetectbarcodesrequest/symbologies.md)
  The barcode symbologies that the request detects in an image.
- [var coalesceCompositeSymbologies: Bool](vndetectbarcodesrequest/coalescecompositesymbologies.md)
  A Boolean value that indicates whether to coalesce multiple codes based on the symbology.
- [struct VNBarcodeSymbology](vnbarcodesymbology.md)
  The barcode symbologies that the framework detects.
- [class var supportedSymbologies: [VNBarcodeSymbology]](vndetectbarcodesrequest/supportedsymbologies.md)
  The array of barcode symbologies that the request supports.
### Accessing the Results
- [var results: [VNBarcodeObservation]?](vndetectbarcodesrequest/results.md)
  The results of a barcode detection request.
- [class VNBarcodeObservation](vnbarcodeobservation.md)
  An object that represents barcode information that an image analysis request detects.
### Identifying Request Revisions
- [let VNDetectBarcodesRequestRevision3: Int](vndetectbarcodesrequestrevision3.md)
  A constant for specifying revision 3 of the barcode detection request.
- [let VNDetectBarcodesRequestRevision2: Int](vndetectbarcodesrequestrevision2.md)
  A constant for specifying revision 2 of the barcode detection request.
- [let VNDetectBarcodesRequestRevision1: Int](vndetectbarcodesrequestrevision1.md)
  A constant for specifying revision 1 of the barcode detection request.

## Relationships

### Inherits From
- [VNImageBasedRequest](vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [enum VNBarcodeCompositeType](vnbarcodecompositetype.md)
  Composite types for barcode requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectbarcodesrequest)*