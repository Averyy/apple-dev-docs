# PartRenderer.AxisValues

**Framework**: hvf  
**Kind**: class

All the axis values applied to a part. The index is the axis number (determined by the loader). Axis values are in design space (-1.0…1.0)

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
class AxisValues
```

## Topics

### Instance Properties
- [var endIndex: PartRenderer.AxisValues.Index](partrenderer/axisvalues/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var isNested: Bool](partrenderer/axisvalues/isnested.md)
  Whether the axis values apply to a nested subpart or not
- [let startIndex: Int](partrenderer/axisvalues/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func blendedValue(axis: Int) -> Double](partrenderer/axisvalues/blendedvalue(axis:).md)
  The final axis values applied to this subpart after the part has been rendered This is useful for detecting axes going out of range (-1.0…1.0)
- [func index(after: PartRenderer.AxisValues.Index) -> PartRenderer.AxisValues.Index](partrenderer/axisvalues/index(after:).md)
  Returns the position immediately after the given index.
### Subscripts
- [subscript(Int) -> Double](partrenderer/axisvalues/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [PartRenderer.AxisValues.Element](partrenderer/axisvalues/element.md)
  A type representing the sequence’s elements.
- [PartRenderer.AxisValues.Index](partrenderer/axisvalues/index.md)
  A type that represents a position in the collection.
- [PartRenderer.AxisValues.Indices](partrenderer/axisvalues/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [PartRenderer.AxisValues.Iterator](partrenderer/axisvalues/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [PartRenderer.AxisValues.SubSequence](partrenderer/axisvalues/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](partrenderer/axisvalues/collection-implementations.md)
- [MutableCollection Implementations](partrenderer/axisvalues/mutablecollection-implementations.md)
- [Sequence Implementations](partrenderer/axisvalues/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/axisvalues)*