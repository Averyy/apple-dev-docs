# UITextSearchAggregator

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The methods you use on a find session’s aggregator to collect matching text ranges for a search.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
@protocol UITextSearchAggregator <NSObject>
```

#### Overview

To track text ranges that match the search, call these methods on the aggregator for the searchable object implementing the [`UITextSearching`](./uitextsearching-53wjq.md) protocol for a [`UITextSearchingFindSession`](./uitextsearchingfindsession.md).

## Topics

### Tracking search results
- [- foundRange:forSearchString:inDocument:](./uitextsearchaggregator-c.protocol/foundrange_forsearchstring_indocument_.md)
  Adds a text range to the set of matches.
- [- invalidateFoundRange:inDocument:](./uitextsearchaggregator-c.protocol/invalidatefoundrange_indocument_.md)
  Removes a text range from the set of matches.
- [- invalidate](./uitextsearchaggregator-c.protocol/invalidate.md)
  Invalidates all currently shown ranges.
- [- finishedSearching](./uitextsearchaggregator-c.protocol/finishedsearching.md)
  Finishes the search for text ranges.
- [allFoundRanges](./uitextsearchaggregator-c.protocol/allfoundranges.md)
  An ordered set of all the text ranges that match the search.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling searches
- [- performTextSearchWithQueryString:usingOptions:resultAggregator:](./uitextsearching-53wjq/performtextsearchwithquerystring_usingoptions_resultaggregator_.md)
  Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [- compareFoundRange:toRange:inDocument:](./uitextsearching-53wjq/comparefoundrange_torange_indocument_.md)
  Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [- compareOrderFromDocument:toDocument:](./uitextsearching-53wjq/compareorderfromdocument_todocument_.md)
  Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
- [UITextSearchDocumentIdentifier](./uitextsearchdocumentidentifier.md)
  A string that uniquely identifies a specific document when searching for matching text across multiple documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-c.protocol)*