# applyStyle(_:)

**Framework**: WebKit  
**Kind**: method

Applies the CSS typing style to the current selection.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func applyStyle(_ style: DOMCSSStyleDeclaration!)
```

#### Discussion

This method does nothing if there is no current selection or if the current selection is collapsed.

This method hides the complexities of applying styles to elements. If necessary, this method will make multiple passes over the range of the current selection to ensure that the requested style is applied to the elements in that range, and takes into account the complexities of CSS style application rules. This method also simplifies styling attributes so that the minimum number of styling directives are used to yield a given computed style.

## Parameters

- `style`: The style to apply to the current selection.

## See Also

- [func computedStyle(for: DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](webview-swift.class/computedstyle(for:pseudoelement:).md)
  Returns the computed style of an element and its pseudo element.
- [var mediaStyle: String!](webview-swift.class/mediastyle.md)
  The receiver’s CSS media property.
- [var typingStyle: DOMCSSStyleDeclaration!](webview-swift.class/typingstyle.md)
  The receiver’s CSS typing style.
- [func styleDeclaration(withText: String!) -> DOMCSSStyleDeclaration!](webview-swift.class/styledeclaration(withtext:).md)
  Returns the CSS style declaration for the specified text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/applystyle(_:))*