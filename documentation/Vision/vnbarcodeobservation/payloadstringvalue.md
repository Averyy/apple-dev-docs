# payloadStringValue

**Framework**: Vision  
**Kind**: property

A string value that represents the barcode payload.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var payloadStringValue: String? { get }
```

#### Discussion

Depending on the symbology or the payload data itself, a string representation of the payload may not be available.

## See Also

- [var payloadData: Data?](vnbarcodeobservation/payloaddata.md)
  The raw data representation of the barcode’s payload.
- [var supplementalPayloadString: String?](vnbarcodeobservation/supplementalpayloadstring.md)
  The supplemental code decoded as a string value.
- [var supplementalPayloadData: Data?](vnbarcodeobservation/supplementalpayloaddata.md)
- [var supplementalCompositeType: VNBarcodeCompositeType](vnbarcodeobservation/supplementalcompositetype.md)
  The supplemental composite type.
- [var isGS1DataCarrier: Bool](vnbarcodeobservation/isgs1datacarrier.md)
  A Boolean value that indicates whether the barcode carries any global standards data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnbarcodeobservation/payloadstringvalue)*