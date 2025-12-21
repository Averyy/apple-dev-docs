# WAError.publisherTimeout(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case

An error that occurs due to publisher timeout.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case publisherTimeout(WAError.PublisherTimeoutDetails)
```

## See Also

- [case connectionIdleTimeout(WAError.ConnectionIdleTimeoutDetails)](waerror/connectionidletimeout(_:).md)
  An error that occurs due to an idle or unused connection.
- [case subscriberTimeout(WAError.SubscriberTimeoutDetails)](waerror/subscribertimeout(_:).md)
  An error that occurs due to subscriber timeout.
- [WAError.ConnectionIdleTimeoutDetails](waerror/connectionidletimeoutdetails.md)
  The optional details describing the missing resources.
- [WAError.PublisherTimeoutDetails](waerror/publishertimeoutdetails.md)
  The optional details describing the timed out publisher.
- [WAError.SubscriberTimeoutDetails](waerror/subscribertimeoutdetails.md)
  The optional details describing the timed out subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/publishertimeout(_:))*