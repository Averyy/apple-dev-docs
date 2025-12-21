# WebUIDelegate

**Framework**: WebKit  
**Kind**: protocol

Web view user interface delegates implement this protocol to control the opening of new windows, augment the behavior of default menu items displayed when the user clicks elements, and perform other user interface–related tasks. These methods can be invoked as a result of handling JavaScript or other plug-in content. Delegates that display more than one web view per window, for example, need to implement some of these methods to handle that case. The default implementation assumes one window per web view, so non-conventional user interfaces might implement a user interface delegate.

**Availability**:
- macOS 10.3+

## Declaration

```swift
protocol WebUIDelegate : NSObjectProtocol
```

## Topics

### Creating and Closing Windows
- [func webView(WebView!, createWebViewModalDialogWith: URLRequest!) -> WebView!](webuidelegate/webview(_:createwebviewmodaldialogwith:).md)
  Creates a modal window containing a web view that loads the specified request.
- [func webViewRunModal(WebView!)](webuidelegate/webviewrunmodal(_:).md)
  Displays a web view in a modal window.
- [func webView(WebView!, createWebViewWith: URLRequest!) -> WebView!](webuidelegate/webview(_:createwebviewwith:).md)
  Creates a window containing a web view to load the specified request.
- [func webViewClose(WebView!)](webuidelegate/webviewclose(_:).md)
  Closes a web view in a window.
### Moving and Resizing Windows
- [func webViewIsResizable(WebView!) -> Bool](webuidelegate/webviewisresizable(_:).md)
  Returns a Boolean value indicating whether a web view’s window can be resized.
- [func webView(WebView!, setResizable: Bool)](webuidelegate/webview(_:setresizable:).md)
  Sets whether a web view’s window can be resized.
- [func webView(WebView!, setFrame: NSRect)](webuidelegate/webview(_:setframe:).md)
  Sets the frame rectangle of a web view’s window to the specified frame size.
- [func webViewFrame(WebView!) -> NSRect](webuidelegate/webviewframe(_:).md)
  Returns the frame rectangle of a web view’s window.
### Making Windows Key and Main
- [func webViewFocus(WebView!)](webuidelegate/webviewfocus(_:).md)
  Brings a web view’s window to the front and makes it the active window.
- [func webViewUnfocus(WebView!)](webuidelegate/webviewunfocus(_:).md)
  Relinquishes focus on a web view’s window.
### Ordering Windows
- [func webViewShow(WebView!)](webuidelegate/webviewshow(_:).md)
  Displays a web view’s window and moves it to the front.
### Working with the Responder Chain
- [func webViewFirstResponder(WebView!) -> NSResponder!](webuidelegate/webviewfirstresponder(_:).md)
  Returns the first responder of the web view’s window.
- [func webView(WebView!, makeFirstResponder: NSResponder!)](webuidelegate/webview(_:makefirstresponder:).md)
  Sets the first responder of a web view’s window to the specified view.
### Handling Mouse Events
- [func webView(WebView!, mouseDidMoveOverElement: [AnyHashable : Any]!, modifierFlags: Int)](webuidelegate/webview(_:mousedidmoveoverelement:modifierflags:).md)
  Updates information about the element the user is mousing over.
- [func webView(WebView!, contextMenuItemsForElement: [AnyHashable : Any]!, defaultMenuItems: [Any]!) -> [Any]!](webuidelegate/webview(_:contextmenuitemsforelement:defaultmenuitems:).md)
  Returns menu items to display in an element’s contextual menu.
### Opening Panels
- [func webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedBy: WebFrame!)](webuidelegate/webview(_:runjavascriptalertpanelwithmessage:initiatedby:).md)
  Displays a JavaScript alert panel containing the specified message.
- [func webView(WebView!, runJavaScriptConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runjavascriptconfirmpanelwithmessage:initiatedby:).md)
  Displays a JavaScript confirmation panel with the specified message.
- [func webView(WebView!, runJavaScriptTextInputPanelWithPrompt: String!, defaultText: String!, initiatedBy: WebFrame!) -> String!](webuidelegate/webview(_:runjavascripttextinputpanelwithprompt:defaulttext:initiatedby:).md)
  Displays a JavaScript text input panel and returns the entered text.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:).md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:allowmultiplefiles:).md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runBeforeUnloadConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runbeforeunloadconfirmpanelwithmessage:initiatedby:).md)
  Displays a confirmation panel containing the specified message before a window closes.
### Displaying Status Messages
- [func webView(WebView!, setStatusText: String!)](webuidelegate/webview(_:setstatustext:).md)
  Sets the status message displayed by a web view’s window, if any, to the specified text.
- [func webViewStatusText(WebView!) -> String!](webuidelegate/webviewstatustext(_:).md)
  Returns the current status message from a web view’s window.
