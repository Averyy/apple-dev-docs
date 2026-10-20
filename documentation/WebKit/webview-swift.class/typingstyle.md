# typingStyle

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s CSS typing style.

**Availability**:
- macOS

## Declaration

```swift
var typingStyle: DOMCSSStyleDeclaration! { get set }
```

```objc
@property (nonatomic, strong) DOMCSSStyleDeclaration * typingStyle;
```

#### Discussion

The typing style is reset automatically when the receiver’s selection changes.

## See Also

### Getting and Setting CSS Properties
- [func computedStyle(for: DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](./computedstyle%28for,pseudoelement%29.md)
  Returns the computed style of an element and its pseudo element.
- [var mediaStyle: String!](./mediastyle.md)
  The receiver’s CSS media property.
- [func styleDeclaration(withText: String!) -> DOMCSSStyleDeclaration!](./styledeclaration%28withtext%29.md)
  Returns the CSS style declaration for the specified text.
- [func applyStyle(DOMCSSStyleDeclaration!)](./applystyle%28_%29.md)
  Applies the CSS typing style to the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/typingstyle)*