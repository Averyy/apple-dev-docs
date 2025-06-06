# CloudCoverByAltitude

**Framework**: Weatherkit  
**Kind**: struct

Contains the percentage of sky covered by low, medium and high altitude cloud.

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
struct CloudCoverByAltitude
```

## Topics

### Instance Properties
- [var high: Double](cloudcoverbyaltitude/high.md)
  The percentage of the sky covered with high-altitude clouds. High-level Cloud Cover (HCC)corresponds to levels higher than 6300m above the model’s earth surface.
- [var low: Double](cloudcoverbyaltitude/low.md)
  The percentage of the sky covered with low-altitude clouds. Low-level Cloud Cover (LCC) corresponds to levels between 0m and 1800m above the model’s earth surface.
- [var medium: Double](cloudcoverbyaltitude/medium.md)
  The percentage of the sky covered with mid-altitude clouds. Medium-level Cloud Cover (MCC) corresponds to levels between 1800m and 6300m above the model’s earth surface.
### Default Implementations
- [Decodable Implementations](cloudcoverbyaltitude/decodable-implementations.md)
- [Encodable Implementations](cloudcoverbyaltitude/encodable-implementations.md)
- [Equatable Implementations](cloudcoverbyaltitude/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/cloudcoverbyaltitude)*