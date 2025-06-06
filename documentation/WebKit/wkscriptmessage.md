# WKScriptMessage

**Framework**: Webkit  
**Kind**: class

An object that encapsulates a message sent by JavaScript code from a webpage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKScriptMessage
```

#### Overview

Use a [`WKScriptMessage`](wkscriptmessage.md) object to get details about a JavaScript message sent to a custom message handler in your app. You don’t create [`WKScriptMessage`](wkscriptmessage.md) objects directly. When JavaScript code targets one of your app’s message handlers, the [`WKUserContentController`](wkusercontentcontroller.md) object of the web view creates a [`WKScriptMessage`](wkscriptmessage.md) object and delivers it to the message handler’s delegate method. Use the object you’re provided to process the message and provide an appropriate response.

For more information about handling script messages, see the [`WKScriptMessageHandler`](wkscriptmessagehandler.md) and [`WKScriptMessageHandlerWithReply`](wkscriptmessagehandlerwithreply.md) protocols. For information about how to register message handlers, see the methods of [`WKUserContentController`](wkusercontentcontroller.md).

## Topics

### Getting the Message Contents
- [var body: Any](wkscriptmessage/body.md)
  The body of the message.
### Getting Message-Related Information
- [var frameInfo: WKFrameInfo](wkscriptmessage/frameinfo.md)
  The frame that sent the message.
- [var webView: WKWebView?](wkscriptmessage/webview.md)
  The web view that sent the message.
- [var world: WKContentWorld](wkscriptmessage/world.md)
  The namespace in which the JavaScript code executes.
### Getting the Message Handler’s Name
- [var name: String](wkscriptmessage/name.md)
  The name of the message handler to which the message is sent.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func userContentController(WKUserContentController, didReceive: WKScriptMessage)](wkscriptmessagehandler/usercontentcontroller(_:didreceive:).md)
  Tells the handler that a webpage sent a script message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkscriptmessage)*