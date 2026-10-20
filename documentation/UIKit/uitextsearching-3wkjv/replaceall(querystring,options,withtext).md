# replaceAll(queryString:options:withText:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Informs the searchable object to replace all matching text across all searchable documents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
func replaceAll(queryString: String, options: UITextSearchOptions, withText: String)
```

#### Discussion

When [`supportsTextReplacement`](./supportstextreplacement.md) returns `YES,` the system calls this method during a find session to request the replacement of all text matching the query string.

## Parameters

- `queryString`: The string to search for and replace.
- `options`: The configurable options to use for matching words and comparing strings.
- `withText`: The string to replace the text with.

## Default Implementations

### UITextSearching Implementations
- [func replaceAll(queryString: String, options: UITextSearchOptions, withText: String)](./replaceall%28querystring,options,withtext%29-72c3k.md)

## See Also

### Handling replacements
- [var supportsTextReplacement: Bool](./supportstextreplacement.md)
  A Boolean value that indicates whether the searchable object supports replacing text.
- [func replace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String)](./replace%28foundtextrange,document,withtext%29.md)
  Informs the searchable object to replace the text range for the highlighted search result.
- [func shouldReplace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String) -> Bool](./shouldreplace%28foundtextrange,document,withtext%29.md)
  Determines whether the searchable object allows replacement of the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/replaceall(querystring:options:withtext:))*