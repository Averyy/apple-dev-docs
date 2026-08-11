# Chaparral Village: Building an immersive visionOS adventure game

**Framework**: visionOS

Create an adventure game using SwiftUI, RealityKit, and Reality Composer Pro 3.

**Availability**:
- visionOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

Chaparral Village is an adventure game that transports you into a miniature clay landscape that demonstrates how to build an immersive video game on visionOS with Reality Composer Pro, RealityKit, and SwiftUI.

![A 3D-rendered scene of a miniature clay village built atop a rocky base. At its center stands a tall dome-shaped hut with an overturned clay dish for a roof, surrounded by smaller adobe buildings, cacti, and dried branches.](https://docs-assets.developer.apple.com/published/43a55b3fae0e0473e2c4a6db97beaa1e/Chaparral-Village-OverviewImage%402x.png)

This sample uses a number of RealityKit and Reality Composer Pro features, including navigation mesh, animation graph, cloth simulation, and baked lighting. It also demonstrates how to use the plug-in interface in Reality Composer Pro to create custom RealityKit components and systems.

> **Note**: This sample code project is associated with WWDC26 sessions 279: [`Explore advances in RealityKit`](https://developer.apple.comhttps://developer.apple.com/wwdc26/279/), 280: [`Iterate your spatial scenes faster with Reality Composer Pro 3`](https://developer.apple.comhttps://developer.apple.com/wwdc26/280/), 281: [`Extend Reality Composer Pro 3 functionality with Xcode`](https://developer.apple.comhttps://developer.apple.com/wwdc26/281/), and 393: [`Supercharge your spatial workflows with Reality Composer Pro 3`](https://developer.apple.comhttps://developer.apple.com/wwdc26/393/).

#### Build Plug Ins for Reality Composer Pro

The core functionality of Chaparral Village is driven by a collection of custom RealityKit components and systems, all written in Swift. These handle everything from foundational systems like input and player navigation to gameplay features like potions, portals, and props.

Make custom components and systems accessible in the Reality Composer Pro editor by adopting the `RealityComposerProPlugin` interface and registering them in its `setup` method:

```swift
public final class RCPCustomComponentsPlugin: RealityComposerProPlugin {
    
    // ...
    
    public func setup(context: any RealityComposerProContext) {
        // Register custom components.
        context.registerComponent(Player.self)
        // ...
        
        // Register custom systems.
        context.registerSystem(PlayerSystem.self)
        // ...
    }
    
    /// Returns a new instance of the plug-in. Making `init()` public would
    /// change the API contract that Reality Composer Pro defines, so use this factory instead.
    public static func create() -> RCPCustomComponentsPlugin {
        return RCPCustomComponentsPlugin()
    }
}    
```

Ensure Reality Composer Pro can discover and load the plug-in by exposing a C entry point:

```swift
@_cdecl("createRealityComposerProPlugin")
public func createRealityComposerProPlugin() -> UnsafeMutableRawPointer {
    return RCPCustomComponentsPlugin().passRetained()
}
```

The sample has a custom `RCPCustomComponents` build target which packages the plug-in and all of the components and systems it registers into a framework. The target also automatically moves the framework into a Plugin Directory folder which Reality Composer Pro has access to.

> **Note**: In Reality Composer Pro, you can set the location of the Plugin Directory in Project Settings > Build > Plugin Directory. See the `InstallPlugin.sh` script in the sample download for an example of how to automatically move the framework to the Plugin Directory when it’s built.

Using the plug-in model makes your custom components available directly inside Reality Composer Pro and allows you to preview your custom systems’ behavior instantly in the editor, without having to deploy to device or simulator.

For more information about the Reality Composer Pro plug-in interface, see the [`RealityComposerPro Plugin Interface`](https://developer.apple.comhttps://github.com/apple/reality-composer-pro-plugin) GitHub repository.

#### Create Cutscenes with Script Graph and Swift

When Chaparral Village starts, a cutscene plays that displays a series of dialogue prompts introducing the main characters and teaching the player how to play the game. The sample contains the majority of its cutscene logic in Script Graph, but relies on bidirectional communication between Script Graph and Swift to react to events and display SwiftUI views.

Cutscenes begin playing when they receive the `On Play Cutscene` event in Script Graph, which the sample defines in a Node Library asset:

To make custom nodes, events, and types accessible in both Script Graph and Swift, define them in a Node Library asset in Reality Composer Pro.

The sample defines a scene extension method in Swift that sends the `On Play Cutscene` event:

```swift
import RealityKitScripting
    
public enum Cutscene: CodingKey, CaseIterable, Codable, Hashable, Equatable, Sendable, InspectableEnum {
    case intro
    case ladder
    case village
    case alchemistLab
    case shrinkPotionCrafted
    case ending
    
    public typealias CodingKeys = Self
}  
    
public struct PlayCutscene: Inspectable {
    public var cutscene: Cutscene
    
    public init(cutscene: Cutscene) {
        self.cutscene = cutscene
    }
}

extension Scene {
    public func send(_ event: PlayCutscene) {
        self.send(name: "PlayCutscene", with: [
            "Cutscene": event.cutscene
        ])
    }
}  
```

The Swift code sets the `name` property to the same string set as the `Identifier` property in the Node Library so the event resolves correctly. For more examples of how to communicate between Swift and Script Graph, see [`Designing no-code games with Reality Composer Pro 3`](designing-no-code-games-in-reality-composer-pro-3.md).

Conversely, Script Graph can initiate logic in Swift by invoking nodes which link to methods written in Swift. For example, the `Show Single Dialog` subgraph in the cutscene Script Graph invokes the `Present Dialog` node. The sample declares this node in its Node Library, linking it to a Swift method with the signature `present(Entity, Number, Number, Entity)`:

Reality Composer Pro can link to the `present` method because the sample bundles it in a `RealityKitScripting.Module` and registers it with the scripting runtime. For more information about the scripting runtime, see the [`RealityKitScripting`](https://developer.apple.comhttps://github.com/apple/realitykitscripting) GitHub repository.

In Swift, the `present` method then displays a SwiftUI attachment with the dialog text:

```swift
extension Dialog {
    // ...
    public static func present(
        on entity: Entity,
        sections: [String],
        width: Float,
        height: Float,
        at marker: Entity,
    ) async throws {
        #if os(macOS)
        return // Automatically advance through dialog on macOS which cannot present dialogs.
        #else
        guard var dialog = entity.components[Dialog.self] else {
            throw Error.noDialog
        }
        // ...
        let transform = marker.transformMatrix(relativeTo: nil)
        try await withCheckedThrowingContinuation { continuation in
            let attachment = Entity()
            let model = DialogModel(
                // ...
            )
            attachment.components.set(ViewAttachmentComponent(rootView: DialogView(model: model)))
            entity.addChild(attachment)
            dialog.active = model
            entity.components.set(dialog)
            attachment.setTransformMatrix(transform, relativeTo: nil)
        }
        #endif
    }
}
```

Bridging Script Graph and Swift allows you to leverage the full suite of features RealityKit and SwiftUI provide, such as view attachments and localization. For more information on bridging functionality between Swift and Reality Composer Pro, watch the WWDC26 session, [`Extend Reality Composer Pro 3 functionality with Xcode`](https://developer.apple.comhttps://developer.apple.com/wwdc26/281/).

#### Handle Input From Any Source

Chaparral Village uses a custom `InputManager` class to handle tap and drag input events in a source-agnostic manner:

```swift
public final class InputManager: SceneBound, Inspectable {
    
    // ...
    public static var sceneToValue: [RealityKit.Scene.ID: InputManager] = [:]
    public nonisolated let id: UUID = UUID()

    @ObservationIgnored public var tapHandlers: [any TapHandler] = []
    @ObservationIgnored public var dragHandlers: [any DragHandler] = []
    
    // ...
    
    public private(set) var isActive: Bool = true
    
    // ...
    
    public init() {
        self.add(DraggableObjectHandler())
        self.add(LadderTapHandler())
        self.add(PathfindPlayerTapHandler())
        self.add(PocketDimensionTapHandler())
    }
    
    public func activate() {
        self.isActive = true
    }
    
    public func deactivate() {
        self.isActive = false
    }
    
    // ...

    public func tap(
        scene: RealityKit.Scene,
        entity: Entity,
        worldLocation: SIMD3<Float>
    ) -> InputAction {
        if !isActive {
            return .ignored
        }
        // ...
    }
    
    public func drag(
        scene: RealityKit.Scene,
        entity: Entity,
        input: DragInput
    ) -> InputAction {
        // ...
    }
}
```

When the `InputManager` is active and receives a tap input event, it forwards that event to its tap handlers for them to react to. The same is true for its drag handlers and drag input events. For example, when the person taps on the ground in the village scene the `PathfindPlayerTapHandler` moves the player that location with pathfinding, and when the person drags a dynamic physics object like a pot or ladder the `DraggableObjectHandler` naturally moves that object with momentum and physics.

One major benefit to this generic approach to input handling is that it works uniformly regardless of where the input event originates. This allows the sample to handle input the same way both in the Reality Composer Pro editor and on device.

In this sample, the `Setup Script` Script Graph forwards `On Tap` and `On Drag` events from Reality Composer Pro to the `InputManager` in Swift:

![A screenshot of the Setup Script Script Graph in Reality Composer Pro. An On Initialize node connects to an Initialize Scene node that receives the current scene. Below that, an On Tap event node forwards its parameters to a Handle Tap node, which passes its result to a Log Message node. An On Drag event node combines with Set Variable and Get Variable nodes to feed two Handle Drag nodes that route drag input to Swift.](https://docs-assets.developer.apple.com/published/6abd1271985ff1036c26c4679862fecb/Chaparral-Village-InputScriptGraph%402x.png)

Like the `present` method mentioned earlier, the sample registers the `handleTap` and `handleDrag` methods with the `RealityKitScripting` framework to make them available in Reality Composer Pro:

```swift
extension InputManager {
    public static func rksModule() -> RealityKitScripting.Module {
        return Module(rksModuleName) {
            TypeSchema<InputManager>("InputManager") {
                StaticFunc("handleTap", body: handleTap)
                StaticFunc("handleDrag", body: handleDrag)
                StaticFunc("activate") { (scene: RealityKit.Scene) in
                    scene[InputManager.self]?.activate()
                }
                StaticFunc("deactivate") { (scene: RealityKit.Scene) in
                    scene[InputManager.self]?.deactivate()
                }
            }
        }
    }

    private static func handleTap(
        scene: RealityKit.Scene,
        entity: Entity,
        position: SIMD3<Float>,
    ) -> Bool {
        guard let manager = scene[InputManager.self] else {
            return false
        }
        switch manager.tap(scene: scene, entity: entity, worldLocation: position) {
            case .handled:
                return true
            case .ignored:
                return false
        }
    }

    private static func handleDrag(
        scene: RealityKit.Scene,
        entity: Entity,
        start: SIMD3<Float>,
        current: SIMD3<Float>,
        manipulator: SIMD3<Float>?,
        isEnding: Bool,
    ) -> Bool {
        guard let manager = scene[InputManager.self] else {
            return false
        }
        let input = DragInput(start: start, current: current, manipulator: manipulator, isEnding: isEnding)
        switch manager.drag(scene: scene, entity: entity, input: input) {
            case .handled:
                return true
            case .ignored:
                return false
        }
    }
}
```

This allows you to preview tap and drag interactions directly inside Reality Composer Pro:

Additionally, the `activate` and `deactivate` methods allow the cutscene Script Graphs to turn off input during cutscenes from Reality Composer Pro.

#### Find a Path Through the Village

Chaparral Village uses a navigation mesh to allow the player to traverse the village scene while avoiding obstacles in their path.

The sample configures navigation in Reality Composer Pro by attaching a [`NavigationMeshComponent`](https://developer.apple.com/documentation/RealityKit/NavigationMeshComponent) to the Village Environment entity and a [`NavigationComponent`](https://developer.apple.com/documentation/RealityKit/NavigationComponent) to the Player entity:

![A screenshot of the Reality Composer Pro editor showing the Chaparral Village scene with navigation mesh geometry visualized on the walkable surfaces of the village terrain. The Navigation Mesh component is selected in the hierarchy on the left, and the Navigation Mesh Component inspector is visible on the right.](https://docs-assets.developer.apple.com/published/3ba09fba9f7c1d766751b194ddbdf33d/Chaparral-Village-NavigationMesh%402x.png)

The `NavigationMeshComponent` defines the walkable surfaces that entities with a `NavigationComponent` can travel across. It also defines connections between walkable surfaces that are otherwise unconnected.

When someone taps on a location in the village, the app calls the `navigate` method which computes an unobstructed path between the player’s current position and the tap location by creating a [`NavigationController`](https://developer.apple.com/documentation/RealityKit/NavigationController) for the player entity and awaiting the result of [`computePath(from:to:)`](https://developer.apple.com/documentation/RealityKit/NavigationController/computePath(from:to:)):

```swift
public func navigate(to location: SIMD3<Float>, in scene: Scene, addedTraversal: [SIMD3<Float>] = []) async {
    let navigator: NavigationController
    do {
        navigator = try NavigationController(entity: self)
    } catch {
        return
    }
    
    guard let navMeshEntity: Entity = navMeshHolder() else {
        return
    }
    
    let fromPosition = pathfindingPosition(relativeTo: navMeshEntity)
    let toPosition = navMeshEntity.convert(position: location, from: nil)
    
    guard let result = await navigator.computePath(from: fromPosition, to: toPosition) else {
        return
    }
    
    // Move the entity along the path.
}
```

The [`computePath(from:to:)`](https://developer.apple.com/documentation/RealityKit/NavigationController/computePath(from:to:)) method returns an array of [`NavigationMeshResource.PathNode`](https://developer.apple.com/documentation/RealityKit/NavigationMeshResource/PathNode) objects to represent the path a player should follow. The sample moves the player along that path by storing the locations of the path’s nodes in a custom component and advancing the player along the path each frame in a custom system. That system also smoothes the trajectory between navigation points and rotates the player to face its direction of travel. To learn more about how to move the player along a path, refer to the `PathfindPlayer.swift` file in the sample project. For more information about working with navigation meshes, see [`Building a navmesh in Reality Composer Pro`](https://developer.apple.com/documentation/RealityComposerPro/building-a-navmesh-in-reality-composer-pro).

#### Animate the Player with Animation Graph

When the player walks along a path, it seamlessly transitions from an idle animation to a walk animation. The sample controls the player’s animation states with an Animation Graph:

![A screenshot of the Animation Graph asset editor in Reality Composer Pro. Three AnimationClipNodeDefinition nodes labeled idle, walk, and spin each output into a State Machine node with corresponding idle, walk, and spin inputs, and the State Machine outputs into a Final Pose node.](https://docs-assets.developer.apple.com/published/ce6bd51ff34b4f49f26208be3c66dbed/Chaparral-Village-AnimationGraph%402x.png)

In Chaparral Village, the character uses a rigged skeleton model and three separate animation files for its `idle`, `walk`, and `spin` animations.

The Animation Graph uses a State Machine to determine the current animation and transition between animations in reaction to state changes. For example, when the `walk` variable is set to `true` in the Animation Graph, and the player is in its `idle` animation state, the character transitions to its `walk` animation. When the `walk` variable is set to false it transitions back to its idle animation:

A Script Graph on the player sets the `walk` variable in the Animation Graph to `true` when it receives the `OnPathFindStarted` scene event, and false when it receives the `OnPathFindEnded` scene event. This allows for smoothly transitioning the player into and out of its `walk` animation while traversing the path:

![A screenshot of a Script Graph with two independent branches. In the top branch, an On Scene Event node listening for OnPathFindStarted feeds a Set Entity Parameter node that sets the walk variable to true. In the bottom branch, an On Scene Event node listening for OnPathFindEnded feeds a Set Entity Parameter node that sets the walk variable to false.](https://docs-assets.developer.apple.com/published/1cc2b70bf5e9d943adbce4641b81a795/Chaparral-Village-SetEntityParameter%402x.png)

For more information about using Animation Graph in Reality Composer Pro, see [`Working with the Animation Graph`](https://developer.apple.com/documentation/RealityComposerPro/working-with-the-animation-graph).

#### Animate Curtains with Cloth Simulation

A small hut sits near the top of Chaparral Village with two curtains covering its doorway. The curtains’ movements are dynamically simulated using the [`Cloth simulation`](https://developer.apple.com/documentation/RealityKit/physics-cloth-simulation) APIs so they react naturally when the player walks through the doorway:

To configure the cloth simulation in Reality Composer Pro, the sample defines a custom `CurtainClothBodyComponent` and applies it to the curtain model entity:

![A screenshot of the Reality Composer Pro editor showing the Curtain scene in the viewport, with two curtains hanging side by side from a horizontal beam. The curtainLeft entity is selected in the hierarchy on the left, exposing a nested CurtainClothBodyComponent, and the Transform Component is shown in the inspector on the right.](https://docs-assets.developer.apple.com/published/839289162720e01b4e7ebff4259c7e02/Chaparral-Village-Curtain%402x.png)

In Swift, the `prepareCurtains` entity extension method adds a [`ClothBodyComponent`](https://developer.apple.com/documentation/RealityKit/ClothBodyComponent) to entities with a [`ModelComponent`](https://developer.apple.com/documentation/RealityKit/ModelComponent) and a `CurtainClothBodyComponent`:

```swift
let clothMesh = try ClothMeshResource(from: model.mesh)
var clothBody = ClothBodyComponent(mesh: clothMesh)
clothBody.materialNames = [component.materialName]

// Pin the vertices of `clothMesh`.
let pins = Array(entity.descendants(includeSelf: false).reading(components: CurtainPinComponent.self))
if pins.isEmpty {
    logger.warning("no CurtainPinComponent descendants found for \(entity.name); cloth will be unpinned.")
}
for (pin, pinComponent) in pins {
    let position = pin.position(relativeTo: entity)
    let shape = ClothVolumeShape.sphere(ClothSphereShape(radius: pinComponent.radius))
    let vertices = clothMesh.vertices(in: shape, center: position)
    clothBody.motionTypes.set(vertexIndices: vertices, value: .kinematic)
}

// Add `clothBody` to `clothEntity`.
entity.components.set(clothBody)
```

This method also pins the curtain to the beam that holds it up by setting the [`motionTypes`](https://developer.apple.com/documentation/RealityKit/ClothBodyComponent/motionTypes) of vertices within the radius of the pins to [`kinematic`](https://developer.apple.com/documentation/RealityKit/ClothBodyComponent/ParticleMotionType/kinematic).

The sample simulates the cloth by adding a [`ClothSimulationComponent`](https://developer.apple.com/documentation/RealityKit/ClothSimulationComponent) to the scene, and allows the player to collide with the cloth by adding a [`ClothColliderComponent`](https://developer.apple.com/documentation/RealityKit/ClothColliderComponent) to the character:

![A screenshot of the Reality Composer Pro editor showing the village scene in the viewport. In the hierarchy panel on the left, the Cloth Simulation component attached to the Village World Root entity and the Cloth Collider component attached to the Player entity are both highlighted. The inspector on the right shows the Cloth Simulation properties, including solver, solver iterations, time step, gravity, wind, and damping factor.](https://docs-assets.developer.apple.com/published/0f1bf7e475abe142ab285bf0aaaa3f1d/Chaparral-Village-ClothSimulationAndCollider%402x.png)

#### Light the Scene

Inside the hut is a cozy interior scene illuminated by a warm fire. The scene uses baked lighting to create ambiance.

To configure the light bake, the sample attaches a [`LightmapComponent`](https://developer.apple.com/documentation/RealityKit/LightmapComponent) to the Alchemy Area Env entity. The `LightmapComponent` pre-calculates indirect lighting for static objects and stores the results as a texture, so that the app can render lighting efficiently at runtime without recalculating it each frame:

![A screenshot of the Reality Composer Pro editor showing the Alchemy Area Env entity selected in the hierarchy. The viewport displays a cutaway of the hut interior with baked lighting, and the inspector on the right shows the Lightmap Component and its bake settings.](https://docs-assets.developer.apple.com/published/aa6a914f889c90266e51f3311d9831ff/Chaparral-Village-LightmapComponent%402x.png)

When the scene’s lights are in place, use the `LightmapComponent` or the Lighting Tools menu at the top right of the window to set the quality level and bake the lighting directly within Reality Composer Pro:

![A screenshot of the Lighting Tools panel in Reality Composer Pro. It contains a Lightmap Bake Quality menu set to Low, an Indirect Bounces field set to two, and buttons for Bake All Lightmaps and Capture Environment Probes. The viewport on the left shows the hut interior scene.](https://docs-assets.developer.apple.com/published/58acc119fa6af6572855937c6fd88c96/Chaparral-Village-BakeSettings%402x.png)

Although the Alchemy area has several light sources, only three render at runtime to improve performance: the room’s primary light source, and two lights in the fireplace. The sample includes the remaining lights in the light bake to create a more dynamic look, but attaches a `TurnOffOnLoad` custom component to each so the app removes them from the scene at runtime.

The sample also uses area reflector entities, which are simply planes with reflective materials, to bounce scattered light back into the scene, providing warmer, fuller lighting:

![A screenshot of the Reality Composer Pro viewport showing two large reflector planes standing vertically at right angles around the hut interior, with a light source above casting illumination that bounces off the planes back onto the hut.](https://docs-assets.developer.apple.com/published/c0b98bc0e523877b0ad2299b1f0bdc4e/Chaparral-Village-BounceLights%402x.png)

## See Also

- [Reality Composer Pro](../RealityComposerPro/RealityComposerPro.md)
  Build, design, and orchestrate 3D content for your RealityKit apps.
- [Designing no-code games with Reality Composer Pro 3](designing-no-code-games-in-reality-composer-pro-3.md)
  Build a video game in Reality Composer Pro without code using Script Graphs.
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
- [Combining 2D and 3D views in an immersive app](../RealityKit/combining-2d-and-3d-views-in-an-immersive-app.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/chaparral-village-building-an-immersive-visionos-adventure-game)*