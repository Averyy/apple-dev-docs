# Creating distribution-signed code for macOS

**Framework**: Xcode

Sign Mac code for distribution using either Xcode or command-line tools.

#### Overview

Before shipping a software product for the Mac, you need to first create distribution-signed code, which is code that you package up and submit to either the Mac App Store or the notary service.  The way you do this depends on the type of your product and how you build it:

- If your product is a Mac app bundle, possibly containing nested code such as an app extension, that you build using Xcode, use Xcode to export a distribution-signed app.
- If your product isn’t an app, but you build it using Xcode, create an Xcode archive, and then manually export distribution-signed code from that archive.
- If you build your product using an external build system, such as `make`, add a manual signing step to your build system.

When you have distribution-signed code, package it for distribution. For more information, see [`Packaging Mac software for distribution`](packaging-mac-software-for-distribution.md).

> **Note**: If you use a third-party developer tool to build your app, consult its documentation for advice specific to that tool.

If you use a third-party developer tool to build your app, consult its documentation for advice specific to that tool.

#### Export an App From Xcode

If your product is a standalone app that you build with Xcode, follow these steps to export a distribution-signed app:

1. Build an Xcode archive from your project.
2. Export a distribution-signed app from that Xcode archive.

You can complete each step from the Xcode app or automate the steps using `xcodebuild`.

To create a distribution-signed app using the Xcode app:

1. Select your app’s scheme.
2. Choose Product > Archive.
3. In the Archives organizer, select the archive created in step 2.
4. Click Distribute App.
5. Choose the appropriate distribution method. For example, to create a notarized app that you send directly to your customers, choose Direct Distribution.
6. Click Distribute.

