# invalidate()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Invalidates all currently shown ranges.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
func invalidate()
```

## Discussion

Calling this method causes the system find panel to update its current state, and might trigger a new search using [`performTextSearch(queryString:options:resultAggregator:)`](../uitextsearching-3wkjv/performtextsearch%28querystring,options,resultaggregator%29.md) (Swift) or [`performTextSearchWithQueryString:usingOptions:resultAggregator:`](../uitextsearching-53wjq/performtextsearchwithquerystring_usingoptions_resultaggregator_.md) (Objective-C) immediately after.

## See Also

### Tracking search results
- [func foundRange(UITextRange, searchString: String, document: DocumentIdentifier)](./foundrange%28_,searchstring,document%29.md)
  Adds a text range to the set of matches.
- [func invalidateFoundRange(UITextRange, document: DocumentIdentifier)](./invalidatefoundrange%28_,document%29.md)
  Removes a text range from the set of matches.
- [func finishedSearching()](./finishedsearching%28%29.md)
  Finishes the search for text ranges.
- [var allFoundRanges: [UITextRange]](./allfoundranges.md)
  An ordered set of all the text ranges that match the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/invalidate())*