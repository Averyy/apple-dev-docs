# Rendering Gaussian splats with RealityKit

**Framework**: visionOS

Bring a real-world scan into an app by loading splat data from a USD or PLY file.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- Xcode 27.0+

#### Overview

A Gaussian splat asset represents a scene as a large collection of colored, oriented ellipsoids instead of a mesh, so a real-world capture keeps details that are hard to model by hand, like soil texture or the fine edges of leaves. Each splat carries position, scale, rotation, opacity, and a set of spherical harmonic coefficients that let its color shift depending on the viewing angle. This reproduces specular highlights and reflections that were present in the original capture. The capture bakes that color in, so scene lighting doesn’t change how a splat looks, and a splat won’t cast a shadow the way mesh-based content does.

![A Gaussian splat asset, showing a potted succulent sitting on a coffee table next to a chair in a well-lit room.](/images/com.apple.visionOS/plant_wwdc_screencapture.png)

This sample uses [`RealityKit`](https://developer.apple.com/documentation/realitykit) to add a scan of a potted plant to a scene. The app loads the same plant from either a USD file or a PLY file, and the code that gets that data onto the GPU is shared across every platform the sample runs on.

A scene can only render a limited number of splat entities at once. When an asset costs more than the renderer can afford, RealityKit reduces its own splat rendering work and reports the change by sending a [`GaussianSplatEvents.RenderingChanged`](https://developer.apple.com/documentation/realitykit/gaussiansplatevents/renderingchanged) event on the entity that owns the splat. The event’s [`isRenderingLimited`](https://developer.apple.com/documentation/realitykit/gaussiansplatevents/renderingchanged/isrenderinglimited) property tells the app whether RealityKit is currently limiting the entity’s splat rendering, and [`renderingStatus`](https://developer.apple.com/documentation/realitykit/gaussiansplatevents/renderingchanged/renderingstatus) indicates which rendering quality the system selected. RealityKit sends the event after it applies that mitigation, so the event reports a decision rather than asking the app to make one. The sample subscribes to the event so the app’s window can report when RealityKit limits splat rendering. Reducing the asset’s splat count gives the renderer less to do and brings back full-quality rendering.

> **Note**: This sample code project is associated with WWDC26 session 287: [`Build next generation experiences with visionOS 27`](https://developer.apple.comhttps://developer.apple.com/wwdc26/287), and session 279: [`Explore advances in RealityKit`](https://developer.apple.comhttps://developer.apple.com/wwdc26/279).

#### Configure the Sample Code Project

Because Gaussian splats don’t render in Simulator, choose a destination from the scheme menu in Xcode and run the app on Apple Vision Pro, iPhone, iPad, or Mac.

The sample shares its loading code for each platform to provide a native environment on launch. For example, on visionOS, the plant appears in a mixed immersive space where a person can pick it up, move it, and anchor it to a nearby table or floor. On macOS and iOS it appears in the app’s window, where dragging turns it.

#### Load a Splat From a Usd File

The sample’s bundled USD asset stores its splat data in a primitive whose schema type is `ParticleField3DGaussianSplat`. This primitive isn’t defined by RealityKit or [`USDKit`](https://developer.apple.com/documentation/usdkit), and is instead created by the tool that authored the asset. `loadUSDEntity(assetName:)` opens the stage with [`open(_:loadingPayloads:)`](https://developer.apple.com/documentation/usdkit/usdstage/open(_:loadingpayloads:)), searches the stage’s [`descendants`](https://developer.apple.com/documentation/usdkit/usdstage/descendants) for the primitive with that schema using [`isSchema(_:)`](https://developer.apple.com/documentation/usdkit/usdprim/isschema(_:)), and reads the attributes of that [`USDPrim`](https://developer.apple.com/documentation/usdkit/usdprim) into a `GaussianSplatBuffers`:

```swift
func loadUSDEntity(assetName: String) async throws -> Entity {
    let url = try bundleUSDURL(assetName: assetName)

    let buffers = try await Task.detached(priority: .userInitiated) {
        let stage = try USDStage.open(url)

        guard let splatPrim = stage.descendants.first(where: {
            $0.isSchema("ParticleField3DGaussianSplat")
        }) else {
            throw GaussianSplatError.invalidData("No ParticleField3DGaussianSplat prim found in \(url.lastPathComponent)")
        }

        return try buildBuffers(from: splatPrim)
    }.value

    return try makeSplatEntity(from: buffers, isLinear: true)
}
```

RealityKit expects each rotation as four contiguous floats in `w`, `x`, `y`, `z` order. [`USDValue.Quatf`](https://developer.apple.com/documentation/usdkit/usdvalue/quatf) exposes its parts through the [`real`](https://developer.apple.com/documentation/usdkit/usdvalue/quatf/real) and [`imaginary`](https://developer.apple.com/documentation/usdkit/usdvalue/quatf/imaginary) accessors rather than as raw fields in that layout, so the loop reads each component through its accessor and writes it into the matching slot of the [`LowLevelBuffer`](https://developer.apple.com/documentation/realitykit/lowlevelbuffer) instead of copying the structure’s bytes directly:

```swift
private nonisolated func fillRotationBuffer(_ buffer: LowLevelBuffer?, quatArray: [USDValue.Quatf], count: Int) {
    buffer?.withUnsafeMutableBytes { dst in
        let out = dst.bindMemory(to: Float.self)
        for idx in 0..<count {
            let quat = quatArray[idx]
            out[idx * 4 + 0] = quat.real          // w
            out[idx * 4 + 1] = quat.imaginary.x   // x
            out[idx * 4 + 2] = quat.imaginary.y   // y
            out[idx * 4 + 3] = quat.imaginary.z   // z
        }
    }
}
```

For more information on providing raw splat data for rendering Gaussian splats in RealityKit, see [`GaussianSplatComponent`](https://developer.apple.com/documentation/realitykit/gaussiansplatcomponent).

#### Load a Splat From a Ply File

PLY is a generic 3D file format and its header declares the elements and properties inside the file. PLY doesn’t have a standard schema for Gaussian splat data. This sample expects a plain-text header that declares each property, followed by a binary block with one record per splat, using the property set that Gaussian splatting tools have settled on as a common convention:

| Property | Contains | Description |
| --- | --- | --- |
| `x, y, z` | 3 floats | Sets the splat’s center in local space. |
| `f_dc_0..2` | 3 floats | Sets the splat’s base color, which looks the same from every angle. |
| `f_rest_0..N` | Varies (0, 9, 24, or 45 floats) | Adds spherical harmonic coefficients that shift the splat’s color based on the viewing angle. The file stores these coefficients as channel-major: all R values, then all G, then all B. The count depends on the [`GaussianSplatResource.SphericalHarmonicDegree`](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/sphericalharmonicdegree) the asset uses. |
| `opacity` | 1 float | Sets the splat’s opacity as an unbounded value. RealityKit maps it to 0…1 with the sigmoid function, `1 / (1 + e^-x)`. |
| `scale_0..2` | 3 floats | Sets the splat’s per-axis size, stored in log space. RealityKit converts it with `exp()`. |
| `rot_0..3` | 4 floats | Forms a quaternion, in `w`, `x`, `y`, `z` order, that sets the splat’s rotation. |

`loadPLYEntity(assetName:)` reads the file, deinterleaves those properties into a `GaussianSplatBuffers`, and calls `makeSplatEntity(from:)` without `isLinear`, so RealityKit converts the log-space scale and unbounded opacity:

```swift
func loadPLYEntity(assetName: String) async throws -> Entity {
    let url = try bundlePLYURL(assetName: assetName)
    let buffers = try await Task.detached(priority: .userInitiated) {
        let splatData = try readGaussianSplatFile(url)
        return try deinterleaveGaussianSplatData(splatData)
    }.value
    return try makeSplatEntity(from: buffers)
}
```

The `deinterleaveGaussianSplatData(_:)` method also sanitizes every value it copies, replacing any `NaN` or infinite float with `0`. RealityKit rejects a splat buffer that contains a non-finite value, so the loader cleans up the capture data before building the buffer.

#### Prepare Buffers for Splat Assets

Whichever format the sample starts from, it fills the same GPU buffers for position, scale, rotation, opacity, and spherical harmonics. This sample defines a custom structure, `GaussianSplatBuffers`, that holds those buffers, and a helper turns a filled-in structure into something the app can add to a scene. `assembleSplatComponent(from:isLinear:)` packages the buffers into a [`GaussianSplatResource.BufferResource`](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/bufferresource-swift.struct), describing where each per-splat property lives with a [`GaussianSplatResource.BufferDescriptor`](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/bufferdescriptor), wraps that in a [`GaussianSplatResource`](https://developer.apple.com/documentation/realitykit/gaussiansplatresource), and builds a [`GaussianSplatComponent`](https://developer.apple.com/documentation/realitykit/gaussiansplatcomponent) from it. `assembleSplatComponent(from:isLinear:)` also sets the resource’s [`scaleActivation`](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/scaleactivation) and [`opacityActivation`](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/opacityactivation), which tell RealityKit how to interpret the raw numbers in the buffers:

```swift
func assembleSplatComponent(from buffers: GaussianSplatBuffers, isLinear: Bool = false) throws -> GaussianSplatComponent {
    guard let pos = buffers.positionBuffer,
          let scale = buffers.scaleBuffer,
          let rotation = buffers.rotationBuffer,
          let opacity = buffers.opacityBuffer,
          let shBuf = buffers.shBuffer else {
        throw GaussianSplatError.invalidData("One or more GPU buffers failed to allocate")
    }

    let degree = GaussianSplatResource.SphericalHarmonicDegree(rawValue: buffers.degreeSH) ?? .zero
    let bufferResource = try GaussianSplatResource.BufferResource(
        count: Int(buffers.splatCount),
        position: makeDescriptor(buffer: pos, format: .float3, stride: 3 * 4),
        scale: makeDescriptor(buffer: scale, format: .float3, stride: 3 * 4),
        rotation: makeDescriptor(buffer: rotation, format: .float4, stride: 4 * 4),
        opacity: makeDescriptor(buffer: opacity, format: .float, stride: 1 * 4),
        sphericalHarmonics: (makeSHDescriptor(buffer: shBuf, tupleSH: buffers.tupleSH), degree)
    )

    let splatResource = GaussianSplatResource(bufferResource)
    if isLinear {
        splatResource.scaleActivation   = .identity
        splatResource.opacityActivation = .identity
    } else {
        splatResource.scaleActivation   = .exponential
        splatResource.opacityActivation = .sigmoid
    }
    return GaussianSplatComponent(splatResource)
}
```

This sample passes `isLinear: true` for data that’s already in linear space, like the USD version of the plant asset. For the PLY asset, the sample leaves it `false`, allowing RealityKit to apply the [`GaussianSplatResource.ActivationFunction.exponential`](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/activationfunction/exponential) and [`GaussianSplatResource.ActivationFunction.sigmoid`](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/activationfunction/sigmoid) conversions for splat data.

#### Add Interactivity to a Splat Entity

A splat entity is an [`Entity`](https://developer.apple.com/documentation/realitykit/entity) like any other, so it takes the same components. The sample’s visionOS view adds a [`GroundingShadowComponent`](https://developer.apple.com/documentation/realitykit/groundingshadowcomponent) and a [`ManipulationComponent`](https://developer.apple.com/documentation/realitykit/manipulationcomponent) so a person can pick up the plant and move it. Because a splat asset has no mesh to derive collision geometry from, the call to [`configureEntity(_:hoverEffect:allowedInputTypes:collisionShapes:)`](https://developer.apple.com/documentation/realitykit/manipulationcomponent/configureentity(_:hovereffect:allowedinputtypes:collisionshapes:)) passes an explicit box from [`generateBox(size:)`](https://developer.apple.com/documentation/realitykit/shaperesource/generatebox(size:)).

```swift
private func configureManipulableObject(_ entity: Entity) {
    ManipulationComponent.configureEntity(
        entity,
        collisionShapes: [ShapeResource.generateBox(size: SIMD3<Float>(repeating: 0.5))]
    )
    var manipulation = entity.components[ManipulationComponent.self] ?? ManipulationComponent()

    // ...

    entity.components.set(manipulation)
    entity.components.set(GroundingShadowComponent(castsShadow: true))
}
```

## See Also

- [Reality Composer Pro](../realitycomposerpro/realitycomposerpro.md)
  Build, design, and orchestrate 3D content for your RealityKit apps.
- [Chaparral Village: Building an immersive visionOS adventure game](chaparral-village-building-an-immersive-visionos-adventure-game.md)
  Create an adventure game using SwiftUI, RealityKit, and Reality Composer Pro 3.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/rendering-gaussian-splats-with-realitykit)*