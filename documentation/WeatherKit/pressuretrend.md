# PressureTrend

**Framework**: WeatherKit  
**Kind**: enum

The atmospheric pressure change over time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum PressureTrend
```

## Topics

### Creating the object
- [init?(rawValue: String)](pressuretrend/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Getting the trend
- [PressureTrend.falling](pressuretrend/falling.md)
  The pressure is falling.
- [PressureTrend.rising](pressuretrend/rising.md)
  The pressure is rising.
- [PressureTrend.steady](pressuretrend/steady.md)
  The pressure is not changing.
### Describing the trend
- [var accessibilityDescription: String](pressuretrend/accessibilitydescription.md)
  A localized accessibility description describing the pressure change over time.
- [var description: String](pressuretrend/description.md)
  A localized string describing the pressure trend.
### Instance Properties
- [var rawValue: String](pressuretrend/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [PressureTrend.AllCases](pressuretrend/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [PressureTrend.RawValue](pressuretrend/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [PressureTrend]](pressuretrend/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](pressuretrend/equatable-implementations.md)
- [RawRepresentable Implementations](pressuretrend/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum Precipitation](precipitation.md)
  The form of precipitation.
- [struct UVIndex](uvindex.md)
  The expected intensity of ultraviolet radiation from the sun.
- [struct Wind](wind.md)
  Contains wind data of speed, direction, and gust.
- [enum WeatherCondition](weathercondition.md)
  A description of the current weather condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/pressuretrend)*