# UVIndex.ExposureCategory

**Framework**: WeatherKit  
**Kind**: enum

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
- [UVIndex.ExposureCategory.extreme](uvindex/exposurecategory/extreme.md)
  The UV index is extreme.
- [UVIndex.ExposureCategory.high](uvindex/exposurecategory/high.md)
  The UV index is high.
- [UVIndex.ExposureCategory.low](uvindex/exposurecategory/low.md)
  The UV index is low.
- [UVIndex.ExposureCategory.moderate](uvindex/exposurecategory/moderate.md)
  The UV index is moderate.
- [UVIndex.ExposureCategory.veryHigh](uvindex/exposurecategory/veryhigh.md)
  The UV index is very high.
### Instance Properties
- [var accessibilityDescription: String](uvindex/exposurecategory/accessibilitydescription.md)
  A localized accessibility description describing the UV Index Exposure Category.
- [var description: String](uvindex/exposurecategory/description.md)
  A localized string describing the risk of harm from unprotected sun exposure.
- [var rangeValue: ClosedRange<Int>](uvindex/exposurecategory/rangevalue.md)
  The range of UV index values that falls into this category.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Comparable](../Swift/Comparable.md)
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

- [var category: UVIndex.ExposureCategory](uvindex/category.md)
  The UV Index exposure category.
- [var value: Int](uvindex/value.md)
  The UV Index value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/uvindex/exposurecategory)*