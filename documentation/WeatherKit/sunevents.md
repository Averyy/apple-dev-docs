# SunEvents

**Framework**: Weatherkit  
**Kind**: struct

An enumeration that represents dates of solar events, including sunrise, sunset, dawn, and dusk.

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
struct SunEvents
```

## Topics

### Getting the sun events
- [var astronomicalDawn: Date?](sunevents/astronomicaldawn.md)
  The time of astronomical sunrise when the sun’s center is 18° below the horizon.
- [var astronomicalDusk: Date?](sunevents/astronomicaldusk.md)
  The time of astronomical sunset, when the sun’s center is 18° below the horizon.
- [var civilDawn: Date?](sunevents/civildawn.md)
  The time of civil sunrise when the sun’s center is 6° below the horizon.
- [var civilDusk: Date?](sunevents/civildusk.md)
  The time of civil sunset, when the sun’s center is 6° below the horizon.
- [var nauticalDawn: Date?](sunevents/nauticaldawn.md)
  The time of nautical sunrise when the sun’s center is 12° below the horizon.
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
### Default Implementations
- [Decodable Implementations](sunevents/decodable-implementations.md)
- [Encodable Implementations](sunevents/encodable-implementations.md)
- [Equatable Implementations](sunevents/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct MoonEvents](moonevents.md)
  A structure that represents lunar events.
- [enum MoonPhase](moonphase.md)
  An enumeration that specifies the moon phase kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/sunevents)*