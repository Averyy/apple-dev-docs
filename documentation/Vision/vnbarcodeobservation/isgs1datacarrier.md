# isGS1DataCarrier

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the barcode carries any global standards data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isGS1DataCarrier: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isGS1DataCarrier;
```

## See Also

### Parsing the Payload
- [var payloadStringValue: String?](./payloadstringvalue.md)
  A string value that represents the barcode payload.
- [var payloadData: Data?](./payloaddata.md)
  The raw data representation of the barcode’s payload.
- [var supplementalPayloadString: String?](./supplementalpayloadstring.md)
  The supplemental code decoded as a string value.
- [var supplementalPayloadData: Data?](./supplementalpayloaddata.md)
- [var supplementalCompositeType: VNBarcodeCompositeType](./supplementalcompositetype.md)
  The supplemental composite type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnbarcodeobservation/isgs1datacarrier)*