# Creating independent watchOS apps

**Framework**: watchOS apps

Set up a watchOS app that installs and runs without a companion iOS app.

#### Overview

Apple Watch users have come to expect that the apps on their watches just work, even when they don’t have their iPhones with them. To ensure the best experience for all Apple Watch users, create an independent watchOS app that doesn’t require a companion iOS app for iPhone. You can do this in two ways:

- Create a watch-only app that doesn’t have a companion iOS app.
- Create a watchOS app that has a companion iOS app, but people can install and run independently of the companion.

Create a watch-only app for apps that only run on Apple Watch. If you have watchOS and iOS apps that are substantially similar, release them as companion apps.

People can purchase watchOS apps directly from the App Store on Apple Watch. They can make in-app purchases directly on Apple Watch as well. If you create a watchOS app with a companion iOS app, the in-app purchases are universal. Users make the purchase once, and the content is available in both watchOS and iOS. For more information, see [`Original API for In-App Purchase`](https://developer.apple.com/documentation/StoreKit/original-api-for-in-app-purchase).

![A screenshot of a watch face displaying the App Store on Apple Watch.](https://docs-assets.developer.apple.com/published/92a97cfa0808e3acca2d664c2f957e03/creating-independent-watchos-apps-2%402x.png)

##### Create Your Watchos Project

When you create a watchOS project in Xcode, you have two choices:

![A screenshot of Xcode’s new project sheet, with the Watch-only App option in a selected state.](https://docs-assets.developer.apple.com/published/226bc2583485631dfbe6dcfbc9284800/creating-independent-watchos-apps-1%402x.png)

##### Create a Watch Only App

To build a watch-only app, start a new project in Xcode, select the App template from the watchOS tab, and then click Next.

![An Xcode screenshot showing the dialog for creating a new project with  watchOS as the selected target operating system. In the Application section, the App template is in a selected state.](https://docs-assets.developer.apple.com/published/65fd4f9309f53a3d067a078f01ab5dee/creating-independent-watchos-apps-3%402x.png)

Provide a name, and choose the Watch-only App option. Select Include Tests, and click Next.

![An Xcode screenshot showing the available options for a new target, which include entering a product name and organization identifier, and choosing a team. The Watch-only App and Include Tests options are each in a selected state.](https://docs-assets.developer.apple.com/published/8a216bc4b7aef5abca82a80857fd67c9/creating-independent-watchos-apps-4%402x.png)

In the main window, Xcode’s Project navigator displays the folders and files for your project. The Watch App folder contains the code and assets for your app. The Watch AppTests and Watch AppUITests folders contain the unit and user interface tests for your app, respectively.

![A screenshot of Xcode’s Project navigator for a watch-only app. The project contains three folders: Watch App, Watch AppTests, and Watch AppUITests.](https://docs-assets.developer.apple.com/published/35a31b3b57be6da6e3e49154ffedae0a/creating-independent-watchos-apps-5%402x.png)

Xcode also creates four targets for your app and its tests, which you can view in the project editor. The root target is a stub that acts as an iOS wrapper for your project. Xcode needs this stub to properly handle your watch-only app, and uses it to:

- Set the root bundle identifier. The system uses this bundle identifier for Universal Purchase and cross-device communication, such as Device Discovery.
- Package your app for distribution to the App Store.

Xcode doesn’t create an iOS executable for the stub. When someone installs your watch-only app, nothing installs on the paired iPhone.

The other three targets represent the functional portions of your project: your app, its unit tests, and its user interface tests, respectively.

![A screenshot of Xcode’s Project navigator for a watch-only app. The project](https://docs-assets.developer.apple.com/published/94c2cbfdf3c83f299149fda6173e1ae7/creating-independent-watchos-apps-6%402x.png)

##### Create a Watch App with a Companion Ios App

If you create a watchOS app with a companion iOS app, the resulting watchOS app can either be dependent upon, or independent of, the iOS app.

The system downloads and installs the watchOS app directly to Apple Watch for both dependent and independent apps. However, the user can’t launch a dependent watchOS app until the iOS app finishes installing on iPhone.

##### Convert a Dependent Watchos App to an Independent Watchos App

After creating a watchOS app with a companion iOS app, you can convert the resulting dependent watchOS app to be independent of the iOS app. To convert your watchOS app, perform the following steps:

1. In Xcode, select your watchOS project to view the project editor.
2. In the General tab, select the Watch App target.
3. In the Deployment Info section, select the Supports Running Without iOS App Installation option. By default, when you create a new project, this option is in a disabled state.

![A screenshot of Xcode’s project editor with the Watch App target and the General tab each in a selected state. In the Deployment Info section, the Supports Running Without iOS App Installation option is in a selected state.](https://docs-assets.developer.apple.com/published/72b21a80df95ca0d73aced5d2ca6ab92/creating-independent-watchos-apps-7%402x.png)

##### Ensure Your Watchos App Runs Independently

Watch-only and Independent watchOS apps function without a companion iOS app, performing tasks like downloading data, setting up the user’s account, and configuring the app.

Make sure you test all of these functions in your watch app to ensure they behave as expected. For example, make sure your watch app can:

- Create new accounts and sign in users. For more information, see [`Authenticating users on Apple Watch`](authenticating-users-on-apple-watch.md).
- Request permission for any system services the app requires so that the user doesn’t need to authorize an app on their iPhone. Frameworks that support independent watchOS apps display their authorization form directly on Apple Watch.
- Download data directly to the watch. Independent watchOS apps can’t rely on the [`Watch Connectivity`](https://developer.apple.com/documentation/WatchConnectivity) framework to transfer data or files from a companion iOS app. If you need to sync data between devices, consider using CloudKit, or syncing through your own server. For more information, see [`Keeping your watchOS content up to date`](keeping-your-watchos-app-s-content-up-to-date.md).
- Send push notifications, including complication pushes, directly to the watch. For more information, see [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/WatchKit/WKExtension/registerForRemoteNotifications()).

An independent watchOS app can use Watch Connectivity to transfer information from its companion iOS app when the iOS device is available. However, the independent watchOS app can’t use Watch Connectivity as its main source of data, so it needs to be capable of accessing information on its own.

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
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

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/creating-independent-watchos-apps)*