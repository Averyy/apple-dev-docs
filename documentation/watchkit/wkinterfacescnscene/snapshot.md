# snapshot()

**Framework**: Watchkit  
**Kind**: method

Renders the scene to a new image object.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func snapshot() -> UIImage
```

## Overview

An image object depicting the scene in its current state.

## Discussion

This method is thread-safe and may be called at any time.

## See Also

- [var antialiasingMode: SCNAntialiasingMode](antialiasingmode.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/antialiasingmode))
- [var preferredFramesPerSecond: Int](preferredframespersecond.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/preferredframespersecond))
- [var scene: SCNScene?](scene.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/scene))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/snapshot())*