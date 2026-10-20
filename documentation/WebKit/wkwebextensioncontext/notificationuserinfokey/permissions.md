# permissions

**Framework**: WebKit  
**Kind**: property  
**Role**: Type Property

The corresponding value represents the affected permissions in [`WKWebExtensionContext`](../../wkwebextensioncontext.md) notifications.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
static let permissions: WKWebExtensionContext.NotificationUserInfoKey
```

```c
extern WKWebExtensionContextNotificationUserInfoKey const WKWebExtensionContextNotificationUserInfoKeyPermissions;
```

## See Also

### Type properties
- [static let matchPatterns: WKWebExtensionContext.NotificationUserInfoKey](./matchpatterns.md)
  The corresponding value represents the affected permission match patterns in [`WKWebExtensionContext`](../../wkwebextensioncontext.md) notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/notificationuserinfokey/permissions)*