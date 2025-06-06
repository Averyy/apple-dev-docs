# compassDirection

**Framework**: Weatherkit  
**Kind**: property

The general indicator of wind direction.

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
var compassDirection: Wind.CompassDirection
```

#### Discussion

This structure refers to the direction the wind is coming from; for instance, a north wind blows from north to south.

## See Also

- [Wind.CompassDirection](wind/compassdirection-swift.enum.md)
  A compass composed of cardinal and intercardinal directions.
- [var direction: Measurement<UnitAngle>](wind/direction.md)
  The direction the wind is coming from in degrees.
- [var gust: Measurement<UnitSpeed>?](wind/gust.md)
  A sudden increase in wind speed due to friction, wind shear, or by heating.
- [var speed: Measurement<UnitSpeed>](wind/speed.md)
  Sustained wind speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/wind/compassdirection-swift.property)*