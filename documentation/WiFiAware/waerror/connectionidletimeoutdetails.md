# WAError.ConnectionIdleTimeoutDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct  
**Role**: Structure

The optional details describing the missing resources.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct ConnectionIdleTimeoutDetails
```

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Checking for timeouts
- [case connectionIdleTimeout(WAError.ConnectionIdleTimeoutDetails)](./connectionidletimeout%28_%29.md)
  An error that occurs due to an idle or unused connection.
- [case publisherTimeout(WAError.PublisherTimeoutDetails)](./publishertimeout%28_%29.md)
  An error that occurs due to publisher timeout.
- [case subscriberTimeout(WAError.SubscriberTimeoutDetails)](./subscribertimeout%28_%29.md)
  An error that occurs due to subscriber timeout.
- [WAError.PublisherTimeoutDetails](./publishertimeoutdetails.md)
  The optional details describing the timed out publisher.
- [WAError.SubscriberTimeoutDetails](./subscribertimeoutdetails.md)
  The optional details describing the timed out subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/connectionidletimeoutdetails)*