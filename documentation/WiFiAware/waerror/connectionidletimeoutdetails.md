# WAError.ConnectionIdleTimeoutDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the missing resources.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct ConnectionIdleTimeoutDetails
```

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case connectionIdleTimeout(WAError.ConnectionIdleTimeoutDetails)](waerror/connectionidletimeout(_:).md)
  An error that occurs due to an idle or unused connection.
- [case publisherTimeout(WAError.PublisherTimeoutDetails)](waerror/publishertimeout(_:).md)
  An error that occurs due to publisher timeout.
- [case subscriberTimeout(WAError.SubscriberTimeoutDetails)](waerror/subscribertimeout(_:).md)
  An error that occurs due to subscriber timeout.
- [WAError.PublisherTimeoutDetails](waerror/publishertimeoutdetails.md)
  The optional details describing the timed out publisher.
- [WAError.SubscriberTimeoutDetails](waerror/subscribertimeoutdetails.md)
  The optional details describing the timed out subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/connectionidletimeoutdetails)*