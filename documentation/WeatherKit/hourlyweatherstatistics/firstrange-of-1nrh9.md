# firstRange(of:)

**Framework**: WeatherKit  
**Kind**: method

Finds and returns the range of the first occurrence of a given collection within this collection.

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
func firstRange<C>(of other: C) -> Range<Self.Index>? where C : Collection, Self.Element == C.Element
```

#### Return Value

A range in the collection of the first occurrence of `sequence`. Returns nil if `sequence` is not found.

## Parameters

- `other`: The collection to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/hourlyweatherstatistics/firstrange(of:)-1nrh9)*