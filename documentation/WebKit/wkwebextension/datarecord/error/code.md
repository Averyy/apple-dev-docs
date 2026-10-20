# WKWebExtension.DataRecord.Error.Code

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate errors in the [`WKWebExtension.DataRecord`](../../datarecord.md) domain.

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

```c
enum WKWebExtensionDataRecordError : NSInteger;
```

## Topics

### Enumeration Cases
- [WKWebExtension.DataRecord.Error.Code.localStorageFailed](./code/localstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating local storage.
- [WKWebExtension.DataRecord.Error.Code.sessionStorageFailed](./code/sessionstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating session storage.
- [WKWebExtension.DataRecord.Error.Code.synchronizedStorageFailed](./code/synchronizedstoragefailed.md)
  Indicates a failure occurred when either deleting or calculating synchronized storage.
- [WKWebExtension.DataRecord.Error.Code.unknown](./code/unknown.md)
  Indicates that an unknown error occurred.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)
  Creates an error code from a raw value you provide.

## Relationships

### Conforms To
- [BitwiseCopyable](../../../../Swift/bitwisecopyable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Web extension errors
- [WKWebExtension.Error.Code](../../error/code.md)
  Constants that indicate errors in the [`WKWebExtension`](../../../wkwebextension.md) domain.
- [WKWebExtensionContext.Error.Code](../../../wkwebextensioncontext/error/code.md)
  Constants that indicate errors in the [`WKWebExtensionContext`](../../../wkwebextensioncontext.md) domain.
- [WKWebExtension.DataRecord.Error](../error.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](../../datarecord.md) domain.
- [WKWebExtension.MatchPattern.Error.Code](../../matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](../../matchpattern.md) domain.
- [WKWebExtension.MessagePort.Error.Code](../../messageport/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](../../messageport.md) domain.
- [WKWebExtension.MessagePort.Error](../../messageport/error.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](../../messageport.md) domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datarecord/error/code)*