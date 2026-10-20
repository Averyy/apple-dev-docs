# scene

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The scene to be displayed.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var scene: SCNScene? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNScene * scene;
```

## See Also

### Managing the SceneKit Scene
- [var antialiasingMode: SCNAntialiasingMode](./antialiasingmode.md)
  The antialiasing mode used for rendering the scene.
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The animation frame rate that the interface uses to render its scene.
- [func snapshot() -> UIImage](./snapshot%28%29.md)
  Renders the scene to a new image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/scene)*