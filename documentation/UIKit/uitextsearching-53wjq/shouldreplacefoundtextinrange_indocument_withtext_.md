# shouldReplaceFoundTextInRange:inDocument:withText:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the searchable object allows replacement of the text range you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (BOOL) shouldReplaceFoundTextInRange:(UITextRange *) range inDocument:(UITextSearchDocumentIdentifier) document withText:(NSString *) replacementText;
```

## Return Value

Return `No` to prevent the replacement of a particular text range.

## Discussion

Returning `NO` from this method disables the “replace” button in the find panel. If you don’t implement this method, the system assumes all results are replacable.

## Parameters

- `range`: The range of characters in a text container to consider a replacement for.
- `document`: A string that uniquely identifies the document containing the text range.
- `replacementText`: The string to replace the text with.

## See Also

### Handling replacements
- [supportsTextReplacement](./supportstextreplacement.md)
  A Boolean value that indicates whether the searchable object supports replacing text.
- [- replaceFoundTextInRange:inDocument:withText:](./replacefoundtextinrange_indocument_withtext_.md)
  Informs the searchable object to replace the text range for the highlighted search result.
- [- replaceAllOccurrencesOfQueryString:usingOptions:withText:](./replacealloccurrencesofquerystring_usingoptions_withtext_.md)
  Informs the searchable object to replace all matching text across all searchable documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/shouldreplacefoundtextinrange:indocument:withtext:)*