# WKWebExtension.MessagePort.Error.Code

**Framework**: WebKit  
**Kind**: enum

Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
enum Code
```

## Topics

### Enumeration Cases
- [WKWebExtension.MessagePort.Error.Code.messageInvalid](wkwebextension/messageport/error/code/messageinvalid.md)
  Indicates that the message is invalid.
- [WKWebExtension.MessagePort.Error.Code.notConnected](wkwebextension/messageport/error/code/notconnected.md)
  Indicates that the message port is disconnected.
- [WKWebExtension.MessagePort.Error.Code.unknown](wkwebextension/messageport/error/code/unknown.md)
  Indicates that an unknown error occurred.
### Initializers
- [init?(rawValue: Int)](wkwebextension/messageport/error/code/init(rawvalue:).md)
  Creates an error code from a raw value you provide.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [WKWebExtension.Error.Code](wkwebextension/error/code.md)
  Constants that indicate errors in the [`WKWebExtension`](wkwebextension.md) domain.
- [WKWebExtensionContext.Error.Code](wkwebextensioncontext/error/code.md)
  Constants that indicate errors in the [`WKWebExtensionContext`](wkwebextensioncontext.md) domain.
- [WKWebExtension.DataRecord.Error.Code](wkwebextension/datarecord/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) domain.
- [WKWebExtension.DataRecord.Error](wkwebextension/datarecord/error.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) domain.
- [WKWebExtension.MatchPattern.Error.Code](wkwebextension/matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](wkwebextension/matchpattern.md) domain.
- [WKWebExtension.MessagePort.Error](wkwebextension/messageport/error.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/messageport/error/code)*