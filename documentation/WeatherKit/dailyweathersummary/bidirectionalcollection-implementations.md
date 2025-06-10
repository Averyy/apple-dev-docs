# BidirectionalCollection Implementations

**Framework**: WeatherKit

## Topics

### Instance Properties
- [var last: Self.Element?](dailyweathersummary/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](dailyweathersummary/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](dailyweathersummary/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func dropLast(Int) -> Self.SubSequence](dailyweathersummary/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstRange<C>(of: C) -> Range<Self.Index>?](dailyweathersummary/firstrange(of:)-234wv.md)
  Finds and returns the range of the first occurrence of a given collection within this collection.
- [func formIndex(before: inout Self.Index)](dailyweathersummary/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func joined(separator: String) -> String](dailyweathersummary/joined(separator:)-7uvyc.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](dailyweathersummary/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](dailyweathersummary/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](dailyweathersummary/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](dailyweathersummary/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](dailyweathersummary/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweathersummary/bidirectionalcollection-implementations)*