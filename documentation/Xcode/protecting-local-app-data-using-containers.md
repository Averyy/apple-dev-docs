# Protecting local app data using containers on macOS

**Framework**: Xcode  
**Role**: Article

Secure your app’s local storage data from unauthorized access and modification.

#### Overview

[App Sandbox](../Security/app-sandbox.md) provides automatic protection for your app’s data. App data containers that the system creates for apps that have the App Sandbox capability offer [System Integrity Protection](https://support.apple.com/en-us/102149), which helps prevent potentially malicious software from modifying protected files and folders.

In macOS 15 and later, app group containers also offer System Integrity Protection for local files for an app even if it doesn’t have the App Sandbox capability. These app group containers limit access by any app that doesn’t belong to the app group. Any app not in the app group that attempts to access locations protected by an app group or app data container, results in a prompt to the user to authorize access. For more information, see the System Integrity Protection section of [macOS Sequoia 15 Release Notes](../macos-release-notes/macos-15-release-notes.md).

> ❗ **Important**: Use an app group container as the primary local storage location for any app that doesn’t have the App Sandbox capability, to help protect private data. These apps include: main executables packaged in a bundle structure, app extensions, App Clips, system extensions, and XPC services.

#### Add app group membership to your app

Follow the steps in [Configuring app groups](./configuring-app-groups.md) to add the [`App Groups Entitlement`](../BundleResources/entitlements/com.apple.security.application-groups.md) to your app’s target. Multiple apps and supporting processes signed by the same developer team may share the same app group.

See [Diagnosing Issues with Entitlements](../BundleResources/diagnosing-issues-with-entitlements.md) for information on diagnosing any issues you encounter when you add the app groups entitlement.

#### Access an app group container

When your app becomes a member of an app group, there are a number of APIs you can use to read and write data to that group’s shared container. See  [Access an app group’s shared container](./configuring-app-groups.md#Access-an-app-groups-shared-container) for more details.

## See Also

### Security
- [Configuring Family Controls](./configuring-family-controls.md)
  Add the Family Controls entitlement to enable parental control features in your app and its Screen Time API app extensions.
- [Configuring the hardened runtime](./configuring-the-hardened-runtime.md)
  Protect the runtime integrity of your macOS app by restricting access to sensitive resources and preventing common exploits.
- [Configuring the macOS App Sandbox](./configuring-the-macos-app-sandbox.md)
  Protect system resources and user data from compromised apps by restricting access to the file system, network connections, and more.
- [Configuring keychain sharing](./configuring-keychain-sharing.md)
  Share keychain items between multiple apps belonging to the same developer.
- [Accessing app group containers in your existing macOS app](./accessing-app-group-containers.md)
  Ensure your app has app group container entitlements and macOS can authorize them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/protecting-local-app-data-using-containers)*