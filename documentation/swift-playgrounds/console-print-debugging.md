# Debugging an App Playground using the Console

**Framework**: Swift Playgrounds

Learn different methods to debug your code using console output.

#### Overview

When writing code in Swift Playgrounds, you can debug your playgrounds by using print statements and viewing their output in the console. You can filter statements in the console to find specific outputs.

#### Add a Print Statement

Call `print(_:separator:terminator)` in the code you’d like to debug and add any items you’d like to output to the console. These items output as `String` values, the same as the output obtained by calling `String(item)`. To customize your debug output for any type, you can add [`CustomDebugStringConvertible`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/customdebugstringconvertible) conformance to provide your own implementation for `debugDescription`. This allows you to print custom `String` representations for any type and view them in the console.

If you’re trying to debug a SwiftUI view, you need to adjust your approach. Because SwiftUI is a [`declarative framework`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/state-and-data-flow), you can’t add an imperative `print` call inside your view declaration. This is because the view `body` property expects to return a [`View`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view) value. To resolve this, you can use one of several approaches.

One approaach to debug your declarative code is to attach the `onAppear(perform:)` modifier to a view in your `body`, and call `print` when the view first appears:

```None
Image(systemName: "globe")
    .onAppear {
        print("This is the debug output.")
    }
```

You could also add an extension on `View` that returns itself and calls the `print` method:

```None
extension View {
    func printOutput(_ value: Any) -> Self {
        print(value)
        return self
    }
}
```

You can then use `printOutput` as a view modifier to print debug information to the console when the view is built:

```None
VStack {
   ForEach(colors, id: \.self) { color in
      Circle()
         .foregroundColor(color)
         .printOutput(color)
   }
}
```

#### Understand When and Why Your Views Change

Another approach that’s particularly useful when debugging SwiftUI view updates is to call the internal method `Self._printChanges()` from the `body` of the view — instead of calling `print`. This records which property caused the view to update and sends that information to the console. In addition to providing property names, `@self` marks the change to the view value, and `@identity` marks the change to the view’s identity.

```None
var body: some View {
    let _ = Self._printChanges()
    // View code 
}
```

#### See Your Apps Output in the Console

Press the console button in the code editor to show and hide the console. To adjust the size of the console, you can drag to increase or decrease the available space.

![The Swift Playgrounds code editor displaying console output](https://docs-assets.developer.apple.com/published/6c0ce410a209737123227e53771c814a/console%402x.png)

To filter results, tap the filter button and enter a phrase you’d like to filter on. The remaining results filter based upon this input.

You can tap to select a result, which allows you to select it as text or to clear the console output by deleting the text.

## See Also

- [Adding a Swift package to your app playground](add-a-swift-package.md)
  Extend the functionality of your app playground by finding and adding a publicly available Swift package.
- [Previewing SwiftUI views in Swift Playgrounds](live-preview.md)
  Use the canvas in Swift Playgrounds to see a live preview of the SwiftUI views in your app.
- [Requesting access to capabilities for your app playground](project-capabilities.md)
  Request access for your app to protected resources, services, or device hardware such as sensors.
- [Importing sample content into user app playgrounds](using-content-in-user-projects.md)
  Learn how to bring sample code into your app playground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/console-print-debugging)*