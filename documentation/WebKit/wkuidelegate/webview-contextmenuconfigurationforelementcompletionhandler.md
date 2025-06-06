# webView(_:contextMenuConfigurationForElement:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Tells the delegate that a contextual menu interaction began.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, contextMenuConfigurationFor elementInfo: WKContextMenuElementInfo) async -> UIContextMenuConfiguration?
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func webView(_ webView: WKWebView, contextMenuConfigurationFor elementInfo: WKContextMenuElementInfo) async -> UIContextMenuConfiguration?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
optional func webView(_ webView: WKWebView, contextMenuConfigurationFor elementInfo: WKContextMenuElementInfo) async -> UIContextMenuConfiguration?
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `webView`: The web view in which the interaction occurred.
- `elementInfo`: An object that contains information about the element involved in the interaction.
- `completionHandler`: The completion handler for you to call with information about how you want to handle the interaction. This handler block has no return value and takes the following parameter:

## See Also

- [Adding context menus in your app](../UIKit/adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [func webView(WKWebView, contextMenuForElement: WKContextMenuElementInfo, willCommitWithAnimator: any UIContextMenuInteractionCommitAnimating)](wkuidelegate/webview(_:contextmenuforelement:willcommitwithanimator:).md)
  Provides the delegate with the animator object that the web view uses to display the contextual menu.
- [func webView(WKWebView, contextMenuWillPresentForElement: WKContextMenuElementInfo)](wkuidelegate/webview(_:contextmenuwillpresentforelement:).md)
  Tells the delegate that the web view is about to present the contextual menu for the specified element.
- [func webView(WKWebView, contextMenuDidEndForElement: WKContextMenuElementInfo)](wkuidelegate/webview(_:contextmenudidendforelement:).md)
  Tells the delegate that the web view dismissed the contextual menu for the specified element.
- [@MainActor class UIContextMenuConfiguration](../UIKit/UIContextMenuConfiguration.md)
  An object containing the configuration details for the contextual menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:contextmenuconfigurationforelement:completionhandler:))*