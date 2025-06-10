# WAError.serviceAlreadyPublishing(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case

An error that occurs if the system can’t create a new publisher or listener.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
case serviceAlreadyPublishing(WAError.ServiceAlreadyPublishingDetails)
```

#### Discussion

This error occurs if a publisher is already active on the service.

## See Also

- [case serviceAlreadySubscribing(WAError.ServiceAlreadySubscribingDetails)](waerror/servicealreadysubscribing(_:).md)
  An error that occurs if the system can’t create a new subscriber or browser.
- [WAError.ServiceAlreadySubscribingDetails](waerror/servicealreadysubscribingdetails.md)
  The optional details describing the service that’s subscribing.
- [WAError.ServiceAlreadyPublishingDetails](waerror/servicealreadypublishingdetails.md)
  The optional details describing the service that’s publishing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/servicealreadypublishing(_:))*