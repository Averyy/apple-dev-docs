# Configuring the Xcode project window

**Framework**: Xcode

Configure the appearance of Xcode project windows by showing and hiding editors, inspectors, and navigation content.

#### Overview

The Xcode  is your primary interface for viewing, editing, and managing all parts of your project. You can configure it to fit your work style and adjust it as you work on different tasks.

The main window opens when you create or open a project. To open additional main windows, choose File > New > Window.

![A screenshot of the Xcode project window and its different panels.](https://docs-assets.developer.apple.com/published/4080348ba7beac8e9815966051eb858f/xcode-project-window%402x.png)

The areas of the main window are:

- The  for building and running your app, viewing the progress of tasks, and configuring the main window. Use the tabs at the top to organize your open files. You can reorder tabs, close them individually, or drag them out of the tab bar to create new windows.
- The  for viewing and editing the contents of your project, including code, user interface files, property lists, project settings, and more.
- The  for viewing the parts of your project, including files, symbols, breakpoints, and build information.
- The  for controlling the app execution during debugging, and for displaying variables, register, and status information.
- The  for viewing and editing information about the project or about the selected object in the navigator or editor area.

##### Configure the Available Editors

Files you select in the Project navigator open in the editor area. The editor that appears depends on the type of file you select. For example, if you select a source file, Xcode displays the source editor.

![A figure that shows the controls for navigating and modifying the editor window.](https://docs-assets.developer.apple.com/published/08ef370e113abfbacd96a7fb4c55c758/editor-windows%402x.png)

To add, remove, and configure editors, use the controls in the jump bar and tab bar, located at the top of the editor area. To change the information you display in the editor area, click the Adjust Editor Options button in the tab bar, and select one of the following:

- The  displays a preview of your SwiftUI interface. Use the  menu to configure the canvas’s position.
- The  editor displays information about what you’re editing. For example, the assistant editor for a SwiftUI view displays the canvas view, and the assistant for an Objective-C source file displays the matching header.
- The  view provides a miniaturized version of your source files content, which you use to navigate around the file.
- The  view displays the commit history of a file under source control management.
- The  view displays statistics about your source code after you run tests. Use it to detect portions of your code not reached by your project’s tests.

When showing multiple editors, click the Enable Code Review button in the tab bar to temporarily expand the current editor to fill the editor area. Click it again to collapse the editor to its original size.

##### Show and Hide Areas of the Main Window

Show and hide different parts of the main window to make more space in the editor area. The window has separate controls to hide the navigator area, inspector area, and debug area.

![A figure that shows the controls for showing and hiding the navigator and inspector panes.](https://docs-assets.developer.apple.com/published/f52b7b3addf332b38a966a8a7c98050e/main-window-show-hide%402x.png)

## See Also

- [Finding and replacing content in a project](finding-and-replacing-content-in-a-project.md)
  Search some or all of your project for text strings or symbol names, and perform advanced searches using regular expressions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-the-xcode-project-window)*