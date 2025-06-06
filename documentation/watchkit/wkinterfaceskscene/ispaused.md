# isPaused

**Framework**: Watchkit  
**Kind**: property

A Boolean value that determines whether the view’s scene animations are paused.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var isPaused: Bool { get set }
```

## Mentions

- [Configuring a WatchKit Scene in a Storyboard](configuring-a-watchkit-scene-in-a-storyboard.md)

#### Discussion

If the value is [`true`](https://developer.apple.com/documentation/swift/true), the scene’s content is fixed onscreen. No actions are executed and no physics simulation is performed.

## See Also

- [var preferredFramesPerSecond: Int](wkinterfaceskscene/preferredframespersecond.md)
  The animation frame rate that the interface uses to render its scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/ispaused)*