# Previewing your app’s interface in Xcode

**Framework**: Xcode

Iterate designs quickly and preview your apps’ displays across different Apple devices.

#### Overview

With Xcode previews, you can make changes to your app’s views in code, and see the result of those changes quickly in the preview canvas. Add previews to your SwiftUI, UIKit, and AppKit views using the preview macro. Then configure how you want your previews to display using Xcode’s preview canvas, or programmatically in code.

##### Add a Preview to Your View Using the Preview Macro

When you create a view in Xcode, you can display it in the preview canvas. The preview canvas shows how your view appears on different devices in a variety of configurations.

![A screenshot of Xcode with the project navigator on the left, the code editor in the middle, and the preview canvas on the right. A callout in the code area in the middle points to the preview macro. A callout at the bottom on the right points to the preview canvas area.](https://docs-assets.developer.apple.com/published/d6c2a3bbe5212fe617b52eb138290fec/dynamically-previewing-1-preview-macro%402x.png)

The Swift preview macro is a snippet of code that makes and configures your view. You use one of the preview macros — such as [`Preview(_:body:)`](https://developer.apple.com/documentation/SwiftUI/Preview(_:body:)) — to tell Xcode what to display. To manually show or hide the preview canvas, select Editor > Canvas from the Xcode menu.

To add a preview macro to your view:

1. Open the source file of the view you want to display.
2. Add the `#Preview` macro to the view.
3. Create and return an instance of the view configuration you want to display in the body of the trailing closure of the macro.

##### Interact with Your View in Live Mode

When you select the live or interactive preview option, your view appears and interacts just like it would on a device or simulator. Use this mode of preview to test control logic, animations, and text entry as well as responses to asynchronous code. When you select this mode, a single device preview appears in the canvas. This is the default mode for new previews you display.

##### Try Out New Designs Quickly with Select Mode

In select mode, the preview displays a snapshot of your view so you can interact with your view’s UI elements in the canvas. Selecting a control in the preview highlights the corresponding line of code in the source editor. Double-clicking certain text views, such as [`Label`](https://developer.apple.com/documentation/SwiftUI/Label), moves focus to the source editor so you can make changes quickly.

![A screenshot of Xcode with the code editor in the middle, and a preview on the right. The select mode button at the bottom of the preview canvas is active. The preview canvas displays a preview of the view in the select mode.](https://docs-assets.developer.apple.com/published/bf5e199e91846e224d9f08586d70d2b9/dynamically-previewing-3-select-mode%402x.png)

##### Control How Your Previews Display with Device Settings

Use Device settings to control how a preview displays for a specific device. For example, to see how your view looks in Dark Mode, in a landscape right orientation, with extra large text:

1. Select the Device settings option at the bottom of the preview canvas.
2. Click the Color Scheme toggle to on, and select the Dark Appearance option under Color Scheme.
3. Click the Orientation toggle to on, and select the Landscape Right option under the Orientation header.
4. Click the Dynamic Type toggle to on, and drag the Dynamic Type slider to the X Large text setting.

![A screenshot of the Xcode preview canvas. The Device settings mode button at the bottom of the preview canvas is active. The preview canvas displays a preview of the view in Dark Mode, in a landscape right orientation, with extra large text on an iPad.](https://docs-assets.developer.apple.com/published/18378e0001627e196d19f14adf33317f/dynamically-previewing-6-device-settings%402x.png)

##### Test Different View Configurations

Use variant mode to see how your view appears in different variations for a given configuration. For example, to test how well your view supports accessibility, select Variant mode from the bottom of the preview canvas, and select the Dynamic Type Variants option. Xcode displays your view with different sizes of text.

![A screenshot of the Xcode preview canvas. The variant mode button at the bottom of the preview canvas is active. The preview canvas displays a preview of the view for each variant of dynamic size. Six previews are visible each displaying the view with a different size of text.](https://docs-assets.developer.apple.com/published/24fcbb9c9cc40e677bd29acde42ce9e9/dynamically-previewing-4-variant-mode%402x.png)

Preview canvas supports the following variations:

> **Note**: Because variant mode shows all the values for a given device setting, you can override what variant mode displays by making further changes in Device settings. For example, to see how your view appears in different sizes of text in Dark Mode, select the Dynamic Type Variants option from Variant mode, and then enable the Dark Mode color scheme in Device settings.

Because variant mode shows all the values for a given device setting, you can override what variant mode displays by making further changes in Device settings. For example, to see how your view appears in different sizes of text in Dark Mode, select the Dynamic Type Variants option from Variant mode, and then enable the Dark Mode color scheme in Device settings.

##### Preview on a Specific Device

To see how your view displays on a specific device, select the Preview destination picker option, and then select the device you want your preview to display. When you do, Xcode displays a preview of your view on that device.

![A screenshot of the Xcode preview canvas. The preview destination mode button at the bottom of the preview canvas is active, set to iPad. The preview canvas displays a preview of the view on an iPad.](https://docs-assets.developer.apple.com/published/d4010f14c748099f82bbb9d7ea74aecd/dynamically-previewing-5-preview-destination%402x.png)

##### Capture Specific Previews in Code

In addition to the preview options Xcode provides, you can also customize and configure previews you want to reuse programmatically in code.

For example, you can add a name to more easily track what each preview displays. When you pass the name of your preview as a string into the preview macro, the name appears in the title of the preview in the preview canvas.

```swift
// A preview with an assigned name.
#Preview("2x2 Grid Portrait") {
   Content()
}
```

You can also control how your preview displays by passing one or more configuration traits as a variadic argument list into the preview macro. For example, to display your view in the landscape left orientation, pass the [`landscapeLeft`](https://developer.apple.com/documentation/DeveloperToolsSupport/PreviewTrait/landscapeLeft) type property into the  [`init(_:traits:body:)`](https://developer.apple.com/documentation/DeveloperToolsSupport/Preview/init(_:traits:body:)-8pemr) preview initializer to tell Xcode which orientation to display.

##### Use Inline Dynamic Properties with Previewable

When a view depends on a [`Binding`](https://developer.apple.com/documentation/SwiftUI/Binding) property wrapper, you can create a functional binding for that property and pass it into your preview using the [`Previewable()`](https://developer.apple.com/documentation/SwiftUI/Previewable()) macro. This macro works on any variable conforming to the [`DynamicProperty`](https://developer.apple.com/documentation/SwiftUI/DynamicProperty) protocol.

```swift
struct PlayButton: View {
    @Binding var isPlaying: Bool

    var body: some View {
        Button(action: {
            self.isPlaying.toggle()
        }) {
            Image(systemName: isPlaying ? "pause.circle" : "play.circle")
            .resizable()
            .scaledToFit()
            .frame(maxWidth: 80)
        }
    }
}

#Preview {
    // Tag the dynamic property with `Previewable`.
    @Previewable @State var isPlaying = true

    // Pass it into your view.
    PlayButton(isPlaying: $isPlaying)
}
```

Tagging a dynamic property with the `Previewable` macro gets rid of the need to create wrapper views in previews.

> **Note**: [`Previewable()`](https://developer.apple.com/documentation/SwiftUI/Previewable()) is a SwiftUI only macro and doesn’t apply to UIKit or AppKit previews.

[`Previewable()`](https://developer.apple.com/documentation/SwiftUI/Previewable()) is a SwiftUI only macro and doesn’t apply to UIKit or AppKit previews.

##### Make Complex Objects Reusable with a Preview Modifier

To avoid recreating expensive objects for every preview that needs them, in SwiftUI you can create these objects once with the [`PreviewModifier`](https://developer.apple.com/documentation/SwiftUI/PreviewModifier) and then pass the preview modifier into your preview using the [`Preview(_:traits:_:body:)`](https://developer.apple.com/documentation/SwiftUI/Preview(_:traits:_:body:)) macro.

Expensive objects — such as objects that make network calls, perform disk access, or just take considerable time and effort to setup — can make your previews take longer to load. By creating these expensive objects once, and sharing them across all your previews, you make your previews more efficient.

For example, if you have an app with an expensive [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) object:

```swift
@Observable
class AppState {
    // An expensive, complex, bulky object.
    var expensiveObject = "Some expensive object"
}

@main
struct MyApp: App {
    @State private var appState = AppState()

    var body: some Scene {
        WindowGroup {
            ComplexView()
                .environment(appState)
        }
    }
}
```

You reuse that expensive object across multiple views in your app:

```swift
struct ComplexView: View {
    @Environment(AppState.self) var appState

    var body: some View {
        Text("\(appState.expensiveObject)")
    }
}
```

For every view you want to preview, you recreate and pass in that expensive object:

```swift
#Preview {
    ComplexView()
        // Potentially expensive if `AppState` is large or complex.
        .environment(AppState())
}
```

Instead, define the expensive object once and share it across multiple previews using the [`PreviewModifier`](https://developer.apple.com/documentation/SwiftUI/PreviewModifier) protocol.

1. Define a structure conforming to the `PreviewModifier` protocol.
2. Implement the static [`makeSharedContext()`](https://developer.apple.com/documentation/SwiftUI/PreviewModifier/makeSharedContext()-4zi8r) function returning the object with the expensive state.
3. Inject that shared context into the view you want to preview using the [`body(content:context:)`](https://developer.apple.com/documentation/SwiftUI/PreviewModifier/body(content:context:)) function.
4. Add the modifier to the preview using the [`Preview(_:traits:_:body:)`](https://developer.apple.com/documentation/SwiftUI/Preview(_:traits:_:body:)) macro.

```swift
// Create a struct conforming to the PreviewModifier protocol.
struct SampleData: PreviewModifier {

    // Define the object to share and return it as a shared context.
    static func makeSharedContext() async throws -> AppState {
        let appState = AppState()
        appState.expensiveObject = "An expensive object to reuse in previews"
        return appState
    }

    func body(content: Content, context: AppState) -> some View {
        // Inject the object into the view to preview.
        content
            .environment(context)
    }
}

// Add the modifier to the preview.
#Preview(traits: .modifier(SampleData())) {
    ComplexView()
}
```

##### Pass Views Only the Data They Need

When creating views, pass in only the data the view needs to display. Avoid passing in objects that fetch data; objects make setting up a view’s preview more complicated and less performant.

Instead, create views with the minimal amount of data they need, favoring simpler, immutable data types. Creating views this way makes testing and previewing your views easier and helps them perform better.

The following example shows how simple data types, like `String` and `enum`, can be used to preview a view in various ways using the preview macro.

![A screenshot of the preview canvas displaying six previews of a data row view in various test scenario configurations. The preview canvas displays view variations for online offline status, with and without an avatar image, and long and short display names.](https://docs-assets.developer.apple.com/published/56f22860fb71dc79905ddbd2df95e955/dynamically-previewing-7-minimal-data%402x.png)

##### Reduce Your App Size with Development Assets

To access resources in your previews, without shipping them in the final version of your app, use development assets. Development assets give you access to resources such as images, video, JSON data, and code files in your previews and Simulator, without increasing the overall size of your app.

Add items to the Development Assets of a project target as follows:

1. Select the project folder in the Project navigator.
2. Select the target you want to add the development assets to.
3. In the General tab, scroll down to Development Assets.
4. In the lower-left corner, click the Add items button (+).
5. In the dialog that appears, select the items that you want to add and click Add.

## See Also

- [Creating an Xcode project for an app](creating-an-xcode-project-for-an-app.md)
  Start developing your app by creating an Xcode project from a template.
- [Creating your app’s interface with SwiftUI](creating-your-app-s-interface-with-swiftui.md)
  Develop apps in SwiftUI with an interactive preview that keeps the code and layout in sync.
- [Building and running an app](building-and-running-an-app.md)
  Compile your source files and assemble an app bundle to run on a device or simulator.
- [Xcode updates](../Updates/Xcode.md)
  Learn about important changes to Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/previewing-your-apps-interface-in-xcode)*