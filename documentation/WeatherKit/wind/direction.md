# direction

**Framework**: WeatherKit  
**Kind**: property

The direction the wind is coming from in degrees.

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
var direction: Measurement<UnitAngle>
```

#### Discussion

True north is at `0` degrees and progresses clockwise from north.

## See Also

- [Wind.CompassDirection](wind/compassdirection-swift.enum.md)
  A compass composed of cardinal and intercardinal directions.
- [var compassDirection: Wind.CompassDirection](wind/compassdirection-swift.property.md)
  The general indicator of wind direction.
- [var gust: Measurement<UnitSpeed>?](wind/gust.md)
  A sudden increase in wind speed due to friction, wind shear, or by heating.
- [var speed: Measurement<UnitSpeed>](wind/speed.md)
  Sustained wind speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/wind/direction)*