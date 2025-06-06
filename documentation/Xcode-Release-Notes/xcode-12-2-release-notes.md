# Xcode 12.2 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 12.2 includes SDKs for iOS 14.2, iPadOS 14.2, tvOS 14.2, watchOS 7.1, and macOS Big Sur 11. The Xcode 12.2 release supports on-device debugging for iOS 9 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 12.2 requires a Mac running macOS 10.15.4 or later.

##### General

###### New Features

- When bringing iPad apps to macOS using Mac Catalyst, you can now enable the “Optimize Interface for Mac” target setting to use native Mac controls and resolution. (56344940)
- Xcode’s scheme menu now includes an Any Mac destination for Mac schemes. This is a new build destination that builds each target in the scheme for all of their supported architectures, regardless of the native architecture of the local Mac. (62736613)
- Xcode now supports iOS, tvOS, and watchOS development on Macs with Apple silicon. (64317985, 65077539, 65701094)

###### Resolved Issues

- You can now upload an app for App Store submission or Developer ID notarization even if Xcode’s path contains a space. (69009477)

###### Known Issues

- Xcode doesn’t prevent you from selecting a macOS destination for an iOS app when the macOS destination doesn’t support the iOS app’s deployment target. (68261281, 68714781, 68948002) If you attempt to launch the app through Xcode on an unsupported macOS destination, Xcode displays the message “The app is incompatible with the current version of macOS. Please check the app’s deployment target.” : Change the iOS deployment target for the iOS app to a version supported by the macOS destination, or upgrade to a version of macOS that supports the iOS deployment target configured in the project. Xcode must be running on macOS 11 or later to build an app with an iOS 14 or later deployment target.

##### Build System

###### Resolved Issues

- When building on the command line, projects now build for all of their configured architectures instead of the first architecture in the list, when `ONLY_ACTIVE_ARCH` is set to `YES` and the `-destination` option to `xcodebuild` isn’t being used. (69242858)

##### Core Ml

###### Resolved Issues

- The Core ML editor’s Preview tab for sound classifier models now shows a classification result when you click on Listen. Also, when you add an audio file, clicking the Play button updates the timeline as the file plays. (67515312)

##### Create Ml

###### New Features

- You can explore and interact with models during training using the new Training Control. You can pause, save, resume, or extend the training process. This feature requires macOS 11 or later. (45241965)
- You can train deep neural networks to stylize photos and videos in real time using the new Style Transfer template. This template requires macOS 11 or later. (55848835)
- You can train neural networks to classify a single person’s actions in a video clip using the new Action Classification template. This template requires macOS 11 or later. (56622350)
- You can improve model accuracy when training data is limited using the Object Detection template’s new Transfer Learning option. This feature requires macOS 11 or later. (58627183)
- The Word Tagger template’s new Transfer Learning option uses dynamic word embeddings to help improve model accuracy when training data is limited. This feature requires macOS 11 or later. (59281335)

##### Debugging

###### Resolved Issues

- Improved Xcode’s error message for app-launch failures when attempting to launch multiple instances of an app built with Mac Catalyst, or an iOS app on Mac, with the same bundle identifier. (66691875)
- Fixed an issue where Quick Look popovers for variables in the Xcode debugger were sometimes too small and truncated their contents. (67580519)

###### Known Issues

- Xcode fails to install an app with multibyte UTF-8 characters in its bundle name, and presents an error of “failed to hardlink copy”. (69887557) (FB8766413) : Use only uppercase letters (A-Z), lowercase letters (a-z), hyphens (-), underscores(__), and spaces in an app’s bundle name. By default, an app’s bundle name matches its target name, which you can change in the project editor. Note that this issue doesn’t impact an app’s Bundle ID or Bundle Display Name, only the name of the app’s `.app` folder on disk, which isn’t usually seen by users.
- When running in macOS 11, Xcode’s navigators lay out at the wrong sizes. The breakpoint navigator may not display the state of the breakpoint, and the breakpoint editor popover may never become visible. (70063096)  Use macOS 11.0.1 or later.

##### Devices

###### Known Issues

