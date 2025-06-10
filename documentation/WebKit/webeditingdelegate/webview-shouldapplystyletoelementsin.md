# webView(_:shouldApplyStyle:toElementsIn:)

**Framework**: WebKit  
**Kind**: method

Returns whether the user should be allowed to apply a style to a range of content.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldApplyStyle style: DOMCSSStyleDeclaration!, toElementsIn range: DOMRange!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user should be allowed to apply the style to the content range; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `webView`: The web view that the user is editing.
- `style`: The style to apply.
- `range`: The range of the content.

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:shouldapplystyle:toelementsin:))*