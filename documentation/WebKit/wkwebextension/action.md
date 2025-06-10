# WKWebExtension.Action

**Framework**: WebKit  
**Kind**: class

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

#### Overview

This class provides access to action properties, such as pop-up, icon, or title, with tab-specific values.

## Topics

### Instance Properties
- [var associatedTab: (any WKWebExtensionTab)?](wkwebextension/action/associatedtab.md)
  The tab that this action is associated with, or `nil` if it’s the default action.
- [var badgeText: String](wkwebextension/action/badgetext.md)
  The badge text for the action.
- [var hasUnreadBadgeText: Bool](wkwebextension/action/hasunreadbadgetext.md)
  A Boolean value indicating whether the badge text is unread.
- [var inspectionName: String?](wkwebextension/action/inspectionname.md)
  The name shown when inspecting the pop-up web view.
- [var isEnabled: Bool](wkwebextension/action/isenabled.md)
  A Boolean value indicating whether the action is enabled.
- [var label: String](wkwebextension/action/label.md)
  The localized display label for the action.
- [var menuItems: [UIMenuElement]](wkwebextension/action/menuitems.md)
  The menu items provided by the extension for this action.
- [var popupPopover: NSPopover?](wkwebextension/action/popuppopover.md)
  A popover that presents a web view loaded with the pop-up page for this action, or `nil` if no popup is specified.
- [var popupViewController: UIViewController?](wkwebextension/action/popupviewcontroller.md)
  A view controller that presents a web view loaded with the pop-up page for this action, or `nil` if no popup is specified.
- [var popupWebView: WKWebView?](wkwebextension/action/popupwebview.md)
  A web view loaded with the pop-up page for this action, or `nil` if no pop-up is specified.
- [var presentsPopup: Bool](wkwebextension/action/presentspopup.md)
  A Boolean value indicating whether the action has a pop-up.
- [var webExtensionContext: WKWebExtensionContext?](wkwebextension/action/webextensioncontext.md)
  The extension context to which this action is related.
### Instance Methods
- [func closePopup()](wkwebextension/action/closepopup.md)
  Triggers the dismissal process of the pop-up.
- [func icon(for: CGSize) -> UIImage?](wkwebextension/action/icon(for:).md)
  Returns the action icon for the specified size.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [WKWebExtension.Command](wkwebextension/command.md)
  An object that encapsulates the properties for an individual web extension command.
- [WKWebExtension.DataRecord](wkwebextension/datarecord.md)
  An object that represents a record of stored data for a specific web extension context.
- [WKWebExtension.MatchPattern](wkwebextension/matchpattern.md)
  An object that represents a way to specify groups of URLs.
- [WKWebExtension.MessagePort](wkwebextension/messageport.md)
  An object that manages message-based communication with a web extension.
- [WKWebExtension.TabConfiguration](wkwebextension/tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](wkwebextension/windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/action)*