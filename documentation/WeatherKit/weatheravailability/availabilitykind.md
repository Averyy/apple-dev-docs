# WeatherAvailability.AvailabilityKind

**Framework**: WeatherKit  
**Kind**: enum  
**Role**: Enumeration

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
- [WeatherAvailability.AvailabilityKind.available](./availabilitykind/available.md)
  The data is available.
- [WeatherAvailability.AvailabilityKind.temporarilyUnavailable](./availabilitykind/temporarilyunavailable.md)
  The data is supported for the location but is temporarily unavailable.
- [WeatherAvailability.AvailabilityKind.unknown](./availabilitykind/unknown.md)
  The availability is unknown.
- [WeatherAvailability.AvailabilityKind.unsupported](./availabilitykind/unsupported.md)
  The data isn’t supported for the location.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
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
- [var alertAvailability: WeatherAvailability.AvailabilityKind](./alertavailability.md)
  The weather alerts availability.
- [var minuteAvailability: WeatherAvailability.AvailabilityKind](./minuteavailability.md)
  The minute forecast availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatheravailability/availabilitykind)*