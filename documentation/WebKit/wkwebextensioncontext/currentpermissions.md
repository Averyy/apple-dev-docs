# currentPermissions

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The currently granted permissions that have not expired.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var currentPermissions: Set<WKWebExtension.Permission> { get }
```

```objc
@property (nonatomic, copy, readonly) NSSet<NSString *> * currentPermissions;
```

## See Also

### Related Documentation
- [var grantedPermissions: [WKWebExtension.Permission : Date]](./grantedpermissions.md)
  The currently granted permissions and their expiration dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/currentpermissions)*