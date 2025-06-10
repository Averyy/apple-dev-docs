# Determining whether to bring your app to visionOS

**Framework**: visionOS

Decide whether to bring your existing iPadOS or iOS app to visionOS.

#### Overview

If you have an existing app that runs in iPadOS or iOS and you want to bring it to visionOS, you can choose to either run your compatible app as-is or create a visionOS-specific version.

visionOS supports most of the same technologies as iOS, so many apps built to run on iPad or iPhone can run unmodified on Apple Vision Pro. When a compatible app runs in visionOS, it retains the same appearance it has in iPadOS or iOS, and its content appears in a window in the person’s surroundings. Apps built specifically for visionOS adopt the standard system appearance, look more natural on the platform, and support 3D content and immersive experiences.

The visionOS SDK has many differences from the iOS SDK. Frameworks and features might behave differently or be unavailable when your app runs in visionOS. Use this article to ensure your app behaves as you expect on every platform.

#### Decide Whether Your App Suits the Platform

In some cases, you may decide your app is not well-suited to visionOS due to platform differences. For example, consider the following types of apps:

-  This includes apps where the primary purpose is to deliver custom keyboard extensions, device drivers, sticker packs, SMS and MMS message-filtering extensions, call directory extensions, or widgets.
-  This includes apps that follow a person’s location changes, such as apps that offer turn-by-turn directions or navigation.
-  This includes apps where the primary purpose is to capture images or video from the device’s cameras. The device cameras are unavailable, but continuity camera and persona capture are available on Apple Vision Pro.

#### Opt Out of Running on Visionos

If you don’t want your app to run on Apple Vision Pro, change your app’s availability in App Store Connect:

1. Select your app in App Store Connect.
2. Navigate to the Pricing and Availability information.
3. Disable the “Make this app available on Apple Vision Pro” option.

When you remove your app’s availability for Apple Vision Pro, the App Store stops making your iOS app available for visionOS. People who already downloaded your app on their Vision Pro can still run it in visionOS, but they can’t download it again and won’t receive any updates. This setting doesn’t affect the version of your app built natively using the visionOS SDK.

For information on managing your app’s availability for Apple Vision Pro, see [`Manage availability of iPhone and iPad apps on Apple Vision Pro`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-of-iphone-and-ipad-apps-on-apple-vision-pro).

#### Run As a Compatible App on Visionos

visionOS runs compatible iPad and iPhone apps by linking against the iOS SDK to provide continuous access to existing content right away. visionOS supports most of the same technologies as iOS, so many apps built to run on iPad or iPhone can run unmodified on Apple Vision Pro. Read [`Making your existing app compatible with visionOS`](making-your-app-compatible-with-visionos.md) to learn how to make your app run successfully as a compatible app in visionOS.

#### Create a Visionos Version of Your App

Apps built specifically for visionOS adopt the standard system appearance, and they look more natural on the platform. Creating a version of your app specifically for visionOS gives you the opportunity to add elements that work well on the platform, such as 3D content and immersive experiences. Read [`Bringing your existing apps to visionOS`](bringing-your-app-to-visionos.md) for more information on how to modify your app to run successfully as a visionOS app and how to update your interface to take advantage of visionOS-specific elements.

#### Check Framework Availability in Visionos

The following frameworks are deprecated in their entirety in both iOS and visionOS. If your app still uses these frameworks, stop using them immediately. The reference documentation for each framework includes information about how to update your code.

