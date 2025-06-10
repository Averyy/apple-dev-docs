# WAError.ServiceAlreadyPublishingDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the service that’s publishing.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct ServiceAlreadyPublishingDetails
```

## Topics

### Generating initializers
- [init(from: any Decoder) throws](waerror/servicealreadypublishingdetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/servicealreadypublishingdetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case serviceAlreadySubscribing(WAError.ServiceAlreadySubscribingDetails)](waerror/servicealreadysubscribing(_:).md)
  An error that occurs if the system can’t create a new subscriber or browser.
- [WAError.ServiceAlreadySubscribingDetails](waerror/servicealreadysubscribingdetails.md)
  The optional details describing the service that’s subscribing.
- [case serviceAlreadyPublishing(WAError.ServiceAlreadyPublishingDetails)](waerror/servicealreadypublishing(_:).md)
  An error that occurs if the system can’t create a new publisher or listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/servicealreadypublishingdetails)*