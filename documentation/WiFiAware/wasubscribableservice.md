# WASubscribableService

**Framework**: Wi-Fi Aware  
**Kind**: struct

A service your app discovers on remote devices and can connect to.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct WASubscribableService
```

## Mentions

- [Adopting Wi-Fi Aware](adopting-wi-fi-aware.md)

#### Overview

You specify the services your app uses in `Info.plist` via a dictionary under the `WiFiAwareServices` key:

- Each  in that dictionary is the fully qualified name of a service, and the  is a dictionary of configuration properties for that service.
- If the configuration dictionary contains the `Subscribable` key, the system creates a `WASubscribableService`  for that service and makes it available in `WASubscribableService.allServices`.

## Topics

### Selecting from your app’s subscribable services
- [static var allServices: [WASubscribableService.ID : WASubscribableService]](wasubscribableservice/allservices.md)
  A dictionary of all subscribable services declared by your app, indexed by service name.
### Checking a service name and ID
- [WASubscribableService.ID](wasubscribableservice/id-swift.typealias.md)
  The type of value that uniquely identifies the service.
- [var id: WASubscribableService.ID](wasubscribableservice/id-swift.property.md)
  A stable ID that can be used to identify this subscribable service.
- [let name: String](wasubscribableservice/name.md)
  The fully qualified name of the service, as sent over the air.
### Getting a String description
- [var description: String](wasubscribableservice/description.md)
  A string description of the service.
### Creating a service
- [init(from: any Decoder) throws](wasubscribableservice/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (WASubscribableService, WASubscribableService) -> Bool](wasubscribableservice/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](wasubscribableservice/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](wasubscribableservice/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](wasubscribableservice/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](wasubscribableservice/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [WAService](waservice.md)

## See Also

- [protocol WAService](waservice.md)
  A protocol that defines a service that a device can publish or subscribe to.
- [struct WAPublishableService](wapublishableservice.md)
  A service, hosted by your app, that remote devices can connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscribableservice)*