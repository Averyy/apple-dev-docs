# styleDeclaration(withText:)

**Framework**: WebKit  
**Kind**: method

Returns the CSS style declaration for the specified text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func styleDeclaration(withText text: String!) -> DOMCSSStyleDeclaration!
```

#### Return Value

The style declaration for `text`.

## Parameters

- `text`: The text whose style declaration is returned.

## See Also

- [func computedStyle(for: DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](webview-swift.class/computedstyle(for:pseudoelement:).md)
  Returns the computed style of an element and its pseudo element.
- [var mediaStyle: String!](webview-swift.class/mediastyle.md)
  The receiver’s CSS media property.
- [var typingStyle: DOMCSSStyleDeclaration!](webview-swift.class/typingstyle.md)
  The receiver’s CSS typing style.
- [func applyStyle(DOMCSSStyleDeclaration!)](webview-swift.class/applystyle(_:).md)
  Applies the CSS typing style to the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/styledeclaration(withtext:))*