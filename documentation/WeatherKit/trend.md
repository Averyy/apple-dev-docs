# Trend

**Framework**: Weatherkit  
**Kind**: struct

A structure describing an observed pattern in the data for weather at a location for a specific condition.

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
struct Trend<Dimension> where Dimension : Dimension
```

## Topics

### Operators
- [static func == (Trend<Dimension>, Trend<Dimension>) -> Bool](trend/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](trend/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var baseline: TrendBaseline<Dimension>](trend/baseline.md)
  The manner in which the comparison between the baseline and current values are compared.
- [var currentValue: Measurement<Dimension>](trend/currentvalue.md)
  The current recorded value for the condition in which the trend is compared against.
- [var deviation: Deviation](trend/deviation.md)
  Semantically describes the manner in which the observed trend compares the current value against the baseline value.
### Instance Methods
- [func encode(to: any Encoder) throws](trend/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](trend/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/trend)*