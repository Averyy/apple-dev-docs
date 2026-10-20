# civilDawn

**Framework**: WeatherKit  
**Kind**: property  
**Role**: Instance Property

The time of civil sunrise when the sun’s center is 6° below the horizon.

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
var civilDawn: Date?
```

#### Discussion

Civil dawn begins when there’s enough light for most objects to be seen, so it’s often used to determine when outdoor activities may begin. This property is optional because it’s possible for the sun to not rise on a given day, at extreme latitudes.

## See Also

### Getting the sun events
- [var astronomicalDawn: Date?](./astronomicaldawn.md)
  The time of astronomical sunrise when the sun’s center is 18° below the horizon.
- [var astronomicalDusk: Date?](./astronomicaldusk.md)
  The time of astronomical sunset, when the sun’s center is 18° below the horizon.
- [var civilDusk: Date?](./civildusk.md)
  The time of civil sunset, when the sun’s center is 6° below the horizon.
- [var nauticalDawn: Date?](./nauticaldawn.md)
  The time of nautical sunrise when the sun’s center is 12° below the horizon.
- [var nauticalDusk: Date?](./nauticaldusk.md)
  The time of nautical sunset, when the sun’s center is 12° below the horizon.
- [var solarMidnight: Date?](./solarmidnight.md)
  Represents solar midnight, the time when the sun reaches its lowest point in the sky.
- [var solarNoon: Date?](./solarnoon.md)
  Represents solar noon, the time when the sun reaches its highest point in the sky.
- [var sunrise: Date?](./sunrise.md)
  The sunrise time immediately before the solar transit closest to calendar noon.
- [var sunset: Date?](./sunset.md)
  The sunset time immediately after the solar transit closest to calendar noon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/sunevents/civildawn)*