# WKWebExtension.WindowConfiguration

**Framework**: Webkit  
**Kind**: class

An object that encapsulates configuration options for a window in an extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class WindowConfiguration
```

#### Overview

This class holds various options that influence the behavior and initial state of a window.

The app retains the discretion to disregard any or all of these options, or even opt not to create a window.

## Topics

### Instance Properties
- [var frame: CGRect](wkwebextension/windowconfiguration/frame.md)
  Indicates the frame where the window should be positioned on the main screen.
- [var shouldBeFocused: Bool](wkwebextension/windowconfiguration/shouldbefocused.md)
  Indicates whether the window should be focused.
- [var shouldBePrivate: Bool](wkwebextension/windowconfiguration/shouldbeprivate.md)
  Indicates whether the window should be private.
- [var tabURLs: [URL]](wkwebextension/windowconfiguration/taburls.md)
  Indicates the URLs that the window should initially load as tabs.
- [var tabs: [any WKWebExtensionTab]](wkwebextension/windowconfiguration/tabs.md)
  Indicates the existing tabs that should be moved to the window.
- [var windowState: WKWebExtension.WindowState](wkwebextension/windowconfiguration/windowstate.md)
  Indicates the window state for the window.
- [var windowType: WKWebExtension.WindowType](wkwebextension/windowconfiguration/windowtype.md)
  Indicates the window type for the window.

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
- [WKWebExtensionController.Configuration](wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/windowconfiguration)*