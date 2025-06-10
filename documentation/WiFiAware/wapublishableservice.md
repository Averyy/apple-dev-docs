# WAPublishableService

**Framework**: Wi-Fi Aware  
**Kind**: struct

A service, hosted by your app, that remote devices can connect to.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct WAPublishableService
```

## Mentions

- [Adopting Wi-Fi Aware](adopting-wi-fi-aware.md)

#### Overview

You specify the services your app uses in `Info.plist` via a dictionary under the `WiFiAwareServices` key:

- Each  in that dictionary is the fully qualified name of a service, and the  is a dictionary of configuration properties for that service.
- If the configuration dictionary contains the `Publishable` key, the system creates a `WAPublishableService` for that service and makes it available in `WAPublishableService.allServices`.

## Topics

### Selecting from your app’s publishable services
- [static var allServices: [WAPublishableService.ID : WAPublishableService]](wapublishableservice/allservices.md)
  A dictionary of all publishable services declared by your app, indexed by service name.
### Checking a service name and ID
- [WAPublishableService.ID](wapublishableservice/id-swift.typealias.md)
  The type of value that uniquely identifies the service.
- [var id: WAPublishableService.ID](wapublishableservice/id-swift.property.md)
  A stable ID that the system can use to identify this publishable service.
- [let name: String](wapublishableservice/name.md)
  The fully qualified name of the service, as sent over the air.
### Getting a string description
- [var description: String](wapublishableservice/description.md)
  A description of the service.
### Creating a service
- [init(from: any Decoder) throws](wapublishableservice/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (WAPublishableService, WAPublishableService) -> Bool](wapublishableservice/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](wapublishableservice/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](wapublishableservice/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](wapublishableservice/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](wapublishableservice/equatable-implementations.md)

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
- [struct WASubscribableService](wasubscribableservice.md)
  A service your app discovers on remote devices and can connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublishableservice)*