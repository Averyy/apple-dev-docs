# WKWebExtensionWindow

**Framework**: WebKit  
**Kind**: protocol

A protocol with methods that represent a window to web extensions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
protocol WKWebExtensionWindow : NSObjectProtocol
```

## Topics

### Instance Methods
- [func activeTab(for: WKWebExtensionContext) -> (any WKWebExtensionTab)?](wkwebextensionwindow/activetab(for:).md)
  Called when the active tab is needed for the window.
- [func close(for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensionwindow/close(for:completionhandler:).md)
  Called to close the window.
- [func focus(for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensionwindow/focus(for:completionhandler:).md)
  Called to focus the window.
- [func frame(for: WKWebExtensionContext) -> CGRect](wkwebextensionwindow/frame(for:).md)
  Called when the frame of the window is needed.
- [func isPrivate(for: WKWebExtensionContext) -> Bool](wkwebextensionwindow/isprivate(for:).md)
  Called when the private state of the window is needed.
- [func screenFrame(for: WKWebExtensionContext) -> CGRect](wkwebextensionwindow/screenframe(for:).md)
  Called when the screen frame containing the window is needed.
- [func setFrame(CGRect, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensionwindow/setframe(_:for:completionhandler:).md)
  Called to set the frame of the window.
- [func setWindowState(WKWebExtension.WindowState, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensionwindow/setwindowstate(_:for:completionhandler:).md)
  Called to set the state of the window.
- [func tabs(for: WKWebExtensionContext) -> [any WKWebExtensionTab]](wkwebextensionwindow/tabs(for:).md)
  Called when the tabs are needed for the window.
- [func windowState(for: WKWebExtensionContext) -> WKWebExtension.WindowState](wkwebextensionwindow/windowstate(for:).md)
  Called when the state of the window is needed.
- [func windowType(for: WKWebExtensionContext) -> WKWebExtension.WindowType](wkwebextensionwindow/windowtype(for:).md)
  Called when the type of the window is needed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKWebExtension](wkwebextension.md)
  An object that encapsulates a web extension’s resources that the manifest file defines.
- [protocol WKWebExtensionTab](wkwebextensiontab.md)
  A protocol with methods that represent a tab to web extensions.
- [class WKWebExtensionContext](wkwebextensioncontext.md)
  An object that represents the runtime environment for a web extension.
- [class WKWebExtensionController](wkwebextensioncontroller.md)
  An object that manages a set of loaded extension contexts.
- [protocol WKWebExtensionControllerDelegate](wkwebextensioncontrollerdelegate.md)
  A group of methods you use to customize web extension interactions.
- [WKWebExtension.Action](wkwebextension/action.md)
  An object that encapsulates the properties for an individual web extension action.
- [WKWebExtension.Command](wkwebextension/command.md)
  An object that encapsulates the properties for an individual web extension command.
- [WKWebExtension.MatchPattern](wkwebextension/matchpattern.md)
  An object that represents a way to specify groups of URLs.
- [WKWebExtension.MessagePort](wkwebextension/messageport.md)
  An object that manages message-based communication with a web extension.
- [WKWebExtension.DataRecord](wkwebextension/datarecord.md)
  An object that represents a record of stored data for a specific web extension context.
- [WKWebExtension.TabConfiguration](wkwebextension/tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](wkwebextension/windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow)*