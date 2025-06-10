# removeScriptMessageHandler(forName:contentWorld:)

**Framework**: WebKit  
**Kind**: method

Uninstalls a custom message handler from the specified content world in your JavaScript code.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeScriptMessageHandler(forName name: String, contentWorld: WKContentWorld)
```

## Parameters

- `name`: The name of the message handler to remove. If no message handler with this name exists in the user content controller, this method does nothing.
- `contentWorld`: The content world from which to remove the message handler. For more information about content worlds, see  .

## See Also

- [func add(any WKScriptMessageHandler, name: String)](wkusercontentcontroller/add(_:name:).md)
  Installs a message handler that you can call from your JavaScript code.
- [func add(any WKScriptMessageHandler, contentWorld: WKContentWorld, name: String)](wkusercontentcontroller/add(_:contentworld:name:).md)
  Installs a message handler that you can call from the specified content world in your JavaScript code.
- [func addScriptMessageHandler(any WKScriptMessageHandlerWithReply, contentWorld: WKContentWorld, name: String)](wkusercontentcontroller/addscriptmessagehandler(_:contentworld:name:).md)
  Installs a message handler that returns a reply to your JavaScript code.
- [func removeScriptMessageHandler(forName: String)](wkusercontentcontroller/removescriptmessagehandler(forname:).md)
  Uninstalls the custom message handler with the specified name from your JavaScript code.
- [func removeAllScriptMessageHandlers(from: WKContentWorld)](wkusercontentcontroller/removeallscriptmessagehandlers(from:).md)
  Uninstalls all custom message handlers from the specified content world in your JavaScript code.
- [func removeAllScriptMessageHandlers()](wkusercontentcontroller/removeallscriptmessagehandlers.md)
  Uninstalls all custom message handlers associated with the user content controller.
- [protocol WKScriptMessageHandler](wkscriptmessagehandler.md)
  An interface for receiving messages from JavaScript code running in a webpage.
- [protocol WKScriptMessageHandlerWithReply](wkscriptmessagehandlerwithreply.md)
  An interface for responding to messages from JavaScript code running in a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/removescriptmessagehandler(forname:contentworld:))*