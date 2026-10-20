# Determining whether to bring your app to visionOS

**Framework**: visionOS  
**Role**: Article

Decide whether to bring your existing iPadOS or iOS app to visionOS.

#### Overview

If you have an existing app that runs in iPadOS or iOS and you want to bring it to visionOS, you can choose to either run your compatible app as-is or create a visionOS-specific version.

visionOS supports most of the same technologies as iOS, so many apps built to run on iPad or iPhone can run unmodified on Apple Vision Pro. When a compatible app runs in visionOS, it retains the same appearance it has in iPadOS or iOS, and its content appears in a window in the person’s surroundings. Apps built specifically for visionOS adopt the standard system appearance, look more natural on the platform, and support 3D content and immersive experiences.

The visionOS SDK has many differences from the iOS SDK. Frameworks and features might behave differently or be unavailable when your app runs in visionOS. Use this article to ensure your app behaves as you expect on every platform.

#### Decide whether your app suits the platform

In some cases, you may decide your app is not well-suited to visionOS due to platform differences. For example, consider the following types of apps:

- **Apps that act as containers for app extensions.** This includes apps where the primary purpose is to deliver custom keyboard extensions, device drivers, sticker packs, SMS and MMS message-filtering extensions, call directory extensions, or widgets.
- **Navigation-based apps.** This includes apps that follow a person’s location changes, such as apps that offer turn-by-turn directions or navigation.
- **Selfie or camera-based apps.** This includes apps where the primary purpose is to capture images or video from the device’s cameras. The device cameras are unavailable, but continuity camera and persona capture are available on Apple Vision Pro.

#### Opt out of running on visionOS

If you don’t want your app to run on Apple Vision Pro, change your app’s availability in App Store Connect:

1. Select your app in App Store Connect.
2. Navigate to the Pricing and Availability information.
3. Disable the “Make this app available on Apple Vision Pro” option.

When you remove your app’s availability for Apple Vision Pro, the App Store stops making your iOS app available for visionOS. People who already downloaded your app on their Vision Pro can still run it in visionOS, but they can’t download it again and won’t receive any updates. This setting doesn’t affect the version of your app built natively using the visionOS SDK.

For information on managing your app’s availability for Apple Vision Pro, see [Manage availability of iPhone and iPad apps on Apple Vision Pro](https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-of-iphone-and-ipad-apps-on-apple-vision-pro).

#### Run as a compatible app on visionOS

visionOS runs compatible iPad and iPhone apps by linking against the iOS SDK to provide continuous access to existing content right away. visionOS supports most of the same technologies as iOS, so many apps built to run on iPad or iPhone can run unmodified on Apple Vision Pro. Read [Making your existing app compatible with visionOS](./making-your-app-compatible-with-visionos.md) to learn how to make your app run successfully as a compatible app in visionOS.

#### Create a visionOS version of your app

Apps built specifically for visionOS adopt the standard system appearance, and they look more natural on the platform. Creating a version of your app specifically for visionOS gives you the opportunity to add elements that work well on the platform, such as 3D content and immersive experiences. Read [Bringing your existing apps to visionOS](./bringing-your-app-to-visionos.md) for more information on how to modify your app to run successfully as a visionOS app and how to update your interface to take advantage of visionOS-specific elements.

#### Check framework availability in visionOS

The following frameworks are deprecated in their entirety in both iOS and visionOS. If your app still uses these frameworks, stop using them immediately. The reference documentation for each framework includes information about how to update your code.

- [Accounts](../Accounts/Accounts.md)
- [Address Book](../AddressBook/AddressBook.md)
- [Address Book UI](../AddressBookUI/AddressBookUI.md)
- [Assets Library](../AssetsLibrary/AssetsLibrary.md)
- [GLKit](../GLKit/GLKit.md)
- [iAd](../iAd/iAd.md)
- Newsstand Kit
- [Notification Center](../NotificationCenter/NotificationCenter.md)

> ❗ **Important**: visionOS removed many deprecated symbols entirely, turning these deprecation warnings into missing-symbol errors on the platform.

Here’s a list of frameworks and features that behave differently in visionOS:

