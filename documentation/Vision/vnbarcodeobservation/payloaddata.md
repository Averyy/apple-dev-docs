# payloadData

**Framework**: Vision  
**Kind**: property

The raw data representation of the barcode’s payload.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var payloadData: Data? { get }
```

## See Also

- [var payloadStringValue: String?](vnbarcodeobservation/payloadstringvalue.md)
  A string value that represents the barcode payload.
- [var supplementalPayloadString: String?](vnbarcodeobservation/supplementalpayloadstring.md)
  The supplemental code decoded as a string value.
- [var supplementalPayloadData: Data?](vnbarcodeobservation/supplementalpayloaddata.md)
- [var supplementalCompositeType: VNBarcodeCompositeType](vnbarcodeobservation/supplementalcompositetype.md)
  The supplemental composite type.
- [var isGS1DataCarrier: Bool](vnbarcodeobservation/isgs1datacarrier.md)
  A Boolean value that indicates whether the barcode carries any global standards data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnbarcodeobservation/payloaddata)*