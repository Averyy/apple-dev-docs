# invalidateFoundRange:inDocument:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes a text range from the set of matches.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) invalidateFoundRange:(UITextRange *) range inDocument:(UITextSearchDocumentIdentifier) document;
```

#### Discussion

Call this method to invalidate a text range when removing or changing text in the document. This causes the system find panel to update its current state, and if the range is the highlighted range, the find panel advances to the next found result.

## Parameters

- `range`: The text range to remove from the set of matches.
- `document`: A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## See Also

### Tracking search results
- [- foundRange:forSearchString:inDocument:](./foundrange_forsearchstring_indocument_.md)
  Adds a text range to the set of matches.
- [- invalidate](./invalidate.md)
  Invalidates all currently shown ranges.
- [- finishedSearching](./finishedsearching.md)
  Finishes the search for text ranges.
- [allFoundRanges](./allfoundranges.md)
  An ordered set of all the text ranges that match the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-c.protocol/invalidatefoundrange:indocument:)*