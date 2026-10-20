# payloadStringValue

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly, nullable) NSString * payloadStringValue;
```

#### Discussion

Depending on the symbology or the payload data itself, a string representation of the payload may not be available.

## See Also

### Parsing the Payload
- [var payloadData: Data?](./payloaddata.md)
  The raw data representation of the barcode’s payload.
- [var supplementalPayloadString: String?](./supplementalpayloadstring.md)
  The supplemental code decoded as a string value.
- [var supplementalPayloadData: Data?](./supplementalpayloaddata.md)
- [var supplementalCompositeType: VNBarcodeCompositeType](./supplementalcompositetype.md)
  The supplemental composite type.
- [var isGS1DataCarrier: Bool](./isgs1datacarrier.md)
  A Boolean value that indicates whether the barcode carries any global standards data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnbarcodeobservation/payloadstringvalue)*