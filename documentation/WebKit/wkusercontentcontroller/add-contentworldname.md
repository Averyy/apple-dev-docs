# add(_:contentWorld:name:)

**Framework**: Webkit  
**Kind**: method

Installs a message handler that you can call from the specified content world in your JavaScript code.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func add(_ scriptMessageHandler: any WKScriptMessageHandler, contentWorld world: WKContentWorld, name: String)
```

#### Discussion

To execute your handler’s code, call the JavaScript function that this method defines. You may pass a parameter value to the method. The user content controller packages that value into an appropriate type and delivers it to your content handler’s delegate method.

## Parameters

- `scriptMessageHandler`: The message handler object that implements your custom code. This object must adopt the   protocol.
- `world`: The content world in which to install the message handler. Use the content world to scope your message handler to specific parts of your JavaScript code.
- `name`: The user content controller uses this parameter to define a JavaScript function for your message handler in all frames in the specified content world. The name of this function is  , where   corresponds to the value of this parameter.  For example, if you specify the string  , the user content controller defines the   function in JavaScript.

## See Also

- [func add(any WKScriptMessageHandler, name: String)](wkusercontentcontroller/add(_:name:).md)
  Installs a message handler that you can call from your JavaScript code.
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
- [protocol WKScriptMessageHandler](wkscriptmessagehandler.md)
  An interface for receiving messages from JavaScript code running in a webpage.
- [protocol WKScriptMessageHandlerWithReply](wkscriptmessagehandlerwithreply.md)
  An interface for responding to messages from JavaScript code running in a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/add(_:contentworld:name:))*