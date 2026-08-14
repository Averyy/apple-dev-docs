# Resetting access to protected resources in macOS

**Framework**: Xcode

Use Terminal to remove your app’s authorization access to protected resources during testing.

#### Overview

The first time your app attempts to access a protected resource such as Reminders or the microphone, the system prompts the person for permission. After the person grants or denies your app’s request for access, the system remembers their choice. For more information, see [`Requesting access to protected resources`](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources).

During development, you might need the system to prompt the person for permission again — to test your app’s onboarding experience, verify that your purpose strings appear correctly in every language you support, or reproduce a bug that only occurs before the person grants access. To make the system prompt the person again, use the `tccutil reset` command in Terminal. The `tccutil reset` command requires a service, each protected resource has a service name. By default, the command affects only your current user account. To reset access for all user accounts on your Mac, run the command with `sudo`. To learn more about `tccutil`, enter `man tccutil` in Terminal.

#### Reset Access

To reset access to a specific protected resource for every app, enter `tccutil reset` with the service name:

```shell
% tccutil reset <service>
```

For example, the following command resets access to Calendar for every app:

```shell
% tccutil reset Calendar
```

The next time any app attempts to access Calendar, the system prompts the person for permission.

To reset access to a specific protected resource — in this case Calendar — for a single app, add the app’s bundle ID to the command:

```shell
% tccutil reset Calendar com.example.company
```

To reset access to all resources at once, pass `All` as the service name:

```shell
% tccutil reset All
```

The next time any app tries to access any protected resource, the system prompts the person for permission.

To reset access to all resources for a single app, add the app’s bundle ID:

```shell
% tccutil reset All com.example.company
```

#### Look Up a Service Name

The `<service>` argument accepts the following values. When applicable, each entry includes the privacy usage description key to add to your app’s `Info.plist`.

