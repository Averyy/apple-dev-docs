# Wind

**Framework**: Weatherkit  
**Kind**: struct

Contains wind data of speed, direction, and gust.

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
struct Wind
```

## Topics

### Getting the properties
- [Wind.CompassDirection](wind/compassdirection-swift.enum.md)
  A compass composed of cardinal and intercardinal directions.
- [var compassDirection: Wind.CompassDirection](wind/compassdirection-swift.property.md)
  The general indicator of wind direction.
- [var direction: Measurement<UnitAngle>](wind/direction.md)
  The direction the wind is coming from in degrees.
- [var gust: Measurement<UnitSpeed>?](wind/gust.md)
  A sudden increase in wind speed due to friction, wind shear, or by heating.
- [var speed: Measurement<UnitSpeed>](wind/speed.md)
  Sustained wind speed.
### Default Implementations
- [Decodable Implementations](wind/decodable-implementations.md)
- [Encodable Implementations](wind/encodable-implementations.md)
- [Equatable Implementations](wind/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [enum Precipitation](precipitation.md)
  The form of precipitation.
- [enum PressureTrend](pressuretrend.md)
  The atmospheric pressure change over time.
- [struct UVIndex](uvindex.md)
  The expected intensity of ultraviolet radiation from the sun.
- [enum WeatherCondition](weathercondition.md)
  A description of the current weather condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/wind)*