# Migrating to a single-target watchOS app

**Framework**: watchOS apps

Adopt the single-target configuration to simplify your project and avoid ambiguity about where to store resources and apply entitlements.

#### Overview

A watchOS app has one of the following project configurations:

- **Dual target**: Contains a watchOS app target and a separate WatchKit extension target that holds the app’s core logic and resources.
- **Single target**: Contains only a watchOS app target, which holds all of the app’s logic and resources.

Single-target apps have a simpler project configuration and avoid ambiguity about where to store resources and apply entitlements.

> **Note**: Both single-target and dual-target apps can include other targets. For example, you can add a target to implement widgets or app intents.

When the minimum deployment target is watchOS 9.2 or later, building a dual-target app with Xcode produces an error, and prompts you to migrate to a single-target app using the built-in migrator. Building a single-target app that still uses the  [`WKExtension`](https://developer.apple.comhttps://developer.apple.com/documentation/watchkit/wkextension) APIs produces warnings that guide you to replace the APIs with the [`WKApplication`](https://developer.apple.comhttps://developer.apple.com/documentation/watchkit/wkapplication) counterparts. If you have a dual-target watchOS app, migrate it to a single-target app.

#### Convert a Dual Target App to a Single Target App

Follow these steps to convert your app:

1. Create a complete backup of your project before you start, so you can roll back if something goes wrong.
2. In the Project navigator, select your project, then choose Xcode > Editor > Validate Settings.
3. Select the “Project `<your project>` - Upgrade `<your watchOS app target>` to a single-target watch app” checkbox if it’s unselected, then choose Perform Changes.
4. If you use storyboards, update the class module for each interface controller to the watchOS app module. Select an interface controller, choose View > Inspectors > Identity, then set the Class field in the Custom Class section. Repeat for each interface controller.
5. Remove any files that only apply to the WatchKit extension, such as the extension’s information property list.
6. Reorganize the groups and files in the Project navigator to clean up your project.
7. Run the project on an Apple Watch to verify everything works.

The second step removes the WatchKit extension target and moves its source code and resources to the watchOS app target. At the code level, it replaces [`WKExtension`](https://developer.apple.comhttps://developer.apple.com/documentation/watchkit/wkextension) and [`WKExtensionDelegate`](https://developer.apple.comhttps://developer.apple.com/documentation/watchkit/wkextensiondelegate) with [`WKApplication`](https://developer.apple.comhttps://developer.apple.com/documentation/watchkit/wkapplication) and [`WKApplicationDelegate`](https://developer.apple.comhttps://developer.apple.com/documentation/watchkit/wkapplicationdelegate).

It also updates the watchOS app target’s information property list as needed. For example, if your watchOS app has a complication, it moves the complication controller class, which is specified with [`CLKComplicationPrincipalClass`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/clkcomplicationprincipalclass), to the watchOS app target, and adds the `CLKComplicationPrincipalClass` and [`CLKComplicationSupportedFamilies`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/clkcomplicationsupportedfamilies) entries to the watchOS app’s information property list.

## See Also

- [Creating an intuitive and effective UI in watchOS 10](creating-an-intuitive-and-effective-ui-in-watchos-10.md)
  Provide an even more streamlined, consistent, and glanceable user experience with new design features.
- [Updating your app and widgets for watchOS 10](updating-your-app-and-widgets-for-watchos-10.md)
  Integrate SwiftUI elements and watch-specific features, and build widgets for the Smart Stack.
- [Building a watchOS app](building_a_watchos_app.md)
  Set up your app’s life cycle and create its user interface with SwiftUI.
- [watchOS updates](../Updates/watchos.md)
  Learn about important changes to watchOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/migrating-to-a-single-target-watchos-app)*