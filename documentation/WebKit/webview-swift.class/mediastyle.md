# mediaStyle

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s CSS media property.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var mediaStyle: String! { get set }
```

```objc
@property (nonatomic, copy) NSString * mediaStyle;
```

## See Also

### Getting and Setting CSS Properties
- [func computedStyle(for: DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](./computedstyle%28for,pseudoelement%29.md)
  Returns the computed style of an element and its pseudo element.
- [var typingStyle: DOMCSSStyleDeclaration!](./typingstyle.md)
  The receiver’s CSS typing style.
- [func styleDeclaration(withText: String!) -> DOMCSSStyleDeclaration!](./styledeclaration%28withtext%29.md)
  Returns the CSS style declaration for the specified text.
- [func applyStyle(DOMCSSStyleDeclaration!)](./applystyle%28_%29.md)
  Applies the CSS typing style to the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/mediastyle)*