# WKWebExtension.TabConfiguration

**Framework**: WebKit  
**Kind**: class

An object that encapsulates configuration options for a tab in an extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class TabConfiguration
```

#### Overview

This class holds various options that influence the behavior and initial state of a tab.

The app retains the discretion to disregard any or all of these options, or even opt not to create a tab.

## Topics

### Instance Properties
- [var index: Int](wkwebextension/tabconfiguration/index.md)
  Indicates the position where the tab should be opened within the window.
- [var parentTab: (any WKWebExtensionTab)?](wkwebextension/tabconfiguration/parenttab.md)
  Indicates the parent tab with which the tab should be related.
- [var shouldAddToSelection: Bool](wkwebextension/tabconfiguration/shouldaddtoselection.md)
  Indicates whether the tab should be added to the current tab selection.
- [var shouldBeActive: Bool](wkwebextension/tabconfiguration/shouldbeactive.md)
  Indicates whether the tab should be the active tab.
- [var shouldBeMuted: Bool](wkwebextension/tabconfiguration/shouldbemuted.md)
  Indicates whether the tab should be muted.
- [var shouldBePinned: Bool](wkwebextension/tabconfiguration/shouldbepinned.md)
  Indicates whether the tab should be pinned.
- [var shouldReaderModeBeActive: Bool](wkwebextension/tabconfiguration/shouldreadermodebeactive.md)
  Indicates whether reader mode in the tab should be active.
- [var url: URL?](wkwebextension/tabconfiguration/url.md)
  Indicates the initial URL for the tab.
- [var window: (any WKWebExtensionWindow)?](wkwebextension/tabconfiguration/window.md)
  Indicates the window where the tab should be opened.

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
- [WKWebExtension.WindowConfiguration](wkwebextension/windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/tabconfiguration)*