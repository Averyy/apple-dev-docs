# Creating a navigation mesh with Reality Composer Pro

**Framework**: visionOS  
**Role**: Sample Code  
**Download**: [CreatingANavigationMeshWithRealityComposerPro.zip](https://docs-assets.developer.apple.com/published/ec56abf1037d/CreatingANavigationMeshWithRealityComposerPro.zip)

Move a character around a game level by defining its walkable surface and driving motion with a behavior tree.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- Xcode 27.0+

## Overview

This sample shows you how to build a navigation mesh in [Reality Composer Pro](https://developer.apple.com/reality-composer-pro/) and [RealityKit](../RealityKit/RealityKit.md) to control the movement of an entity around a game level. When a person taps a spot on the ground, the character turns, plays a walk cycle, and follows the shape of the terrain to reach the tapped destination.

![The Reality Composer Pro viewport showing a rocky terrain model with a small character standing on it. A cyan wireframe covers the surfaces the character can walk on, and an orange marker bridges the gap between the two raised ledges.](https://developer.apple.com/tutorials/images/com.apple.visionOS/navmesh-overview@3x.png)

This sample uses almost no Swift. The navigation mesh generated in Reality Composer Pro defines the walkable surface. A behavior tree drives the movement, and Script Graphs set the destination and animations. The Swift layer only starts the RealityKitScripting runtime and loads the scene.

> **Note**: For more on initializing the runtime and passing messages between Script Graphs and [SwiftUI](../SwiftUI/SwiftUI.md), see [Designing no-code games with Reality Composer Pro 3](./designing-no-code-games-in-reality-composer-pro-3.md).

## Generate the navigation mesh

A navigation mesh represents the walkable surface that an entity can stand on. Reality Composer Pro generates this mesh according to configurable parameters on a [`NavigationMeshComponent`](../RealityKit/navigationmeshcomponent.md) in the scene. Specify a Shapes list to restrict mesh generation to inside those shapes.

The generation parameters are all in meters, and the defaults assume a human-scale world where objects and characters are about 1 meter in size. However, this sample is a tabletop diorama roughly 0.5 meters across, so many default values are off by two orders of magnitude. If the configuration values don’t match the scale of your surface, the mesh doesn’t generate when you click Generate Navigation Mesh.

Cell Size and Cell Height refer to the resolution of voxels Reality Composer Pro samples when generating the navigation mesh, and the system ignores details smaller than these values. This sample sets both Cell Size and Cell Height to `0.01`, which is equivalent to 1 centimeter.

The sample also reduces Walkable Climb Height to `0.01`, which prevents the mesh from connecting surfaces farther apart than this value on the vertical axis.

Under Advanced, the sample sets Max Simplification Error to `0.01`. This parameter controls how closely the edges of the mesh follow the shape of the voxelized representation of the surface. Values smaller than Cell Size can create jagged edges that conform to the shape of those voxels, and equal or slightly larger values create edges that smooth out the voxel shapes.

## Bridge gaps with off-mesh connections

Generation produces polygons only where geometry exists. Gaps in the geometry produce islands in the navigation mesh that are inaccessible to each other. An off-mesh connection is a manual link that bridges those islands.

Use gizmos in the viewport to edit the Start Position and End Position of the off-mesh connection.

Set Radius to some permissive distance that allows the navigating entity to reach the start and end points from a position on your mesh. Radius needs a positive value unless the start and end points are coplanar with the face of your navigation mesh, which is often difficult to achieve consistently.

This sample sets Bidirectional to `true` to allow the character to walk back and forth across the connection. When this parameter is `false`, the connection becomes one-way and the entity can traverse the connection only if the start position is accessible. Reality Composer Pro bakes connections into the mesh at generation time, so changes don’t affect navigation until you click Generate Navigation Mesh again.

![A screenshot of the Reality Composer Pro viewport showing an off-mesh connection drawn as a line with directional cones and radius circles spanning a gap in the terrain. In the inspector, the Configuration and Off Mesh Connections settings are visible, showing values scaled appropriately for the scene.](https://developer.apple.com/tutorials/images/com.apple.visionOS/navmesh-off-mesh-connection@3x.png)

## Move the character with a behavior tree

For an entity to navigate along a navigation mesh, it needs a [`NavigationComponent`](../RealityKit/navigationcomponent.md), but this component alone doesn’t move the entity.

The Move on Navigation Mesh node in the entity’s behavior tree moves an entity to the position parameter. This sample uses a parameter named `Navigation Target` and a simple behavior tree, because navigating is the only behavior the entity requires.

![A screenshot of the Player_Behavior behavior tree in Reality Composer Pro, showing a Root node connected to a Move on Navigation Mesh node. In the Inspector, Can Navigate, Move Speed, and Navigation Target are defined as inputs for the behavior tree.](https://developer.apple.com/tutorials/images/com.apple.visionOS/navmesh-behavior-tree@3x.png)

The behavior tree defines Inputs — entity parameters the behavior tree can read from the entity to modify its execution. The Move on Navigation Mesh node requires two input parameters, one of type `Vector3` and one of type `float`. This sample names them `Navigation Target` and `Move Speed`, and configures the node to use them. These names match the entity parameter names that a Script Graph sets on the entity.

This sample uses a series of Script Graphs to pass along data from the player’s tap inputs against the scene geometry to the behavior tree, and finally to the navigation system so the entity can move around on the navigation mesh.

The `TapTerrain` Script Graph emits a `Scene Event` with a `Vector3` parameter named `Tap_Position` each time the player taps the collider on the `Terrain` entity. Scene events propagate to any Script Graph in the current scene that’s listening for an event with the same name.

On the player entity, a Script Graph named `PlayerLogic` responds to the scene event, reads the `Tap_Position` event parameter, and sets the value on its entity as an entity parameter named `Navigation Target`. The behavior tree on the same entity can read this parameter, and the next time the Move on Navigation Mesh node runs, the system uses this value to tell the navigating entity where to move next on the navigation mesh.

> **Note**: The Move on Navigation Mesh node runs until the entity reaches its destination, so it doesn’t read a new target until then.

![A screenshot of a Script Graph that sets the Navigation Target parameter on the entity.](https://developer.apple.com/tutorials/images/com.apple.visionOS/navmesh-set-nav-target@3x.png)

## Drive animation and orientation

In addition to moving the entity around the scene, this sample demonstrates how to animate an entity in sync with movement across the mesh, orienting the entity along the direction of movement and alternating between idle and walking animations based on whether the entity is moving.

Each frame, an On Update branch in `PlayerLogic` calculates the `Move Direction` and `Is Moving` entity parameters. The Script Graph stores a local variable, `Previous Position`, containing the entity’s position on the previous frame. Then the sample compares that value to the entity’s position to derive the direction of motion and whether the entity is moving at all.

![A screenshot of the Calculate move direction section of the PlayerLogic Script Graph in Reality Composer Pro.](https://developer.apple.com/tutorials/images/com.apple.visionOS/navmesh-move-direction@3x.png)

The `PlayerModelLogic` graph on the `ModelRoot` entity reads these parameters from the player entity to orient the model and play its animations.

For orientation, the graph reads `Move Direction` from the player entity, feeds that value to a quaternion node to build a look-at rotation, and blends toward that rotation with spherical linear interpolation, using the frame’s delta time multiplied by `4` as the blend factor.

![A screenshot of a Script Graph that spherically interpolates an entity's rotation to face along a direction vector.](https://developer.apple.com/tutorials/images/com.apple.visionOS/navmesh-rotation@3x.png)

For animation, the skinned mesh under `ModelRoot` has an [`AnimationLibraryComponent`](../RealityKit/animationlibrarycomponent.md) holding `player_anim_idle` and `player_anim_walk`. The graph reads `Is Moving`, compares it against a `was_moving` graph variable, and only acts on the frames where the values differ. On a change it stores the new value and routes to one of two Play Named Animation nodes — `player_anim_walk` when movement starts, `player_anim_idle` when it stops.

![A screenshot of the Play animation when toggling is moving section of the PlayerModelLogic Script Graph in Reality Composer Pro.](https://developer.apple.com/tutorials/images/com.apple.visionOS/navmesh-animation@3x.png)

## See Also

### RealityKit and Reality Composer Pro
- [Reality Composer Pro](../RealityComposerPro/RealityComposerPro.md)
  Build, design, and orchestrate 3D content for your RealityKit apps.
- [Chaparral Village: Building an immersive visionOS adventure game](./chaparral-village-building-an-immersive-visionos-adventure-game.md)
  Create an adventure game using SwiftUI, RealityKit, and Reality Composer Pro 3.
- [Designing no-code games with Reality Composer Pro 3](./designing-no-code-games-in-reality-composer-pro-3.md)
  Build a video game in Reality Composer Pro without code using Script Graphs.
- [Petite Asteroids: Building a volumetric visionOS game](./petite-asteroids-building-a-volumetric-visionos-game.md)
  Use the latest RealityKit APIs to create a beautiful video game for visionOS.
- [BOT-anist](./bot-anist.md)
  Build a multiplatform app that uses windows, volumes, and animations to create a robot botanist’s greenhouse.
- [Swift Splash](./swift-splash.md)
  Use RealityKit to create an interactive ride in visionOS.
- [Diorama](./diorama.md)
  Design scenes for your visionOS app using Reality Composer Pro.
- [Building an immersive media viewing experience](./building-an-immersive-media-viewing-experience.md)
  Add a deeper level of immersion to media playback in your app with RealityKit and Reality Composer Pro.
- [Enabling video reflections in an immersive environment](./enabling-video-reflections-in-an-immersive-environment.md)
  Create a more immersive experience by adding video reflections in a custom environment.
- [Combining 2D and 3D views in an immersive app](../RealityKit/combining-2d-and-3d-views-in-an-immersive-app.md)
  Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Understanding the modular architecture of RealityKit](./understanding-the-realitykit-modular-architecture.md)
  Learn how everything fits together in RealityKit.
- [Using transforms to move, scale, and rotate entities](./understanding-transforms.md)
  Learn how to use Transforms to move, scale, and rotate entities in RealityKit.
- [Capturing screenshots and video from Apple Vision Pro for 2D viewing](./capturing-screenshots-and-video-from-your-apple-vision-pro-for-2d-viewing.md)
  Create screenshots and record high-quality video of your visionOS app and its surroundings for app previews.
- [Implementing object tracking in your app](./implementing-object-tracking-in-your-app.md)
  Create engaging interactions by training models to recognize and track real-world objects in people’s surroundings.
- [Placing entities using head and device transform](./placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/creating-a-navigation-mesh-with-reality-composer-pro)*