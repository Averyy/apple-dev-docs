# Embedding controls in an immersive space

**Framework**: visionOS

Keep controls visible throughout an immersive experience by displaying them in a window or a view attachment.

**Availability**:
- visionOS 26.0+
- Xcode 26.0+

#### Overview

This sample displays controls in an immersive space, either in their own window or embedded within the space. It uses the window’s scene phase to determine where the controls appear, and uses a [`ViewAttachmentComponent`](https://developer.apple.com/documentation/RealityKit/ViewAttachmentComponent) to embed the controls in the immersive space. For example, a creative app can let a person float the tool palette as its own window to browse materials, or show a simplified version in the immersive space for quick brush changes. A game might handle its map the same way: A mini map can be visible in the space during play, with the option to open it as a full window, complete with additional features like route planning and waypoints.

The sample includes the following scenes:

- A [`WindowGroup`](https://developer.apple.com/documentation/SwiftUI/WindowGroup) containing a [`NavigationStack`](https://developer.apple.com/documentation/SwiftUI/NavigationStack) for viewing sphere details and opening the immersive space
- A [`Window`](https://developer.apple.com/documentation/SwiftUI/Window) displaying controls
- An [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace) with a [`ViewAttachmentComponent`](https://developer.apple.com/documentation/RealityKit/ViewAttachmentComponent) for embedded controls

#### Handle the View Life Cycle

This sample app presents a controls window within an immersive space without using [`pushWindow`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/pushWindow) to associate the window with the immersive space. When a person closes the window, they remain in the immersive space without any controls. Similarly, if they close the immersive space, a controls window for the immersive space remains visible. At any time, they can close the immersive space and return to the visionOS apps screen. On relaunch, the app restores to the last opened nonimmersive scene. When there are multiple window scene types, the [`defaultLaunchBehavior(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/defaultLaunchBehavior(_:)) API can mark secondary windows as [`suppressed`](https://developer.apple.com/documentation/SwiftUI/SceneLaunchBehavior/suppressed), which prevents them from appearing when the system relaunches the application.

```swift
Window("Controls", id: SceneID.controlsScene.rawValue) {
    ControlsWindow()
        .environment(appModel)
}
.restorationBehavior(.disabled)
.defaultLaunchBehavior(.suppressed)
```

This sample code shows how to combine scene phase with [`ViewAttachmentComponent`](https://developer.apple.com/documentation/RealityKit/ViewAttachmentComponent) to keep controls visible within your immersive space. The controls provide an affordance to reopen the immersive space; the sample app shows a button to open the sphere launcher that opens an immersive space.

> **Note**: To present and dismiss the immersive space and window together, use [`pushWindow`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/pushWindow), which allows a person to dismiss any scene without staying in the immersive space. For an example, see [`Associating a window with an immersive space`](associating-a-window-with-an-immersive-space.md).

#### Embed Controls in the Immersive Space

The sample code launches with a [`WindowGroup`](https://developer.apple.com/documentation/SwiftUI/WindowGroup) that is a [`NavigationStack`](https://developer.apple.com/documentation/SwiftUI/NavigationStack) for viewing multiple `SphereDetails` navigation destinations at once. The navigation destination shows more information and provides a button to open the immersive space. In the immersive space, the app uses a [`ViewAttachmentComponent`](https://developer.apple.com/documentation/RealityKit/ViewAttachmentComponent) to provide fixed controls to the person. The app positions the controls out of the way so the person can interact with content in the immersive space and the windows. The following code displays the `ControlsAttachment` view using a [`ViewAttachmentComponent`](https://developer.apple.com/documentation/RealityKit/ViewAttachmentComponent) on an entity that is offset from the root of the scene:

```swift
let controlsEntity = Entity()
controlsEntity.position = SIMD3<Float>(x: 0, y: 1.0, z: -1.0)
controlsEntity.transform.rotation = simd_quatf(angle: -.pi / 6, axis: SIMD3<Float>(1, 0, 0))
controlsEntity.components.set(ViewAttachmentComponent(
    rootView: ControlsAttachment(sphere: sphere)
))
content.add(controlsEntity)
```

The `ControlsAttachment` shows a `DebugMainSceneStates` that displays the state of the different main navigation menus. When there’s no active sphere-navigation menu, the `ControlsAttachment` provides an option to open a new navigation stack window:

```swift
// When all main scenes are no longer active, provide an option to open a new main scene.
if !appModel.mainSceneStates.anySceneViewActive {
    Button {
        openWindow(id: SceneID.mainScene.rawValue)
    } label: {
        Text("Open Spheres Menu")
    }
}
```

The application monitors the state of the different main scenes using the [`ScenePhase`](https://developer.apple.com/documentation/SwiftUI/ScenePhase) property on the root view of the main scene.

```swift
.onAppear {
    appModel.mainSceneStates[windowID] = .inTransition
}
.onDisappear {
    appModel.mainSceneStates[windowID] = .closed
}
.onChange(of: scenePhase, initial: true) {
    appModel.mainSceneStates[windowID] = .open(scenePhase)
}
```

#### Move the Controls to a Separate Window

The sample app includes an additional window scene so it can present the controls using a system window rather than embedding them in the immersive space. This is a [`Window`](https://developer.apple.com/documentation/SwiftUI/Window), rather than a [`WindowGroup`](https://developer.apple.com/documentation/SwiftUI/WindowGroup), so there’s a single, unique window for the controls.

The sample disables the [`restorationBehavior(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/restorationBehavior(_:)) for this scene, informing the system to not restore this window on launch. Additionally, the sample configures [`defaultLaunchBehavior(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/defaultLaunchBehavior(_:)) as [`suppressed`](https://developer.apple.com/documentation/SwiftUI/SceneLaunchBehavior/suppressed) so if this is the last window when the application closes, the system doesn’t present it when the person taps the application icon to relaunch the app.

```swift
Window("Controls", id: SceneID.controlsScene.rawValue) {
    ControlsWindow()
        .environment(appModel)
}
.restorationBehavior(.disabled)
.defaultLaunchBehavior(.suppressed)
```

The window state of the controls window determines when the app shows the contents of the [`ViewAttachmentComponent`](https://developer.apple.com/documentation/RealityKit/ViewAttachmentComponent). When the controls window is open, the attachment is empty, and when the controls window closes, the attachment reappears.

```swift
var showControlsAttachment: Bool {
    if case .open = appModel.controlsWindowState {
        return false
    }

    return true
}

var body: some View {
    if showControlsAttachment {
        controls
    }
}
```

The app dismisses the controls window when the immersive space closes and other active windows exist.

```swift
.onChange(of: appModel.immersiveSpaceState) {
    if
        case .closed = appModel.immersiveSpaceState,
        appModel.mainSceneStates.anySceneViewActive
    {
        dismiss()
    }
}
```

When the controls window is the only open window, it provides a button to navigate to the spheres menu to open a new immersive space. This code provides the affordance to directly reopen the immersive space from the controls:

```swift
// When all main scenes are no longer active, provide an option to open a new main scene.
if !appModel.mainSceneStates.anySceneViewActive {
    Button {
        openWindow(id: SceneID.mainScene.rawValue)
    } label: {
        Text("Open Spheres Menu")
    }
}
```

#### Restore State Across Launches

Scene restoration is an important part of a seamless experience in visionOS. People expect content to persist where they’ve placed it. And after restarting their device, they expect to pick up where they left off.

> **Note**: For details on creating persistent and contextually relevant spatial experiences, see [`Adopting best practices for persistent UI`](adopting-best-practices-for-scene-restoration.md).

In this sample, a person can open multiple instances of the `SphereNavigationStack` to see the details of multiple spheres simultaneously. The sample uses [`SceneStorage`](https://developer.apple.com/documentation/SwiftUI/SceneStorage) to restore the destination of the `SphereNavigationStack`. Without this property wrapper, when the system restores the window, the `SphereNavigationStack` returns to its initial state, reset to the list of spheres.

```swift
/// The scene state for the sphere detail-navigation destination.
@SceneStorage("ContentView.selectedSphere") private var selectedSphereID: SphereModel.ID?
```

Similarly, the `ImmersiveView` uses [`AppStorage`](https://developer.apple.com/documentation/SwiftUI/AppStorage) to sync and store the transform of each sphere. The sample provides an initializer to this view so the storage key is unique per `SphereModel`.

```swift
@AppStorage private var sphereTransformLeft: StorableTransform
@AppStorage private var sphereTransformRight: StorableTransform

init(sphere: SphereModel) {
    self.sphere = sphere
    _sphereTransformLeft = AppStorage(wrappedValue: .left, sphere.leftKey)
    _sphereTransformRight = AppStorage(wrappedValue: .right, sphere.rightKey)
}
```

[`AppStorage`](https://developer.apple.com/documentation/SwiftUI/AppStorage) persists this state in [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults), a persistent store for app information. For secure storage of personal or sensitive information, use the person’s keychain, as described in [`Storing Keys in the Keychain`](https://developer.apple.com/documentation/Security/storing-keys-in-the-keychain).

##### Managing Multiple Scenes


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/embedding-controls-in-an-immersive-space)*