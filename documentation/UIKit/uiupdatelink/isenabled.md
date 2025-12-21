# isEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the UI update link is monitoring UI updates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

By default, the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), which means the system invokes the actions of the UI update link for each UI update.

When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the UI update link has no effect. Set the value to [`false`](https://developer.apple.com/documentation/Swift/false) if you want to temporarily turn off the UI update link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/isenabled)*