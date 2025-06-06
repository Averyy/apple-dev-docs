# WeatherAvailability.AvailabilityKind

**Framework**: Weatherkit  
**Kind**: enum

The availability kind.

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
enum AvailabilityKind
```

## Topics

### Enumeration Cases
- [WeatherAvailability.AvailabilityKind.available](weatheravailability/availabilitykind/available.md)
  The data is available.
- [WeatherAvailability.AvailabilityKind.temporarilyUnavailable](weatheravailability/availabilitykind/temporarilyunavailable.md)
  The data is supported for the location but is temporarily unavailable.
- [WeatherAvailability.AvailabilityKind.unknown](weatheravailability/availabilitykind/unknown.md)
  The availability is unknown.
- [WeatherAvailability.AvailabilityKind.unsupported](weatheravailability/availabilitykind/unsupported.md)
  The data isn’t supported for the location.
### Initializers
- [init?(rawValue: String)](weatheravailability/availabilitykind/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](weatheravailability/availabilitykind/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [WeatherAvailability.AvailabilityKind.RawValue](weatheravailability/availabilitykind/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](weatheravailability/availabilitykind/equatable-implementations.md)
- [RawRepresentable Implementations](weatheravailability/availabilitykind/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var alertAvailability: WeatherAvailability.AvailabilityKind](weatheravailability/alertavailability.md)
  The weather alerts availability.
- [var minuteAvailability: WeatherAvailability.AvailabilityKind](weatheravailability/minuteavailability.md)
  The minute forecast availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatheravailability/availabilitykind)*