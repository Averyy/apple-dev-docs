# isUserAuthenticationEnabled

**Framework**: UIKit  
**Kind**: property

The current status of system user authentication.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
var isUserAuthenticationEnabled: Bool { get }
```

#### Discussion

This value is `true` if the system requires device owner authentication challenges to reveal the content of the scene associated with this manager, `false` otherwise.

> **Note**: This value represents whether protection is enabled in general. It doesn’t indicate the instantaneous state of whether any system-provided shield covers the UI at the moment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/systemprotectionmanager-swift.class/isuserauthenticationenabled)*