# WAError.ServiceAlreadySubscribingDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct  
**Role**: Structure

The optional details describing the service that’s subscribing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct ServiceAlreadySubscribingDetails
```

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Checking for service already in use
- [case serviceAlreadySubscribing(WAError.ServiceAlreadySubscribingDetails)](./servicealreadysubscribing%28_%29.md)
  An error that occurs if a new subscriber or `Network/NetworkBrowser` can’t be created.
- [case serviceAlreadyPublishing(WAError.ServiceAlreadyPublishingDetails)](./servicealreadypublishing%28_%29.md)
  An error that occurs if a new publisher or `Network/NetworkListener` can’t be created.
- [WAError.ServiceAlreadyPublishingDetails](./servicealreadypublishingdetails.md)
  The optional details describing the service that’s publishing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/servicealreadysubscribingdetails)*