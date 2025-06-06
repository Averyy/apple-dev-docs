# WKWebExtensionContext.NotificationUserInfoKey

**Framework**: Webkit  
**Kind**: struct

Constants for specifying web extension context information in notifications.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct NotificationUserInfoKey
```

## Topics

### Type properties
- [static let matchPatterns: WKWebExtensionContext.NotificationUserInfoKey](wkwebextensioncontext/notificationuserinfokey/matchpatterns.md)
  The corresponding value represents the affected permission match patterns in [`WKWebExtensionContext`](wkwebextensioncontext.md) notifications.
- [static let permissions: WKWebExtensionContext.NotificationUserInfoKey](wkwebextensioncontext/notificationuserinfokey/permissions.md)
  The corresponding value represents the affected permissions in [`WKWebExtensionContext`](wkwebextensioncontext.md) notifications.
### Initializers
- [init(String)](wkwebextensioncontext/notificationuserinfokey/init(_:).md)
  Creates a constant from a value you provide.
- [init(rawValue: String)](wkwebextensioncontext/notificationuserinfokey/init(rawvalue:).md)
  Creates a constant from a raw value you provide.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [WKWebExtensionContext.Error](wkwebextensioncontext/error.md)
  Constants used to indicate errors in the web extension context domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/notificationuserinfokey)*