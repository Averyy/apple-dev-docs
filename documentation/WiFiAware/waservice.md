# WAService

**Framework**: Wi-Fi Aware  
**Kind**: protocol

A protocol that defines a service that a device can publish or subscribe to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol WAService : CustomStringConvertible, Decodable, Encodable, Hashable, Identifiable, Sendable
```

#### Overview

A service represents a specific function or use case that’s performed over Wi-Fi Aware. Services are specific functionality and protocols that your app can publish or subscribe to on other devices.

Services are identified by a service name string that follows the rules in [`RFC 6763`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc6763#section-4.1.2) and [`RFC 6335`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc6335#section-5.1). For a service name of `example-service`, the full service name encoded in the `Info.plist` and sent over the air is either `_example-service._tcp` if using the TCP protocol or `_example-service._udp` if using any other protocol.

You must register your app with a unique name in the [`IANA service name registry`](https://developer.apple.comhttps://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml) to avoid conflicts with other apps and devices.

If you have an invalid service name in the `Info.plist`, your app crashes.

## Topics

### Selecting from your app’s services
- [static var allServices: [String : Self]](waservice/allservices.md)
  A dictionary of all services declared by your app, indexed by service name.
### Checking a service name
- [var name: String](waservice/name.md)
  The full name of the service, as sent over the air.

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [WAPublishableService](wapublishableservice.md)
- [WASubscribableService](wasubscribableservice.md)

## See Also

- [struct WASubscribableService](wasubscribableservice.md)
  A service your app discovers on remote devices and can connect to.
- [struct WAPublishableService](wapublishableservice.md)
  A service, hosted by your app, that remote devices can connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waservice)*