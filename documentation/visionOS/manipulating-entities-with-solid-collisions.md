# Manipulating entities with solid collisions

**Framework**: visionOS

Extend the capabilities of your app by using entities, components, and systems to maintain solid collisions when manipulating entities.

**Availability**:
- visionOS 26.0+
- Xcode 26.0+

#### Overview

Set up an interaction using [`ManipulationComponent`](https://developer.apple.com/documentation/RealityKit/ManipulationComponent),  [`ForceEffectComponent`](https://developer.apple.com/documentation/RealityKit/ForceEffectComponent), and custom components that maintain solid collisions while manipulating entities. This sample shows how to create a proxy [`Entity`](https://developer.apple.com/documentation/RealityKit/Entity) that follows the manipulated entity using forces. Because it is moved with forces, the proxy bumps into solid objects as person drags the entity with their hand.

#### Configure the Entity with a Custom Component

After configuring an entity with [`ManipulationComponent`](https://developer.apple.com/documentation/RealityKit/ManipulationComponent), it passes through other colliders while using the gesture. The entity ignores other colliders because its motion is guided by the person’s hand. To create an interaction where an entity respects collisions and forces during a gesture, this sample moves the visual components from the “real” entity to a “proxy” entity for the duration of the gesture. With the real entity invisible and the proxy entity visible, [`ForceEffectComponent`](https://developer.apple.com/documentation/RealityKit/ForceEffectComponent) applies forces to the proxy entity that move it toward the real entity. This creates an interaction where you can manipulate the entity, but it no longer passes through solid colliders.

An extension for the custom [`Component`](https://developer.apple.com/documentation/RealityKit/Component), `ManipulateWithSolidCollisionsComponent`, configures the entity for the interaction. This method first creates and places a proxy entity as a descendant of the real entity. Then it copies the real entity’s [`ModelComponent`](https://developer.apple.com/documentation/RealityKit/ModelComponent) and [`GroundingShadowComponent`](https://developer.apple.com/documentation/RealityKit/GroundingShadowComponent) onto the proxy.

For more information about the entity component system (ECS) in RealityKit, see [`Implementing systems for entities in a scene`](https://developer.apple.com/documentation/RealityKit/implementing-systems-for-entities-in-a-scene).

#### Modify Entities at Specific Moments During a Gesture

To run code at specific moments during a manipulation gesture for a specific entity use [`ManipulationEvents.WillBegin`](https://developer.apple.com/documentation/RealityKit/ManipulationEvents/WillBegin) and [`ManipulationEvents.WillRelease`](https://developer.apple.com/documentation/RealityKit/ManipulationEvents/WillRelease). To subscribe to these events, the sample first subscribes to [`ComponentEvents.DidAdd`](https://developer.apple.com/documentation/RealityKit/ComponentEvents/DidAdd) inside the initializer for a custom system.

```swift
// Subscribe to an event for when the component is added.
scene.subscribe(to: ComponentEvents.DidAdd.self,
                componentType: ManipulateWithSolidCollisionsComponent.self,
                onDidAddManipulateWithSolidCollisionsComponent).store(in: &subscriptions)
```

When the custom component is added to an entity, the app subscribes to the manipulation events on the entity.

```swift
// Subscribe to manipulation events when ManipulateWithSolidCollisionsComponent is added to an entity.
event.entity.scene?.subscribe(to: ManipulationEvents.WillBegin.self,
                              on: event.entity,
                              onManipulationWillBegin).store(in: &subscriptions)
event.entity.scene?.subscribe(to: ManipulationEvents.WillRelease.self,
                              on: event.entity,
                              onManipulationWillRelease).store(in: &subscriptions)
```

When the manipulation gesture begins, the app hides the real entity and reveals the proxy. To do this, the app copies [`PhysicsBodyComponent`](https://developer.apple.com/documentation/RealityKit/PhysicsBodyComponent), [`CollisionComponent`](https://developer.apple.com/documentation/RealityKit/CollisionComponent), and [`OpacityComponent`](https://developer.apple.com/documentation/RealityKit/OpacityComponent) from the real entity to the proxy:

```swift
// Copy physics components from the real entity to the proxy.
if let physicsBody = event.entity.components[PhysicsBodyComponent.self] {
    proxy.components.set(physicsBody)
    event.entity.components.remove(PhysicsBodyComponent.self)
}
if var collision = event.entity.components[CollisionComponent.self] {
    collision.filter.group = ManipulateWithSolidCollisionsComponent.proxyGroup
    proxy.components.set(collision)
    event.entity.components.remove(CollisionComponent.self)
}
if let opacity = event.entity.components[OpacityComponent.self] {
    proxy.components.set(opacity)
}
event.entity.components[OpacityComponent.self]?.opacity = 0
```

> **Note**: Use a [`CollisionGroup`](https://developer.apple.com/documentation/RealityKit/CollisionGroup) to control how a collider interacts with other colliders and forces in your scene.

The inverse operations occur when a person releases the entity and the app transfers the components back to the real entity.

#### Use Forces to Move the Entity with Realistic Physics

During the manipulation gesture, a custom [`System`](https://developer.apple.com/documentation/RealityKit/System) runs code each frame to apply a [`ForceEffectComponent`](https://developer.apple.com/documentation/RealityKit/ForceEffectComponent) to the real entity. [`ConstantRadialForceEffect`](https://developer.apple.com/documentation/RealityKit/ConstantRadialForceEffect) attracts physics bodies to its center. [`DragForceEffect`](https://developer.apple.com/documentation/RealityKit/DragForceEffect) applies a force opposite to an entity’s direction of motion. Together these forces move the proxy entity toward the real entity during the manipulation gesture.

Additionally, configure each [`ForceEffect`](https://developer.apple.com/documentation/RealityKit/ForceEffect) with a mask so that forces are only applied to entities that belong to a particular group.

```swift
// `ConstantRadialForce` will attract entities toward its center.
// This force will cause the proxy entity to move toward the real entity.
let constantForceEffect = ConstantRadialForceEffect(
    strength: strength * strengthMultiplier,
)

// Apply a drag force to avoid orbiting.
// Without this force, the proxy entity will be difficult to control.
let dragForceEffect = DragForceEffect(strength: strength)

// Set the `ForceEffectComponent` on the real entity.
entity.components.set(ForceEffectComponent(effects: [
    // Use a collision group as a mask to only affect colliders in the group.
    ForceEffect(effect: constantForceEffect, mask: ManipulateWithSolidCollisionsComponent.proxyGroup),
    ForceEffect(effect: dragForceEffect, mask: ManipulateWithSolidCollisionsComponent.proxyGroup)
]))
```

## See Also

- [Reality Composer Pro](../RealityComposerPro/RealityComposerPro.md)
  Build, design, and orchestrate 3D content for your RealityKit apps.
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
- [Gaussian splats on visionOS](gaussian-splats-on-visionos.md)
  Use the new Gaussian splat APIs available in RealityKit in visionOS 27.
- [Manipulating models with RealityKit](../RealityKit/manipulating-models-with-realitykit.md)
  Interact with detailed 3D models using manipulation and clipping controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/manipulating-entities-with-solid-collisions)*