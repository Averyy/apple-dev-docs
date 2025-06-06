# Configuring HealthKit access

**Framework**: Xcode

Read and write health and activity data in the Health app.

#### Overview

HealthKit is the central repository for health and fitness data in iOS and watchOS. Health apps that integrate with HealthKit can request a user’s permission to both read health data from and write data to this central repository. The data your app writes to the HealthKit store is visible to the user in the Health app, alongside their other health-related data.

To enable your app to access the user’s HealthKit store, you must add the HealthKit capability to your app’s target and include a short description of the app’s functionality in its target’s `Info.plist` file.

##### Add the Healthkit Capability to Your Target

Follow the steps in [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) to add the capability to your app’s target; be sure to select the HealthKit capability from Xcode’s Capabilities library. For watchOS apps with separate WatchKit extensions, you must add the capability to the WatchKit Extension target.

> **Note**: The HealthKit capability is available for iOS and watchOS apps. watchOS apps can only access certain health data. Clinical Health Records aren’t accessible by watchOS apps.

The HealthKit capability is available for iOS and watchOS apps. watchOS apps can only access certain health data. Clinical Health Records aren’t accessible by watchOS apps.

![A screenshot of Xcode’s Capabilities library with a list of available capabilities on the left and an information pane on the right. The list shows a range of capabilities from HealthKit to MDM Managed Associated Domains, and the HealthKit capability is in a selected state. The text on the information pane explains that, by enabling HealthKit, your app, with the user’s permission, is able to store and retrieve personal health information.](https://docs-assets.developer.apple.com/published/6900f466c38e7fe44766968a62821d44/healthkit%402x.png)

After you add the HealthKit capability, Xcode links the [`HealthKit`](https://developer.apple.com/documentation/HealthKit) framework to your target and updates the target’s entitlements file to include the [`HealthKit Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.healthkit). If Xcode automatically manages the signing of your app, it also enables HealthKit for your app’s App ID.

> **Note**: If you later remove the HealthKit capability in Xcode, you must manually update your App ID’s configuration in your developer account to disable HealthKit.

If you later remove the HealthKit capability in Xcode, you must manually update your App ID’s configuration in your developer account to disable HealthKit.

##### Request Access to the Users Health Data

HealthKit uses a fine-grained authorization mechanism to help protect the user’s privacy; your app must request permission to read and, optionally, write each individual sample type it supports. For more information, see [`Authorizing access to health data`](https://developer.apple.com/documentation/HealthKit/authorizing-access-to-health-data).

Before prompting the user for their permission, you must configure your app to include one or more , which accurately and concisely describe why the app needs to read the user’s health data, write health data to their HealthKit store, or both. The presence of these purpose strings is an App Store requirement for any app that integrates with HealthKit. The system displays this information to the user when requesting their permission, along with the specific sample types that your app needs to access, which helps them make an informed decision.

Follow these steps to add the purpose string for reading health data to your app’s target:

1. In the Project navigator, select your target’s `Info.plist` file.
2. Move the mouse pointer over the “Information Property List” key.
3. Click the Add button (+) that appears.
4. Choose “Privacy - Health Share Usage Description”.
5. Double-click the Value column to the right of the key and enter your app’s purpose string.

![A screenshot of an app’s Info.plist file open in Xcode’s property list editor. The property list contains the Privacy - Health Share Usage Description key with an example purpose string as its value.](https://docs-assets.developer.apple.com/published/783ab0bb8945c7fe5efdfce2265de5bc/health-share-usage-description%402x.png)

If your app writes health data to the HealthKit store, repeat the steps above and add the “Privacy - Health Update Usage Description” key.

Remember that the user can revoke their permission at any time in the Settings app or the Health app. If your app requires access to certain health data, you must clearly display information about why your app requires access to the user’s health data and request that the user reauthorize to grant your app access to the HealthKit data.

You can check your app’s current authorization status using the [`authorizationStatus(for:)`](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614154-authorizationstatus) method. HealthKit also returns a [`HKError.Code.errorAuthorizationDenied`](https://developer.apple.com/documentation/HealthKit/HKError/Code/errorAuthorizationDenied) error if your app attempts unauthorized access to the user’s health data.

##### Request Access to a Users Health Records

HealthKit’s clinical-record support allows users to download their records in the Fast Healthcare Interoperability Resources (FHIR) format from supported healthcare institutions. HealthKit then periodically updates those records in the background.

Due to the sensitive nature of health records, your app requires a special entitlement before it can access them. Follow these steps to configure that entitlement:

1. Select your project in Xcode’s Project navigator.
2. Select your app’s target from the Targets list.
3. Click the Signing & Capabilities tab in the project editor.
4. Find the HealthKit capability.
5. Enable the nested Clinical Health Records capability.

![A screenshot of the HealthKit capability after you add it to a target. The Clinical Health Records capability is in an enabled state.](https://docs-assets.developer.apple.com/published/f44dc6888f10098c6cd63859643b7b6f/clinical-health-records%402x.png)

Xcode adds the [`HealthKit Capabilities Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.healthkit.access) to your target’s entitlements file and appends the `health-records` value to the array it contains.

After you enable the capability, there are additional configuration steps you must complete before your app can access the user’s health records, such as providing an additional purpose string and declaring the types of health records that your app supports. For more information, see [`Accessing Health Records`](https://developer.apple.com/documentation/HealthKit/accessing-health-records).

##### Receive Sample Updates in the Background

HealthKit observer queries are long-running ones that watch the HealthKit store for changes to specific sample types and deliver those changes to your app on a background thread. Typically, observer queries only provide those changes when your app is running in the foreground.

However, by enabling Background Delivery, your app can continue to receive and process changes while it’s in the background. You pair each executed observer query with a call to [`enableBackgroundDelivery(for:frequency:withCompletion:)`](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614175-enablebackgrounddelivery) and specify the same sample type. The system then wakes your app when changes occur in the HealthKit store — at most, once per the update frequency you specify — and delivers those changes to the corresponding observer queries. For more information, see [`Executing Observer Queries`](https://developer.apple.com/documentation/HealthKit/executing-observer-queries).

To enable HealthKit to continue updating your app’s observer queries while its in the background, perform the following:

1. Select your project in Xcode’s Project navigator.
2. Select the app’s target from the Targets list.
3. Click the Signing & Capabilities tab in the project editor.
4. Find the HealthKit capability.
5. Enable the nested Background Delivery capability.

![A screenshot of the HealthKit capability after you add it to a target. The Background Delivery capability is in an enabled state.](https://docs-assets.developer.apple.com/published/5550ba5b6d202e6d9c8b48f8edf5050a/background-delivery%402x.png)

Xcode adds the [`com.apple.developer.healthkit.background-delivery`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.healthkit.background-delivery) entitlement to the target’s entitlements file.

## See Also

- [Configuring HomeKit access](configuring-homekit-access.md)
  Discover compatible accessories and communicate with configured accessories and services to perform actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-healthkit-access)*