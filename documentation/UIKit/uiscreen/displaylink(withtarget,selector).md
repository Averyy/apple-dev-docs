# displayLink(withTarget:selector:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a display link object for the current screen.

**Availability**:
- iOS 4.0+ - Deprecated in 27.0
- iPadOS 4.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0

> **Deprecated**: Use the equivalent display link API on UIWindowScene

## Declaration

```swift
func displayLink(withTarget target: Any, selector sel: Selector) -> CADisplayLink?
```

```objc
- (CADisplayLink *) displayLinkWithTarget:(id) target selector:(SEL) sel;
```

## Return Value

A newly constructed display link object.

## Discussion

You use display link objects to synchronize your drawing code to the screen’s refresh rate. The newly constructed display link retains the target.

## Parameters

- `target`: An object to be notified when the screen should be updated.
- `sel`: The method of `target` to call. This selector must have the following signature:

  ```objc
  - (void)selector:(CADisplayLink *)sender;
  ```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/displaylink(withtarget:selector:))*