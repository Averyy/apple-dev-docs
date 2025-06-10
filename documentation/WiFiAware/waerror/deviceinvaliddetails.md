# WAError.DeviceInvalidDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the device that’s invalid.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct DeviceInvalidDetails
```

## Topics

### Initializers - generated
- [init(from: any Decoder) throws](waerror/deviceinvaliddetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/deviceinvaliddetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case deviceInvalid(WAError.DeviceInvalidDetails)](waerror/deviceinvalid(_:).md)
  An error that occurs if your app specifies a paired device to which it doesn’t have access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/deviceinvaliddetails)*