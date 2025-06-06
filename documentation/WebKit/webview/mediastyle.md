# mediaStyle

**Framework**: Webkit  
**Kind**: property

The receiver’s CSS media property.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var mediaStyle: String! { get set }
```

## See Also

- [func computedStyle(for: DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](webview/computedstyle(for:pseudoelement:).md)
  Returns the computed style of an element and its pseudo element.
- [var typingStyle: DOMCSSStyleDeclaration!](webview/typingstyle.md)
  The receiver’s CSS typing style.
- [func styleDeclaration(withText: String!) -> DOMCSSStyleDeclaration!](webview/styledeclaration(withtext:).md)
  Returns the CSS style declaration for the specified text.
- [func applyStyle(DOMCSSStyleDeclaration!)](webview/applystyle(_:).md)
  Applies the CSS typing style to the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/mediastyle)*