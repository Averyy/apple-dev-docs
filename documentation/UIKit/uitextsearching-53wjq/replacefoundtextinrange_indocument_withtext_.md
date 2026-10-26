# replaceFoundTextInRange:inDocument:withText:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the searchable object to replace the text range for the highlighted search result.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) replaceFoundTextInRange:(UITextRange *) range inDocument:(UITextSearchDocumentIdentifier) document withText:(NSString *) replacementText;
```

#### Discussion

When [`supportsTextReplacement`](./supportstextreplacement.md) returns `YES,` the system calls this method during a find session to request a text range to replace.

## Parameters

- `range`: The text range to replace.
- `document`: A string that uniquely identifies a document when searching multiple documents, or `nil` when searching a single document.
- `replacementText`: The string to replace the text with.

## See Also

### Handling replacements
- [supportsTextReplacement](./supportstextreplacement.md)
  A Boolean value that indicates whether the searchable object supports replacing text.
- [- replaceAllOccurrencesOfQueryString:usingOptions:withText:](./replacealloccurrencesofquerystring_usingoptions_withtext_.md)
  Informs the searchable object to replace all matching text across all searchable documents.
- [- shouldReplaceFoundTextInRange:inDocument:withText:](./shouldreplacefoundtextinrange_indocument_withtext_.md)
  Determines whether the searchable object allows replacement of the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/replacefoundtextinrange:indocument:withtext:)*