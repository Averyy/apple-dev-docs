# createDocumentFragment(withMarkupString:baseURL:)

**Framework**: Webkit  
**Kind**: method

Creates a document fragment containing the given HTML markup.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func createDocumentFragment(withMarkupString markupString: String!, baseURL: URL!) -> DOMDocumentFragment!
```

#### Return Value

A `DOMDocumentFragment` derived from the original markup string.

#### Discussion

This is a convenience method for the `createDocumentFragment` method in `DOMDocument`. It creates a fragment that has the HTML markup parsed into child nodes of the fragment using the `baseURL` to resolve any relative paths for images or other resources.

## Parameters

- `markupString`: The HTML content to parse into a DOM tree.
- `baseURL`: The URI from which the content originated. Used for interpreting relative URLs.

## See Also

- [func createDocumentFragment(withText: String!) -> DOMDocumentFragment!](domhtmldocument/createdocumentfragment(withtext:).md)
  Creates a document fragment containing the given text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domhtmldocument/createdocumentfragment(withmarkupstring:baseurl:))*