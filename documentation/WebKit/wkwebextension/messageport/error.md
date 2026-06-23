# WKWebExtension.MessagePort.Error

**Framework**: WebKit  
**Kind**: struct

Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct Error
```

## Topics

### Type Properties
- [static var errorDomain: String](wkwebextension/messageport/error/errordomain.md)
  A string that identifies the error domain.
- [static var messageInvalid: WKWebExtension.MessagePort.Error.Code](wkwebextension/messageport/error/messageinvalid.md)
  Indicates that the message is invalid.
- [static var notConnected: WKWebExtension.MessagePort.Error.Code](wkwebextension/messageport/error/notconnected.md)
  Indicates that the message port is disconnected.
- [static var unknown: WKWebExtension.MessagePort.Error.Code](wkwebextension/messageport/error/unknown.md)
  Indicates that an unknown error occurred.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [WKWebExtension.MessagePort.Error.Code](wkwebextension/messageport/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/messageport/error)*