# UITextSearchAggregator

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The methods you use on a find session’s aggregator to collect matching text ranges for a search.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
struct UITextSearchAggregator<DocumentIdentifier> where DocumentIdentifier : Hashable
```

#### Overview

To track text ranges that match the search, call these methods on the aggregator for the searchable object implementing the [`UITextSearching`](./uitextsearching-53wjq.md) protocol for a [`UITextSearchingFindSession`](./uitextsearchingfindsession.md).

## Topics

### Tracking search results
- [func foundRange(UITextRange, searchString: String, document: DocumentIdentifier)](./uitextsearchaggregator-swift.struct/foundrange%28_,searchstring,document%29.md)
  Adds a text range to the set of matches.
- [func invalidateFoundRange(UITextRange, document: DocumentIdentifier)](./uitextsearchaggregator-swift.struct/invalidatefoundrange%28_,document%29.md)
  Removes a text range from the set of matches.
- [func invalidate()](./uitextsearchaggregator-swift.struct/invalidate%28%29.md)
  Invalidates all currently shown ranges.
- [func finishedSearching()](./uitextsearchaggregator-swift.struct/finishedsearching%28%29.md)
  Finishes the search for text ranges.
- [var allFoundRanges: [UITextRange]](./uitextsearchaggregator-swift.struct/allfoundranges.md)
  An ordered set of all the text ranges that match the search.

## See Also

### Handling searches
- [func performTextSearch(queryString: String, options: UITextSearchOptions, resultAggregator: UITextSearchAggregator<Self.DocumentIdentifier>)](./uitextsearching-3wkjv/performtextsearch%28querystring,options,resultaggregator%29.md)
  Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [func compare(UITextRange, toRange: UITextRange, document: Self.DocumentIdentifier?) -> ComparisonResult](./uitextsearching-3wkjv/compare%28_,torange,document%29.md)
  Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [func compare(document: Self.DocumentIdentifier, toDocument: Self.DocumentIdentifier) -> ComparisonResult](./uitextsearching-3wkjv/compare%28document,todocument%29.md)
  Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
- [associatedtype DocumentIdentifier : Hashable = AnyHashable?](./uitextsearching-3wkjv/documentidentifier.md)
  An object that uniquely identifies a specific document when searching for matching text across multiple documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct)*