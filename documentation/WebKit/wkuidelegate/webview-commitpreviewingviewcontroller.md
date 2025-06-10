# webView(_:commitPreviewingViewController:)

**Framework**: WebKit  
**Kind**: method

Called when the user performs a pop action on the preview.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, commitPreviewingViewController previewingViewController: UIViewController)
```

#### Discussion

You must display the previewed view controller inside of your app.

## Parameters

- `webView`: The web view invoking the delegate method.
- `previewingViewController`: The view controller that is popped.

## See Also

- [func webView(WKWebView, shouldPreviewElement: WKPreviewElementInfo) -> Bool](wkuidelegate/webview(_:shouldpreviewelement:).md)
  Determines whether the given element should show a preview.
- [func webView(WKWebView, previewingViewControllerForElement: WKPreviewElementInfo, defaultActions: [any WKPreviewActionItem]) -> UIViewController?](wkuidelegate/webview(_:previewingviewcontrollerforelement:defaultactions:).md)
  Called when the user performs a peek action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:commitpreviewingviewcontroller:))*