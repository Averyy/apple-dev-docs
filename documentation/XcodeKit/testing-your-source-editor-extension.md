# Testing Your Source Editor Extension

**Framework**: Xcodekit

Launch a special instance of Xcode to test your source editor extension.

#### Overview

Source editor extensions run in a separate instance of Xcode to help prevent mistakes in your in-progress extension from interfering with your development environment.

##### Test the Source Editor Extension

Test a source editor extension you’re developing by running your project when your extension’s scheme is selected. A dialog appears, asking you to choose an app to run.

![Screenshot showing an Xcode dialog with a list of apps to run. The selected app is Xcode.](https://docs-assets.developer.apple.com/published/60fe88b8abb39ae3a7fba25239722e29/media-2902155%402x.png)

Choose Xcode, and your source editor extension is initialized inside the second instance of Xcode. You can tell the two instances of Xcode apart based on the background color of the app icons. The instance of Xcode that’s running your source editor extension has a black background rather than the lighter blue background of the first instance.

![The app icon for Xcode with a black background instead of the usual blue background.](https://docs-assets.developer.apple.com/published/18a5019838f9e6f2ae83f22589221101/media-2902156%402x.png)

To test commands defined by your extension, open a source file in the test instance of Xcode. All of the commands defined by your extension appear in the Editor menu, nested under your extension’s name.  Selecting a command causes the [`perform(with:completionHandler:)`](xcsourceeditorcommand/perform(with:completionhandler:).md) method defined in your extension to be called with a command invocation that specifies a command identifier corresponding to that command.

While you test your source editor extension, the original instance of Xcode continues running. Use it to debug or to view console output from the extension you’re testing.

## See Also

- [class XCSourceEditorCommandInvocation](xcsourceeditorcommandinvocation.md)
  An object that identifies the command issued to your extension and provides the contents of the active source editor.
- [Creating a Source Editor Extension](creating-a-source-editor-extension.md)
  Add and configure a source editor extension in your Xcode project.
- [protocol XCSourceEditorExtension](xcsourceeditorextension.md)
  The protocol you implement to create Xcode source editor extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/testing-your-source-editor-extension)*