# AsyncSequence Implementations

**Framework**: Wi-Fi Aware

## Topics

### Instance Methods
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](wapaireddevice/devicessequence/allsatisfy(_:).md)
  Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](wapaireddevice/devicessequence/compactmap(_:)-2zq8u.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](wapaireddevice/devicessequence/compactmap(_:)-4buj4.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [func contains(Self.Element) async rethrows -> Bool](wapaireddevice/devicessequence/contains(_:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](wapaireddevice/devicessequence/contains(where:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](wapaireddevice/devicessequence/drop(while:).md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](wapaireddevice/devicessequence/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](wapaireddevice/devicessequence/filter(_:).md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](wapaireddevice/devicessequence/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](wapaireddevice/devicessequence/flatmap(_:)-6z27p.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult>](wapaireddevice/devicessequence/flatmap(_:)-7b44u.md)
  Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](wapaireddevice/devicessequence/flatmap(_:)-7pr29.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](wapaireddevice/devicessequence/flatmap(_:)-o1y1.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](wapaireddevice/devicessequence/map(_:)-1jqj0.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](wapaireddevice/devicessequence/map(_:)-4nzpv.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](wapaireddevice/devicessequence/max(by:).md)
  Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func min(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](wapaireddevice/devicessequence/min(by:).md)
  Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func prefix(Int) -> AsyncPrefixSequence<Self>](wapaireddevice/devicessequence/prefix(_:).md)
  Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](wapaireddevice/devicessequence/prefix(while:).md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](wapaireddevice/devicessequence/reduce(_:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](wapaireddevice/devicessequence/reduce(into:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/devicessequence/asyncsequence-implementations)*