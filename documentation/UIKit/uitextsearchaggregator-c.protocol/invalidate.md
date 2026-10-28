# invalidate

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Invalidates all currently shown ranges.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) invalidate;
```

## Discussion

Calling this method causes the system find panel to update its current state, and might trigger a new search using [`performTextSearchWithQueryString:usingOptions:resultAggregator:`](../uitextsearching-53wjq/performtextsearchwithquerystring_usingoptions_resultaggregator_.md) immediately after.

## See Also

### Tracking search results
- [- foundRange:forSearchString:inDocument:](./foundrange_forsearchstring_indocument_.md)
  Adds a text range to the set of matches.
- [- invalidateFoundRange:inDocument:](./invalidatefoundrange_indocument_.md)
  Removes a text range from the set of matches.
- [- finishedSearching](./finishedsearching.md)
  Finishes the search for text ranges.
- [allFoundRanges](./allfoundranges.md)
  An ordered set of all the text ranges that match the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-c.protocol/invalidate)*