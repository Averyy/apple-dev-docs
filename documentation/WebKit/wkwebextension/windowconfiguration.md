# WKWebExtension.WindowConfiguration

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface WKWebExtensionWindowConfiguration : NSObject
```

## Overview

This class holds various options that influence the behavior and initial state of a window.

The app retains the discretion to disregard any or all of these options, or even opt not to create a window.

## Topics

### Instance Properties
- [var frame: CGRect](./windowconfiguration/frame.md)
  Indicates the frame where the window should be positioned on the main screen.
- [var shouldBeFocused: Bool](./windowconfiguration/shouldbefocused.md)
  Indicates whether the window should be focused.
- [var shouldBePrivate: Bool](./windowconfiguration/shouldbeprivate.md)
  Indicates whether the window should be private.
- [var tabURLs: [URL]](./windowconfiguration/taburls.md)
  Indicates the URLs that the window should initially load as tabs.
- [var tabs: [any WKWebExtensionTab]](./windowconfiguration/tabs.md)
  Indicates the existing tabs that should be moved to the window.
- [var windowState: WKWebExtension.WindowState](./windowconfiguration/windowstate.md)
  Indicates the window state for the window.
- [var windowType: WKWebExtension.WindowType](./windowconfiguration/windowtype.md)
  Indicates the window type for the window.

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
- [WKWebExtension.Action](./action.md)
  An object that encapsulates the properties for an individual web extension action.
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
- [WKWebExtensionController.Configuration](../wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](../wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/windowconfiguration)*