# MoonPhase

**Framework**: WeatherKit  
**Kind**: enum

An enumeration that specifies the moon phase kind.

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
enum MoonPhase
```

#### Overview

Waxing and waning provide information about direction. Crescent and gibbous describe shape.

## Topics

### Creating the object
- [init?(rawValue: String)](moonphase/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Getting the moon phase
- [MoonPhase.firstQuarter](moonphase/firstquarter.md)
  The disk is half lit.
- [MoonPhase.full](moonphase/full.md)
  The disk is fully lit where the moon is visible.
- [MoonPhase.lastQuarter](moonphase/lastquarter.md)
  The disk is half lit.
- [MoonPhase.new](moonphase/new.md)
  The disk is unlit where the moon is not visible.
- [MoonPhase.waningCrescent](moonphase/waningcrescent.md)
  The disk is partially lit as the moon is waning.
- [MoonPhase.waningGibbous](moonphase/waninggibbous.md)
  The disk is half lit as the moon is waning.
- [MoonPhase.waxingCrescent](moonphase/waxingcrescent.md)
  The disk is partially lit as the moon is waxing.
- [MoonPhase.waxingGibbous](moonphase/waxinggibbous.md)
  The disk is half lit as the moon is waxing.
### Describing the moon phase
- [var accessibilityDescription: String](moonphase/accessibilitydescription.md)
  A localized accessibility description describing the moon phase.
- [var description: String](moonphase/description.md)
  A localized string describing the moon phase.
- [var symbolName: String](moonphase/symbolname.md)
  The SF Symbol icon that represents the moon phase.
### Instance Properties
- [var rawValue: String](moonphase/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [MoonPhase.AllCases](moonphase/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [MoonPhase.RawValue](moonphase/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [MoonPhase]](moonphase/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](moonphase/equatable-implementations.md)
- [RawRepresentable Implementations](moonphase/rawrepresentable-implementations.md)

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

- [struct SunEvents](sunevents.md)
  An enumeration that represents dates of solar events, including sunrise, sunset, dawn, and dusk.
- [struct MoonEvents](moonevents.md)
  A structure that represents lunar events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/moonphase)*