# Sequence Implementations

**Framework**: WeatherKit

## Topics

### Instance Properties
- [var lazy: LazySequence<Self>](forecast/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](forecast/publisher.md)
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](forecast/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](forecast/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](forecast/compare(_:_:).md)
  If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s
- [func contains(Self.Element) -> Bool](forecast/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](forecast/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](forecast/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](forecast/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](forecast/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](forecast/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](forecast/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](forecast/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](forecast/flatmap(_:)-8di7o.md)
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](forecast/flatmap(_:)-9oyxq.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func forEach((Self.Element) throws -> Void) rethrows](forecast/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func formatted() -> String](forecast/formatted.md)
- [func formatted<S>(S) -> S.FormatOutput](forecast/formatted(_:).md)
- [func joined() -> FlattenSequence<Self>](forecast/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](forecast/joined(separator:)-3pmb0.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func joined(separator: String) -> String](forecast/joined(separator:)-59nrx.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](forecast/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](forecast/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](forecast/map(_:)-8cehe.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func max() -> Self.Element?](forecast/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](forecast/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](forecast/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](forecast/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](forecast/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](forecast/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func shuffled() -> [Self.Element]](forecast/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](forecast/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted() -> [Self.Element]](forecast/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](forecast/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](forecast/sorted(using:)-286yx.md)
  Returns the elements of the sequence, sorted using the given array of `SortComparator`s to compare elements.
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](forecast/sorted(using:)-5aia3.md)
  Returns the elements of the sequence, sorted using the given comparator to compare elements.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](forecast/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](forecast/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](forecast/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/forecast/sequence-implementations)*