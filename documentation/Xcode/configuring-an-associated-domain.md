# Configuring an associated domain

**Framework**: Xcode

Create a two-way association between your app and your website to enable universal links, Handoff, App Clips, and shared web credentials.

#### Overview

The system uses associated domains to initiate a secure association between your app and specific domains so they can share saved passwords, perform Handoff activities, and support universal links that allow users to open your app in a specific context and quickly complete their current task. To create such an association, you configure your app with the necessary entitlements by using Xcode to define associated domains, and then serve a special file from your web server that the system requires in order to verify those entitlements.

Before you can define associated domains and the services they provide, follow the steps in the [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) section of [`Adding capabilities to your app`](adding-capabilities-to-your-app.md) to add the capability to your app’s target, making sure you select the Associated Domains capability from Xcode’s Capabilities library. For watchOS apps with separate WatchKit extensions, add the capability to the WatchKit Extension target.

![A screenshot of Xcode’s Capabilities library with a list of available capabilities on the left and an information pane on the right. The list shows a range of capabilities from Associated Domains to FileProvider Testing Mode, and the Associated Domains capability is in a selected state. The text on the information pane explains that associated domains allow your app to associate with a specific domain for a specific service, such as accessing Safari saved password and activity continuation.](https://docs-assets.developer.apple.com/published/117997d21b6866c2bab5a72e614b2c35/associated-domains%402x.png)

If not already present, Xcode updates your target’s entitlements file to include the [`Associated Domains Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.associated-domains), which is an array that contains each associated domain you define. If you enable the “Automatically manage signing” option for your target, Xcode also updates your app’s App ID in your developer account and generates and downloads an updated provisioning profile.

> **Note**: If you later remove the Associated Domains capability in Xcode, you must manually update your App ID’s configuration in your developer account to fully disable the feature.

If you later remove the Associated Domains capability in Xcode, you must manually update your App ID’s configuration in your developer account to fully disable the feature.

##### Define a Service and Its Associated Domain

When you want your app and one or more of your websites to interact using predefined services, define an associated domain by performing the following steps. Xcode automatically updates the `com.apple.developer.associated-domains` array in your target’s entitlements file to include those you define.

1. Select your project in Xcode’s Project navigator.
2. Select the app’s target in the Targets list.
3. Click the Signing & Capabilities tab in the project editor.
4. Find the Associated Domains capability.
5. Click the Add button (+) to insert a service-domain placeholder.
6. Double-click the inserted placeholder to edit it.

Update the placeholder to contain the service your app supports and its associated domain, which must be in the following format:

```None
<service>:<fully qualified domain>
```

![A screenshot of the Associated Domains capability after you add it to your app’s target. The Domains list contains two associated domains; one for the applinks service and one for the appclips service.](https://docs-assets.developer.apple.com/published/a80ea5021f852cea27649f643086b76f/associated-domains-list%402x.png)

Only include the top-level domain and, where necessary, the subdomain; don’t include path and query components, or a trailing slash.

> 💡 **Tip**: For services other than App Clips, prefix a domain with `*.` to include all of its subdomains.

For services other than App Clips, prefix a domain with `*.` to include all of its subdomains.

The following table describes the services that associated domains support:

| Service | Description |
| --- | --- |
| `webcredentials` | If your domain supports shared web credentials, see [`Managing Shared Credentials`](https://developer.apple.com/documentation/Security/managing-shared-credentials) for more information. |
| `authsrv` | If your domain needs to authenticate people, see [`Authenticating a User Through a Web Service`](https://developer.apple.com/documentation/AuthenticationServices/authenticating-a-user-through-a-web-service) for more information. |
| `applinks` | If your domain supports universal links, see [`Supporting universal links in your app`](supporting-universal-links-in-your-app.md) for more information. |
| `activitycontinuation` | If your domain supports Handoff, see [`Web Browser-to-Native App Handoff`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Handoff/AdoptingHandoff/AdoptingHandoff.html#//apple_ref/doc/uid/TP40014338-CH2-SW10) for more information. |
| `appclips` | If your domain supports App Clips, see [`Associating your App Clip with your website`](https://developer.apple.com/documentation/AppClip/associating-your-app-clip-with-your-website) for more information. |

##### Provide an Apple App Site Association File

When the user installs your app that contains associated domains, the system fetches the corresponding  (AASA) file from an Apple-managed content delivery network (CDN) and uses its JSON contents to verify those associated domains. If the CDN doesn’t store a copy of that file, or has an outdated version, it automatically connects to your server and retrieves the latest version.

After you define your app’s associated domains in Xcode, you must create this file and serve it using HTTPS from your website’s `.well-known` directory. For more information, see [`Add the associated domain file to your website`](supporting-associated-domains#Add-the-associated-domain-file-to-your-website.md).

##### Enable Alternate Mode for Unreachable Servers

If you use a private web server while developing your app that’s unreachable from the public internet, enable  — an option you specify that allows the system to bypass Apple’s CDN and fetch the AASA file directly from your web server.

Follow these steps to enable alternate mode on a specific associated domain:

1. Select your project in Xcode’s Project navigator.
2. Select the app’s target in the Targets list.
3. Click the Signing & Capabilities tab in the project editor.
4. Find the Associated Domains capability.
5. Double-click the associated domain in the Domains list to edit it.
6. Append the string `?mode=<alternate mode>` to the associated domain. Replace `<alternate mode>` with one of the modes shown in the list below.
7. Press Return to save the updated associated domain.

![A screenshot of the Associated Domains capability after you add it to your app’s target. The Domains list contains a single associated domain that includes the developer alternate mode.](https://docs-assets.developer.apple.com/published/625b8058510f80792e47ae36ef3e6ded/alternate-mode%402x.png)

The following table describes the alternate modes that associated domains support:

| Mode | Description |
| --- | --- |
| `developer` | The domain is accessible from devices with Developer Mode enabled. You must sign the app with a development profile and users must opt-in on their device by enabling the Associated Domains Development option in Settings > Developer. |
| `managed` | The domain is accessible from devices using a mobile device management (MDM) profile and that have authorization from the MDM administrator. |
| `developer+managed` | The domain is accessible only from devices that are in both `developer` and `managed` modes. |

> ❗ **Important**: Only use alternate mode during development; you must remove the query string from the associated domains before you submit your app to the App Store.

Only use alternate mode during development; you must remove the query string from the associated domains before you submit your app to the App Store.

## See Also

- [Configuring app groups](configuring-app-groups.md)
  Enable communication and data sharing between multiple installed apps created by the same developer.
- [Configuring iCloud services](configuring-icloud-services.md)
  Share user or app data among multiple instances of your app running on different devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-an-associated-domain)*