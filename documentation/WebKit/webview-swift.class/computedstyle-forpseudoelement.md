# computedStyle(for:pseudoElement:)

**Framework**: WebKit  
**Kind**: method

Returns the computed style of an element and its pseudo element.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func computedStyle(for element: DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!
```

#### Return Value

An immutable object describing the computed style of `element` and `pseudoElement` according to the Cascading Style Sheets Specification at `http://www.w3.org/TR/CSS21`. Returns `nil` if the receiver doesn’t display `element`.

## Parameters

- `element`: The element whose computed style is returned.
- `pseudoElement`: The pseudo element for  .

## See Also

- [var mediaStyle: String!](webview-swift.class/mediastyle.md)
  The receiver’s CSS media property.
- [var typingStyle: DOMCSSStyleDeclaration!](webview-swift.class/typingstyle.md)
  The receiver’s CSS typing style.
- [func styleDeclaration(withText: String!) -> DOMCSSStyleDeclaration!](webview-swift.class/styledeclaration(withtext:).md)
  Returns the CSS style declaration for the specified text.
- [func applyStyle(DOMCSSStyleDeclaration!)](webview-swift.class/applystyle(_:).md)
  Applies the CSS typing style to the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/computedstyle(for:pseudoelement:))*