# Building local experiences with room tracking

**Framework**: visionOS

Use room tracking in visionOS to provide custom interactions with physical spaces.

**Availability**:
- visionOS 2.0+
- Xcode 16.0+

#### Overview

This sample allows your app to keep track of rooms as discrete, identifiable places, and enables you to provide a customized virtual experience inside a specific room, and to get notified when someone enters or leaves the room. These customizations can be as simple as knowing when to stop room-specific animations, or to support the creation of location-specific virtual content such as in-game treasures, effects, or even portals to virtual worlds that contain other content.

This sample demonstrates how to use room tracking by enabling a person to place spheres in a space and continuously query the framework as to whether those spheres are in the same room as the person. As someone moves into, through, and out of the room, ARKit delivers [`RoomAnchor`](https://developer.apple.com/documentation/ARKit/RoomAnchor) updates that represent the latest knowledge of the current room. This structure provides a [`contains(_:)`](https://developer.apple.com/documentation/ARKit/RoomAnchor/contains(_:)) query method that you use to determine if the spheres are in the current room, and highlight them accordingly.

The app has an , in which the room geometry the framework renders is a transparent occluder that hides virtual objects outside the room. It also has a , in which someone may select a specific wall for the purpose of replacing it with a video or virtual portal.

> **Note**: This app requires Xcode 16 and visionOS 2 or later, and an Apple Vision Pro. ARKit room tracking isn’t supported in Simulator.

#### Ensure All Data Providers Are in an Authorized State

Your app must request permission to use certain visionOS capabilities before being able to access data associated with them. For example, attempting to access the [`RoomTrackingProvider`](https://developer.apple.com/documentation/ARKit/RoomTrackingProvider) displays a permission sheet asking the user to authorize your app’s access. If the user has previously denied this request, the app displays an error message in the scene. For information about using a `RoomTrackingProvider`, see [`Setting up access to ARKit data`](setting-up-access-to-arkit-data.md). For information about best practices for privacy, see [`Adopting best practices for privacy and user preferences`](adopting-best-practices-for-privacy.md).

> **Note**: To use the room tracking capabilities in visionOS in your app, you need to provide the  [`NSWorldSensingUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSWorldSensingUsageDescription) key in your app’s `Info.plist` along with a description of why your app uses this feature. This sample already provides this key and description.

```swift
func areAllDataProvidersAuthorized() async -> Bool {
    // It's sufficient to check that the authorization status isn't `denied`.
    // If it's `notdetermined`, ARKit presents a permission pop-up menu that appears as soon
    // as the session runs.
    let authorization = await ARKitSession().queryAuthorization(for: [.worldSensing])
    return authorization[.worldSensing] != .denied
}
```

#### Configure Room Tracking

Set up room tracking by first configuring an [`ARKitSession`](https://developer.apple.com/documentation/ARKit/ARKitSession) instance, then add a  [`WorldTrackingProvider`](https://developer.apple.com/documentation/ARKit/WorldTrackingProvider) and a  [`RoomTrackingProvider`](https://developer.apple.com/documentation/ARKit/RoomTrackingProvider) to the session as shown in the following example:

```swift
private let session = ARKitSession()
private let worldTracking = WorldTrackingProvider()
private let roomTracking = RoomTrackingProvider()
```

In addition to instantiating the world and room tracking providers in the `AppState`, you need to create storage for the in-room anchors the app tracks:

```swift
/// A dictionary that contains `RoomAnchor` structures.
private var roomAnchors = [UUID: RoomAnchor]()
/// A dictionary that contains `WorldAnchor` structures.
private var worldAnchors = [UUID: WorldAnchor]()
/// A dictionary that contains `ModelEntity` structures for spheres.
private var sphereEntities = [UUID: ModelEntity]()
/// A dictionary that contains `ModelEntity` structures for room anchors.
private var roomEntities = [UUID: ModelEntity]()
```

You also need to create the materials the framework uses to render the in-room anchors:

```swift
// Material for spheres in the current room.
private let inRoomSphereMaterial = SimpleMaterial(color: .green, roughness: 0.2, isMetallic: true)
// Material for spheres not in the current room.
private let outOfRoomSphereMaterial = SimpleMaterial(color: .red, roughness: 0.2, isMetallic: true)
// Material the app applies to room entities to show occlusion effects.
private let occlusionMaterial = OcclusionMaterial()
// Material for current room walls.
private var wallMaterial = UnlitMaterial(color: .blue)
```

#### Allow a Person to Place Room Tracking Anchors

Placing a `roomAnchor` object in the room consists of two processes. The first phase allows the person to review the anchor, which the sample renders as a sphere in front of the device from the person’s perspective:

```swift
private func createPreviewSphere() -> ModelEntity {
    let sphereMesh = MeshResource.generateSphere(radius: 0.1)
    let sphereMaterial = SimpleMaterial(color: .gray.withAlphaComponent(0.5), roughness: 0.2, isMetallic: false)
    let sphere = ModelEntity(mesh: sphereMesh, materials: [sphereMaterial])
    
    // Enables gestures on the preview sphere.
    // Looking at the preview and using a pinch gesture causes a world anchored sphere to appear.
    sphere.generateCollisionShapes(recursive: false, static: true)
    // Ensures the preview only accepts indirect input (for tap gestures).
    sphere.components.set(InputTargetComponent(allowedInputTypes: [.indirect]))
    
    // The preview sphere only becomes visible once someone clicks the Add a Sphere button.
    sphere.isEnabled = false
    
    return sphere
}
```

The second phase allows a person to place the sphere (a [`WorldAnchor`](https://developer.apple.com/documentation/ARKit/WorldAnchor)) in their surroundings  with a tap gesture. Gestures such as this are SwiftUI view modifiers you apply to the room’s `View`, as shown below:

```swift
.gesture(SpatialTapGesture().targetedToAnyEntity().onEnded { event in
    if event.entity == previewSphere {
        Task {
            // To place a sphere you need to:
            // 1. Create a world anchor with the translation of that offset transform and add the anchor to the world tracking provider.
            // 2. Create the sphere's geometry in `processWorldTrackingUpdates()` after you have successfully added the world anchor.
            await appState.addWorldAnchor(at: event.entity.transformMatrix(relativeTo: nil))
            appState.showPreviewSphere = false
        }
    }
})
```

As a person places spheres in the room, they appear in green to indicate they’re anchors in the current room. If a person leaves the room, all of the room anchors in the previous room dim and become red to indicate a person has left the room. If there are anchors in the room a person enters into, they change color to indicate the person is currently in the room.

This changing state and the property of a room being  is what allows an app to make decisions about what actions, animations, or other processes make sense in a specific location.

#### Check the Current Room and Respond to Updates

As a person moves from room to room, ARKit’s room tracking process checks to see which room is current and reports back changes to the app through the `RoomTrackingProvider` property  [`anchorUpdates`](https://developer.apple.com/documentation/ARKit/RoomTrackingProvider/anchorUpdates), which is an asynchronous sequence of all anchor updates. As these updates come in, a `Task` view modifier in the app’s `WorldAndRoomView` calls a method that looks for anchors to update, as demonstrated here:

```swift
func processRoomTrackingUpdates() async {
    for await update in roomTracking.anchorUpdates {
        let roomAnchor = update.anchor
        switch update.event {
        case .removed:
            if roomAnchor.isCurrentRoom {
                colliderWallsRoot.children.removeAll()
                if let currentRenderedWall {
                    renderWallRoot.removeChild(currentRenderedWall)
                }
            }
            roomAnchors.removeValue(forKey: roomAnchor.id)
            roomEntities[roomAnchor.id]?.removeFromParent()
            roomEntities.removeValue(forKey: roomAnchor.id)
            updateSphereState()
        case .added, .updated:
            roomAnchors[roomAnchor.id] = roomAnchor
            guard let roomMeshResource = roomAnchor.geometry.asMeshResource() else { continue }
            if update.event == .added {
                let roomEntity = ModelEntity(mesh: roomMeshResource, materials: [occlusionMaterial])
                roomEntity.transform = Transform(matrix: roomAnchor.originFromAnchorTransform)
                roomEntities[roomAnchor.id] = roomEntity
                roomEntity.isEnabled = roomAnchor.isCurrentRoom
                roomRoot.addChild(roomEntity)
                
            } else if update.event == .updated {
                guard let roomEntity = roomEntities[roomAnchor.id] else { continue }
                roomEntity.model?.mesh = roomMeshResource
                roomEntity.transform = Transform(matrix: roomAnchor.originFromAnchorTransform)
                roomEntity.isEnabled = roomAnchor.isCurrentRoom
            }
            
            updateSphereState()
            
            if roomAnchor.isCurrentRoom {
                currentRoomID = roomAnchor.id
                if renderWallRoot.isEnabled {
                    await updateCurrentRoomWalls(for: roomAnchor)
                }
            }
        }
    }
}
```

#### Find and Select Walls

Room tracking also enables someone to find and select walls in the current room. You can use this as an additional interaction surface, such as creating a “portal” to another virtual space. The process of selecting a wall in a room is split into two modes: an  where actively looking at a specific wall causes ARKit to highlight it in blue, and  where a person has selected a wall and it receives continuous updates from the `RoomTrackingProvider`. The  requires performing a ray cast query in the direction of the a person’s head, which returns the first wall that it hits, as shown here:

```swift
/// Updates the wall in front of the person when a wall isn't in a selected state.
func updateFacingWall() {
    guard renderWallRoot.isEnabled && !isWallSelectionLocked else {
        return
    }
    // Update within 10 m.
    let distance: Float = 10
    
    let deviceAnchor = worldTracking.queryDeviceAnchor(atTimestamp: CACurrentMediaTime())
    guard let deviceAnchor, deviceAnchor.isTracked == true else {
        return
    }
    let deviceInOriginCoordinates = deviceAnchor.originFromAnchorTransform
    
    let lookAtPointInDeviceCoordinate = SIMD4<Float>(0, 0, -distance, 1)
    let lookAtPointInOriginCoordinates = deviceInOriginCoordinates * lookAtPointInDeviceCoordinate
    
    guard let scene = colliderWallsRoot.scene else {
        logger.error("Failed to find the scene of `colliderWallsRoot`.")
        return
    }
    
    let hitWall = scene.raycast(from: deviceInOriginCoordinates.columns.3.xyz, to: lookAtPointInOriginCoordinates.xyz, query: .nearest)
    
    guard !hitWall.isEmpty else {
        return
    }
    // Render the first hit wall.
    renderWallRoot.children.removeAll()

    let hitEntity = hitWall[0].entity
    currentRenderedWall = hitEntity
    renderWallRoot.addChild(hitEntity)
}

/// Updates walls under the collider walls root.
///
/// If someone has chosen and locked a wall, this method updates and renders that wall.
/// If someone hasn't locked a wall, the method updates and renders the wall in front of
/// them  in `WorldAndRoomView` at a rate of 10 Hz.
private func updateCurrentRoomWalls(for roomAnchor: RoomAnchor) async {
    let newColliderWalls = Entity()
    let wallGeometries = roomAnchor.geometries(of: .wall)
    for wallGeometry in wallGeometries {
        guard let wallMeshResource = wallGeometry.asMeshResource() else {
            continue
        }
        
        let wallEntity = ModelEntity(mesh: wallMeshResource, materials: [wallMaterial])
        wallEntity.transform = Transform(matrix: roomAnchor.originFromAnchorTransform)
        
        guard let shape = try? await ShapeResource.generateStaticMesh(from: wallMeshResource) else {
            logger.error("Failed to create ShapeResource from wall geometries.")
            continue
        }
        
        wallEntity.collision = CollisionComponent(shapes: [shape], isStatic: true)
        newColliderWalls.addChild(wallEntity)
    }
    // Clear old walls.
    colliderWallsRoot.children.removeAll()
    colliderWallsRoot.addChild(newColliderWalls)
    
    if isWallSelectionLocked {
        let wallCandidateEntities = Array(newColliderWalls.children)
        updateLockedWall(wallCandidateEntities: wallCandidateEntities)
    }
}
```

#### Keep Focus on the Current Room

Room tracking operates only in the current room a person is in. If someone leaves one room and enters another, the previous room is no longer valid, and the framework only updates mesh-room associations and plane-room associations for the current room. Only use the current room anchor and discard any noncurrent rooms.

#### Be Aware of Limitations

Clutter in a room, large furniture elements, and very large spaces may interfere with ARKit’s ability to accurately detect walls and fully detect the dimensions of a room. In the case of very large indoor spaces, or in rooms with low-light conditions, the framework may only provide a floor mesh. Additionally, visionOS doesn’t support using room tracking outdoors or when Apple Vision Pro is in Travel Mode. In these cases, there’s no current room. For more information on implementing immersive experiences, see Human Interface Guidelines > [`Immersive experiences`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/immersive-experiences).

> ⚠️ **Warning**: Be mindful of how much content you include in immersive scenes that use the [`mixed`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/mixed) style. Content that fills a significant portion of the screen, even if that content is partially transparent, can prevent the person from seeing potential hazards in their surroundings. If you want to immerse the person in your content, configure your space with the  [`full`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/full) style. For more information, see [`Creating fully immersive experiences in your app`](https://developer.apple.comhttps://developer.apple.com/documentation/visionos/creating-fully-immersive-experiences).

## See Also

- [Happy Beam](happybeam.md)
  Leverage a Full Space to create a fun game using ARKit.
- [Setting up access to ARKit data](setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [Incorporating real-world surroundings in an immersive experience](incorporating-real-world-surroundings-in-an-immersive-experience.md)
  Create an immersive experience by making your app’s content respond to the local shape of the world.
- [Placing content on detected planes](placing-content-on-detected-planes.md)
  Detect horizontal surfaces like tables and floors, as well as vertical planes like walls and doors.
- [Tracking specific points in world space](tracking-points-in-world-space.md)
  Retrieve the position and orientation of anchors your app stores in ARKit.
- [Tracking preregistered images in 3D space](tracking-images-in-3d-space.md)
  Place content based on the current position of a known image in a person’s surroundings.
- [Exploring object tracking with ARKit](exploring_object_tracking_with_arkit.md)
  Find and track real-world objects in visionOS using reference objects trained with Create ML.
- [Object tracking with Reality Composer Pro experiences](object-tracking-with-reality-composer-pro-experiences.md)
  Use object tracking in visionOS to attach digital content to real objects to create engaging experiences.
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/building_local_experiences_with_room_tracking)*