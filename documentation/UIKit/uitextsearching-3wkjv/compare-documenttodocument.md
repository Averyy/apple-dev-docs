# compare(document:toDocument:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func compare(document: Self.DocumentIdentifier, toDocument: Self.DocumentIdentifier) -> ComparisonResult
```

#### Return Value

Returns the result of comparing the two documents.

#### Discussion

The system calls this method during a find session to determine which document’s ranges to highlight next when a user taps the “next” or “previous” button. Return [`ComparisonResult.orderedAscending`](https://developer.apple.com/documentation/Foundation/ComparisonResult/orderedAscending) if the text ranges found in the `fromDocument` come before those found in the `toDocument` in your view. Otherwise, return [`ComparisonResult.orderedDescending`](https://developer.apple.com/documentation/Foundation/ComparisonResult/orderedDescending).

The system only calls this method if you provide document identifiers to the session’s result aggregator.

## Parameters

- `document`: A string that uniquely identifies the document to compare from.
- `toDocument`: A string that uniquely identifies the document to compare to.

## See Also

- [func performTextSearch(queryString: String, options: UITextSearchOptions, resultAggregator: UITextSearchAggregator<Self.DocumentIdentifier>)](uitextsearching-3wkjv/performtextsearch(querystring:options:resultaggregator:).md)
  Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [struct UITextSearchAggregator](uitextsearchaggregator-swift.struct.md)
  The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [func compare(UITextRange, toRange: UITextRange, document: Self.DocumentIdentifier?) -> ComparisonResult](uitextsearching-3wkjv/compare(_:torange:document:).md)
  Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [associatedtype DocumentIdentifier : Hashable = AnyHashable?](uitextsearching-3wkjv/documentidentifier.md)
  An object that uniquely identifies a specific document when searching for matching text across multiple documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/compare(document:todocument:))*