# Configuring keychain sharing

**Framework**: Xcode  
**Role**: Article

Share keychain items between multiple apps belonging to the same developer.

#### Overview

Sharing keychain items between multiple targets of the same app, or between different apps that belong to the same developer, relies on the concept of an *access group* — a collection of targets that all share a common keychain group. When a particular target wants to make a keychain item accessible to the rest of the access group, it specifies the shared keychain group when writing that item to the keychain, which can be useful for apps that need to share account credentials and other sensitive information. For more information, see [Sharing access to keychain items among a collection of apps](../Security/sharing-access-to-keychain-items-among-a-collection-of-apps.md).

Before you make a keychain group accessible to your target, follow the steps in the [Add a capability](./adding-capabilities-to-your-app.md#Add-a-capability) section of [Adding capabilities to your app](./adding-capabilities-to-your-app.md) to add the Keychain Sharing capability to that target. For watchOS apps with separate WatchKit extensions, add the capability to the WatchKit Extension target.

![A screenshot of Xcode’s Capabilities library. The Keychain Sharing capability is in a selected state.](https://developer.apple.com/tutorials/images/com.apple.Xcode/keychain-sharing@2x.png)

If not already present, Xcode updates your target’s entitlements file to include the [`Keychain Access Groups Entitlement`](../BundleResources/entitlements/keychain-access-groups.md), which is an array that contains each keychain group you specify.

##### Make a keychain group accessible to your target

When you want two (or more) targets to share common keychain items, make the same keychain group accessible to both by following these steps:

1. Select your project in Xcode’s Project navigator.
2. Select the app’s target from the Targets list.
3. Click the Signing & Capabilities tab in the project editor.
4. Find the Keychain Sharing capability.
5. Click the Add button (+) below the Keychain Groups list.
6. Double-click the inserted keychain group to edit it.
7. Enter a name for the keychain group: either the name of an existing group that’s already in use by your other apps, or a brand new group. For new groups, use reverse DNS notation for the name.
8. Press the Return key to save the updated keychain group.

![A screenshot of the Keychain Sharing capability after you add it to your target. The keychain groups list contains a single group.](https://developer.apple.com/tutorials/images/com.apple.Xcode/keychain-groups@2x.png)

> **Note**: Although not visible, Xcode prepends the name of each keychain group with the `$(AppIdentifierPrefix)` build variable, which it automatically resolves at build time.

After you make a keychain group accessible to your target, you can later revoke that access by selecting the appropriate keychain group and clicking the Remove button (-) below the Keychain Groups list.

Keychain groups you specify are then available to use with the [Keychain services](../Security/keychain-services.md) APIs, such as [`SecItemAdd(_:_:)`](../Security/secitemadd%28_,_%29.md) and [`SecItemCopyMatching(_:_:)`](../Security/secitemcopymatching%28_,_%29.md).

##### Specify the default keychain group

During compilation, the system determines the canonical list of keychain groups accessible to your app by concatenating the groups you specify with the app’s unique application identifier and any App Groups you configure; the system considers the first item in that list as the default keychain group. If you omit the [`kSecAttrAccessGroup`](../Security/ksecattraccessgroup.md) attribute when writing keychain items, the system automatically populates that attribute with the default keychain group, and therefore the order in which you specify your keychain groups matters.

To change the order of your keychain groups, follow these steps:

1. In the Project navigator, Control-click your target’s entitlements file.
2. Choose Open As > Property List.
3. Expand the Keychain Access Groups key.
4. Drag the array’s nested items into your preferred order. Each item’s value is the name of a keychain group.

![A screenshot of an app’s entitlements file open in Xcode’s plist editor. The Keychain Access Groups key is in an expanded state and contains two items, each representing a different keychain group.](https://developer.apple.com/tutorials/images/com.apple.Xcode/keychain-groups-plist@2x.png)

After making changes to the order, choose File > Save to store those changes and cause Xcode to update the order it displays the groups in the target’s Signing & Capabilities tab.

> **Note**: Although you can use an App Group to share keychain items, it can never be the default keychain group because the app’s unique application identifier always takes precedence.

## See Also

### Security
- [Configuring Family Controls](./configuring-family-controls.md)
  Add the Family Controls entitlement to enable parental control features in your app and its Screen Time API app extensions.
- [Configuring the hardened runtime](./configuring-the-hardened-runtime.md)
  Protect the runtime integrity of your macOS app by restricting access to sensitive resources and preventing common exploits.
- [Configuring the macOS App Sandbox](./configuring-the-macos-app-sandbox.md)
  Protect system resources and user data from compromised apps by restricting access to the file system, network connections, and more.
- [Protecting local app data using containers on macOS](./protecting-local-app-data-using-containers.md)
  Secure your app’s local storage data from unauthorized access and modification.
- [Accessing app group containers in your existing macOS app](./accessing-app-group-containers.md)
  Ensure your app has app group container entitlements and macOS can authorize them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-keychain-sharing)*