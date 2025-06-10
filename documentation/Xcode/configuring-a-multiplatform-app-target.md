# Configuring a multiplatform app

**Framework**: Xcode

Share project settings and code across platforms in a single app target.

#### Overview

Multiplatform apps broaden the experience of your app to each additional platform you support. In Xcode 14 or later, you can share your app’s project settings and code across platforms using a single, multiplatform target.

In Xcode, an  specifies project settings information like your app’s bundle identifier and display name, as well as which source code files belong to your app. By default, apps that share a multiplatform target share project settings, so you only need to set them once. You can adjust your project settings as needed for individual platforms.

Before you combine targets into a multiplatform target, check your app to determine the differences in build configuration, framework availability, and API availability.

> **Note**: iOS, iPadOS, macOS, tvOS, and visionOS apps can share a single target. watchOS apps remain in a separate target.

##### Evaluate the Project Settings and Code Your Apps Share

If you want to bring an existing app to a new platform, consider the technologies you use on the platform you already support and the additional platforms you plan to build for. If the technologies and project settings that you plan to use overlap considerably, multiplatform app targets are a good fit. Otherwise, use a separate target for each platform. For example, if your existing app uses SwiftUI and you plan to use SwiftUI for the new platform, use one multiplatform target. However, if your existing app uses UIKit and you want to use AppKit for the Mac, use separate targets.

If your app already supports multiple platforms and shares substantial amounts of code and configuration between those projects, consider combining your multiple targets into a single target. In particular, if you’re developing your app in SwiftUI, your app targets likely already share a lot of the same code and configuration. You can use a single `App` structure to define the SwiftUI app life cycle for each platform.

If your app already supports multiple platforms, but you’ve been building each platform separately for a long time, the targets might not share much code or configuration. In these cases, continue using separate targets unless you have a longer term plan for converging platform support.

##### Configure the Supported Destinations for a Target

To add a destination to a target, click the Add (+) button under Supported Destinations, and then select the destination you’d like to add. Depending on the platforms your app already supports, the Add (+) button brings up a different set of destinations that are available to add to the current target. To remove a destination from a target, select the destination, then click the Remove (-) button. The following shows an app target that supports iPhone and iPad:

![A screenshot of Xcode showing the target editor area. Under General Settings, a list of Supported Destinations shows iPhone and iPad, followed by a plus button.](https://docs-assets.developer.apple.com/published/6e3e896f8aa033e38a9930334c44c508/configuring-a-multiplatform-app-target-1%402x.png)

The following shows the additional destinations available to that target:

![A screenshot of Xcode showing platforms you can add. The list shows Apple TV and Mac options. Under Mac, there are options for Mac, Mac Catalyst, and Designed for iPad.](https://docs-assets.developer.apple.com/published/3470ce8d788d165beb9844f98fdb7692/configuring-a-multiplatform-app-target-3%402x.png)

If you’re adding a Mac or Apple Vision destination to a target, choose the destination type that matches the kind of experience you want to provide:

##### Customize Project Settings

Adding support for another platform can reveal places in your project where you want to customize your app for one of the platforms you support or for a new build configuration. You can conditionalize build settings either by build configuration or by platform. Use the Add (+) button next to the setting you want to customize.

The following shows an app that adds “Beta” to the app’s display name in the Beta build configuration and adds “Mobile” to the iOS app’s display name in the Release configuration:

![A screenshot of Xcode showing a popover for configuring an app’s display name.](https://docs-assets.developer.apple.com/published/77980be04111a425925778e6ac608323/configuring-a-multiplatform-app-target-2%402x.png)

##### Resolve Build Issues By Adding Conditional Statements

Adding another platform can also reveal build-time issues in your app. To resolve those issues, insert conditional statements around any code that uses platform-specific APIs or frameworks. For example, an app that includes an AR experience in iOS and iPadOS likely contains code that uses ARKit. ARKit isn’t available in macOS or tvOS, so you need to separate out code that uses platform-specific APIs or frameworks.

Xcode identifies this sort of build-time issue when you build your project. To try a build on a new platform, pick the new run destination in the scheme menu that corresponds with the platform you added. If Xcode identifies any issues, navigate to them one-by-one and use the following steps to resolve them.

 If a framework isn’t available for a platform, surround the import with a `canImport` conditional statement:

```swift
#if canImport(ARKit)
import ARKit
#endif
```

 Frameworks that are available across multiple platforms might have individual symbols likes types, methods, or enumeration cases that are restricted to a subset of platforms. To resolve these availability issues, surround the relevant code with an `#if os` platform compilation condition statement:

```swift
Toggle(isOn: $isOn) {
    Text("Show Holidays calendar")
}
#if os(macOS)
.toggleStyle(.checkbox)
#endif
```

If an entire file is platform specific, you can remove it entirely from the platforms where it’s not applicable. In the target editor for your project, go to Build Phases > Compile Sources, and deselect the source file from the Filters column.

![A screenshot of Xcode that shows the platform selection popover for a source file. The current selection includes both platforms and there are checkboxes to include or exclude iOS or macOS.](https://docs-assets.developer.apple.com/published/7dc777b6d235e1ad0e7f9ce3d329a081/configuring-a-multiplatform-app-target-4%402x.png)

##### Customize the Experience of Your App for Each Platform

Ensure that your app’s user interface and experience fit the needs of each platform by adding platform-specific views and features. For example, some Mac apps include a menu bar extra that appears even when the app isn’t the frontmost app. The following adds a `MenuBarExtra` instance only in the macOS version of a scene:

```swift
var body: some Scene {
    WindowGroup {
        PrimaryView()
    }
    #if os(macOS)
    MenuBarExtra("Inspect", systemImage: "eyedropper") {
        VStack {
            Button("Action One") {
                // ...
            }
            Button("Action Two") {
                // ...
            }
        }
    }
    #endif
}
```

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/).

##### Prepare Each Platform for App Store Submission

Build, run, and test your app on each platform before submitting each version to the App Store separately. Each submission involves a separate build and archival process.

## See Also

- [Configuring a new target in your project](configuring-a-new-target-in-your-project.md)
  Configure your project to build a new product, and add the code and resources the product requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-a-multiplatform-app-target)*