### Managing Toolbars and the Status Bar
- [func webViewAreToolbarsVisible(WebView!) -> Bool](webuidelegate/webviewaretoolbarsvisible(_:).md)
  Returns a Boolean value indicating whether any toolbars are visible in a web view’s window.
- [func webView(WebView!, setToolbarsVisible: Bool)](webuidelegate/webview(_:settoolbarsvisible:).md)
  Sets whether a web view’s toolbars should be visible.
- [func webViewIsStatusBarVisible(WebView!) -> Bool](webuidelegate/webviewisstatusbarvisible(_:).md)
  Returns a Boolean value indicating whether the status bar in a web view’s window is visible.
- [func webView(WebView!, setStatusBarVisible: Bool)](webuidelegate/webview(_:setstatusbarvisible:).md)
  Sets the visibility of the status bar in a web view’s window.
### Controlling Drag Behavior
- [func webView(WebView!, dragDestinationActionMaskFor: (any NSDraggingInfo)!) -> Int](webuidelegate/webview(_:dragdestinationactionmaskfor:).md)
  Returns a mask indicating which drag operations are allowed by the sender.
- [func webView(WebView!, dragSourceActionMaskFor: NSPoint) -> Int](webuidelegate/webview(_:dragsourceactionmaskfor:).md)
  Returns a mask indicating which drag-source actions are allowed for a drag that begins at the specified location.
- [func webView(WebView!, willPerform: WebDragDestinationAction, for: (any NSDraggingInfo)!)](webuidelegate/webview(_:willperform:for:).md)
  Tells the receiver that the sending web view will perform the specified drag-destination action.
- [func webView(WebView!, willPerform: WebDragSourceAction, from: NSPoint, with: NSPasteboard!)](webuidelegate/webview(_:willperform:from:with:).md)
  Tells the receiver that the sending web view will perform the specified drag-source action.
### Controlling Other Behaviors
- [func webView(WebView!, shouldPerformAction: Selector!, fromSender: Any!) -> Bool](webuidelegate/webview(_:shouldperformaction:fromsender:).md)
  Returns a Boolean value that indicates whether the action sent by the specified object should be performed.
- [func webView(WebView!, validate: (any NSValidatedUserInterfaceItem)!, defaultValidation: Bool) -> Bool](webuidelegate/webview(_:validate:defaultvalidation:).md)
  Returns a Boolean value that indicates whether the specified user interface item is valid.
### Printing
- [func webView(WebView!, print: WebFrameView!)](webuidelegate/webview(_:print:).md)
  Prints the contents of a web frame view.
- [func webViewHeaderHeight(WebView!) -> Float](webuidelegate/webviewheaderheight(_:).md)
  Returns the height of the web view’s printed page header.
- [func webViewFooterHeight(WebView!) -> Float](webuidelegate/webviewfooterheight(_:).md)
  Returns the height of the web view’s printed page footer.
- [func webView(WebView!, drawHeaderIn: NSRect)](webuidelegate/webview(_:drawheaderin:).md)
  Draws the web view’s header in the specified rectangle.
- [func webView(WebView!, drawFooterIn: NSRect)](webuidelegate/webview(_:drawfooterin:).md)
  Draws the web view’s footer in the specified rectangle.
### Constants
- [Menu Item Tags](menu-item-tags.md)
  Tags that define the types of default menu items passed to the [`webView(_:contextMenuItemsForElement:defaultMenuItems:)`](webuidelegate/webview(_:contextmenuitemsforelement:defaultmenuitems:).md) method.
- [struct WebDragDestinationAction](webdragdestinationaction.md)
  Actions that the destination object of a drag operation can perform.
- [struct WebDragSourceAction](webdragsourceaction.md)
  Actions that the source object of a drag operation can perform.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WebView](webview-swift.class.md)
  `WebView` is the core view class in the WebKit framework that manages interactions between the `WebFrame` and `WebFrameView` classes. To embed web content in your application, you just create a `WebView` object, attach it to a window, and send a [`load(_:)`](webframe/load(_:)-47p2s.md) message to its main frame.
- [class WebPreferences](webpreferences.md)
  WebPreferences encapsulates the preferences you can change per WebView object. These preferences include font, text encoding, and image settings. Normally a WebView object uses the standard preferences returned by the [`standard()`](webpreferences/standard().md) class method. However, you can modify the preferences for individual WebView instances too. Use the [`preferencesIdentifier`](webview-swift.class/preferencesidentifier.md) WebView method to change a WebView object’s preferences, or to share preferences between WebView objects. Use the [`autosaves`](webpreferences/autosaves.md) method to specify if the preferences object should be automatically saved to the user defaults database.
- [protocol WebEditingDelegate](webeditingdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate)*