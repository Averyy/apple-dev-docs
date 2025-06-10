# typingStyle

**Framework**: WebKit  
**Kind**: property

The receiver’s CSS typing style.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var typingStyle: DOMCSSStyleDeclaration! { get set }
```

#### Discussion

The typing style is reset automatically when the receiver’s selection changes.

## See Also

- [func computedStyle(for: DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](webview-swift.class/computedstyle(for:pseudoelement:).md)
  Returns the computed style of an element and its pseudo element.
- [var mediaStyle: String!](webview-swift.class/mediastyle.md)
  The receiver’s CSS media property.
- [func styleDeclaration(withText: String!) -> DOMCSSStyleDeclaration!](webview-swift.class/styledeclaration(withtext:).md)
  Returns the CSS style declaration for the specified text.
- [func applyStyle(DOMCSSStyleDeclaration!)](webview-swift.class/applystyle(_:).md)
  Applies the CSS typing style to the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/typingstyle)*