# UVIndex.ExposureCategory

**Framework**: Weatherkit  
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

### Operators
- [static func < (UVIndex.ExposureCategory, UVIndex.ExposureCategory) -> Bool](uvindex/exposurecategory/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
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
### Initializers
- [init?(rawValue: String)](uvindex/exposurecategory/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var accessibilityDescription: String](uvindex/exposurecategory/accessibilitydescription.md)
  A localized accessibility description describing the UV Index Exposure Category.
- [var description: String](uvindex/exposurecategory/description.md)
  A localized string describing the risk of harm from unprotected sun exposure.
- [var rangeValue: ClosedRange<Int>](uvindex/exposurecategory/rangevalue.md)
  The range of UV index values that falls into this category.
- [var rawValue: String](uvindex/exposurecategory/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [UVIndex.ExposureCategory.AllCases](uvindex/exposurecategory/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [UVIndex.ExposureCategory.RawValue](uvindex/exposurecategory/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [UVIndex.ExposureCategory]](uvindex/exposurecategory/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Comparable Implementations](uvindex/exposurecategory/comparable-implementations.md)
- [Equatable Implementations](uvindex/exposurecategory/equatable-implementations.md)
- [RawRepresentable Implementations](uvindex/exposurecategory/rawrepresentable-implementations.md)

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

## See Also

- [var category: UVIndex.ExposureCategory](uvindex/category.md)
  The UV Index exposure category.
- [var value: Int](uvindex/value.md)
  The UV Index value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/uvindex/exposurecategory)*