# supplementalPayloadString

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The supplemental code decoded as a string value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var supplementalPayloadString: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * supplementalPayloadString;
```

## See Also

### Parsing the Payload
- [var payloadStringValue: String?](./payloadstringvalue.md)
  A string value that represents the barcode payload.
- [var payloadData: Data?](./payloaddata.md)
  The raw data representation of the barcode’s payload.
- [var supplementalPayloadData: Data?](./supplementalpayloaddata.md)
- [var supplementalCompositeType: VNBarcodeCompositeType](./supplementalcompositetype.md)
  The supplemental composite type.
- [var isGS1DataCarrier: Bool](./isgs1datacarrier.md)
  A Boolean value that indicates whether the barcode carries any global standards data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnbarcodeobservation/supplementalpayloadstring)*