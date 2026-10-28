# UITextSearchDocumentIdentifier

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A string that uniquely identifies a specific document when searching for matching text across multiple documents.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```c
typedef id<NSCopying,NSObject> UITextSearchDocumentIdentifier;
```

## Discussion

The [`UITextSearching`](./uitextsearching-53wjq.md) and [`UITextSearchAggregator`](./uitextsearchaggregator-swift.struct.md) protocols use this type to distinguish matches in a specific document from text in other documents with the same range.

## See Also

### Handling searches
- [- performTextSearchWithQueryString:usingOptions:resultAggregator:](./uitextsearching-53wjq/performtextsearchwithquerystring_usingoptions_resultaggregator_.md)
  Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [UITextSearchAggregator](./uitextsearchaggregator-c.protocol.md)
  The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [- compareFoundRange:toRange:inDocument:](./uitextsearching-53wjq/comparefoundrange_torange_indocument_.md)
  Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [- compareOrderFromDocument:toDocument:](./uitextsearching-53wjq/compareorderfromdocument_todocument_.md)
  Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchdocumentidentifier)*