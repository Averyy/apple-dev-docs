# webExtensionController(_:sendMessage:toApplicationWithIdentifier:for:replyHandler:)

**Framework**: WebKit  
**Kind**: method

Called when an extension context wants to send a one-time message to an application.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func webExtensionController(_ controller: WKWebExtensionController, sendMessage message: Any, toApplicationWithIdentifier applicationIdentifier: String?, for extensionContext: WKWebExtensionContext) async throws -> Any?
```

#### Discussion

This method should be implemented by the app to handle one-off messages to applications.

If not implemented, the default behavior is to pass the message to the app extension handler within the extension’s bundle, if the extension was loaded from an app extension bundle; otherwise, no action is performed if not implemented.

> **Note**: The reply message must be JSON-serializable according to [`JSONSerialization`](https://developer.apple.com/documentation/Foundation/JSONSerialization).

## Parameters

- `controller`: The web extension controller that is managing the extension.
- `message`: The message to be sent.
- `applicationIdentifier`: The unique identifier for the application, or \c nil if none was specified.
- `extensionContext`: The context in which the web extension is running.
- `replyHandler`: A block to be called with a JSON-serializable reply message or an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontrollerdelegate/webextensioncontroller(_:sendmessage:toapplicationwithidentifier:for:replyhandler:))*