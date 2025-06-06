# Designing RealityKit content with Reality Composer Pro

**Framework**: Visionos

Design RealityKit scenes for your visionOS app.

#### Overview

In addition to helping you compose scenes, Reality Composer Pro also gives you the ability to add and configure components — even custom components that you’ve written — to the entities in your scenes and also lets you create complex materials and effects using a node-based material editor called Shader Graph.

##### Launch Reality Composer Pro

When you create a visionOS project in Xcode, it also contains a default Reality Composer Pro project named `RealityKitContent` within the Packages folder, which is a Swift package. The `RealityKitContent` package can include images, 3D models, and other assets like audio and video files. The assets you add to your project go in the `RealityKitContent.rkassets` bundle, while your source code goes into its Sources directory. The package also contains a file called `Package.realitycomposerpro`, which is the actual Reality Composer Pro project.

To launch Reality Composer Pro, double-click the `Package.realitycomposerpro` file in the Project navigator, or click the Open in Reality Composer Pro button. If your project doesn’t already have a Reality Composer Pro project, you can launch Reality Composer Pro directly by choosing Xcode > Open Developer Tool > Reality Composer Pro.

For efficiency, store all of your RealityKit assets in Reality Composer Pro projects. Xcode compiles Reality Composer Pro projects into a more efficient format when you build your app.

> **Note**: Loading assets from a `.reality` file is considerably faster and more resource efficient than loading individual asset files.

##### Orient Yourself in Reality Composer Pro

The Reality Composer Pro window has several sections. The top-half displays the active scene. If you have multiple scenes, the window shows a tab bar at the top with one tab for each open scene. A  in Reality Composer Pro is an entity hierarchy stored in a `.usda` file.

The left side of the top pane contains the hierarchy browser, which shows a tree representation of the entities in the active scene. You can toggle it using the top-left toolbar button to reveal errors and warnings. The middle pane is the 3D View, which shows a 3D representation of the active scene. The top-right is the inspector, which shows configurable values for the item selected in the 3D view, hierarchy view, or Shader Graph, depending on which has focus.

> 💡 **Tip**: A Reality Composer Pro scene can represent an entire RealityKit scene, and you can have multiple scenes in your Reality Composer Pro project, each driving a different [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) in the same app. A scene can also contain a collection of entities to use as a building block. For example, if you had an airplane model, you might build a scene for it that contains its 3D model, a particle effect to make smoke come out its engine, and audio entities or components that represent the various sounds a plane makes. Your app could then load those combined assets and use them together anywhere it needs.

The bottom half of Reality Composer Pro contains the following four tabs:

