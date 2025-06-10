# Adding capabilities to your app

**Framework**: Xcode

Configure your target to include and customize capabilities that provide access to Apple’s app services.

#### Overview

A  grants your app access to an  that Apple provides, such as CloudKit, Game Center, or In-App Purchase. To use some app services, you must provision your app, adding a capability with Xcode’s project editor that configures the app service correctly for you. Xcode edits the [`Entitlements`](https://developer.apple.com/documentation/BundleResources/Entitlements) and [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List) files, adds related frameworks, and configures your signing assets.

However, some app services — such as Game Center and In-App Purchase — require additional configuration in App Store Connect and your developer account. For example, you need to [`upload a geographic coverage file`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev4ba662442) using App Store Connect for an app that uses Maps to provide directions for other apps.

The platform, and whether you’re a member of the [`Apple Developer Program`](https://developer.apple.comhttps://developer.apple.com/programs/), may limit the capabilities available to your app. For the supported capabilities, go to the Reference section of [`Developer Account Help`](https://developer.apple.comhttps://developer.apple.com/help/account/) — for example, go to [`Supported capabilities (iOS)`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/supported-capabilities-ios) for the capabilities available to iOS apps.

Before you begin, [`add your Apple Account`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devaf282080a) and [`assign the project to a team`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev23aab79b4) so that Xcode can provision your app. For iOS, iPadOS, tvOS, visionOS, and watchOS apps, [`run your app on a device`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev5a825a1ca) to register the device and create a development provisioning profile.

> ❗ **Important**: Use the default automatic signing when you create a project from a template. If you [`manually sign your app`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev1bf96f17e), you need to perform the capability configuration steps yourself.

##### Add a Capability

You add capabilities to your app using the Signing & Capabilities pane of the project editor.

In the Project navigator of the main window, select the project — the root group with the same name as your app — and in the project editor that appears, select the appropriate target and then click the Signing & Capabilities tab.

![A screenshot of Xcode’s project editor with the Signing & Capabilities tab open. The screenshot includes callouts that instruct you to choose your project in the Project navigator, then choose a target from the targets list, and finally click the Signing & Capabilities tab to reveal the relevant configuration for the project’s selected target.](https://docs-assets.developer.apple.com/published/4730dda867b70c6919ba22cdc7772c02/signing-capabilities%402x.png)

Optionally, select a build configuration (All, Debug, or Release). For example, if you want to add the capability to the Debug configuration only, select Debug; otherwise, select All.

In the toolbar, click the Library button (+) to open the Capabilities library. Alternatively, click + Capability to the left of the build configurations, or choose Editor > Add Capability. The Capabilities library displays only the capabilities available to the target platform and your program membership. Select a capability in the list to view its description on the right.

![A screenshot of Xcode with the Capabilities library open. The screenshot highlights the two buttons you can use to open the library, which shows a list of available capabilities on the left, where you can double-click or drag a capability to add it to the selected target. On the right is a textual description of the selected capability. There’s also a text box at the top of the library that allows you to filter the list of capabilities.](https://docs-assets.developer.apple.com/published/0077bd161691f1b7ffa7b1e405aab7d0/capabilities-library%402x.png)

To add a capability to the app target, double-click the capability in the library or drag the capability from the library to the Signing & Capabilities pane. The capability appears below the Signing section. If there are more configuration steps, the capability expands to show additional controls (see [`Perform additional configuration steps`](adding-capabilities-to-your-app#Perform-additional-configuration-steps.md) below). To remove a capability, click the Delete (x) button in the upper-right corner of the capability in the Signing & Capabilities pane.

![A screenshot of Xcode displaying the additional configuration options for the Associated Domains capability, which appears after you add the capability to the selected target. There’s a button at the upper right of the configuration section that enables you to remove the capability from the target.](https://docs-assets.developer.apple.com/published/1f7b8e10474727826b8d17e04d34bfda/additional-configuration%402x.png)

If errors appear in the Signing section, read the message, correct the problem, then click Try Again. For example, the bundle ID ([`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier)) that appears in the Bundle Identifier field under Signing needs to be unique. The default value for the bundle ID is the organization identifier concatenated with the app name that you enter when creating a project.

##### Perform Additional Configuration Steps

For some capabilities, you may need to perform additional configuration steps in Xcode, your developer account, or App Store Connect. For other capabilities, you may need to write some code.

For more guidance on specific capabilities, see the table below:

| Capability | Additional information |
| --- | --- |
| App Groups | [`Configuring app groups`](configuring-app-groups.md) |
| App Sandbox | [`Configuring the macOS App Sandbox`](configuring-the-macos-app-sandbox.md) |
| Apple Pay | [`Configuring Apple Pay support`](configuring-apple-pay-support.md) |
| Associated Domains | [`Configuring an associated domain`](configuring-an-associated-domain.md) |
| Background Modes | [`Configuring background execution modes`](configuring-background-execution-modes.md) |
| ClassKit | [`Enabling ClassKit in your app`](https://developer.apple.com/documentation/ClassKit/enabling-classkit-in-your-app) |
| Fonts | [`Configuring custom fonts`](configuring-custom-fonts.md) |
| Game Controllers | [`Configuring game controllers`](configuring-game-controllers.md) |
| Group Activities | [`Configuring Group Activities`](configuring-group-activities.md) |
| Hardened Runtime | [`Configuring the hardened runtime`](configuring-the-hardened-runtime.md) |
| HealthKit | [`Configuring HealthKit access`](configuring-healthkit-access.md) |
| HomeKit | [`Configuring HomeKit access`](configuring-homekit-access.md) |
| iCloud | [`Configuring iCloud services`](configuring-icloud-services.md) |
| In-App Purchase | [`Configuring in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases) |
| Keychain Sharing | [`Configuring keychain sharing`](configuring-keychain-sharing.md) |
| Maps | [`Configuring Maps support`](configuring-maps-support.md) |
| Media Device Discovery | [`Configuring media device discovery`](configuring-media-device-discovery.md) |
| Network Extensions | [`Configuring network extensions`](configuring-network-extensions.md) |
| On-Demand Install Capable | [`Creating an App Clip with Xcode`](https://developer.apple.com/documentation/AppClip/creating-an-app-clip-with-xcode) |
| Push Notifications | [`Registering your app with APNs`](https://developer.apple.com/documentation/UserNotifications/registering-your-app-with-apns) |
| Sign in with Apple | [`Configuring Sign in with Apple support`](configuring-sign-in-with-apple.md) |
| Siri | [`Configuring Siri support`](configuring-siri-support.md) |
| Wallet | [`Configuring Wallet support`](configuring-wallet-support.md) |


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app)*