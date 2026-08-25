# Creating an Xcode project for an app

**Framework**: Xcode

Set up a new project to start developing your app.

#### Overview

Xcode creates a project for the platforms and type of app you want to make, so you can begin writing and testing code immediately. You can start with a basic SwiftUI project or customize one of the templates for the technologies you want to use. Then familiarize yourself with the project window and learn where to change the project configuration.

#### Create a Swiftui App Project

On the Welcome to Xcode window that appears when you first launch Xcode, choose App from the New Project pop-up menu or choose File > New > Project and select App from anywhere in Xcode.

![A screenshot of the Welcome to Xcode window showing App chosen from the New Project pop-up menu.](/images/com.apple.Xcode/choosing-new-project-app@2x.png)

To save your code changes, choose File > Save Project, and in the sheet that appears, enter the project name in the Save As field and click Save. To use a different name for the app, toggle off Rename Target.

#### Create a Project From a Template

For more complex apps that use specific technologies, create a project from an Xcode template to get started. For example, you can create a project for a SwiftUI app that uses SwiftData, a macOS command-line tool, an iOS augmented reality app, or a visionOS immersive environment app.

On the Welcome to Xcode window, choose Choose Template from the New Project pop-up menu or choose File > New > Project and then click Choose Template from anywhere in Xcode.

In the sheet that appears, select Multiplatform for an app that runs on all platforms or a specific platform, such as iOS or macOS. Then select a template under Application depending on the platform you select.

![A screenshot of an Xcode window showing the template choices for a new project. At the top is a list of platforms from which to choose, including Multiplatform, iOS, and macOS. In the lower half of the window, options for types of apps are displayed, such as a game and an augmented reality app.](/images/com.apple.Xcode/choosing-an-app-template@2x.png)

If you see a banner that says you don’t have support for a platform, you can create the project, but you can’t build and run it. To install the platform now, click the Get button on the right of the banner. Otherwise, manage downloads in the Components settings later. For more information, see [`Downloading and installing additional Xcode components`](downloading-and-installing-additional-xcode-components.md).

In the “Choose options for your new project” sheet:

- Enter a *product name* for your app as you want it to appear on App Store product pages and when someone installs your app. Later, you can change the app name in the General pane of the project editor.
- Optionally, choose an account from the Team pop-up menu that Xcode uses to code sign your app. If your account doesn’t appear, choose Add an Account to enter your credentials in Apple Accounts settings. To create an Apple developer account, see [`Apple Developer Program`](https://developer.apple.comhttps://developer.apple.com/programs/).
- Enter an *organization identifier* that Xcode uses to create the *bundle identifier* ([`CFBundleIdentifier`](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundleidentifier)) that uniquely identifies your app throughout the system.
- Choose other options from pop-up menus below depending on the template you select, such as SwiftUI for the interface and Swift for the language.

![A screenshot showing new project options where you enter a product name and organization identifier, and choose a Team and other options depending on the template.](/images/com.apple.Xcode/choosing-template-options@2x.png)

In the last sheet, choose a location for your project, select other options, and click Create. Xcode creates a project containing essential configuration and source code files to build and run the type of app you select.

For more information on properties in your project that the App Store uses, see [`App information`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-information) in App Store Connect Help.

#### Manage Files in the Main Window

When you create a project or open an existing project, the *main window* appears, showing the necessary files and resources for developing your app.

You can access different parts of your project from the *navigator area* on the left. Use the *Project navigator* to select files you want to edit in the *editor area*. For example, when you select a Swift file in the Project navigator, the file opens in the *source editor*, where you can modify the code and set breakpoints.

![A screenshot showing the location of the main window areas: the toolbar at the top, navigator area on the far left, editor area in the middle, canvas area on the right, debug area below, and inspector area on the far right.](/images/com.apple.Xcode/project-main-window-anatomy@2x.png)

Details about the selected file also appear in the *inspector area* on the right. In the inspector area, you can select the File inspector to edit properties of a file. If you want to hide the inspector to make more room for the editor, click the “Hide or show the Inspectors” button in the upper-right corner of the toolbar.

You use the *toolbar* to build and run your app on a simulated or physical device. For an iOS app, choose a device from the run destination pop-up menu and click Run. For a macOS app, choose My Mac and click Run. For more information, see [`Running your app on simulated or physical devices`](running-your-app-on-simulated-or-physical-devices.md).

When your app launches, the *debug area* opens, where you can control the execution of your app and inspect variables. When the app stops at a breakpoint that you set, use the controls in the debug area to step through the code or continue execution. When you are done running the app, click Stop in the toolbar. For more information on using the debugger, see [`Diagnosing and resolving bugs in your running app`](diagnosing-and-resolving-bugs-in-your-running-app.md).

If you add a preview or playground to your source file, you can interact with it in the canvas area. Most projects you create from a template already contain previews that appear in the canvas. For more information, see [`Adding previews to your interface files`](adding-previews-to-your-interface-files.md) and [`Running code snippets using the playground macro`](running-code-snippets-using-the-playground-macro.md).

To use the coding assistant to explain or generate code, see [`Writing code with intelligence in Xcode`](writing-code-with-intelligence-in-xcode.md).

#### Change the Configuration in the Project Editor

To view your project configuration, select the project in the Project navigator, then select the target in the *project editor* on the right. Click the tabs in the project editor, such as General and Signing & Capabilities, to make changes.

![A screenshot of the General pane of the project editor with the Supported Destinations and Identity settings visible.](/images/com.apple.Xcode/showing-the-project-editor@2x.png)

For example, on the General pane you can change the bundle ID after you create your project. For all the steps to change the bundle ID, see [`Changing the bundle identifier`](changing-the-bundle-identifier.md).

To add a [`Liquid Glass`](https://developer.apple.com/documentation/technologyoverviews/liquid-glass) app icon that supports different platforms and appearances to your project, see [`Creating your app icon using Icon Composer`](creating-your-app-icon-using-icon-composer.md).

## See Also

- [Interacting with previews in the canvas](interacting-with-previews-in-the-canvas.md)
  Use the canvas controls to test your view’s appearance and behavior on different devices and configurations.
- [Adding previews to your interface files](adding-previews-to-your-interface-files.md)
  Write code to test your views on different devices and configurations without needing to run your app.
- [Running your app on simulated or physical devices](running-your-app-on-simulated-or-physical-devices.md)
  Launch your app on a simulated iOS, iPadOS, tvOS, visionOS, or watchOS device, or on a physical device paired with your Mac.
- [Xcode updates](../updates/xcode.md)
  Learn about important changes to Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-an-xcode-project-for-an-app)*