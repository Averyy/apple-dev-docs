# WebEditingDelegate

**Framework**: WebKit  
**Kind**: protocol

**Availability**:
- macOS 10.3+

## Declaration

```swift
protocol WebEditingDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func undoManager(for: WebView!) -> UndoManager!](webeditingdelegate/undomanager(for:).md)
  Returns the undo manager to be used by a web view.
- [func webView(WebView!, doCommandBy: Selector!) -> Bool](webeditingdelegate/webview(_:docommandby:).md)
  Returns whether the receiver performs a command instead of the web view.
- [func webView(WebView!, shouldApplyStyle: DOMCSSStyleDeclaration!, toElementsIn: DOMRange!) -> Bool](webeditingdelegate/webview(_:shouldapplystyle:toelementsin:).md)
  Returns whether the user should be allowed to apply a style to a range of content.
- [func webView(WebView!, shouldBeginEditingIn: DOMRange!) -> Bool](webeditingdelegate/webview(_:shouldbegineditingin:).md)
  Returns whether the user is allowed to edit a range of content in a web view.
- [func webView(WebView!, shouldChangeSelectedDOMRange: DOMRange!, to: DOMRange!, affinity: NSSelectionAffinity, stillSelecting: Bool) -> Bool](webeditingdelegate/webview(_:shouldchangeselecteddomrange:to:affinity:stillselecting:).md)
  Returns whether the user should be allowed to change the selected range.
- [func webView(WebView!, shouldChangeTypingStyle: DOMCSSStyleDeclaration!, toStyle: DOMCSSStyleDeclaration!) -> Bool](webeditingdelegate/webview(_:shouldchangetypingstyle:tostyle:).md)
  Returns whether the user should be allowed to change the typing style in a web view.
- [func webView(WebView!, shouldDelete: DOMRange!) -> Bool](webeditingdelegate/webview(_:shoulddelete:).md)
  Returns whether the user should be allowed to delete a range of content.
- [func webView(WebView!, shouldEndEditingIn: DOMRange!) -> Bool](webeditingdelegate/webview(_:shouldendeditingin:).md)
  Returns whether the user should be allowed to end editing.
- [func webView(WebView!, shouldInsert: DOMNode!, replacing: DOMRange!, given: WebViewInsertAction) -> Bool](webeditingdelegate/webview(_:shouldinsert:replacing:given:).md)
  Returns whether the user should be allowed to insert a node in place of a range of content.
- [func webView(WebView!, shouldInsertText: String!, replacing: DOMRange!, given: WebViewInsertAction) -> Bool](webeditingdelegate/webview(_:shouldinserttext:replacing:given:).md)
  Returns whether a user should be allowed to insert text in place of a range of content.
- [func webViewDidBeginEditing(Notification!)](webeditingdelegate/webviewdidbeginediting(_:).md)
  Sent by the default notification center when the user begins editing the web view.
- [func webViewDidChange(Notification!)](webeditingdelegate/webviewdidchange(_:).md)
  Sent by the default notification center when the user changes content in the web view.
- [func webViewDidChangeSelection(Notification!)](webeditingdelegate/webviewdidchangeselection(_:).md)
  Sent by the default notification center when the user changes the selection in the web view.
- [func webViewDidChangeTypingStyle(Notification!)](webeditingdelegate/webviewdidchangetypingstyle(_:).md)
  Sent by the default notification center when the user changes the typing style in the web view.
- [func webViewDidEndEditing(Notification!)](webeditingdelegate/webviewdidendediting(_:).md)
  Sent by the default notification center when the user stops editing the web view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WebPreferences](webpreferences.md)
  WebPreferences encapsulates the preferences you can change per WebView object. These preferences include font, text encoding, and image settings. Normally a WebView object uses the standard preferences returned by the [`standard()`](webpreferences/standard().md) class method. However, you can modify the preferences for individual WebView instances too. Use the [`preferencesIdentifier`](webview-swift.class/preferencesidentifier.md) WebView method to change a WebView object’s preferences, or to share preferences between WebView objects. Use the [`autosaves`](webpreferences/autosaves.md) method to specify if the preferences object should be automatically saved to the user defaults database.
- [protocol WebUIDelegate](webuidelegate.md)
  Web view user interface delegates implement this protocol to control the opening of new windows, augment the behavior of default menu items displayed when the user clicks elements, and perform other user interface–related tasks. These methods can be invoked as a result of handling JavaScript or other plug-in content. Delegates that display more than one web view per window, for example, need to implement some of these methods to handle that case. The default implementation assumes one window per web view, so non-conventional user interfaces might implement a user interface delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate)*