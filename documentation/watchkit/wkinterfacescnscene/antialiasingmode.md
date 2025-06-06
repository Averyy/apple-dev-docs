# antialiasingMode

**Framework**: Watchkit  
**Kind**: property

The antialiasing mode used for rendering the scene.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var antialiasingMode: SCNAntialiasingMode { get set }
```

#### Discussion

SceneKit can provide antialiasing, which smooths edges in a rendered scene, using a technique called multisampling. Multisampling renders each pixel multiple times and combines the results, creating a higher quality image at a performance cost proportional to the number of samples it uses.

For available values, see [`SCNAntialiasingMode`](https://developer.apple.com/documentation/SceneKit/SCNAntialiasingMode). The default mode is [`SCNAntialiasingModeNone`](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/scnantialiasingmodenone).

## See Also

- [var preferredFramesPerSecond: Int](wkinterfacescnscene/preferredframespersecond.md)
  The animation frame rate that the interface uses to render its scene.
- [var scene: SCNScene?](wkinterfacescnscene/scene.md)
  The scene to be displayed.
- [func snapshot() -> UIImage](wkinterfacescnscene/snapshot.md)
  Renders the scene to a new image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/antialiasingmode)*