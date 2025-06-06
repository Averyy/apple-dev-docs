# currentPermissions

**Framework**: Webkit  
**Kind**: property

The currently granted permissions that have not expired.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var currentPermissions: Set<WKWebExtension.Permission> { get }
```

## See Also

- [var grantedPermissions: [WKWebExtension.Permission : Date]](wkwebextensioncontext/grantedpermissions.md)
  The currently granted permissions and their expiration dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/currentpermissions)*