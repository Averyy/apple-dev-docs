# webView(_:previewingViewControllerForElement:defaultActions:)

**Framework**: WebKit  
**Kind**: method

Called when the user performs a peek action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, previewingViewControllerForElement elementInfo: WKPreviewElementInfo, defaultActions previewActions: [any WKPreviewActionItem]) -> UIViewController?
```

#### Return Value

Return `nil` to use Webkit’s default preview behavior. Returning a view controller allows [`webView(_:commitPreviewingViewController:)`](wkuidelegate/webview(_:commitpreviewingviewcontroller:).md) to be invoked when the user performs a pop action.

#### Discussion

To use the default actions, your app must return the actions to be run in your view controller’s implementation of [`previewActionItems`](https://developer.apple.com/documentation/UIKit/UIViewController/previewActionItems).

## Parameters

- `webView`: The web view invoking the delegate method.
- `elementInfo`: The information associated with the element.
- `previewActions`: An array of default actions used by the element.

## See Also

- [func webView(WKWebView, shouldPreviewElement: WKPreviewElementInfo) -> Bool](wkuidelegate/webview(_:shouldpreviewelement:).md)
  Determines whether the given element should show a preview.
- [func webView(WKWebView, commitPreviewingViewController: UIViewController)](wkuidelegate/webview(_:commitpreviewingviewcontroller:).md)
  Called when the user performs a pop action on the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:previewingviewcontrollerforelement:defaultactions:))*