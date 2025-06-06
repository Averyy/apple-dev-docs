# Collection Implementations

**Framework**: Weatherkit

## Topics

### Instance Properties
- [var count: Int](dailyweathersummary/count.md)
  The number of elements in the collection.
- [var first: Self.Element?](dailyweathersummary/first.md)
  The first element of the collection.
- [var isEmpty: Bool](dailyweathersummary/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var underestimatedCount: Int](dailyweathersummary/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dailyweathersummary/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](dailyweathersummary/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](dailyweathersummary/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](dailyweathersummary/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func firstRange<C>(of: C) -> Range<Self.Index>?](dailyweathersummary/firstrange(of:)-9t55z.md)
  Finds and returns the range of the first occurrence of a given collection within this collection.
- [func formIndex(inout Self.Index, offsetBy: Int)](dailyweathersummary/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](dailyweathersummary/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](dailyweathersummary/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(of: Self.Element) -> Self.Index?](dailyweathersummary/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](dailyweathersummary/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](dailyweathersummary/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](dailyweathersummary/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](dailyweathersummary/map(_:)-4p0g9.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](dailyweathersummary/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](dailyweathersummary/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](dailyweathersummary/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dailyweathersummary/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](dailyweathersummary/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](dailyweathersummary/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func ranges<C>(of: C) -> [Range<Self.Index>]](dailyweathersummary/ranges(of:).md)
  Finds and returns the ranges of the all occurrences of a given sequence within the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](dailyweathersummary/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](dailyweathersummary/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](dailyweathersummary/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](dailyweathersummary/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func trimmingPrefix<Prefix>(Prefix) -> Self.SubSequence](dailyweathersummary/trimmingprefix(_:).md)
  Returns a new collection of the same type by removing `prefix` from the start of the collection.
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dailyweathersummary/trimmingprefix(while:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweathersummary/collection-implementations)*