- Xcode may spontaneously lose device configuration information for an Apple Watch. This may cause Xcode to crash or display an error stating that your app “cannot be installed on (null)”. (54768855) : On the Mac you’re using for development, run the following command in Terminal: ```shell
sudo killall -9 usbmuxd
``` After running this command, restart Xcode.
- Xcode 11 and 12 may fail to prepare a wirelessly connected iOS device for debugging with the error “Failed _shouldMakeReadyForDevelopment check”. Even if Xcode prepares the device successfully, the Devices and Simulators window may continue to display stale errors for the device’s status. (61227501) (FB7649607) : Keep the wirelessly connected iOS device unlocked while deploying or debugging an app on the device. Restart Xcode if you want to clear stale device preparation errors. Whenever possible, use a USB cable instead of a wireless connection between your Mac and iOS device.
- Xcode may fail to copy symbols from iOS devices, and fail to prepare the devices for debugging, then take several minutes to attach to the debugger and reach breakpoints that would normally be reached immediately on launch. (68221778) (FB8611135) : Re-copy symbols from your devices by following these steps. 1. Disconnect all iOS devices from your Mac.
2. Delete this directory: `~/Library/Developer/Xcode/iOS DeviceSupport`
3. Open the Devices and Simulators window in Xcode.
4. Use a USB cable to connect any arm64e iOS devices (iPhone XS, iPhone XS Max, or later).
5. Wait for the Devices and Simulators window to finish copying symbols for these devices.
6. Use a USB cable to connect any arm64 iOS devices and copy their symbols.
- After installing Xcode, you must reboot your Mac before you can use `rvictl`. (70403127)

###### Resolved Issues

- You can now debug a WatchKit App when an App Clip is added to its paired iOS App, even if that iOS App isn’t installed. (65784374, 70152797) (FB8065876)
- Fixed a crash that could occur when you click the View Device Logs button for a device you select in the Devices and Simulators window. (66303792, 70152877)

##### Documentation Viewer

###### Known Issues

- Xcode may crash when you open the Developer Documentation window if you install and run Xcode outside of `/Applications`. (70631583) : Move Xcode to `/Applications` and relaunch.

##### Interface Builder

###### New Features

