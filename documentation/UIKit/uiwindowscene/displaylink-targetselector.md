# displayLink(target:selector:)

**Framework**: UIKit  
**Kind**: method

Creates a display link targeting the display associated with this scene.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func displayLink(target: Any, selector sel: Selector) -> CADisplayLink?
```

#### Return Value

A new display link, or `nil` only in exceptional cases where the system cannot construct a display link.

#### Discussion

The returned display link is automatically retargeted when the scene moves between displays.

## Parameters

- `target`: An object that is the target of the display link callback.
- `sel`: A selector on `target` to call when the display link fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/displaylink(target:selector:))*