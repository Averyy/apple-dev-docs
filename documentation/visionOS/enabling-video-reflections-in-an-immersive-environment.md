# Enabling video reflections in an immersive environment

**Framework**: Visionos

Create a more immersive experience by adding video reflections in a custom environment.

**Availability**:
- visionOS 2.0+
- Xcode 16.0+

#### Overview

RealityKit and Reality Composer Pro provide the tools to build immersive media viewing environments in visionOS. The [`Destination Video`](destination-video.md) sample uses these features to build a realistic custom environment called Studio. The environment adds to its realism and makes the video player feel grounded in the space by applying reflections of the player’s content onto the surfaces of the scene.

RealityKit and Reality Composer Pro support two types of video reflections:

- Specular reflections provide a direct reflection of the video content, and are typically useful to apply to glossy surfaces like metals and water.
- Diffuse reflections provide a softer falloff of video content, and are useful to apply to rougher, more organic surfaces.

This article describes how to adopt reflections in your own environment, and shows how Destination Video’s Studio environment supports these effects to create a compelling media viewing experience.

#### Define a Video Docking Location

Apps that use [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) to present video participate in system docking behavior. When you play a full-window video inside an immersive space, the system docks the video screen into a fixed location and presents streamlined playback controls. By default, the system determines the docking location for the scene, but starting in visionOS 2, you can customize this location by specifying a custom docking region.

The Studio environment defines a custom docking region that anchors the player to the walkway at the top of the staircase like shown below.

