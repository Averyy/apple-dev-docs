# WKWebExtension.DataRecord.Error

**Framework**: WebKit  
**Kind**: struct

Constants that indicate errors in the [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) domain.

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
- [static var errorDomain: String](wkwebextension/datarecord/error/errordomain.md)
  Indicates a [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) error.
- [static var localStorageFailed: WKWebExtension.DataRecord.Error.Code](wkwebextension/datarecord/error/localstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating local storage.
- [static var sessionStorageFailed: WKWebExtension.DataRecord.Error.Code](wkwebextension/datarecord/error/sessionstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating session storage.
- [static var synchronizedStorageFailed: WKWebExtension.DataRecord.Error.Code](wkwebextension/datarecord/error/synchronizedstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating synchronized storage.
- [static var unknown: WKWebExtension.DataRecord.Error.Code](wkwebextension/datarecord/error/unknown.md)
  Indicates that an unknown error occurred.

## Relationships

### Conforms To
- [CustomNSError](../foundation/customnserror.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [WKWebExtension.Error.Code](wkwebextension/error/code.md)
  Constants that indicate errors in the [`WKWebExtension`](wkwebextension.md) domain.
- [WKWebExtensionContext.Error.Code](wkwebextensioncontext/error/code.md)
  Constants that indicate errors in the [`WKWebExtensionContext`](wkwebextensioncontext.md) domain.
- [WKWebExtension.DataRecord.Error.Code](wkwebextension/datarecord/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) domain.
- [WKWebExtension.MatchPattern.Error.Code](wkwebextension/matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](wkwebextension/matchpattern.md) domain.
- [WKWebExtension.MessagePort.Error.Code](wkwebextension/messageport/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.
- [WKWebExtension.MessagePort.Error](wkwebextension/messageport/error.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datarecord/error)*