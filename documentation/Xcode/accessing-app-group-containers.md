# Accessing app group containers in your existing macOS app

**Framework**: Xcode

Ensure your app has app group container entitlements and macOS can authorize them.

#### Overview

In macOS 15 and later, app group containers offer [`System Integrity Protection`](https://developer.apple.comhttps://developer.apple.com/documentation/macos-release-notes/macos-15-release-notes#System-Integrity-Protection) for your app’s local files even if the app doesn’t have the App Sandbox capability. These app group containers limit access by apps that aren’t in the app group. Apps not in the app group that attempt to access locations within an app group or app data container, result in a user prompt that requests their authorization.

To ensure your apps that use app groups also include System Integrity Protection, you need to confirm they have the correct entitlements and macOS can authorize those entitlements. For more information on adding an app group to an app, see [`Configuring app groups`](configuring-app-groups.md).

Apps that can use app group containers include: main executables packaged in bundled structures, app extensions, App Clips, and XPC Services.

#### Add App Group Membership to Your App

Ensure that your app target lists all the app groups to which it belongs in the [`App Groups Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.application-groups). You can use Xcode to entitle your app for app groups. For more details, see [`Configuring app groups`](configuring-app-groups.md).

An app can belong to more than one app group, with these guidelines:

- Different developer teams can’t use the same app group.
- The same developer team can share the same app group for multiple apps and supporting processes signed by that team.

> ❗ **Important**: On macOS, it’s recommended that you use `group.` prefixed identifiers. The `<Developer team identifier>.<group name>` prefixed identifier is also supported with some limitations described in the “Use app groups that you don’t provision” section below.

##### Use Provisioned App Groups

If your app declares that it belongs to an app group that begins with `group.`, you need to include the group in your app’s provisioning profile.

Include all the restricted entitlements, including the app group entitlement, in the provisioning profile of the process; the values of these entitlements must match and account for any wildcards in the provisioning profile entitlements.

Provisioning profiles for macOS apps that you previously created might not include authorization for the app group entitlement. You can check whether macOS set the entitlements validated flag on your process at runtime by running the command `sudo launchctl procinfo <pid>` in Terminal:

```None
% sudo launchctl procinfo `pgrep <your app's executable file name>`
…
code signing info = valid
    …
    entitlements validated
…
```

Xcode automatically obtains new provisioning profiles if you check “Automatically manage signing” in the Signing & Capabilities editor for your app target, and set the `REGISTER_APP_GROUPS` build setting to `Yes`. To apply a provisioning profile to a daemon, or another executable file that you don’t distribute in a bundle, see [`Signing a daemon with a restricted entitlement`](signing-a-daemon-with-a-restricted-entitlement.md).

If you encounter any issues provisioning the app group entitlement properly, see  [`Diagnosing Issues with Entitlements`](https://developer.apple.com/documentation/BundleResources/diagnosing-issues-with-entitlements) for help diagnosing these issues.

##### Use App Groups That You Dont Provision

To use app groups that have the `<Developer team identifier>.<group name>` identifiers on macOS, you don’t need a provisioning profile. The system checks that the team identifier prefix matches the developer team identifier you use to sign the app. You also don’t need to register these app group identifiers on the Developer website. But, there are limitations to using these identifiers:

- `<Developer team identifier>.<group name>` is not supported on iOS, iPadOS, tvOS, visionOS, or watchOS.
- Keychain Access Groups doesn’t support the `<Developer team identifier>.<group name>` prefixed identifier. For more information, see [`Sharing access to keychain items among a collection of apps`](https://developer.apple.com/documentation/Security/sharing-access-to-keychain-items-among-a-collection-of-apps)

#### Access an App Group Container

When your app becomes a member of an app group, use FileManager APIs to get the path to the shared container. For more details on accessing that data, see [`Access an app group’s shared container`](configuring-app-groups#Access-an-app-groups-shared-container.md).

## See Also

- [Configuring Family Controls](configuring-family-controls.md)
  Add the Family Controls entitlement to enable parental control features in your app and its Screen Time API app extensions.
- [Configuring the hardened runtime](configuring-the-hardened-runtime.md)
  Protect the runtime integrity of your macOS app by restricting access to sensitive resources and preventing common exploits.
- [Configuring the macOS App Sandbox](configuring-the-macos-app-sandbox.md)
  Protect system resources and user data from compromised apps by restricting access to the file system, network connections, and more.
- [Configuring keychain sharing](configuring-keychain-sharing.md)
  Share keychain items between multiple apps belonging to the same developer.
- [Protecting local app data using containers on macOS](protecting-local-app-data-using-containers.md)
  Secure your app’s local storage data from unauthorized access and modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/accessing-app-group-containers)*