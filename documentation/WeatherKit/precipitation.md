# Precipitation

**Framework**: Weatherkit  
**Kind**: enum

The form of precipitation.

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
enum Precipitation
```

## Topics

### Creating the object
- [init?(rawValue: String)](precipitation/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Specifying precipitation types
- [Precipitation.hail](precipitation/hail.md)
  A form of precipitation consisting of solid ice.
- [Precipitation.mixed](precipitation/mixed.md)
  Wintry Mix.
- [Precipitation.rain](precipitation/rain.md)
  Rain.
- [Precipitation.sleet](precipitation/sleet.md)
  A form of precipitation consisting of ice pellets.
- [Precipitation.snow](precipitation/snow.md)
  Snow.
- [Precipitation.none](precipitation/none.md)
  No precipitation.
### Describing the precipitation
- [var accessibilityDescription: String](precipitation/accessibilitydescription.md)
  A localized accessibility description describing the form of precipitation.
- [var description: String](precipitation/description.md)
  A localized string describing the form of precipitation.
### Instance Properties
- [var rawValue: String](precipitation/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [Precipitation.AllCases](precipitation/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [Precipitation.RawValue](precipitation/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [Precipitation]](precipitation/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](precipitation/equatable-implementations.md)
- [RawRepresentable Implementations](precipitation/rawrepresentable-implementations.md)

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

## See Also

- [enum PressureTrend](pressuretrend.md)
  The atmospheric pressure change over time.
- [struct UVIndex](uvindex.md)
  The expected intensity of ultraviolet radiation from the sun.
- [struct Wind](wind.md)
  Contains wind data of speed, direction, and gust.
- [enum WeatherCondition](weathercondition.md)
  A description of the current weather condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/precipitation)*