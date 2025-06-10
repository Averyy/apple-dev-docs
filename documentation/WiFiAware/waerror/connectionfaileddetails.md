# WAError.ConnectionFailedDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the failed connection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct ConnectionFailedDetails
```

## Topics

### Generating initializers
- [init(from: any Decoder) throws](waerror/connectionfaileddetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/connectionfaileddetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case connectionFailed(WAError.ConnectionFailedDetails)](waerror/connectionfailed(_:).md)
  An error that occurs if the service is unable to connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/connectionfaileddetails)*