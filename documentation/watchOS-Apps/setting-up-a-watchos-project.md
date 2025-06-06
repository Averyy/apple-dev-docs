# Setting up a watchOS project

**Framework**: Watchos Apps

Create a new watchOS project or add a watch target to an existing iOS project.

#### Overview

Before you start a new watchOS project, you need to decide how you’re going to distribute that project: as a watch-only app or as a watchOS app with an iOS app. If your app is only available on Apple Watch, create a new watch-only project. If you want both a watchOS and an iOS app that deliver related experiences, either create a new watchOS app with a companion iOS app or add a watchOS target to an existing iOS project.

##### Create a New Watchos Project

To create a new watchOS project:

1. In Xcode, choose File > New > Project.
2. Select the watchOS tab.
3. Select the App icon and click Next.
4. In the project options sheet, enter a name for the project. To create a watch-only app, select “Watch-only App.” To create both a watchOS app and an iOS app, select “Watch App with New Companion iOS App.” Then click Next.
5. Select a location for the project and click Create.

![A screenshot of Xcode’s project option sheet. The project name is set to MyWatchApp, and the Watch-only App setting is selected.](https://docs-assets.developer.apple.com/published/88ef10c12f874110f31de25d63d77369/setting-up-a-watchos-project-project-settings%402x.png)

##### Add a Watchos Target to an Existing Ios App

To add a watchOS target to an existing iOS project:

1. Select the project in the Project navigator.
2. Click the “Add a target” button in the Project editor.
3. Select the watchOS tab.
4. Select the App icon and click Next.
5. In the project option sheet, enter a name for the watchOS app, and select “Watch app for Existing iOS App.” Make sure to select the correct iOS app in the pull-down menu, and click Finish.

![A screenshot of Xcode’s project option sheet. The project name is set to MyWatchApp. The Watch app for Existing iOS App setting is selected, and MyApp is selected in the pull-down menu.](https://docs-assets.developer.apple.com/published/32ea965cdeb449091024e0533fdcd0c7/setting-up-a-watchos-project-adding-watch-target%402x.png)

## Topics

### Information property list keys
- [WKWatchKitApp](../BundleResources/Information-Property-List/WKWatchKitApp.md)
  A Boolean value that indicates whether the bundle is a watchOS app.
- [WKAppBundleIdentifier](../BundleResources/Information-Property-List/WKAppBundleIdentifier.md)
  The bundle ID of the watchOS app.
- [WKCompanionAppBundleIdentifier](../BundleResources/Information-Property-List/WKCompanionAppBundleIdentifier.md)
  The bundle ID of the watchOS app’s companion iOS app.
- [WKExtensionDelegateClassName](../BundleResources/Information-Property-List/WKExtensionDelegateClassName.md)
  The name of your watchOS app’s extension delegate.
- [WKRunsIndependentlyOfCompanionApp](../BundleResources/Information-Property-List/WKRunsIndependentlyOfCompanionApp.md)
  A Boolean value indicating whether the user can install and run the watchOS app independently of its iOS companion app.
- [WKWatchOnly](../BundleResources/Information-Property-List/WKWatchOnly.md)
  A Boolean value indicating whether the app is a watch-only app.

## See Also

- [Creating independent watchOS apps](creating-independent-watchos-apps.md)
  Set up a watchOS app that installs and runs without a companion iOS app.
- [Keeping your watchOS content up to date](keeping-your-watchos-app-s-content-up-to-date.md)
  Ensure that your app’s content is relevant and up to date.
- [Updating watchOS apps with timelines](updating-watchos-apps-with-timelines.md)
  Seamlessly schedule updates to your user interface, even while it’s inactive.
- [Authenticating users on Apple Watch](authenticating-users-on-apple-watch.md)
  Create an account sign-up and sign-in strategy for your app.
- [Responding to the Action button on Apple Watch Ultra](../AppIntents/ActionButtonArticle.md)
  Use App Intents to register actions for your app.
- [Enabling the double-tap gesture on Apple Watch](enabling-double-tap.md)
  Customize your app’s response to the double-tap gesture on Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/setting-up-a-watchos-project)*