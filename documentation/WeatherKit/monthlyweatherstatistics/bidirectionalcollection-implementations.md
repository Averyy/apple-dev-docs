# BidirectionalCollection Implementations

**Framework**: WeatherKit

## Topics

### Instance Properties
- [var last: Self.Element?](monthlyweatherstatistics/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](monthlyweatherstatistics/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](monthlyweatherstatistics/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func dropLast(Int) -> Self.SubSequence](monthlyweatherstatistics/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstRange<C>(of: C) -> Range<Self.Index>?](monthlyweatherstatistics/firstrange(of:)-9t3on.md)
  Finds and returns the range of the first occurrence of a given collection within this collection.
- [func formIndex(before: inout Self.Index)](monthlyweatherstatistics/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func joined(separator: String) -> String](monthlyweatherstatistics/joined(separator:)-k48p.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](monthlyweatherstatistics/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](monthlyweatherstatistics/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](monthlyweatherstatistics/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](monthlyweatherstatistics/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](monthlyweatherstatistics/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/monthlyweatherstatistics/bidirectionalcollection-implementations)*