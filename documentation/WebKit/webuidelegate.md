# WebUIDelegate

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

Web view user interface delegates implement this protocol to control the opening of new windows, augment the behavior of default menu items displayed when the user clicks elements, and perform other user interface–related tasks. These methods can be invoked as a result of handling JavaScript or other plug-in content. Delegates that display more than one web view per window, for example, need to implement some of these methods to handle that case. The default implementation assumes one window per web view, so non-conventional user interfaces might implement a user interface delegate.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
protocol WebUIDelegate : NSObjectProtocol
```

```objc
@protocol WebUIDelegate <NSObject>
```

## Topics

### Creating and Closing Windows
- [func webView(WebView!, createWebViewModalDialogWith: URLRequest!) -> WebView!](./webuidelegate/webview%28_,createwebviewmodaldialogwith%29.md)
  Creates a modal window containing a web view that loads the specified request.
- [func webViewRunModal(WebView!)](./webuidelegate/webviewrunmodal%28_%29.md)
  Displays a web view in a modal window.
- [func webView(WebView!, createWebViewWith: URLRequest!) -> WebView!](./webuidelegate/webview%28_,createwebviewwith%29.md)
  Creates a window containing a web view to load the specified request.
- [func webViewClose(WebView!)](./webuidelegate/webviewclose%28_%29.md)
  Closes a web view in a window.
### Moving and Resizing Windows
- [func webViewIsResizable(WebView!) -> Bool](./webuidelegate/webviewisresizable%28_%29.md)
  Returns a Boolean value indicating whether a web view’s window can be resized.
- [func webView(WebView!, setResizable: Bool)](./webuidelegate/webview%28_,setresizable%29.md)
  Sets whether a web view’s window can be resized.
- [func webView(WebView!, setFrame: NSRect)](./webuidelegate/webview%28_,setframe%29.md)
  Sets the frame rectangle of a web view’s window to the specified frame size.
- [func webViewFrame(WebView!) -> NSRect](./webuidelegate/webviewframe%28_%29.md)
  Returns the frame rectangle of a web view’s window.
### Making Windows Key and Main
- [func webViewFocus(WebView!)](./webuidelegate/webviewfocus%28_%29.md)
  Brings a web view’s window to the front and makes it the active window.
- [func webViewUnfocus(WebView!)](./webuidelegate/webviewunfocus%28_%29.md)
  Relinquishes focus on a web view’s window.
### Ordering Windows
- [func webViewShow(WebView!)](./webuidelegate/webviewshow%28_%29.md)
  Displays a web view’s window and moves it to the front.
### Working with the Responder Chain
- [func webViewFirstResponder(WebView!) -> NSResponder!](./webuidelegate/webviewfirstresponder%28_%29.md)
  Returns the first responder of the web view’s window.
- [func webView(WebView!, makeFirstResponder: NSResponder!)](./webuidelegate/webview%28_,makefirstresponder%29.md)
  Sets the first responder of a web view’s window to the specified view.
### Handling Mouse Events
- [func webView(WebView!, mouseDidMoveOverElement: [AnyHashable : Any]!, modifierFlags: Int)](./webuidelegate/webview%28_,mousedidmoveoverelement,modifierflags%29.md)
  Updates information about the element the user is mousing over.
- [func webView(WebView!, contextMenuItemsForElement: [AnyHashable : Any]!, defaultMenuItems: [Any]!) -> [Any]!](./webuidelegate/webview%28_,contextmenuitemsforelement,defaultmenuitems%29.md)
  Returns menu items to display in an element’s contextual menu.
### Opening Panels
- [func webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedBy: WebFrame!)](./webuidelegate/webview%28_,runjavascriptalertpanelwithmessage,initiatedby%29.md)
  Displays a JavaScript alert panel containing the specified message.
- [func webView(WebView!, runJavaScriptConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](./webuidelegate/webview%28_,runjavascriptconfirmpanelwithmessage,initiatedby%29.md)
  Displays a JavaScript confirmation panel with the specified message.
- [func webView(WebView!, runJavaScriptTextInputPanelWithPrompt: String!, defaultText: String!, initiatedBy: WebFrame!) -> String!](./webuidelegate/webview%28_,runjavascripttextinputpanelwithprompt,defaulttext,initiatedby%29.md)
  Displays a JavaScript text input panel and returns the entered text.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!)](./webuidelegate/webview%28_,runopenpanelforfilebuttonwith%29.md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)](./webuidelegate/webview%28_,runopenpanelforfilebuttonwith,allowmultiplefiles%29.md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runBeforeUnloadConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](./webuidelegate/webview%28_,runbeforeunloadconfirmpanelwithmessage,initiatedby%29.md)
  Displays a confirmation panel containing the specified message before a window closes.
- [- webView:runJavaScriptAlertPanelWithMessage:](./webuidelegate/webview_runjavascriptalertpanelwithmessage_.md)
  Displays a JavaScript alert panel.
- [- webView:runJavaScriptConfirmPanelWithMessage:](./webuidelegate/webview_runjavascriptconfirmpanelwithmessage_.md)
  Displays a JavaScript confirm panel.
- [- webView:runJavaScriptTextInputPanelWithPrompt:defaultText:](./webuidelegate/webview_runjavascripttextinputpanelwithprompt_defaulttext_.md)
  Displays a JavaScript text input panel and returns the entered text.
### Displaying Status Messages
- [func webView(WebView!, setStatusText: String!)](./webuidelegate/webview%28_,setstatustext%29.md)
  Sets the status message displayed by a web view’s window, if any, to the specified text.
- [func webViewStatusText(WebView!) -> String!](./webuidelegate/webviewstatustext%28_%29.md)
  Returns the current status message from a web view’s window.
### Managing Toolbars and the Status Bar
- [func webViewAreToolbarsVisible(WebView!) -> Bool](./webuidelegate/webviewaretoolbarsvisible%28_%29.md)
  Returns a Boolean value indicating whether any toolbars are visible in a web view’s window.
- [func webView(WebView!, setToolbarsVisible: Bool)](./webuidelegate/webview%28_,settoolbarsvisible%29.md)
  Sets whether a web view’s toolbars should be visible.
- [func webViewIsStatusBarVisible(WebView!) -> Bool](./webuidelegate/webviewisstatusbarvisible%28_%29.md)
  Returns a Boolean value indicating whether the status bar in a web view’s window is visible.
- [func webView(WebView!, setStatusBarVisible: Bool)](./webuidelegate/webview%28_,setstatusbarvisible%29.md)
  Sets the visibility of the status bar in a web view’s window.
### Controlling Drag Behavior
- [func webView(WebView!, dragDestinationActionMaskFor: (any NSDraggingInfo)!) -> Int](./webuidelegate/webview%28_,dragdestinationactionmaskfor%29.md)
  Returns a mask indicating which drag operations are allowed by the sender.
- [func webView(WebView!, dragSourceActionMaskFor: NSPoint) -> Int](./webuidelegate/webview%28_,dragsourceactionmaskfor%29.md)
  Returns a mask indicating which drag-source actions are allowed for a drag that begins at the specified location.
- [func webView(WebView!, willPerform: WebDragDestinationAction, for: (any NSDraggingInfo)!)](./webuidelegate/webview%28_,willperform,for%29.md)
  Tells the receiver that the sending web view will perform the specified drag-destination action.
- [func webView(WebView!, willPerform: WebDragSourceAction, from: NSPoint, with: NSPasteboard!)](./webuidelegate/webview%28_,willperform,from,with%29.md)
  Tells the receiver that the sending web view will perform the specified drag-source action.
### Controlling Other Behaviors
- [func webView(WebView!, shouldPerformAction: Selector!, fromSender: Any!) -> Bool](./webuidelegate/webview%28_,shouldperformaction,fromsender%29.md)
  Returns a Boolean value that indicates whether the action sent by the specified object should be performed.
- [func webView(WebView!, validate: (any NSValidatedUserInterfaceItem)!, defaultValidation: Bool) -> Bool](./webuidelegate/webview%28_,validate,defaultvalidation%29.md)
  Returns a Boolean value that indicates whether the specified user interface item is valid.
### Printing
- [func webView(WebView!, print: WebFrameView!)](./webuidelegate/webview%28_,print%29.md)
  Prints the contents of a web frame view.
- [func webViewHeaderHeight(WebView!) -> Float](./webuidelegate/webviewheaderheight%28_%29.md)
  Returns the height of the web view’s printed page header.
- [func webViewFooterHeight(WebView!) -> Float](./webuidelegate/webviewfooterheight%28_%29.md)
  Returns the height of the web view’s printed page footer.
- [func webView(WebView!, drawHeaderIn: NSRect)](./webuidelegate/webview%28_,drawheaderin%29.md)
  Draws the web view’s header in the specified rectangle.
- [func webView(WebView!, drawFooterIn: NSRect)](./webuidelegate/webview%28_,drawfooterin%29.md)
  Draws the web view’s footer in the specified rectangle.
### Constants
- [Menu Item Tags](./menu-item-tags.md)
  Tags that define the types of default menu items passed to the [`webView(_:contextMenuItemsForElement:defaultMenuItems:)`](./webuidelegate/webview%28_,contextmenuitemsforelement,defaultmenuitems%29.md) method.
- [struct WebDragDestinationAction](./webdragdestinationaction.md)
  Actions that the destination object of a drag operation can perform.
- [struct WebDragSourceAction](./webdragsourceaction.md)
  Actions that the source object of a drag operation can perform.
### Moving and Resizing Content Views
- [- webView:setContentRect:](./webuidelegate/webview_setcontentrect_.md)
  Sets the window’s content view frame to the specified content rectangle.
- [- webViewContentRect:](./webuidelegate/webviewcontentrect_.md)
  Returns a web view window’s content rectangle.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting Up a Web View (Legacy)
- [class WebView](./webview-swift.class.md)
  `WebView` is the core view class in the WebKit framework that manages interactions between the `WebFrame` and `WebFrameView` classes. To embed web content in your application, you just create a `WebView` object, attach it to a window, and send a [`load(_:)`](./webframe/load%28_%29-47p2s.md) message to its main frame.
- [class WebPreferences](./webpreferences.md)
  WebPreferences encapsulates the preferences you can change per WebView object. These preferences include font, text encoding, and image settings. Normally a WebView object uses the standard preferences returned by the [`standard()`](./webpreferences/standard%28%29.md) class method. However, you can modify the preferences for individual WebView instances too. Use the [`preferencesIdentifier`](./webview-swift.class/preferencesidentifier.md) WebView method to change a WebView object’s preferences, or to share preferences between WebView objects. Use the [`autosaves`](./webpreferences/autosaves.md) method to specify if the preferences object should be automatically saved to the user defaults database.
- [protocol WebEditingDelegate](./webeditingdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate)*