# webView(_:contextMenuForElement:willCommitWithAnimator:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Provides the delegate with the animator object that the web view uses to display the contextual menu.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, contextMenuForElement elementInfo: WKContextMenuElementInfo, willCommitWithAnimator animator: any UIContextMenuInteractionCommitAnimating)
```

```objc
- (void) webView:(WKWebView *) webView contextMenuForElement:(WKContextMenuElementInfo *) elementInfo willCommitWithAnimator:(id<UIContextMenuInteractionCommitAnimating>) animator;
```

## Parameters

- `webView`: The web view in which the interaction occurred.
- `elementInfo`: An object that contains information about the element involved in the interaction.
- `animator`: The animator object to use to commit additional animations related to the appearance of the contextual menu.

## See Also

### Displaying a contextual menu
- [Adding context menus in your app](../../UIKit/adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [func webView(WKWebView, contextMenuConfigurationForElement: WKContextMenuElementInfo, completionHandler: (UIContextMenuConfiguration?) -> Void)](./webview%28_,contextmenuconfigurationforelement,completionhandler%29.md)
  Tells the delegate that a contextual menu interaction began.
- [func webView(WKWebView, contextMenuWillPresentForElement: WKContextMenuElementInfo)](./webview%28_,contextmenuwillpresentforelement%29.md)
  Tells the delegate that the web view is about to present the contextual menu for the specified element.
- [func webView(WKWebView, contextMenuDidEndForElement: WKContextMenuElementInfo)](./webview%28_,contextmenudidendforelement%29.md)
  Tells the delegate that the web view dismissed the contextual menu for the specified element.
- [class UIContextMenuConfiguration](../../UIKit/uicontextmenuconfiguration.md)
  An object containing the configuration details for the contextual menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:contextmenuforelement:willcommitwithanimator:))*