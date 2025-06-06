# Creating your app’s interface with SwiftUI

**Framework**: Xcode

Develop apps in SwiftUI with an interactive preview that keeps the code and layout in sync.

#### Overview

If you choose the SwiftUI framework to develop your app, you can see an interactive preview as you lay out your user interface. Xcode keeps the changes you make to the source code, the user interface layout, and the inspector in sync. For example, when you edit attributes in the inspector, Xcode adds the corresponding code to the source file.

##### Display the Swiftui Preview

To show the preview, select a file that uses SwiftUI in the project navigator, and choose Editor > Canvas. Then click the Resume button in the upper-right corner of the canvas to start the preview. Xcode builds and runs the code, displaying the results directly in the canvas.

![Screenshot showing a SwiftUI file selected in the project navigator and preview displayed in the editor area.](https://docs-assets.developer.apple.com/published/a311c2ad23768cbb9cf5bc4056725ba4/creating-your-app-s-interface-with-swiftui-1%402x.png)

Use the controls at the bottom of the preview to run the app on a simulated device in the canvas, with or without a debug session, or run the app on a connected device.

##### Add Views and Modifiers

To add views and modifiers to your app, click the Library button (+) in the toolbar to open the library, then drag user interface elements from the library to either the canvas or source code. Regardless of where you drop the elements, Xcode keeps the source code and the layout in sync.

![Screenshot showing the library when a SwiftUI element is selected.](https://docs-assets.developer.apple.com/published/01fa3adce78feb9482de961b08675184/creating-your-app-s-interface-with-swiftui-2%402x.png)

##### Edit User Interface Elements

Edit element attributes using either the Action menu or the inspector, or by entering code in the source editor. Command-click the element in the canvas or the structure in the code, choose Show SwiftUI Inspector from the Action menu, then change the attributes in the next pane. Alternatively, choose View > Inspectors > Show Attributes Inspector, and change the attributes in the Attributes inspector that appears on the right.

![Screenshot showing the Action menu in the canvas with the Show Attributes Inspector menu item selected.](https://docs-assets.developer.apple.com/published/a1a83f62dbc1ce7d1bfd93509df4963d/creating-your-app-s-interface-with-swiftui-3%402x.png)

##### Embed User Interface Elements

Additionally, you can modify the user interface by embedding elements in other structures. Command-click an element in the source code or in the canvas, then choose an “Embed in [Generic Structure]” action from the pop-up menu. For example, choose “Embed in HStack” to embed an element that arranges a view’s children in a horizontal line.

![Screenshot showing the Action menu in the source editor with the Embed in HStack menu item selected.](https://docs-assets.developer.apple.com/published/940b4aaf4747f3eb1b6a22e50615b155/creating-your-app-s-interface-with-swiftui-4%402x.png)

To learn more about SwiftUI, go to [`Introducing SwiftUI`](https://developer.apple.com/tutorials/SwiftUI).

## See Also

- [Creating an Xcode project for an app](creating-an-xcode-project-for-an-app.md)
  Start developing your app by creating an Xcode project from a template.
- [Previewing your app’s interface in Xcode](previewing-your-apps-interface-in-xcode.md)
  Iterate designs quickly and preview your apps’ displays across different Apple devices.
- [Building and running an app](building-and-running-an-app.md)
  Compile your source files and assemble an app bundle to run on a device or simulator.
- [Xcode updates](../Updates/Xcode.md)
  Learn about important changes to Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-your-app-s-interface-with-swiftui)*