# nauticalDawn

**Framework**: Weatherkit  
**Kind**: property

The time of nautical sunrise when the sun’s center is 12° below the horizon.

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
var nauticalDawn: Date?
```

#### Discussion

There is enough light for sailors to distinguish the horizon at sea, but the sky is too dark for outdoor activities. This property is optional because it’s possible for the sun to not rise on a given day, at extreme latitudes.

## See Also

- [var astronomicalDawn: Date?](sunevents/astronomicaldawn.md)
  The time of astronomical sunrise when the sun’s center is 18° below the horizon.
- [var astronomicalDusk: Date?](sunevents/astronomicaldusk.md)
  The time of astronomical sunset, when the sun’s center is 18° below the horizon.
- [var civilDawn: Date?](sunevents/civildawn.md)
  The time of civil sunrise when the sun’s center is 6° below the horizon.
- [var civilDusk: Date?](sunevents/civildusk.md)
  The time of civil sunset, when the sun’s center is 6° below the horizon.
- [var nauticalDusk: Date?](sunevents/nauticaldusk.md)
  The time of nautical sunset, when the sun’s center is 12° below the horizon.
- [var solarMidnight: Date?](sunevents/solarmidnight.md)
  Represents solar midnight, the time when the sun reaches its lowest point in the sky.
- [var solarNoon: Date?](sunevents/solarnoon.md)
  Represents solar noon, the time when the sun reaches its highest point in the sky.
- [var sunrise: Date?](sunevents/sunrise.md)
  The sunrise time immediately before the solar transit closest to calendar noon.
- [var sunset: Date?](sunevents/sunset.md)
  The sunset time immediately after the solar transit closest to calendar noon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/sunevents/nauticaldawn)*