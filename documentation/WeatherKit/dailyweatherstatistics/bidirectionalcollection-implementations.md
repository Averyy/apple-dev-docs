# BidirectionalCollection Implementations

**Framework**: WeatherKit

## Topics

### Instance Properties
- [var last: Self.Element?](dailyweatherstatistics/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](dailyweatherstatistics/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](dailyweatherstatistics/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func dropLast(Int) -> Self.SubSequence](dailyweatherstatistics/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstRange<C>(of: C) -> Range<Self.Index>?](dailyweatherstatistics/firstrange(of:)-1x8lz.md)
  Finds and returns the range of the first occurrence of a given collection within this collection.
- [func formIndex(before: inout Self.Index)](dailyweatherstatistics/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func joined(separator: String) -> String](dailyweatherstatistics/joined(separator:)-60fmk.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](dailyweatherstatistics/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](dailyweatherstatistics/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](dailyweatherstatistics/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](dailyweatherstatistics/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](dailyweatherstatistics/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweatherstatistics/bidirectionalcollection-implementations)*