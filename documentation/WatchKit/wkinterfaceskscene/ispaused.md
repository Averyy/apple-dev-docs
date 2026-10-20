# isPaused

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the view’s scene animations are paused.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var isPaused: Bool { get set }
```

```objc
@property (nonatomic, getter=isPaused) BOOL paused;
```

## Mentions

- [Configuring a WatchKit Scene in a Storyboard](../configuring-a-watchkit-scene-in-a-storyboard.md)

#### Discussion

If the value is [`true`](../../Swift/true.md), the scene’s content is fixed onscreen. No actions are executed and no physics simulation is performed.

## See Also

### Controlling the Timing of a Scene’s Rendering
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The animation frame rate that the interface uses to render its scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/ispaused)*