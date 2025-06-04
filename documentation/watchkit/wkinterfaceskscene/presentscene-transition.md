# presentScene(_:transition:)

**Framework**: Watchkit  
**Kind**: method

Transitions from the current scene to a new scene.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func presentScene(_ scene: SKScene, transition: SKTransition)
```

## Overview

If the interface is not currently presenting a scene, the new scene is presented immediately, and the `transition` property is ignored. Otherwise, the interface’s [`scene`](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/scene) property is updated immediately, and the transition is executed to animate the swap between scenes.

## Parameters

- `scene`: The scene to present.
- `transition`: A transition used to animate between the two scenes.

## See Also

- [var scene: SKScene?](scene.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/scene))
- [func presentScene(SKScene?)](presentscene(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/presentscene(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/presentscene(_:transition:))*