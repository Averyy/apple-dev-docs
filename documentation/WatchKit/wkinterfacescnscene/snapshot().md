# snapshot()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Renders the scene to a new image object.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func snapshot() -> UIImage
```

```objc
- (UIImage *) snapshot;
```

## Return Value

An image object depicting the scene in its current state.

## Discussion

This method is thread-safe and may be called at any time.

## See Also

### Managing the SceneKit Scene
- [var antialiasingMode: SCNAntialiasingMode](./antialiasingmode.md)
  The antialiasing mode used for rendering the scene.
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The animation frame rate that the interface uses to render its scene.
- [var scene: SCNScene?](./scene.md)
  The scene to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/snapshot())*