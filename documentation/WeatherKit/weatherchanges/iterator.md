# WeatherChanges.Iterator

**Framework**: WeatherKit  
**Kind**: typealias

A type that provides the collection’s iteration interface and encapsulates its iteration state.

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
typealias Iterator = IndexingIterator<WeatherChanges>
```

#### Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherchanges/iterator)*