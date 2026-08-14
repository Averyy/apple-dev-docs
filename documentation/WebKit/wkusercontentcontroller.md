# WKUserContentController

**Framework**: WebKit  
**Kind**: class

An object for managing interactions between JavaScript code and your web view, and for filtering content in your web view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKUserContentController
```

#### Overview

A [`WKUserContentController`](wkusercontentcontroller.md) object provides a bridge between your app and the JavaScript code running in the web view. Use this object to do the following:

- Inject JavaScript code into webpages running in your web view.
- Install custom JavaScript functions that call through to your app’s native code.
- Specify custom filters to prevent the webpage from loading restricted content.

Create and configure a [`WKUserContentController`](wkusercontentcontroller.md) object as part of your overall web view setup. Assign the object to the [`userContentController`](wkwebviewconfiguration/usercontentcontroller.md) property of your [`WKWebViewConfiguration`](wkwebviewconfiguration.md) object before creating your web view.

## Topics

### Adding and Removing Custom Scripts
- [func addUserScript(WKUserScript)](wkusercontentcontroller/adduserscript(_:).md)
  Injects the specified script into the webpage’s content.
- [func removeAllUserScripts()](wkusercontentcontroller/removealluserscripts.md)
  Removes all user scripts from the web view.
- [var userScripts: [WKUserScript]](wkusercontentcontroller/userscripts.md)
  The user scripts associated with the user content controller.
### Adding and Removing Message Handlers
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
- [protocol WKScriptMessageHandler](wkscriptmessagehandler.md)
  An interface for receiving messages from JavaScript code running in a webpage.
- [protocol WKScriptMessageHandlerWithReply](wkscriptmessagehandlerwithreply.md)
  An interface for responding to messages from JavaScript code running in a webpage.
### Adding and Removing Content Rules
- [func add(WKContentRuleList)](wkusercontentcontroller/add(_:).md)
  Adds the specified content rule list to the content controller object.
- [func remove(WKContentRuleList)](wkusercontentcontroller/remove(_:).md)
  Removes the specified rule list from the content controller object.
- [func removeAllContentRuleLists()](wkusercontentcontroller/removeallcontentrulelists.md)
  Removes all rules lists from the content controller.
- [class WKContentRuleList](wkcontentrulelist.md)
  A compiled list of rules to apply to web content.
### Initializers
- [init?(coder: NSCoder)](wkusercontentcontroller/init(coder:).md)
### Instance Methods
- [func addBuffer(RawSpan, name: String, to: WKContentWorld)](wkusercontentcontroller/addbuffer(_:name:to:).md)
  Adds a data buffer that will be available to JavaScript through the `window.webkit.buffers` object.
- [func removeBuffer(named: String, from: WKContentWorld)](wkusercontentcontroller/removebuffer(named:from:).md)
  Removes a previously added data buffer from the given `WKContentWorld`.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)

## See Also

- [class WKContentRuleListStore](wkcontentruleliststore.md)
  An object that contains the rules for how to load and filter content in the web view.
- [class WKContentWorld](wkcontentworld.md)
  An object that defines a scope of execution for JavaScript code, and which you use to prevent conflicts between different scripts.
- [class WKFrameInfo](wkframeinfo.md)
  An object that contains information about a frame on a webpage.
- [class WKSecurityOrigin](wksecurityorigin.md)
  An object that identifies the origin of a particular resource.
- [class WKUserScript](wkuserscript.md)
  A script that the web view injects into a webpage.
- [WKContentWorld.Configuration](wkcontentworld/configuration.md)
- [class WKJSHandle](wkjshandle.md)
  A WKJSHandle object contains a reference to a JavaScript object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller)*