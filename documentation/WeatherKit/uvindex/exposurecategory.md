# UVIndex.ExposureCategory

**Framework**: WeatherKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that indicates risk of harm from unprotected sun exposure.

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
enum ExposureCategory
```

## Topics

### Enumeration Cases
- [UVIndex.ExposureCategory.extreme](./exposurecategory/extreme.md)
  The UV index is extreme.
- [UVIndex.ExposureCategory.high](./exposurecategory/high.md)
  The UV index is high.
- [UVIndex.ExposureCategory.low](./exposurecategory/low.md)
  The UV index is low.
- [UVIndex.ExposureCategory.moderate](./exposurecategory/moderate.md)
  The UV index is moderate.
- [UVIndex.ExposureCategory.veryHigh](./exposurecategory/veryhigh.md)
  The UV index is very high.
### Instance Properties
- [var accessibilityDescription: String](./exposurecategory/accessibilitydescription.md)
  A localized accessibility description describing the UV Index Exposure Category.
- [var description: String](./exposurecategory/description.md)
  A localized string describing the risk of harm from unprotected sun exposure.
- [var rangeValue: ClosedRange<Int>](./exposurecategory/rangevalue.md)
  The range of UV index values that falls into this category.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [CaseIterable](../../Swift/caseiterable.md)
- [Comparable](../../Swift/comparable.md)
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

### Getting the UV index
- [var category: UVIndex.ExposureCategory](./category.md)
  The UV Index exposure category.
- [var value: Int](./value.md)
  The UV Index value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/uvindex/exposurecategory)*