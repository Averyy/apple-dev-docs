# WKScriptMessageHandler

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

An interface for receiving messages from JavaScript code running in a webpage.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
@MainActor
protocol WKScriptMessageHandler : NSObjectProtocol
```

```objc
@protocol WKScriptMessageHandler <NSObject>
```

## Overview

Adopt the [`WKScriptMessageHandler`](./wkscriptmessagehandler.md) protocol when your app needs a way to respond to JavaScript messages in the web view. When JavaScript code sends a message that specifically targets your message handler, WebKit calls your handler’s [`userContentController(_:didReceive:)`](./wkscriptmessagehandler/usercontentcontroller%28_,didreceive%29.md) method. Use that method to implement your response. For example, you might update other parts of your app in response to web content changes.

To call your message handler from JavaScript, call the function `window.webkit.messageHandlers.<messageHandlerName>.postMessage(<messageBody>)` in your code. You specify the value of `<messageHandlerName>` when you install your message handler in a [`WKUserContentController`](./wkusercontentcontroller.md) object.

> **Note**:  If you want to provide a response back to JavaScript, implement your message handler using the [`WKScriptMessageHandlerWithReply`](./wkscriptmessagehandlerwithreply.md) protocol instead.

## Topics

### Receiving Messages
- [func userContentController(WKUserContentController, didReceive: WKScriptMessage)](./wkscriptmessagehandler/usercontentcontroller%28_,didreceive%29.md)
  Tells the handler that a webpage sent a script message.
- [class WKScriptMessage](./wkscriptmessage.md)
  An object that encapsulates a message sent by JavaScript code from a webpage.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Adding and Removing Message Handlers
- [func add(any WKScriptMessageHandler, name: String)](./wkusercontentcontroller/add%28_,name%29.md)
  Installs a message handler that you can call from your JavaScript code.
- [func add(any WKScriptMessageHandler, contentWorld: WKContentWorld, name: String)](./wkusercontentcontroller/add%28_,contentworld,name%29.md)
  Installs a message handler that you can call from the specified content world in your JavaScript code.
- [func addScriptMessageHandler(any WKScriptMessageHandlerWithReply, contentWorld: WKContentWorld, name: String)](./wkusercontentcontroller/addscriptmessagehandler%28_,contentworld,name%29.md)
  Installs a message handler that returns a reply to your JavaScript code.
- [func removeScriptMessageHandler(forName: String)](./wkusercontentcontroller/removescriptmessagehandler%28forname%29.md)
  Uninstalls the custom message handler with the specified name from your JavaScript code.
- [func removeScriptMessageHandler(forName: String, contentWorld: WKContentWorld)](./wkusercontentcontroller/removescriptmessagehandler%28forname,contentworld%29.md)
  Uninstalls a custom message handler from the specified content world in your JavaScript code.
- [func removeAllScriptMessageHandlers(from: WKContentWorld)](./wkusercontentcontroller/removeallscriptmessagehandlers%28from%29.md)
  Uninstalls all custom message handlers from the specified content world in your JavaScript code.
- [func removeAllScriptMessageHandlers()](./wkusercontentcontroller/removeallscriptmessagehandlers%28%29.md)
  Uninstalls all custom message handlers associated with the user content controller.
- [protocol WKScriptMessageHandlerWithReply](./wkscriptmessagehandlerwithreply.md)
  An interface for responding to messages from JavaScript code running in a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkscriptmessagehandler)*