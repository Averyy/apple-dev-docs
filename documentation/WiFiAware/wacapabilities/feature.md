# WACapabilities.Feature

**Framework**: Wi-Fi Aware  
**Kind**: enum

Features that your app’s current host device can support.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum Feature
```

#### Overview

Supported features are typically created by the system on behalf of the client, so they usually don’t need to be instantiated directly.

## Topics

### Checking for Wi-Fi Aware support
- [WACapabilities.Feature.wifiAware](wacapabilities/feature/wifiaware.md)
  Indicates that the host supports Wi-Fi Aware.
### Creating supported features
- [init(from: any Decoder) throws](wacapabilities/feature/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (WACapabilities.Feature, WACapabilities.Feature) -> Bool](wacapabilities/feature/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](wacapabilities/feature/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](wacapabilities/feature/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](wacapabilities/feature/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [WACapabilities.Feature.AllCases](wacapabilities/feature/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Type Properties
- [static var allCases: [WACapabilities.Feature]](wacapabilities/feature/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](wacapabilities/feature/equatable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WACapabilities](wacapabilities.md)
  A structure that checks the host device’s supported features and capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wacapabilities/feature)*