# Sequence Implementations

**Framework**: WeatherKit

## Topics

### Instance Properties
- [var lazy: LazySequence<Self>](dailyweathersummary/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](dailyweathersummary/publisher.md)
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](dailyweathersummary/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dailyweathersummary/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](dailyweathersummary/compare(_:_:).md)
  If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s
- [func contains(Self.Element) -> Bool](dailyweathersummary/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](dailyweathersummary/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](dailyweathersummary/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](dailyweathersummary/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](dailyweathersummary/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](dailyweathersummary/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](dailyweathersummary/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](dailyweathersummary/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](dailyweathersummary/flatmap(_:)-34dpm.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dailyweathersummary/flatmap(_:)-7fv2p.md)
- [func forEach((Self.Element) throws -> Void) rethrows](dailyweathersummary/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func formatted() -> String](dailyweathersummary/formatted.md)
- [func formatted<S>(S) -> S.FormatOutput](dailyweathersummary/formatted(_:).md)
- [func joined() -> FlattenSequence<Self>](dailyweathersummary/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](dailyweathersummary/joined(separator:)-3x4ok.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func joined(separator: String) -> String](dailyweathersummary/joined(separator:)-7ehx.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](dailyweathersummary/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](dailyweathersummary/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](dailyweathersummary/map(_:)-91m9m.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func max() -> Self.Element?](dailyweathersummary/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](dailyweathersummary/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](dailyweathersummary/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](dailyweathersummary/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](dailyweathersummary/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](dailyweathersummary/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func shuffled() -> [Self.Element]](dailyweathersummary/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](dailyweathersummary/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted() -> [Self.Element]](dailyweathersummary/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](dailyweathersummary/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](dailyweathersummary/sorted(using:)-38sia.md)
  Returns the elements of the sequence, sorted using the given array of `SortComparator`s to compare elements.
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](dailyweathersummary/sorted(using:)-6i4ol.md)
  Returns the elements of the sequence, sorted using the given comparator to compare elements.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](dailyweathersummary/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](dailyweathersummary/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](dailyweathersummary/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweathersummary/sequence-implementations)*