- **`All`**: To reset access to every protected resource listed below.
- **`Accessibility`**: To reset access to Accessibility features.
- **`AddressBook`**: To reset access to Contacts. Privacy usage description key: [`NSContactsUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nscontactsusagedescription).
- **`AppleEvents`**: To reset access for sending Apple Events. Privacy usage description key: [`NSAppleEventsUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsappleeventsusagedescription).
- **`AudioCapture`**: To reset access for capturing system audio. Privacy usage description key: [`NSAudioCaptureUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsaudiocaptureusagedescription).
- **`BluetoothAlways`**: To reset access to Bluetooth. Privacy usage description key: [`NSBluetoothAlwaysUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsbluetoothalwaysusagedescription).
- **`Calendar`**: To reset access to Calendar. Privacy usage description keys: [`NSCalendarsWriteOnlyAccessUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nscalendarswriteonlyaccessusagedescription) and [`NSCalendarsFullAccessUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nscalendarsfullaccessusagedescription).
- **`Camera`**: To reset access to the camera. Privacy usage description key: [`NSCameraUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nscamerausagedescription).
- **`DeveloperTool`**: To reset access to Developer Tools, which lets apps run code that is unsigned or noncompliant with the system’s security policy.
- **`EnergyKitGuidance`**: To reset access to EnergyKit for energy usage guidance and monitoring.
- **`ExternalCameraMedia`**: To reset access to external camera devices and their media content.
- **`FileProviderDomain`**: To reset access to files that a file provider manages. Privacy usage description key: [`NSFileProviderDomainUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsfileproviderdomainusagedescription).
- **`FileProviderPresence`**: To reset access for a file provider to determine which files the person is accessing. Privacy usage description key: [`NSFileProviderPresenceUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsfileproviderpresenceusagedescription).
- **`FocusStatus`**: To reset access to a person’s focus status. Privacy usage description key: [`NSFocusStatusUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsfocusstatususagedescription).
- **`GameCenterFriends`**: To reset access to the Game Center friends list. Privacy usage description key: [`NSGKFriendListUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsgkfriendlistusagedescription).
- **`HomeKit`**: To reset access to HomeKit. Privacy usage description key: [`NSHomeKitUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nshomekitusagedescription).
- **`ListenEvent`**: To reset access to Input Monitoring.
- **`MediaLibrary`**: To reset access to the Apple Music library. Privacy usage description key: [`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapplemusicusagedescription).
- **`Microphone`**: To reset access to the microphone. Privacy usage description key: [`NSMicrophoneUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsmicrophoneusagedescription).
- **`Motion`**: To reset access to the device’s motion data. Privacy usage description key: [`NSMotionUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsmotionusagedescription).
- **`Photos`**: To reset access to Photos. Privacy usage description key: [`NSPhotoLibraryUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsphotolibraryusagedescription).
- **`PhotosAdd`**: To reset access for adding photos to the Photos library. Privacy usage description key: [`NSPhotoLibraryAddUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsphotolibraryaddusagedescription).
- **`PostEvent`**: To reset access for sending keystrokes.
- **`Reminders`**: To reset access to Reminders. Privacy usage description key: [`NSRemindersFullAccessUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsremindersfullaccessusagedescription).
- **`RemoteDesktop`**: To reset access to Remote Desktop.
- **`ScreenCapture`**: To reset access to Screen Recording.
- **`Siri`**: To reset access to Siri. Privacy usage description key: [`NSSiriUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nssiriusagedescription).
- **`SpeechRecognition`**: To reset access to Speech Recognition. Privacy usage description key: [`NSSpeechRecognitionUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsspeechrecognitionusagedescription).
- **`SystemPolicyAllFiles`**: To reset access to all files (Full Disk Access).
- **`SystemPolicyAppBundles`**: To reset access to app bundles. Privacy usage description key: [`NSAppBundlesUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsappbundlesusagedescription).
- **`SystemPolicyAppData`**: To reset access to files in other apps’ sandbox containers. Privacy usage description key: [`NSAppDataUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsappdatausagedescription).
- **`SystemPolicyDesktopFolder`**: To reset access to files in the person’s Desktop folder. Privacy usage description key: [`NSDesktopFolderUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsdesktopfolderusagedescription).
- **`SystemPolicyDocumentsFolder`**: To reset access to files in the person’s Documents folder. Privacy usage description key: [`NSDocumentsFolderUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsdocumentsfolderusagedescription).
- **`SystemPolicyDownloadsFolder`**: To reset access to files in the person’s Downloads folder. Privacy usage description key: [`NSDownloadsFolderUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsdownloadsfolderusagedescription).
- **`SystemPolicyNetworkVolumes`**: To reset access to files on a network volume. Privacy usage description key: [`NSNetworkVolumesUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsnetworkvolumesusagedescription).
- **`SystemPolicyRemovableVolumes`**: To reset access to files on a removable volume. Privacy usage description key: [`NSRemovableVolumesUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsremovablevolumesusagedescription).
- **`SystemPolicySysAdminFiles`**: To reset access to system configuration files. Privacy usage description key: [`NSSystemAdministrationUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nssystemadministrationusagedescription).
- **`UserTracking`**: To reset access to tracking data for the person or device. Privacy usage description key: [`NSUserTrackingUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsusertrackingusagedescription).
- **`VirtualMachineNetworking`**: To reset access to networking for virtual machines.
- **`VoiceBanking`**: To reset access to Personal Voice and voice banking.
- **`WebBrowserPublicKeyCredential`**: To reset access to public key credentials (passkeys and WebAuthn) in web browsers.

## See Also

- [Locating a missing debug symbol file](locating-a-missing-debug-symbol-file.md)
  Find the debug symbol file (`.dSYM`) required to decode the hexadecimal address from a crash report.
- [Acquiring operating system symbol information](acquiring-operating-system-symbol-information.md)
  Download symbols for Apple system frameworks using Xcode or Terminal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/resetting-access-to-protected-resources-in-macos)*