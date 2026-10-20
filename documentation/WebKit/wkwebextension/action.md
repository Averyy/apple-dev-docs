# WKWebExtension.Action

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

An object that encapsulates the properties for an individual web extension action.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class Action
```

```objc
@interface WKWebExtensionAction : NSObject
```

#### Overview

This class provides access to action properties, such as pop-up, icon, or title, with tab-specific values.

## Topics

### Instance Properties
- [var associatedTab: (any WKWebExtensionTab)?](./action/associatedtab.md)
  The tab that this action is associated with, or `nil` if it’s the default action.
- [var badgeText: String](./action/badgetext.md)
  The badge text for the action.
- [var hasUnreadBadgeText: Bool](./action/hasunreadbadgetext.md)
  A Boolean value indicating whether the badge text is unread.
- [var inspectionName: String?](./action/inspectionname.md)
  The name shown when inspecting the pop-up web view.
- [var isEnabled: Bool](./action/isenabled.md)
  A Boolean value indicating whether the action is enabled.
- [var label: String](./action/label.md)
  The localized display label for the action.
- [var menuItems: [UIMenuElement]](./action/menuitems.md)
  The menu items provided by the extension for this action.
- [var popupPopover: NSPopover?](./action/popuppopover.md)
  A popover that presents a web view loaded with the pop-up page for this action, or `nil` if no popup is specified.
- [var popupViewController: UIViewController?](./action/popupviewcontroller.md)
  A view controller that presents a web view loaded with the pop-up page for this action, or `nil` if no popup is specified.
- [var popupWebView: WKWebView?](./action/popupwebview.md)
  A web view loaded with the pop-up page for this action, or `nil` if no pop-up is specified.
- [var presentsPopup: Bool](./action/presentspopup.md)
  A Boolean value indicating whether the action has a pop-up.
- [var webExtensionContext: WKWebExtensionContext?](./action/webextensioncontext.md)
  The extension context to which this action is related.
### Instance Methods
- [func closePopup()](./action/closepopup%28%29.md)
  Triggers the dismissal process of the pop-up.
- [func icon(for: CGSize) -> UIImage?](./action/icon%28for%29.md)
  Returns the action icon for the specified size.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Web extensions
- [class WKWebExtension](../wkwebextension.md)
  An object that encapsulates a web extension’s resources that the manifest file defines.
- [protocol WKWebExtensionTab](../wkwebextensiontab.md)
  A protocol with methods that represent a tab to web extensions.
- [protocol WKWebExtensionWindow](../wkwebextensionwindow.md)
  A protocol with methods that represent a window to web extensions.
- [class WKWebExtensionContext](../wkwebextensioncontext.md)
  An object that represents the runtime environment for a web extension.
- [class WKWebExtensionController](../wkwebextensioncontroller.md)
  An object that manages a set of loaded extension contexts.
- [protocol WKWebExtensionControllerDelegate](../wkwebextensioncontrollerdelegate.md)
  A group of methods you use to customize web extension interactions.
- [WKWebExtension.Command](./command.md)
  An object that encapsulates the properties for an individual web extension command.
- [WKWebExtension.MatchPattern](./matchpattern.md)
  An object that represents a way to specify groups of URLs.
- [WKWebExtension.MessagePort](./messageport.md)
  An object that manages message-based communication with a web extension.
- [WKWebExtension.DataRecord](./datarecord.md)
  An object that represents a record of stored data for a specific web extension context.
- [WKWebExtension.TabConfiguration](./tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](./windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](../wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](../wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/action)*