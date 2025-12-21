# Configuring the Xcode project window

**Framework**: Xcode

Customize the Xcode project window and editor area to view and edit project files in a configuration you prefer.

#### Overview

The Xcode  is your primary interface for viewing, editing, and managing all parts of your project. You can configure it to fit your work style and adjust it as you work on different tasks. It’s especially helpful to configure the editor area, where you spend most of your time modifying files. Then use features, like the jump bar, minimap, and tab bar, to navigate quickly around your project files.

The main window opens when you create or open a project. To open additional main windows, choose File > New > Window.

![An Xcode screenshot of the project editor showing the location of the main window areas: the toolbar at the top, navigator area on the far left, editor area in the middle, and inspector area on the far right. In the editor area, the source editor is on the left, the canvas is on the right, and the debugger is below.](https://docs-assets.developer.apple.com/published/d950a7772e9d4bfbe652ccb68b3ddc58/xcode-window-areas%402x.png)

The areas of the main window:

- The  — for building and running your app, viewing the progress of tasks, and configuring the main window — appears at the top of the window.
- The  — for viewing and editing the contents of your project, including code, user interface files, property lists, project settings, and more — appears in the middle of the window.
- The  — for viewing the parts of your project, including files, symbols, breakpoints, and build information — appears on the right of the editor area.
- The  — for controlling the app runtime during debugging, and for displaying variables, register, and status information — appears below an editor pane.
- The  — for viewing and editing information about the project, or about the selected object in the navigator or editor area — appears on the right of the editor area.

To create an Xcode project, see [`Creating an Xcode project for an app`](creating-an-xcode-project-for-an-app.md).

> **Note**: You can perform most commands described in this document using corresponding menus in the Xcode menu bar. Refer to the menu items for keyboard shortcuts.

##### Show and Hide Areas of the Main Window

Configure the areas of the main window to focus on your specific task. To show or hide the navigator, inspector, and debug areas:

- Click the Navigators button on the far left of the toolbar.
- Click the Inspectors button on the far right of the toolbar.
- Click the Debug Area button on the right of the debugger toolbar.

To switch the navigator, click a navigator in the control above the navigator area.

For information about the coding assistant, which appears in the navigator area when you click the Coding Assistant button, see [`Writing code with intelligence in Xcode`](writing-code-with-intelligence-in-xcode.md).

##### Navigate the Project Files

You browse the hierarchy of your project files using the Project navigator. Files that you select in the Project navigator open in the editor area. The editor that appears depends on the type of file that you select. For example, if you select a source file, Xcode opens it in the source editor.

Then you can use the related menu, arrows, and jump bar that appear in the toolbar above the editor to view or open other files in the editor area.

##### Add Multiple Editor Panes to the Editor Area

Use the controls on the editor toolbar to open multiple files in separate editor panes.

- To add an editor pane, click the Add button (+) on the far right of the editor toolbar and choose either Editor Pane on Right or Editor Pane Below from the pop-up menu.
- To close an editor pane, click the X button on the left of the editor toolbar above the pane.
- To change the focus of the Project navigator and inspector to an editor pane, click it.
- To temporarily expand or collapse an editor pane, click the Focus/Unfocus this Editor Pane button on the left of the editor toolbar.

![An Xcode screenshot of the project editor with the Project navigator on the left and a source file selected. The editor area on the right shows the comparison view above and two source editor panes side-by-side below with the Canvas menu item selected from the Adjust Editor Options pop-up menu.](https://docs-assets.developer.apple.com/published/c902ea1cf11e2fa48287367f158132d3/configuring-editor-area%402x.png)

##### Choose Editor Options and Companion Views

You configure editor panes using controls on the editor toolbar. Use the Adjust Editor Options pop-up menu on the right of the editor toolbar to add options to an editor pane and change the layout of it. You can choose from the following editor options:

##### Compare File Changes with Previous Versions

For files under source control, you can compare your changes with a previous commit. To toggle the comparsion view, click the Enable/Disable Code Review button on the left of the editor toolbar.

To show the previous commit on the right of an editor, choose Side By Side Comparison from the Adjust Editor Options pop-up menu. To show the changes in an editor, choose Inline Comparison.

Then use the controls on the bottom of the comparison view to select versions of the file to compare.

##### Switch Quickly Between Files Using the Tab Bar

Use the  that appears above an editor pane to open and pin files that you access frequently. To show the tab bar, choose View > Show Editor Tab Bar. Then add, remove, and pin files:

- To add a new tab, choose Tab from the Add button pop-up menu to the right of the tab bar, then enter a filename or select a recent file in the Start Page below.
- To open one or more files in tabs, select the files in the Project navigator, then choose either File > Open in New Tab or File > Open in New Tabs.
- To pin or unpin a tab, hover over the tab and click the pin icon on the right side of the tab.
- To close a tab, hover over the tab and click the X on the left side of the tab.

For other actions, Control-click the tab and choose an item from the pop-up menu, such as Close Other Tabs.

![An Xcode screenshot of the project editor with the Project navigator on the left and a source file selected. The editor area is on the right with the source editor on its right and the canvas on its left. The tab bar appears above the editor toolbar with a tab contextual pop-up menu showing the Close Other Tabs menu item selected.](https://docs-assets.developer.apple.com/published/526fd0bed9b35ee85a941e3ad7b9eecf/using-editor-tabs%402x.png)

## See Also

- [Finding and replacing content in a project](finding-and-replacing-content-in-a-project.md)
  Search some or all of your project for text strings or symbol names, and perform advanced searches using regular expressions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-the-xcode-project-window)*