# displayLink(withTarget:selector:)

**Framework**: UIKit  
**Kind**: method

Returns a display link object for the current screen.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func displayLink(withTarget target: Any, selector sel: Selector) -> CADisplayLink?
```

#### Return Value

A newly constructed display link object.

#### Discussion

You use display link objects to synchronize your drawing code to the screen’s refresh rate. The newly constructed display link retains the target.

## Parameters

- `target`: An object to be notified when the screen should be updated.
- `sel`: The method of   to call. This selector must have the following signature:

## See Also

- [var maximumFramesPerSecond: Int](uiscreen/maximumframespersecond.md)
  The maximum number of frames per second a screen can render.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/displaylink(withtarget:selector:))*