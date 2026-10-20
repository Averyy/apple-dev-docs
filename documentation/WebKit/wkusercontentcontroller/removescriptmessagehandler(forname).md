# removeScriptMessageHandler(forName:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Uninstalls the custom message handler with the specified name from your JavaScript code.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func removeScriptMessageHandler(forName name: String)
```

```objc
- (void) removeScriptMessageHandlerForName:(NSString *) name;
```

#### Discussion

Use this method to remove a message handler that you previously installed using the [`add(_:name:)`](./add%28_,name%29.md) method. This method removes the message handler from the page content world — that is, the content world available from the [`page`](../wkcontentworld/page.md) property of [`WKContentWorld`](../wkcontentworld.md). If you installed the message handler in a different content world, this method doesn’t remove it.

## Parameters

- `name`: The name of the message handler to remove. If no message handler with this name exists in the user content controller, this method does nothing.

## See Also

### Adding and Removing Message Handlers
- [func add(any WKScriptMessageHandler, name: String)](./add%28_,name%29.md)
  Installs a message handler that you can call from your JavaScript code.
- [func add(any WKScriptMessageHandler, contentWorld: WKContentWorld, name: String)](./add%28_,contentworld,name%29.md)
  Installs a message handler that you can call from the specified content world in your JavaScript code.
- [func addScriptMessageHandler(any WKScriptMessageHandlerWithReply, contentWorld: WKContentWorld, name: String)](./addscriptmessagehandler%28_,contentworld,name%29.md)
  Installs a message handler that returns a reply to your JavaScript code.
- [func removeScriptMessageHandler(forName: String, contentWorld: WKContentWorld)](./removescriptmessagehandler%28forname,contentworld%29.md)
  Uninstalls a custom message handler from the specified content world in your JavaScript code.
- [func removeAllScriptMessageHandlers(from: WKContentWorld)](./removeallscriptmessagehandlers%28from%29.md)
  Uninstalls all custom message handlers from the specified content world in your JavaScript code.
- [func removeAllScriptMessageHandlers()](./removeallscriptmessagehandlers%28%29.md)
  Uninstalls all custom message handlers associated with the user content controller.
- [protocol WKScriptMessageHandler](../wkscriptmessagehandler.md)
  An interface for receiving messages from JavaScript code running in a webpage.
- [protocol WKScriptMessageHandlerWithReply](../wkscriptmessagehandlerwithreply.md)
  An interface for responding to messages from JavaScript code running in a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/removescriptmessagehandler(forname:))*