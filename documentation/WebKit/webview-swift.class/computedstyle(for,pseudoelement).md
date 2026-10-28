# computedStyle(for:pseudoElement:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the computed style of an element and its pseudo element.

**Availability**:
- macOS

## Declaration

```swift
func computedStyle(for element: DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!
```

```objc
- (DOMCSSStyleDeclaration *) computedStyleForElement:(DOMElement *) element pseudoElement:(NSString *) pseudoElement;
```

## Return Value

An immutable object describing the computed style of `element` and `pseudoElement` according to the Cascading Style Sheets Specification at `http://www.w3.org/TR/CSS21`. Returns `nil` if the receiver doesn’t display `element`.

## Parameters

- `element`: The element whose computed style is returned.
- `pseudoElement`: The pseudo element for `element`.

## See Also

### Getting and Setting CSS Properties
- [var mediaStyle: String!](./mediastyle.md)
  The receiver’s CSS media property.
- [var typingStyle: DOMCSSStyleDeclaration!](./typingstyle.md)
  The receiver’s CSS typing style.
- [func styleDeclaration(withText: String!) -> DOMCSSStyleDeclaration!](./styledeclaration%28withtext%29.md)
  Returns the CSS style declaration for the specified text.
- [func applyStyle(DOMCSSStyleDeclaration!)](./applystyle%28_%29.md)
  Applies the CSS typing style to the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/computedstyle(for:pseudoelement:))*