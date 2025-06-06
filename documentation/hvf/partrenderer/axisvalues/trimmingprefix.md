# trimmingPrefix(_:)

**Framework**: hvf  
**Kind**: method

Returns a new collection of the same type by removing `prefix` from the start of the collection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func trimmingPrefix<Prefix>(_ prefix: Prefix) -> Self.SubSequence where Prefix : Sequence, Self.Element == Prefix.Element
```

#### Return Value

A collection containing the elements of the collection that are not removed by `prefix`.

## Parameters

- `prefix`: The collection to remove from this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/axisvalues/trimmingprefix(_:))*