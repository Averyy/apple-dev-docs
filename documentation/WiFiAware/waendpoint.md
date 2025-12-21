# WAEndpoint

**Framework**: Wi-Fi Aware  
**Kind**: struct

The endpoint of a Wi-Fi Aware connection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct WAEndpoint
```

## Topics

### Getting the service
- [var publishedService: WAPublishableService?](waendpoint/publishedservice.md)
  The publishable service that is, or can be, connected.
- [var subscribedService: WASubscribableService?](waendpoint/subscribedservice.md)
  The subscribable service that is, or can be, connected.
### Getting the device anchoring the endpoint
- [let device: WAPairedDevice](waendpoint/device.md)
  The remote device that is, or can be, connected.
### Getting a string description
- [var description: String](waendpoint/description.md)
  The description of the object.
### Hashing and comparing
- [static func == (WAEndpoint, WAEndpoint) -> Bool](waendpoint/==(_:_:).md)
  Two endpoints are logically equivalent if they have the same service type (publish vs subscribe) with the same name, and refer to the same device.
- [func hash(into: inout Hasher)](waendpoint/hash(into:).md)
  Compute unique hash of this object.

## Relationships

### Conforms To
- [Connectable](../Network/Connectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waendpoint)*