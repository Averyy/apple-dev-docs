# scene

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The currently presented SpriteKit scene.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var scene: SKScene? { get }
```

```objc
@property (nonatomic, readonly, nullable) SKScene * scene;
```

## Mentions

- [Configuring a WatchKit Scene in a Storyboard](../configuring-a-watchkit-scene-in-a-storyboard.md)

#### Discussion

The default value is `nil`.

## See Also

### Displaying a Scene
- [func presentScene(SKScene?)](./presentscene%28_%29.md)
  Presents a scene.
- [func presentScene(SKScene, transition: SKTransition)](./presentscene%28_,transition%29.md)
  Transitions from the current scene to a new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/scene)*