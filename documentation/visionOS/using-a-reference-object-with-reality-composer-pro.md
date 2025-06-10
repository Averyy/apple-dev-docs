# Using a reference object with Reality Composer Pro

**Framework**: visionOS

Import a reference object file to track a real-world object in your visionOS app.

#### Overview

You can use reference objects in your visionOS app to track real-world objects in a person’s surroundings. With this capability, you can attach virtual content to those real-world objects to create engaging experiences. For example, with a reference object, you can track a household item and add virtual content to it, like highlighting a part and showing how to fix it.

To create a reference object, first, you obtain a 3D model asset, train a machine learning model with that 3D model asset in Create ML, and then import the resulting reference object file into your app. With Reality Composer Pro, you can set up object tracking by using the reference object file as an anchor entity to track your real-world object in your app. For more information about creating a reference object file, see [`Implementing object tracking in your visionOS app`](implementing-object-tracking-in-your-visionos-app.md).

##### Set Up a Scene in Reality Composer Pro

You can use Reality Composer Pro to import your reference object file and set up it up for tracking. However, before importing your reference object file, you need to set up a scene in Reality Composer Pro by following these steps:

1. Create a project in Xcode using the visionOS app template.
2. When choosing options for your project, be sure to choose the RealityKit option from the Immersive Space Renderer pop-up menu to configure an immersive space.
3. Select the `Package` file with the `.realitycomposerpro` extension in the Project navigator on the left.
4. Click the Open in Reality Composer Pro button at the top right of the 3D View.
5. When Reality Composer Pro opens, delete both default spheres and the grid material in the Scene navigator on the left to begin with an empty scene.

![An Xcode screenshot showing the Package file selected in the Project navigator on the left, and the Open in Reality Composer Pro button highlighted at the top of the 3D View.](https://docs-assets.developer.apple.com/published/3b6af3b046f7a2bb43ef6f0818a2892c/package-and-rcp%402x.png)

##### Create an Anchor Entity

After creating an empty scene, you need to create an anchor entity for your reference object. This allows you to track the real-word object and attach virtual content to it.

Start by clicking the Add button (+) at the bottom of the Scene navigator on the left and choosing Transform from the menu.

![A Reality Composer Pro screenshot of the menu that appears when you click the Add button (+) in the Scene navigator. The Transform option is selected.](https://docs-assets.developer.apple.com/published/7220637c29c8cbe097cc4b2e94ff775c/adding-transform%402x.png)

To add anchoring behavior to the entity, you need to add a [`Component`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/component). Click the Add Component button at the bottom of the inspector area to the right of the 3D View. From the list of available components that appears, double-click the Anchoring option. The Anchoring component appears in the inspector area for the entity.

![A Reality Composer Pro screenshot highlighting the Add Component button and the Component library dialog with the Anchoring option selected.](https://docs-assets.developer.apple.com/published/dea309094ba7e4fb503583076c577521/adding-anchoring%402x.png)

The Anchoring component requires a target to tether the anchor entity to. Because you’re tracking an object within your app, click the Target pop-up button for the Anchoring component and choose Object from the menu.

![A Reality Composer Pro screenshot highlighting the Target pop-up menu with the Object option selected.](https://docs-assets.developer.apple.com/published/fdef2f1f1d3ede81347b4c08ca0fcac2/adding-anchoring-object%402x.png)

To import your reference object file, click the Anchor Object button for the Anchoring component, navigate to the file, and click Select.

![A Reality Composer Pro screenshot showing the File Selection dialog with a reference object file selected.](https://docs-assets.developer.apple.com/published/4aa6dfa606725c8041f356b734e82bb2/importing-reference-object%402x.png)

After importing your reference object file, a semitransparent model of it appears in the 3D View. You can use this  as a guide to place virtual content precisely on top of the real object.

You can move the visual cue away from the origin by moving an ancestor entity of the entity with the Anchoring component. This is particularly helpful when you have multiple entities acting as object anchors, which might cause the visual cues to overlap at the origin.

![A Reality Composer Pro screenshot showing the 3D View with a semitransparent model of the reference object.](https://docs-assets.developer.apple.com/published/af82fee711b9f9d15a483cdd2c514186/reference-object-model%402x.png)

To get the anchor’s position in the real world (an anchor transform) during tracking, you need to configure a `SpatialTrackingSession` using RealityKit. For more information, see [`SpatialTrackingSession`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/spatialtrackingsession/).

## See Also

- [Using a reference object with RealityKit](using-a-reference-object-with-realitykit.md)
  Import a reference object file to track a real-world object in your visionOS app.
- [Using a reference object with ARKit](using-a-reference-object-with-arkit.md)
  Import a reference object file and track a real-world object in your visionOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/using-a-reference-object-with-reality-composer-pro)*