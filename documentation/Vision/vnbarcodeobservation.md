# VNBarcodeObservation

**Framework**: Vision  
**Kind**: class

An object that represents barcode information that an image analysis request detects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNBarcodeObservation
```

#### Overview

This type of observation results from a [`VNDetectBarcodesRequest`](vndetectbarcodesrequest.md). It contains information about the detected barcode, including parsed payload data for supported symbologies.

## Topics

### Parsing the Payload
- [var payloadStringValue: String?](vnbarcodeobservation/payloadstringvalue.md)
  A string value that represents the barcode payload.
- [var payloadData: Data?](vnbarcodeobservation/payloaddata.md)
  The raw data representation of the barcode’s payload.
- [var supplementalPayloadString: String?](vnbarcodeobservation/supplementalpayloadstring.md)
  The supplemental code decoded as a string value.
- [var supplementalPayloadData: Data?](vnbarcodeobservation/supplementalpayloaddata.md)
- [var supplementalCompositeType: VNBarcodeCompositeType](vnbarcodeobservation/supplementalcompositetype.md)
  The supplemental composite type.
- [var isGS1DataCarrier: Bool](vnbarcodeobservation/isgs1datacarrier.md)
  A Boolean value that indicates whether the barcode carries any global standards data.
### Reading Barcode Descriptors
- [var barcodeDescriptor: CIBarcodeDescriptor?](vnbarcodeobservation/barcodedescriptor.md)
  An object that describes the low-level details about the barcode and its data.
### Identifying Barcode Types
- [var symbology: VNBarcodeSymbology](vnbarcodeobservation/symbology.md)
  The symbology of the observed barcode.
### Identifying Barcode Colors
- [var isColorInverted: Bool](vnbarcodeobservation/iscolorinverted.md)
  A Boolean value that indicates whether the barcode is color inverted.

## Relationships

### Inherits From
- [VNRectangleObservation](vnrectangleobservation.md)
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
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [var results: [VNBarcodeObservation]?](vndetectbarcodesrequest/results.md)
  The results of a barcode detection request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnbarcodeobservation)*