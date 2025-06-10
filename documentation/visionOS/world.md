# Hello World

**Framework**: visionOS

Use windows, volumes, and immersive spaces to teach people about the Earth.

**Availability**:
- visionOS 2.0+
- Xcode 16.0+

#### Overview

You can use visionOS scene types and styles to share information in fun and compelling ways. Features like volumes and immersive spaces let you put interactive virtual objects into people’s environments, or put people into a virtual environment.

Hello World uses these tools to teach people about the Earth — the planet we call home. The app shows how the Earth’s tilt creates the seasons, how objects move as they orbit the Earth, and how Earth appears from space.

The app uses SwiftUI to define its interface, including both 2D and 3D elements. To create, customize, and manage 3D models and effects, it also relies on the RealityKit framework and Reality Composer Pro.

##### Create an Entry Point Into the App

Hello World constructs the scene that it displays at launch — the first scene that appears in the `WorldApp` structure — using a [`WindowGroup`](https://developer.apple.com/documentation/SwiftUI/WindowGroup):

```swift
WindowGroup("Hello World", id: "modules") {
    Modules()
        .environment(model)
}
.windowStyle(.plain)
```

Like other platforms — for example, macOS and iOS — visionOS displays a window group as a familiar-looking window. In visionOS, people can resize and move windows around the Shared Space. Even if your app offers a sophisticated 3D experience, a window is a great starting point for an app because it eases people into the experience. It’s also a good place to provide instructions or controls.

> 💡 **Tip**: This particular window group uses the [`plain`](https://developer.apple.com/documentation/SwiftUI/WindowStyle/plain) window style to maintain control over the glass background effect that visionOS would otherwise automatically add.

##### Present Different Modules Using a Navigation Stack

After you watch a brief introductory animation that shows the text Hello World typing in, the `Modules` view that defines the primary scene’s content presents options to explore different aspects of the world. This view contains a table of contents at the root of a [`NavigationStack`](https://developer.apple.com/documentation/SwiftUI/NavigationStack):

```swift
NavigationStack(path: $model.navigationPath) {
    TableOfContents()
        .navigationDestination(for: Module.self) { module in
            ModuleDetail(module: module)
                .navigationTitle(module.eyebrow)
        }
}
```

The trailing closure of the [`navigationDestination(for:destination:)`](https://developer.apple.com/documentation/SwiftUI/View/navigationDestination(for:destination:)) view modifier in the code above displays a view when someone activates a link based on a `module` input that comes from the corresponding link’s initializer:

```swift
NavigationLink(value: module) { /* The link's label. */ }
```

The possible `module` values come from a custom `Module` enumeration:

```swift
enum Module: String, Identifiable, CaseIterable, Equatable {
    case globe, orbit, solar
    // ...
}
```

##### Display an Interactive Globe in a New Scene

To be able to open multiple scene types, Hello World includes the [`UIApplicationSceneManifest`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest) key in its [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List) file. The value for this key is a dictionary that includes the [`UIApplicationSupportsMultipleScenes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UIApplicationSupportsMultipleScenes) key with a value of `true`:

```swift
<key>UIApplicationSceneManifest</key>
<dict>
    <key>UIApplicationSupportsMultipleScenes</key>
    <true/>
    <key>UISceneConfigurations</key>
    <dict/>
</dict>
```

##### Declare a Volume for the Globe

With the key in place, the app makes use of a second [`WindowGroup`](https://developer.apple.com/documentation/SwiftUI/WindowGroup) in its [`App`](https://developer.apple.com/documentation/SwiftUI/App) declaration. This new window group uses the `Globe` view as its content:

```swift
WindowGroup(id: Module.globe.name) {
    Globe()
        .environment(model)
}
.windowStyle(.volumetric)
.defaultSize(width: 0.6, height: 0.6, depth: 0.6, in: .meters)
```

The `Globe` view inside the volume contains 3D content, but is still just a SwiftUI view. It contains two elements in a [`ZStack`](https://developer.apple.com/documentation/SwiftUI/ZStack): a subview that draws a model of the Earth, and another that provides a control panel that people can use to configure the model’s appearance.

##### Open and Dismiss the Globe Volume

```swift
struct GlobeToggle: View {
    @Environment(ViewModel.self) private var model
    @Environment(\.openWindow) private var openWindow
    @Environment(\.dismissWindow) private var dismissWindow

    var body: some View {
        @Bindable var model = model

        Toggle(Module.globe.callToAction, isOn: $model.isShowingGlobe)
            .onChange(of: model.isShowingGlobe) { _, isShowing in
                if isShowing {
                    openWindow(id: Module.globe.name)
                } else {
                    dismissWindow(id: Module.globe.name)
                }
            }
            .toggleStyle(.button)
    }
}
```

When someone taps the toggle, the `isShowingGlobe` state changes, and the [`onChange(of:initial:_:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:initial:_:)-4psgg) modifier calls the [`openWindow`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/openWindow) or [`dismissWindow`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/dismissWindow) action to open or dismiss the volume, respectively. The view gets these actions from the environment and uses an identifier that matches the volume’s identifier.

##### Display Objects That Orbit the Earth

Hello World loads these models from the asset bundle using a [`Model3D`](https://developer.apple.com/documentation/RealityKit/Model3D) structure inside a custom `ItemView`. The view scales and positions the model to fit the available space, and applies optional orientation adjustments:

```swift
private struct ItemView: View {
    var item: Item
    var orientation: SIMD3<Double> = .zero

    var body: some View {
        Model3D(named: item.name, bundle: worldAssetsBundle) { model in
            model.resizable()
                .scaledToFit()
                .rotation3DEffect(
                    Rotation3D(
                        eulerAngles: .init(angles: orientation, order: .xyz)
                    )
                )
                .frame(depth: modelDepth)
                .offset(z: -modelDepth / 2)
        } placeholder: {
            ProgressView()
                .offset(z: -modelDepth * 0.75)
        }
    }
}
```

The app uses this `ItemView` once for each model, placing each in an overlay that only becomes visible based on the current selection. For example, the following overlay displays the satellite model with a small amount of tilt in the x-axis and z-axis:

```swift
.overlay {
    ItemView(item: .satellite, orientation: [0.15, 0, 0.15])
        .opacity(selection == .satellite ? 1 : 0)
}
```

The [`VStack`](https://developer.apple.com/documentation/SwiftUI/VStack) that contains the models also contains a [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker) that people use to select a model to view:

```swift
Picker("Satellite", selection: $selection) {
    ForEach(Item.allCases) { item in
        Text(item.name)
    }
}
.pickerStyle(.segmented)
```

When you add 3D effects to a 2D window, keep this guidance in mind:

-  These kinds of effects add interest, but can unintentionally obscure important controls or information as people view the window from different directions.
-  Excess depth causes elements to clip. Account for any position or orientation changes that might occur after initial placement.
-  Again, account for potential movement after initial placement.

##### Show Earths Relationship to Its Satellites in an Immersive Space

> **Note**: To learn about designing with gestures in visionOS, read [`Gestures`](https://developer.apple.com/design/Human-Interface-Guidelines/gestures) in [`Human Interface Guidelines`](https://developer.apple.com/design/human-interface-guidelines).

To create this visualization, the app displays the `Orbit` view — which contains a single [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) that models the entire system — in an [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace) scene with the [`mixed`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/mixed) immersion style:

```swift
ImmersiveSpace(id: Module.orbit.name) {
    Orbit()
        .environment(model)
}
.immersionStyle(selection: $orbitImmersionStyle, in: .mixed)
```

As with any secondary scene in a visionOS app, this scene depends on having the [`UIApplicationSupportsMultipleScenes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UIApplicationSupportsMultipleScenes) key in the [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List) file. The app also opens and closes the space using a toggle view that resembles the one used for the globe:

```swift
struct OrbitToggle: View {
    @Environment(ViewModel.self) private var model
    @Environment(\.openImmersiveSpace) private var openImmersiveSpace
    @Environment(\.dismissImmersiveSpace) private var dismissImmersiveSpace

    var body: some View {
        @Bindable var model = model

        Toggle(Module.orbit.callToAction, isOn: $model.isShowingOrbit)
            .onChange(of: model.isShowingOrbit) { _, isShowing in
                Task {
                    if isShowing {
                        await openImmersiveSpace(id: Module.orbit.name)
                    } else {
                        await dismissImmersiveSpace()
                    }
                }
            }
            .toggleStyle(.button)
    }
}
```

There are a few key differences from the version that appears in the section [`Open and dismiss the globe volume`](world#Open-and-dismiss-the-globe-volume.md):

- `OrbitToggle` uses [`openImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/openImmersiveSpace) and [`dismissImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/dismissImmersiveSpace) from the environment, rather than the window equivalents.
- The dismiss action in this case doesn’t require an identifier, because people can only open one space at a time, even across apps.
- The open and dismiss actions for spaces operate asynchronously, and so they appear inside a [`Task`](https://developer.apple.com/documentation/Swift/Task).

##### View the Solar System From Space Using Full Immersion

> 💡 **Tip**: People can always close the currently open immersive space by pressing the device’s Digital Crown, but it’s typically useful when you provide a built-in mechanism to maintain control of the experience within your app.

The app uses another immersive space scene for this module, but here with the [`full`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/full) immersion style that turns off the passthrough video:

```swift
ImmersiveSpace(id: Module.solar.name) {
    SolarSystem()
        .environment(model)
}
.immersionStyle(selection: $solarImmersionStyle, in: .full)
```

This scene depends on the same [`UIApplicationSupportsMultipleScenes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UIApplicationSupportsMultipleScenes) key that other secondary scenes do, and is activated by a `SolarSystemToggle` that’s similar to the ones that the app uses for the other scenes:

```swift
struct SolarSystemToggle: View {
    @Environment(ViewModel.self) private var model
    @Environment(\.openImmersiveSpace) private var openImmersiveSpace
    @Environment(\.dismissImmersiveSpace) private var dismissImmersiveSpace

    var body: some View {
        Button {
            Task {
                if model.isShowingSolar {
                    await dismissImmersiveSpace()
                } else {
                    await openImmersiveSpace(id: Module.solar.name)
                }
            }
        } label: {
            if model.isShowingSolar {
                Label(
                    "Exit the Solar System",
                    systemImage: "arrow.down.right.and.arrow.up.left")
            } else {
                Text(Module.solar.callToAction)
            }
        }
    }
}
```

This control appears in the main window to provide a way to begin the fully immersive experience, and separately in the control panel as a way to exit the experience. Because the app uses this control as two distinct buttons rather than as a toggle in one location, it’s composed of a [`Button`](https://developer.apple.com/documentation/SwiftUI/Button) with behavior that changes depending on the app state rather than as a toggle with a button style.

To reuse the main window for the solar system controls, Hello World places both the navigation stack and the controls in a [`ZStack`](https://developer.apple.com/documentation/SwiftUI/ZStack), and then sets the opacity of each to ensure that only one appears at a time:

```swift
ZStack {
    SolarSystemControls()
        .opacity(model.isShowingSolar ? 1 : 0)

    NavigationStack(path: $model.navigationPath) {
        // ...
    }
    .opacity(model.isShowingSolar ? 0 : 1)
}
.animation(.default, value: model.isShowingSolar)
```

###### Related Samples

###### Related Articles

###### Related Videos


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/world)*