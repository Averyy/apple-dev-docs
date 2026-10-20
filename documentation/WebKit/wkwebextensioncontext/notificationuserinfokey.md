# WKWebExtensionContext.NotificationUserInfoKey

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * WKWebExtensionContextNotificationUserInfoKey;
```

## Topics

### Type properties
- [static let matchPatterns: WKWebExtensionContext.NotificationUserInfoKey](./notificationuserinfokey/matchpatterns.md)
  The corresponding value represents the affected permission match patterns in [`WKWebExtensionContext`](../wkwebextensioncontext.md) notifications.
- [static let permissions: WKWebExtensionContext.NotificationUserInfoKey](./notificationuserinfokey/permissions.md)
  The corresponding value represents the affected permissions in [`WKWebExtensionContext`](../wkwebextensioncontext.md) notifications.
### Initializers
- [init(String)](./notificationuserinfokey/init%28_%29.md)
  Creates a constant from a value you provide.
- [init(rawValue: String)](./notificationuserinfokey/init%28rawvalue%29.md)
  Creates a constant from a raw value you provide.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Structures
- [WKWebExtensionContext.Error](./error.md)
  Constants used to indicate errors in the web extension context domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/notificationuserinfokey)*