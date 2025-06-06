# Signing a daemon with a restricted entitlement

**Framework**: Xcode

Wrap a daemon in an app-like structure to use an entitlement thatʼs authorized by a provisioning profile.

#### Overview

Some APIs are usable from a daemon but require that the daemon claim a restricted entitlement thatʼs authorized by a provisioning profile. For example, the [`Endpoint Security`](https://developer.apple.com/documentation/EndpointSecurity) API is usable from a daemon but requires that the daemon has the [`com.apple.developer.endpoint-security.client`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.endpoint-security.client) entitlement, and that it’s authorized by a provisioning profile. This is problematic because a daemon is a standalone executable, so you canʼt embed a provisioning profile in it. To get around this limitation, wrap your daemon in an app-like structure.

> ❗ **Important**: If the API youʼre using supports system extensions, avoid this issue by switching from a daemon to a system extension. System extensions readily support provisioning profiles, and Xcode automatically creates and embeds the profile in that case.

If the API youʼre using supports system extensions, avoid this issue by switching from a daemon to a system extension. System extensions readily support provisioning profiles, and Xcode automatically creates and embeds the profile in that case.

##### Create a Minimal Daemon Project

The basic idea is to create an app target, rather than a command-line tool target, and then remove all of the app-specific content and replace it with your daemon code. To start, create a new project with an app target by choosing File > New > Project and selecting the macOS > App template. Set the Interface popup to Storyboard, the Life Cycle popup (if present) to AppKit App Delegate, and the Language popup to Swift.

> **Note**: This example uses Swift but this approach works just fine if you choose Objective-C.

This example uses Swift but this approach works just fine if you choose Objective-C.

In the General tab of the target editor, ensure that the Bundle Identifier field has the right value.  This is important because your provisioning profile is tied to your App ID, and the bundle identifier is a key part of that App ID.

Also, clear the Deployment Info > Main Interface field and set the App Icons > Source popup to “Donʼt use asset catalogs”.

Switch to the Signing & Capabilities tab and configure it as follows:

- Ensure that “Automatically manage signing” is set.
- Select your team in the Team popup.
- Remove the App Sandbox capability (if present).  The App Sandbox is, as the name suggests, not appropriate for daemons.
- Add the Hardened Runtime capability, which youʼll need to notarize your daemon.
- Add the Custom Network Protocol capability, which enables the `com.apple.developer.networking.custom-protocol` entitlement that must be authorized by a provisioning profile. Adding it to your target triggers Xcodeʼs automatic code-signing machinery to register your App ID, create a provisioning profile for that App ID, and embed that provisioning profile in the built product.

> ❗ **Important**: If your ultimate goal is to use the [`com.apple.developer.endpoint-security.client`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.endpoint-security.client) entitlement, first add the Custom Network Protocol capability to force Xcode to register your App ID and generate an initial provisioning profile. Then follow the instructions on [`Provisioning with managed capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities) to add the Endpoint Security additional capability to your App ID.  Finally, remove the Custom Network Protocol capability, assuming your daemon doesn’t need it for other reasons.

If your ultimate goal is to use the [`com.apple.developer.endpoint-security.client`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.endpoint-security.client) entitlement, first add the Custom Network Protocol capability to force Xcode to register your App ID and generate an initial provisioning profile. Then follow the instructions on [`Provisioning with managed capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities) to add the Endpoint Security additional capability to your App ID.  Finally, remove the Custom Network Protocol capability, assuming your daemon doesn’t need it for other reasons.

Switch to the Build Settings tab and remove the Enable App Sandbox (`ENABLE_APP_SANDBOX`) build setting, if present.

Switch to the Info tab and delete all the app-specific items ([`NSPrincipalClass`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSPrincipalClass), [`NSMainStoryboardFile`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMainStoryboardFile), [`NSSupportsSuddenTermination`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSupportsSuddenTermination), `NSSupportsAutomaticTermination`, and [`CFBundleIconFile`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIconFile)).  Some of these items may not be present, depending on the exact version of Xcode youʼre using.

In the Project navigator, remove the `AppDelegate.swift`, `ViewController.swift`, `Assets.xcassets`, and `Main.storyboard` files.

Add a `main.swift` file and populate it with your daemon code.  For a minimal daemon, use this:

```swift
import Foundation

/// A helper for calling the Security framework from Swift.

func secCall<Result>(_ body: (_ resultPtr: UnsafeMutablePointer<Result?>) -> OSStatus  ) throws -> Result {
    var result: Result? = nil
    let err = body(&result)
    guard err == errSecSuccess else {
        throw NSError(domain: NSOSStatusErrorDomain, code: Int(err), userInfo: nil)
    }
    return result!
}

func main() throws {
    let me = try secCall { SecCodeCopySelf([], $0) }
    let meStatic = try secCall { SecCodeCopyStaticCode(me, [], $0) }
    let infoCF = try secCall { SecCodeCopySigningInformation(meStatic, [], $0) }
    let info = infoCF as NSDictionary
    let entitlements = info[kSecCodeInfoEntitlementsDict] as? NSDictionary
    NSLog("entitlements: %@", entitlements ?? [:])
}

try! main()
```

This code logs the current processʼs entitlements, which is a good way to confirm that youʼre set up correctly.

Build and run the daemon from Xcode.  The program logs its entitlements:

```None
2021-08-04 16:24:10.979941+0100 DaemonInAppsClothing[50219:4886989] entitlements: {
    "com.apple.application-identifier" = "SKMME9E2Y8.com.example.apple-samplecode.DaemonInAppsClothing";
    "com.apple.developer.networking.custom-protocol" = 1;
    "com.apple.developer.team-identifier" = SKMME9E2Y8;
    "com.apple.security.get-task-allow" = 1;
}
```

The final structure of your daemon should look like this:

```None
DaemonInAppsClothing.app/
  Contents/
    Info.plist
    MacOS/
      DaemonInAppsClothing
    PkgInfo
    _CodeSignature/
      CodeResources
    embedded.provisionprofile
```

Note the presence of the embedded provisioning profile; itʼs this profile that authorizes your daemon to use the `com.apple.developer.networking.custom-protocol` entitlement.

##### Test Your Daemon

To properly test your daemon, run it in a daemon context.  First, copy the built daemon to a secure location:

```None
% sudo mkdir "/Library/Application Support/DaemonInAppsClothing"
% sudo cp -R "DaemonInAppsClothing.app" "/Library/Application Support/DaemonInAppsClothing/"
```

Now create a `launchd` property list file that points to the daemonʼs main executable:

```None
% /usr/libexec/PlistBuddy -c "Add :Label string com.example.apple-samplecode.DaemonInAppsClothing" "com.example.apple-samplecode.DaemonInAppsClothing.plist"
File Doesn't Exist, Will Create: com.example.apple-samplecode.DaemonInAppsClothing.plist
% /usr/libexec/PlistBuddy -c 'Add :Program string "/Library/Application Support/DaemonInAppsClothing/DaemonInAppsClothing.app/Contents/MacOS/DaemonInAppsClothing"' "com.example.apple-samplecode.DaemonInAppsClothing.plist"
% cat com.example.apple-samplecode.DaemonInAppsClothing.plist 
…
<dict>
    <key>Label</key>
    <string>com.example.apple-samplecode.DaemonInAppsClothing</string>
    <key>Program</key>
    <string>/Library/Application Support/DaemonInAppsClothing/DaemonInAppsClothing.app/Contents/MacOS/DaemonInAppsClothing</string>
</dict>
</plist>
```

Copy that to `/Library/LaunchDaemons` and then load and start your daemon:

```None
% sudo cp com.example.apple-samplecode.DaemonInAppsClothing.plist /Library/LaunchDaemons 
% sudo launchctl load /Library/LaunchDaemons/com.example.apple-samplecode.DaemonInAppsClothing.plist 
% sudo launchctl start com.example.apple-samplecode.DaemonInAppsClothing                      
```

Run the Console app and look in the system log.  At the point when you started the daemon, youʼll see a log entry like this:

```None
entitlements: {
    "com.apple.application-identifier" = "SKMME9E2Y8.com.example.apple-samplecode.DaemonInAppsClothing";
    "com.apple.developer.networking.custom-protocol" = 1;
    "com.apple.developer.team-identifier" = SKMME9E2Y8;
    "com.apple.security.get-task-allow" = 1;
}
```

If you miss it, run the `launchctl start` command to start your daemon again.

##### Integrate Your Daemon Code

Now that you have a working minimal daemon, itʼs time to integrate your real daemon code into the project.  Add your code to the project as you would with any other Xcode project.  If necessary, replace `main.swift` with a C, C++, Objective-C, or Objective-C++ main entry point.

Or, if youʼre using an alternative build system, like a makefile, update it to create a structure that matches the one created by Xcode.

## See Also

- [Creating distribution-signed code for macOS](creating-distribution-signed-code-for-the-mac.md)
  Sign Mac code for distribution using either Xcode or command-line tools.
- [Using the latest code signature format](using-the-latest-code-signature-format.md)
  Update legacy app code signatures so your app runs on current OS releases.
- [Notarizing macOS software before distribution](../Security/notarizing-macos-software-before-distribution.md)
  Give users even more confidence in your macOS software by submitting it to Apple for notarization.
- [Synchronizing code signing identities with your developer account](sharing-your-teams-signing-certificates.md)
  Ensure you and other team members can sign your organization’s code and installer packages in Xcode.
- [TN3125: Inside Code Signing: Provisioning Profiles](../Technotes/tn3125-inside-code-signing-provisioning-profiles.md)
  Learn how provisioning profiles enable third-party code to run on Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/signing-a-daemon-with-a-restricted-entitlement)*