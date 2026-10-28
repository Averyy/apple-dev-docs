# compareOrderFromDocument:toDocument:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (NSComparisonResult) compareOrderFromDocument:(UITextSearchDocumentIdentifier) fromDocument toDocument:(UITextSearchDocumentIdentifier) toDocument;
```

## Return Value

Returns the result of comparing the two documents.

## Discussion

The system calls this method during a find session to determine which document’s ranges to highlight next when a user taps the “next” or “previous” button. Return [`ComparisonResult.orderedAscending`](../../Foundation/comparisonresult/orderedascending.md) if the text ranges found in the `fromDocument` come before those found in the `toDocument` in your view. Otherwise, return [`ComparisonResult.orderedDescending`](../../Foundation/comparisonresult/ordereddescending.md).

The system only calls this method if you provide document identifiers to the session’s result aggregator.

## Parameters

- `fromDocument`: A string that uniquely identifies the document to compare from.
- `toDocument`: A string that uniquely identifies the document to compare to.

## See Also

### Handling searches
- [- performTextSearchWithQueryString:usingOptions:resultAggregator:](./performtextsearchwithquerystring_usingoptions_resultaggregator_.md)
  Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [UITextSearchAggregator](../uitextsearchaggregator-c.protocol.md)
  The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [- compareFoundRange:toRange:inDocument:](./comparefoundrange_torange_indocument_.md)
  Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [UITextSearchDocumentIdentifier](../uitextsearchdocumentidentifier.md)
  A string that uniquely identifies a specific document when searching for matching text across multiple documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/compareorderfromdocument:todocument:)*