- **ActivityKit.** Available on iOS only. Check the [`areActivitiesEnabled`](../ActivityKit/activityauthorizationinfo/areactivitiesenabled.md) property of [`ActivityAuthorizationInfo`](../ActivityKit/activityauthorizationinfo.md) to determine if Live Activities are authorized.
- **AirPlay.** visionOS hides AirPlay sharing buttons in system interfaces, and you can’t use AirPlay features from compatible apps.
- **App extensions.** visionOS doesn’t load App Clips, device drivers, device activity monitors, keyboard extensions, Messages app extensions, photo-editing app extensions, SMS and call-reporting extensions, or widgets.
- **Apple Watch features.** visionOS ignores watchOS apps and WatchKit extensions in your iOS or iPadOS app. Face sharing in [ClockKit](../ClockKit/ClockKit.md) does nothing in visionOS.
- **ARKit.** This framework requires you to use different APIs for iOS and visionOS, as visionOS can’t display windows that contain ARKit views. Check the [`isSupported`](../ARKit/arconfiguration/issupported.md) property of your configuration object to determine availability of augmented reality features. In visionOS, ARKit views such as  [`ARView`](../RealityKit/arview.md) are never available, so isolate interface code containing those views to the iOS version of your app. For information about how to bring an ARKit app to visionOS, see [Bringing your ARKit app to visionOS](./bringing-your-arkit-app-to-visionos.md).
- **Audio and video.** visionOS doesn’t support Picture in Picture or AV routing features. Check the availability of video features before using them. Be prepared for audio playback to stop automatically when your app moves to the background.
- **Automatic Assessment Configuration.** Check for error values when you configure an [`AEAssessmentSession`](../AutomaticAssessmentConfiguration/aeassessmentsession.md) object. The framework returns an error if you try to start a test in visionOS.
- **AVFoundation.** Identify what cameras are available using the [`AVCaptureDevice.DiscoverySession`](../AVFoundation/avcapturedevice/discoverysession.md) class. Don’t assume the presence of specific cameras. Capture interfaces aren’t available in visionOS. Use availability checks to determine which services are present.
- **Cellular telephony and CallKit.** You can still implement Voice-over-IP (VoIP) services using [CallKit](../CallKit/CallKit.md) and [Core Telephony](../CoreTelephony/CoreTelephony.md). Phone number verification, call-blocking, and other cellular-related services are unavailable.
- **Contacts.** Use the [`CNContactStore`](../Contacts/cncontactstore.md) class to determine your app’s authorization status.
- **Core Bluetooth.** Use the [`CBCentralManager`](../CoreBluetooth/cbcentralmanager.md) and [`CBPeripheralManager`](../CoreBluetooth/cbperipheralmanager.md) classes to determine feature availability and your app’s authorization status.
- **Core Haptics.** visionOS plays audio feedback instead of haptic feedback. Call the [`capabilitiesForHardware()`](../CoreHaptics/chhapticengine/capabilitiesforhardware%28%29.md) method of the haptic engine to determine the available features.
- **Core Location.** You can request location using the standard location service, but most other services are unavailable. Use availability checks to determine which services are present. The Always authorization level is unavailable and automatically becomes When in Use authorization. Check the properties of [`CLLocationManager`](../CoreLocation/cllocationmanager.md) to determine the availability of location services.
- **Core Motion.** Barometer data is unavailable, but most other sensors are available. Use availability checks to determine which sensors you can use. Check the properties of [`CMMotionManager`](../CoreMotion/cmmotionmanager.md) to determine the availability of accelerometers, gyroscopes, magnetometers, and other hardware sensors.
- **Core NFC.** Check the [`readingAvailable`](../CoreNFC/nfcreadersession-swift.class/readingavailable.md) property of your reader session to determine if NFC tag reading is available.
- **Device management.** Calls to the [Managed Settings](../ManagedSettings/ManagedSettings.md) and [Managed Settings UI](../ManagedSettingsUI/ManagedSettingsUI.md) frameworks do nothing in visionOS.
- **EventKit.** Use the [`EKEventStore`](../EventKit/ekeventstore.md) class to determine your app’s authorization status.
- **Exposure Notification.** Use the [`ENManager`](../ExposureNotification/enmanager.md) class to determine your app’s authorization status.
- **Game controllers.** visionOS delivers game controller events only when someone is looking at your app. To require a game controller as an input device, add the [`GCRequiresControllerUserInteraction`](../BundleResources/information-property-list/gcrequirescontrolleruserinteraction.md) key with the visionOS value to your app’s `Info.plist`.
- **Handoff.** visionOS doesn’t attempt to hand off user activities to other devices.
- **HomeKit.** You can’t add accessories using a QR code from Apple Vision Pro. Check the properties of [`HMHomeManager`](../HomeKit/hmhomemanager.md) to determine your app’s authorization status.
- **Local Authentication.** Use the [`LAContext`](../LocalAuthentication/lacontext.md) class to determine the authentication policies you can use.
- **MapKit.** User-tracking features that involve heading information aren’t available in visionOS.
- **Media Player.** Some APIs are unavailable in visionOS. Use the [`MPMediaLibrary`](../MediaPlayer/mpmedialibrary.md) class to determine your app’s authorization status.
- **Metrics.** You can use [MetricKit](../MetricKit/MetricKit.md) to gather on-device diagnostic logs and generate reports, but you can’t gather metrics in visionOS.
- **Multi-Touch.** The system reports a maximum of two simultaneous touch inputs — one for each of the person’s hands. All system gesture recognizers handle these inputs appropriately, including for zoom and rotation gestures that require multiple fingers. If you have custom gesture recognizers that require more than two points of interaction, update them to support only one or two touches in visionOS.
- **MusicKit.** Some APIs are unavailable in visionOS.
- **Nearby Interaction.** The framework does nothing in visionOS. Check the [`deviceCapabilities`](../NearbyInteraction/nisession/devicecapabilities.md) property of your session to determine whether features are available.
- **Parental controls.** Calls to the [Family Controls](../FamilyControls/FamilyControls.md) framework do nothing in visionOS.
- **PencilKit.** visionOS doesn’t report touches of type [`UITouch.TouchType.pencil`](../UIKit/uitouch/touchtype/pencil.md), but it does report other types of touches.
- **PhotoKit.** Use the [`PHPhotoLibrary`](https://developer.apple.com/documentation/photos/phphotolibrary) class to determine your app’s authorization status.
- **ProximityReader.** Check the [`isSupported`](../ProximityReader/paymentcardreader/issupported.md) property of the card reader object to determine if Tap to Pay on iPhone is available.
- **Push to Talk.** These services are unavailable in visionOS. Check for errors when creating a [`PTChannelManager`](../PushToTalk/ptchannelmanager.md).
- **ReplayKit.** Check the [`isAvailable`](../ReplayKit/rpscreenrecorder/isavailable.md) property of [`RPScreenRecorder`](../ReplayKit/rpscreenrecorder.md) to determine if screen recording support is available.
- **RoomPlan.** Check the [`isSupported`](../RoomPlan/roomcapturesession/issupported.md) property of the [`RoomCaptureSession`](../RoomPlan/roomcapturesession.md) object to determine if LiDAR scanning is available on the device.
- **Safari Services.** A link that presents a [`SFSafariViewController`](../SafariServices/sfsafariviewcontroller.md) now opens a new scene in the Safari app.
- **Screen Time.** Calls to the [Screen Time](../ScreenTime/ScreenTime.md) framework do nothing in visionOS.
- **Sensor-related features.** The [SensorKit](../SensorKit/SensorKit.md) framework is unavailable in the native visionOS SDK and calls to it do nothing when running a compatible app. Use the [`SRSensorReader`](../SensorKit/srsensorreader.md) class to determine your app’s authorization status for compatible apps.
- **Social media.** Calls to the [Social](../Social/Social.md) framework do nothing in visionOS.
- **Speech.** Use the [`SFSpeechRecognizer`](../Speech/sfspeechrecognizer.md) class to determine if speech recognition is available.
- **System interfaces.** Authorization prompts, Sign in with Apple prompts, and other system-provided interfaces run asynchronously outside of your app’s process. Because these interfaces don’t run modally in your app, your app might not receive immediate responses.
- **User Notifications.** Use the [`getNotificationSettings(completionHandler:)`](../UserNotifications/unusernotificationcenter/getnotificationsettings%28completionhandler%29.md) method of [`UNUserNotificationCenter`](../UserNotifications/unusernotificationcenter.md) to determine your app’s authorization status.
- **Vehicle features.** The system doesn’t call your app’s [CarPlay](../CarPlay/CarPlay.md) code. Calls you make using [CarKey](../CarKey/CarKey.md) do nothing in visionOS.
- **VisionKit.** The [`DataScannerViewController`](../VisionKit/datascannerviewcontroller.md) APIs are unavailable, but other features are still available. Data scanners do nothing in [VisionKit](../VisionKit/VisionKit.md) in visionOS.
- **Watch Connectivity.** The framework supports connections only between an iPhone and Apple Watch. Call the  [`isSupported()`](../WatchConnectivity/wcsession/issupported%28%29.md) method of the [`WCSession`](../WatchConnectivity/wcsession.md) object to determine if the framework is available.

> **Note**: Review [Building spatial experiences for business apps with enterprise APIs for visionOS](./building-spatial-experiences-for-business-apps-with-enterprise-apis.md) for information on enterprise APIs and how to request the entitlements.

## See Also

### iOS migration and compatibility
- [Bringing your existing apps to visionOS](./bringing-your-app-to-visionos.md)
  Build a version of your iPadOS or iOS app using the visionOS SDK, and update your code for platform differences.
- [Bringing your ARKit app to visionOS](./bringing-your-arkit-app-to-visionos.md)
  Update an iPadOS or iOS app that uses ARKit, and provide an equivalent experience in visionOS.
- [Making your existing app compatible with visionOS](./making-your-app-compatible-with-visionos.md)
  Modify your iPadOS or iOS app to run successfully in visionOS as a compatible app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/determining-whether-to-bring-your-app-to-visionos)*