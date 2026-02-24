# Creating your first visionOS app

**Framework**: visionOS

Build a new visionOS app using SwiftUI and add platform-specific features.

#### Overview

If you’re new to visionOS, start with a new Xcode project to learn about the platform features, and to familiarize yourself with visionOS content and techniques. When you build an app for visionOS, SwiftUI is an excellent choice because it gives you full access to visionOS features. Although you can also use UIKit to build portions of your app, you need to use SwiftUI for many features that are unique to the platform.

> **Note**: Developing for visionOS requires a Mac with Apple silicon.

In any SwiftUI app, you place content onscreen using scenes. A scene contains the views and controls to display onscreen. Scenes also define the appearance of those views and controls when they appear onscreen. In visionOS, you can include both 2D and 3D views in the same scene, and you can present those views in a window or as part of the person’s surroundings.

Start with a new Xcode project and add features to familiarize yourself with visionOS content and techniques. Run your app in Simulator to verify your content looks like you expect, and run it on device to see your 3D content come to life.

Organize your content around one or more scenes, which manage your app’s interface. Each scene contains the views and controls you want to display, and the scene type determines whether your content adopts a 2D or 3D appearance. SwiftUI adds 3D scene types specifically for visionOS, and also adds 3D elements and layout options for all scene types.

##### Create Your Xcode Project

Create a new project in Xcode by choosing File > New > Project. Navigate to the visionOS section of the template chooser, and choose the App template. When prompted, specify a name for your project along with other options.

When creating a new visionOS app, you can configure your app’s initial scene types from the configuration dialog. To display primarily 2D content in your initial scene, choose a Window as your initial scene type. For primarily 3D content, choose a Volume. You can also add an immersive scene to place your content in the person’s surroundings.

![A screenshot of Xcode’s new project panel where you can select the initial scene type and immersive space options.](https://docs-assets.developer.apple.com/published/f0264311b8746ae62bc82059b514367a/xcode-template-options%402x.png)

Include a Reality Composer Pro project file when you want to create 3D assets or scenes to display from your app. Use this project file to build content from primitive shapes and existing USDZ assets. You can also use it to build and test custom RealityKit animations and behaviors for your content.

##### Modify the Existing Window

Build your initial interface using standard SwiftUI views. Views provide the basic content for your interface, and you customize the appearance and behavior of them using SwiftUI modifiers. For example, the `.background` modifier adds a partially transparent tint color behind your content:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
               .background(.black.opacity(0.8))
        }

        ImmersiveSpace(id: "Immersive") {
            ImmersiveView()
        }
    }
}
```

To learn more about how to create and configure interfaces using SwiftUI, see [`SwiftUI Essentials`](https://developer.apple.comhttps://developer.apple.com/tutorials/swiftui).

##### Handle Events in Your Views

Many SwiftUI views handle interactions automatically — all you do is provide code to run when the interactions occur. You can also add SwiftUI gesture recognizers to a view to handle tap, long-press, drag, rotate, and zoom gestures. The system automatically maps the following types of input to your SwiftUI event-handling code:

For more information about handling interactions in SwiftUI views, see [`Handling User Input`](https://developer.apple.comhttps://developer.apple.com/tutorials/swiftui/handling-user-input) in the [`SwiftUI Essentials`](https://developer.apple.comhttps://developer.apple.com/tutorials/swiftui) tutorial.

##### Build and Run Your App

Build and run your app in Simulator to see how it looks. Simulator for visionOS has a virtual background as the backdrop for your app’s content. Use your keyboard and your mouse or trackpad to navigate around the environment and interact with your app.

Tap and drag the window bar below your app’s content to reposition the window in the environment. Move the pointer over the circle next to the window bar to reveal the window’s close button. Move the cursor to one of the window’s corners to turn the window bar into a resizing control.

> **Note**: Apps don’t control the placement of windows in the space. The system places each window in its initial position, and updates that position based on further interactions with the app.

For additional information about how to interact with your app in Simulator, see [`Interacting with your app in the visionOS simulator`](https://developer.apple.com/documentation/Xcode/interacting-with-your-app-in-the-visionos-simulator).

## See Also

- [Adding 3D content to your app](adding-3d-content-to-your-app.md)
  Add depth and dimension to your visionOS app and discover how to incorporate your app’s content into a person’s surroundings.
- [Creating fully immersive experiences in your app](creating-fully-immersive-experiences.md)
  Build fully immersive experiences by combining spaces with content you create using RealityKit or Metal.
- [Drawing sharp layer-based content in visionOS](drawing-sharp-layer-based-content.md)
  Deliver text and vector images at multiple resolutions from custom Core Animation layers in visionOS.
- [Introductory visionOS samples](introductory-visionos-samples.md)
  Learn the fundamentals of building apps for visionOS with beginner-friendly sample code projects.
- [Combining spatial support from multiple frameworks](combining-spatial-support-from-multiple-frameworks.md)
  Integrate the features of an array of frameworks seamlessly to enhance your spatial app.
- [Connecting iPadOS and visionOS apps over the local network](connecting-ipados-and-visionos-apps-over-the-local-network.md)
  Build an iPadOS companion app to control your visionOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/creating-your-first-visionos-app)*