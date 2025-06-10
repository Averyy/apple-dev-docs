# Diorama

**Framework**: visionOS

Design scenes for your visionOS app using Reality Composer Pro.

**Availability**:
- visionOS 2.0+
- Xcode 16.1+

#### Overview

Use Reality Composer Pro to compose, edit, and preview RealityKit content for your visionOS app. In your Reality Composer Pro project, you can create one or more scenes, each of which contains a hierarchy of virtual objects called entities that your app can efficiently load and display.

In addition to helping you compose entity hierarchies, Reality Composer Pro also gives you the ability to add and configure components — even custom components that you’ve written — to the entities in your scenes.

You can also design the visual appearance of entities using , a node-based visual tool for creating RealityKit materials. Shader Graph gives you a tremendous amount of control over the surface details and shape of entities. You can even create animated materials and dynamic materials that change based on the state of your app or user input.

Diorama demonstrates many of RealityKit and Reality Composer Pro’s features. It displays an interactive, virtual topographical trail map, much like the real-world dioramas you find at trailheads and ranger stations in national parks. This virtual map has points of interest you can tap to bring up more detailed information. You can also smoothly transition between two trail maps: Yosemite and Catalina Island.

##### Import Assets for Building the Scene

Diorama uses custom assets instead of the available library assets. To use custom assets in your own Reality Composer Pro scenes, import them into your project in one of three ways: by dragging them to Reality Composer Pro’s project browser, using File > Import from the File menu, or copying the assets into the `.rkassets` bundle inside your project’s Swift package.

