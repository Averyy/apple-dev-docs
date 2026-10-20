# WKWebExtensionContext.Error.Code

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate errors in the [`WKWebExtensionContext`](../../wkwebextensioncontext.md) domain.

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
enum WKWebExtensionContextError : NSInteger;
```

## Topics

### Enumeration Cases
- [WKWebExtensionContext.Error.Code.alreadyLoaded](./code/alreadyloaded.md)
  Indicates that the context is already loaded by a [`WKWebExtensionController`](../../wkwebextensioncontroller.md).
- [WKWebExtensionContext.Error.Code.backgroundContentFailedToLoad](./code/backgroundcontentfailedtoload.md)
  Indicates that an error occurred loading the background content.
- [WKWebExtensionContext.Error.Code.baseURLAlreadyInUse](./code/baseurlalreadyinuse.md)
  Indicates that another context is already using the specified base URL.
- [WKWebExtensionContext.Error.Code.noBackgroundContent](./code/nobackgroundcontent.md)
  Indicates that the extension does not have background content.
- [WKWebExtensionContext.Error.Code.notLoaded](./code/notloaded.md)
  Indicates that the context is not loaded by a [`WKWebExtensionController`](../../wkwebextensioncontroller.md).
- [WKWebExtensionContext.Error.Code.unknown](./code/unknown.md)
  Indicates that an unknown error occurred.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)
  Creates an error code from a raw value you provide.

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Web extension errors
- [WKWebExtension.Error.Code](../../wkwebextension/error/code.md)
  Constants that indicate errors in the [`WKWebExtension`](../../wkwebextension.md) domain.
- [WKWebExtension.DataRecord.Error.Code](../../wkwebextension/datarecord/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](../../wkwebextension/datarecord.md) domain.
- [WKWebExtension.DataRecord.Error](../../wkwebextension/datarecord/error.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](../../wkwebextension/datarecord.md) domain.
- [WKWebExtension.MatchPattern.Error.Code](../../wkwebextension/matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](../../wkwebextension/matchpattern.md) domain.
- [WKWebExtension.MessagePort.Error.Code](../../wkwebextension/messageport/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](../../wkwebextension/messageport.md) domain.
- [WKWebExtension.MessagePort.Error](../../wkwebextension/messageport/error.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](../../wkwebextension/messageport.md) domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/error/code)*