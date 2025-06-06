# swapAt(_:_:)

**Framework**: hvf  
**Kind**: method

Exchanges the values at the specified indices of the collection.

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
mutating func swapAt(_ i: Self.Index, _ j: Self.Index)
```

#### Discussion

Both parameters must be valid indices of the collection that are not equal to `endIndex`. Calling `swapAt(_:_:)` with the same index as both `i` and `j` has no effect.

> **Note**: O(1)

O(1)

## Parameters

- `i`: The index of the first value to swap.
- `j`: The index of the second value to swap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/axisvalues/swapat(_:_:))*