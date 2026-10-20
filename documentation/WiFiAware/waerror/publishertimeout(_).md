# WAError.publisherTimeout(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case  
**Role**: Case

An error that occurs due to publisher timeout.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
case publisherTimeout(WAError.PublisherTimeoutDetails)
```

## See Also

### Checking for timeouts
- [case connectionIdleTimeout(WAError.ConnectionIdleTimeoutDetails)](./connectionidletimeout%28_%29.md)
  An error that occurs due to an idle or unused connection.
- [case subscriberTimeout(WAError.SubscriberTimeoutDetails)](./subscribertimeout%28_%29.md)
  An error that occurs due to subscriber timeout.
- [WAError.ConnectionIdleTimeoutDetails](./connectionidletimeoutdetails.md)
  The optional details describing the missing resources.
- [WAError.PublisherTimeoutDetails](./publishertimeoutdetails.md)
  The optional details describing the timed out publisher.
- [WAError.SubscriberTimeoutDetails](./subscribertimeoutdetails.md)
  The optional details describing the timed out subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/publishertimeout(_:))*