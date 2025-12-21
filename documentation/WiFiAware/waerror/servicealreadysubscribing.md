# WAError.serviceAlreadySubscribing(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case

An error that occurs if a new subscriber or `Network/NetworkBrowser` can’t be created.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

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
  An error that occurs if a new publisher or `Network/NetworkListener` can’t be created.
- [WAError.ServiceAlreadyPublishingDetails](waerror/servicealreadypublishingdetails.md)
  The optional details describing the service that’s publishing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/servicealreadysubscribing(_:))*