![A screenshot of a Reality Composer Pro project window. The window has a single tab at the top called Biplane. The window is divided vertically into two sections. The top section has three panes: a hierarchical view of the 3D scene on the left, an toy airplane model in the middle, and an inspector on the right. The bottom section has four tabs, labeled Project Browser, Shader Graph, Audio Mixer, and Statistics. Project Browser is currently selected, and it is also divided into three sections with a hierarchy on the left, a grid of icons in the middle, and an inspector on the right showing the entity hierarchy for the asset selected in the middle.](https://docs-assets.developer.apple.com/published/0838e5075126ee9f4025dae677c6c63f/RCPro-BiplaneWindow%402x.png)

Reality Composer Pro projects start with a single empty scene called `Scene` which is stored in a file called `Scene.usda`. You can create as many additional scenes as you need by choosing File > New > Scene. New scenes open as tabs along the top of the window, and they also appear in the Project Browser as `.usda` files.

If you close a scene’s tab and need to re-open it, double-click on the scene’s `.usda` file in the Project Browser. If you no longer need a scene, delete its `.usda` file from the Project Browser or remove it from your project’s `.rkassets` bundle in Xcode.

To delete a scene:

1. Close the scene tab by selecting File > Close Tab
2. Select the scene’s `.usda` file in the Project Browser
3. Control-click the scene’s `.usda` file  the Project Browser.
4. Choose Delete from the contextual menu.
5. Click Move to Trash.

This removes the scene’s `.usda` and the scene tab at the top of the window.

##### Add Assets to Your Project

In Reality Composer Pro, you design scenes by first importing assets into your project. Then add assets to scenes and move, rotate, and scale them. The Project Browser tab displays all of the asset files in your project. You can add new assets by dragging them to the Project Browser or by choosing File > Import and select the assets to add to your project. To add an asset from the Project Browser to the current scene, drag it to the 3D view in the center of the window, or to the hierarchy view in the top-left of the window.

> **Note**: Reality Composer Pro projects can contain assets not used in any scene. Such assets are still compiled into your app and can be loaded at runtime and take full advantage of the efficient loading process for `.reality` files.

Reality Composer Pro can represent many assets as entities, but it can’t represent all assets that way; for example:

- USDZ models do become an entity or entity hierarchy when you add them to a scene.
- Image files do not become an entity. Reality Composer Pro only uses image assets indirectly, such as being the source texture for materials you build in Shader Graph. If you drag assets that Reality Composer Pro can’t turn into an entity, nothing happens.

> ❗ **Important**: Reality Composer Pro treats your imported assets as read-only.

Changes you make to assets in a scene only affect that scene’s copy of the asset. The changes you make are stored in the scene’s `.usda` file, not in the original asset. That means you can work without fear of inadvertently changing other scenes. If you plan to make significant changes to an imported 3D model, such as by replacing its materials with dynamic Shader Graph materials, import the model as a`.usdc` file instead of as a `.usdz` file, and then separately import just the supporting assets you need to avoid Xcode compiling assets that you don’t need into your app.

##### Compose Scenes From Assets

All RealityKit entities in a scene exist at a specific position, orientation, and scale, even if that entity has no visual representation. When you click to select an entity in the 3D view or hierarchy view, Reality Composer Pro displays:

- A manipulator over the entity in the 3D view.
- Any configurable values from the entity’s components in the inspector on the right. You can use the manipulator to move, rotate, and scale the selected entity.
- To move the selected entity around the 3D scene, drag the small colored cone that corresponds to the axis you want to move it along. Alternatively, you can drag the entity itself to move it freely relative to your viewing angle.
- To rotate the selected entity, click on the manipulator’s rotation control, which looks like a circle, and drag in a circular motion. - Reality Composer Pro’s manipulator only shows one rotation control at a time.
- To rotate an entity on one of the other axes, click the cone corresponding to the axis you want to rotate. For example, if you want to rotate the entity on the `X` axis, tap the red cone to bring up the red rotation handle for that axis.
- To scale the selected entity uniformly, click the rotation circle and drag away from the entity origin to scale it up, or toward the entity origin to scale it down. Because it scales uniformly, it doesn’t matter which rotation handle Reality Composer Pro is showing.

> **Note**: In the manipulator, Red indicates the X axis, Green indicates the Y axis, and Blue indicates the Z axis.

##### Activate and Deactivate Scene Entities

Reality Composer Pro scenes can get quite complex and sometimes contain overlapping entities, which can be difficult to work with. To simplify a scene, you can deactivate entities to remove them from the 3D view. Deactivate entities by Control-clicking them and selecting Deactivate from the contextual menu. The entity still exists in your project and is shown in the hierarchy view, albeit grayed out and without any child entities. It won’t, however, appear in the 3D view. Xcode doesn’t compile deactivated entities into your app’s bundle, so it’s important to re-activate any entities your app needs before saving your project. To reactivate an entity, Control-click the entity in the hierarchy view and select Activate from the contextual menu.

##### Add Components to Entities

RealityKit follows a design pattern called Entity-Component-System (ECS). In ECS, you store data on an entity using components and then implement entity behavior by writing systems that use the data from those components. You can add and configure components to entities in Reality Composer Pro, including both built-in components like [`ParticleEmitterComponent`](https://developer.apple.com/documentation/RealityKit/ParticleEmitterComponent), and custom components that you write and place in the Sources folder of your Reality Composer Pro Swift package. You can also create new components in Reality Composer Pro and edit them in Xcode.

For more information about ECS, see [`Understanding the modular architecture of RealityKit`](understanding-the-realitykit-modular-architecture.md).

##### Create or Modify Entity Hierarchies

Reality Composer Pro scenes are hierarchies of RealityKit entities. You can change the relationship between entities in the hierarchy browser except for parts of the hierarchy imported from a `.usdz` file, which Reality Composer Pro treats as a read-only file.

To change the relationship between entities, or to create a relationship between two currently unrelated entities, use the hierarchy view and drag an entity onto the entity that you want it to be part of. If you want an entity to become a root entity, drag it to the Root transform at the top of the hierarchy view.

##### Modify or Create New Materials

When you import a USDZ model into Reality Composer Pro, it creates a RealityKit material for every physically-based rendering (PBR) material the asset contains. Reality Composer Pro displays materials in the hierarchy view just like it displays entities, except it uses a paintbrush icon. Reality Composer Pro doesn’t display materials in the 3D view.

> **Note**: The library in Reality Composer Pro contains materials for several common real-world surfaces like metal, wood, and denim that you can import into your project.

##### Build Materials in Shader Graph

PBR materials are great at reproducing real-world surfaces. However, they can’t represent nonrealistic materials like cartoon shaders, and they can’t contain logic. This means that you can’t animate a PBR material or have it react to input from your app.

Reality Composer Pro offers a second type of material called a . You can build and edit custom materials using the Shader Graph tab. Shader Graph provides a tremendous amount of control over materials and allows you to do things that would otherwise require writing Metal shaders. For more information on writing Metal shaders, see [`Metal`](https://developer.apple.com/documentation/Metal).

> **Note**: RealityKit doesn’t represent Reality Composer Pro custom materials as an instance of [`CustomMaterial`](https://developer.apple.com/documentation/RealityKit/CustomMaterial), as you might expect. Instead, RealityKit represents these materials as [`ShaderGraphMaterial`](https://developer.apple.com/documentation/RealityKit/ShaderGraphMaterial) instances.

![A screenshot showing a complex graph of nodes in the Shader Graph tab.](https://docs-assets.developer.apple.com/published/1994cf8e5f506e92a38542f52d2c41a8/RCPro-ShaderGraphWindow%402x.png)

The materials you build in the editor can affect both the look of an entity and its shape. If you build a node graph and connect it to the Custom Surface pin on the output node, that node graph controls the surface appearance of the model and roughly equates to writing Metal code in a fragment shader. If you build a node graph and connect it to the Custom Geometry Modifier output pin, those nodes control the shape of the entity, which equates to Metal code running in a vertex shader.

Nodes represent values and operations and serve the same purpose as either a variable or constant, or a function in Metal. If you need the sine of a value, for example, connect the value’s output node to the input pin of a `Sin` node. Add new nodes to the graph by double-clicking the background of the Shader Graph view or click the New Node button on the right side of the screen.

> ❗ **Important**: Some nodes, like `Sin`, are universal and can be used with either output pin. Other nodes are specific to either the Custom Surface or Geometry Modifier outputs. If a node name starts with Geometry Modifier, you can only connect it to the Geometry Modifier output pin. If the node’s name starts with “Surface”, you can only connect it to the Custom Surface output pin.

To unlock the real power of Shader Graph, you need to be able to change values on the material from Swift code. Shader Graph allows you to do this by creating , which are parameters you can set and read from Swift to change your material at runtime. If you have a feature that you want to turn on and off, you might create a Boolean input parameter and have conditional logic based on its value. If you want to smoothly interpolate between two colors, you might create a `Float` input parameter and use it to control how to interpolate between the two colors. You can Control-click on a constant node and select Promote to turn it into a promoted input. You can also turn a promoted input back into a constant by Control-clicking it and selecting Demote.

To change the value of an input parameter from Swift code, use [`setParameter(name:value:)`](https://developer.apple.com/documentation/RealityKit/ShaderGraphMaterial/setParameter(name:value:)), passing the name of the parameter and the new value. Note that parameter names are case sensitive, so your `name` string must exactly match what you called the parameter in Shader Graph.

For examples of Shader Graph use, see [`Diorama`](diorama.md) and [`Happy Beam`](happybeam.md).

##### Use References to Reuse Assets

If your project has multiple scenes that share assets, you can use references to avoid creating duplicate assets. A  acts like an alias in Finder — it points to the original asset and functions just as if it were another copy of that asset.

To add a reference, click the Add button (+) at the bottom of the references section in the inspector, choose the `.usda` file for the scene that contains the asset, then choose the asset you want to link to. After you do that, the selected entity or material becomes a copy of the one you linked to.

> ❗ **Important**: If you make changes to a linked asset, those changes will affect every linked reference.

##### Preview Scenes on Device

If you have an Apple Vision Pro connected to your Mac, choose Preview > Play or click the preview button in the Reality Composer Pro toolbar to view your scene on device. The Preview button is the left-most button on the right side of the toolbar — the one with an Apple Vision Pro icon. If you have multiple Apple Vision Pro devices connected, choose which device to use by clicking the pull-down menu next to the Preview button.

##### Load Reality Composer Pro Scenes in Realitykit

Loading a Reality Composer Pro scene is nearly identical to loading a USDZ asset from your app bundle, except you have to specify the Reality Composer Pro package bundle instead. You typically do this in the `make` closure of a [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) initializer. Reality Composer Pro packages define a global constant that points to its bundle, which is named after the project with “Bundle” appended to it. In the default Xcode visionOS template, the Reality Composer Pro project is called `RealityKitContent`, so the global bundle variable is called `realityKitContentBundle`:

```swift
RealityView { content in
    if let scene = try? await Entity.load(named: "Biplane", 
                                          in: realityKitContentBundle) {
        myDataModel.add(scene) 
        content.add(scene)
    }
} update: { content in
    // ...
}
```

> **Note**: The code above saves a reference to the root node. This isn’t required, but with [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView), unlike [`ARView`](https://developer.apple.com/documentation/RealityKit/ARView) on iOS and macOS, you don’t have ready access to the scene content, so it’s often handy to maintain your own reference to the root entity of your scene in your app’s data model.

When RealityKit finishes loading the scene, the `scene` variable contains the root entity of the scene you specified. Add it to `content` and RealityKit displays it to the user.

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
- [Capturing screenshots and video from Apple Vision Pro for 2D viewing](capturing-screenshots-and-video-from-your-apple-vision-pro-for-2d-viewing.md)
  Create screenshots and record high-quality video of your visionOS app and its surroundings for app previews.
- [Implementing object tracking in your visionOS app](implementing-object-tracking-in-your-visionos-app.md)
  Create engaging interactions by training models to recognize and track real-world objects in your app.
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionOS/designing-realitykit-content-with-reality-composer-pro)*