- Interface Builder now supports Inline and Compact [`UIDatePicker`](https://developer.apple.com/documentation/UIKit/UIDatePicker) styles. (65085323) (FB7847821)

###### Resolved Issues

- Enabled safe area relative margins by default for navigation bars of [`UINavigationController`](https://developer.apple.com/documentation/UIKit/UINavigationController). For existing navigation controllers in storyboards, you can correct clipping by selecting the navigation bar in the controller, and enable Size Inspector > Safe Area Relative Margins. (66566017) (FB8269384)
- Fixed an issue that could cause an [`NSTableView`](https://developer.apple.com/documentation/AppKit/NSTableView) to lose its Source List style when deploying to macOS versions earlier than macOS 11. (67700315) (FB8525478)

##### Organizer

###### Resolved Issues

- You can now export a watchOS app for Ad Hoc or Development distribution with thinning enabled for “All compatible device variants”. (66637482)

##### Previews

###### New Features

- The action menu has a new “Embed…” menu item that lets you specify the type of View container in which to embed the selected view hierarchy. (51152198)
- The action menu has a new “Embed in ZStack” menu item. (56989502)
- Xcode provides SwiftUI previews for macOS Widget extensions. (57990060)
- The SwiftUI previews canvas now automatically shows and hides based on the presence of a [`PreviewProvider`](https://developer.apple.com/documentation/SwiftUI/PreviewProvider) in the file you’re editing. (67083504, 67693254)
- The Editor menu now includes Create Preview to create a [`PreviewProvider`](https://developer.apple.com/documentation/SwiftUI/PreviewProvider), and Create Library Item to create a [`LibraryContentProvider`](https://developer.apple.com/documentation/DeveloperToolsSupport/LibraryContentProvider). (67110969)

###### Resolved Issues

- Fixed an issue that prevented previews from loading in projects with non-ASCII characters in their names, or in symbols within the project. (57260388) (FB7451792)
- Previews correctly display interpolated strings, including for localized strings. (64278576)
- Fixed an issue that prevented previews from loading for code that contains multi-line string literals. (65735599)
- The canvas now displays error details when a preview fails to launch due to the underlying app crashing, such as when the app doesn’t have an [`EnvironmentObject`](https://developer.apple.com/documentation/SwiftUI/EnvironmentObject). (67955924)

###### Known Issues

- Using the device name “Mac Catalyst” in a SwiftUI [`PreviewDevice`](https://developer.apple.com/documentation/SwiftUI/PreviewDevice) modifier may cause the preview to fail to update. Instead, the banner displays the error “Cannot preview in this file – rendering service was interrupted”. (65305155) : Remove the `previewDevice` modifier and switch to the “My Mac” run destination.

##### Realitykit

###### Known Issues

- Xcode can’t build an app with Mac Catalyst if the app imports the RealityKit framework (70102384)

##### Signing and Distribution

###### New Features

- Xcode can now sign iOS apps for development or distribution to Macs with Apple silicon. You must register your Mac with Apple silicon on the [`Developer website`](https://developer.apple.comhttps://developer.apple.com) in order to run Mac, iPhone, or iPad apps. Registration requires your Mac’s hardware identifier, which you can find in Xcode’s error message or in the System Information app’s Hardware > Provisioning UDID field. Once you’ve registered your Mac, you can use Xcode’s automatic signing or manually sign apps to run on the device. (54476962, 65752056)
- Xcode can sign and provision an archived iOS app to run on your Mac with Apple silicon. Find the archive in the Organizer window, click on Distribute App, select either “Ad Hoc” or “Development”, choose your distribution options, select “Automatically manage signing”, and proceed through the remainder of the distribution assistant to create an IPA. Once you’ve created the IPA, you can transfer it to your Mac with Apple silicon, and double-click on it to install. During the app’s first launch, macOS prompts you to open the Security & Privacy preferences pane and enable the app. To see the launch button in the preferences pane, make sure your Mac is configured to only allow apps from the App Store and identified developers. (68513041, 68528315).

###### Resolved Issues

- Xcode automatic signing includes your registered Macs with Apple silicon in your provisioning profile when exporting an archive. (66857321)
- Xcode can now distribute an archive containing an App Clip even if the parent app’s application identifier doesn’t begin with a Team ID. (67401115) (FB8461092)

##### Simulator

###### New Features

- Simulated watchOS 7 devices support 64-bit processes. To verify watchOS projects are 64-bit clean in Simulator, make sure `ARCHS` is set to its default value. (54654060, 66352876) > **Note**: Projects must be 64-bit clean to run in Simulator on Macs with Apple silicon, which doesn’t support 32-bit code. Projects must be 64-bit clean to run in Simulator on Macs with Apple silicon, which doesn’t support 32-bit code.

###### Resolved Issues

- Fixed an issue that could cause apps linking against [`Core NFC`](https://developer.apple.com/documentation/CoreNFC) to crash with an error of “Library not loaded” from `dyld`. (67961203)

###### Known Issues

- Simulators may not be available when running command-line tools like `simctl` or `xcodebuild` from a non-root LaunchDaemon, or when launching as a different user from the current user (for example, with `sudo` or `launchctl`). (62188195)
- Simulator runtimes for iOS 13, tvOS 13, and watchOS 6 and earlier don’t work on the Developer Transition Kit. Preferences offers these runtimes for download, but creating a simulated device from one of these runtimes fails, claiming the runtime is unavailable. Other Macs with Apple silicon support a limited set of older simulator runtimes for iOS and tvOS. (66115743, 70472441) (FB8157217)

###### Deprecations

- Simulators for watchOS 6 or earlier aren’t supported on Macs with Apple silicon. (66352760)

##### Source Editor

###### Resolved Issues

- The source editor properly displays errors and warnings from Run Script build phases that use relative paths; clicking the issue in the Issues navigator takes you to the issue in the source editor. (43290386, 70152655) (FB5420750)

##### Storekit

###### Resolved Issues

- Fixed a crash that could occur when selecting “Subscription Options” in the StoreKit transaction manager. (68354368)

##### Swift

###### Resolved Issues

- Fixed a compiler crash that could occur when a function builder body contains an empty switch statement. This issue could also cause a SourceKit crash while typing a switch statement in a SwiftUI view body. (65983237) (FB8111944)
- Fixed a regression that caused property wrappers to leak objects during their initialization. (69023636)

###### Known Issues

- Compiling a project with Mac Catalyst that imports [`OSLog`](https://developer.apple.com/documentation/OSLog) from Swift may fail. (68597591)  Consider importing `os.log` and similar services directly, or guarding the `OSLog` import with a `targetEnvironment` compiler directive.

##### Swift Packages

###### Known Issues

- Swift Packages may not respect the “Build Active Architecture Only” project build setting when you try to build universal binaries. (64344067) : Use the “Any Mac”, “Any iOS Device (arm64)”, “Any watchOS Device”, or “Any tvOS Device” destination to build for all applicable devices.

##### Testing

###### Known Issues

- Xcode can’t run UI tests for an iOS app on Apple silicon. If the active scheme or test plan includes both unit and UI tests, Xcode skips the UI tests, and logs a message that the UI tests were skipped in the test-activity log. (60059698)
- Xcode doesn’t run iOS app tests in parallel on Apple silicon. The tests run sequentially instead. (60514529)
- iOS unit tests fail to launch on Apple silicon if the test target’s host application is set to None. (65309328) : In the General tab of the test target’s project settings, set the host application to an iOS application target.
- Test Runner fails to re-launch on older simulator runtimes when the test hangs and times out. (68288321) : Fix the test that is hanging, or use a newer simulator runtime version.

## See Also

- [Xcode 12.5.1 Release Notes](xcode-12_5_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.5 Release Notes](xcode-12_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.4 Release Notes](xcode-12_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.3 Release Notes](xcode-12_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.1 Release Notes](xcode-12_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.0.1 Release Notes](xcode-12_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12 Release Notes](xcode-12-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-12_2-release-notes)*