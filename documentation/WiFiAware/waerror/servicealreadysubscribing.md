# WAError.serviceAlreadySubscribing(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case

An error that occurs if the system can’t create a new subscriber or browser.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
case serviceAlreadySubscribing(WAError.ServiceAlreadySubscribingDetails)
```

#### Discussion

This error occurs if a subscriber is already active on the service.

## See Also

- [WAError.ServiceAlreadySubscribingDetails](waerror/servicealreadysubscribingdetails.md)
  The optional details describing the service that’s subscribing.
- [case serviceAlreadyPublishing(WAError.ServiceAlreadyPublishingDetails)](waerror/servicealreadypublishing(_:).md)
  An error that occurs if the system can’t create a new publisher or listener.
- [WAError.ServiceAlreadyPublishingDetails](waerror/servicealreadypublishingdetails.md)
  The optional details describing the service that’s publishing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/servicealreadysubscribing(_:))*