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

## Relationships

### Conforms To
- [CaseIterable](../swift/caseiterable.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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