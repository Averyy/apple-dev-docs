# flushUpdates

**Framework**: UIKit  
**Kind**: property

Flush all pending updates (including traits, properties, and layout) whenever the animation context changes. This includes flushing updates:

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
var flushUpdates: Bool { get set }
```

#### Discussion

- Before entering an animation scope, for invalidations that happened previously without animation.
- Before entering a nested animation scope, for invalidations that happened in the outer animation scope.
- Before exiting any animation scope, for invalidations that happened in that animation scope.
- Before disabling animations, for invalidations that happened in the animation scope with animations enabled.
- Before re-enabling animations, for invalidations that happened in the scope with animations disabled. This behavior implicitly applies to any nested animation scopes, even if they don’t explicitly specify this.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/flushupdates)*