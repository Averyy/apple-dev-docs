# UVIndex

**Framework**: Weatherkit  
**Kind**: struct

The expected intensity of ultraviolet radiation from the sun.

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
struct UVIndex
```

## Topics

### Getting the UV index
- [var category: UVIndex.ExposureCategory](uvindex/category.md)
  The UV Index exposure category.
- [var value: Int](uvindex/value.md)
  The UV Index value.
- [UVIndex.ExposureCategory](uvindex/exposurecategory.md)
  An enumeration that indicates risk of harm from unprotected sun exposure.
### Default Implementations
- [Decodable Implementations](uvindex/decodable-implementations.md)
- [Encodable Implementations](uvindex/encodable-implementations.md)
- [Equatable Implementations](uvindex/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [enum Precipitation](precipitation.md)
  The form of precipitation.
- [enum PressureTrend](pressuretrend.md)
  The atmospheric pressure change over time.
- [struct Wind](wind.md)
  Contains wind data of speed, direction, and gust.
- [enum WeatherCondition](weathercondition.md)
  A description of the current weather condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/uvindex)*