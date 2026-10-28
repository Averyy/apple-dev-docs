# foundRange:forSearchString:inDocument:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds a text range to the set of matches.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) foundRange:(UITextRange *) range forSearchString:(NSString *) string inDocument:(UITextSearchDocumentIdentifier) document;
```

## Discussion

Call this method to add a text range found in your document to the set of matches.

## Parameters

- `range`: The text range to add to the set of matches.
- `string`: The query string the search used to locate this range of text.
- `document`: A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## See Also

### Tracking search results
- [- invalidateFoundRange:inDocument:](./invalidatefoundrange_indocument_.md)
  Removes a text range from the set of matches.
- [- invalidate](./invalidate.md)
  Invalidates all currently shown ranges.
- [- finishedSearching](./finishedsearching.md)
  Finishes the search for text ranges.
- [allFoundRanges](./allfoundranges.md)
  An ordered set of all the text ranges that match the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchaggregator-c.protocol/foundrange:forsearchstring:indocument:)*