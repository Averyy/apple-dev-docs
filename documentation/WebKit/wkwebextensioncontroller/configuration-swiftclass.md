# WKWebExtensionController.Configuration

**Framework**: WebKit  
**Kind**: class

A [`WKWebExtensionController.Configuration`](wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.

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

#### Overview

Contains properties used to configure a [`WKWebExtensionController`](wkwebextensioncontroller.md).

## Topics

### Initializers
- [convenience init(identifier: UUID)](wkwebextensioncontroller/configuration-swift.class/init(identifier:).md)
  Returns a new configuration that is persistent and unique for the specified identifier.
### Instance Properties
- [var defaultWebsiteDataStore: WKWebsiteDataStore!](wkwebextensioncontroller/configuration-swift.class/defaultwebsitedatastore.md)
  The default data store for website data and cookie access in extension contexts.
- [var identifier: UUID?](wkwebextensioncontroller/configuration-swift.class/identifier.md)
  The unique identifier used for persistent configuration storage, or `nil` when it is the default or not persistent.
- [var isPersistent: Bool](wkwebextensioncontroller/configuration-swift.class/ispersistent.md)
  A Boolean value indicating if this context will write data to the the file system.
- [var webViewConfiguration: WKWebViewConfiguration!](wkwebextensioncontroller/configuration-swift.class/webviewconfiguration.md)
  The web view configuration to be used as a basis for configuring web views in extension contexts.
### Type Methods
- [class func `default`() -> Self](wkwebextensioncontroller/configuration-swift.class/default.md)
  Returns a new default configuration that is persistent and not unique.
- [class func nonPersistent() -> Self](wkwebextensioncontroller/configuration-swift.class/nonpersistent.md)
  Returns a new non-persistent configuration.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
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
- [WKWebExtension.WindowConfiguration](wkwebextension/windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/configuration-swift.class)*