- [`Accounts`](https://developer.apple.com/documentation/Accounts)
- [`Address Book`](https://developer.apple.com/documentation/AddressBook)
- [`Address Book UI`](https://developer.apple.com/documentation/AddressBookUI)
- [`Assets Library`](https://developer.apple.com/documentation/AssetsLibrary)
- [`GLKit`](https://developer.apple.com/documentation/GLKit)
- [`iAd`](https://developer.apple.com/documentation/iAd)
- Newsstand Kit
- [`Notification Center`](https://developer.apple.com/documentation/NotificationCenter)

> ❗ **Important**: visionOS removed many deprecated symbols entirely, turning these deprecation warnings into missing-symbol errors on the platform.

Here’s a list of frameworks and features that behave differently in visionOS:

-  Available on iOS only. Check the [`areActivitiesEnabled`](https://developer.apple.com/documentation/ActivityKit/ActivityAuthorizationInfo/areActivitiesEnabled) property of [`ActivityAuthorizationInfo`](https://developer.apple.com/documentation/ActivityKit/ActivityAuthorizationInfo) to determine if Live Activities are authorized.
-  visionOS hides AirPlay sharing buttons in system interfaces, and you can’t use AirPlay features from compatible apps.
-  visionOS doesn’t load App Clips, device drivers, device activity monitors, keyboard extensions, Messages app extensions, photo-editing app extensions, SMS and call-reporting extensions, or widgets.
-  visionOS ignores watchOS apps and WatchKit extensions in your iOS or iPadOS app. Face sharing in [`ClockKit`](https://developer.apple.com/documentation/ClockKit) does nothing in visionOS.
-  This framework requires you to use different APIs for iOS and visionOS, as visionOS can’t display windows that contain ARKit views. Check the [`isSupported`](https://developer.apple.com/documentation/ARKit/ARConfiguration/isSupported) property of your configuration object to determine availability of augmented reality features. In visionOS, ARKit views such as  [`ARView`](https://developer.apple.com/documentation/RealityKit/ARView) are never available, so isolate interface code containing those views to the iOS version of your app. For information about how to bring an ARKit app to visionOS, see [`Bringing your ARKit app to visionOS`](bringing-your-arkit-app-to-visionos.md).
-  visionOS doesn’t support Picture in Picture or AV routing features. Check the availability of video features before using them. Be prepared for audio playback to stop automatically when your app moves to the background.
-  Check for error values when you configure an [`AEAssessmentSession`](https://developer.apple.com/documentation/AutomaticAssessmentConfiguration/AEAssessmentSession) object. The framework returns an error if you try to start a test in visionOS.
-  Identify what cameras are available using the [`AVCaptureDevice.DiscoverySession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/DiscoverySession) class. Don’t assume the presence of specific cameras. Capture interfaces aren’t available in visionOS. Use availability checks to determine which services are present.
-  You can still implement Voice-over-IP (VoIP) services using [`CallKit`](https://developer.apple.com/documentation/CallKit) and [`Core Telephony`](https://developer.apple.com/documentation/CoreTelephony). Phone number verification, call-blocking, and other cellular-related services are unavailable.
-  Use the [`CNContactStore`](https://developer.apple.com/documentation/Contacts/CNContactStore) class to determine your app’s authorization status.
-  Use the [`CBCentralManager`](https://developer.apple.com/documentation/CoreBluetooth/CBCentralManager) and [`CBPeripheralManager`](https://developer.apple.com/documentation/CoreBluetooth/CBPeripheralManager) classes to determine feature availability and your app’s authorization status.
-  visionOS plays audio feedback instead of haptic feedback. Call the [`capabilitiesForHardware()`](https://developer.apple.com/documentation/CoreHaptics/CHHapticEngine/capabilitiesForHardware()) method of the haptic engine to determine the available features.
-  You can request location using the standard location service, but most other services are unavailable. Use availability checks to determine which services are present. The Always authorization level is unavailable and automatically becomes When in Use authorization. Check the properties of [`CLLocationManager`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager) to determine the availability of location services.
-  Barometer data is unavailable, but most other sensors are available. Use availability checks to determine which sensors you can use. Check the properties of [`CMMotionManager`](https://developer.apple.com/documentation/CoreMotion/CMMotionManager) to determine the availability of accelerometers, gyroscopes, magnetometers, and other hardware sensors.
-  Check the [`readingAvailable`](https://developer.apple.com/documentation/CoreNFC/NFCReaderSession-swift.class/readingAvailable) property of your reader session to determine if NFC tag reading is available.
-  Calls to the [`ManagedSettings`](https://developer.apple.com/documentation/ManagedSettings) and [`ManagedSettingsUI`](https://developer.apple.com/documentation/ManagedSettingsUI) frameworks do nothing in visionOS.
-  Use the [`EKEventStore`](https://developer.apple.com/documentation/EventKit/EKEventStore) class to determine your app’s authorization status.
-  Use the [`ENManager`](https://developer.apple.com/documentation/ExposureNotification/ENManager) class to determine your app’s authorization status.
-  visionOS delivers game controller events only when someone is looking at your app. To require a game controller as an input device, add the [`GCRequiresControllerUserInteraction`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCRequiresControllerUserInteraction) key with the visionOS value to your app’s `Info.plist`.
-  visionOS doesn’t attempt to hand off user activities to other devices.
-  You can’t add accessories using a QR code from Apple Vision Pro. Check the properties of [`HMHomeManager`](https://developer.apple.com/documentation/HomeKit/HMHomeManager) to determine your app’s authorization status.
-  Use the [`LAContext`](https://developer.apple.com/documentation/LocalAuthentication/LAContext) class to determine the authentication policies you can use.
-  User-tracking features that involve heading information aren’t available in visionOS.
-  Some APIs are unavailable in visionOS. Use the [`MPMediaLibrary`](https://developer.apple.com/documentation/MediaPlayer/MPMediaLibrary) class to determine your app’s authorization status.
-  You can use [`MetricKit`](https://developer.apple.com/documentation/MetricKit) to gather on-device diagnostic logs and generate reports, but you can’t gather metrics in visionOS.
-  The system reports a maximum of two simultaneous touch inputs — one for each of the person’s hands. All system gesture recognizers handle these inputs appropriately, including for zoom and rotation gestures that require multiple fingers. If you have custom gesture recognizers that require more than two points of interaction, update them to support only one or two touches in visionOS.
-  Some APIs are unavailable in visionOS.
-  The framework does nothing in visionOS. Check the [`deviceCapabilities`](https://developer.apple.com/documentation/NearbyInteraction/NISession/deviceCapabilities) property of your session to determine whether features are available.
-  Calls to the [`FamilyControls`](https://developer.apple.com/documentation/FamilyControls) framework do nothing in visionOS.
-  visionOS doesn’t report touches of type [`UITouch.TouchType.pencil`](https://developer.apple.com/documentation/UIKit/UITouch/TouchType/pencil), but it does report other types of touches.
-  Use the [`PHPhotoLibrary`](https://developer.apple.com/documentation/Photos/PHPhotoLibrary) class to determine your app’s authorization status.
-  Check the [`isSupported`](https://developer.apple.com/documentation/ProximityReader/PaymentCardReader/isSupported) property of the card reader object to determine if Tap to Pay on iPhone is available.
-  These services are unavailable in visionOS. Check for errors when creating a [`PTChannelManager`](https://developer.apple.com/documentation/PushToTalk/PTChannelManager).
-  Check the [`isAvailable`](https://developer.apple.com/documentation/ReplayKit/RPScreenRecorder/isAvailable) property of [`RPScreenRecorder`](https://developer.apple.com/documentation/ReplayKit/RPScreenRecorder) to determine if screen recording support is available.
-  Check the [`isSupported`](https://developer.apple.com/documentation/RoomPlan/RoomCaptureSession/isSupported) property of the [`RoomCaptureSession`](https://developer.apple.com/documentation/RoomPlan/RoomCaptureSession) object to determine if LiDAR scanning is available on the device.
-  A link that presents a [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) now opens a new scene in the Safari app.
-  Calls to the [`Screen Time`](https://developer.apple.com/documentation/ScreenTime) framework do nothing in visionOS.
-  The [`SensorKit`](https://developer.apple.com/documentation/SensorKit) framework is unavailable in the native visionOS SDK and calls to it do nothing when running a compatible app. Use the [`SRSensorReader`](https://developer.apple.com/documentation/SensorKit/SRSensorReader) class to determine your app’s authorization status for compatible apps.
-  Calls to the [`Social`](https://developer.apple.com/documentation/Social) framework do nothing in visionOS.
-  Use the [`SFSpeechRecognizer`](https://developer.apple.com/documentation/Speech/SFSpeechRecognizer) class to determine if speech recognition is available.
-  Authorization prompts, Sign in with Apple prompts, and other system-provided interfaces run asynchronously outside of your app’s process. Because these interfaces don’t run modally in your app, your app might not receive immediate responses.
-  Use the [`getNotificationSettings(completionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter/getNotificationSettings(completionHandler:)) method of [`UNUserNotificationCenter`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter) to determine your app’s authorization status.
-  The system doesn’t call your app’s [`CarPlay`](https://developer.apple.com/documentation/CarPlay) code. Calls you make using [`CarKey`](https://developer.apple.com/documentation/CarKey) do nothing in visionOS.
-  The [`DataScannerViewController`](https://developer.apple.com/documentation/VisionKit/DataScannerViewController) APIs are unavailable, but other features are still available. Data scanners do nothing in [`VisionKit`](https://developer.apple.com/documentation/VisionKit) in visionOS.
-  The framework supports connections only between an iPhone and Apple Watch. Call the  [`isSupported()`](https://developer.apple.com/documentation/WatchConnectivity/WCSession/isSupported()) method of the [`WCSession`](https://developer.apple.com/documentation/WatchConnectivity/WCSession) object to determine if the framework is available.

> **Note**: Review [`Building spatial experiences for business apps with enterprise APIs for visionOS`](building-spatial-experiences-for-business-apps-with-enterprise-apis.md) for information on enterprise APIs and how to request the entitlements.

## See Also

- [Bringing your existing apps to visionOS](bringing-your-app-to-visionos.md)
  Build a version of your iPadOS or iOS app using the visionOS SDK, and update your code for platform differences.
- [Bringing your ARKit app to visionOS](bringing-your-arkit-app-to-visionos.md)
  Update an iPadOS or iOS app that uses ARKit, and provide an equivalent experience in visionOS.
- [Making your existing app compatible with visionOS](making-your-app-compatible-with-visionos.md)
  Modify your iPadOS or iOS app to run successfully in visionOS as a compatible app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/determining-whether-to-bring-your-app-to-visionos)*