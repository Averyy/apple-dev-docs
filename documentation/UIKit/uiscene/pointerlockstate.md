# pointerLockState

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The pointer lock state for the scene.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var pointerLockState: UIPointerLockState? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIPointerLockState * pointerLockState;
```

## Discussion

If a scene can’t lock the pointer, this property is `nil`.

## See Also

### Getting the pointer lock state
- [class UIPointerLockState](../uipointerlockstate.md)
  An object that contains information about a scene’s pointer lock state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/pointerlockstate)*