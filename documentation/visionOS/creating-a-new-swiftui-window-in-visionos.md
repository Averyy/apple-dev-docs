# Creating SwiftUI windows in visionOS

**Framework**: Visionos

Display and manage multiple SwiftUI windows in your visionOS app.

**Availability**:
- visionOS 2.0+
- Xcode 16.0+

#### Overview

This sample code project demonstrates how to open a new SwiftUI view and a separate window group to manage multiple windows, assigning a unique `id` to each newly created window. In the sample, the app displays a SwiftUI window with a [`Button`](https://developer.apple.com/documentation/SwiftUI/Button) that a person can tap to open a new window view, as the following image illustrates:

![A screenshot of a visionOS app in Simulator displaying one center window, with a button labeled 'Open a new window', and two smaller translucent windows on either side labeled 'New window number 0' and 'New window number 1'.](https://docs-assets.developer.apple.com/published/c598c2c0c671cf1a943975fee28877ba/sample-new-window-1-main-view.png)

##### Create a Variable to Track Window Ids

To manage multiple windows for an app, the app uses the [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) protocol to establish an ID value for each new window view.

```swift
import SwiftUI

struct NewWindowID: Identifiable {
    /// The unique identifier for the window.
    var id: Int
}

```

##### Add a Button for Creating Windows

The `OpenNewWindow` view creates and displays a SwiftUI button. When a person taps the button, a new SwiftUI window appears.

```swift
import SwiftUI

struct OpenWindowView: View {
    /// The `id` value that the main view uses to identify the SwiftUI window.
    @State var nextWindowID = NewWindowID(id: 1)

    /// The environment value for getting an `OpenWindowAction` instance.
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        // Create a button in the center of the window that
        // launches a new SwiftUI window.
        Button("Open a new window") {
            // Open a new window with the assigned ID.
            openWindow(value: nextWindowID.id)

            // Increment the `id` value of the `nextWindowID` by 1.
            nextWindowID.id += 1
        }
    }
}
```

The [`openWindow`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/openWindow) instance property invokes a new window view in an app’s environment.

##### Create a View for the New Window

The `NewWindow` view displays the window’s `id` value in a [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) instance.

```swift
import SwiftUI

struct NewWindow: View {
    /// Acts as the main identifier for the new view.
    let id: Int
    
    var body: some View {
        // Create a text view that displays
        // the window's `id` value.
        Text("New window number \(id)")
    }
}
```

##### Add New Windows to a Window Group

The `EntryPoint` provides a specific [`WindowGroup`](https://developer.apple.com/documentation/SwiftUI/WindowGroup) to create a window view and add the new window to the app’s main view.

```swift
import SwiftUI

@main
struct EntryPoint: App {
    var body: some Scene {
        WindowGroup {
            MainView()
        }
        
        /// A `WindowGroup` for each newly created window in the app's main view.
        WindowGroup("New Window", for: NewWindowID.ID.self) { $id in
            NewWindow(id: id ?? 1)
        }
    }
}
```

###### Related Samples


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/creating-a-new-swiftui-window-in-visionos)*