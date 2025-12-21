# Precipitation

**Framework**: WeatherKit  
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