# webView(_:shouldPreviewElement:)

**Framework**: Webkit  
**Kind**: method

Determines whether the given element should show a preview.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, shouldPreviewElement elementInfo: WKPreviewElementInfo) -> Bool
```

#### Return Value

Return `NO` to disable previews for the given element.

#### Discussion

This method is only invoked for elements that have a default preview in WebKit.

## Parameters

- `webView`: The web view invoking the delegate method.
- `elementInfo`: The information associated with the element.

## See Also

- [func webView(WKWebView, previewingViewControllerForElement: WKPreviewElementInfo, defaultActions: [any WKPreviewActionItem]) -> UIViewController?](wkuidelegate/webview(_:previewingviewcontrollerforelement:defaultactions:).md)
  Called when the user performs a peek action.
- [func webView(WKWebView, commitPreviewingViewController: UIViewController)](wkuidelegate/webview(_:commitpreviewingviewcontroller:).md)
  Called when the user performs a pop action on the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:shouldpreviewelement:))*