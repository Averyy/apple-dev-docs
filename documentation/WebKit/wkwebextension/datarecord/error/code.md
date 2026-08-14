# WKWebExtension.DataRecord.Error.Code

**Framework**: WebKit  
**Kind**: enum

Constants that indicate errors in the [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) domain.

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
- [WKWebExtension.DataRecord.Error.Code.localStorageFailed](wkwebextension/datarecord/error/code/localstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating local storage.
- [WKWebExtension.DataRecord.Error.Code.sessionStorageFailed](wkwebextension/datarecord/error/code/sessionstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating session storage.
- [WKWebExtension.DataRecord.Error.Code.synchronizedStorageFailed](wkwebextension/datarecord/error/code/synchronizedstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating synchronized storage.
- [WKWebExtension.DataRecord.Error.Code.unknown](wkwebextension/datarecord/error/code/unknown.md)
  Indicates that an unknown error occurred.
### Initializers
- [init?(rawValue: Int)](wkwebextension/datarecord/error/code/init(rawvalue:).md)
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
- [WKWebExtension.DataRecord.Error](wkwebextension/datarecord/error.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) domain.
- [WKWebExtension.MatchPattern.Error.Code](wkwebextension/matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](wkwebextension/matchpattern.md) domain.
- [WKWebExtension.MessagePort.Error.Code](wkwebextension/messageport/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.
- [WKWebExtension.MessagePort.Error](wkwebextension/messageport/error.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datarecord/error/code)*