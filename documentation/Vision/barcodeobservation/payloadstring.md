# payloadString

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A string value that represents the barcode payload.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
let payloadString: String?
```

#### Discussion

Depending on the symbology or the payload data itself, a string representation of the payload may not be available.

## See Also

### Getting the payload
- [let payloadData: Data?](./payloaddata.md)
  The raw data representation of the barcode’s payload.
- [let supplementalPayloadData: Data?](./supplementalpayloaddata.md)
  The raw data representation of the barcode’s supplemental payload.
- [let supplementalPayloadString: String?](./supplementalpayloadstring.md)
  The supplemental code decoded as a string value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/barcodeobservation/payloadstring)*