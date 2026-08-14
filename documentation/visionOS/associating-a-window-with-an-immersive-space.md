# Associating a window with an immersive space

**Framework**: visionOS

Tightly couple a window with an immersive space for persistent controls.

**Availability**:
- visionOS 26.0+
- Xcode 26.0+

#### Overview

This sample code project demonstrates how you can present an immersive space alongside a window so that both remain active together. Closing either the window or the immersive space closes the associated scene. This approach is useful when a window and an immersive space need to stay synchronized. For example, a shopping app can display a catalog with configuration options while showing a life-size replica of each selection in a person’s space, or a training app can present a checklist in the window that guides a person through tasks in the immersive experience.

See [`Embedding controls in an immersive space`](embedding-controls-in-an-immersive-space.md) for an alternative to this approach using [`ViewAttachmentComponent`](https://developer.apple.com/documentation/realitykit/viewattachmentcomponent).

#### Create Three Scenes

In the sample, [`pushWindow`](https://developer.apple.com/documentation/swiftui/environmentvalues/pushwindow) opens a new window on top of the existing window. The system removes the existing window from view, and it enters the background scene phase. When the sample uses [`pushWindow`](https://developer.apple.com/documentation/swiftui/environmentvalues/pushwindow) at the same time as [`openImmersiveSpace`](https://developer.apple.com/documentation/swiftui/environmentvalues/openimmersivespace), the resulting  app consists of three scenes: the backgrounded scene that called [`pushWindow`](https://developer.apple.com/documentation/swiftui/environmentvalues/pushwindow), the new visible window that [`pushWindow`](https://developer.apple.com/documentation/swiftui/environmentvalues/pushwindow) opens, and the immersive scene.

```swift
.onChange(of: appModel.immersiveSpaceState) {
    if appModel.immersiveSpaceState == .open {
        pushWindow(id: SceneID.controlsScene.rawValue)
    }
}
```

The app can dismiss its own scenes as long as it’s not the last scene; the person decides when to dismiss the last scene, closing the app. The sample can close the scene that [`pushWindow`](https://developer.apple.com/documentation/swiftui/environmentvalues/pushwindow) opens at any time to dismiss the pushed window and show the backgrounded window. When either the immersive scene or the system controls scene disappears, the sample app closes the other scene, which reactivates the backgrounded scene.

#### Dismiss the Window and Immersive Space Together

When the immersive space opens, the sample calls [`pushWindow`](https://developer.apple.com/documentation/swiftui/environmentvalues/pushwindow) with the controls scene identifier inside of `ContentView`. The new controls scene replaces `ContentView`, and `ContentView` moves to the background.

The pushed window’s view uses two view modifiers to close the immersive space and the pushed window at the same time. The sample uses [`onDisappear(perform:)`](https://developer.apple.com/documentation/swiftui/view/ondisappear(perform:)) to detect when the system removes the pushed window from the view hierarchy and then to dismiss the immersive space. The sample app calls [`dismiss`](https://developer.apple.com/documentation/swiftui/environmentvalues/dismiss) to dismiss the pushed window when the immersive space closes.

```swift
.onDisappear {
    Task {
        if appModel.immersiveSpaceState == .open {
            await dismissImmersiveSpace()
        }
    }
}
.onChange(of: appModel.immersiveSpaceState) {
    if appModel.immersiveSpaceState == .closed {
        dismiss()
    }
}
```

##### Managing Multiple Scenes


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/associating-a-window-with-an-immersive-space)*