# Handling the window life cycle with multiple scenes

**Framework**: visionOS

Track scene state across different window types.

**Availability**:
- visionOS 26.0+
- Xcode 26.0+

#### Overview

This sample code project demonstrates managing the life cycle of multiple scene types. In visionOS, a person can close any scene of your application at any time. For applications that support multiple scenes, provide an affordance for the person to reopen the desired scene. This sample includes the following scenes:

- A [`Window`](https://developer.apple.com/documentation/swiftui/window) for quickly opening different sphere volumes
- A [`WindowGroup`](https://developer.apple.com/documentation/swiftui/windowgroup) for viewing sphere details and opening volumes
- A volumetric [`WindowGroup`](https://developer.apple.com/documentation/swiftui/windowgroup) for displaying the spheres

#### Manage the Scene Life Cycle

In visionOS, calling [`onAppear(perform:)`](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) on the root view of a scene updates state when that scene opens. Similarly, the [`onDisappear(perform:)`](https://developer.apple.com/documentation/swiftui/view/ondisappear(perform:)) method updates the state when the system eliminates that scene. When a person closes a window in visionOS, the system backgrounds that scene. When another nonimmersive scene of the application is open, the system also immediately eliminates the backgrounded scene. The last closed nonimmersive scene enters the [`ScenePhase.background`](https://developer.apple.com/documentation/swiftui/scenephase/background) phase but doesn’t immediately receive the [`onDisappear(perform:)`](https://developer.apple.com/documentation/swiftui/view/ondisappear(perform:)) callback. When a person reopens the application, the system launches the backgrounded scene. For more details on launch behavior, see [`Customize window launch behavior`](adopting-best-practices-for-scene-restoration#Customize-window-launch-behavior.md).

The sample creates a `WindowState` enumeration to save the window state and updates it when the life cycle of the scene changes:

```swift
/// The state of the sphere launcher window.
var sphereLauncherWindowState: WindowState = .closed
```

```swift
.onAppear {
    appModel.sphereLauncherWindowState = .inTransition
}
.onDisappear {
    appModel.sphereLauncherWindowState = .closed
}
.onChange(of: scenePhase, initial: true) {
    appModel.sphereLauncherWindowState = .open(scenePhase)
}
```

#### Open the Sphere Launcher Window

In the sample code, the `ControlsView` exists as an ornament on the `SphereVolume`. This view provides the controls to enlarge the content inside the volume and to open or close the sphere window.

```swift
let action = appModel.sphereLauncherWindowState == .closed ? "Open" : "Close"
Button("\(action) Sphere Launcher") {
    if appModel.sphereLauncherWindowState == .closed {
        openWindow(id: SceneID.sphereLauncher.rawValue)
    } else {
        dismissWindow(id: SceneID.sphereLauncher.rawValue)
    }
}
```

#### Track the Sphere Window States

The `AppModel` contains a dictionary for each of the sphere models to store the associated window state of each volume.

```swift
/// The state for each individual sphere volume.
var sphereVolumeStates: [SphereModel.ID: WindowState] = [:]
```

The view life cycle callbacks update this dictionary, which is used to determine when the windows open or close.

```swift
.onAppear {
    appModel.sphereVolumeStates[sphere] = .inTransition
}
.onDisappear {
    appModel.sphereVolumeStates[sphere] = .closed
}
.onChange(of: scenePhase, initial: true) {
    appModel.sphereVolumeStates[sphere] = .open(scenePhase)
}
```

The sphere launcher window shows each sphere option and a button to open the volume for that sphere.

![The window that contains the sphere launcher which has a button to open a volume for each provided color.](/images/com.apple.visionOS/sample-scenes-01-sphere-launcher-image.png)

The `WindowStateButton` uses the `sphereVolumeStates` on the `AppModel` to display either the close or open button, which calls [`dismissWindow`](https://developer.apple.com/documentation/swiftui/environmentvalues/dismisswindow) or [`openWindow`](https://developer.apple.com/documentation/swiftui/environmentvalues/openwindow), respectively.

```swift
if case .open = appModel.sphereVolumeStates[sphere.id] {
    CloseButton(sphere: sphere)
} else {
    OpenButton(sphere: sphere)
}
```

#### Restore Scene State Across Launches

Scene restoration is an important part of a seamless experience in visionOS. People expect content to persist where they place it. After restarting their device, they expect to pick up where they left off. This sample uses [`SceneStorage`](https://developer.apple.com/documentation/swiftui/scenestorage) to restore the sphere size in `SphereVolume` and to restore the navigation location in the `SphereNavigationStack`.

> **Note**: For more details on creating persistent and contextually relevant spatial experiences, see [`Adopting best practices for persistent UI`](adopting-best-practices-for-scene-restoration.md).

The volumetric windows start with an initial state of `enlarge` set to `false`. The app stores this value using [`SceneStorage`](https://developer.apple.com/documentation/swiftui/scenestorage) so when a person returns to this view, scene restoration restores it:

```swift
/// The scene state for the enlarged Boolean value, which is tied to the specific scene session
/// and not the identifiable model for the window group.
@SceneStorage("enlarge") var enlarge: Bool = false
```

As both `SphereVolume` and the `ControlsView` exist within the same scene, they can access the underlying value through [`SceneStorage`](https://developer.apple.com/documentation/swiftui/scenestorage) rather than using a [`Binding`](https://developer.apple.com/documentation/swiftui/binding).

The sample app stores the selected sphere using [`SceneStorage`](https://developer.apple.com/documentation/swiftui/scenestorage) for each [`WindowGroup`](https://developer.apple.com/documentation/swiftui/windowgroup) so when the system restores the scene, it also restores the selected detail screen.

```swift
/// The scene state for the sphere detail-navigation destination.
@SceneStorage("ContentView.selectedSphere") private var selectedSphereID: SphereModel.ID?
```

#### Manage Multiple Window Instances

When the main window is a [`WindowGroup`](https://developer.apple.com/documentation/swiftui/windowgroup), there are additional considerations because multiple instances of this window can be open at one time. The sample app uses [`openWindow`](https://developer.apple.com/documentation/swiftui/environmentvalues/openwindow) to create a new scene with the default value of `UUID()`, allowing a person to have multiple windows for this scene ID.

![Three windows of the same scene ID, showing different navigation destinations in each.](/images/com.apple.visionOS/sample-scenes-01-multiple-navigation-windows.png)

It uses [`dismissWindow`](https://developer.apple.com/documentation/swiftui/environmentvalues/dismisswindow) with an ID but without specifying a value, which dismisses all instances of that scene. The sample code provides an affordance to open a new `SphereNavigationStack` when there are no longer any active navigation windows.

```swift
if !appModel.navigationWindowScenes.anySceneViewActive {
    Button {
        openWindow(id: SceneID.navigationWindow.rawValue)
    } label: {
        Text("Open New Sphere Viewer")
    }
}

if !appModel.navigationWindowScenes.isEmpty {
    Button {
        dismissWindow(id: SceneID.navigationWindow.rawValue)
    } label: {
        Text("Close Sphere Viewer\(appModel.navigationWindowScenes.count > 1 ? "s" : "") (\(appModel.navigationWindowScenes.count))")
    }
}
```

##### Managing Multiple Scenes

Explore these concepts further in the following samples, which use window state to hide controls and transfer controls between a window and an immersive space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/handling-the-window-life-cycle-with-multiple-scenes)*