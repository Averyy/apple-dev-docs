# Deviation

**Framework**: WeatherKit  
**Kind**: enum

Describes a comparison between two values in a trend.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum Deviation
```

## Topics

### Operators
- [static func == (Deviation, Deviation) -> Bool](deviation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Deviation.higher](deviation/higher.md)
  The most recently observed value is larger than the value it is being compared against.
- [Deviation.lower](deviation/lower.md)
  The most recently observed value is lower than the value it is being compared against.
- [Deviation.muchHigher](deviation/muchhigher.md)
  The most recently observed value is much larger than the value it is being compared against.
- [Deviation.muchLower](deviation/muchlower.md)
  The most recently observed value is much lower than the value it is being compared against.
- [Deviation.normal](deviation/normal.md)
  The most recently observed value is about the same as the value it is being compared against.
### Initializers
- [init(from: any Decoder) throws](deviation/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](deviation/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](deviation/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](deviation/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](deviation/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/deviation)*