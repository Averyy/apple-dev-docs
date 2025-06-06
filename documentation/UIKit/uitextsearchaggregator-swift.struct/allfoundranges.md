# allFoundRanges

**Framework**: UIKit  
**Kind**: property

An ordered set of all the text ranges that match the search.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
var allFoundRanges: [UITextRange] { get }
```

## See Also

- [func foundRange(UITextRange, searchString: String, document: DocumentIdentifier)](uitextsearchaggregator-swift.struct/foundrange(_:searchstring:document:).md)
  Adds a text range to the set of matches.
- [func invalidateFoundRange(UITextRange, document: DocumentIdentifier)](uitextsearchaggregator-swift.struct/invalidatefoundrange(_:document:).md)
  Removes a text range from the set of matches.
- [func invalidate()](uitextsearchaggregator-swift.struct/invalidate.md)
  Invalidates all currently shown ranges.
- [func finishedSearching()](uitextsearchaggregator-swift.struct/finishedsearching.md)
  Finishes the search for text ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/allfoundranges)*