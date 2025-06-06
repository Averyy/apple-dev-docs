# invalidate()

**Framework**: UIKit  
**Kind**: method

Invalidates all currently shown ranges.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func invalidate()
```

#### Discussion

Calling this method causes the system find panel to update its current state, and might trigger a new search using [`performTextSearch(queryString:options:resultAggregator:)`](uitextsearching-3wkjv/performtextsearch(querystring:options:resultaggregator:).md) (Swift) or [`performTextSearchWithQueryString:usingOptions:resultAggregator:`](uitextsearching-53wjq/performtextsearchwithquerystring:usingoptions:resultaggregator:.md) (Objective-C) immediately after.

## See Also

- [func foundRange(UITextRange, searchString: String, document: DocumentIdentifier)](uitextsearchaggregator-swift.struct/foundrange(_:searchstring:document:).md)
  Adds a text range to the set of matches.
- [func invalidateFoundRange(UITextRange, document: DocumentIdentifier)](uitextsearchaggregator-swift.struct/invalidatefoundrange(_:document:).md)
  Removes a text range from the set of matches.
- [func finishedSearching()](uitextsearchaggregator-swift.struct/finishedsearching.md)
  Finishes the search for text ranges.
- [var allFoundRanges: [UITextRange]](uitextsearchaggregator-swift.struct/allfoundranges.md)
  An ordered set of all the text ranges that match the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/invalidate())*