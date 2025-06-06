# WKWebExtension.Command

**Framework**: Webkit  
**Kind**: class

An object that encapsulates the properties for an individual web extension command.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class Command
```

#### Overview

Provides access to command properties such as a unique identifier, a descriptive title, and shortcut keys. Commands can be used by a web extension to perform specific actions within a web extension context, such toggling features, or interacting with web content. These commands enhance the functionality of the extension by allowing users to invoke actions quickly.

## Topics

### Instance Properties
- [var activationKey: String?](wkwebextension/command/activationkey.md)
  The primary key used to trigger the command, distinct from any modifier flags.
- [var id: String](wkwebextension/command/id.md)
  A unique identifier for the command.
- [var keyCommand: UIKeyCommand?](wkwebextension/command/keycommand.md)
  A key command representation of the web extension command for use in the responder chain.
- [var menuItem: UIMenuElement](wkwebextension/command/menuitem.md)
  A menu item representation of the web extension command for use in menus.
- [var modifierFlags: UIKeyModifierFlags](wkwebextension/command/modifierflags.md)
  The modifier flags used with the activation key to trigger the command.
- [var title: String](wkwebextension/command/title.md)
  A descriptive title for the command to help discoverability.
- [var webExtensionContext: WKWebExtensionContext?](wkwebextension/command/webextensioncontext.md)
  The web extension context associated with the command.

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

- [WKWebExtension.Action](wkwebextension/action.md)
  An object that encapsulates the properties for an individual web extension action.
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/command)*