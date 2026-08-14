# Designing no-code games with Reality Composer Pro 3

**Framework**: visionOS

Build a video game in Reality Composer Pro without code using Script Graphs.

**Availability**:
- visionOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

> **Note**: This sample code project is associated with WWDC26 session 252: [`Design no-code games with Reality Composer Pro`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2026/252/).

This sample code project uses [`Reality Composer Pro`](https://developer.apple.comhttps://developer.apple.com/reality-composer-pro/) and [`RealityKit`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit) to build a video game whose gameplay you author visually instead of by writing code. The game follows a sleepy squirrel who is taking a nap on top of a leafy pad. The goal of the game is to wake up the squirrel, guide them up a tree through the branches and leaves, so they make it home in time for dinner.

![A screenshot of the squirrel asleep on a leafy pad inside a scene in Reality Composer Pro 3.](/images/com.apple.visionOS/squirrel-overview@2x.png)

Rather than writing code, the sample relies on Script Graphs to drive almost every behavior of the squirrel and the world. A small [`SwiftUI`](https://developer.apple.com/documentation/swiftui) layer hosts the scene, shows the speech bubbles and buttons, and trades messages with those graphs. This sample demonstrates how to initialize the [`RealityKitScripting`](https://developer.apple.comhttps://github.com/apple/realitykitscripting) runtime, pass messages between the Script Graph layer and the SwiftUI layer, and design platformer game mechanics inside Reality Composer Pro.

#### Start the Script Graph Runtime

Script Graphs are the visual gameplay logic you author in Reality Composer Pro. Inside Reality Composer Pro, you attach a Scripting component to entities, edit the Script Graph associated with those entities, then publish the entities and logic together as a Reality file. Then in your Xcode project, you initialize the runtime before loading your content in a [`RealityView`](https://developer.apple.com/documentation/realitykit/realityview) marked with the `.realityScripting()` view modifier.

The runtime and view modifier ships in [`RealityKitScripting`](https://developer.apple.comhttps://github.com/apple/realitykitscripting), an open source Swift package maintained by Apple that you add to your Xcode project. Use the Swift Package Manager to add a dependency pointing at `RealityKitScripting`, link the `RealityKitScripting` library to your app target, then import the module wherever your code starts or talks to the runtime. For more detailed instructions on how to add a package to your Xcode project, see [`Adding package dependencies to your app`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app).

The app initializes the runtime by calling `RKS.initialize(inputOptions:)`, setting the initialization option to `.all.subtracting(.ar)` because `.ar` input modes aren’t available in a volumetric window.

```swift
import RealityKit
import RealityKitScripting
import SwiftUI

@main
struct SquirrelApp: App {
    init() {
        do {
            try RKS.initialize(inputOptions: .all.subtracting(.ar))
        } catch {
            assertionFailure("Failed to initialize the Script Graph runtime: \(error)")
        }
    }

    // ...
}
```

Then the sample loads the `world` entity from the built Reality file inside a `RealityView`, and uses the `.realityScripting()` view modifier to run your scene’s logic:

```swift
RealityView { content, attachments in
    let entity = try await Entity(named: "world")
    content.add(entity)

    // ...
}
.realityScripting()
```

#### Pass Messages Between Swiftui and the Graph

The interface and the gameplay logic need to stay in agreement. When the squirrel speaks, a bubble appears, and when you press a button, the game responds. Script Graphs and [`SwiftUI`](https://developer.apple.com/documentation/swiftui) keep that agreement through named scene events. You declare each event once in Reality Composer Pro, after which both sides refer to the events by name.

Send events to the [`Scene`](https://developer.apple.com/documentation/realitykit/scene) using the extension method `.send(name:with:)` provided by the `RealityKitScripting` package. Events that require extra data can receive that information in a dictionary using the `with:` parameter.

```swift
scene.send(name: "setCurrentLevelScreen", with: ["levelScreenName": sceneName])
```

Receive events from the [`Scene`](https://developer.apple.com/documentation/realitykit/scene) by using the `.subscribe(forEventName:on:)` extension method provided by the `RealityKitScripting` package.

```swift
scene.subscribe(forEventName: "squirrelTalk", on: { event in
    if let sayThis: String = try? event.value("sayThis") {
        DispatchQueue.main.async {
            if sayThis == "zzz" {
                self.showSquirrelTalk = true
            }
            self.squirrelTalkText = sayThis
            self.squirrelTalkTrigger += 1
        }
    }
}).store(in: &cancellables)
```

#### Drive Game Mechanics with Script Graphs

Script Graphs drive almost every behavior in this game instead of Swift code. The moving platforms, the collectibles, and the squirrel’s animations all run as visual node graphs in the scene.

To learn more about building logic in the Script Graph editor, see [`Getting started with Script Graphs`](https://developer.apple.com/documentation/realitycomposerpro/getting-started-with-script-graphs).

Consider the example of bouncy animations on some of the platforms the squirrel jumps across. When the squirrel lands on a surface, the surface squashes under the impact then bounces back to rest. Two Script Graphs produce this behavior, coordinating through a single named event. Unlike the squirrel talk example above, where the graph exchanges messages with SwiftUI, both sides of this event are graphs — one graph detects the landing and announces it, and the other graph plays the reaction.

One graph detects the landing and announces it. In `OnFloorCollision`, an `On Collision Began` node starts when the squirrel touches the surface, and a `Send Entity Event` node sends an event named `bounce` to the entity that plays the animation.

![A screenshot of the OnFloorCollision Script Graph in Reality Composer Pro, where an On Collision Began node feeds a Send Entity Event node that sends an event named bounce.](/images/com.apple.visionOS/collision-began@2x.png)

In `BounceAnim`, an `On Entity Event` node listens for `bounce` and records the moment it arrives. The rest of the graph uses that timestamp to animate the surface so it squashes and springs back.

![A screenshot of the BounceAnim Script Graph in Reality Composer Pro, where an On Entity Event node for bounce sets a variable to the current time to start the animation.](/images/com.apple.visionOS/bounce-anim@2x.png)

## See Also

- [Reality Composer Pro](../realitycomposerpro/realitycomposerpro.md)
  Build, design, and orchestrate 3D content for your RealityKit apps.
- [Chaparral Village: Building an immersive visionOS adventure game](chaparral-village-building-an-immersive-visionos-adventure-game.md)
  Create an adventure game using SwiftUI, RealityKit, and Reality Composer Pro 3.
- [Petite Asteroids: Building a volumetric visionOS game](petite-asteroids-building-a-volumetric-visionos-game.md)
  Use the latest RealityKit APIs to create a beautiful video game for visionOS.
- [BOT-anist](bot-anist.md)
  Build a multiplatform app that uses windows, volumes, and animations to create a robot botanist’s greenhouse.
- [Swift Splash](swift-splash.md)
  Use RealityKit to create an interactive ride in visionOS.
- [Diorama](diorama.md)
  Design scenes for your visionOS app using Reality Composer Pro.
- [Building an immersive media viewing experience](building-an-immersive-media-viewing-experience.md)
  Add a deeper level of immersion to media playback in your app with RealityKit and Reality Composer Pro.
- [Enabling video reflections in an immersive environment](enabling-video-reflections-in-an-immersive-environment.md)
  Create a more immersive experience by adding video reflections in a custom environment.
- [Combining 2D and 3D views in an immersive app](../realitykit/combining-2d-and-3d-views-in-an-immersive-app.md)
  Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Understanding the modular architecture of RealityKit](understanding-the-realitykit-modular-architecture.md)
  Learn how everything fits together in RealityKit.
- [Using transforms to move, scale, and rotate entities](understanding-transforms.md)
  Learn how to use Transforms to move, scale, and rotate entities in RealityKit.
- [Capturing screenshots and video from Apple Vision Pro for 2D viewing](capturing-screenshots-and-video-from-your-apple-vision-pro-for-2d-viewing.md)
  Create screenshots and record high-quality video of your visionOS app and its surroundings for app previews.
- [Implementing object tracking in your app](implementing-object-tracking-in-your-app.md)
  Create engaging interactions by training models to recognize and track real-world objects in people’s surroundings.
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.
- [Manipulating entities with solid collisions](manipulating-entities-with-solid-collisions.md)
  Extend the capabilities of your app by using entities, components, and systems to maintain solid collisions when manipulating entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/designing-no-code-games-in-reality-composer-pro-3)*