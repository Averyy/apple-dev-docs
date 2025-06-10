# Creating an Xcode project for an app

**Framework**: Xcode

Start developing your app by creating an Xcode project from a template.

#### Overview

To create an Xcode project for your app, choose a template for the platform on which your app will run, and select the type of app you wish to develop, such as a single view, game, or document-based for iOS. Xcode templates include essential project configuration and files that help you start developing your app quickly.

##### Prepare Configuration Information

Before you create a project, collect the information that Xcode needs to identify your app and you as a developer:

-  The name of your app as it will appear in the App Store and appear on a device when installed. The product name must be at least 2 characters and no more than 255 bytes, and should be similar to the app name that you enter later in App Store Connect.
-  A reverse DNS string that uniquely identifies your organization. If you don’t have a company identifier, use `com.example.` followed by your organization name, and replace it before you distribute your app.
-  The name that appears in boilerplate text throughout your project folder. For example, the source and header file copyright strings contain the organization name. The organization name in your project isn’t the same as the organization name that appears in the App Store.

> ❗ **Important**: The organization identifier is part of the bundle ID ([`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier)) by default. Xcode uses the bundle ID to register an App ID when you first run your app on a device. The number of App IDs are limited if you are not a member of the Apple Developer Program, and you can’t change the App ID after you upload a build to App Store Connect, so choose the organization identifier carefully.

##### Create a Project

Launch Xcode, then click “Create a new Xcode project” in the Welcome to Xcode window or choose File > New > Project. In the sheet that appears, select the target operating system or platform and a template under Application. In the following sheets, fill out the forms and choose options to configure your project.

![Screenshot of an Xcode window depicting the choices for a template for a new project. At the top are a list of platforms from which to choose, including iOS, watchOS, and so on. In the lower half of the window, options for types of applications are displayed, such as a game and an augmented reality app. The type “Single View App” is highlighted.](https://docs-assets.developer.apple.com/published/714daaca83de4a304e3a9c351f0d468d/creating-an-xcode-project-for-an-app-1%402x.png)

If you see a banner that says you don’t have support for the platform, you can create the project, but you can’t build and run it on a device. To install the platform now, click the Get button on the right of the banner. Otherwise, you can manage downloads in the Components settings later (see [`Downloading and installing additional Xcode components`](downloading-and-installing-additional-xcode-components.md)).

To continue creating your project, you need to provide a  and  because they are used to create the  that identifies your app throughout the system. Also enter an . If you don’t belong to an organization, enter your name.

![Screenshot showing new project options where you enter a product name, organization name, and organization identifier, and choose a Team and a programming language.](https://docs-assets.developer.apple.com/published/fc17beb75b820e8ebb654513906e95fd/creating-an-xcode-project-for-an-app-2%402x.png)

To develop for all platforms and see an interactive preview of your layout, choose SwiftUI as the user interface before you click Next on this sheet.

##### Manage Files in the Main Window

When you create a project or open an existing project, the  appears, showing the necessary files and resources for developing your app.

You can access different parts of your project from the  in the main window. Use the  to select files you want to edit in the . For example, when you select a Swift file in the project navigator, the file opens in the  where you can modify the code and set breakpoints.

![Screenshot showing the location of the main window areas: the toolbar at the top, navigator area on the left, editor area to the right, debug area below, and inspector area on the right.](https://docs-assets.developer.apple.com/published/7df07db6e97c54d87701e9fa161ef946/creating-an-xcode-project-for-an-app-3%402x.png)

Details about the selected file also appear in the  on the right. In the inspector area, you can select the Attributes inspector to edit properties of a file or user interface element. If you want to hide the inspector to make more room for the editor, click the “Hide or show the Inspectors” button in the upper-right corner of the toolbar.

You use the  to build and run your app on a simulated or real device. For iOS apps, choose the app target and a simulator or device from the run destination menu in the toolbar, then click the Run button.

For macOS apps, just click the Run button. When your app launches, the  opens, where you can control the execution of your app and inspect variables. When the app stops at the breakpoint, use the controls in the debug area to step through the code or continue execution. When you are done running the app, click the Stop button in the toolbar.

If you use SwiftUI, you can see an interactive preview of the user interface while you create your app. Xcode keeps the changes you make in the source file, the canvas on the right, and the inspector in sync. You can use the controls in the preview to run the app with the debugger, too. For details, see [`Creating your app’s interface with SwiftUI`](creating-your-app-s-interface-with-swiftui.md).

To change properties you entered when creating your project, select the project name in the project navigator that appears at the top, then the  opens in the editor area. Most of the properties you entered appear on the  of the project editor.

![Screenshot showing the General pane of the project editor with the Identity and Deployment Info settings revealed.](https://docs-assets.developer.apple.com/published/ad8ace328b4d964404e745d30c8629f4/creating-an-xcode-project-for-an-app-4%402x.png)

## See Also

- [Creating your app’s interface with SwiftUI](creating-your-app-s-interface-with-swiftui.md)
  Develop apps in SwiftUI with an interactive preview that keeps the code and layout in sync.
- [Previewing your app’s interface in Xcode](previewing-your-apps-interface-in-xcode.md)
  Iterate designs quickly and preview your apps’ displays across different Apple devices.
- [Building and running an app](building-and-running-an-app.md)
  Compile your source files and assemble an app bundle to run on a device or simulator.
- [Xcode updates](../Updates/Xcode.md)
  Learn about important changes to Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-an-xcode-project-for-an-app)*