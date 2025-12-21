# Configuring Family Controls

**Framework**: Xcode

Add the Family Controls entitlement to enable parental control features in your app and its Screen Time API app extensions.

#### Overview

The Family Controls framework enables your app to use Screen Time API app extensions to implement parental controls through the Managed Settings and Device Activity frameworks. For more information on the Screen Time APIs, see [`Screen Time Technology Frameworks`](https://developer.apple.com/documentation/ScreenTimeAPIDocumentation).

To enable the Family Controls functionality, add the capability to your target. Xcode automatically updates your app target’s entitlements file to include the `com.apple.developer.family-controls` entitlement key set to `true`, and you can access the entitlement through the Apple Developer Program during development. Configure it for the App ID of your app and its Screen Time API app extensions under the Capabilities tab in [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list).

##### Add the Family Controls Capability to Your Target

To add the capability to your app’s target, follow the steps in the [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) section of [`Adding capabilities to your app`](adding-capabilities-to-your-app.md), then select Family Controls from Xcode’s Capabilities library. If you add a new target in your Xcode project using a Screen Time API extension template such as Device Activity Monitor, Device Activity Report, Shield Action, or Shield Configuration, Xcode enables Family Controls automatically. This capability is available on iOS and visionOS. ![A screenshot of Xcode’s Capabilities library with a list of available capabilities on the left and an information pane on the right. The list shows a range of capabilities from Family Controls (Development) to Group Activities. The Family Controls (Development) capability is in a selected state. The text on the information pane explains that this capability enables your app for parental controls, granting access to the Managed Settings and Device Activity frameworks in the Screen Time API.](https://docs-assets.developer.apple.com/published/6f3cffa69a2bae157e58fe192c8f75b4/configuring-family-controls-01%402x.png)

If you remove the Family Controls capability in Xcode, disable this capability for your app’s App ID in Certificates, Identifiers & Profiles, [`regenerate your provisioning profile`](https://developer.apple.comhttps://developer.apple.com/help/account/provisioning-profiles/edit-download-or-delete-profiles#regenerate-a-provisioning-profile), and re-sign your app with this profile.

##### Add the Family Controls Entitlement Key

When you add the Family Controls capability, Xcode automatically updates your app target’s entitlements file to include the `com.apple.developer.family-controls` entitlement key set to `true`:

```None
<plist>
    <dict>
        <key>com.apple.developer.family-controls</key>
        <true/>
    </dict>
</plist>
```

If your app target doesn’t include an entitlements file, remove then re-add the Family Controls capability.

##### Update Your Provisioning Profile

After you add the Family Controls capability to your app’s target in Xcode, generate a provisioning profile, and re-sign your app with the profile. Use automatic signing to let Xcode manage signing for you. If you use automatic signing, Xcode automatically enables Family Controls for your app’s App ID in [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list) and requests a new provisioning profile for your app. For more information, see [`Edit, download, or delete provisioning profiles`](https://developer.apple.comhttps://developer.apple.com/help/account/provisioning-profiles/edit-download-or-delete-profiles).

If you manually sign your app, enable the Family Controls capability for your app’s App ID in [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list), then [`regenerate your provisioning profile`](https://developer.apple.comhttps://developer.apple.com/help/account/provisioning-profiles/edit-download-or-delete-profiles#regenerate-a-provisioning-profile). For more information, see [`Enable app capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/identifiers/enable-app-capabilities). After you regenerate the profile, download it or select Download Profile from the Provisioning Profile dropdown menu in Xcode to install it. For more information, see [`Distributing your app to registered devices`](distributing-your-app-to-registered-devices.md).

If your app includes a Screen Time API extension, use the same steps to update the provisioning profile of the extension.

##### Request the Family Controls Entitlement

To distribute your app, you need an entitlement that enables distribution. When you submit your app to TestFlight and the App Store, request permission to use the [`Family Controls`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.family-controls) entitlement. This entitlement supports provisioning profiles for development, Ad Hoc, and App Store distribution. If your app includes a Screen Time API app extension, submit the same request for the extension.

## See Also

- [Configuring the hardened runtime](configuring-the-hardened-runtime.md)
  Protect the runtime integrity of your macOS app by restricting access to sensitive resources and preventing common exploits.
- [Configuring the macOS App Sandbox](configuring-the-macos-app-sandbox.md)
  Protect system resources and user data from compromised apps by restricting access to the file system, network connections, and more.
- [Configuring keychain sharing](configuring-keychain-sharing.md)
  Share keychain items between multiple apps belonging to the same developer.
- [Protecting local app data using containers on macOS](protecting-local-app-data-using-containers.md)
  Secure your app’s local storage data from unauthorized access and modification.
- [Accessing app group containers in your existing macOS app](accessing-app-group-containers.md)
  Ensure your app has app group container entitlements and macOS can authorize them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-family-controls)*