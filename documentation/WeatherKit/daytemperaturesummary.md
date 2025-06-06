# DayTemperatureSummary

**Framework**: Weatherkit  
**Kind**: struct

A structure that describes the temperature summary for a day.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct DayTemperatureSummary
```

## Topics

### Operators
- [static func == (DayTemperatureSummary, DayTemperatureSummary) -> Bool](daytemperaturesummary/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](daytemperaturesummary/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var date: Date](daytemperaturesummary/date.md)
  The day of the observed temperature summary.
- [var highTemperature: Measurement<UnitTemperature>](daytemperaturesummary/hightemperature.md)
  The observed high temperature for the day.
- [var lowTemperature: Measurement<UnitTemperature>](daytemperaturesummary/lowtemperature.md)
  The observed low temperature for the day.
### Instance Methods
- [func encode(to: any Encoder) throws](daytemperaturesummary/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](daytemperaturesummary/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/daytemperaturesummary)*