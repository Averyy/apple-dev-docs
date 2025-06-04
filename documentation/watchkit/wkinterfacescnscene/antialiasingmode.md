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

## Overview

SceneKit can provide antialiasing, which smooths edges in a rendered scene, using a technique called multisampling. Multisampling renders each pixel multiple times and combines the results, creating a higher quality image at a performance cost proportional to the number of samples it uses.

For available values, see [`SCNAntialiasingMode`](https://developer.apple.com/documentation/SceneKit/SCNAntialiasingMode). The default mode is [`SCNAntialiasingModeNone`](https://developer.apple.com/documentation/scenekit/scnantialiasingmode/scnantialiasingmodenone).

## See Also

- [var preferredFramesPerSecond: Int](preferredframespersecond.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/preferredframespersecond))
- [var scene: SCNScene?](scene.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/scene))
- [func snapshot() -> UIImage](snapshot().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/snapshot()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/antialiasingmode)*