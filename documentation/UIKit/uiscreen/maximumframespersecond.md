# maximumFramesPerSecond

**Framework**: UIKit  
**Kind**: property

The maximum number of frames per second a screen can render.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 10.2+

## Declaration

```swift
@MainActor
var maximumFramesPerSecond: Int { get }
```

#### Discussion

In iOS, the value of this property can be up to `120` for devices with ProMotion displays.

In tvOS, the value of this property depends on the hardware capabilities of the attached screen and the user’s selected resolution on Apple TV.

## See Also

- [func displayLink(withTarget: Any, selector: Selector) -> CADisplayLink?](uiscreen/displaylink(withtarget:selector:).md)
  Returns a display link object for the current screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/maximumframespersecond)*