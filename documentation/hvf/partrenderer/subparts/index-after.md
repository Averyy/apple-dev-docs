# index(after:)

**Framework**: hvf  
**Kind**: method

Returns the position immediately after the given index.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func index(after: PartRenderer.Subparts.Index) -> PartRenderer.Subparts.Index
```

#### Return Value

The index value immediately after `i`.

#### Discussion

The successor of an index must be well defined. For an index `i` into a collection `c`, calling `c.index(after: i)` returns the same index every time.

## Parameters

- `i`: A valid index of the collection.   must be less than   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/subparts/index(after:))*