# WAError.DeviceNoLongerAvailableDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the lost device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct DeviceNoLongerAvailableDetails
```

## Topics

### Initializers - generated
- [init(from: any Decoder) throws](waerror/devicenolongeravailabledetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/devicenolongeravailabledetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case deviceNoLongerAvailable(WAError.DeviceNoLongerAvailableDetails)](waerror/devicenolongeravailable(_:).md)
  An error that occurs if a device is out of range or no longer available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/devicenolongeravailabledetails)*