# webView(_:previewingViewControllerForElement:defaultActions:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when the user performs a peek action.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func webView(_ webView: WKWebView, previewingViewControllerForElement elementInfo: WKPreviewElementInfo, defaultActions previewActions: [any WKPreviewActionItem]) -> UIViewController?
```

```objc
- (UIViewController *) webView:(WKWebView *) webView previewingViewControllerForElement:(WKPreviewElementInfo *) elementInfo defaultActions:(NSArray<id<WKPreviewActionItem>> *) previewActions;
```

## Return Value

Return `nil` to use Webkit’s default preview behavior. Returning a view controller allows [`webView(_:commitPreviewingViewController:)`](./webview%28_,commitpreviewingviewcontroller%29.md) to be invoked when the user performs a pop action.

## Discussion

To use the default actions, your app must return the actions to be run in your view controller’s implementation of [`previewActionItems`](../../UIKit/uiviewcontroller/previewactionitems.md).

## Parameters

- `webView`: The web view invoking the delegate method.
- `elementInfo`: The information associated with the element.
- `previewActions`: An array of default actions used by the element.

## See Also

### Responding to Force Touch actions
- [func webView(WKWebView, shouldPreviewElement: WKPreviewElementInfo) -> Bool](./webview%28_,shouldpreviewelement%29.md)
  Determines whether the given element should show a preview.
- [func webView(WKWebView, commitPreviewingViewController: UIViewController)](./webview%28_,commitpreviewingviewcontroller%29.md)
  Called when the user performs a pop action on the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:previewingviewcontrollerforelement:defaultactions:))*