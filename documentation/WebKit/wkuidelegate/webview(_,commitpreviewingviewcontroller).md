# webView(_:commitPreviewingViewController:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when the user performs a pop action on the preview.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func webView(_ webView: WKWebView, commitPreviewingViewController previewingViewController: UIViewController)
```

```objc
- (void) webView:(WKWebView *) webView commitPreviewingViewController:(UIViewController *) previewingViewController;
```

## Discussion

You must display the previewed view controller inside of your app.

## Parameters

- `webView`: The web view invoking the delegate method.
- `previewingViewController`: The view controller that is popped.

## See Also

### Responding to Force Touch actions
- [func webView(WKWebView, shouldPreviewElement: WKPreviewElementInfo) -> Bool](./webview%28_,shouldpreviewelement%29.md)
  Determines whether the given element should show a preview.
- [func webView(WKWebView, previewingViewControllerForElement: WKPreviewElementInfo, defaultActions: [any WKPreviewActionItem]) -> UIViewController?](./webview%28_,previewingviewcontrollerforelement,defaultactions%29.md)
  Called when the user performs a peek action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:commitpreviewingviewcontroller:))*