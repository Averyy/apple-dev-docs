# HourTemperatureStatistics

**Framework**: Weatherkit  
**Kind**: struct

A structure that describes temperature statistics for a specific hour.

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
struct HourTemperatureStatistics
```

## Topics

### Operators
- [static func == (HourTemperatureStatistics, HourTemperatureStatistics) -> Bool](hourtemperaturestatistics/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](hourtemperaturestatistics/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hour: Int](hourtemperaturestatistics/hour.md)
  The hour of the year, in UTC.
- [var percentiles: Percentiles<UnitTemperature>](hourtemperaturestatistics/percentiles.md)
  The temperature statistics for the hour.
### Instance Methods
- [func encode(to: any Encoder) throws](hourtemperaturestatistics/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](hourtemperaturestatistics/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/hourtemperaturestatistics)*