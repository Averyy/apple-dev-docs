# WKWebExtension.MessagePort

**Framework**: WebKit  
**Kind**: class

An object that manages message-based communication with a web extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class MessagePort
```

#### Overview

Contains properties and methods to handle message exchanges with a web extension.

## Topics

### Structures
- [WKWebExtension.MessagePort.Error](wkwebextension/messageport/error.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.
### Instance Properties
- [var applicationIdentifier: String?](wkwebextension/messageport/applicationidentifier.md)
  The unique identifier for the app to which this port should be connected.
- [var disconnectHandler: (((any Error)?) -> Void)?](wkwebextension/messageport/disconnecthandler.md)
  The block to be executed when the port disconnects.
- [var isDisconnected: Bool](wkwebextension/messageport/isdisconnected.md)
  Indicates whether the message port is disconnected.
- [var messageHandler: ((Any?, (any Error)?) -> Void)?](wkwebextension/messageport/messagehandler.md)
  The block to be executed when a message is received from the web extension.
### Instance Methods
- [func disconnect()](wkwebextension/messageport/disconnect.md)
  Disconnects the port, terminating all further messages.
- [func disconnect(throwing: (any Error)?)](wkwebextension/messageport/disconnect(throwing:).md)
  Disconnects the port, terminating all further messages with an optional error.
- [func sendMessage(Any?, completionHandler: (((any Error)?) -> Void)?)](wkwebextension/messageport/sendmessage(_:completionhandler:).md)
  Sends a message to the connected web extension.

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
- [WKWebExtension.TabConfiguration](wkwebextension/tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](wkwebextension/windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/messageport)*