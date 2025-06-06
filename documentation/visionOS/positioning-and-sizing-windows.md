# Positioning and sizing windows

**Framework**: Visionos

Influence the initial geometry of windows that your app presents.

#### Overview

visionOS and macOS enable people to move and resize windows. In some cases, your app can use scene modifiers to influence a window’s initial geometry on these platforms, as well as to specify the strategy that the system employs to place minimum and maximum size limitations on a window. This kind of configuration affects both windows and volumes, which are windows with the [`volumetric`](https://developer.apple.com/documentation/SwiftUI/WindowStyle/volumetric) window style.

Your ability to configure window size and position is subject to the following constraints:

- The system might be unable to fulfill your request. For example, if you specify a default size that’s outside the range of the window’s resizability, the system clamps the affected dimension to keep it in range.
- Although you can change the window’s content, you can’t directly manipulate window position or size after the window appears. This ensures that people have full control over their workspace.
- During state restoration, the system restores windows to their previous position and size.

> **Note**: Windows in iPadOS occupy the full screen, or share the screen with another window in Slide Over or Split View. You can’t programmatically affect window geometry on that platform.

##### Specify Initial Window Position

##### Specify Initial Window Size

You can indicate a default initial size for a new window that the system creates from a [`Scene`](https://developer.apple.com/documentation/SwiftUI/Scene) declaration by applying one of the default size scene modifiers, like [`defaultSize(width:height:)`](https://developer.apple.com/documentation/SwiftUI/Scene/defaultSize(width:height:)). For example, you can request that new windows that a [`WindowGroup`](https://developer.apple.com/documentation/SwiftUI/WindowGroup) generates occupy 600 points in the x-dimension and 400 points in the y-dimension.

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .defaultSize(CGSize(width: 600, height: 400))
    }
}
```

The system might clamp the actual size of the window, depending on both the window’s content and resizability settings.

##### Specify Window Resizability

Both macOS and visionOS provide interface controls that enable people to resize windows within certain limits. For example, people can use the control that appears when they look at the corner of a visionOS window to resize a window on that platform.

You can specify how the system limits window resizability. The default resizability for all scenes is [`automatic`](https://developer.apple.com/documentation/SwiftUI/WindowResizability/automatic). With that strategy, [`Settings`](https://developer.apple.com/documentation/SwiftUI/Settings) windows use the [`contentSize`](https://developer.apple.com/documentation/SwiftUI/WindowResizability/contentSize) strategy, where both the minimum and maximum window size match the respective minimum and maximum sizes of the content that the window contains. Other scene types use [`contentMinSize`](https://developer.apple.com/documentation/SwiftUI/WindowResizability/contentMinSize) by default, which retains the minimum size restriction, but doesn’t limit the maximium size.

You can specify one of these resizability strategies explicitly by adding the [`windowResizability(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/windowResizability(_:)) scene modifier to a scene. For example, people can resize windows from the following window group to between 100 and 400 points in both dimensions because the frame modifier imposes those bounds on the content view:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .frame(
                    minWidth: 100, maxWidth: 400,
                    minHeight: 100, maxHeight: 400)
        }
        .windowResizability(.contentSize)
    }
}
```

You can take this even further and enforce a specific size for a window with content that has a fixed size.

##### Specify a Volume Size

When you create a volume, which is a window with the [`volumetric`](https://developer.apple.com/documentation/SwiftUI/WindowStyle/volumetric) style, you can specify the volume’s size using one of the three-dimensional default size modifiers, like [`defaultSize(width:height:depth:in:)`](https://developer.apple.com/documentation/SwiftUI/Scene/defaultSize(width:height:depth:in:)). The following code creates a volume that’s one meter on a side:

```swift
WindowGroup(id: "globe") {
    Globe()
}
.windowStyle(.volumetric)
.defaultSize(width: 1, height: 1, depth: 1, in: .meters)
```

The volume maintains this size for its entire lifetime. People can’t change the size of a volume at runtime.

Although you can specify a volume’s size in points, it’s typically better to use physical units, like the above code, which specifies a size in meters. This is because the system renders a volume with fixed scaling rather than dynamic scaling, unlike a regular window, which means the volume appears more like a physical object than a user interface. For information about the different kinds of scaling, see [`Spatial layout`](https://developer.apple.com/design/Human-Interface-Guidelines/spatial-layout).

## See Also

- [Hello World](world.md)
  Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Presenting windows and spaces](presenting-windows-and-spaces.md)
  Open and close the scenes that make up your app’s interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionOS/positioning-and-sizing-windows)*