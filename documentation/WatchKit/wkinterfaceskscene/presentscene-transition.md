# presentScene(_:transition:)

**Framework**: WatchKit  
**Kind**: method

Transitions from the current scene to a new scene.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func presentScene(_ scene: SKScene, transition: SKTransition)
```

#### Discussion

If the interface is not currently presenting a scene, the new scene is presented immediately, and the `transition` property is ignored. Otherwise, the interface’s [`scene`](wkinterfaceskscene/scene.md) property is updated immediately, and the transition is executed to animate the swap between scenes.

## Parameters

- `scene`: The scene to present.
- `transition`: A transition used to animate between the two scenes.

## See Also

- [var scene: SKScene?](wkinterfaceskscene/scene.md)
  The currently presented SpriteKit scene.
- [func presentScene(SKScene?)](wkinterfaceskscene/presentscene(_:).md)
  Presents a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/presentscene(_:transition:))*