# WAError.SubscriberTimeoutDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct  
**Role**: Structure

The optional details describing the timed out subscriber.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct SubscriberTimeoutDetails
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
- [WAError.ConnectionIdleTimeoutDetails](./connectionidletimeoutdetails.md)
  The optional details describing the missing resources.
- [WAError.PublisherTimeoutDetails](./publishertimeoutdetails.md)
  The optional details describing the timed out publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/subscribertimeoutdetails)*