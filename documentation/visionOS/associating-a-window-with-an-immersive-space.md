# Associating a window with an immersive space

**Framework**: visionOS  
**Role**: Sample Code  
**Download**: [AssociatingAWindowWithAnImmersiveSpace.zip](https://docs-assets.developer.apple.com/published/23edf9072f98/AssociatingAWindowWithAnImmersiveSpace.zip)

Tightly couple a window with an immersive space for persistent controls.

**Availability**:
- visionOS 26.0+
- Xcode 26.0+

#### Overview

This sample code project demonstrates how you can present an immersive space alongside a window so that both remain active together. Closing either the window or the immersive space closes the associated scene. This approach is useful when a window and an immersive space need to stay synchronized. For example, a shopping app can display a catalog with configuration options while showing a life-size replica of each selection in a person’s space, or a training app can present a checklist in the window that guides a person through tasks in the immersive experience.

[Video: An app transitioning in and out of the immersive space with a pushed window.](https://developer.apple.com/tutorials/videos/com.apple.visionOS/sample-scenes-02-associating-a-window-with-an-immersive-space.mov)

See [Embedding controls in an immersive space](./embedding-controls-in-an-immersive-space.md) for an alternative to this approach using [`ViewAttachmentComponent`](../RealityKit/viewattachmentcomponent.md).

#### Create three scenes

In the sample, [`pushWindow`](../SwiftUI/environmentvalues/pushwindow.md) opens a new window on top of the existing window. The system removes the existing window from view, and it enters the background scene phase. When the sample uses [`pushWindow`](../SwiftUI/environmentvalues/pushwindow.md) at the same time as [`openImmersiveSpace`](../SwiftUI/environmentvalues/openimmersivespace.md), the resulting  app consists of three scenes: the backgrounded scene that called [`pushWindow`](../SwiftUI/environmentvalues/pushwindow.md), the new visible window that [`pushWindow`](../SwiftUI/environmentvalues/pushwindow.md) opens, and the immersive scene.

```swift
.onChange(of: appModel.immersiveSpaceState) {
    if appModel.immersiveSpaceState == .open {
        pushWindow(id: SceneID.controlsScene.rawValue)
    }
}
```

The app can dismiss its own scenes as long as it’s not the last scene; the person decides when to dismiss the last scene, closing the app. The sample can close the scene that [`pushWindow`](../SwiftUI/environmentvalues/pushwindow.md) opens at any time to dismiss the pushed window and show the backgrounded window. When either the immersive scene or the system controls scene disappears, the sample app closes the other scene, which reactivates the backgrounded scene.

#### Dismiss the window and immersive space together

When the immersive space opens, the sample calls [`pushWindow`](../SwiftUI/environmentvalues/pushwindow.md) with the controls scene identifier inside of `ContentView`. The new controls scene replaces `ContentView`, and `ContentView` moves to the background.

The pushed window’s view uses two view modifiers to close the immersive space and the pushed window at the same time. The sample uses [`onDisappear(perform:)`](../SwiftUI/view/ondisappear%28perform%29.md) to detect when the system removes the pushed window from the view hierarchy and then to dismiss the immersive space. The sample app calls [`dismiss`](../SwiftUI/environmentvalues/dismiss.md) to dismiss the pushed window when the immersive space closes.

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

#### See Also

##### Managing multiple scenes

- [Handling the window life cycle with multiple scenes](./handling-the-window-life-cycle-with-multiple-scenes.md)
  Track scene state across different window types.
- [Embedding controls in an immersive space](./embedding-controls-in-an-immersive-space.md)
  Keep controls visible throughout an immersive experience by displaying them in a window or a view attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/associating-a-window-with-an-immersive-space)*