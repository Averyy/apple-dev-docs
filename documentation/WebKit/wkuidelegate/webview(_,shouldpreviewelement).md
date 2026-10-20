# webView(_:shouldPreviewElement:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the given element should show a preview.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func webView(_ webView: WKWebView, shouldPreviewElement elementInfo: WKPreviewElementInfo) -> Bool
```

```objc
- (BOOL) webView:(WKWebView *) webView shouldPreviewElement:(WKPreviewElementInfo *) elementInfo;
```

#### Return Value

Return `NO` to disable previews for the given element.

#### Discussion

This method is only invoked for elements that have a default preview in WebKit.

## Parameters

- `webView`: The web view invoking the delegate method.
- `elementInfo`: The information associated with the element.

## See Also

### Responding to Force Touch actions
- [func webView(WKWebView, previewingViewControllerForElement: WKPreviewElementInfo, defaultActions: [any WKPreviewActionItem]) -> UIViewController?](./webview%28_,previewingviewcontrollerforelement,defaultactions%29.md)
  Called when the user performs a peek action.
- [func webView(WKWebView, commitPreviewingViewController: UIViewController)](./webview%28_,commitpreviewingviewcontroller%29.md)
  Called when the user performs a pop action on the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:shouldpreviewelement:))*