# finishedSearching()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Finishes the search for text ranges.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
func finishedSearching()
```

#### Discussion

Call this method after searching all documents.

## See Also

### Tracking search results
- [func foundRange(UITextRange, searchString: String, document: DocumentIdentifier)](./foundrange%28_,searchstring,document%29.md)
  Adds a text range to the set of matches.
- [func invalidateFoundRange(UITextRange, document: DocumentIdentifier)](./invalidatefoundrange%28_,document%29.md)
  Removes a text range from the set of matches.
- [func invalidate()](./invalidate%28%29.md)
  Invalidates all currently shown ranges.
- [var allFoundRanges: [UITextRange]](./allfoundranges.md)
  An ordered set of all the text ranges that match the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/finishedsearching())*