# WAError.serviceAlreadySubscribing(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case  
**Role**: Case

An error that occurs if a new subscriber or `Network/NetworkBrowser` can’t be created.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
case serviceAlreadySubscribing(WAError.ServiceAlreadySubscribingDetails)
```

#### Discussion

This error occurs if a subscriber is already active on the service.

## See Also

### Checking for service already in use
- [WAError.ServiceAlreadySubscribingDetails](./servicealreadysubscribingdetails.md)
  The optional details describing the service that’s subscribing.
- [case serviceAlreadyPublishing(WAError.ServiceAlreadyPublishingDetails)](./servicealreadypublishing%28_%29.md)
  An error that occurs if a new publisher or `Network/NetworkListener` can’t be created.
- [WAError.ServiceAlreadyPublishingDetails](./servicealreadypublishingdetails.md)
  The optional details describing the service that’s publishing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/servicealreadysubscribing(_:))*