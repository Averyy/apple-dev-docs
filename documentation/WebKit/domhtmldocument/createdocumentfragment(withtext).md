# createDocumentFragment(withText:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Creates a document fragment containing the given text.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func createDocumentFragment(withText text: String!) -> DOMDocumentFragment!
```

```objc
- (DOMDocumentFragment *) createDocumentFragmentWithText:(NSString *) text;
```

## Return Value

A `DOMDocumentFragment` object derived from the source text.

## Discussion

This is a convenience method for the `createDocumentFragment` method in `DOMDocument`. This method creates a fragment that contains the supplied plain text.

## Parameters

- `text`: The text to convert.

## See Also

### Creating Document Fragments
- [func createDocumentFragment(withMarkupString: String!, baseURL: URL!) -> DOMDocumentFragment!](./createdocumentfragment%28withmarkupstring,baseurl%29.md)
  Creates a document fragment containing the given HTML markup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/domhtmldocument/createdocumentfragment(withtext:))*