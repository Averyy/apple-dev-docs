# Embedding a command-line tool in a sandboxed app

**Framework**: Xcode

Add a command-line tool to a sandboxed app’s Xcode project so the resulting app can run it as a helper tool.

#### Overview

When building an app for the Mac, you can embed a command-line tool in the app to act as a helper tool. Instances where this may be helpful include, for example:

- You want to run some code in a separate process. In many cases, an XPC service is a better choice for this, but sometimes it’s easier to embed a command-line tool.
- You want to build a command-line tool with an external build system (for example, `make`) and then run it from your app.

Embedding a command-line tool in a sandbox app does present some unique challenges. The best approach depends on whether you’re building the tool with Xcode or using a tool built by an external build system.

> **Note**: These steps assume that you’re building an app for the App Store because that’s the most common destination for sandboxed apps. However, the same basic process works for apps distributed independently using Developer ID signing; you just need to choose a different distribution path in the Xcode organizer.

##### Create the App Project

To get started, create a new project from the macOS > App template. Name it `AppWithTool`, resulting in a bundle ID like `com.example.apple-samplecode.AppWithTool`.

In the project editor, set the deployment target to 10.15. Later on, you’ll configure the tool target to inherit this deployment target, which helps to keep everything in sync.

In the General tab of the app target editor, set the App Category to Utilities. This avoids a warning when you build for distribution.

In the Signing & Capabilities tab of the app target editor, make sure “Automatically manage signing” is checked, and then select the appropriate team. The Signing Certificate popup should switch to Development, which is exactly what you want for day-to-day development.

Add the Hardened Runtime capability, which isn’t necessary for App Store apps but is best practice for new code.

Choose Product > Archive, which builds the app into an Xcode archive and reveals that archive in the Xcode organizer. The goal here is to check that everything is working so far.

In the organizer, delete the new archive, just to reset to the original state.

##### Create the Helper Tool Target

With the app target in the project building correctly, it’s time to create a helper tool target so you can embed its product into the app. To start, create a new target from the macOS > Command Line Tool template. Name this `ToolX`, where the  stands for .

In the General tab of the tool target editor, clear the Deployment Target field. This configures the tool target to inherit its deployment target (macOS 10.15) from the project.

In the Signing & Capabilities tab of the tool target editor, ensure that “Automatically manage signing” is checked, and then select the appropriate team. Again, the Signing Certificate popup switches to Development.

Fill in the Bundle Identifier field. The app’s bundle ID is `com.example.apple-samplecode.AppWithTool`, so set this to `com.example.apple-samplecode.AppWithTool.ToolX`. This value becomes the helper tool’s code signing identifier. See the discussion of the Other Code Signing Flags build setting, below.

Add the App Sandbox and Hardened Runtime capabilities. Again, the hardened runtime isn’t required for App Store apps, but it’s best practice for new code.

In the Build Settings tab, enable the Skip Install (`SKIP_INSTALL`) build setting. Without this setting, Xcode puts a standalone copy of the tool in your Xcode archive (in addition to the one embedded within your app). That copy of the tool causes problems when you try to distribute that archive.

Also, disable the Code Signing Inject Base Entitlements (`CODE_SIGN_INJECT_BASE_ENTITLEMENTS`) build setting. If you leave this setting enabled, then Xcode includes the `com.apple.security.get-task-allow` entitlement in development builds of your tool. This is problematic because that entitlement is incompatible with the `com.apple.security.inherit` entitlement.

> ❗ **Important**: The absence of the `com.apple.security.get-task-allow` entitlement means that you won’t be able to debug your tool. If you need to debug, create a new command-line tool target, one that’s not sandboxed, specifically for debugging. Be warned, however, that this target may behave differently from the normal tool target because it’s not running in a sandbox.

Set the Other Code Signing Flags (`OTHER_CODE_SIGN_FLAGS`) build setting to `$(inherited) -i $(PRODUCT_BUNDLE_IDENTIFIER)`, which ensures that the tool’s code signing identifier matches its bundle ID.

