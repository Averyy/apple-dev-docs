# pressure

**Framework**: WeatherKit  
**Kind**: property

The sea level air pressure in millibars.

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
var pressure: Measurement<UnitPressure>
```

#### Discussion

This is a reduced pressure calculated by using observed conditions to remove the effects of elevation from pressure readings.

## See Also

- [var pressureTrend: PressureTrend](currentweather/pressuretrend.md)
  The direction of change of the sea level air pressure.
- [var wind: Wind](currentweather/wind.md)
  The wind speed, direction, and gust.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/currentweather/pressure)*