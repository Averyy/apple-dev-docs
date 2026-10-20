# WKWebExtension.MessagePort.Error

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

Constants that indicate errors in the [`WKWebExtension.MessagePort`](../messageport.md) domain.

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
- [static var errorDomain: String](./error/errordomain.md)
  A string that identifies the error domain.
- [static var messageInvalid: WKWebExtension.MessagePort.Error.Code](./error/messageinvalid.md)
  Indicates that the message is invalid.
- [static var notConnected: WKWebExtension.MessagePort.Error.Code](./error/notconnected.md)
  Indicates that the message port is disconnected.
- [static var unknown: WKWebExtension.MessagePort.Error.Code](./error/unknown.md)
  Indicates that an unknown error occurred.

## Relationships

### Conforms To
- [CustomNSError](../../../Foundation/customnserror.md)
- [Equatable](../../../Swift/equatable.md)
- [Error](../../../Swift/error.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Web extension errors
- [WKWebExtension.Error.Code](../error/code.md)
  Constants that indicate errors in the [`WKWebExtension`](../../wkwebextension.md) domain.
- [WKWebExtensionContext.Error.Code](../../wkwebextensioncontext/error/code.md)
  Constants that indicate errors in the [`WKWebExtensionContext`](../../wkwebextensioncontext.md) domain.
- [WKWebExtension.DataRecord.Error.Code](../datarecord/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](../datarecord.md) domain.
- [WKWebExtension.DataRecord.Error](../datarecord/error.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](../datarecord.md) domain.
- [WKWebExtension.MatchPattern.Error.Code](../matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](../matchpattern.md) domain.
- [WKWebExtension.MessagePort.Error.Code](./error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](../messageport.md) domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/messageport/error)*