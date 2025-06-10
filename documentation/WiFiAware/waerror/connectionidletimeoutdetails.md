# WAError.ConnectionIdleTimeoutDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the missing resources.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct ConnectionIdleTimeoutDetails
```

## Topics

### Initializers - generated
- [init(from: any Decoder) throws](waerror/connectionidletimeoutdetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/connectionidletimeoutdetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case connectionIdleTimeout(WAError.ConnectionIdleTimeoutDetails)](waerror/connectionidletimeout(_:).md)
  An error that occurs due to an idle or unused connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/connectionidletimeoutdetails)*