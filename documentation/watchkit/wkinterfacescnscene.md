# WKInterfaceSCNScene

**Framework**: Watchkit  
**Kind**: class

An object that lets you manage SceneKit content for display in your app.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKInterfaceSCNScene
```

#### Overview

To provide content for a [`WKInterfaceSCNScene`](wkinterfacescnscene.md) interface object, assign a [`SCNScene`](https://developer.apple.com/documentation/SceneKit/SCNScene) object to the interface’s [`scene`](wkinterfacescnscene/scene.md) property. For additional methods and properties for working with SceneKit, see the [`SCNSceneRenderer`](https://developer.apple.com/documentation/SceneKit/SCNSceneRenderer) protocol, which defines functionality common across all platforms.

Do not subclass or create instances of this class yourself. Instead, drag a SceneKit Scene object from your Object Library and add it to your storyboard. Then define an outlet in your interface controller class and connect it to the SceneKit Scene object. For example, to refer to a scene in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the SceneKit scene.

The SceneKit scene in your Watch app must be connected to a [`WKInterfaceSCNScene`](wkinterfacescnscene.md) outlet in your WatchKit extension for the scene to be visible in your watchOS app’s user interface.

##### Interface Builder Attributes

Xcode lets you configure information about your SceneKit Scene in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| Attribute | Description |
| --- | --- |
| Antialiasing | The antialiasing mode used for rendering the scene. You can also set this value programmatically using the [`antialiasingMode`](wkinterfacescnscene/antialiasingmode.md) property. |
| Frame Rate | The desired frame rate for the scene’s animation. You can also set this value programmatically using the [`WKInterfaceSCNScene`](wkinterfacescnscene.md) property. |
| Default Lighting | A checkbox that determines whether SceneKit automatically adds lights to a scene. If unchecked, SceneKit uses only the light sources contained in the scene graph. If checked, SceneKit automatically adds and places an omnidirectional light source when rendering scenes that contain no lights or only contain ambient lights. You can also set this value programmatically using the [`autoenablesDefaultLighting`](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523812-autoenablesdefaultlighting) property. |
| Jitter | A checkbox that determines whether SceneKit applies jittering to reduce aliasing artifacts. Jittering is a process that SceneKit uses to improve the visual quality of a rendered scene. While the scene’s content is still, SceneKit moves the [`pointOfView`](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523982-pointofview) location very slightly (by less than a pixel in projected screen space). It then composites images rendered after several such moves to create the final rendered scene, creating an antialiasing effect that smooths the edges of rendered geometry. You can also set this value programmatically using the [`isJitteringEnabled`](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1524026-isjitteringenabled) property. |
| Play | A checkbox that determines whether the scene is animated. If unchecked, SceneKit does not increment the scene time, so animations associated with the scene do not play. You can also set this value programmatically using the [`isPlaying`](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523401-isplaying) property. |
| Loop | A checkbox that determines whether SceneKit restarts the scene time after all animations in the scene have played. If checked, SceneKit returns the scene time to zero after all animations associated with the scene have played, causing those animations to repeat; otherwise, SceneKit stops playing the scene when all animations have completed. You can also set this value programmatically using the [`loops`](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522878-loops) property. |

##### Enabling Full Screen Mode

By default, when a watchOS app is running, the system reserves a strip of space across the top of the screen to display the time. The app’s content is only displayed in the area below the time.

In watchOS 4 and later, SpriteKit and SceneKit scenes can fill the full screen. When full screen mode is enabled, the SpriteKit or SceneKit scene extends up, under the time. The system still displays the time in the upper right corner with a gradient behind it, making it clearly visible against the scene.

To enable full screen mode, place a SpriteKit or SceneKit scene as the interface controller’s only content. Then, in the interface controller’s Attribute inspector, enable the Full Screen attribute.

![A screenshot showing the Full Screen attribute. ](https://docs-assets.developer.apple.com/published/27bd4b57c9ca3d48a96447c8972c2b98/media-2929968%402x.png)

## Topics

### Managing the SceneKit Scene
- [var antialiasingMode: SCNAntialiasingMode](wkinterfacescnscene/antialiasingmode.md)
  The antialiasing mode used for rendering the scene.
- [var preferredFramesPerSecond: Int](wkinterfacescnscene/preferredframespersecond.md)
  The animation frame rate that the interface uses to render its scene.
- [var scene: SCNScene?](wkinterfacescnscene/scene.md)
  The scene to be displayed.
- [func snapshot() -> UIImage](wkinterfacescnscene/snapshot.md)
  Renders the scene to a new image object.
### Initializing for SwiftUI
- [init()](wkinterfacescnscene/init.md)
  Creates a SceneKit scene for use in SwiftUI.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [SCNSceneRenderer](../SceneKit/SCNSceneRenderer.md)

## See Also

- [class WKInterfaceSKScene](wkinterfaceskscene.md)
  A visual WatchKit element that displays a SpriteKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene)*