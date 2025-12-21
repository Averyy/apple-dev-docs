# WAError.ServiceAlreadyPublishingDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the service that’s publishing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct ServiceAlreadyPublishingDetails
```

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case serviceAlreadySubscribing(WAError.ServiceAlreadySubscribingDetails)](waerror/servicealreadysubscribing(_:).md)
  An error that occurs if a new subscriber or `Network/NetworkBrowser` can’t be created.
- [WAError.ServiceAlreadySubscribingDetails](waerror/servicealreadysubscribingdetails.md)
  The optional details describing the service that’s subscribing.
- [case serviceAlreadyPublishing(WAError.ServiceAlreadyPublishingDetails)](waerror/servicealreadypublishing(_:).md)
  An error that occurs if a new publisher or `Network/NetworkListener` can’t be created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/servicealreadypublishingdetails)*