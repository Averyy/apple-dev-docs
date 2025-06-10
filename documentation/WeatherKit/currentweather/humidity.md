# humidity

**Framework**: WeatherKit  
**Kind**: property

The amount of water vapor in the air.

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
var humidity: Double
```

#### Discussion

Relative humidity measures the amount of water vapor in the air, compared to the maximum amount that the air can hold at the current temperature.

The range of this property is from `0` to `1`, inclusive.

## See Also

- [var apparentTemperature: Measurement<UnitTemperature>](currentweather/apparenttemperature.md)
  The feels-like temperature when factoring wind and humidity.
- [var dewPoint: Measurement<UnitTemperature>](currentweather/dewpoint.md)
  The temperature at which relative humidity is 100%.
- [var temperature: Measurement<UnitTemperature>](currentweather/temperature.md)
  The current temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/currentweather/humidity)*