# WAError.connectionIdleTimeout(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case

An error that occurs due to an idle or unused connection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case connectionIdleTimeout(WAError.ConnectionIdleTimeoutDetails)
```

#### Discussion

This error occurs when a connection is unused for an excessive duration and closed as a result.

## See Also

- [case publisherTimeout(WAError.PublisherTimeoutDetails)](waerror/publishertimeout(_:).md)
  An error that occurs due to publisher timeout.
- [case subscriberTimeout(WAError.SubscriberTimeoutDetails)](waerror/subscribertimeout(_:).md)
  An error that occurs due to subscriber timeout.
- [WAError.ConnectionIdleTimeoutDetails](waerror/connectionidletimeoutdetails.md)
  The optional details describing the missing resources.
- [WAError.PublisherTimeoutDetails](waerror/publishertimeoutdetails.md)
  The optional details describing the timed out publisher.
- [WAError.SubscriberTimeoutDetails](waerror/subscribertimeoutdetails.md)
  The optional details describing the timed out subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/connectionidletimeout(_:))*