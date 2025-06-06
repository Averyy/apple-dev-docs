# hasRequestedOptionalAccessToAllHosts

**Framework**: Webkit  
**Kind**: property

A Boolean value indicating if the extension has requested optional access to all hosts.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var hasRequestedOptionalAccessToAllHosts: Bool { get set }
```

#### Discussion

If this property is `YES`, the extension has asked for access to all hosts in a call to `browser.runtime.permissions.request()`, and future permission checks will present discrete hosts for approval as being implicitly requested. This value should be saved and restored as needed by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/hasrequestedoptionalaccesstoallhosts)*