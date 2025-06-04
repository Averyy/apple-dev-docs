# WKInterfaceSKScene

**Framework**: WatchKit  
**Kind**: class

A visual WatchKit element that displays a SpriteKit scene.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKInterfaceSKScene
```

#### Overview

Present a scene by calling the interface’s [`presentScene(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/presentscene(_:)) or [`presentScene(_:transition:)`](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/presentscene(_:transition:)) method and passing in a [`SKScene`](https://developer.apple.com/documentation/SpriteKit/SKScene) object. When a scene is presented, it alternates between running its simulation (which animates the content) and rendering the content for display. You can pause the scene by setting the interface’s [`isPaused`](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/ispaused) property to [`true`](https://developer.apple.com/documentation/swift/true).

Do not subclass or create instances of this class yourself. Instead, drag a SpriteKit Scene object from your Object Library and add it to your storyboard. Then define an outlet in your interface controller class and connect it to the SpriteKit Scene object. For example, to refer to a scene object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the SpriteKit scene.

The SpriteKit scene in your Watch app must be connected to a [`WKInterfaceSKScene`](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene) outlet in your WatchKit extension for the scene to be visible in your watchOS app’s user interface.

## Topics

### Displaying a Scene
- [var scene: SKScene?](scene.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/scene))
  The currently presented SpriteKit scene.
- [func presentScene(SKScene?)](presentscene(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/presentscene(_:)))
  Presents a scene.
- [func presentScene(SKScene, transition: SKTransition)](presentscene(_:transition:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/presentscene(_:transition:)))
  Transitions from the current scene to a new scene.
### Configuring the Scene in a Storyboard
- [Configuring a WatchKit Scene in a Storyboard](configuring-a-watchkit-scene-in-a-storyboard.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/configuring-a-watchkit-scene-in-a-storyboard))
  Xcode lets you configure information about your SpriteKit Scene in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.
### Controlling the Timing of a Scene’s Rendering
- [var preferredFramesPerSecond: Int](preferredframespersecond.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/preferredframespersecond))
  The animation frame rate that the interface uses to render its scene.
- [var isPaused: Bool](ispaused.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/ispaused))
  A Boolean value that determines whether the view’s scene animations are paused.
### Snapshotting Nodes to a Texture
- [func texture(from: SKNode) -> SKTexture?](texture(from:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/texture(from:)))
  Renders the contents of a node tree and returns the rendered image as a SpriteKit texture.
- [func texture(from: SKNode, crop: CGRect) -> SKTexture?](texture(from:crop:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/texture(from:crop:)))
  Renders a portion of a node’s contents and returns the rendered image as a SpriteKit texture.
### Initializing for SwiftUI
- [init()](init().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/init()))
  Creates a SpriteKit scene for use in SwiftUI.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [class WKInterfaceSCNScene](wkinterfacescnscene.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene))
  An object that lets you manage SceneKit content for display in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene)*