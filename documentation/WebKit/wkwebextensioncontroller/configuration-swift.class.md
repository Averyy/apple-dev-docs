# WKWebExtensionController.Configuration

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

A [`WKWebExtensionController.Configuration`](./configuration-swift.class.md) object with which to initialize a web extension controller.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class Configuration
```

```objc
@interface WKWebExtensionControllerConfiguration : NSObject
```

#### Overview

Contains properties used to configure a [`WKWebExtensionController`](../wkwebextensioncontroller.md).

## Topics

### Initializers
- [init?(coder: NSCoder)](./configuration-swift.class/init%28coder%29.md)
- [convenience init(identifier: UUID)](./configuration-swift.class/init%28identifier%29.md)
  Returns a new configuration that is persistent and unique for the specified identifier.
### Instance Properties
- [var defaultWebsiteDataStore: WKWebsiteDataStore!](./configuration-swift.class/defaultwebsitedatastore.md)
  The default data store for website data and cookie access in extension contexts.
- [var identifier: UUID?](./configuration-swift.class/identifier.md)
  The unique identifier used for persistent configuration storage, or `nil` when it is the default or not persistent.
- [var isPersistent: Bool](./configuration-swift.class/ispersistent.md)
  A Boolean value indicating if this context will write data to the the file system.
- [var webViewConfiguration: WKWebViewConfiguration!](./configuration-swift.class/webviewconfiguration.md)
  The web view configuration to be used as a basis for configuring web views in extension contexts.
### Type Methods
- [class func `default`() -> Self](./configuration-swift.class/default%28%29.md)
  Returns a new default configuration that is persistent and not unique.
- [class func nonPersistent() -> Self](./configuration-swift.class/nonpersistent%28%29.md)
  Returns a new non-persistent configuration.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
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
- [WKWebExtension.Action](../wkwebextension/action.md)
  An object that encapsulates the properties for an individual web extension action.
- [WKWebExtension.Command](../wkwebextension/command.md)
  An object that encapsulates the properties for an individual web extension command.
- [WKWebExtension.MatchPattern](../wkwebextension/matchpattern.md)
  An object that represents a way to specify groups of URLs.
- [WKWebExtension.MessagePort](../wkwebextension/messageport.md)
  An object that manages message-based communication with a web extension.
- [WKWebExtension.DataRecord](../wkwebextension/datarecord.md)
  An object that represents a record of stored data for a specific web extension context.
- [WKWebExtension.TabConfiguration](../wkwebextension/tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](../wkwebextension/windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/configuration-swift.class)*