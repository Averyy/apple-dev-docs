# isWritingToolsAvailable

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether Writing Tools features are currently available.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class var isWritingToolsAvailable: Bool { get }
```

#### Discussion

The value of this property is `true` when Writing Tools features are available, and `false` when they aren’t. Writing Tools support might be unavailable because of device constraints or because the system isn’t ready to process Writing Tools requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/iswritingtoolsavailable)*