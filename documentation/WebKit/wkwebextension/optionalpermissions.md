# optionalPermissions

**Framework**: WebKit  
**Kind**: property

The set of permissions that the extension may need for optional functionality.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var optionalPermissions: Set<WKWebExtension.Permission> { get }
```

#### Discussion

These permissions can be requested by the extension at a later time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/optionalpermissions)*