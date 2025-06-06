# distance(from:to:)

**Framework**: hvf  
**Kind**: method

Returns the distance between two indices.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func distance(from start: Self.Index, to end: Self.Index) -> Int
```

#### Return Value

The distance between `start` and `end`. The result can be negative only if the collection conforms to the `BidirectionalCollection` protocol.

#### Discussion

Unless the collection conforms to the `BidirectionalCollection` protocol, `start` must be less than or equal to `end`.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the resulting distance.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the resulting distance.

## Parameters

- `start`: A valid index of the collection.
- `end`: Another valid index of the collection. If   is equal to   , the result is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/axisvalues/distance(from:to:))*