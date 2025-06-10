# WAError.PublisherTimeoutDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the timed out publisher.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct PublisherTimeoutDetails
```

## Topics

### Generating initializers
- [init(from: any Decoder) throws](waerror/publishertimeoutdetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/publishertimeoutdetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WAError.ConnectionTerminatedDetails](waerror/connectionterminateddetails.md)
  The optional details describing the terminated connection.
- [WAError.SubscriberTimeoutDetails](waerror/subscribertimeoutdetails.md)
  The optional details describing the timed-out subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/publishertimeoutdetails)*