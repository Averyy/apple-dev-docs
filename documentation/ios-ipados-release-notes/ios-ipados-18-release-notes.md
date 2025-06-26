# iOS & iPadOS 18 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 18 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 18. The SDK comes bundled with Xcode 16, available from the Mac App Store. For information on the compatibility requirements for Xcode 16, see [`Xcode 16 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16-release-notes).

##### Accessibility

###### Resolved Issues

- Fixed: User might be unable to play newly added background sounds (Fire and Night).  (128898875)
- Fixed: Sound Recognition and Sound Actions might not work on iPad Pro models with M4.  (128949527)
- Fixed: Music Haptics might disappear after the first time it is entered in Accessibility Settings until Settings restarts.  (128960448)

##### Accessorysetupkit

###### Resolved Issues

- Fixed: Users might be unable to rename Accessory’s display name or SSID.  (128958722)

##### Activity Sharing

###### Resolved Issues

- Fixed: Notifications for workouts completed by a friend might show incorrect text.  (128939058)

##### Adattributionkit

###### New Features

- [`AdAttributionKit`](https://developer.apple.comhttps://developer.apple.com/documentation/AdAttributionKit) now supports measuring re-engagement, which is click-through attribution for apps that were already installed. Re-engagement also supports deep linking into content in apps using Universal Links.  (111224069)

###### Resolved Issues

- Fixed an issue where development postbacks fail to send after developer mode has been enabled for an extended period of time.  (130100361)

##### App Intents

###### Resolved Issues

- Fixed: EntityURLRepresentation allows arbitrary custom URLs without validation.   (119524801)
- Fixed: AppIntent static properties including title and description are not concurrency-safe.  (128090148)
- Fixed: Parameterless `@Parameter` and `@Property` wrappers might cause protocol conformance failures.  (130219933)

###### Known Issues

- `@UnionValue` types currently only work as intent results. Attempting to use a `@UnionValue` as the type of an intent parameter or entity property results in failure to compile.  (128069844)

##### App Store

###### New Features

- On-demand resources limits were increased for iOS 18, iPadOS 18, tvOS 18 and visionOS 2. See [`On-demand resources size limits`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/on-demand-resources-size-limits/) for more information.  (122163236)

##### Apple Cash

###### Known Issues

- With Tap to Cash, you can send and receive Apple Cash by holding two iPhones together. An Apple Cash account is required to send and receive payments. Payments will be returned to the sender if the receiver doesn’t set up an Apple Cash account or verify their personal information within 7 days. For Developer Beta, Tap to Cash payments cannot exceed $250 per transaction. Transaction limits are subject to change, including lowering limits, at any time during the Developer or Public Betas without notice.  (128977390)

##### Assistive Access

###### Resolved Issues

- Fixed: The Messages app might hang in Assistive Access.   (127601737)
- Fixed: Users might not be able to add Photos or Camera apps to Assistive Access and the apps might be removed from an existing user’s setup if they open Assistive Access settings.  (128905924)

##### Audio

###### Resolved Issues

- Fixed: Some bluetooth headphones might not be useable as an audio output route with certain AVAudioSession configurations.  (126693883)

##### Calculator

###### Resolved Issues

- Fixed: Deleting history item with the Edit button visually deletes the top item in the list. The backing data stays correct.  (126768783)

##### Camera

###### Resolved Issues

- Fixed: For Camera background replacement, it might be necessary to double click to add a background image from your Photos Library using the Photo Picker.  (122358378)
- Fixed: First Portrait capture after boot might take longer than expected to finish.  (128881179)
- Fixed: Camera functions might take up to 2 minutes to work after booting iPhone/iPad.  (128899310)
- Fixed: When using the Document Scanning feature from Camera app on iPad, it might sometimes result in a black screen instead of a live preview from camera.  (128907349)
- Fixed: Portrait mode preview with rear facing camera might show artifacts when pointed at objects when using Stage Light, Stage Light Mono, and High-Key Light Mono light filters. Artifacts will not affect captured assets.  (129024197)

##### Carplay

###### Resolved Issues

- Fixed: Bluetooth pairing UI could become irresponsive for BMW users, which leads to failed contact transfer.   (129043855)

##### Cfnetwork

###### Resolved Issues

- Fixed: `CFNetworkExecuteProxyAutoConfigurationScript` and `CFNetworkExecuteProxyAutoConfigurationURL` have always returned a +1 retained CF type object, but the function declarations were not decorated with the `CF_RETURNS_RETAINED` attribute until iOS 18, macOS 15, tvOS 18, and visionOS 2. For C-based languages, the clang static analyzer might note if the object is leaked. No source code changes are required, but they are encouraged to fix the leak. For Swift, this changes the return type of these functions from `Unmanaged<>` to the actual CF type returned, which will require a source change to fix when compiling with newer SDKs. However, Swift programs compiled with older SDKs will continue to work on the new OSes, though the returned CF type object will continue to leak as it did prior to this change.  (126154509)

##### Containerization

###### Resolved Issues

- Fixed: Improved the handling of the duplicate containers created by Xcode 15 through 15.3. Those versions of Xcode might create duplicate containers on the device. This change ensures that the app launches with a consistent container and that deleting the app also deletes any duplicate containers.  (123480553)

##### Control Center

###### Resolved Issues

- Fixed: Control Center page control is overlapped by the Dynamic Island in landscape.  (125913281)
- Fixed: Empty pages in Control Center might linger after exiting edit mode.  (126760824)
- Fixed: Control widgets with a parameterized OpenIntent action are not configurable.  (128241927)
- Fixed: Voice Memos control will not render correctly or be functional after upgrading to iOS 18 if it was part of Control Center prior to the update.  (129184182)

###### Known Issues

- App Icons in Control Center gallery always appear in Dark Mode.  (126721275)

##### Core Ml

###### Resolved Issues

- Fixed: Core ML Model Deployment API is unavailable (`MLModelCollection` and `MLModelCollectionEntry`). Consider using Background Assets or `NSURLSession` instead.  (122955353)

##### Coremedia

###### Resolved Issues

- Fixed: Seeking into an interstitial event with non-zero resumption offset on the integrated timeline might result in the event being cancelled.  (129175283)

##### Display

###### Resolved Issues

- Fixed: Phones with Always on Display enabled might panic/reboot on exit.  (128268712)

##### Facetime

###### New Features

- FaceTime in Low Data Mode now uses more data when network conditions are good for improved video call quality.  (128408959)

###### Resolved Issues

- Fixed: When user picks up FaceTime Video call from lock screen and unlock the device later, the camera might be disabled where user cannot see remote side via PiP and vice versa.  (124719544)

##### Files

###### Resolved Issues

- Fixed: Users might be unable to navigate within Move panel in the Files app on iPhone.  (128868597)

###### Known Issues

- Creating local files in the Files app fails in the visionOS 2 and iOS 18 simulators if the host is not upgraded to macOS Sequoia Beta.  (132561244)

##### Financekit

###### Resolved Issues

- Fixed: Transactions shared via the Transaction Picker might have empty description strings.  (128618523)

##### Fitness+

###### Resolved Issues

- Fixed: The Fitness app might not load the Fitness+ For You page immediately on first launch.  (127116109)

##### Foundation

###### New Features

- JSONEncoder.OutputFormatting.sortedKeys will now sort keys with a different ordering. Previously, keys were sorted using a numeric, case-insensitive, or localized ordering. Beginning in beta 4, keys are sorted lexicographically based on the keys’ UTF-8 contents.  (126874437)

###### Resolved Issues

- Fixed: [`Date.ComponentsFormatStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/date/componentsformatstyle) was incorrectly producing strings like `"1m"` with the `Date.ComponentsFormatStyle.Style.condensedAbbreviated` style and strings like `"1min"` with the `.narrow` style instead of the other way around. The behavior was corrected to match the behavior of [`Duration.UnitsFormatStyle.UnitWidth`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct).  (125790342)

##### Freeform

###### Resolved Issues

- Fixed: Some images inserted into iWork and Freeform might be zoomed in.  (128637913)

##### Handwriting

###### Resolved Issues

- Fixed: Auto-refine animation contains rendering issues for users with Display Zoom set to “More Space” within the Display & Brightness settings.  (129419813)

##### Headphone Accommodations

###### New Features

- Headphone Accommodations can now be configured on macOS. When user set up Headphone Accommodations with AirPods Pro 2s, user will continue to hear audio adjusted when connected to other audio sources.  (130245415)

##### Health

###### Resolved Issues

- Fixed: In Cycle Tracking, multiple pregnancy samples might be saved after a user adds or edits a pregnancy.   (121271613)
- Fixed: Doses of medication logged via mirrored watch notifications for incompatible schedule types do not save on phone if device is locked.  (128635016)
- Fixed: Cardio Fitness notifications will not turn back on automatically 12 weeks post pregnancy or after a pregnancy cycle factor is deleted.   (128659463)
- Fixed: Period flow is displayed as Bleeding during Pregnancy and Bleeding after Pregnancy in Cycle Detail View.  (128929595)
- Fixed: When Heart Rate Watch App is deleted, Health Checklist in Health App and Watch Settings still show features (Irregular Rhythm Notifications, High Heart Rate Notifications, Low Heart Rate Notifications) as active.  (128970200)
- Fixed: The Cycle Tracking snippet might continue to display flow or symptoms logged pre-pregnancy.  (129066144)
- Fixed: In Cycle Tracking, if a pregnancy sample is edited or created on a device different than where pregnancy onboarding was completed, Medical ID might not display pregnancy information correctly.  (130777331)

###### Known Issues

- If a pregnancy sample is deleted on a device that is not on iOS 18, users are not prompted to remove pregnancy data from MedicalID if applicable.   (129296194)  Manually delete pregnancy data from Medical ID.
- In Cycle Tracking, if a pregnancy sample is edited or created on a device different than where pregnancy onboarding was completed, Medical ID might not display pregnancy information correctly.  (130784441)  Edit Medical ID to add pregnancy information.

##### Healthkit

###### Resolved Issues

- Fixed: Workout routes for workout types created by Apple Watch Workout app are not available in third-party workout apps.  (123450917)

###### Known Issues

- With the introduction of Swift 6 this year, developers who update their projects to use Swift 6 might have issues with their apps, which can lead to app crashes when executing a variety of HealthKit API calls.  (131794283)  Annotate your callbacks in code with @sendable, NS_SWIFT_SENDABLE, or use pre-Swift 6 versions of the language.

##### Home App

###### Known Issues

- If a user has multiple devices running beta 1 or 2 and onboarded Home with a Utility account, the account might get offboarded when one device is upgraded to beta 3.  (130850945)  Re-onboard Home Utility account, only after upgrading all devices to beta 3.

##### Home Screen

###### Resolved Issues

- Fixed: There might be a delay when switching to dark or tinted icons on the home screen.  (129069905)
- Fixed: Icon tint slider knob might not update to selected color on the first use after boot.  (129114071)

##### Homekit

###### Resolved Issues

- Fixed: Accessory Firmware update will not be offered for an accessory if a user reboots the resident or the primary switches.  (128255088)

##### Hotspot

###### Resolved Issues

- Fixed: Carrier EAP-SIM/EAP-AKA auto-joint will fail and user will be unable to use carrier public Hotspot.  (130650425)

##### Icloud Drive

###### Resolved Issues

- Fixed: Frequently changed files syncing over iCloud Drive will use more data than expected.  (128771010)

##### Iphone Mirroring

###### Resolved Issues

- Fixed: Dictation is available during iPhone Mirroring.  (126654567)
- Fixed: Keyboard input might not work in Spotlight or App Library when using iPhone Mirroring.  (126928807)
- Fixed: Users might be able to launch lock screen apps while using iPhone Mirroring.  (128281331)
- Fixed: Settings might show incompatible devices under iPhone Mirroring.  (128633492)
- Fixed: The camera is not enabled in any case, and only FaceTime shows the alert. FaceTime triggers the “Camera not allowed in iPhone Mirroring” alert. Other apps do not trigger the alert though the Camera is disabled.  (128646948)

##### Journaling Suggestions

###### New Features

- Journaling Suggestions is introducing a set of new features to keep encouraging people to reflect and write about their day-to-day experiences to get the mental wellbeing benefits of Journaling. The API now supports Landscape mode and Reflection prompts. Added support for State of Mind logged on Health or Journal app, Run and mixed Walk/Run sessions performed while carrying a standalone iPhone, Media played by apps that donate to MPNowPlayingInfoCenter, People and Pet names from Photos and enhancements to Trips Suggestions to highlight Countries and States visited.  (129029773)

###### Resolved Issues

- Fixed: Users might experience blank suggestions or engineering text.  (128774773)
- Fixed: Users might experience long spinner after tapping ‘+’ to open Journaling Suggestions sheet.  (128950895)
- Fixed: When tapping ‘+’ to launch the Journaling Suggestions sheet, it might not launch.  (128970387)

##### Kernel

###### Deprecations

- `kern.bootsessionuuid` is no longer available to apps.  (47217954)

##### Keyboard

###### Resolved Issues

- Fixed: Users will not be able to configure Keyboard in Settings, including adding/removing keyboards for different languages or adding/removing keyboard extensions.  (129174947)

##### Lock Screen

###### Resolved Issues

- Fixed: Lock Screen Quick Action buttons might disappear.  (128096099)
- Fixed: Users will be unable to configure Controls that have configuration on the Lock Screen.  (128967021)

##### Mail

###### Resolved Issues

- Fixed: The Mail badge count might not update until Mail is launched.  (129914323)

###### Known Issues

- Upgrading from iOS 18.0 beta 5 to iOS 18.1 beta might cause all Mail to redownload.  (132930689)

##### Maps

###### New Features

- Introduced Place ID, a unique and persistent identifier.  (129071038)
- Added new resultTypes to MKLocalSearch.Request and additional PointofInterestCategory values.  (129073725)
- Introduced Place Card API to show Maps Place Card UI.  (129073922)

###### Resolved Issues

- Fixed: Maps Share ETA might fail when sending to a recipient via SMS.  (127547239)
- Fixed: The Place Card API might fail to load place details.  (128504304)
- Fixed: In searches that use MKLocalSearch.Request, the result type option physicalFeature is ignored.  (128961972)

###### Known Issues

- Conversion between a point in the map view and a physical location (CLLocationCoordinate2D) might be imprecise at high zoom levels.  (129042241)

##### Math Notes

###### Resolved Issues

- Fixed: Adjusting negative numbers can lead to multiple negative signs.  (123738353)
- Fixed: Adjusting a number with a comma can immediately change the number value to 0.  (127904684)

##### Memory Allocation

###### New Features

- The system memory allocator (malloc(3)) has switched to a new implementation for most allocation sizes. Users might experience exposure of latent memory access bugs due to changes in heap layout, differences in performance for allocation-heavy workloads, and changes in fragmentation.  (127493322)

##### Messages

###### New Features

- Sent and received messages via satellite might not be relayed to your other devices.  (125574729)
- Messages via satellite is currently available only in the U.S. SMS messaging via satellite is available on select carriers.  (127751557)
- Messages via satellite is currently available only in the U.S. SMS messaging via satellite is available on select carriers.  (131421891)
- RCS messaging is available on select carriers.  (131499640)

###### Resolved Issues

- Fixed: A send message sound will  play when scheduling the message instead of when the message is sent.  (121896789)
- Fixed: When applying tapbacks by long pressing on a Message, users will be unable to use 3rd party stickers.  (122379099)
- Fixed: When off grid, text message conversations might incorrectly display text suggesting that the carrier does not support text messages via satellite, even though user is able to send and receive text messages over satellite.  (127334940)
- Fixed: Emoji tapbacks might display incorrectly in SMS group conversations.  (127446747)
- Fixed an issue where multi-part SMS notifications for MMS are not correctly processed by the device while on-grid.  (128880899)
- Fixed: Existing RCS 1:1/Group chat will downgrade to SMS even if RCS is still registered.  (130029732)

###### Known Issues

- For group messages with RCS and iMessage participants, a reply to a text message attachment might not display as a thread on the receiver device.  (133326509)

##### Networking

###### Resolved Issues

- Fixed: For apps linked on macOS 15 / iOS 18 or newer, the default User-Agent request header field value generated by URLSession now includes the unlocalized bundle name instead of the localized bundle name.  (117380285)

##### Notifications

###### Resolved Issues

- Fixed: Incoming notifications on Lock Screen might not be seen when in List View.  (129021171)

##### Phone

###### Resolved Issues

- Fixed: In the Phone app, the Keypad search results always display a video icon, although tapping the icon places audio calls.  (131601723)

##### Photos

###### New Features

- Collection order and visibility changes will be reset if they were made on iOS and iPadOS 18.0 beta 4 or earlier.  (132117458)

###### Resolved Issues

- Fixed: Photos and videos might stop syncing via iCloud Photo Library.  (128325085)
- Fixed: Photos-related services might not respond. This issue can impact iCloud Photo Library syncing, Camera captures, Screenshot captures, and Sharing.  (130739189)
- Fixed: Upgrading from iOS 18.0 beta 5 to iOS 18.1 beta results in a Photos Library rebuild.  (131845921)

##### Platform

###### New Features

- On Apple Silicon based devices with M3 or later, and A16 Bionic or later, the values returned by reading the CNTFRQ_EL0 and CNTVCT_EL0 registers have been updated to 1 GHz, instead of the prior value of 24 MHz. It is still recommended for apps to use libsystem APIs like `mach_absolute_time()` for timekeeping. Your app will not be impacted by this change if it uses Apple’s timekeeping APIs. For compatibility purposes, this change will only be visible when using the SDK associated with this release or later. On macOS, applications running inside a Virtualization.framework VM will continue to receive the legacy behavior.  (84639494)
- The firmware image for iBoot will be made available in cleartext in the PCC image. To reduce the overhead imposed by firmware encryption and align policies where appropriate, firmware encryption has been disabled for iBoot on iOS, macOS, watchOS, tvOS, and visionOS. See [`Private Cloud Compute`](https://developer.apple.comhttps://security.apple.com/blog/private-cloud-compute/) for more details.  (125171074)

##### Podcasts

###### Resolved Issues

- Fixed: Podcasts will incorrectly show “View Transcript” as an option in shortcuts.  (131070716)

##### Previews

###### Resolved Issues

- Fixed: Triggering an on-device preview might fail.  (129150211)

##### Realitykit

###### New Features

- USD files which use Catmull-Clark subdivision now render using subdivision in RealityKit. Meshes which produce less than 35,000 patches can render using subdivision. This can increase memory consumption and reduce rendering performance.  (129016034)
- Virtual objects now render using the Display P3 color gamut. When using a `DrawableQueue` connected to a `TextureResource` with the `.color` semantic, render using the Display P3 color space.  (129017592)

###### Resolved Issues

- In iOS & iPadOS 17, macOS 14, visionOS 1 and earlier, UnlitMaterials’ blending modes inconsistently respond to `.blending`, `.color`, and `.baseColor` setters. In applications building against RealityKit from iOS & iPadOS 18, macOS 15, or visionOS 2, alpha-blending enablement should be configured explicitly with `.blending = .transparent(opacity:)`. Developers are advised to check that their code-configured materials are alpha-blending as intended, and use the `.blending` setting where appropriate.  (118210191)
- In iOS & iPadOS 17, macOS 14, visionOS 1 and earlier, transparent materials’ apparent final opacities respond inconsistently to `.blending`, `.color`, and `.baseColor` setters. In applications building against RealityKit from iOS & iPadOS 18, macOS 15, or visionOS 2, the final opacity of transparent materials is computed as a multiplication of its `.color` or `.baseColor`’s alpha and `.blending = .transparent(opacity:)`. Developers are advised to check that their code-configured transparent materials render with the intended final opacities, and update their usages of `.color`, `.baseColor` and/or `.blending = .transparent(opacity:)` when necessary.  (125431647)
- Fixed: The `pixelCast` function might not work correctly on iOS.  (125742631)
- Fixed: Grounding shadows are less prominent than expected.  (126498888)
- Fixed: Using an `Image 2D Array` Shader Graph node in Reality Composer Pro might result in corruption or a system crash.  (127122590)
- Fixed: Grounding shadows will not be visible in ARQL on certain iPad Pros. Apps enabling ray-traced shadows via Xcode storyboards will not take affect.  (127748381)
- Fixed: Setting the `environment` property of a `RealityView` to `.worldTracking` does not automatically start an ARKit session, and the background of your `RealityView` might be black.  (128417183)
- Fixed: Reality files written by beta versions of RealityKit might not load in later versions.  (128424173)
- Fixed: Physics simulation behavior is different from previous releases.  (128435086)
- Fixed: The `stop` function on SpatialTrackingSesssion has no effect.  (128559666)
- Fixed: Emphasize actions are always additive and should be played with `separateAnimatedValue` set to `true`.  (128622689)
- Fixed: In the Swift 6 language mode, subclasses of the `Entity` class fail to compile.  (128787131)
- Fixed: The `.trigger` mode of CollisionComponent no longer generates CollisionEvents when both involved collision shapes use the `.trigger` mode.  (129016567)
- Fixed: `[.world, .plane, .image, .object, .face, .camera]` anchor capabilities used in conjunction with any scene understanding capabilities on a device without a LiDAR scanner would cause those anchor capabilities to not work.  (129253808)

###### Deprecations

- In previous versions, the order of child entities was sometimes preserved. Now, the order of an `Entity`’s children might not be reliable and can change unexpectedly when any child is reparented.  (129015381)

##### Screen Time

###### Resolved Issues

- Fixed: Parent approving remotely from the parent device will always grant 1 hour, regardless of whether a child asks for a 15-minute, 1-hour, or all-day exception for an app or website.   (129084141)
- Fixed: When an Apple Watch is upgraded to 11.0 from an earlier Beta, Screen Time App Limits might be deleted for both the parent and child. If this occurs, parent will need to add back the app limits.  (130981807)

##### Search

###### Resolved Issues

- Fixed: The “Help Apple Improve Search” control is not functional.  (129226418)

##### Settings

###### Resolved Issues

- Fixed: Recents and search results are sometimes missing and might not navigate to nested panes.  (128802504)
- Fixed: The available storage listed in General > About might be incorrect.   (129688831)
- Fixed: When navigating to Settings > General > Storage, the Settings app might crash if you have not opened Podcasts prior.  (131180865)

##### Shortcuts

###### Resolved Issues

- Fixed: The Shortcuts editor might offer some new actions that are not yet ready for use. If you save a shortcut with one of these actions, you might need to correct it after a future update with the corrected actions.  (128841105)
- Fixed: Adding or removing SiriKit intents or App Intents might not reflect immediately in the Shortcuts app.  (130039560)
- Fixed: The Create Board and Open Board Shortcuts actions and App Shortcuts might not be available.  (133023610)

##### Simulator

###### Resolved Issues

- Fixed: Using Safari in the simulator can cause the simulator to hang.  (128545001)

##### Siri

###### New Features

- In iOS 18, when an iPhone is connected via Bluetooth to a vehicle without CarPlay, Siri’s audio quality can be significantly improved through the new option “Respond over Media Source”. First, users need to enable the setting by going to (with Developer settings enabled) Settings, “Developers” → “Siri in Bluetooth Car testing” → Toggle “Show Audio Output in Settings”. Users then will be able to use this feature by going to Settings “Siri & Search” → “Siri Responses” → “When Connected to Car Bluetooth”.  (128692679)

##### Software Update

###### Resolved Issues

- Fixed: Devices updating from an iOS/iPadOS 18 beta build or macOS 15 beta build prior to iOS 18 beta 4 or macOS 15 beta 4 can hit a download error.  (130652449)

##### Spotlight

###### Known Issues

- Icons in Spotlight might not match icons on the Home Screen.  (134088480)

##### Storekit

###### New Features

- The [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) now supports custom control styles. To create a custom control style, declare a type that conforms to [`SubscriptionStoreControlStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle) and implement `makeBody(configuration:)` method.  (106819454)
- New standard styles are available for laying out subscription store view controls with a compact height. Use `pagedPicker` and `pagedProminentPicker` for a platform appropriate paging effect, or `compactPicker` to place options in a horizontal stack. For watchOS, the new `pagedPicker` style is available for laying out [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) controls with a compact height.  (110286601)
- Use types such as `SubscriptionOptionGroup` and `SubscriptionPeriodGroupSet` to declare a hierarchical structure for your [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview). You can use the `subscriptionStoreOptionGroupStyle(_:)` to choose between presenting groups as a tab view or as navigation links.  (110429924) (FB12264937)
- The subscription status [`RenewalInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/status/3822294-renewalinfo) object now supports new properties `renewalPrice` and `currency` to indicate the price at which the subscription will renew, and its currency. There is also a new `offer` property containing the information of the offer that will be applied to the next renewal, if there is any. This includes the offer ID, the offer type, and the payment mode.  (114217892)
- Finished consumables can now be included when using the [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction) APIs. Users can enable this feature by setting `SKInAppPurchaseHistoryIncludesConsumables` to true in app’s Info.plist.  (115079880)
- When configuring the control style for a [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview), users can specify a placement for the controls using the `subscriptionStoreControlStyle(_:placement:)` view modifier. For tvOS, by default [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) will place the controls trailing the marketing content.  (115319543)
- When building an app with Xcode 16, [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) instances using the picker control style have an updated appearance. Use `subscriptionStorePickerItemBackground(_:in:)` to configure a different background color and shape for the picker items.  (120558960)
- Users can now use APIs like monthly or yearly to get common [`Product.SubscriptionPeriod`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptionperiod) values when comparing subscription periods.  (122684230)

###### Resolved Issues

- Fixed: Selecting `Done` in the refund request confirmation sheet returns an error when using the [`refund request API`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/3803220-beginrefundrequest/) with StoreKit Testing in Xcode.  (123865137)
- Fixed: VoiceOver does not read a product’s title and description in [`ProductView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/productview) and [`StoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/storeview).  (124254957) (FB13679318)
- Fixed an issue where the tab control in [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) is too wide when using [`StoreContent`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/storecontent) with the [`tabs`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionoptiongroupstyle/4354834-tabs) option group style.  (128567088)
- The [`requestReview`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/environmentvalues/requestreview) environment variable is now compatible with Swift 6.  (129929512) (FB13922875)

###### Known Issues

- When using `SubscriptionStorePicker` within a container view, the window bar doesn’t work correctly.   (117701666)  Return `SubscriptionStorePicker` as a top level view from `makeBody(configuration:)` method, instead of using it within a container.

###### Deprecations

- The Original API for In-App Purchase is now deprecated, including: SKStoreReviewController, SKProduct, SKReceiptRefreshRequest, SKStorefront, SKPayment, SKRequest, SKProductsRequest, and SKProductDiscount. Please upgrade to [`StoreKit 2`](https://developer.apple.comhttps://developer.apple.com/storekit/) for current APIs and future enhancements.  (116600524)

##### Swift Charts

###### New Features

- Plot math functions using `LinePlot` and `AreaPlot`.  (117186178)
- Visualize large datasets more efficiently using vectorized plot APIs such as `PointPlot` and `RectanglePlot`.  (117469419)

###### Resolved Issues

- Fixed: Rotated axis labels stretch to incorrect sizes.  (106013386)
- Fixed: Blur and shadow effects on marks might disappear during animation.  (125493885)
- Fixed: Glitches when animating a connected scatter plot made of `LineMark`.  (127196185)
- Fixed: Stroke styles can now be animated.  (127465359)
- Fixed: For function plots, the Y domain cannot be inferred automatically.  (128877906)
- Fixed: Animations involving charts might lead to the disappearance of marks with a `.foregroundStyle(Color)` throughout the duration of the animation, even if the color did not change.  (130023892)

##### Swiftui

###### New Features

- When using a `TabView`, tapping on the current tab now pops any embedded navigation stack.  (50924017)
- Pickers now can have keyboard shortcuts attached to their individual options, by attaching the `keyboardShortcut()` modifier to the individual views in the picker content.  (67682762) (FB8522629)
- If `Label` is used inside of a `List` with multiple views as its title, it will now stack them vertically and apply subtitle treatments to every view after the first.  (115528544)
- For `ObservableObject` subclasses used with `@EnvironmentObject`, `@ObservedObject`, and `@StateObject`, SwiftUI will now only call `objectWillChange` once per property per object instance. If you use `@Published` and the default `ObservableObjectPublisher`, you do not need to change anything. If you override `objectWillChange`, ensure the lifetime of the publisher you return matches the lifetime of its enclosing `ObservableObject`.  (116197689)
- On iPad, TabViews using the `automatic` style have a new appearance in the `regular` horizontal size class. The tab bar now appears at the top, instead of the bottom, with a more compact visual appearance.  (117029720)
- SwiftUI sheets presented with the `.sheet` modifier now use `.automatic` sizing by default. `.automatic` resolves to `.form` or `.form.fitted(horizontal:false, vertical: true)` depending on the platform (see the symbol’s documentation for more). Platforms prior to iOS 18 and aligned releases used different, non-customizable default sheet sizing. iOS 17 and earlier used what is now called `.page` presentation sizing. macOS 14 and earlier used what is now called `.fitted` sizing. visionOS 1 used `.fitted` sizing. When linking apps against iOS 18 and aligned SDKs, audit your sheet presentations and pick the sizing best for you. Apply a `.presentationSizing` modifier to sheet contents: ```swift
 ContentView().sheet(isPresented: $present) {
   SheetView().presentationSizing(.form)
 }
``` (117551515)
- Improved the interaction of highPriorityGesture with ScrollView.  (119333786)
- Document-based applications linked against iOS 18 now have a new launch screen design. Users can customize the default design by adding a `DocumentGroupLaunchScene` to the app definition. Users can change the screen title and background, replace action buttons, and add decorative accessory views. Non-document-based apps also can use the new screen via `DocumentLaunchView`.  (119843158)
- Types conforming to the View protocol, and other similar SwiftUI protocols, are now isolated to the `@MainActor` by default. SwiftUI’s runtime behavior with respect to actor isolation has not changed: SwiftUI views and similar types have always been evaluated on the main actor at runtime; this change improves compile-time diagnostics for potential data-race safety issues. To opt out of the new default main actor isolation and restore the previous default isolation, add the nonisolated keyword to methods and properties as needed, or move the protocol conformance to an extension to opt out the entire type.  (120815051)
- Known FormatStyles that are dependent on a FormatStyleCapitalizationContext and are embedded into a LocalizableStringResource via string interpolation now automatically infer capitalization based on sentence structure. The capitalization is only inferred automatically if it was `unknown` before.  (122688257)
- [`Text(_:format:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(_:format:)) now automatically injects `FormatStyle` known to SwiftUI with the `TimeZone` and `Calendar` from the environment.  (123662780)
- `@Entry` macro can now be used to simplify declarations of custom `EnvironmentValues`, `FocusedValues`, `Transaction`, and `ContainerValues` properties.  (125568810)
- Added the ability to give a gesture a name, which gets surfaced to UIGestureRecognizers when establishing dependencies.  (126527559)
- Nesting a TabSection within a TabSection is supported in the `.sidebarAdaptable` TabViewStyle on iPadOS and visionOS.  (128237671)

###### Resolved Issues

- Fixed an issue where long press gestures would block gestures on other descendant views.  (57368881)
- Fixed an issue where `UIButton` used with `UIViewRepresentable` might not receive touches. Tap gestures in SwiftUI also now correctly coordinate with `UITapGestureRecognizer` instances.  (57885589)
- Fixed: For apps linked on or after iOS 18, the `popover` modifier now respects the `arrowEdge` argument on iOS and iPadOS.  (66839017) (FB8350757)
- Fixed: SwiftUI gestures no longer errantly trigger when dismissing a menu.  (69703502) (FB8751308)
- Fixed: `ForEach` is now able to reclaim persistent state of unused child views. `@State` values created by views inside `ForEach` elements might be destroyed earlier than previously observed.  (90667238)
- Fixed: A `DismissAction` captured in the content or detail column of a `NavigationSplitView` now pops the implicit stack. For apps linked on or after iOS 18 and aligned releases, the button in the example below will now clear any selection in the sidebar `List`. Previously, this would fail silently on iOS, and close the window on macOS. ```None
 NavigationSplitView {
   List(…)
 } detail: {
   DetailView()
 }
 
 struct DetailView: View {
   @Environment(\.dismiss) private var dismiss
 
   var body: some View { 
     Button("Pop") { dismiss() }
   }
 }
``` To retain the previous behavior, capture the `DismissAction` from the environment above the `NavigationSplitView`.  (92522613)
- Fixed: A `ScrollView` now propagates safe area insets on its non-scrollable edges. By default, Scroll indicator for scroll views that occupy the size of the screen have improved insets.  (102766716)
- Fixed: Outline Lists do not animate correctly.  (106239318)
- Fixed an issue where searchable suggestions automatically filter out completion options that have a `searchCompletion` matching the current search text. Exact matches should be explicitly elided from the suggestions if desired.  (107706241)
- Fixed: `View._printChanges` now outputs key path of mutated observable properties instead of “@dependencies”.  (111392797)
- Fixed: Using the `scrollClipDisabled()` view modifier with a `ScrollView` with a `LazyHStack` or `LazyVStack` will use the containing window to determine what content the lazy stack should render.  (111796138)
- Fixed: SwiftUI will now assert that types conforming to the `App` protocol are value types.  (113634782)
- Fixed: In macOS, a Toggle of the `.switch` style now animates when its `isOn` state is changed programatically, matching the existing behavior on iOS and iPadOS. The animation can be disabled in all platforms by setting the transaction’s `disablesAnimations` property when updating a Toggle’s state.  (115071023)
- Fixed: Automatically updating `Text` created via [`Text(_:style:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(_:style:)) or [`Text(timerInterval:pauseTime:countsDown:showsHours:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:)) was causing increased battery drain when used in long running Live Activities. They now no longer animate changes in digits that signal the seconds value, keeping the power impact to a minimum.  (115906895)
- Fixed: SwiftUI no longer overrides a nil `scrollTargetAnchor` when using the `scrollPosition(id:anchor:)` modifier with a nil anchor. Specify a `topLeading` anchor to restore the previous behavior.  (116124988)
- Fixed: When linking against iOS 18 SDKs, SwiftUI prevents cycles in `.sheet` presentations caused by presentations preferences (e.g. `presentationDetents` or `presentationBackground`) that depend on the size of the sheet. In some cases prior to iOS 18, these cycles might settle independently after some oscillation.  (117699610)
- Fixed: App scenePhase now reports as active when at least one scene is active.  (117864591)
- Fixed: The `arrowEdge` argument in `.popover` modifiers is now respected when linking against the iOS 18 SDK. If previously relying on the default argument of `.top`, this argument was not respected, and instead, the popover presented with `.any` behavior. If passing an explicit value, that value will now be respected. If not passing an explicit argument to the `arrowEdge` parameter, upon recompiling with the iOS 18 SDK, overload resolution will select a new method that takes no arrow edge in which the system picks the best arrow edge. When recompiling with the iOS 18 SDK, ensure popovers are not clipped or off-screen due to presenting in the wrong direction.  (117921721)
- Fixed: Scroll views can now accept interaction in their content insets.  (117928468)
- Fixed: `.navigationDestination(for:destination)` modifiers inside of lazy containers are no longer evaluated. `.navigationDestination(isPresented:destination:)` and `navigationDestination(item:destination)` will log warning when used in lazy containers. Lazy containers in this context include: `List`, `LazyVGrid`, `LazyHGrid`, `LazyHStack`, `LazyVStack` `Table`, and `TabView`. If using `navigationDestination`s in lazy containers, users will see logged errors at runtime. Lift the modifiers higher up in the view hierarchy so they are outside of the lazy containers. Allowing navigation destination modifiers in lazy containers had two significant costs: (1) app navigation state could be undefined if a navigationDestination had been scrolled off screen (2) The navigation system had to explore all list contents to ensure navigation destinations remained up to date. Only allowing these modifiers outside of lazy containers improves app navigation reliability and performance.  (117998693)
- Fixed an issue that caused SwiftUI gestures to trigger simultaenously with `UIControl` subclasses or gestures in `UIViewRepresentable` views.  (119335307)
- Fixed: Views at the root of a `NavigationStack` will now always have matching `onAppear` and `onDisappear` callbacks.  (119737698)
- Fixed: The order of `ShapeStyle` compositing modifiers is now honored with respect to shadows. Previously in `fill(style.blendMode(…).shadow(…))` the added blend mode would also apply to the shadow, that is no longer the case. The blend mode modifier must be added after the shadow modifier to affect it. As a consequence, the fill and any shadows added can now use different blend modes. Similar rules apply to `ShapeStyle.opacity()` except that outer `opacity()` modifiers multiply with inner modifiers, e.g. in `fill(style.opacity(0.5).shadow(…).opacity(0.5))` the shadow is drawn with 50% opacity (of whatever `style` draws) and `style` itself draws with 25% opacity.  (119738072)
- Fixed an issue where Popover presentations automatically dismiss if they go outside the safe area.  (120458490)
- Fixed: The meaning of the boolean value passed to the `ContentTransition.numericText(countsDown:)` function has been flipped for apps deployed prior to iOS 18 aligned releases.  (120561508)
- Fixed: Gestures might not pick up a modified content shape, such as when increasing the tappable area of a button.  (120938385)
- Fixed: A `Picker`’s current value label does not default to the first option anymore when initialized with an invalid selection.  (121871839)
- Fixed: Resolved an issue where rapidly toggling the visibilility of columns in a NavigationSplitView could cause the sidebar to become stuck in either the visible or hidden position.  (122840735)
- Fixed: Sidebar headers no longer respond to increased prominence.  (123518195)
- Fixed an issue when a `sheet` modifier is removed from a view hierarchy. This can happen if the `sheet` modifier is in one branch of an `if` statement and the statement’s condition changes. For apps linked on or after iOS 18 and aligned releases, when a `sheet` modifier is completely removed from the hierarchy, the binding associated with the sheet will not be reset.  (123742063)
- Fixed: `ForEach` child views are no longer re-evaluated unconditionally, only when a parameter of the `ForEach` view might have changed.  (123902210)
- Fixed: Apps might crash when nesting a TabSection inside of another TabSection.  (123928013)
- Fixed: Scroll views have improved behavior in right to left languages when the size of their content is smaller than the size of their container.  (124008045)
- Fixed: Elements along a `NavigationPath` or the data structure passed to the `path` parameter of `NavigationStack(path:root:)` are now compared more efficiently. Any side-effects from setting a `path` equal to itself are no longer reliable and likely will not occur.  (125093883)
- Fixed: The state of the root view of `UIHostingConfiguration` is now reset before the associated cell is displayed.  (125100960)
- Fixed: `SceneBuilder`, `WidgetBundleBuilder`, `TableColumnBuilder`, `TableRowBuilder`, `CommandsBuilder`, and `ToolbarContentBuilder` now diagnose unsupported `if #available` conditions at compile time instead of crashing at run time.  (125379937)
- Fixed: Resolved an issue where context menus with custom previews could not be interacted with.  (125517121)
- Fixed: `UIViewRepresentable`, `NSViewRepresentable` and their view controller variants no longer create a layer with `allowsGroupOpacity` set to true.  (125561916)
- Fixed: In certain scenarios, [`Text(_:style:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(_:style:)) produced suboptimal output, such as choosing an unnecessarily small calendar unit, showing zero values for large calendar units instead of omitting them, or showing seconds in Always On Display.  (125885307)
- Fixed: [`Text(timerInterval:pauseTime:countsDown:showsHours:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:)) was redacting the seconds value even when the timer was paused, had not started yet, or had already reached its end.  (125885429)
- Fixed: When applying a `searchable()` modifier to a `TabView`, the tab view will reset the search state when switching tabs.  (125926765)
- Fixed: Resolved an issue where scroll views would not receive touches if placed near a tappable control. When rebuilt with the newer SDK, make sure that small buttons and tap targets are correctly enlarged. You can use the `contentShape` modifier.  (126232279)
- Fixed: `DocumentGroup` scenes that do not allow document editing, created via `DocumentGroup(viewing:viewer:)`, will not render the document view.  (127076044)
- Fixed: NewDocumentButton() within DocumentLaunchView fails to create a document when pressed.  (127389818)
- Fixed: TabView customization emits runtime errors if customization identifiers are not provided for tabs with `automatic` customization behavior.  (127442031)
- Fixed: Some NavigationLinks in the deprecated `NavigationView` might not work.  (128358023)
- Fixed: Sheets presented with the `.sheet` modifier will have `FittedPresentationSizing` by default. This can cause sheets to appear too narrow or too large, depending on their contents. This is incorrect. The default presentation sizing should be `.form`.  (128902804)
- Fixed: Deprecated `NavigationLinks` links with an `isActive` argument that are wrapped with a get/set `Binding` derived from another `Binding` might not update the destination view if the derived binding updates too late.  (129018685)
- Fixed: In the Swift 6 language mode, the `@Entry` macro now works with non-`Sendable` types if the type of the entry is declared explicitly.  (129073803)
- Fixed an issue where the name passed to the `gesture` modifier would not be available when resolving UIKit dependencies.  (129590852)

##### Tipkit

###### New Features

- The new `TipGroup` API and `CloudKitContainer` syncing will be made available via an upcoming beta SDK release.  (129425412)

##### Translation

###### New Features

- Users can translate text and display results in app. See the `TranslationSession` class, and learn more in the WWDC24 video “Meet the Translation API.”  (112844581)
- Translation now supports translating Hindi in the Translate app, System-wide translation, Safari translation, and the new Translation APIs.  (116622913)

###### Resolved Issues

- Fixed: When using `.translationPresentation()` on an iPhone, the background above the sheet blocks the presenting view instead of letting it show through.  (128504309)

##### Uiapplication

###### Resolved Issues

- Fixed: Applications built with iOS 18, iPadOS 18, Mac Catalyst 18, or tvOS 18 SDKs will call to the deprecated method `UIApplication.openURL(_:)`. The specified URL will not open and will always return `false`.  (125695759)

##### Uikit

###### Resolved Issues

- Fixed: `UITabGroup.managingNavigationController` does not work as expected.  (126277771)
- Fixed: Creating a new document in using “+” sign in “Recents” tab of UIDocumentBrowserViewController might fail.  (128520498)
- Fixed: tabBarController(_:didSelectTab:previousTab:) is not called when a child of a `UITabGroup` is selected.  (128697021)
- Fixed: Tab titles are missing in iPad tab bars for RTL languages.  (130154177)

###### Deprecations

- If `UIImage(named:)` was called with the name of an app icon, it would previously return an undefined image of the icon set, without any masking or shadowing applied. On iOS 18, it now returns nil. To display an icon within the app itself, add the desired image to the asset catalog as an image set.  (130491812) (FB14052579)

##### Vision Framework

###### Deprecations

- `faceCaptureQuality` is now replaced by `captureQuality.score` on `FaceObservation`.  (132508104)

##### Wallet

###### New Features

- To help prevent fraud, when adding an ID to iPhone, the user might be asked to take a Live Photo instead of, or in addition to, conducting a series of head and facial movements. The Live Photo is evaluated by the device and Apple to help ensure that the photo being submitted is of a live person and that the same live person is submitting the photo.  (129338051)

###### Resolved Issues

- Fixed: Sharing your ID in Wallet within apps is not available when Require Face ID for Wallet is enabled.  (128775860)

##### Wallet Apple Pay

###### Known Issues

- Users with an Apple Watch might be prompted to reauthorize Connected Accounts in Wallet on iPhone.  (129127520)  Wait for iPhone and Apple Watch to synchornize. If the issue persists after several minutes, try reauthorizing the connection on iPhone.

##### Watch Faces

###### Resolved Issues

- Fixed: In Apple Watch > Face Gallery on iPhone, complications for the Podcasts and Music apps are unavailable.  (131747921)

##### Weatherkit

###### Resolved Issues

- Fixed: HistoricalComparisons data will not be returned unless it is requested with other weather datasets (e.g. CurrentWeather).  (107204312)
- Fixed: Returned HistoricalComparisons conditions, such as precipitation, might have placeholder values for baseline and currentValue.  (126496817)
- Fixed: Responses for more than 90 days of DayTemperatureSummary and DayPrecipitationSummary data might be slow to return.  (127768828)
- Fixed: Some PrecipitationStatistics fields such as averagePrecipitationProbability and averageSnowfallAmount might show placeholder values.  (128008885)
- Fixed: WeatherKit v2 is currently available only for Swift, not for the REST API.  (128024852)

##### Widgetkit

###### Resolved Issues

- Fixed: Adopting ‘autoPresentConfigAfterAdding’ currently doesn’t auto present config sheet for widgets or controls.  (114470520)
- Fixed: Disabled and privacy-redacted control states do not render properly for control widgets used with the Action button.  (125867980)
- Fixed: Control widget label views might not be able to read redaction reasons from the environment.  (126232534)
- Fixed: The `promptsForUserConfiguration()` modifier has no effect for control widgets in Control Center, the Lock Screen, and the Action button.  (126862283)
- Fixed: ControlCenter.currentConfigurations does not include configured control push tokens.  (127601613)
- Fixed: An error building a control template that states “Template request failed: WidgetKit.ChronoError.AppIntent.conversionFailure(underlyingError: AppIntent has missing parameter value for ’timerName’” might occur. Users might need to set a default value in the initializer of @Parameter, or using the default method on Query.  (129066701)
- Fixed: Widget extensions using ControlWidgetButton and ControlWidgetToggle will crash on iOS 18 beta 5 and later when built from Xcode 16 beta 4 and earlier.  (130760581)

###### Known Issues

- For control widgets that specify both a subtitle and value, Control Center displays only the subtitle.  (127906735)
- Images used in a ControlWidgetConfiguration that are loaded from the app extension’s bundle might glitch when using a symbol effect content transition.  (131789007)  Apply the .contentTransition(.identity) view modifier to the Image.

##### Widgets

###### Resolved Issues

- Fixed: Resizing widgets on the home screen in RTL might not work as expected.  (128625613)
- Fixed: If tinting is enabled for the home screen shortly after updating, the widgets might appear with the incorrect background color until it reloads automatically by the system.  (128701638)

###### Deprecations

- Legacy Today View extensions are removed in iOS 18.  (116246167)

##### Wifi Calling

###### Resolved Issues

- Fixed: T-Mobile Users will not be able to initiate/receive wifi calls on secondary devices that are signed onto the same iCloud account.  (130227345)

## See Also

- [iOS & iPadOS 18.6 Beta Release Notes](ios-ipados-18_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.5 Release Notes](ios-ipados-18_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.4 Release Notes](ios-ipados-18_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.3 Release Notes](ios-ipados-18_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.2 Release Notes](ios-ipados-18_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.1 Release Notes](ios-ipados-18_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-18-release-notes)*