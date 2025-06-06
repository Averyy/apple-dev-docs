# preferredFramesPerSecond

**Framework**: Watchkit  
**Kind**: property

The animation frame rate that the interface uses to render its scene.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var preferredFramesPerSecond: Int { get set }
```

## Mentions

- [Configuring a WatchKit Scene in a Storyboard](configuring-a-watchkit-scene-in-a-storyboard.md)

#### Discussion

SpriteKit chooses an actual frame rate that is as close as possible to your preferred frame rate based on the capabilities of the hardware and the systems other requirements. Choose a frame rate that your app can consistently maintain. The default value is 60 frames per second.

To provide a consistent frame rate, SpriteKit usually selects a frame rate that is a factor of the hardware’s maximum refresh rate. For example, if Apple Watch’s maximum refresh rate is 60 frames per second, then that is also the highest frame rate used by SpriteKit. However, if you ask for a lower frame rate, SpriteKit might choose 30, 20, 15 or some other factor as the actual frame rate.

## See Also

- [var isPaused: Bool](wkinterfaceskscene/ispaused.md)
  A Boolean value that determines whether the view’s scene animations are paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/preferredframespersecond)*