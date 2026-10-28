# presentScene(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Presents a scene.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func presentScene(_ scene: SKScene?)
```

```objc
- (void) presentScene:(SKScene *) scene;
```

## Discussion

The new scene immediately replaces the current scene, if one exists.

## Parameters

- `scene`: The scene to present.

## See Also

### Displaying a Scene
- [var scene: SKScene?](./scene.md)
  The currently presented SpriteKit scene.
- [func presentScene(SKScene, transition: SKTransition)](./presentscene%28_,transition%29.md)
  Transitions from the current scene to a new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/presentscene(_:))*