# styleDeclaration(withText:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the CSS style declaration for the specified text.

**Availability**:
- macOS

## Declaration

```swift
func styleDeclaration(withText text: String!) -> DOMCSSStyleDeclaration!
```

```objc
- (DOMCSSStyleDeclaration *) styleDeclarationWithText:(NSString *) text;
```

#### Return Value

The style declaration for `text`.

## Parameters

- `text`: The text whose style declaration is returned.

## See Also

### Getting and Setting CSS Properties
- [func computedStyle(for: DOMElement!, pseudoElement: String!) -> DOMCSSStyleDeclaration!](./computedstyle%28for,pseudoelement%29.md)
  Returns the computed style of an element and its pseudo element.
- [var mediaStyle: String!](./mediastyle.md)
  The receiver’s CSS media property.
- [var typingStyle: DOMCSSStyleDeclaration!](./typingstyle.md)
  The receiver’s CSS typing style.
- [func applyStyle(DOMCSSStyleDeclaration!)](./applystyle%28_%29.md)
  Applies the CSS typing style to the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/styledeclaration(withtext:))*