Select `ToolX.entitlements` in the Project navigator and add `com.apple.security.inherit` to it, with a Boolean value of `true`. For more information about this entitlement, see [`Enabling App Sandbox Inheritance`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW15).

Select the ToolX scheme and chose Product > Build, just to make sure that the tool builds correctly.

Now switch back to the app (`AppWithTool`) scheme.

##### Embed the Helper Tool

In the Build Phases tab of the app target editor, add the ToolX target to the Dependencies build phase. This ensures that Xcode builds the tool target before building the app target.

Add a new Copy Files build phase. Double-click the build phase name and change it to `Embed Helper Tools` (the exact name doesn’t matter, but it’s best to pick a descriptive one). Set the Destination popup to Executables.  This places the helper tool in your app’s `Contents/MacOS` directory, one of the locations recommended by [`Placing content in a bundle`](https://developer.apple.com/documentation/BundleResources/placing-content-in-a-bundle).

Add the `ToolX` executable to that build phase, making sure Code Sign On Copy is checked.

For more information about build phases, see [`What are build phases?`](https://developer.apple.comhttps://help.apple.com/xcode/mac/11.4/index.html#/dev50bab713d)

##### Build and Validate

With the project set up, it’s time to test that everything builds correctly. To start, choose Product > Archive, which builds the tool target and then the app target, embedding the result of the former within the latter.

In the Xcode organizer, select the newly created archive and click Distribute App.

> **Note**: If the button says Distribute Content rather than Distribute App, go back and check that you enabled the Skip Install build setting on the tool target.

Select App Store Connect and click Next, then select Export and click Next.

Go through the rest of the export workflow. The end result is a directory with a name like `AppWithTool 2021-05-17 14-07-21`. Within that directory is an installer package (with the `.pkg` extension). Unpack that package.

> **Note**: The easiest way to unpack an installer package is to install it. If you’d rather not install it, unpack it manually using `xar` and `cpio`. For more information, read the manual pages for these tools (see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages)).

Run the following commands to confirm that Xcode constructed everything correctly:

```None
% codesign -d -vvv --entitlements :- AppWithTool.app 
…
Identifier=com.example.apple-samplecode.AppWithTool
Format=app bundle with Mach-O universal (x86_64 arm64)
CodeDirectory v=20500 size=822 flags=0x10000(runtime) hashes=14+7 location=embedded
…
Authority=Apple Distribution: …
…
TeamIdentifier=SKMME9E2Y8
…
<dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.files.user-selected.read-only</key>
    <true/>
</dict>
</plist>
% codesign -d -vvv --entitlements :- AppWithTool.app/Contents/MacOS/ToolX 
…
Identifier=com.example.apple-samplecode.AppWithTool.ToolX
Format=Mach-O universal (x86_64 arm64)
CodeDirectory v=20500 size=796 flags=0x10000(runtime) hashes=13+7 location=embedded
…
Authority=Apple Distribution: …
…
TeamIdentifier=SKMME9E2Y8
…
<dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.inherit</key>
    <true/>
</dict>
</plist>
```

Check the following:

- The `Identifier` field is the code signing identifier.
- The `Format` field shows that the executable is universal.
- The `runtime` flag, in the `CodeDirectory` field, shows that the hardened runtime is enabled.
- The `Authority` field shows that the code was signed by an Apple Distribution signing identity, which is what you’d expect for an App Store submission.
- The `TeamIdentifier` field is your Team ID.
- The app’s entitlements include `com.apple.security.app-sandbox` and whatever other entitlements are appropriate for this app.
- The tool’s entitlements include just `com.apple.security.app-sandbox` and `com.apple.security.inherit`.

> ❗ **Important**: Adding other entitlements to the tool can cause problems. If the tool immediately crashes with a code signing error when your app runs the tool, check that the tool is signed with just these two entitlements: `com.apple.security.app-sandbox` and `com.apple.security.inherit`.

##### Embed an Externally Built Tool

With the app and Xcode-built helper tool working correctly, it’s time to repeat the process for a tool built using an external build system. The following example creates an example helper tool from the command line and then embeds the tool in the AppWithTool app. In a real project, you’d use the command-line tool’s external build system (for example, `make`) to build the tool that you want to embed.

##### Build the Tool

Create a new directory and change into it:

```None
% mkdir ToolC
% cd ToolC
```

Here  stands for .

Create a source file in the directory that looks like this:

```None
% cat main.c 
#include <stdio.h>

int main(int argc, char ** argv) {
    printf("Hello Cruel World!\n");
    return 0;
}
```

Build that source file with `clang` twice, once for each architecture, and then `lipo` them together:

```None
% clang -o ToolC-x86_64 -mmacosx-version-min=10.15 -arch x86_64 main.c
% clang -o ToolC-arm64 -mmacosx-version-min=11.0 -arch arm64 main.c
% lipo ToolC-x86_64 ToolC-arm64 -create -output ToolC 
```

The `-mmacosx-version-min` option sets the deployment target to match the AppWithTool app. For the Intel architecture, this is macOS 10.15, as discussed above. For the Apple silicon architecture, this is macOS 11.0, the first macOS release to support Apple silicon.

Create an entitlements file for the tool:

```None
% /usr/libexec/PlistBuddy -c "Add :com.apple.security.app-sandbox bool true" "ToolC.entitlements"
File Doesn't Exist, Will Create: ToolC.entitlements
% /usr/libexec/PlistBuddy -c "Add :com.apple.security.inherit bool true" ToolC.entitlements
% cat ToolC.entitlements 
…
<dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.inherit</key>
    <true/>
</dict>
</plist>
```

Sign the tool as shown below:

```None
% codesign -s - -i com.example.apple-samplecode.AppWithTool.ToolC -o runtime --entitlements ToolC.entitlements -f ToolC
```

This breaks down as follows:

- The `-s -` argument applies an ad hoc signature (in Xcode parlance, this is Sign to Run Locally). Setting up the code signature here is critical. It sets up a pattern that Xcode uses when it re-signs the tool when embedding it into the final app. The signing identity is the only thing that doesn’t matter. Xcode overrides that identity with the product’s signing identity during the embedding process, which is why you can get away with an ad hoc signature.
- The `-i com.example.apple-samplecode.AppWithTool.ToolC` option sets the code signing identifier.
- The `-o runtime` option enables the hardened runtime. Again, this isn’t necessary for App Store distribution, but it’s best practice for new code.
- The `--entitlements ToolC.entitlements` option supplies the signature’s entitlements.
- The `-f` option overrides any existing signature. This isn’t strictly necessary but it avoids any confusion about the existing ad hoc signature applied by `clang` to the `arm64` architecture. Apple silicon requires that all code be signed, and so `clang` automatically applies an ad hoc signature when building for Apple silicon.

Add the `ToolC` executable to your Xcode project. When you do this:

- Enable “Copy items if needed”.
- Select “Create groups” rather than “Create folder reference”.
- Uncheck all the boxes in the “Add to targets” list.

In the Build Phases tab of the app target editor, add `ToolC` to the Embed Helper Tools build phase, making sure that Code Sign On Copy is checked.

##### Build and Validate Again

To validate your work, follow the process described in [`Build and validate`](embedding-a-helper-tool-in-a-sandboxed-app#Build-and-validate.md), substituting `ToolC` for `ToolX` everywhere.

## See Also

- [Managing Your App’s Information Property List](../BundleResources/managing-your-app-s-information-property-list.md)
  Create and customize an information property list file for your app using Xcode.
- [Adding package dependencies to your app](adding-package-dependencies-to-your-app.md)
  Integrate package dependencies to share code between projects, or leverage code from other developers.
- [Creating a Mac version of your iPad app](../UIKit/creating-a-mac-version-of-your-ipad-app.md)
  Bring your iPad app to macOS with Mac Catalyst.
- [Setting up a watchOS project](../WatchKit/setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/embedding-a-helper-tool-in-a-sandboxed-app)*