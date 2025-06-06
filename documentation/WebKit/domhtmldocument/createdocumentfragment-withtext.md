# createDocumentFragment(withText:)

**Framework**: Webkit  
**Kind**: method

Creates a document fragment containing the given text.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func createDocumentFragment(withText text: String!) -> DOMDocumentFragment!
```

#### Return Value

A `DOMDocumentFragment` object derived from the source text.

#### Discussion

This is a convenience method for the `createDocumentFragment` method in `DOMDocument`. This method creates a fragment that contains the supplied plain text.

## Parameters

- `text`: The text to convert.

## See Also

- [func createDocumentFragment(withMarkupString: String!, baseURL: URL!) -> DOMDocumentFragment!](domhtmldocument/createdocumentfragment(withmarkupstring:baseurl:).md)
  Creates a document fragment containing the given HTML markup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domhtmldocument/createdocumentfragment(withtext:))*