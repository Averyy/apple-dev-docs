# performTextSearch(queryString:options:resultAggregator:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func performTextSearch(queryString: String, options: UITextSearchOptions, resultAggregator: UITextSearchAggregator<Self.DocumentIdentifier>)
```

#### Discussion

The system calls this method during a find session to perform the search. Your implenentation should search for matching text ranges in your app’s documents and call [`foundRange(_:searchString:document:)`](uitextsearchaggregator-swift.struct/foundrange(_:searchstring:document:).md) on the aggregator object to add them to the set of matching ranges.

## Parameters

- `queryString`: The string to search for.
- `options`: The configurable options to use for matching words and comparing strings.
- `resultAggregator`: An object you use to collect matching results. The aggregator is thread-safe, so you may send it messages on other threads.

## See Also

- [struct UITextSearchAggregator](uitextsearchaggregator-swift.struct.md)
  The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [func compare(UITextRange, toRange: UITextRange, document: Self.DocumentIdentifier?) -> ComparisonResult](uitextsearching-3wkjv/compare(_:torange:document:).md)
  Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [func compare(document: Self.DocumentIdentifier, toDocument: Self.DocumentIdentifier) -> ComparisonResult](uitextsearching-3wkjv/compare(document:todocument:).md)
  Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
- [associatedtype DocumentIdentifier : Hashable = AnyHashable?](uitextsearching-3wkjv/documentidentifier.md)
  An object that uniquely identifies a specific document when searching for matching text across multiple documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/performtextsearch(querystring:options:resultaggregator:))*