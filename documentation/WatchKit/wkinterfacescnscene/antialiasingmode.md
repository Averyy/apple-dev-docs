# antialiasingMode

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The antialiasing mode used for rendering the scene.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var antialiasingMode: SCNAntialiasingMode { get set }
```

```objc
@property (nonatomic) SCNAntialiasingMode antialiasingMode;
```

## Discussion

SceneKit can provide antialiasing, which smooths edges in a rendered scene, using a technique called multisampling. Multisampling renders each pixel multiple times and combines the results, creating a higher quality image at a performance cost proportional to the number of samples it uses.

For available values, see [`SCNAntialiasingMode`](../../SceneKit/scnantialiasingmode.md). The default mode is [`SCNAntialiasingMode.none`](../../SceneKit/scnantialiasingmode/none.md).

## See Also

### Managing the SceneKit Scene
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The animation frame rate that the interface uses to render its scene.
- [var scene: SCNScene?](./scene.md)
  The scene to be displayed.
- [func snapshot() -> UIImage](./snapshot%28%29.md)
  Renders the scene to a new image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/antialiasingmode)*