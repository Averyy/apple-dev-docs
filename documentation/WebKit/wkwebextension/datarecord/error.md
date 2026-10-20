# WKWebExtension.DataRecord.Error

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

Constants that indicate errors in the [`WKWebExtension.DataRecord`](../datarecord.md) domain.

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
  Indicates a [`WKWebExtension.DataRecord`](../datarecord.md) error.
- [static var localStorageFailed: WKWebExtension.DataRecord.Error.Code](./error/localstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating local storage.
- [static var sessionStorageFailed: WKWebExtension.DataRecord.Error.Code](./error/sessionstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating session storage.
- [static var synchronizedStorageFailed: WKWebExtension.DataRecord.Error.Code](./error/synchronizedstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating synchronized storage.
- [static var unknown: WKWebExtension.DataRecord.Error.Code](./error/unknown.md)
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
- [WKWebExtension.DataRecord.Error.Code](./error/code.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](../datarecord.md) domain.
- [WKWebExtension.MatchPattern.Error.Code](../matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](../matchpattern.md) domain.
- [WKWebExtension.MessagePort.Error.Code](../messageport/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](../messageport.md) domain.
- [WKWebExtension.MessagePort.Error](../messageport/error.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](../messageport.md) domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datarecord/error)*