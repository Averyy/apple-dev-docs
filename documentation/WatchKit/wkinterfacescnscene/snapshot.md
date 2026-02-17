# snapshot()

**Framework**: WatchKit  
**Kind**: method

Renders the scene to a new image object.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func snapshot() -> UIImage
```

#### Return Value

An image object depicting the scene in its current state.

#### Discussion

This method is thread-safe and may be called at any time.

## See Also

- [var antialiasingMode: SCNAntialiasingMode](wkinterfacescnscene/antialiasingmode.md)
  The antialiasing mode used for rendering the scene.
- [var preferredFramesPerSecond: Int](wkinterfacescnscene/preferredframespersecond.md)
  The animation frame rate that the interface uses to render its scene.
- [var scene: SCNScene?](wkinterfacescnscene/scene.md)
  The scene to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/snapshot())*