# PartRenderer.Subparts

**Framework**: hvf  
**Kind**: struct

Collection of part parameters for the subparts of a part. The index is the subpart number (determined by the loader)

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
struct Subparts
```

## Topics

### Instance Properties
- [var endIndex: PartRenderer.Subparts.Index](partrenderer/subparts/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [let startIndex: Int](partrenderer/subparts/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func index(after: PartRenderer.Subparts.Index) -> PartRenderer.Subparts.Index](partrenderer/subparts/index(after:).md)
  Returns the position immediately after the given index.
### Subscripts
- [subscript(Int) -> PartRenderer.PartParameters](partrenderer/subparts/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [PartRenderer.Subparts.Element](partrenderer/subparts/element.md)
  A type representing the sequence’s elements.
- [PartRenderer.Subparts.Index](partrenderer/subparts/index.md)
  A type that represents a position in the collection.
- [PartRenderer.Subparts.Indices](partrenderer/subparts/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [PartRenderer.Subparts.Iterator](partrenderer/subparts/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [PartRenderer.Subparts.SubSequence](partrenderer/subparts/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](partrenderer/subparts/bidirectionalcollection-implementations.md)
- [Collection Implementations](partrenderer/subparts/collection-implementations.md)
- [RandomAccessCollection Implementations](partrenderer/subparts/randomaccesscollection-implementations.md)
- [Sequence Implementations](partrenderer/subparts/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/subparts)*