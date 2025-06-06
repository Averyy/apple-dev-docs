# pointerLockState

**Framework**: UIKit  
**Kind**: property

The pointer lock state for the scene.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var pointerLockState: UIPointerLockState? { get }
```

#### Discussion

If a scene can’t lock the pointer, this property is `nil`.

## See Also

- [class UIPointerLockState](uipointerlockstate.md)
  An object that contains information about a scene’s pointer lock state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/pointerlockstate)*