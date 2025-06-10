# WAError.NoRadioResourcesDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing what resources are lacking.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct NoRadioResourcesDetails
```

## Topics

### Initializers - generated
- [init(from: any Decoder) throws](waerror/noradioresourcesdetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/noradioresourcesdetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case noRadioResources(WAError.NoRadioResourcesDetails)](waerror/noradioresources(_:).md)
  An error that occurs if the radio lacks resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/noradioresourcesdetails)*