![A screenshot that shows Reality Composer Pro with multiple scenes open. At the top of the window are several tabs, one for each open scene. The project browser is showing a selection of assets including sound files, images, and 3D models.](https://docs-assets.developer.apple.com/published/e31f4da3e3aadabb15f50ace406f6b81/rcpro-assets%402x.png)

> **Note**: Although you can still load USDZ files and other assets directly in visionOS, RealityKit compiles assets in your Reality Composer Pro project into a binary format that loads considerably faster than loading from individual files.

##### Create Scenes Containing the Apps Entities

A single Reality Composer Pro project can have multiple scenes. A  is an entity hierarchy stored in the project as a `.usda` file that you can load and display in a [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView). You can use Reality Composer’s scenes to build an entire RealityKit scene, or to store reusable entity hierarchies that you can use as building block for composing scenes at runtime — the approach Diorama uses. You can add as many different scenes to your project as you need by selecting File > New > Scene, or pressing ⌘N.

At the top of the Reality Composer Pro window, there’s a separate tab for every scene that’s currently open. To open a scene, double-click the scene’s `.usda` file in the project browser. To edit a scene, select its tab, and make changes using the hierarchy viewer, the 3D view, and the inspector.

![A screenshot showing Reality Composer Pro with multiple scenes open. At the top of the window are several tabs, one for each open scene.](https://docs-assets.developer.apple.com/published/7b08ca4b0e489767d821e0ae7b79d895/rcpro-scene-tabs%402x.png)

##### Add Assets to Your Scenes

RealityKit can only include entities in a scene, but it can’t use every type of asset that Reality Composer Pro supports as an entity. Reality Composer Pro automatically turns some assets, like 3D models, into an entity when you place them in a scene. It uses other assets indirectly. It uses image files, for example, primarily to define the surface details of model entities.

Diorama uses multiple scenes to group assets together and then, at runtime, combines those scenes into a single immersive experience. For example, the diorama table has its own scene that includes the table, the map surface, and the trail lines. There are separate scenes for the birds that flock over the table, and for the clouds that float above it.

##### Add Components to Entities

RealityKit follows a design pattern called Entity Component System (ECS). In an ECS app, you store additional data on an entity using components and can implement entity behavior by writing systems that use the data from those components. You can add and configure components to entities in Reality Composer Pro, including both shipped components like `PhysicsBodyComponent`, and custom components that you write and place in the Sources folder of your Reality Composer Pro Swift package. You can even create new components in Reality Composer Pro and then edit them in Xcode. For more information about ECS, see [`Understanding the modular architecture of RealityKit`](understanding-the-realitykit-modular-architecture.md).

Diorama uses custom components to identify which transforms are points of interest, to mark the birds so the app can make sure they flock together, and to control the opacity of entities that are specific to just one of the two maps.

To add a component to an entity, select that entity in the hierarchy view or 3D view. At the bottom right of the inspector window, click on the Add Component button. A list of available components appears and the first item in that list is New Component. This item creates a new component class, and optionally a new system class, and adds the component to the selected entity.

##### Use Transforms to Mark Locations

In Reality Composer Pro, a  is an empty entity that marks a point in space. A transform contains a location, rotation, and scale, and its child entities inherit those. But, transforms have no visual representation and do nothing by themselves. Use transforms to mark locations in your scene or organize your entity hierarchy. For example, you might make several entities that need to move together into child entities of the same transform, so you can move them together by moving the parent transform.

##### Load a Scene at Runtime

To load a Reality Composer Pro scene, use [`load(named:in:)`](https://developer.apple.com/documentation/RealityKit/Entity/load(named:in:)), passing the name of the scene you want to load and the project’s bundle. Reality Composer Pro Swift packages define a constant that provides ready access to its bundle. The constant is the name of the Reality Composer Pro project with “Bundle” appended to the end. In this case, the project is called `RealityKitContent`, so the constant is called `RealityKitContentBundle`. Here’s how Diorama loads the map table in the [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) initializer:

```swift
let entity = try await Entity.load(named: "DioramaAssembled", 
                                   in: RealityKitContent.RealityKitContentBundle)
```

The [`load(named:in:)`](https://developer.apple.com/documentation/RealityKit/Entity/load(named:in:)) function is asynchronous when called from an asynchronous context. Because the content closure of the [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) initializer is asynchronous, it automatically uses the `async` version to load the scene.  Note that when using it asynchronously, you must call it using the `await` keyword.

##### Create the Floating View

Diorama adds a `PointOfInterestComponent` to a transform to display details about interesting places. Every point of interest’s name appears in a view that floats above its location on the map. When you tap the floating view, it expands to show detailed information, which the app pulls from the `PointOfInterestComponent`. The app shows these details by creating a SwiftUI view for each point of interest and querying for all entities that have a `PointOfInterestComponent` using this query declared in `ImmersiveView.swift`:

```swift
static let markersQuery = EntityQuery(where: .has(PointOfInterestComponent.self))
```

In the [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) initializer, Diorama queries to retrieve the points of interest entities and passes them to a function called `createLearnMoreView(for:)`, which creates the view and saves it for display when it’s tapped.

```swift
subscriptions.append(content.subscribe(to: ComponentEvents.DidAdd.self, componentType: PointOfInterestComponent.self, { event in
    createLearnMoreView(for: event.entity)
}))
```

##### Create Attachments for Points of Interest

Diorama displays the information added to a `PointOfInterestComponent` in a `LearnMoreView`, which it stores as an attachment.  are SwiftUI views that are also RealityKit entities and that you can place into a RealityKit scene at a specific location. Diorama uses attachments to position the view that floats above each point of interest.

The app first checks to see if the entity has a component called `PointOfInterestRuntimeComponent`. If it doesn’t, it creates a new one and adds it to the entity. This new component contains a value you only use at runtime that you don’t need to edit in Reality Composer Pro.

By putting this value into a separate component and adding it to entities at runtime, Reality Composer Pro never displays it in the inspector. The `PointOfInterestRuntimeComponent` stores an identifier called an , which uniquely identifies an attachment so the app can retrieve and display it at the appropriate time.

```swift
struct PointOfInterestRuntimeComponent: Component {
    let attachmentTag: ObjectIdentifier
}
```

Next, Diorama creates a SwiftUI view called a `LearnMoreView` with the information from the `PointOfInterestComponent`, tags that view, and stores the tag in the `PointOfInterestRuntimeComponent`. Finally, it stores the view in an `AttachmentProvider`, which is a custom class that maintains references to the attachment views so they don’t get deallocated when they’re not in a scene.

```swift
let tag: ObjectIdentifier = entity.id

let view = LearnMoreView(name: pointOfInterest.name,
                         description: pointOfInterest.description ?? "",
                         imageNames: pointOfInterest.imageNames,
                         trail: trailEntity,
                         viewModel: viewModel)
    .tag(tag)
entity.components[PointOfInterestRuntimeComponent.self] = PointOfInterestRuntimeComponent(attachmentTag: tag)

attachmentsProvider.attachments[tag] = AnyView(view)
```

##### Display Point of Interest Attachments

Assigning a view to an attachment provider doesn’t actually display that view in the scene. The initializer for [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) has an optional view builder called `attachments` that’s used to specify the attachments.

```swift
ForEach(attachmentsProvider.sortedTagViewPairs, id: \.tag) { pair in
    pair.view
}
```

In the `update` closure of the initializer, which RealityKit calls when the contents of the view change, the app queries for entities with a `PointOfInterestRuntimeComponent`, uses the tag from that component to retrieve the correct attachment for it, and then adds that attachment and places it above its location on the map.

```swift
viewModel.rootEntity?.scene?.performQuery(Self.runtimeQuery).forEach { entity in

    guard let attachmentEntity = attachments.entity(for: component.attachmentTag) else { return }
    
    if let pointOfInterestComponent = entity.components[PointOfInterestComponent.self] {
        attachmentEntity.components.set(RegionSpecificComponent(region: pointOfInterestComponent.region))
        attachmentEntity.components.set(OpacityComponent(opacity: 0))
    }
    
    viewModel.rootEntity?.addChild(attachmentEntity)
    attachmentEntity.setPosition([0, 0.2, 0], relativeTo: entity)
}
```

##### Create Custom Materials with Shader Graph

To switch between the two different topographical maps, Diorama shows a slider that morphs the map between the two locations. To accomplish this, and to draw elevation lines on the map, the `FlatTerrain` entity in the `DioramaAssembled` scene uses a . Shader Graph is a node-based material editor that’s built into Reality Composer Pro. Shader Graph gives you the ability to create dynamic materials that you can change at runtime. Prior to Reality Composer Pro, the only way to implement a dynamic material like this was to create a [`CustomMaterial`](https://developer.apple.com/documentation/RealityKit/CustomMaterial) and write Metal shaders to implement the necessary logic.

Diorama’s `DynamicTerrainMaterialEnhanced` does two things. It draws contour lines on the map based on height data stored in displacement map images, and it also offsets the vertices of the flat disk based on the same data. By interpolating between two different height maps, the app achieves a smooth transition between the two different sets of height data.

Node graphs can contain , which are similar to functions. They contain reusable sets of nodes with inputs and outputs. Subgraphs contain the logic to draw the contour lines and the logic to offset the vertices. Double-click a subgraph to edit it. For more information about building materials using Shader Graph, see [`Explore Materials in Reality Composer Pro`](https://developer.apple.comhttps://developer.apple.com/wwdc23/10202).

##### Update the Shader Graph Material at Runtime

To change the map, `DynamicTerrainMaterialEnhanced` has a promoted input called `Progress`. If that parameter is set to `1.0`, it displays Catalina Island. If it’s set to `0`, it displays Yosemite. Any other number shows a state in transition between the two. When someone manipulates the slider, the app updates that input parameter based on the slider’s value.

> ❗ **Important**: Shader Graph material parameters are case-sensitive. If the capitalization is wrong, your code won’t actually update the material.

The app sets the value of the input parameter in a function called `handleMaterial()` that the slider’s `.onChanged` closure calls. That function retrieves the [`ShaderGraphMaterial`](https://developer.apple.com/documentation/RealityKit/ShaderGraphMaterial) from the terrain entity and calls [`setParameter(name:value:)`](https://developer.apple.com/documentation/RealityKit/ShaderGraphMaterial/setParameter(name:value:)) on it.

```swift
private func handleMaterial() {
    guard let terrain = viewModel.rootEntity?.terrain,
            let terrainMaterial = terrainMaterial else { return }
    do {
        var material = terrainMaterial
        try material.setParameter(name: materialParameterName, value: .float(viewModel.sliderValue))
        
        if var component = terrain.modelComponent {
            component.materials = [material]
            terrain.components.set(component)
        }
        
        try terrain.update(shaderGraphMaterial: terrainMaterial, { m in
            try m.setParameter(name: materialParameterName, value: .float(viewModel.sliderValue))
        })
    } catch {
        print("problem: \(error)")
    }
}
```

###### Related Samples

###### Related Articles

###### Related Videos


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/diorama)*