![An image that shows a bounding rectangle that represents the docked location of the video screen. The scene anchors the video screen to the walkway that runs horizontally across the immersive environment.](https://docs-assets.developer.apple.com/published/0031e4d0a7d2af1bec510593134e6f32/docking-region.jpg)

To create the docking region, the project defines a `Player` entity that contains a [`DockingRegionComponent`](https://developer.apple.com/documentation/RealityKit/DockingRegionComponent). This component defines the bounding region for the player, which has a depth of 0 and uses a fixed 2.4:1 aspect ratio. You configure the docking region’s size through its `width` property, and you can optionally specify a preview video to display in the docking region’s space within Reality Composer Pro.

![An image that shows a docking region component in Reality Composer Pro’s Inspector pane. The component has the title Docking Region at the top. Below the title is a width field with the value of 850 centimeters. Below the width configuration is a button to select a preview video to display within Reality Composer Pro.](https://docs-assets.developer.apple.com/published/fbcb1da42d7b60a5a419c358def079a0/docking-region-component%402x.png)

To provide an optimal viewing experience, the Studio environment minimizes objects between the viewer and the video. Additionally, it provides a comfortable viewing angle to avoid causing strain or discomfort during longer viewing sessions. Using Reality Composer Pro to define the docking region is a great way to visualize how it looks in context, but always review your environment on Apple Vision Pro to get a true sense of layout and scale.

> **Note**: Reality Composer Pro provides a template to set up a docking region and default video reflection configuration. You can access this template from the Insert menu by selecting Insert > Environment > Video Dock.

Reality Composer Pro provides a template to set up a docking region and default video reflection configuration. You can access this template from the Insert menu by selecting Insert > Environment > Video Dock.

#### Display Specular Video Reflections

Specular reflections, like shown below, provide a direct reflection of the video’s content onto surrounding surfaces. You typically apply this type of reflection to glossy surfaces such as metals, mirrors, and water.

![An image that shows an example of a specular reflection. The image displays a multicolored bounding rectangle that represents a docked video screen. Below the video screen is a mirror image reflection of it on the ground plane.](https://docs-assets.developer.apple.com/published/50e416ed9a99d74e6ad7fa1f091d7ef0/specular-example%402x.png)

To enable this type of reflection, you define a material with the [`Reflection Specular (RealityKit)`](https://developer.apple.com/documentation/ShaderGraph/Other/Reflection-Specular-(RealityKit)) node connected and apply it to a surface in your scene. The system automatically calculates the appropriate reflection based on your viewing angle relative to the docking region.

![An image that shows the Reflection Specular node in Reality Composer Pro’s Shader Graph. The image shows a View Direction node connected to the Unreflected Direction input of the reflection node, and the output of the reflection node connected to an undetermined destination.](https://docs-assets.developer.apple.com/published/f76f8e1519599bb125e4a628cddaf47f/specular-shader-graph%402x.png)

The output of this node contains the reflected color in the RGB channels, and a blend factor in the alpha channel, which you can use to composite the reflection with your existing material.

Destination Video uses subtle specular reflections in its custom environment like shown below. Applying specular reflections helps to add depth and space to the experience. To learn more about how the environment uses specular reflections, open the Studio project in Reality Composer Pro to view its configuration.

![An image of Destination Video’s Studio environment. The image shows the docked video screen casting a subtle specular reflection of the video content onto the floor of the environment.](https://docs-assets.developer.apple.com/published/8cf84fa7d1d72c9af58913d80f0418f9/specular-example-dv.jpg)

#### Provide Diffuse Video Reflections

Diffuse reflections provide a softer falloff of media content, which can be useful to apply to rougher, more organic surfaces like a concrete or wood floor. The image below shows a diffuse reflection from a video screen.

![An image that shows an example of a diffuse reflection. The image shows a multicolored bounding rectangle that represents a docked video screen. Below the video screen is a soft glow of the video content’s color and light reflected on onto the ground plane.](https://docs-assets.developer.apple.com/published/a8ca9357b8fc1b65d22337b75cee0a39/diffuse-example%402x.png)

You enable diffuse reflections by adding a material on a surface with the [`Reflection Diffuse (RealityKit)`](https://developer.apple.com/documentation/ShaderGraph/Other/Reflection-Diffuse-(RealityKit)) node connected.

![An image that shows the Reflection Diffuse node in Reality Composer Pro’s Shader Graph. The image shows two Primvar Reader nodes connected to inputs of the reflection node. The configuration connects one node to the Emitter UV input of the reflection node and the other to the Attenuation UV input. The output of the Reflection Diffuse node connects to an undetermined destination.](https://docs-assets.developer.apple.com/published/4dfa7f4477e06cfa2b5595995104c560/diffuse-shader-graph%402x.png)

This node requires the following inputs:

Destination Video’s custom environment applies diffuse reflections to the surfaces immediately surrounding the docked video screen as shown below:

![An image that shows an example of a diffuse reflection. The image shows a multicolored bounding rectangle that represents a docked video screen. Below the video screen is a soft glow of the video content’s color and light reflected onto the ground plane.](https://docs-assets.developer.apple.com/published/1b725833f0413adea7a6c41d9389dc88/diffuse-example-dv.jpg)

Enabling diffuse reflections enhances the level of immersion by making the video player feel grounded in the experience.

To calculate Emitter UVs, iterate over each vertex of the surface mesh, and sample a set number of random points on the docking region. The u-value and v-value of each of the random sample points on the docking region are weighted by measuring both the distance and the angle to the mesh vertex. The resulting emitter UV set is the average of the weighted docking region UV values.

> ❗ **Important**: The number of random points sampled from the docking region can have a large impact on the overall computation time when generating emitter UVs. You can configure how many samples to use when calculating emitter UVs with the [`ComputeDiffuseReflectionUVs`](https://developer.apple.comhttps://developer.apple.com/sample-code/ar/WWDC_2024_Diffuse_Reflection_UV_Computation_Tool.zip) python script.

The number of random points sampled from the docking region can have a large impact on the overall computation time when generating emitter UVs. You can configure how many samples to use when calculating emitter UVs with the [`ComputeDiffuseReflectionUVs`](https://developer.apple.comhttps://developer.apple.com/sample-code/ar/WWDC_2024_Diffuse_Reflection_UV_Computation_Tool.zip) python script.

Attenuation UVs are a top-down projection of the attenuation texture onto the input geometry (UV-coordinate system). An attenuation texture contains a soft falloff mask that shapes the light from the emitter.

The attenuation texture contains a falloff pattern that shapes the the diffuse reflection on to the surface mesh. The image below shows the default Reality Composer Pro attenuation texture.

![The default Reality Composer Pro attenuation texture.](https://docs-assets.developer.apple.com/published/d3d5a8bb938c3b15baf21c98805b9536/attenuation-uv-default-texture%402x.png)

The default falloff pattern doesn’t extend all the way to the edges of the texture. In order to generate the attenuation UV set, calculate the edges of the falloff pattern from the texture. The image below shows the default falloff pattern in a standard UV-coordinate system, with the top-left point equal to `(0,0)` and the bottom-right point equal to `(1,1)`.

![A visualization of the values used to calculate the attenuation UV set from the default Reality Composer Pro attenuation texture.](https://docs-assets.developer.apple.com/published/6df1627df0e30884cd82409b64ddf595/attenuation-uv-texture-calculations%402x.png)

The following four values define the attenuation UV set:

After calculating the attenuation texture, map it to the geometry. To visualize the attenuation texture mapping, the image below shows a square red mesh as the custom surface mesh that extends towards the user with sides that are equal to the width of the docking region.

![A illustration of a simple scene setup that has a grey square to represent the docking reigon, a red square with sides equal to the width of the docking region that extends towards a representation of the user.](https://docs-assets.developer.apple.com/published/b77e0e9753206ad08d5fbd5bc06d2d32/attenuation-sample-scene%402x.png)

The attenuation UVs are calculated from mapping the surface mesh, in world space, to the area defined by the `uStart`, `uEnd`, `vStart`, and `vEnd` values, in the UV-coordinate space. The image below shows the surface mesh with the attenuation texture applied.

![An illustration of a simple scene setup that has a grey square to represent the docking reigon, a dotted-line outlines a square that extends towards a representation of the user. A line extends to the left from each corner of the outline of the square which connects to the corner of a rectangle that's on top of the default attenuation pattern.](https://docs-assets.developer.apple.com/published/ddedab266bd956caabc86b1ae9a327cb/attenuation-uv-mapping%402x.png)

> **Note**: When using the [`ComputeDiffuseReflectionUVs`](https://developer.apple.comhttps://developer.apple.com/sample-code/ar/WWDC_2024_Diffuse_Reflection_UV_Computation_Tool.zip) python script for mapping using a custom attenuation texture, you only need to measure the the `uStart`, `uEnd`, `vStart`, and `vEnd` values of your attenuation texture. If you’re using the default attenuation texture in Reality Composer Pro, the script uses the default values.

When using the [`ComputeDiffuseReflectionUVs`](https://developer.apple.comhttps://developer.apple.com/sample-code/ar/WWDC_2024_Diffuse_Reflection_UV_Computation_Tool.zip) python script for mapping using a custom attenuation texture, you only need to measure the the `uStart`, `uEnd`, `vStart`, and `vEnd` values of your attenuation texture. If you’re using the default attenuation texture in Reality Composer Pro, the script uses the default values.

To learn more about how the environment sets up and applies diffuse reflections, open the Studio project in Reality Composer Pro to view its configuration.

###### Related Samples

###### Related Articles

###### Related Videos


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/enabling-video-reflections-in-an-immersive-environment)*