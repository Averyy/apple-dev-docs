# Previewing SwiftUI views in Swift Playgrounds

**Framework**: Swift Playgrounds

Use the canvas in Swift Playgrounds to see a live preview of the SwiftUI views in your app.

#### Overview

In Swift Playgrounds, you can see live Previews of your SwiftUI views just like [`Previews in Xcode`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/previews-in-xcode). In an app playground, you have a default App Preview that generates from the structure that conforms to the [`App`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/app) protocol. The canvas on the right hand side updates its title to “App Preview” when the App Preview renders.

![A screenshot of Swift Playgrounds that shows the Date Planner app playground with the DatePlannerApp file open in the editor and its App Preview displayed in the Previews canvas.](https://docs-assets.developer.apple.com/published/f83b2bd38fb10927265d26d3a2df174b/app-previews-in-playgrounds%402x.png)

To see live Previews, use a structure that conforms to the [`PreviewProvider`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/previewprovider) protocol. When you create a SwiftUI view in code, the canvas displays an interactive Preview. The Preview renders live updates when you make changes to its associated file. Making small edits in a file, like changing a property value or string literal changes, causes the Preview to update instantly, while making bigger changes, like adding a new type or changing types, causes the Preview to refresh. When a Preview is available for a specific SwiftUI view, you can see that the canvas displays a page control under the current Previews. This page control allows you to switch between the App Preview and any view previews in the current file. The canvas updates its title to “Preview” when a view preview renders.

![A screenshot of Swift Playgrounds that shows the Date Planner app playground with the EventDetail file open in the editor and its live Preview displayed in the Preview canvas.](https://docs-assets.developer.apple.com/published/2518685513d04f9207158169994a6601/previews-in-playgrounds%402x.png)

You can run your app within Swift Playgrounds. When you tap Run, Swift Playgrounds builds and displays your app so you can see what your app looks like and test its functionality. While running the app, you interact with Playgrounds App window by tapping the Swift icon in the status bar. This opens a menu with the following options:

![A screenshot of Swift Playgrounds that shows pop up of Playground’s App window with its available options while the Date Planner app runs in the App window’s background.](https://docs-assets.developer.apple.com/published/5485679049fc8ed21284597f221a8814/playgrounds-app-window%402x.png)

- Restart – Restarts your app and creates a new instance.
- Stop – Stops the current running instance of your app.
- Show Project – Go back to your app playground files to look at code while your app is running.
- Show Console – See any live print statements that you may have in your code.
- Delete App Data and Restart – Deletes any cached app data and restarts your app.

## See Also

- [Adding a Swift package to your app playground](add-a-swift-package.md)
  Extend the functionality of your app playground by finding and adding a publicly available Swift package.
- [Debugging an App Playground using the Console](console-print-debugging.md)
  Learn different methods to debug your code using console output.
- [Requesting access to capabilities for your app playground](project-capabilities.md)
  Request access for your app to protected resources, services, or device hardware such as sensors.
- [Importing sample content into user app playgrounds](using-content-in-user-projects.md)
  Learn how to bring sample code into your app playground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/live-preview)*