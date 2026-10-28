# WKWebExtension.DataRecord

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

An object that represents a record of stored data for a specific web extension context.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class DataRecord
```

```objc
@interface WKWebExtensionDataRecord : NSObject
```

## Overview

Contains properties and methods to query the data types and sizes.

## Topics

### Structures
- [WKWebExtension.DataRecord.Error](./datarecord/error.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](./datarecord.md) domain.
### Instance Properties
- [var containedDataTypes: Set<WKWebExtension.DataType>](./datarecord/containeddatatypes.md)
  The set of data types contained in this data record.
- [var displayName: String](./datarecord/displayname.md)
  The display name for the web extension to which this data record belongs.
- [var errors: [any Error]](./datarecord/errors.md)
  An array of errors that may have occurred when either calculating or deleting storage.
- [var totalSizeInBytes: Int](./datarecord/totalsizeinbytes.md)
  The total size in bytes of all data types contained in this data record.
- [var uniqueIdentifier: String](./datarecord/uniqueidentifier.md)
  Unique identifier for the web extension context to which this data record belongs.
### Instance Methods
- [func sizeInBytes(ofTypes: Set<WKWebExtension.DataType>) -> Int](./datarecord/sizeinbytes%28oftypes%29.md)
  Retrieves the size in bytes of the specific data types in this data record.
### Errors
- [WKWebExtensionDataRecordError](./datarecord/error/code.md)
  Constants that indicate errors in the [`WKWebExtensionDataRecord`](./datarecord.md) domain.
- [WKWebExtensionDataRecordErrorDomain](./datarecord/errordomain.md)
  Indicates a [`WKWebExtensionDataRecord`](./datarecord.md) error.

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
- [WKWebExtension.TabConfiguration](./tabconfiguration.md)
  An object that encapsulates configuration options for a tab in an extension.
- [WKWebExtension.WindowConfiguration](./windowconfiguration.md)
  An object that encapsulates configuration options for a window in an extension.
- [WKWebExtensionController.Configuration](../wkwebextensioncontroller/configuration-swift.class.md)
  A [`WKWebExtensionController.Configuration`](../wkwebextensioncontroller/configuration-swift.class.md) object with which to initialize a web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datarecord)*