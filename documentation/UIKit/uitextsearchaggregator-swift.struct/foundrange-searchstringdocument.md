# foundRange(_:searchString:document:)

**Framework**: UIKit  
**Kind**: method

Adds a text range to the set of matches.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func foundRange(_ range: UITextRange, searchString: String, document: DocumentIdentifier)
```

#### Discussion

Call this method to add a text range found in your document to the set of matches.

## Parameters

- `range`: The text range to add to the set of matches.
- `searchString`: The query string the search used to locate this range of text.
- `document`: A string that uniquely identifies the document containing the text range.   when searching a single document.

## See Also

- [func invalidateFoundRange(UITextRange, document: DocumentIdentifier)](uitextsearchaggregator-swift.struct/invalidatefoundrange(_:document:).md)
  Removes a text range from the set of matches.
- [func invalidate()](uitextsearchaggregator-swift.struct/invalidate.md)
  Invalidates all currently shown ranges.
- [func finishedSearching()](uitextsearchaggregator-swift.struct/finishedsearching.md)
  Finishes the search for text ranges.
- [var allFoundRanges: [UITextRange]](uitextsearchaggregator-swift.struct/allfoundranges.md)
  An ordered set of all the text ranges that match the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/foundrange(_:searchstring:document:))*