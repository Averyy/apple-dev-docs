# WAError.serviceAlreadyPublishing(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case  
**Role**: Case

An error that occurs if a new publisher or `Network/NetworkListener` can’t be created.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
case serviceAlreadyPublishing(WAError.ServiceAlreadyPublishingDetails)
```

## Discussion

This error occurs if a publisher is already active on the service.

## See Also

### Checking for service already in use
- [case serviceAlreadySubscribing(WAError.ServiceAlreadySubscribingDetails)](./servicealreadysubscribing%28_%29.md)
  An error that occurs if a new subscriber or `Network/NetworkBrowser` can’t be created.
- [WAError.ServiceAlreadySubscribingDetails](./servicealreadysubscribingdetails.md)
  The optional details describing the service that’s subscribing.
- [WAError.ServiceAlreadyPublishingDetails](./servicealreadypublishingdetails.md)
  The optional details describing the service that’s publishing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/servicealreadypublishing(_:))*