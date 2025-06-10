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
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datarecord/error)*