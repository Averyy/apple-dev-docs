# grantedPermissionsWereRemovedNotification

**Framework**: WebKit  
**Kind**: property  
**Role**: Type Property

This notification is sent whenever a web extension context has newly removed granted permissions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
class let grantedPermissionsWereRemovedNotification: NSNotification.Name
```

```c
extern NSNotificationName const WKWebExtensionContextGrantedPermissionsWereRemovedNotification;
```

## See Also

### Variables
- [WKWebExtensionContextDeniedPermissionMatchPatternsWereRemovedNotification](./deniedpermissionmatchpatternswereremovednotification.md)
  A notification the system sends whenever a web extension context has newly removed denied permission match patterns.
- [WKWebExtensionContextDeniedPermissionsWereRemovedNotification](./deniedpermissionswereremovednotification.md)
  A notification the system sends whenever a web extension context has newly removed denied permissions.
- [WKWebExtensionContextErrorDomain](./errordomain.md)
- [WKWebExtensionContextErrorsDidUpdateNotification](./errorsdidupdatenotification.md)
  This notification is sent whenever a web extension context has new errors or errors were cleared.
- [WKWebExtensionContextGrantedPermissionMatchPatternsWereRemovedNotification](./grantedpermissionmatchpatternswereremovednotification.md)
  This notification is sent whenever a web extension context has newly removed granted permission match patterns.
- [WKWebExtensionContextPermissionMatchPatternsWereDeniedNotification](./permissionmatchpatternsweredeniednotification.md)
  This notification is sent whenever a web extension context has newly denied permission match patterns.
- [WKWebExtensionContextPermissionMatchPatternsWereGrantedNotification](./permissionmatchpatternsweregrantednotification.md)
  This notification is sent whenever a web extension context has newly granted permission match patterns.
- [WKWebExtensionContextPermissionsWereDeniedNotification](./permissionsweredeniednotification.md)
  This notification is sent whenever a web extension context has newly denied permissions.
- [WKWebExtensionContextPermissionsWereGrantedNotification](./permissionsweregrantednotification.md)
  This notification is sent whenever a web extension context has newly granted permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/grantedpermissionswereremovednotification)*