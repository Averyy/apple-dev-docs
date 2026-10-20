# foundRange(_:searchString:document:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds a text range to the set of matches.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
func foundRange(_ range: UITextRange, searchString: String, document: DocumentIdentifier)
```

#### Discussion

Call this method to add a text range found in your document to the set of matches.

## Parameters

- `range`: The text range to add to the set of matches.
- `searchString`: The query string the search used to locate this range of text.
- `document`: A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## See Also

### Tracking search results
- [func invalidateFoundRange(UITextRange, document: DocumentIdentifier)](./invalidatefoundrange%28_,document%29.md)
  Removes a text range from the set of matches.
- [func invalidate()](./invalidate%28%29.md)
  Invalidates all currently shown ranges.
- [func finishedSearching()](./finishedsearching%28%29.md)
  Finishes the search for text ranges.
- [var allFoundRanges: [UITextRange]](./allfoundranges.md)
  An ordered set of all the text ranges that match the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/foundrange(_:searchstring:document:))*