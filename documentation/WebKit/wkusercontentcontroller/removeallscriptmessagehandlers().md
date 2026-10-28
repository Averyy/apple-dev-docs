# removeAllScriptMessageHandlers()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Uninstalls all custom message handlers associated with the user content controller.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeAllScriptMessageHandlers()
```

```objc
- (void) removeAllScriptMessageHandlers;
```

## Discussion

Use this method to remove all message handlers in all content worlds in your JavaScript code.

## See Also

### Adding and Removing Message Handlers
- [func add(any WKScriptMessageHandler, name: String)](./add%28_,name%29.md)
  Installs a message handler that you can call from your JavaScript code.
- [func add(any WKScriptMessageHandler, contentWorld: WKContentWorld, name: String)](./add%28_,contentworld,name%29.md)
  Installs a message handler that you can call from the specified content world in your JavaScript code.
- [func addScriptMessageHandler(any WKScriptMessageHandlerWithReply, contentWorld: WKContentWorld, name: String)](./addscriptmessagehandler%28_,contentworld,name%29.md)
  Installs a message handler that returns a reply to your JavaScript code.
- [func removeScriptMessageHandler(forName: String)](./removescriptmessagehandler%28forname%29.md)
  Uninstalls the custom message handler with the specified name from your JavaScript code.
- [func removeScriptMessageHandler(forName: String, contentWorld: WKContentWorld)](./removescriptmessagehandler%28forname,contentworld%29.md)
  Uninstalls a custom message handler from the specified content world in your JavaScript code.
- [func removeAllScriptMessageHandlers(from: WKContentWorld)](./removeallscriptmessagehandlers%28from%29.md)
  Uninstalls all custom message handlers from the specified content world in your JavaScript code.
- [protocol WKScriptMessageHandler](../wkscriptmessagehandler.md)
  An interface for receiving messages from JavaScript code running in a webpage.
- [protocol WKScriptMessageHandlerWithReply](../wkscriptmessagehandlerwithreply.md)
  An interface for responding to messages from JavaScript code running in a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/removeallscriptmessagehandlers())*