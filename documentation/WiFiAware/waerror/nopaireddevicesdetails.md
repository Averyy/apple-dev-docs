# WAError.NoPairedDevicesDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the lack of paired devices.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct NoPairedDevicesDetails
```

## Topics

### Initializers - generated
- [init(from: any Decoder) throws](waerror/nopaireddevicesdetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/nopaireddevicesdetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case noPairedDevices(WAError.NoPairedDevicesDetails)](waerror/nopaireddevices(_:).md)
  An error that occurs if your app doesn’t have access to any paired devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/nopaireddevicesdetails)*