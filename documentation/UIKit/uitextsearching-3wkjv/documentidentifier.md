# DocumentIdentifier

**Framework**: UIKit  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

An object that uniquely identifies a specific document when searching for matching text across multiple documents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
associatedtype DocumentIdentifier : Hashable = AnyHashable?
```

## Discussion

The [`UITextSearching`](../uitextsearching-53wjq.md) and [`UITextSearchAggregator`](../uitextsearchaggregator-swift.struct.md) protocols use this type to distinguish matches in a specific document from text in other documents with the same range.

## See Also

### Handling searches
- [func performTextSearch(queryString: String, options: UITextSearchOptions, resultAggregator: UITextSearchAggregator<Self.DocumentIdentifier>)](./performtextsearch%28querystring,options,resultaggregator%29.md)
  Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [struct UITextSearchAggregator](../uitextsearchaggregator-swift.struct.md)
  The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [func compare(UITextRange, toRange: UITextRange, document: Self.DocumentIdentifier?) -> ComparisonResult](./compare%28_,torange,document%29.md)
  Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [func compare(document: Self.DocumentIdentifier, toDocument: Self.DocumentIdentifier) -> ComparisonResult](./compare%28document,todocument%29.md)
  Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/documentidentifier)*