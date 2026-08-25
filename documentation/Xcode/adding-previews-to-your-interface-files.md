# Adding previews to your interface files

**Framework**: Xcode

Write code to test your views on different devices and configurations without needing to run your app.

#### Overview

Show previews of your views in the canvas by adding preview macros to your SwiftUI, UIKit, and AppKit files. The Swift preview macro is a snippet of code that displays and configures your view.

![A screenshot of Xcode with the Project navigator on the left with an interface file selected, the code editor in the middle with a preview macro highlighted, and the canvas on the right showing the view in landscape orientation and with the device settings popover.](/images/com.apple.Xcode/adding-previews@2x.png)

You can change environment and device settings in the code or using controls in the canvas. To show the canvas next to the source editor, click Show Canvas in the upper-right corner of the toolbar. You can also give previews sample data to display that’s separate from your app.

For more information on using the canvas, see [`Interacting with previews in the canvas`](interacting-with-previews-in-the-canvas.md). To generate previews using coding intelligence instead, see [`Generate playgrounds and previews`](using-coding-intelligence-in-the-source-editor#Generate-playgrounds-and-previews.md).

#### Add a Preview Macro

Add one of the `#Preview` macros to an interface file — such as [`Preview(_:body:)`](https://developer.apple.com/documentation/swiftui/preview(_:body:)) — to tell Xcode what to display in the canvas. In the body of the macro trailing closure, add code that creates and returns an instance of the view configuration you want to display.

For SwiftUI, you configure a view in a preview macro. For UIKit and AppKit, you can configure either a view or view controller in a preview macro.

**SwiftUI**:

```swift
struct ContentView: View {
    var body: some View {
        // ...
    }
}

// A SwiftUI preview.
#Preview {
    ContentView()
}
```

**UIKit**:

```swift
class WeatherViewController: UIViewController {
    // ...
}

// A UIKit UIViewController preview.
#Preview {
    let viewController = WeatherViewController()
    viewController.title = "Current Weather"
    return viewController
}

class WeatherView: UIView {
    var icon: UIImage?
}

// A UIKit UIView preview.
#Preview {
    let view = WeatherView()
    if let image = UIImage(systemName: "sun.max.fill") {
        view.icon = image
    }
    return view
}
```

**AppKit**:

```swift
class WeatherViewController: NSViewController {
    // ...
}

// An AppKit NSViewController preview.
#Preview {
    let viewController = WeatherViewController()
    viewController.title = "Current Weather"
    return viewController
}

class WeatherView: NSView {
    var icon: NSImage?
}

// An AppKit NSView preview.
#Preview {
    let view = WeatherView()
    view.icon = NSImage(symbolName: "sun.max.fill", variableValue: 0.0)
    return view
}
```

#### Capture Specific Previews in Code

In addition to the preview options Xcode provides, you can also customize and configure previews you want to reuse programmatically.

For example, you can add a name to more easily track what each preview displays. Xcode also uses the name that you pass to the macro as the label for that preview in the tab bar of the canvas.

```swift
// A preview with an assigned name.
#Preview("2x2 Grid Portrait") {
   Content()
}
```

Display a variant of the view by passing one or more configuration traits as a variadic argument list into the preview macro. For example, to display your view in the landscape left orientation, pass the [`landscapeLeft`](https://developer.apple.com/documentation/developertoolssupport/previewtrait/landscapeleft) type property into the  [`init(_:traits:body:)`](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:traits:body:)-8pemr) preview initializer to tell Xcode which orientation to display.

**SwiftUI**:

```swift
// A SwiftUI preview with name and orientation.
#Preview("2x2 grid", traits: .landscapeLeft) {
    CollageView(layout: .twoByTwoGrid)
}
```

**UIKit**:

```swift
// A UIKit preview with name and orientation.
#Preview("Camera setting sunning day", traits: .landscapeLeft) {
    let viewController = CameraViewController()
    if let image = UIImage(systemName: "sun.max.fill") {
        viewController.lastImage = image
    }
    return viewController
}
```

**AppKit**:

```swift
// An AppKit preview with name and orientation.
#Preview("Camera setting sunning day", traits: .landscapeLeft) {
    let viewController = CameraViewController()
    viewController.lastImage = NSImage(symbolName: "sun.max.fill", variableValue: 0.0)
    return viewController
}
```

#### Tag Dynamic Properties for Use in Previews

When a view depends on a [`Binding`](https://developer.apple.com/documentation/swiftui/binding) property wrapper, you can create a functional binding for that property and pass it into your preview using the [`Previewable()`](https://developer.apple.com/documentation/swiftui/previewable()) macro. This macro works on any variable conforming to the [`DynamicProperty`](https://developer.apple.com/documentation/swiftui/dynamicproperty) protocol.

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

Tagging a dynamic property with the `Previewable` macro eliminates the need to create wrapper views in previews.

> **Note**: [`Previewable()`](https://developer.apple.com/documentation/swiftui/previewable()) is a SwiftUI-only macro and doesn’t apply to UIKit or AppKit previews.

#### Make Complex Objects Reusable with a Preview Modifier

To avoid recreating expensive objects for every preview that needs them, in SwiftUI you can create these objects once with the [`PreviewModifier`](https://developer.apple.com/documentation/swiftui/previewmodifier) and then pass the preview modifier into your preview using the [`Preview(_:traits:_:body:)`](https://developer.apple.com/documentation/swiftui/preview(_:traits:_:body:)) macro.

Expensive objects — such as objects that make network calls, perform disk access, or just take considerable time and effort to set up — can make your previews take longer to load. By creating these expensive objects once, and sharing them across all your previews, you make your previews more efficient.

For example, if you have an app with an expensive [`Observable()`](https://developer.apple.com/documentation/observation/observable()) object:

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

Instead, define the expensive object once and share it across multiple previews using the [`PreviewModifier`](https://developer.apple.com/documentation/swiftui/previewmodifier) protocol.

1. Define a structure conforming to the `PreviewModifier` protocol.
2. Implement the static [`makeSharedContext()`](https://developer.apple.com/documentation/swiftui/previewmodifier/makesharedcontext()-4zi8r) function returning the object with the expensive state.
3. Inject that shared context into the view you want to preview using the [`body(content:context:)`](https://developer.apple.com/documentation/swiftui/previewmodifier/body(content:context:)) function.
4. Add the modifier to the preview using the [`Preview(_:traits:_:body:)`](https://developer.apple.com/documentation/swiftui/preview(_:traits:_:body:)) macro.

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

#### Pass Views Only the Data They Need

When creating views, pass in only the data the view needs to display. Avoid passing in objects that fetch data; objects make setting up a view’s preview more complicated and less performant.

Instead, create views with the minimal amount of data they need, favoring simpler, immutable data types. Creating views this way makes testing and previewing your views easier and helps them perform better.

The following example shows how you can use simple data types, like `String` and `enum`, to preview a view in various ways using the preview macro.

**SwiftUI**:

```swift
struct CollaboratorCell: View {
    // Construct your view with only the data it needs.
    let name: String
    let image: Image?
    let connectionStatus: ConnectionStatus
    
    enum ConnectionStatus {
        case online
        case offline
    }

    // ...
}

#Preview("Supported cell combinations", traits: .sizeThatFitsLayout) {
    let image = Image(systemName: "person.circle")
    VStack {
        // Then test each scenario in your preview macro.
        CollaboratorCell(name: "Ravi Patel", image: nil, connectionStatus: .offline)
        CollaboratorCell(name: "Anne Johnson", image: image, connectionStatus: .offline)
        CollaboratorCell(name: "Tom Clark", image: nil, connectionStatus: .online)
        CollaboratorCell(name: "Mei Chen", image: image, connectionStatus: .online)
        CollaboratorCell(name: "Bill Long Middle James", image: nil, connectionStatus: .offline)
        CollaboratorCell(name: "Maria Long Middle Ruiz", image: image, connectionStatus: .online)
    }
}
```

**UIKit**:

```swift
class CollaboratorCell: UIView {
    // Construct your view with only the data it needs.
    let name: String
    let image: UIImage?
    let connectionStatus: ConnectionStatus
    
    enum ConnectionStatus {
        case online
        case offline
    }
    
    // ...
}

#Preview("Supported cell combinations", traits: .sizeThatFitsLayout) {
    let image = UIImage(systemName: "person.circle")
    
    // Then test each scenario in your preview macro.
    let cell1 = CollaboratorCell(name: "Tom Clark", image: nil, connectionStatus: .offline)
    let cell2 = CollaboratorCell(name: "Tom Clark", image: image, connectionStatus: .offline)
    let cell3 = CollaboratorCell(name: "Tom Clark", image: nil, connectionStatus: .online)
    let cell4 = CollaboratorCell(name: "Tom Clark", image: image, connectionStatus: .online)
    let cell5 = CollaboratorCell(name: "Tom Long Middle Clark", image: nil, connectionStatus: .offline)
    let cell6 = CollaboratorCell(name: "Tom Long Middle Clark", image: image, connectionStatus: .online)
    
    // Create a test harness to display.
    let stackView = UIStackView()
    stackView.axis = .vertical
    stackView.spacing = 8.0

    stackView.addArrangedSubview(cell1)
    stackView.addArrangedSubview(cell2)
    stackView.addArrangedSubview(cell3)
    stackView.addArrangedSubview(cell4)
    stackView.addArrangedSubview(cell5)
    stackView.addArrangedSubview(cell6)

    return stackView
}
```

**AppKit**:

```swift
class CollaboratorCell: NSView {
    // Construct your view with only the data it needs.
    let name: String
    let image: NSImage?
    let connectionStatus: ConnectionStatus

    enum ConnectionStatus {
        case online
        case offline
    }

    // ...
}

#Preview("Supported cell combinations", traits: .sizeThatFitsLayout) {
    let image = NSImage(systemSymbolName: "person.circle", accessibilityDescription: "A person symbol inside the outline of a circle.")

    // Then test each scenario in your preview macro.
    let cell1 = CollaboratorCell(name: "Tom Clark", image: nil, connectionStatus: .offline)
    let cell2 = CollaboratorCell(name: "Tom Clark", image: image, connectionStatus: .offline)
    let cell3 = CollaboratorCell(name: "Tom Clark", image: nil, connectionStatus: .online)
    let cell4 = CollaboratorCell(name: "Tom Clark", image: image, connectionStatus: .online)
    let cell5 = CollaboratorCell(name: "Tom Long Middle Clark", image: nil, connectionStatus: .offline)
    let cell6 = CollaboratorCell(name: "Tom Long Middle Clark", image: image, connectionStatus: .online)

    // Create a test harness to display.
    let stackView = NSStackView()
    stackView.orientation = .vertical
    stackView.spacing = 8.0

    stackView.addArrangedSubview(cell1)
    stackView.addArrangedSubview(cell2)
    stackView.addArrangedSubview(cell3)
    stackView.addArrangedSubview(cell4)
    stackView.addArrangedSubview(cell5)
    stackView.addArrangedSubview(cell6)

    return stackView
}
```

#### Reduce Your App Size with Development Assets

To access resources in your previews, without shipping them in the final version of your app, use development assets in your Xcode project. Development assets give you access to resources such as images, video, JSON data, and code files in your previews, without increasing the size of your app.

Add items to the Development Assets of a target in Xcode as follows:

1. In the Project navigator, select the project.
2. In the project editor on the right, select the target.
3. In the General tab, scroll down to Development Assets.
4. In the lower-left corner, click the Add items button (+).
5. In the dialog that appears, select the items that you want to add and click Add.

## See Also

- [Creating an Xcode project for an app](creating-an-xcode-project-for-an-app.md)
  Set up a new project to start developing your app.
- [Interacting with previews in the canvas](interacting-with-previews-in-the-canvas.md)
  Use the canvas controls to test your view’s appearance and behavior on different devices and configurations.
- [Running your app on simulated or physical devices](running-your-app-on-simulated-or-physical-devices.md)
  Launch your app on a simulated iOS, iPadOS, tvOS, visionOS, or watchOS device, or on a physical device paired with your Mac.
- [Xcode updates](../updates/xcode.md)
  Learn about important changes to Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/adding-previews-to-your-interface-files)*