# removeScriptMessageHandler(forName:contentWorld:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Uninstalls a custom message handler from the specified content world in your JavaScript code.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeScriptMessageHandler(forName name: String, contentWorld: WKContentWorld)
```

```objc
- (void) removeScriptMessageHandlerForName:(NSString *) name contentWorld:(WKContentWorld *) contentWorld;
```

## Parameters

- `name`: The name of the message handler to remove. If no message handler with this name exists in the user content controller, this method does nothing.
- `contentWorld`: The content world from which to remove the message handler. For more information about content worlds, see [`WKContentWorld`](../wkcontentworld.md).

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
- [func removeAllScriptMessageHandlers(from: WKContentWorld)](./removeallscriptmessagehandlers%28from%29.md)
  Uninstalls all custom message handlers from the specified content world in your JavaScript code.
- [func removeAllScriptMessageHandlers()](./removeallscriptmessagehandlers%28%29.md)
  Uninstalls all custom message handlers associated with the user content controller.
- [protocol WKScriptMessageHandler](../wkscriptmessagehandler.md)
  An interface for receiving messages from JavaScript code running in a webpage.
- [protocol WKScriptMessageHandlerWithReply](../wkscriptmessagehandlerwithreply.md)
  An interface for responding to messages from JavaScript code running in a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/removescriptmessagehandler(forname:contentworld:))*