> **Note**: If the button says Distribute Content rather than Distribute App, your archive has multiple items in its `Products` directory.  To avoid copying a target’s product into the `Products` directory, set the Skip Install (`SKIP_INSTALL`) build setting for that target. Do this for every target that has output embedded in your app. For more information, see [`TN3110: Resolving generic Xcode archive issue`](https://developer.apple.com/documentation/Technotes/tn3110-resolving-generic-xcode-archive-issue).

If the button says Distribute Content rather than Distribute App, your archive has multiple items in its `Products` directory.  To avoid copying a target’s product into the `Products` directory, set the Skip Install (`SKIP_INSTALL`) build setting for that target. Do this for every target that has output embedded in your app. For more information, see [`TN3110: Resolving generic Xcode archive issue`](https://developer.apple.com/documentation/Technotes/tn3110-resolving-generic-xcode-archive-issue).

For more information about Xcode archives and the Archives organizer, see [`Distributing your app for beta testing and releases`](distributing-your-app-for-beta-testing-and-releases.md).

To export a distribution-signed app from the command line:

1. Run `xcodebuild` with the `archive` action to build and archive your app.
2. Run `xcodebuild` with the `exportArchive` action to export the distribution-signed app from the archive created in step 1.

For more information about `xcodebuild`, see its manual page.  For instructions on how to read a manual page, see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).  For information about the keys supported by the export options property list, run `xcodebuild` with the `-help` argument.

#### Export a Non App Product Built with Xcode

To archive a non-app product in Xcode, follow the steps in “Export an app from Xcode” above.

To export a distribution-signed product from the Xcode archive:

1. Copy the relevant components from the archive.
2. Sign those components manually.

The commands that you use depend on your project structure. For example, imagine your product is a daemon, but it also has an associated configuration app.  The configuration app has a share extension and an embedded framework to share code between the app and the extension. An archive of this product in Xcode has the following structure:

```None
DaemonWithApp.xcarchive/
  Info.plist
  Products/
    usr/
      local/
        bin/
          Daemon
    Applications/
      ConfigApp.app/
        Contents/
          embedded.provisionprofile
          Frameworks/
            Core.framework/
              …
          PlugIns/
            Share.appex/
              Contents/
                embedded.provisionprofile
                …
          …
  …
```

The `Products` directory contains two items: the daemon itself (`Daemon`) and the configuration app (`ConfigApp.app`). To sign this product, first copy these items out of the archive.

```None
% mkdir "to-be-signed"
% ditto "DaemonWithApp.xcarchive/Products/usr/local/bin/Daemon" "to-be-signed/Daemon"
% ditto "DaemonWithApp.xcarchive/Products/Applications/ConfigApp.app" "to-be-signed/ConfigApp.app" 
```

> ❗ **Important**: When you copy code, use `ditto` rather than `cp` because `ditto` preserves symlinks, which are critical to the structure of Mac frameworks. For more information on this structure, see [`Placing content in a bundle`](https://developer.apple.com/documentation/BundleResources/placing-content-in-a-bundle). Symlinks are also useful when dealing with nonstandard code structures.  For more details, see [`Embedding nonstandard code structures in a bundle`](embedding-nonstandard-code-structures-in-a-bundle.md).

When you copy code, use `ditto` rather than `cp` because `ditto` preserves symlinks, which are critical to the structure of Mac frameworks. For more information on this structure, see [`Placing content in a bundle`](https://developer.apple.com/documentation/BundleResources/placing-content-in-a-bundle). Symlinks are also useful when dealing with nonstandard code structures.  For more details, see [`Embedding nonstandard code structures in a bundle`](embedding-nonstandard-code-structures-in-a-bundle.md).

#### Identify the Code to Sign

To sign your product, first identify each code item that you need to sign. For example, in the `DaemonWithApp` product, there are four code items: `ConfigApp.app`, `Core.framework`, `Share.appex`, and `Daemon`.

For each code item, determine the following:

- Is it bundled code?
- Is it a main executable?

Bundled code is the main code within a bundle. If, for example, you have an app with a nested helper tool, there are two code items: the app and the helper tool. The app is considered bundled code, but the helper tool isn’t.

The following table shows the code items in the `DaemonWithApp` product and whether they’re bundled code or a main executable:

| Code item | Bundled code? | Main executable? |
| --- | --- | --- |
| ConfigApp.app | yes | yes |
| Core.framework | yes | no |
| Share.appex | yes | yes |
| Daemon | no | yes |

In some cases, it might not be obvious whether the code item is a main executable. To confirm, run the `file` command. A main executable says `Mach-O … executable` as the following example shows:

```None
% file "to-be-signed/ConfigApp.app/Contents/Frameworks/Core.framework/Versions/A/Core"
…
… Mach-O 64-bit dynamically linked shared library x86_64
…
% file "to-be-signed/ConfigApp.app/Contents/PlugIns/Share.appex/Contents/MacOS/Share"
…
… Mach-O 64-bit executable x86_64
…
```

`Core.framework` isn’t a main executable, but `Share.appex` is.

#### Determine the Signing Order

Sign code from the inside out.  That is, if component `A` depends on component `B`, sign `B` before you sign `A`.  For the `DaemonWithApp` example, sign the components in the following order:

1. `Core.framework`
2. `Share.appex `
3. `ConfigApp.app`

The app and daemon are independent, so you can sign them in either order.

#### Configure Your Entitlements

A code signature can include  — key-value pairs that grant an executable permission to use a service or technology. When macOS runs a process, it grants that process the entitlements that its executable’s code signature claims. For more information, see [`Entitlements`](https://developer.apple.com/documentation/BundleResources/Entitlements).

> ❗ **Important**: Don’t apply entitlements to library code.  It doesn’t do anything useful and can prevent your code from running.

Don’t apply entitlements to library code.  It doesn’t do anything useful and can prevent your code from running.

You apply entitlements to a main executable. If your main executable needs entitlements, create an `.entitlements` property list file, and add the key-value pairs for the entitlements that the executable claims.

If you build your product with Xcode, you might be able to use the `.entitlements` file that Xcode manages in your source code.  If not, create the `.entitlements` file yourself.

> ❗ **Important**: The entitlements file needs to be a property list in the standard XML format with LF line endings, no comments, and no byte-order mark (BOM).  If you’re not sure if your file conforms to these requirements, use `plutil` to convert it to the standard format.  For specific instructions, see [`Resolving common notarization issues`](https://developer.apple.com/documentation/Security/resolving-common-notarization-issues).

The entitlements file needs to be a property list in the standard XML format with LF line endings, no comments, and no byte-order mark (BOM).  If you’re not sure if your file conforms to these requirements, use `plutil` to convert it to the standard format.  For specific instructions, see [`Resolving common notarization issues`](https://developer.apple.com/documentation/Security/resolving-common-notarization-issues).

If you have a development-signed version of your program, you can print its entitlements using the `codesign` command-line tool, and use that information as the basis for your entitlements property list file as the following example shows:

```None
% codesign -d --entitlements - --xml "to-be-signed/ConfigApp.app" | plutil -convert xml1 -o - -
…
<dict>
  <key>com.apple.application-identifier</key>
  <string>[Your Team ID].com.example.apple-samplecode.DaemonWithApp.App</string>
  <key>com.apple.developer.team-identifier</key>
  <string>[Your Team ID]</string>
  <key>com.apple.security.app-sandbox</key>
  <true/>
  <key>keychain-access-groups</key>
  <array>
    <string>[Your Team ID].com.example.apple-samplecode.DaemonWithApp.SharedKeychain</string>
  </array>
</dict>
</plist>
```

If you use the entitlements from a development-signed version of your program to create the entitlements property list file for your distribution-signed code, consider the following changes to the entitlements:

- Change the value of [`APS Environment (macOS) Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.aps-environment) from `development` to `production`.
- The `com.apple.security.get-task-allow` entitlement allows the debugger to attach to your program, so you rarely apply it to a distribution-signed program. For more information, see [`Resolving common notarization issues`](https://developer.apple.com/documentation/Security/resolving-common-notarization-issues).

For any other entitlement, see the documentation for that specific entitlement in [`Entitlements`](https://developer.apple.com/documentation/BundleResources/Entitlements).

#### Configure Your Designated Requirements

A code signature includes a designated requirement (DR) that macOS uses to identify the code.  For example, macOS uses the DR to track access to privacy-protected resources like the microphone.  For more information, see [`TN3127: Inside Code Signing: Requirements`](https://developer.apple.com/documentation/Technotes/tn3127-inside-code-signing-requirements).

When you sign code with the `codesign` tool, it applies a default DR.  The default DR works well for most products, with one notable exception: The default DR for a Mac App Store app and a Developer ID-signed app are not mutually compatible.  If you distribute two variants of your app, one on the Mac App Store and one that you distribute directly using Developer ID signing, then, by default, those variants don’t share access to privacy-protected resources.

To share access to privacy-protected resources across variants, sign the variants with mutually compatible DRs.  For advice on how to craft these DRs, see [`TN3127: Inside Code Signing: Requirements`](https://developer.apple.com/documentation/Technotes/tn3127-inside-code-signing-requirements).

If you decide to use a custom DR, save it to a requirements file.  Mutually compatible DRs include a code-signing identifier.  If your product has multiple code items, copy this requirements file for each code item and update the code-signing identifier to match that of the code.

#### Embed Distribution Provisioning Profiles

For security reasons, a provisioning profile needs to authorize most entitlement claims. For example, the `keychain-access-groups` entitlement requires authorization by a provisioning profile. This stops other developers from distributing apps that impersonate your app to access its confidential keychain items.

macOS allows programs to claim certain entitlements without such authorization.  These unrestricted entitlements include:

- `com.apple.security.get-task-allow`
- `com.apple.security.application-groups`
- Entitlements that enable and configure the [`App Sandbox`](https://developer.apple.com/documentation/Security/app-sandbox)
- Entitlements that configure the [`Hardened Runtime`](https://developer.apple.com/documentation/Security/hardened-runtime)

If your program claims a restricted entitlement, include a distribution provisioning profile to authorize that claim as follows:

1. Create the profile on the developer website. For more information, see [`Developer Account Help`](https://developer.apple.comhttps://help.apple.com/developer-account/). Make sure to choose a profile type that matches your distribution channel (Mac App Store or Developer ID).
2. Copy that profile into your program’s bundle. For more information, see [`Placing content in a bundle`](https://developer.apple.com/documentation/BundleResources/placing-content-in-a-bundle).

If your product includes a nonbundled executable that uses a restricted entitlement, package that executable in an app-like structure.  For more information, see [`Signing a daemon with a restricted entitlement`](signing-a-daemon-with-a-restricted-entitlement.md).

In the `DaemonWithApp` example, the configuration app and its share extension use a keychain access group to share secrets. The system grants the programs access to that group based on their `keychain-access-groups` entitlement claim, and a provisioning profile needs to authorize such claims. The app and the share extension each have their own profile. To distribute the app, update the app and share extension bundles with the corresponding distribution provisioning profile.

```None
% cp "ConfigApp-Dist.provisionprofile" "to-be-signed/ConfigApp.app/Contents/embedded.provisionprofile"
% cp "Share-Dist.provisionprofile" "to-be-signed/ConfigApp.app/Contents/PlugIns/Share.appex/Contents/embedded.provisionprofile"
```

Modifying the app in this way breaks the seal on its code signature.  You re-sign the app before you distribute it.

> ❗ **Important**: If you build your product with Xcode, you might find that Xcode embeds a provisioning profile within your bundle.  This is a development provisioning profile.  Replace it with a distribution provisioning profile.

If you build your product with Xcode, you might find that Xcode embeds a provisioning profile within your bundle.  This is a development provisioning profile.  Replace it with a distribution provisioning profile.

#### Confirm Your Code Signing Identity

The code you copy from the Xcode archive is typically signed using a development code-signing identity.

```None
% codesign -d -vv to-be-signed/Daemon
…
Authority=Apple Development: …
…
```

To ship a product that you signed for development, you need to re-sign it for distribution using an appropriate code-signing identity.  Choose one of the following identities for your distribution channel:

- To distribute an app on the Mac App Store, use an Apple Distribution code-signing identity.  This is named `Apple Distribution: <Team Name> (<Team ID>)`, where `<Team Name>` and `<Team ID>` identifies your team.
- To distribute a product independently, use a Developer ID Application code-signing identity.  This is named `Developer ID Application: <Team ID>`, where `<Team ID>` identifies your team.

For information on how to set up these code-signing identities, see [`Developer Account Help`](https://developer.apple.comhttps://help.apple.com/developer-account/).

To confirm that your code-signing identity is present and correct, run the following command:

```None
% security find-identity -p codesigning -v
  1) A06E7F3F8237330EE15CB91BE1A511C00B853358 "Apple Distribution: …"
  2) ADC03B244F4C1018384DCAFFC920F26136F6B59B "Developer ID Application: …"
     2 valid identities found
```

The `-p codesigning` argument filters for code-signing identities. The `-v` argument filters for valid identities only.  If the code-signing identity that you need isn’t listed, see [`Developer Account Help`](https://developer.apple.comhttps://help.apple.com/developer-account/).

Each output line includes a SHA-1 hash that uniquely identifies the identity. If you have multiple identities with the same name, sign your code using this hash rather than the identity name.

#### Sign Each Code Item

For all code types, the basic `codesign` command looks like the following:

```None
% codesign -s <CodeSigningIdentity> <PathToExecutable>
```

Replace `<CodeSigningIdentity>` with the name of the code-signing identity to use, and replace `<PathToExecutable>` with the path to the code to sign.

The specific identity you use for `<CodeSigningIdentity>` depends on your distribution channel, as discussed in “Confirm your code-signing identity” above.

> **Note**: If you have multiple identities with the same name, supply the identity’s SHA-1 hash to specify it unambiguously.  For information on how to get this hash, see “Confirm your code-signing identity” above.

If you have multiple identities with the same name, supply the identity’s SHA-1 hash to specify it unambiguously.  For information on how to get this hash, see “Confirm your code-signing identity” above.

If you’re re-signing code — that is, the code you’re signing is already signed — add the `-f` option.

If you’re signing a main executable that needs entitlements, add the `--entitlements <entitlementsPath>` option, where `<entitlementsPath>` is the path to the entitlements file that you created for that executable.

If you’re signing for Developer ID distribution, add the `--timestamp` option to include a secure timestamp.

If you’re signing a main executable for Developer ID distribution, add the `-o runtime` option to enable the Hardened Runtime.  For more information about the Hardened Runtime, see [`Hardened Runtime`](https://developer.apple.com/documentation/Security/hardened-runtime).

If you’re signing nonbundled code, add the `-i <BundleID>` option to set the code-signing identifier, where `<BundleID>` is the bundle ID the code would have if it had a bundle ID.  For example, for an app with a  bundle ID of `com.example.flying-animals` that has a nested command-line tool called `pig-jato`, you can use `com.example.flying-animals.pig-jato` as the bundle ID for the command-line tool.

> **Note**: For bundled code, you don’t need to supply a code-signing identifier because `codesign` defaults to using the bundle ID.

For bundled code, you don’t need to supply a code-signing identifier because `codesign` defaults to using the bundle ID.

If you’re using a custom DR, add the `-r <ReqPath>` option, where `<ReqPath>` is the path to the requirements file containing the DR for this code item.

Repeat this signing step for every code item in your product, in the order you established in “Determine the signing order” above. If you have a complex product with many code items to sign, create a script to automate this process.

The folloiwng code shows the complete sequence of commands to sign the `DaemonWithApp` example for Developer ID distribution:

```None
% codesign -s "Developer ID Application" -f --timestamp "to-be-signed/ConfigApp.app/Contents/Frameworks/Core.framework"
to-be-signed/ConfigApp.app/Contents/Frameworks/Core.framework: replacing existing signature
% codesign -s "Developer ID Application" -f --timestamp -o runtime --entitlements "Share.entitlements" "to-be-signed/ConfigApp.app/Contents/PlugIns/Share.appex"
to-be-signed/ConfigApp.app/Contents/PlugIns/Share.appex: replacing existing signature
% codesign -s "Developer ID Application" -f --timestamp -o runtime --entitlements "ConfigApp.entitlements" "to-be-signed/ConfigApp.app"
to-be-signed/ConfigApp.app: replacing existing signature
% codesign -s "Developer ID Application" -f --timestamp -o runtime -i "com.example.apple-samplecode.DaemonWithApp.Daemon" "to-be-signed/Daemon"
to-be-signed/Daemon: replacing existing signature
```

> ❗ **Important**:  Don’t run `codesign` using `sudo` because `codesign` relies on information in your user account when it signs code. Using tools like `sudo` to change user accounts causes problems when `codesign` tries to access this information.

 Don’t run `codesign` using `sudo` because `codesign` relies on information in your user account when it signs code. Using tools like `sudo` to change user accounts causes problems when `codesign` tries to access this information.

#### Avoid Deep Code Signing

Don’t pass the `--deep` option to `codesign` when you sign code.  This option is helpful in some specific circumstances (for example, in verifying a code signature), but it causes the following problems when signing a complex product:

- The `--deep` option applies the same code-signing options to every code item that it signs. For example, if you have an app with an embedded command-line tool, where the app and the tool need different entitlements, `codesign --deep` applies the same entitlements to both.
- `codesign` only signs nested code when you use the `--deep` option if that code is in particular locations in the top-level bundle. If you put code in a place where `codesign` expects to find data, `codesign --deep` doesn’t sign it. For information on the correct organization of nested code within a bundle, see [`Placing content in a bundle`](https://developer.apple.com/documentation/BundleResources/placing-content-in-a-bundle).

## See Also

- [Using the latest code signature format](using-the-latest-code-signature-format.md)
  Update legacy app code signatures so your app runs on current OS releases.
- [Notarizing macOS software before distribution](../Security/notarizing-macos-software-before-distribution.md)
  Give users even more confidence in your macOS software by submitting it to Apple for notarization.
- [Signing a daemon with a restricted entitlement](signing-a-daemon-with-a-restricted-entitlement.md)
  Wrap a daemon in an app-like structure to use an entitlement thatʼs authorized by a provisioning profile.
- [Synchronizing code signing identities with your developer account](sharing-your-teams-signing-certificates.md)
  Ensure you and other team members can sign your organization’s code and installer packages in Xcode.
- [TN3125: Inside Code Signing: Provisioning Profiles](../Technotes/tn3125-inside-code-signing-provisioning-profiles.md)
  Learn how provisioning profiles enable third-party code to run on Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-distribution-signed-code-for-the-mac)*