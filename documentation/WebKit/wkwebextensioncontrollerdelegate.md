# WKWebExtensionControllerDelegate

**Framework**: Webkit  
**Kind**: protocol

A group of methods you use to customize web extension interactions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
protocol WKWebExtensionControllerDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func webExtensionController(WKWebExtensionController, connectUsing: WKWebExtension.MessagePort, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensioncontrollerdelegate/webextensioncontroller(_:connectusing:for:completionhandler:).md)
  Called when an extension context wants to establish a persistent connection to an application.
- [func webExtensionController(WKWebExtensionController, didUpdate: WKWebExtension.Action, forExtensionContext: WKWebExtensionContext)](wkwebextensioncontrollerdelegate/webextensioncontroller(_:didupdate:forextensioncontext:).md)
  Called when an action’s properties are updated.
- [func webExtensionController(WKWebExtensionController, focusedWindowFor: WKWebExtensionContext) -> (any WKWebExtensionWindow)?](wkwebextensioncontrollerdelegate/webextensioncontroller(_:focusedwindowfor:).md)
  Called when an extension context requests the currently focused window.
- [func webExtensionController(WKWebExtensionController, openNewTabUsing: WKWebExtension.TabConfiguration, for: WKWebExtensionContext, completionHandler: ((any WKWebExtensionTab)?, (any Error)?) -> Void)](wkwebextensioncontrollerdelegate/webextensioncontroller(_:opennewtabusing:for:completionhandler:).md)
  Called when an extension context requests a new tab to be opened.
- [func webExtensionController(WKWebExtensionController, openNewWindowUsing: WKWebExtension.WindowConfiguration, for: WKWebExtensionContext, completionHandler: ((any WKWebExtensionWindow)?, (any Error)?) -> Void)](wkwebextensioncontrollerdelegate/webextensioncontroller(_:opennewwindowusing:for:completionhandler:).md)
  Called when an extension context requests a new window to be opened.
- [func webExtensionController(WKWebExtensionController, openOptionsPageFor: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensioncontrollerdelegate/webextensioncontroller(_:openoptionspagefor:completionhandler:).md)
  Called when an extension context requests its options page to be opened.
- [func webExtensionController(WKWebExtensionController, openWindowsFor: WKWebExtensionContext) -> [any WKWebExtensionWindow]](wkwebextensioncontrollerdelegate/webextensioncontroller(_:openwindowsfor:).md)
  Called when an extension context requests the list of ordered open windows.
- [func webExtensionController(WKWebExtensionController, presentActionPopup: WKWebExtension.Action, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensioncontrollerdelegate/webextensioncontroller(_:presentactionpopup:for:completionhandler:).md)
  Called when a popup is requested to be displayed for a specific action.
- [func webExtensionController(WKWebExtensionController, promptForPermissionMatchPatterns: Set<WKWebExtension.MatchPattern>, in: (any WKWebExtensionTab)?, for: WKWebExtensionContext, completionHandler: (Set<WKWebExtension.MatchPattern>, Date?) -> Void)](wkwebextensioncontrollerdelegate/webextensioncontroller(_:promptforpermissionmatchpatterns:in:for:completionhandler:).md)
  Called when an extension context requests access to a set of match patterns.
- [func webExtensionController(WKWebExtensionController, promptForPermissionToAccess: Set<URL>, in: (any WKWebExtensionTab)?, for: WKWebExtensionContext, completionHandler: (Set<URL>, Date?) -> Void)](wkwebextensioncontrollerdelegate/webextensioncontroller(_:promptforpermissiontoaccess:in:for:completionhandler:).md)
  Called when an extension context requests access to a set of URLs.
- [func webExtensionController(WKWebExtensionController, promptForPermissions: Set<WKWebExtension.Permission>, in: (any WKWebExtensionTab)?, for: WKWebExtensionContext, completionHandler: (Set<WKWebExtension.Permission>, Date?) -> Void)](wkwebextensioncontrollerdelegate/webextensioncontroller(_:promptforpermissions:in:for:completionhandler:).md)
  Called when an extension context requests permissions.
- [func webExtensionController(WKWebExtensionController, sendMessage: Any, toApplicationWithIdentifier: String?, for: WKWebExtensionContext, replyHandler: (Any?, (any Error)?) -> Void)](wkwebextensioncontrollerdelegate/webextensioncontroller(_:sendmessage:toapplicationwithidentifier:for:replyhandler:).md)
  Called when an extension context wants to send a one-time message to an application.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKWebExtension](wkwebextension.md)
  An object that encapsulates a web extension’s resources that the manifest file defines.
- [protocol WKWebExtensionTab](wkwebextensiontab.md)
  A protocol with methods that represent a tab to web extensions.
- [protocol WKWebExtensionWindow](wkwebextensionwindow.md)
  A protocol with methods that represent a window to web extensions.
- [class WKWebExtensionContext](wkwebextensioncontext.md)
  An object that represents the runtime environment for a web extension.
- [class WKWebExtensionController](wkwebextensioncontroller.md)
  An object that manages a set of loaded extension contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontrollerdelegate)*