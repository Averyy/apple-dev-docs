# pressure

**Framework**: WeatherKit  
**Kind**: property  
**Role**: Instance Property

The atmospheric pressure at sea level at a given location.

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

### Getting pressure
- [var pressureTrend: PressureTrend](./pressuretrend.md)
  The kind and amount of atmospheric pressure change over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/hourweather/pressure)*