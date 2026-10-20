# WKUIDelegate

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

The methods for presenting native user interface elements on behalf of a webpage.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
@MainActor
protocol WKUIDelegate : NSObjectProtocol
```

```objc
@protocol WKUIDelegate <NSObject>
```

#### Overview

Web view user interface delegates implement this protocol to control the opening of new windows, augment the behavior of default menu items displayed when the user clicks elements, and perform other user interface-related tasks. These methods can be invoked as a result of handling JavaScript or other plug-in content. The default web view implementation assumes one window per web view, so nonconventional user interfaces might implement a user interface delegate.

## Topics

### Creating and closing the web view
- [func webView(WKWebView, createWebViewWith: WKWebViewConfiguration, for: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView?](./wkuidelegate/webview%28_,createwebviewwith,for,windowfeatures%29.md)
  Creates a new web view.
- [func webViewDidClose(WKWebView)](./wkuidelegate/webviewdidclose%28_%29.md)
  Notifies your app that the DOM window closed successfully.
### Displaying UI panels
- [func webView(WKWebView, runJavaScriptAlertPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: () -> Void)](./wkuidelegate/webview%28_,runjavascriptalertpanelwithmessage,initiatedbyframe,completionhandler%29.md)
  Displays a JavaScript alert panel.
- [func webView(WKWebView, runJavaScriptConfirmPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: (Bool) -> Void)](./wkuidelegate/webview%28_,runjavascriptconfirmpanelwithmessage,initiatedbyframe,completionhandler%29.md)
  Displays a JavaScript confirm panel.
- [func webView(WKWebView, runJavaScriptTextInputPanelWithPrompt: String, defaultText: String?, initiatedByFrame: WKFrameInfo, completionHandler: (String?) -> Void)](./wkuidelegate/webview%28_,runjavascripttextinputpanelwithprompt,defaulttext,initiatedbyframe,completionhandler%29.md)
  Displays a JavaScript text input panel.
- [func webView(WKWebView, showLockdownModeFirstUseMessage: String, completionHandler: (WKDialogResult) -> Void)](./wkuidelegate/webview%28_,showlockdownmodefirstusemessage,completionhandler%29.md)
  Displays a custom Lockdown Mode first use message.
- [enum WKDialogResult](./wkdialogresult.md)
  An enumeration that lists the possible ways a delegate handled displaying a custom Lockdown Mode first use dialog.
### Displaying an upload panel
- [func webView(WKWebView, runOpenPanelWith: WKOpenPanelParameters, initiatedByFrame: WKFrameInfo, completionHandler: ([URL]?) -> Void)](./wkuidelegate/webview%28_,runopenpanelwith,initiatedbyframe,completionhandler%29.md)
  Displays a file upload panel.
- [class WKOpenPanelParameters](./wkopenpanelparameters.md)
  The configuration details of a file upload control in your web content.
### Displaying a contextual menu
- [Adding context menus in your app](../UIKit/adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [func webView(WKWebView, contextMenuConfigurationForElement: WKContextMenuElementInfo, completionHandler: (UIContextMenuConfiguration?) -> Void)](./wkuidelegate/webview%28_,contextmenuconfigurationforelement,completionhandler%29.md)
  Tells the delegate that a contextual menu interaction began.
- [func webView(WKWebView, contextMenuForElement: WKContextMenuElementInfo, willCommitWithAnimator: any UIContextMenuInteractionCommitAnimating)](./wkuidelegate/webview%28_,contextmenuforelement,willcommitwithanimator%29.md)
  Provides the delegate with the animator object that the web view uses to display the contextual menu.
- [func webView(WKWebView, contextMenuWillPresentForElement: WKContextMenuElementInfo)](./wkuidelegate/webview%28_,contextmenuwillpresentforelement%29.md)
  Tells the delegate that the web view is about to present the contextual menu for the specified element.
- [func webView(WKWebView, contextMenuDidEndForElement: WKContextMenuElementInfo)](./wkuidelegate/webview%28_,contextmenudidendforelement%29.md)
  Tells the delegate that the web view dismissed the contextual menu for the specified element.
- [class UIContextMenuConfiguration](../UIKit/uicontextmenuconfiguration.md)
  An object containing the configuration details for the contextual menu.
### Displaying an edit menu
- [func webView(WKWebView, willDismissEditMenuWithAnimator: any UIEditMenuInteractionAnimating)](./wkuidelegate/webview%28_,willdismisseditmenuwithanimator%29.md)
  Tells the delegate that the web view is about to dismiss an edit menu.
- [func webView(WKWebView, willPresentEditMenuWithAnimator: any UIEditMenuInteractionAnimating)](./wkuidelegate/webview%28_,willpresenteditmenuwithanimator%29.md)
  Tells the delegate that the web view is about to present an edit menu.
### Requesting permissions
- [func webView(WKWebView, requestDeviceOrientationAndMotionPermissionFor: WKSecurityOrigin, initiatedByFrame: WKFrameInfo, decisionHandler: (WKPermissionDecision) -> Void)](./wkuidelegate/webview%28_,requestdeviceorientationandmotionpermissionfor,initiatedbyframe,decisionhandler%29.md)
  Determines whether a web resource, which the security origin object describes, can access the device’s orientation and motion.
- [func webView(WKWebView, requestMediaCapturePermissionFor: WKSecurityOrigin, initiatedByFrame: WKFrameInfo, type: WKMediaCaptureType, decisionHandler: (WKPermissionDecision) -> Void)](./wkuidelegate/webview%28_,requestmediacapturepermissionfor,initiatedbyframe,type,decisionhandler%29.md)
  Determines whether a web resource, which the security origin object describes, can access to the device’s microphone audio and camera video.
- [enum WKPermissionDecision](./wkpermissiondecision.md)
  An enumeration of possible permission decisions for device resource access.
- [enum WKMediaCaptureType](./wkmediacapturetype.md)
  An enumeration listing the types of media devices that can capture audio, video, or both.
### Deprecated
- [Deprecated symbols](./wkuidelegate-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Methods
- [func webView(WKWebView, insertInputSuggestion: UIInputSuggestion)](./wkuidelegate/webview%28_,insertinputsuggestion%29.md)
- [func webView(WKWebView, requestGeolocationPermissionFor: WKSecurityOrigin, initiatedByFrame: WKFrameInfo, decisionHandler: (WKPermissionDecision) -> Void)](./wkuidelegate/webview%28_,requestgeolocationpermissionfor,initiatedbyframe,decisionhandler%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Web views
- [Replacing UIWebView in your app](./replacing-uiwebview-in-your-app.md)
  Find a suitable alternative to handle your app’s web content.
- [Viewing Desktop or Mobile Web Content Using a Web View](./viewing-desktop-or-mobile-web-content-using-a-web-view.md)
  Implement a simple iPad web browser that can view either the desktop or mobile version of a website.
- [class WKWebView](./wkwebview.md)
  An object that displays interactive web content, such as for an in-app browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate)*