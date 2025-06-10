# WKWebExtensionContext.Error

**Framework**: WebKit  
**Kind**: struct

Constants used to indicate errors in the web extension context domain.

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
- [static var alreadyLoaded: WKWebExtensionContext.Error.Code](wkwebextensioncontext/error/alreadyloaded.md)
  Indicates that the context is already loaded by a [`WKWebExtensionController`](wkwebextensioncontroller.md).
- [static var backgroundContentFailedToLoad: WKWebExtensionContext.Error.Code](wkwebextensioncontext/error/backgroundcontentfailedtoload.md)
  Indicates that an error occurred loading the background content.
- [static var baseURLAlreadyInUse: WKWebExtensionContext.Error.Code](wkwebextensioncontext/error/baseurlalreadyinuse.md)
  Indicates that another context is already using the specified base URL.
- [static var errorDomain: String](wkwebextensioncontext/error/errordomain.md)
  A string that identifies the error domain.
- [static var noBackgroundContent: WKWebExtensionContext.Error.Code](wkwebextensioncontext/error/nobackgroundcontent.md)
  Indicates that the extension does not have background content.
- [static var notLoaded: WKWebExtensionContext.Error.Code](wkwebextensioncontext/error/notloaded.md)
  Indicates that the context is not loaded by a [`WKWebExtensionController`](wkwebextensioncontroller.md).
- [static var unknown: WKWebExtensionContext.Error.Code](wkwebextensioncontext/error/unknown.md)
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

- [WKWebExtensionContext.NotificationUserInfoKey](wkwebextensioncontext/notificationuserinfokey.md)
  Constants for specifying web extension context information in notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/error)*