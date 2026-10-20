# webView(_:contextMenuWillPresentForElement:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the web view is about to present the contextual menu for the specified element.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, contextMenuWillPresentForElement elementInfo: WKContextMenuElementInfo)
```

```objc
- (void) webView:(WKWebView *) webView contextMenuWillPresentForElement:(WKContextMenuElementInfo *) elementInfo;
```

## Parameters

- `webView`: The web view in which the interaction occurred.
- `elementInfo`: An object that contains information about the element involved in the interaction.

## See Also

### Displaying a contextual menu
- [Adding context menus in your app](../../UIKit/adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [func webView(WKWebView, contextMenuConfigurationForElement: WKContextMenuElementInfo, completionHandler: (UIContextMenuConfiguration?) -> Void)](./webview%28_,contextmenuconfigurationforelement,completionhandler%29.md)
  Tells the delegate that a contextual menu interaction began.
- [func webView(WKWebView, contextMenuForElement: WKContextMenuElementInfo, willCommitWithAnimator: any UIContextMenuInteractionCommitAnimating)](./webview%28_,contextmenuforelement,willcommitwithanimator%29.md)
  Provides the delegate with the animator object that the web view uses to display the contextual menu.
- [func webView(WKWebView, contextMenuDidEndForElement: WKContextMenuElementInfo)](./webview%28_,contextmenudidendforelement%29.md)
  Tells the delegate that the web view dismissed the contextual menu for the specified element.
- [class UIContextMenuConfiguration](../../UIKit/uicontextmenuconfiguration.md)
  An object containing the configuration details for the contextual menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:contextmenuwillpresentforelement:))*