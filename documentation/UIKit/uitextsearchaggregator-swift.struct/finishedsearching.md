# finishedSearching()

**Framework**: UIKit  
**Kind**: method

Finishes the search for text ranges.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func finishedSearching()
```

#### Discussion

Call this method after searching all documents.

## See Also

- [func foundRange(UITextRange, searchString: String, document: DocumentIdentifier)](uitextsearchaggregator-swift.struct/foundrange(_:searchstring:document:).md)
  Adds a text range to the set of matches.
- [func invalidateFoundRange(UITextRange, document: DocumentIdentifier)](uitextsearchaggregator-swift.struct/invalidatefoundrange(_:document:).md)
  Removes a text range from the set of matches.
- [func invalidate()](uitextsearchaggregator-swift.struct/invalidate.md)
  Invalidates all currently shown ranges.
- [var allFoundRanges: [UITextRange]](uitextsearchaggregator-swift.struct/allfoundranges.md)
  An ordered set of all the text ranges that match the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/finishedsearching())*