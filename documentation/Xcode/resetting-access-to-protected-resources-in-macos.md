# Resetting access to protected resources in macOS

**Framework**: Xcode  
**Role**: Article

Use Terminal to remove your app’s authorization access to protected resources during testing.

#### Overview

The first time your app attempts to access a protected resource such as Reminders or the microphone, the system prompts the person for permission. After the person grants or denies your app’s request for access, the system remembers their choice. For more information, see [Requesting access to protected resources](../UIKit/requesting-access-to-protected-resources.md).

During development, you might need the system to prompt the person for permission again — to test your app’s onboarding experience, verify that your purpose strings appear correctly in every language you support, or reproduce a bug that only occurs before the person grants access. To make the system prompt the person again, use the `tccutil reset` command in Terminal. The `tccutil reset` command requires a service, each protected resource has a service name. By default, the command affects only your current user account. To reset access for all user accounts on your Mac, run the command with `sudo`. To learn more about `tccutil`, enter `man tccutil` in Terminal.

#### Reset access

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

#### Look up a service name

The `<service>` argument accepts the following values. When applicable, each entry includes the privacy usage description key to add to your app’s `Info.plist`.

- **`All`**: To reset access to every protected resource listed below.
- **`Accessibility`**: To reset access to Accessibility features.
- **`AddressBook`**: To reset access to Contacts. Privacy usage description key: [`NSContactsUsageDescription`](../BundleResources/information-property-list/nscontactsusagedescription.md).
- **`AppleEvents`**: To reset access for sending Apple Events. Privacy usage description key: [`NSAppleEventsUsageDescription`](../BundleResources/information-property-list/nsappleeventsusagedescription.md).
- **`AudioCapture`**: To reset access for capturing system audio. Privacy usage description key: [`NSAudioCaptureUsageDescription`](../BundleResources/information-property-list/nsaudiocaptureusagedescription.md).
- **`BluetoothAlways`**: To reset access to Bluetooth. Privacy usage description key: [`NSBluetoothAlwaysUsageDescription`](../BundleResources/information-property-list/nsbluetoothalwaysusagedescription.md).
- **`Calendar`**: To reset access to Calendar. Privacy usage description keys: [`NSCalendarsWriteOnlyAccessUsageDescription`](../BundleResources/information-property-list/nscalendarswriteonlyaccessusagedescription.md) and [`NSCalendarsFullAccessUsageDescription`](../BundleResources/information-property-list/nscalendarsfullaccessusagedescription.md).
- **`Camera`**: To reset access to the camera. Privacy usage description key: [`NSCameraUsageDescription`](../BundleResources/information-property-list/nscamerausagedescription.md).
- **`DeveloperTool`**: To reset access to Developer Tools, which lets apps run code that is unsigned or noncompliant with the system’s security policy.
- **`EnergyKitGuidance`**: To reset access to EnergyKit for energy usage guidance and monitoring.
- **`ExternalCameraMedia`**: To reset access to external camera devices and their media content.
- **`FileProviderDomain`**: To reset access to files that a file provider manages. Privacy usage description key: [`NSFileProviderDomainUsageDescription`](../BundleResources/information-property-list/nsfileproviderdomainusagedescription.md).
- **`FileProviderPresence`**: To reset access for a file provider to determine which files the person is accessing. Privacy usage description key: [`NSFileProviderPresenceUsageDescription`](../BundleResources/information-property-list/nsfileproviderpresenceusagedescription.md).
- **`FocusStatus`**: To reset access to a person’s focus status. Privacy usage description key: [`NSFocusStatusUsageDescription`](../BundleResources/information-property-list/nsfocusstatususagedescription.md).
- **`GameCenterFriends`**: To reset access to the Game Center friends list. Privacy usage description key: [`NSGKFriendListUsageDescription`](../BundleResources/information-property-list/nsgkfriendlistusagedescription.md).
- **`HomeKit`**: To reset access to HomeKit. Privacy usage description key: [`NSHomeKitUsageDescription`](../BundleResources/information-property-list/nshomekitusagedescription.md).
- **`ListenEvent`**: To reset access to Input Monitoring.
- **`MediaLibrary`**: To reset access to the Apple Music library. Privacy usage description key: [`NSAppleMusicUsageDescription`](../BundleResources/information-property-list/nsapplemusicusagedescription.md).
- **`Microphone`**: To reset access to the microphone. Privacy usage description key: [`NSMicrophoneUsageDescription`](../BundleResources/information-property-list/nsmicrophoneusagedescription.md).
- **`Motion`**: To reset access to the device’s motion data. Privacy usage description key: [`NSMotionUsageDescription`](../BundleResources/information-property-list/nsmotionusagedescription.md).
- **`Photos`**: To reset access to Photos. Privacy usage description key: [`NSPhotoLibraryUsageDescription`](../BundleResources/information-property-list/nsphotolibraryusagedescription.md).
- **`PhotosAdd`**: To reset access for adding photos to the Photos library. Privacy usage description key: [`NSPhotoLibraryAddUsageDescription`](../BundleResources/information-property-list/nsphotolibraryaddusagedescription.md).
- **`PostEvent`**: To reset access for sending keystrokes.
- **`Reminders`**: To reset access to Reminders. Privacy usage description key: [`NSRemindersFullAccessUsageDescription`](../BundleResources/information-property-list/nsremindersfullaccessusagedescription.md).
- **`RemoteDesktop`**: To reset access to Remote Desktop.
- **`ScreenCapture`**: To reset access to Screen Recording.
- **`Siri`**: To reset access to Siri. Privacy usage description key: [`NSSiriUsageDescription`](../BundleResources/information-property-list/nssiriusagedescription.md).
- **`SpeechRecognition`**: To reset access to Speech Recognition. Privacy usage description key: [`NSSpeechRecognitionUsageDescription`](../BundleResources/information-property-list/nsspeechrecognitionusagedescription.md).
- **`SystemPolicyAllFiles`**: To reset access to all files (Full Disk Access).
- **`SystemPolicyAppBundles`**: To reset access to app bundles. Privacy usage description key: [`NSAppBundlesUsageDescription`](../BundleResources/information-property-list/nsappbundlesusagedescription.md).
- **`SystemPolicyAppData`**: To reset access to files in other apps’ sandbox containers. Privacy usage description key: [`NSAppDataUsageDescription`](../BundleResources/information-property-list/nsappdatausagedescription.md).
- **`SystemPolicyDesktopFolder`**: To reset access to files in the person’s Desktop folder. Privacy usage description key: [`NSDesktopFolderUsageDescription`](../BundleResources/information-property-list/nsdesktopfolderusagedescription.md).
- **`SystemPolicyDocumentsFolder`**: To reset access to files in the person’s Documents folder. Privacy usage description key: [`NSDocumentsFolderUsageDescription`](../BundleResources/information-property-list/nsdocumentsfolderusagedescription.md).
- **`SystemPolicyDownloadsFolder`**: To reset access to files in the person’s Downloads folder. Privacy usage description key: [`NSDownloadsFolderUsageDescription`](../BundleResources/information-property-list/nsdownloadsfolderusagedescription.md).
- **`SystemPolicyNetworkVolumes`**: To reset access to files on a network volume. Privacy usage description key: [`NSNetworkVolumesUsageDescription`](../BundleResources/information-property-list/nsnetworkvolumesusagedescription.md).
- **`SystemPolicyRemovableVolumes`**: To reset access to files on a removable volume. Privacy usage description key: [`NSRemovableVolumesUsageDescription`](../BundleResources/information-property-list/nsremovablevolumesusagedescription.md).
- **`SystemPolicySysAdminFiles`**: To reset access to system configuration files. Privacy usage description key: [`NSSystemAdministrationUsageDescription`](../BundleResources/information-property-list/nssystemadministrationusagedescription.md).
- **`UserTracking`**: To reset access to tracking data for the person or device. Privacy usage description key: [`NSUserTrackingUsageDescription`](../BundleResources/information-property-list/nsusertrackingusagedescription.md).
- **`VirtualMachineNetworking`**: To reset access to networking for virtual machines.
- **`VoiceBanking`**: To reset access to Personal Voice and voice banking.
- **`WebBrowserPublicKeyCredential`**: To reset access to public key credentials (passkeys and WebAuthn) in web browsers.

## See Also

### Debugging
- [Locating a missing debug symbol file](./locating-a-missing-debug-symbol-file.md)
  Find the debug symbol file (`.dSYM`) required to decode the hexadecimal address from a crash report.
- [Acquiring operating system symbol information](./acquiring-operating-system-symbol-information.md)
  Download symbols for Apple system frameworks using Xcode or Terminal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/resetting-access-to-protected-resources-in-macos)*