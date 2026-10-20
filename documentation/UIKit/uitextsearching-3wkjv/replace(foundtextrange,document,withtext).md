# replace(foundTextRange:document:withText:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Informs the searchable object to replace the text range for the highlighted search result.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
func replace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String)
```

#### Discussion

When [`supportsTextReplacement`](./supportstextreplacement.md) returns `YES,` the system calls this method during a find session to request a text range to replace.

## Parameters

- `foundTextRange`: The text range to replace.
- `document`: A string that uniquely identifies a document when searching multiple documents, or `nil` when searching a single document.
- `withText`: The string to replace the text with.

## Default Implementations

### UITextSearching Implementations
- [func replace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String)](./replace%28foundtextrange,document,withtext%29-4psma.md)

## See Also

### Handling replacements
- [var supportsTextReplacement: Bool](./supportstextreplacement.md)
  A Boolean value that indicates whether the searchable object supports replacing text.
- [func replaceAll(queryString: String, options: UITextSearchOptions, withText: String)](./replaceall%28querystring,options,withtext%29.md)
  Informs the searchable object to replace all matching text across all searchable documents.
- [func shouldReplace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String) -> Bool](./shouldreplace%28foundtextrange,document,withtext%29.md)
  Determines whether the searchable object allows replacement of the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/replace(foundtextrange:document:withtext:))*