# Wind.CompassDirection

**Framework**: WeatherKit  
**Kind**: enum

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

#### Overview

This enumeration represents true headings.

## Topics

### Creating the object
- [init?(rawValue: String)](wind/compassdirection-swift.enum/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Describing the compass direction
- [var abbreviation: String](wind/compassdirection-swift.enum/abbreviation.md)
  A localized short abbreviation of the wind compass direction.
- [var accessibilityDescription: String](wind/compassdirection-swift.enum/accessibilitydescription.md)
  A localized accessibility description describing the compass direction.
- [var description: String](wind/compassdirection-swift.enum/description.md)
  A localized string describing the compass direction.
### Enumeration Cases
- [Wind.CompassDirection.east](wind/compassdirection-swift.enum/east.md)
- [Wind.CompassDirection.eastNortheast](wind/compassdirection-swift.enum/eastnortheast.md)
- [Wind.CompassDirection.eastSoutheast](wind/compassdirection-swift.enum/eastsoutheast.md)
- [Wind.CompassDirection.north](wind/compassdirection-swift.enum/north.md)
- [Wind.CompassDirection.northNortheast](wind/compassdirection-swift.enum/northnortheast.md)
- [Wind.CompassDirection.northNorthwest](wind/compassdirection-swift.enum/northnorthwest.md)
- [Wind.CompassDirection.northeast](wind/compassdirection-swift.enum/northeast.md)
- [Wind.CompassDirection.northwest](wind/compassdirection-swift.enum/northwest.md)
- [Wind.CompassDirection.south](wind/compassdirection-swift.enum/south.md)
- [Wind.CompassDirection.southSoutheast](wind/compassdirection-swift.enum/southsoutheast.md)
- [Wind.CompassDirection.southSouthwest](wind/compassdirection-swift.enum/southsouthwest.md)
- [Wind.CompassDirection.southeast](wind/compassdirection-swift.enum/southeast.md)
- [Wind.CompassDirection.southwest](wind/compassdirection-swift.enum/southwest.md)
- [Wind.CompassDirection.west](wind/compassdirection-swift.enum/west.md)
- [Wind.CompassDirection.westNorthwest](wind/compassdirection-swift.enum/westnorthwest.md)
- [Wind.CompassDirection.westSouthwest](wind/compassdirection-swift.enum/westsouthwest.md)
### Instance Properties
- [var rawValue: String](wind/compassdirection-swift.enum/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [Wind.CompassDirection.AllCases](wind/compassdirection-swift.enum/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [Wind.CompassDirection.RawValue](wind/compassdirection-swift.enum/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [Wind.CompassDirection]](wind/compassdirection-swift.enum/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](wind/compassdirection-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](wind/compassdirection-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var compassDirection: Wind.CompassDirection](wind/compassdirection-swift.property.md)
  The general indicator of wind direction.
- [var direction: Measurement<UnitAngle>](wind/direction.md)
  The direction the wind is coming from in degrees.
- [var gust: Measurement<UnitSpeed>?](wind/gust.md)
  A sudden increase in wind speed due to friction, wind shear, or by heating.
- [var speed: Measurement<UnitSpeed>](wind/speed.md)
  Sustained wind speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/wind/compassdirection-swift.enum)*