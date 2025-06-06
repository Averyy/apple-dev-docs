# WKScriptMessageHandler

**Framework**: Webkit  
**Kind**: protocol

An interface for receiving messages from JavaScript code running in a webpage.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol WKScriptMessageHandler : NSObjectProtocol
```

#### Overview

Adopt the [`WKScriptMessageHandler`](wkscriptmessagehandler.md) protocol when your app needs a way to respond to JavaScript messages in the web view. When JavaScript code sends a message that specifically targets your message handler, WebKit calls your handler’s [`userContentController(_:didReceive:)`](wkscriptmessagehandler/usercontentcontroller(_:didreceive:).md) method. Use that method to implement your response. For example, you might update other parts of your app in response to web content changes.

To call your message handler from JavaScript, call the function `window.webkit.messageHandlers.``.postMessage(``)` in your code. You specify the value of  when you install your message handler in a [`WKUserContentController`](wkusercontentcontroller.md) object.

> **Note**:  If you want to provide a response back to JavaScript, implement your message handler using the [`WKScriptMessageHandlerWithReply`](wkscriptmessagehandlerwithreply.md) protocol instead.

## Topics

### Receiving Messages
- [func userContentController(WKUserContentController, didReceive: WKScriptMessage)](wkscriptmessagehandler/usercontentcontroller(_:didreceive:).md)
  Tells the handler that a webpage sent a script message.
- [class WKScriptMessage](wkscriptmessage.md)
  An object that encapsulates a message sent by JavaScript code from a webpage.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func add(any WKScriptMessageHandler, name: String)](wkusercontentcontroller/add(_:name:).md)
  Installs a message handler that you can call from your JavaScript code.
- [func add(any WKScriptMessageHandler, contentWorld: WKContentWorld, name: String)](wkusercontentcontroller/add(_:contentworld:name:).md)
  Installs a message handler that you can call from the specified content world in your JavaScript code.
- [func addScriptMessageHandler(any WKScriptMessageHandlerWithReply, contentWorld: WKContentWorld, name: String)](wkusercontentcontroller/addscriptmessagehandler(_:contentworld:name:).md)
  Installs a message handler that returns a reply to your JavaScript code.
- [func removeScriptMessageHandler(forName: String)](wkusercontentcontroller/removescriptmessagehandler(forname:).md)
  Uninstalls the custom message handler with the specified name from your JavaScript code.
- [func removeScriptMessageHandler(forName: String, contentWorld: WKContentWorld)](wkusercontentcontroller/removescriptmessagehandler(forname:contentworld:).md)
  Uninstalls a custom message handler from the specified content world in your JavaScript code.
- [func removeAllScriptMessageHandlers(from: WKContentWorld)](wkusercontentcontroller/removeallscriptmessagehandlers(from:).md)
  Uninstalls all custom message handlers from the specified content world in your JavaScript code.
- [func removeAllScriptMessageHandlers()](wkusercontentcontroller/removeallscriptmessagehandlers.md)
  Uninstalls all custom message handlers associated with the user content controller.
- [protocol WKScriptMessageHandlerWithReply](wkscriptmessagehandlerwithreply.md)
  An interface for responding to messages from JavaScript code running in a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WebKit/wkscriptmessagehandler)*