# Configuring iCloud services

**Framework**: Xcode

Share user or app data among multiple instances of your app running on different devices.

#### Overview

As an app developer, you can use one or more iCloud services to securely store your users’ data on the iCloud servers and make it available across all of their iCloud-enabled devices, thereby providing a seamless experience regardless of which device they use.

Xcode’s iCloud capability allows you to configure the following services:

- Key-value storage provides your app with 1 MB of iCloud storage that can contain up to 1024 key-value pairs, which is useful for syncing small amounts of data, such as the user’s preferences. For more information, see [`NSUbiquitousKeyValueStore`](https://developer.apple.com/documentation/Foundation/NSUbiquitousKeyValueStore).
- iCloud Documents allows your app to store data as files and sync those files across devices, which is relevant if your app is already using [`UIDocument`](https://developer.apple.com/documentation/UIKit/UIDocument) or [`NSDocument`](https://developer.apple.com/documentation/AppKit/NSDocument). For more information, see [`Designing for Documents in iCloud`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesigningForDocumentsIniCloud.html#//apple_ref/doc/uid/TP40012094-CH2).
- CloudKit allows your app to store structured objects and relationships in remote databases and provides full control over those databases’ schemas. Users can also choose to share their data with other iCloud users. You can use the [`CloudKit`](https://developer.apple.com/documentation/CloudKit) framework directly, or if your app uses Core Data to persist its data, leverage CloudKit to sync that data across devices. For more information, see [`Mirroring a Core Data store with CloudKit`](https://developer.apple.com/documentation/CoreData/mirroring-a-core-data-store-with-cloudkit).

iCloud Documents and CloudKit both use , although their purpose differs depending on the service. For iCloud Documents, a container — alternatively known as a  — serves as a local representation of the corresponding iCloud storage and is a specialized location on-disk where your app stores its files. For CloudKit, a container isolates your app’s databases on the iCloud servers and manages their access and operations. For more information, see [`CKContainer`](https://developer.apple.com/documentation/CloudKit/CKContainer). You can also use containers to share files and data between multiple apps belonging to the same developer.

Before you can enable an iCloud service, follow the steps in the [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) section of [`Adding capabilities to your app`](adding-capabilities-to-your-app.md) to add the capability to your app’s target, and select the iCloud capability from Xcode’s Capabilities library. For watchOS apps with separate WatchKit extensions, add the capability to the WatchKit Extension target. To access a public iCloud database in your App Clip, add the capability to your App Clip target and be sure to read [`Choosing the right functionality for your App Clip`](https://developer.apple.com/documentation/AppClip/choosing-the-right-functionality-for-your-app-clip) for more information about using iCloud services in your App Clip.

![A screenshot of Xcode’s Capabilities library with a list of available capabilities on the left and an information pane on the right. The list shows a range of capabilities from iCloud to Network Extensions, and the iCloud capability is in a selected state. The text on the information pane explains that the iCloud storage APIs enable your apps to store data and documents in iCloud, keeping your apps up to date automatically, and providing your users with a consistent and seamless experience across their iCloud-enabled devices.](https://docs-assets.developer.apple.com/published/8bcbe9e18681fa99d72a732b826ca708/icloud-services%402x.png)

After you add the iCloud capability, Xcode updates your target’s entitlements file to include the [`iCloud Container Identifiers Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.icloud-container-identifiers), which is an array that comprises the containers you select. If Xcode automatically manages your app’s signing, it also enables the iCloud capability for your app’s App ID in your developer account.

> **Note**: If you later remove the iCloud capability in Xcode, you must manually update your App ID’s configuration in your developer account to disable iCloud.

##### Enable One or More Icloud Services

Prior to using an iCloud service to sync your users’ data across their devices, you must enable that service in Xcode to add the necessary entitlements to your app’s entitlements file. Use the checkbox next to the service’s name in the Services section of the iCloud capability to enable that service.

![A screenshot of the iCloud capability after you add it to your target. The Key-value storage service is in an enabled state.](https://docs-assets.developer.apple.com/published/c0b9ac8ac16188b10123d3fc3488d6da/key-value-storage%402x.png)

Depending on the services you enable, Xcode adds the following additional entitlements (if they’re not already present).

| Service | Entitlement |
| --- | --- |
| Key-value storage | `com.apple.developer.ubiquity-kvstore-identifier` |
| iCloud Documents | `com.apple.developer.icloud-services` |
|  | `com.apple.developer.ubiquity-container-identifiers` |
| CloudKit | `com.apple.developer.icloud-services` |

For more information, see [`iCloud Key-Value Store Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.ubiquity-kvstore-identifier) and [`iCloud Services Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.icloud-services).

> **Note**: Xcode automatically adds the Push Notifications capability to your target if you enable the CloudKit service because CloudKit uses push notifications to inform your app of server-side changes to your data. For more information, see [`Remote Records`](https://developer.apple.com/documentation/CloudKit/remote-records).

##### Manage Your Apps Icloud Containers

After adding the iCloud capability, Xcode retrieves any existing iCloud containers from your developer account and displays them in the capability’s configuration section. Use the Refresh button below the list to re-fetch your account’s iCloud containers at any time.

![A screenshot of the iCloud capability after you add it to your target. The Key-value storage, iCloud Documents, and CloudKit services are each in a disabled state. The containers list displays three fetched iCloud containers, none of which are in an enabled state.](https://docs-assets.developer.apple.com/published/1bb11a948f39306d683947272c12f550/icloud-containers%402x.png)

Enable one or more iCloud containers in the list using their checkboxes. Conversely, uncheck a container’s checkbox to prevent your app from using it. Xcode associates the selected iCloud containers with your app’s App ID in your developer account and makes the following changes to your app’s entitlements file:

- For apps that enable iCloud Documents, or both iCloud Documents and CloudKit, Xcode updates the following entitlements to include the selected containers: - `com.apple.developer.icloud-container-identifiers`
- `com.apple.developer.ubiquity-container-identifiers`
- Xcode updates just the `com.apple.developer.icloud-container-identifiers` entitlement for apps that enable only CloudKit.

> **Note**: To avoid breaking existing versions of your app that depend on the container association, Xcode doesn’t automatically dissociate a deselected container from your App ID in your developer account.

To create a new iCloud container, perform the following steps:

1. Click the Add button (+) below the iCloud containers list.
2. Enter an iCloud container in the dialog that appears. You must begin the container’s name with `iCloud.` and use a unique string in reverse DNS notation.
3. Click OK to save the new iCloud container.

![A screenshot of the Add a new container dialog that appears after you click the Add button. The dialog’s text explains that Xcode will create a new container if the named container doesn’t already exist, add it to your App ID, and add the new container to your app’s entitlements.](https://docs-assets.developer.apple.com/published/900cc747a92eb9a4f70dc8ad8d9233eb/add-new-icloud-container%402x.png)

Xcode automatically registers the iCloud container in your developer account, adds it to your app’s entitlements file, and selects it in the list of containers, indicating that your app is now able to use the new container.

![A screenshot of the iCloud capability after you add it to your target. The iCloud Documents service is in an enabled state, and a single iCloud container is in a selected state.](https://docs-assets.developer.apple.com/published/648730c820dfdb595f4d3da084d8f7bc/selected-icloud-container%402x.png)

After selecting the required containers, update your app to perform one or more of following:

- For document-based apps, call [`url(forUbiquityContainerIdentifier:)`](https://developer.apple.com/documentation/foundation/filemanager/1411653-url) to determine the location of your app’s ubiquity container.
- For CloudKit apps, use [`init(identifier:)`](https://developer.apple.com/documentation/CloudKit/CKContainer/init(identifier:)) to initialize an instance of [`CKContainer`](https://developer.apple.com/documentation/CloudKit/CKContainer) that provides access to the container’s databases and executes operations against those databases.
- For Core Data apps that sync with CloudKit, use [`NSPersistentCloudKitContainerOptions`](https://developer.apple.com/documentation/CoreData/NSPersistentCloudKitContainerOptions) to configure your Core Data stack to use your new container.

##### Access the Cloudkit Console

If your app enables the CloudKit service, use the web-based CloudKit Console to manage all aspects of your app’s iCloud containers, including the schemas for their databases, operation logs, and performance telemetry. For more information, see [`Managing iCloud Containers with CloudKit Database App`](https://developer.apple.com/documentation/CloudKit/managing-icloud-containers-with-cloudkit-database-app).

Follow these steps to access the CloudKit Console:

1. Click the CloudKit Console button below the list of containers in the iCloud capability.
2. In the browser window that opens, sign in to the CloudKit Console using the same Apple Account as your developer account.

Alternatively, you can access the console directly at [`icloud.developer.apple.com`](https://developer.apple.comhttps://icloud.developer.apple.com).

## See Also

- [Configuring an associated domain](configuring-an-associated-domain.md)
  Create a two-way association between your app and your website to enable universal links, Handoff, App Clips, and shared web credentials.
- [Configuring app groups](configuring-app-groups.md)
  Enable communication and data sharing between multiple installed apps created by the same developer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/configuring-icloud-services)*