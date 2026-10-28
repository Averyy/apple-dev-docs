# Wind.CompassDirection

**Framework**: WeatherKit  
**Kind**: enum  
**Role**: Enumeration

A compass composed of cardinal and intercardinal directions.

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
@frozen
enum CompassDirection
```

## Overview

This enumeration represents true headings.

## Topics

### Describing the compass direction
- [var abbreviation: String](./compassdirection-swift.enum/abbreviation.md)
  A localized short abbreviation of the wind compass direction.
- [var accessibilityDescription: String](./compassdirection-swift.enum/accessibilitydescription.md)
  A localized accessibility description describing the compass direction.
- [var description: String](./compassdirection-swift.enum/description.md)
  A localized string describing the compass direction.
### Enumeration Cases
- [Wind.CompassDirection.east](./compassdirection-swift.enum/east.md)
- [Wind.CompassDirection.eastNortheast](./compassdirection-swift.enum/eastnortheast.md)
- [Wind.CompassDirection.eastSoutheast](./compassdirection-swift.enum/eastsoutheast.md)
- [Wind.CompassDirection.north](./compassdirection-swift.enum/north.md)
- [Wind.CompassDirection.northNortheast](./compassdirection-swift.enum/northnortheast.md)
- [Wind.CompassDirection.northNorthwest](./compassdirection-swift.enum/northnorthwest.md)
- [Wind.CompassDirection.northeast](./compassdirection-swift.enum/northeast.md)
- [Wind.CompassDirection.northwest](./compassdirection-swift.enum/northwest.md)
- [Wind.CompassDirection.south](./compassdirection-swift.enum/south.md)
- [Wind.CompassDirection.southSoutheast](./compassdirection-swift.enum/southsoutheast.md)
- [Wind.CompassDirection.southSouthwest](./compassdirection-swift.enum/southsouthwest.md)
- [Wind.CompassDirection.southeast](./compassdirection-swift.enum/southeast.md)
- [Wind.CompassDirection.southwest](./compassdirection-swift.enum/southwest.md)
- [Wind.CompassDirection.west](./compassdirection-swift.enum/west.md)
- [Wind.CompassDirection.westNorthwest](./compassdirection-swift.enum/westnorthwest.md)
- [Wind.CompassDirection.westSouthwest](./compassdirection-swift.enum/westsouthwest.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the properties
- [var compassDirection: Wind.CompassDirection](./compassdirection-swift.property.md)
  The general indicator of wind direction.
- [var direction: Measurement<UnitAngle>](./direction.md)
  The direction the wind is coming from in degrees.
- [var gust: Measurement<UnitSpeed>?](./gust.md)
  A sudden increase in wind speed due to friction, wind shear, or by heating.
- [var speed: Measurement<UnitSpeed>](./speed.md)
  Sustained wind speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/wind/compassdirection-swift.enum)*