# WKWebExtension.DataRecord

**Framework**: Webkit  
**Kind**: class

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

#### Overview

Contains properties and methods to query the data types and sizes.

## Topics

### Structures
- [WKWebExtension.DataRecord.Error](wkwebextension/datarecord/error.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) domain.
### Instance Properties
- [var containedDataTypes: Set<WKWebExtension.DataType>](wkwebextension/datarecord/containeddatatypes.md)
  The set of data types contained in this data record.
- [var displayName: String](wkwebextension/datarecord/displayname.md)
  The display name for the web extension to which this data record belongs.
- [var errors: [any Error]](wkwebextension/datarecord/errors.md)
  An array of errors that may have occurred when either calculating or deleting storage.
- [var totalSizeInBytes: Int](wkwebextension/datarecord/totalsizeinbytes.md)
  The total size in bytes of all data types contained in this data record.
- [var uniqueIdentifier: String](wkwebextension/datarecord/uniqueidentifier.md)
  Unique identifier for the web extension context to which this data record belongs.
### Instance Methods
- [func sizeInBytes(ofTypes: Set<WKWebExtension.DataType>) -> Int](wkwebextension/datarecord/sizeinbytes(oftypes:).md)
  Retrieves the size in bytes of the specific data types in this data record.

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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datarecord)*