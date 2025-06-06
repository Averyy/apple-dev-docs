# Using the latest code signature format

**Framework**: Xcode

Update legacy app code signatures so your app runs on current OS releases.

#### Overview

Before you distribute an app, you apply a code signature to it. The signature certifies that you are the app’s creator and enables the system to detect unwanted modifications — whether accidental or malicious — that happen after you sign your app. As a security measure, iOS refuses to launch an app that has a missing or invalid signature.

Starting in iOS 15, iPadOS 15, tvOS 15, and watchOS 8, the system checks for a new, more secure signature format that uses Distinguished Encoding Rules, or DER, to embed entitlements into your app’s signature. Apps signed with a previous signature format will not launch.

##### Determine Whether Your App Needs a New Signature

This change to DER embeddded entitlements  won’t affect most apps. For apps that you distribute through the App Store or TestFlight, App Store Connect first verifies your signature, and then re-signs the app using an Apple identity, before making the app available for download. Apps available through these channels already have the new signature format.

For apps that you distribute other ways, such as Ad Hoc or through the [`Apple Developer Enterprise Program`](https://developer.apple.comhttps://developer.apple.com/programs/enterprise), Xcode and the `codesign` utility have created signatures that use the new format for several years. If you signed your app on a Mac running macOS 10.14 through macOS 11, the app already has the new signature format, but your signature may not include the required DER entitlements. macOS 11 and later will sign app bundles with the new signature format that include the DER entitlements by default.

To check whether an app called `MyApp.app` has the new signature, you can use the [`codesign`](https://developer.apple.comx-man-page://1/codesign) utility:

```other
% codesign -dv /path/to/MyApp.app
```

Look in the output for a string such as `CodeDirectory v=20500`. For any value of `v` less than `20400`, you need to re-sign your app.

If the code directory value is 20400 or higher, and the app does not install on iOS 15, iPadOS 15, tvOS 15, or watchOS 8, confirm that the system has added DER entitlements to the app’s signature. Also confirm that you have correctly signed any nested code, for example, an app extension, a framework, or a bundled watchOS app.

To check whether the app has the DER entitlements, look for the hash list under Page size in the signature. If `-5` contains a value and `-7` contains a zero value, or is not present, you need to re-sign your app to include the new DER entitlements.

Valid signature:

```other
Page size=4096
     -7=f4c7c0ae394247097dca9b19333001200747691e1d9e25ec0cf0f35a8ade21f3
     -6=0000000000000000000000000000000000000000000000000000000000000000
     -5=7379374fd375633558fd972e33809c06e61f9f8191f67c71875899b0dc290945
     -4=0000000000000000000000000000000000000000000000000000000000000000
     -3=53cc3cc9830555e6d7bc864522fdf160b61ccc0d2fda9331368d333dfaa4fe24
```

Invalid signature:

```other
Page size=4096
     -5=7c741a970873bb7f6a05c1ad5b9425f4b5b1ac86645b2cb8c842a57f51818eb5
     -4=0000000000000000000000000000000000000000000000000000000000000000
     -3=f7ddc8d932def2f393dfc1719252e61b1561afeed76d32044ae0cd793e380bc6
     -2=904f563968898c7569794e19bcd9304d46ca5c0b9f09c792081bdb8ec9c04c92
```

##### Determine Whether Your App Needs a New Provisioning Profile

Starting in iOS 15, iPadOS 15, tvOS 15, and watchOS 8, apps that have entitlements, and that you build outside the com.apple.developer namespace, and are not included by default in a provisioning profile (including application-identifier or get-task-allow) may require a DER-encoded version of the provisioning profile. Beginning with Xcode 13, provisioning profiles are issued with DER encoding by default. If your app successfully installs, but doesn’t launch, your app needs to be re-signed with a new provisioning profile. For more information about DER encoded provisioning profiles, see [`Provisioning profile updates.`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-profiles/provisioning-profile-updates)

##### Re Sign Your App

If your app doesn’t have the new signature format, or is missing the DER entitlements in the signature, you’ll need to re-sign the app on a Mac running macOS 11 or later, which includes the DER encoding by default.

If you’re unable to use macOS 11 or later to re-sign your app, you can re-sign it from the command-line in macOS 10.14 and later. To do so, use the following command to re-sign the `MyApp.app` app bundle with DER entitlements by using a signing identity named “Your Codesign Identity” stored in the keychain:

```other
% codesign -s "Your Codesign Identity" -f --preserve-metadata --generate-entitlement-der /path/to/MyApp.app
```

For more information on using the codesign utility, see its [`codesign`](https://developer.apple.comx-man-page://1/codesign) via Terminal.

> ❗ **Important**: Only re-sign apps from the command-line as a last resort to update your code signature to include the DER entitlements. Re-signing apps from the command-line is not supported for iOS, iPadOS, tvOS, visionOS, and watchOS. It’s recommended that you to sign your app using macOS 11 or later as soon as you are able.

Only re-sign apps from the command-line as a last resort to update your code signature to include the DER entitlements. Re-signing apps from the command-line is not supported for iOS, iPadOS, tvOS, visionOS, and watchOS. It’s recommended that you to sign your app using macOS 11 or later as soon as you are able.

If your app contains nested code, such as an app extension, a framework, or a bundled watchOS app, sign each item separately, starting with the most deeply nested executable, and working your way out; then sign your main app last. Don’t include entitlements or profiles when signing frameworks. Including them produces an invalid code signature.

For general information about app distribution, see [`Distributing Your App for Beta Testing and Releases`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases).

## See Also

- [Creating distribution-signed code for macOS](creating-distribution-signed-code-for-the-mac.md)
  Sign Mac code for distribution using either Xcode or command-line tools.
- [Notarizing macOS software before distribution](../Security/notarizing-macos-software-before-distribution.md)
  Give users even more confidence in your macOS software by submitting it to Apple for notarization.
- [Signing a daemon with a restricted entitlement](signing-a-daemon-with-a-restricted-entitlement.md)
  Wrap a daemon in an app-like structure to use an entitlement thatʼs authorized by a provisioning profile.
- [Synchronizing code signing identities with your developer account](sharing-your-teams-signing-certificates.md)
  Ensure you and other team members can sign your organization’s code and installer packages in Xcode.
- [TN3125: Inside Code Signing: Provisioning Profiles](../Technotes/tn3125-inside-code-signing-provisioning-profiles.md)
  Learn how provisioning profiles enable third-party code to run on Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/using-the-latest-code-signature-format)*