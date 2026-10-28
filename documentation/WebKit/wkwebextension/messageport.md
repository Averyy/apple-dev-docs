# WKWebExtension.MessagePort

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface WKWebExtensionMessagePort : NSObject
```

## Overview

Contains properties and methods to handle message exchanges with a web extension.

## Topics

### Structures
- [WKWebExtension.MessagePort.Error](./messageport/error.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](./messageport.md) domain.
### Instance Properties
- [var applicationIdentifier: String?](./messageport/applicationidentifier.md)
  The unique identifier for the app to which this port should be connected.
- [var disconnectHandler: (((any Error)?) -> Void)?](./messageport/disconnecthandler.md)
  The block to be executed when the port disconnects.
- [var isDisconnected: Bool](./messageport/isdisconnected.md)
  Indicates whether the message port is disconnected.
- [var messageHandler: ((Any?, (any Error)?) -> Void)?](./messageport/messagehandler.md)
  The block to be executed when a message is received from the web extension.
### Instance Methods
- [func disconnect()](./messageport/disconnect%28%29.md)
  Disconnects the port, terminating all further messages.
- [func disconnect(throwing: (any Error)?)](./messageport/disconnect%28throwing%29.md)
  Disconnects the port, terminating all further messages with an optional error.
- [func sendMessage(Any?, completionHandler: (((any Error)?) -> Void)?)](./messageport/sendmessage%28_,completionhandler%29.md)
  Sends a message to the connected web extension.
### Errors
- [WKWebExtensionMessagePortError](./messageport/error/code.md)
  Constants that indicate errors in the [`WKWebExtensionMessagePort`](./messageport.md) domain.
- [WKWebExtensionMessagePortErrorDomain](./messageport/errordomain.md)
  A string that identifies the error domain.

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
- [WKWebExtension.DataRecord](./datarecord.md)
  An object that represents a record of stored data for a specific web extension context.
- [WKWebExtension.TabConfiguration](./tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](./windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](../wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](../wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/messageport)*