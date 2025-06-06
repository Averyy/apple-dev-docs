# webView(_:contextMenuForElement:willCommitWithAnimator:)

**Framework**: Webkit  
**Kind**: method

Provides the delegate with the animator object that the web view uses to display the contextual menu.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, contextMenuForElement elementInfo: WKContextMenuElementInfo, willCommitWithAnimator animator: any UIContextMenuInteractionCommitAnimating)
```

## Parameters

- `webView`: The web view in which the interaction occurred.
- `elementInfo`: An object that contains information about the element involved in the interaction.
- `animator`: The animator object to use to commit additional animations related to the appearance of the contextual menu.

## See Also

- [Adding context menus in your app](../UIKit/adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [func webView(WKWebView, contextMenuConfigurationForElement: WKContextMenuElementInfo, completionHandler: (UIContextMenuConfiguration?) -> Void)](wkuidelegate/webview(_:contextmenuconfigurationforelement:completionhandler:).md)
  Tells the delegate that a contextual menu interaction began.
- [func webView(WKWebView, contextMenuWillPresentForElement: WKContextMenuElementInfo)](wkuidelegate/webview(_:contextmenuwillpresentforelement:).md)
  Tells the delegate that the web view is about to present the contextual menu for the specified element.
- [func webView(WKWebView, contextMenuDidEndForElement: WKContextMenuElementInfo)](wkuidelegate/webview(_:contextmenudidendforelement:).md)
  Tells the delegate that the web view dismissed the contextual menu for the specified element.
- [@MainActor class UIContextMenuConfiguration](../UIKit/UIContextMenuConfiguration.md)
  An object containing the configuration details for the contextual menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:contextmenuforelement:willcommitwithanimator:))*