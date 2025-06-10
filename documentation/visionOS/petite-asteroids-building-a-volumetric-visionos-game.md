# Petite Asteroids: Building a volumetric visionOS game

**Framework**: visionOS

Use the latest RealityKit APIs to create a beautiful video game for visionOS.

**Availability**:
- visionOS 26.0+ (Beta)
- Xcode 26.0+ (Beta)

#### Overview

This sample code project uses RealityKit for visionOS to create a video game that tells the story of a lost chondrite as she collects her missing rock friends in a beautifully rendered environment.

![A screenshot of a towering butte presented in a volume within a mixed reality space running inside the visionOS simulator.](https://docs-assets.developer.apple.com/published/5c5cbc2b0a27d9ff68fcc88012c36f5b/petite-asteroids-overview%403x.png)

The sample shows you how to use native APIs to leverage the full power of Apple Vision Pro in a real-world scenario. Its code and assets provide examples and inspiration so that you can create your own spectacular apps and games for Apple Vision Pro.

#### Climb the Butte with Gestures

After our hero crash-lands on Earth, you begin controlling her movement using hand input. By pinching and dragging with your hand, you can guide the character toward her destination. And by looking and tapping at a target destination, the character leaps into the air, allowing her to begin the treacherous journey up the rocky landmark.

Use a [`SpatialTapGesture`](https://developer.apple.com/documentation/SwiftUI/SpatialTapGesture) to handle jumping.

```swift
.gesture(SpatialTapGesture()
    // Target this gesture to only entities with the custom component.
    .targetedToEntity(where: .has(LevelInputTargetComponent.self))
    // Have the character jump when the gesture ends.
    .onEnded() { event in
        // Guard for the character's container entity.
        guard let containerEntity = appModel.character.parent else { return }
        
        // Convert the tap position to scene space.
        var targetPosition = event.convert(event.location3D, from: .local, to: .scene)
        
        // Next, convert the scene space position to one in the character's container entity space.
        targetPosition = containerEntity.convert(position: targetPosition, from: nil)

        // Pass the jump target position to a custom component for this game.
        appModel.character.components[CharacterMovementComponent.self]?.targetJumpPosition = targetPosition
        
        // Reset the jump buffer timer, which helps the game feel more responsive when players try to jump a few frames before hitting the
        // ground.
        appModel.character.components[CharacterMovementComponent.self]?.jumpBufferTimer = GameSettings.jumpBufferTime
    
    // Enable the gesture only when the player is actively playing the game.
    }, isEnabled: appModel.root.observable.components[GamePlayStateComponent.self]?.isPlayingGame == true)
```

A separate [`DragGesture`](https://developer.apple.com/documentation/SwiftUI/DragGesture) handles character movement, and an `@State` field on the reality view tracks the drag start position. After converting the drag start position and current position into the scene’s coordinate space, calculate the input direction and pass it to the character movement component.

```swift
// Get the drag position in scene space.
let dragPosition = event.convert(event.location3D, from: .local, to: .scene)
        
// Start the drag if the player isn't already dragging.
if !isDragging {
    dragStartPosition = dragPosition
    isDragging = true
}
        
// ...
     
// Normalize the scene space drag translation and pass it to the character movement component.
let inputDirection = (dragPosition - dragStartPosition) / GameSettings.dragRadius
appModel.character.components[CharacterMovementComponent.self]?.inputMoveDirection = inputDirection
```

To improve the player’s experience using a drag gesture to move the character, update the drag start position to follow behind the current drag position if the player drags beyond a specific radius.

```swift
// Convert the drag start and current position to the local space of the physics root.
let dragPositionInPhysicsSpace = physicsRoot.convert(position: dragPosition, from: nil)
var dragStartPositionInPhysicsSpace = physicsRoot.convert(position: dragStartPosition, from: nil)
// Project the drag start position to an XZ plane that's parallel to the current drag position.
dragStartPositionInPhysicsSpace.y = dragPositionInPhysicsSpace.y
// Get the drag translation in the XZ plane of the local space of the physics root.
let dragDelta = (dragPositionInPhysicsSpace - dragStartPositionInPhysicsSpace)

// Move the drag start position so that it follows behind the current drag position so the player doesn't have to move their hand all
// the way back to change direction.
let dragDistance = length(dragDelta)
let dragRadius = GameSettings.dragRadius / GameSettings.scale
if dragDistance > dragRadius {
    let normalizedDragDelta = dragDelta / dragDistance
    dragStartPositionInPhysicsSpace = dragPositionInPhysicsSpace - normalizedDragDelta * dragRadius
}

// Update the scene-space drag-start position.
dragStartPosition = physicsRoot.convert(position: dragStartPositionInPhysicsSpace, to: nil)
```

#### Rotate the World in a Mixed Space

In this game, the world itself rotates as the character circles the butte. All physics entities in this sample app are descendants of a [`PhysicsSimulationComponent`](https://developer.apple.com/documentation/RealityKit/PhysicsSimulationComponent) entity. When you translate, rotate, or scale this entity, the entire physics world transforms with it. The physics simulation component entity serves as the root entity for the physics world, and you can move it like a camera inside custom systems (although the transformations are inverted). For more information, see [`Handling different-sized objects in physics simulations`](https://developer.apple.com/documentation/RealityKit/handling-different-sized-objects-in-physics-simulations).

Before animating the physics root, create an extension method to interpolate floating-point values using a damping function. This makes animations feel less abrupt.

```swift
private func dampingFactor(smoothing: Float, deltaTime: Float) -> Float {
    smoothing == 0 ? 0 : 1 - exp2(-deltaTime / smoothing)
}

public extension Float {
    /// Perform a damped interpolation between the current value and a target value.
    mutating func lerpTo(_ targetFloat: Float, smoothing: Float, deltaTime: Float) {
        self = simd_mix(self, targetFloat, dampingFactor(smoothing: smoothing, deltaTime: deltaTime))
    }
}
```

Additionally, to perform the necessary calculations to determine which direction the butte rotates, the sample uses helper functions to derive the signed angle between two directions.

```swift
public func angleBetween(from fromVector: SIMD3<Float>, to toVector: SIMD3<Float>) -> Float {
    acos(simd_clamp(dot(normalize(fromVector), normalize(toVector)), -1, 1))
}

public func signedAngleBetween(from fromVector: SIMD3<Float>, to toVector: SIMD3<Float>, axis: SIMD3<Float>) -> Float {
    let sign: Float = dot(cross(fromVector, toVector), axis) > 0 ? 1 : -1
    let angleBetween = angleBetween(from: fromVector, to: toVector)
    return angleBetween * sign
}
```

There is no camera entity in this sample code project. Instead, the butte itself rotates as the character progresses through the level. When the character moves outside a threshold, the sample calculates the angle necessary to rotate the butte so the character is always visible to the player.

```swift
// Get the direction to the follow target entity.
var toFollowTarget = rotationComponent.followTarget.position(relativeTo: rotationEntity)
toFollowTarget.y = 0

// Calculate the angle between the follow target and the forward direction.
var forwardDirection = rotationEntity.convert(direction: .forward, from: nil)
forwardDirection.y = 0
let angleBetweenForward = signedAngleBetween(from: toFollowTarget, to: forwardDirection, axis: [0, 1, 0])
let isOutsideThreshold = abs(angleBetweenForward) > rotationComponent.rotationThreshold

// Determine whether the target entity is in the camera rotation deadzone.
let distance = length(SIMD3<Float>(rotationComponent.followTarget.position.x, 0, rotationComponent.followTarget.position.z))
let isInHorizontalDeadzone = distance <= rotationComponent.deadZoneRadiusAndHeight.radius
let height = rotationComponent.followTarget.position.y
let isInDeadzone = (isInHorizontalDeadzone && height >= rotationComponent.deadZoneRadiusAndHeight.height)
    || height >= rotationComponent.deadzoneMinHeight

// When outside the threshold, calculate a new rotation for the butte that brings the player back within the threshold.
if isOutsideThreshold && isInDeadzone == false {
    let angleDifference = if angleBetweenForward > 0 {
        angleBetweenForward - rotationComponent.rotationThreshold
    } else {
        angleBetweenForward + rotationComponent.rotationThreshold
    }
    rotationComponent.targetAngle = rotationComponent.angle + angleDifference
}

// Increase the rotation smoothing when inside the deadzone, and decrease it back to its normal value when outside.
if isInDeadzone {
    rotationComponent.dyanamicRotationSmoothing.lerpTo(1, smoothing: 1, deltaTime: deltaTime)
} else {
    rotationComponent.dyanamicRotationSmoothing.lerpTo(rotationComponent.rotationSmoothing, smoothing: 1.5, deltaTime: deltaTime)
}

// Rotate the camera rotation angle toward the target rotation angle.
rotationComponent.angle
    .lerpTo(rotationComponent.targetAngle, smoothing: rotationComponent.dyanamicRotationSmoothing, deltaTime: deltaTime)
```

#### Prepare Assets for Gameplay

Using third-party digital content creation (DCC) tools to create the visual assets for this sample app, you can export those assets as USD files, and then import and arrange them inside Reality Composer Pro. Then you can apply custom components to the entities in a Reality Composer Pro scene, and custom systems can look for those components to process entities for gameplay. For more information, see [`Designing RealityKit content with Reality Composer Pro`](designing-realitykit-content-with-reality-composer-pro.md).

To generate the collision component that uses the shape of the butte, you first use a DCC to generate a model that matches the shape of the butte and platforms, but that contains fewer vertices. In Reality Composer Pro, you apply a custom component to the model entity. The custom system looks for that component by subscribing to the [`ComponentEvents.DidAdd`](https://developer.apple.com/documentation/RealityKit/ComponentEvents/DidAdd) event for a custom type in the initializer for a custom system.

```swift
// Store subscriptions in a list.
var subscriptions: [AnyCancellable] = .init()

required init (scene: Scene ) {
    // Register the `onDidAddCompoundCollisionMarker` callback when adding a custom component to an `Entity`.
    // The callback runs on the scene load.
    scene.subscribe(
        to: ComponentEvents.DidAdd.self,
        componentType: CompoundCollisionMarkerComponent.self,
        onDidAddCompoundCollisionMarker
    ).store(in: &subscriptions)
}
```

On the first scene load, RealityKit adds the component to an entity. The custom system searches for model components that descend from that entity. The system then creates a collision component on the entity using all the shapes that the mesh data generates.

To perform a recursive operation on each descendant entity, the sample uses an extension method for [`Entity`](https://developer.apple.com/documentation/RealityKit/Entity).

```swift
/// A recursive search of all descendants with a specific component.
public func forEachDescendant<T: Component>(withComponent componentClass: T.Type, _ closure: (Entity, T) -> Void) {
    for descendant in children {
        
        // Run the closure using the subentity and its component as parameters.
        if let component = descendant.components[componentClass] {
            closure(descendant, component)
        }
        
        // Call this same function for each descendant entity.
        descendant.forEachDescendant(withComponent: componentClass, closure)
    }
}
```

You can then use this extension method to generate the shape data for every descendant model component.

```swift
var meshes = [(entity: Entity, mesh: MeshResource)]()
collisionRoot.forEachDescendant(withComponent: ModelComponent.self) {
    (entity, modelComponent) in
    
    // Skip descendant entities that you don't want to become part of the collision shape.
    guard entity.components.has(IgnoreCompoundCollisionMarkerComponent.self) == false else { return }
    
    meshes.append((entity: entity, mesh: modelComponent.mesh))
    
    // Optionally, delete the source model component if you're no longer using it.
    if deleteModel {
        entity.components.remove(ModelComponent.self)
    }
}
```

Next, use [`generateStaticMesh(from:)`](https://developer.apple.com/documentation/RealityKit/ShapeResource/generateStaticMesh(from:)) to create a shape from each discovered mesh resource, and then offset that shape relative to the collision root entity (the original entity with the custom component).

```swift
for (entity, mesh) in meshes {
    // Generate the shape from the mesh data.
    guard var shape = if isStatic {
        try? await ShapeResource.generateStaticMesh(from: mesh)
    } else {
        try? await ShapeResource.generateConvex(from: mesh)
    } else {
        continue
    }
    
    // Offset the shape by its translation and orientation relative to the collision root.
    shape = shape.offsetBy(rotation: entity.orientation(relativeTo: collisionRoot), translation: entity.position(relativeTo: collisionRoot))
    shapes.append(shape)
}
```

Finally, the sample initializes the collision component with the array of shapes and then adds it to the collision root.

```swift
let collision = CollisionComponent(shapes: shapes, mode: collisionMode)
collisionRoot.components.set(collision)
```

#### Structure Your Project for Development

During development, many people with a diverse set of expertise work on the same Xcode project and in the same Reality Composer Pro scenes. It’s important to think strategically about your project structure to avoid cumbersome merge conflicts or accidentally undoing someone else’s changes.

Within Reality Composer Pro, USD references allow you to isolate your work to individual files. The same asset becomes available for reference multiple times throughout a Reality Composer Pro project.

As an example, in this sample code project, the original materials are in a separate scene. Additionally, the main materials scene instances and reuses custom node graphs in other materials. One example is `DropShadow`, the node graph for rendering drop shadows.

![A screenshot of a custom shader created with Shader Graph that renders drop shadows for the sample.](https://docs-assets.developer.apple.com/published/33c163485ffe0db4e1ed9803f25002a7/drop-shadow-shader-graph%403x.png)

For USD assets, the source models are in their own folder. These assets don’t have applied materials, and don’t contain any configuration data necessary for gameplay.

![A screenshot of a folder inside the Reality Composer Pro project containing unmodified source assets.](https://docs-assets.developer.apple.com/published/ffdcb62fffbf2029abc5cb671ed6db86/source-models%403x.png)

> ❗ **Important**: Be mindful of the size of your assets during development. Textures and other large assets affect the build times for your app.

In the `GameAssets` folder, create game assets by configuring source assets with materials and any custom component data necessary. Those game assets are then ready for a designer to assemble into levels.

![A screenshot of many different modular assets in the GameAssets folder inside the Reality Composer Pro project.](https://docs-assets.developer.apple.com/published/a09dfab36450f7ba6ff216cfee75dcf2/game-assets%403x.png)

Finally, assemble the game assets in the completed game level scene.

![A screenshot of the main level scene inside Reality Composer Pro.](https://docs-assets.developer.apple.com/published/9f59c47ebc3884ff46e4b0d22cd7bd5f/main-level-scene%403x.png)

#### Create Effects with the Shader Graph

Adopting a variety of techniques, including making custom materials with [`ShaderGraph`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/) in Reality Composer Pro, promotes efficient rendering of the towering landmark at the center of the hero’s journey. A combination of baked light maps, which you generate in an external DCC, and clever lighting techniques come together to make the player’s experience smooth and rewarding.

Unlit materials are very performant because they don’t require lighting calculations from the GPU to determine their color. The materials for the butte use textures you create in an external DCC, allowing you to calculate shadows from the sun ahead of time, and preventing real-time lights from casting shadows onto the butte.

To achieve effective grounding shadows beneath the character, perform a raycast downward from her position and check for collisions with geometry. `calculateParametersForShadow` implements the check and returns shader parameters in a tuple.

```swift
func calculateParametersForShadow(_ entity: Entity, _ physicsRoot: Entity) -> (characterPosition: SIMD3<Float>, shadowPosition: SIMD3<Float>)? {
    // Get the origin relative to the physics root entity.
    let origin = entity.position(relativeTo: physicsRoot)
    
    // Peform a raycast against the scene downward from the origin.
    return if let hit = entity.scene?.raycast(
        origin: origin,
        direction: [0, -1, 0],
        query: .nearest,
        // Use a mask to make sure you're only performing a raycast against entities in the shadow receiver group.
        mask: GameCollisionGroup.shadowReceiver.collisionGroup,
        relativeTo: physicsRoot
    ).first {
        // Return a tuple when the raycast is successful.
        (origin, hit.position)
    } else {
        nil
    }
}
```

On each frame, the CPU calculates the shader parameters and passes them to the GPU. This happens in the update function of a custom system.

```swift
func update(context: SceneUpdateContext) {
    // Guard for the physics root and the character entity.
    guard let physicsRoot = context.first(withComponent: PhysicsSimulationComponent.self)?.entity,
            let character = context.first(withComponent: CharacterMovementComponent.self)?.entity else { return }
    
    // Get the matrix that transforms from world space to level space.
    let worldToLevelMatrix = physicsRoot.transformMatrix(relativeTo: nil).inverse
    
    // Raycast downward to determine where the character's shadow lands.
    if let (characterPosition, characterShadowPosition) = calculateParametersForShadow(character, physicsRoot) {
        
        // Raycast downward for each rock friend to determine where their shadows land.
        var rockFriendPositions = [(position: SIMD3<Float>, shadowPosition: SIMD3<Float>)]()
        for rockFriend in context.entities(matching: rockFriendQuery, updatingSystemWhen: .rendering) {
            if let (friendPosition, friendShadowPosition) = calculateParametersForShadow(rockFriend, physicsRoot) {
                rockFriendPositions.append((friendPosition, friendShadowPosition))
            }
        }
        
        // Set the shader parameters in a custom function.
        for dropShadowReceiver in context.entities(matching: dropShadowReceiverQuery, updatingSystemWhen: .rendering) {
            setShadowShaderParameters(
                entity: dropShadowReceiver,
                characterPosition: characterPosition,
                characterShadowPosition: characterShadowPosition,
                worldToLevelMatrix: worldToLevelMatrix,
                rockFriendPositions: rockFriendPositions)
        }
    }
}
```

Inside `setShadowShaderParameters`, the sample sets the properties on the custom material by getting a reference to the `ShaderGraphMaterial` on the entity’s [`ModelComponent`](https://developer.apple.com/documentation/RealityKit/ModelComponent). The sample then applies the modified shader graph material back to the shadow receiver entity directly.

```swift
func setShadowShaderParameters (
    entity: Entity,
    characterPosition: SIMD3<Float>,
    characterShadowPosition: SIMD3<Float>,
    worldToLevelMatrix: simd_float4x4,
    rockFriendPositions: [(SIMD3<Float>, SIMD3<Float>)]
) {
    // Guard for the entity's model component and a custom shadow receiver component.
    guard let modelComponent = entity.components[ModelComponent.self],
            let shadowReceiver = entity.components[DropShadowReceiverModelComponent.self] else { return }
    
    // Iterate through each shadow material on this model and apply the shadow shader parameters.
    for index in shadowReceiver.shadowMaterialIndices {
        guard var shaderGraphMaterial = modelComponent.materials[index] as? ShaderGraphMaterial else { continue }

        try? shaderGraphMaterial.setParameter(
            handle: shadowReceiver.worldToLevelMatrixParameterHandle,
            value: .float4x4(worldToLevelMatrix))
        try? shaderGraphMaterial.setParameter(
            handle: shadowReceiver.characterPositionParameterHandle,
            value: .simd3Float(characterPosition))
        try? shaderGraphMaterial.setParameter(
            handle: shadowReceiver.characterShadowPositionParameterHandle,
            value: .simd3Float(characterShadowPosition))

        for friendIndex in 0..<rockFriendPositions.count {
            let rockFriendPosition = rockFriendPositions[friendIndex].0
            let rockFriendShadowPosition = rockFriendPositions[friendIndex].1
            try? shaderGraphMaterial.setParameter(
                handle: shadowReceiver.rockFriendPositionParameterHandles[friendIndex],
                value: .simd3Float(rockFriendPosition))
            try? shaderGraphMaterial.setParameter(
                handle: shadowReceiver.rockFriendShadowPositionParameterHandles[friendIndex],
                value: .simd3Float(rockFriendShadowPosition))
        }
        
        try? shaderGraphMaterial.setParameter(
            handle: shadowReceiver.rockFriendShadowRadiusHandle,
            value: .float(0.45))
        
        // Set the material directly onto the entity with the model component.
        entity.components[ModelComponent.self]?.materials[index] = shaderGraphMaterial
    }
}
```

> ❗ **Important**: Updating parameters on an entity’s material can be computationally expensive. Avoid sharing shader graph material handles between entity instances, or setting the model component back on the entity unnecessarily.

## See Also

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
- [Designing RealityKit content with Reality Composer Pro](designing-realitykit-content-with-reality-composer-pro.md)
  Design RealityKit scenes for your visionOS app.
- [Capturing screenshots and video from Apple Vision Pro for 2D viewing](capturing-screenshots-and-video-from-your-apple-vision-pro-for-2d-viewing.md)
  Create screenshots and record high-quality video of your visionOS app and its surroundings for app previews.
- [Implementing object tracking in your visionOS app](implementing-object-tracking-in-your-visionos-app.md)
  Create engaging interactions by training models to recognize and track real-world objects in your app.
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/petite-asteroids-building-a-volumetric-visionos-game)*