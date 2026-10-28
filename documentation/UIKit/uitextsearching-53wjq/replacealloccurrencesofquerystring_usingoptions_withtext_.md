# replaceAllOccurrencesOfQueryString:usingOptions:withText:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the searchable object to replace all matching text across all searchable documents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) replaceAllOccurrencesOfQueryString:(NSString *) queryString usingOptions:(UITextSearchOptions *) options withText:(NSString *) replacementText;
```

## Discussion

When [`supportsTextReplacement`](./supportstextreplacement.md) returns `YES,` the system calls this method during a find session to request the replacement of all text matching the query string.

## Parameters

- `queryString`: The string to search for and replace.
- `options`: The configurable options to use for matching words and comparing strings.
- `replacementText`: The string to replace the text with.

## See Also

### Handling replacements
- [supportsTextReplacement](./supportstextreplacement.md)
  A Boolean value that indicates whether the searchable object supports replacing text.
- [- replaceFoundTextInRange:inDocument:withText:](./replacefoundtextinrange_indocument_withtext_.md)
  Informs the searchable object to replace the text range for the highlighted search result.
- [- shouldReplaceFoundTextInRange:inDocument:withText:](./shouldreplacefoundtextinrange_indocument_withtext_.md)
  Determines whether the searchable object allows replacement of the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/replacealloccurrencesofquerystring:usingoptions:withtext:)*