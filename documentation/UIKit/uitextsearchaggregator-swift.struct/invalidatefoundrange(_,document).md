# invalidateFoundRange(_:document:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes a text range from the set of matches.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
func invalidateFoundRange(_ range: UITextRange, document: DocumentIdentifier)
```

## Discussion

Call this method to invalidate a text range when removing or changing text in the document. This causes the system find panel to update it’s current state, and if the range is the highlighted range, the find panel advances to the next found result.

## Parameters

- `range`: The text range to remove from the set of matches.
- `document`: A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## See Also

### Tracking search results
- [func foundRange(UITextRange, searchString: String, document: DocumentIdentifier)](./foundrange%28_,searchstring,document%29.md)
  Adds a text range to the set of matches.
- [func invalidate()](./invalidate%28%29.md)
  Invalidates all currently shown ranges.
- [func finishedSearching()](./finishedsearching%28%29.md)
  Finishes the search for text ranges.
- [var allFoundRanges: [UITextRange]](./allfoundranges.md)
  An ordered set of all the text ranges that match the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/invalidatefoundrange(_:document:))*