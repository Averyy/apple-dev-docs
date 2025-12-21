# payloadString

**Framework**: Vision  
**Kind**: property

A string value that represents the barcode payload.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let payloadString: String?
```

#### Discussion

Depending on the symbology or the payload data itself, a string representation of the payload may not be available.

## See Also

- [let payloadData: Data?](barcodeobservation/payloaddata.md)
  The raw data representation of the barcode’s payload.
- [let supplementalPayloadData: Data?](barcodeobservation/supplementalpayloaddata.md)
  The raw data representation of the barcode’s supplemental payload.
- [let supplementalPayloadString: String?](barcodeobservation/supplementalpayloadstring.md)
  The supplemental code decoded as a string value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/barcodeobservation/payloadstring)*