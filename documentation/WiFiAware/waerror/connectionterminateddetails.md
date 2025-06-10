# WAError.ConnectionTerminatedDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the terminated connection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct ConnectionTerminatedDetails
```

## Topics

### Initializers - generated
- [init(from: any Decoder) throws](waerror/connectionterminateddetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/connectionterminateddetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WAError.PublisherTimeoutDetails](waerror/publishertimeoutdetails.md)
  The optional details describing the timed out publisher.
- [WAError.SubscriberTimeoutDetails](waerror/subscribertimeoutdetails.md)
  The optional details describing the timed-out subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/connectionterminateddetails)*