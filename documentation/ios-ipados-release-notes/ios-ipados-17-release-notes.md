# iOS & iPadOS 17 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 17 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 17. The SDK comes bundled with Xcode 15, available from the Mac App Store. For information on the compatibility requirements for Xcode 15, see [`Xcode 15 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15-release-notes).

##### General

###### Resolved Issues

- Fixed: Devices with a large number of installed apps will display an Apple logo with progress bar for an extended period while the file system format is updated. This is a one-time migration when upgrading to iOS 17 beta for the first time.  (109431767)

##### 3d Objects

###### Resolved Issues

- Fixed: Freeform - The ability to add 3D Files to a board is currently unavailable on iOS/iPadOS Beta 3.  (111197819)

##### Accelerate

###### New Features

- Spatial - Introduced trigonometry functions for [`Spatial angle type`](https://developer.apple.comhttps://developer.apple.com/documentation/spatial/angle2d#4180998).
- Introduced spherical linear interpolation for [`Spatial rotations`](https://developer.apple.comhttps://developer.apple.com/documentation/spatial/rotation3d/4157007-slerp).
- Introduced  swing-twist decomposition for [`Spatial rotations`](https://developer.apple.comhttps://developer.apple.com/documentation/spatial/rotation3d#4130747).
- BNNS - Introduced [`BNNSRandomFillCategoricalFloat`](https://developer.apple.comhttps://developer.apple.com/documentation/accelerate/4126856-bnnsrandomfillcategoricalfloat) that fills a tensor with random values from the categorical distributions with event probabilities.
- Introduced [`k-nearest neighbors calculation`](https://developer.apple.comhttps://developer.apple.com/documentation/accelerate/bnns#4164142).
- vImage - Introduced [`vImageConvolveFloatKernel_ARGB8888`](https://developer.apple.comhttps://developer.apple.com/documentation/accelerate/4172614-vimageconvolvefloatkernel_argb88) that applies convolution to 8-bit-per-channel, 4-channel interleaved images using 32-bit floating-point weights.
- Introduced [`vImageSepConvolve_ARGB8888`](https://developer.apple.comhttps://developer.apple.com/documentation/accelerate/4172615-vimagesepconvolve_argb8888) that applies separable convolution to 8-bit-per-channel, 4-channel interleaved images.
- Added flood fill, perspective transform, and new lookup table transforms to [`vImage.PixelBuffer`](https://developer.apple.comhttps://developer.apple.com/documentation/accelerate/vimage/pixelbuffer).  (105830806)

##### Accessibility

###### Resolved Issues

- Fixed: VoiceOver might not speak predictive text in some text fields.  (108858169)
- Fixed: After creating a Personal Voice, you might not be able to select this voice to use with Live Speech.  (109580709)

##### Airdrop

###### Resolved Issues

- Fixed: With any Classroom class set up, the AirDrop browser on teacher and student devices will not show any device.  (111254299)
- Fixed: On iPad, in Settings > General > AirDrop, a switch is shown labeled “Bringing Devices Together”.  This switch is without function on iPad.  (112292330)

##### Airplay

###### Resolved Issues

- Fixed: The AirPlay picker list might not populate, except for the current route.  (109610361)
- Fixed: AirPlay mirroring isn’t currently available on iPad Pro (10.5-inch) or iPad Pro (12.9-inch) (2nd generation). Using iPad as an extended display for a Mac might also be affected.  (109683501)

##### Airpods

###### New Features

- To test new features such as Adaptive Audio, Personalized Volume, and Conversation Awareness, developers need to install AirPods beta firmware. To learn more, see [`Installing Apple Beta Software`](https://developer.apple.comhttps://developer.apple.com/support/install-beta/)  (110183983)
- With Personalized Volume, when watching third party media, a volume slider might show up.  (110266313)
- Conversation Awareness might react to self-made sounds such as humming, throat clearing, and might fail to end automatically when there is ongoing speech nearby.  (110266324)
- Conversation Boost in Control Center Hearing Module will not turn on the feature.   (110266328)

###### Resolved Issues

- Fixed: Press and Hold AirPods in Settings on iOS and macOS for AirPods will only save the noise control rotations on the local device.  (110266311)
- Fixed: FaceTime calls from iOS answered with macOS with AirPods stem might not able to mute.   (110266339)
- Fixed: Spotify App on macOS will automatically route audio from Spotify on iOS without playing audio.  (110266347)
- Fixed: AirPods color might be inverted in dark mode in the tutorial cards for Adaptive Audio.  (110266361)

##### App Intents

###### Resolved Issues

- Fixed: The `DeprecatedAppIntent` protocol might not show the App Intent as deprecated in the Shortcuts app.  (103277731)
- Fixed: UI shown in Widget configuration and the Shortcuts editor might not respect the `size` of an array `@Parameter`.  (109050453)
- Fixed: Widget configuration, Focus Filters, and Shortcuts editor might not allow some `Measurement` dimensions to be configured.  (109114787)
- Fixed: The Shortcuts App might quit unexpectedly on launch if certain App Intents-providing apps are installed.  (109781493)
- Fixed: The “isDiscoverable” static method on an App Intent might not function correctly.  (111268992)

##### Apple Studio Display

###### Resolved Issues

- Fixed: Unplugging Apple Studio Display while playing audio might cause the display to continue looping the last second of audio.  (105232584)

##### Assistive Access

###### New Features

- Assistive Access provides an alternative iOS experience. Assistive Access can be configured and enabled in Settings > Accessibility > Assistive Access. To end Assistive Access, triple-click side or home button, and type in the Exit Passcode that was configured.  (109227206)

###### Resolved Issues

- Fixed: While in a call, the End Call button might become inoperative.  (107597320)
- Fixed: When setting up Assistive Access with Calls set to receive calls from Selected Contacts, calls might not be received.  (110815616)

##### Audio

###### Resolved Issues

- Fixed: Some wired headphones with Lightning connector might experience audio playback interruption.  (112384341)

##### Audio Codecs

###### Deprecations

- The QDesign audio codecs (qdmc & qdm2) and Qualcomm PureVoice audio codecs (qclp & qclq) are no longer supported.  (82414419)

##### Authentication Services and Passkeys

###### New Features

- The Credential Provider API for password managers has been expanded to support passkeys. Credential providers can save and offer passkeys for apps and websites across the system.  (83501802) (FB9651656)
- `ASSettingsHelper` allows password manager apps to directly open the Settings view where the Credential Provider Extension for system-wide Password AutoFill and passkey sign-in can be enabled. `ASSettingsHelper` also allows verification code (TOTP) apps to directly open the Settings view where you can configure which app opens verification code setup links.  (106351958) (FB12039478)

##### Camera and Avfoundation Capture

###### Resolved Issues

- Fixed: On iPhone 14 and 14 Plus models third-party camera applications might fail to capture images, and the built-in Camera app and third-party applications using the new Deferred Processing API might fail to process final images.  (113158045)

##### Car Key

###### Resolved Issues

- Fixed: Car keys shared from Android to iOS/watchOS cannot be added to Wallet app.  (104402733)
- Fixed: Car keys shared from Android to iOS/watchOS cannot be added to Wallet app  (110800534)

##### Carplay

###### Resolved Issues

- Fixed: Following a short disconnection from CarPlay, Maps might present a blank map view while other information remains visible. This issue doesn’t affect Apple Maps in the CarPlay Dashboard.  (109433602)
- Fixed: During navigation using Apple Maps, upcoming turn information might not be displayed correctly in the vehicle’s instrument cluster or heads-up display.  (109437630)
- Fixed: For users in vehicles that support focus input with a knob controller or trackpad, the Now Playing screen might not correctly display which control is focused.  (110609967)
- Fixed: Missing progress bar progression on CarPlay Now Playing widget.  (110845144)

##### Cellular

###### Resolved Issues

- Fixed: iPad (6th generation) (Wi-Fi + Cellular) might display No Service after toggling Settings > Cellular > Cellular Data.  (109705637)

##### Center Stage

###### Resolved Issues

- Fixed: The user cannot disable Center Stage in Control Center for FaceTime when using an Apple Studio Display’s camera. This affects iPads without a front-facing Ultra Wide camera.  (109838002)

##### Check in

###### Resolved Issues

- Fixed: If a Check In is set and the device goes offline, there might be inconsistency between what was requested to be shared with the Check In recipient and what is actually shared.  (108265124)
- Fixed: Siri announcements might repeat part of the incoming Check In notification.  (109409441)
- Fixed: The state might become disassociated, leaving a Live Activity visible after the session ends.   (110066137)
- Fixed: Check In isn’t currently available in China.  (110069236)

##### Content Caching

###### Resolved Issues

- Fixed: The current state of Content Caching in Settings might not be displayed correctly.  (109496539)

##### Content Restrictions

###### New Features

- Siri Explicit Language filter can’t be enabled for the following locales: he-IL and tr-TR.  (109157875)

##### Enterprise Software Updates

###### Known Issues

- Shared iPad will sit in “Prepared” state when using Declarative Device Management to enforce a software update.  (111934749)  Use legacy MDM commands to update the shared iPad.

##### Esim Transfer

###### Resolved Issues

- Fixed: eSIM transfer using “Transfer From Nearby iPhone” between devices using different iCloud accounts, or devices without an iCloud account might fail.  (109543664)

##### Facetime

###### Resolved Issues

- Fixed: Black rectangle is shown behind the reaction picker while it is being animated. After animation completes, the picker has black corners.  (113222206)

##### Facetime Handoff

###### Resolved Issues

- Fixed: Facetime handoff to another device might result in call drop or no media.  (110126569)

##### Facetime on Apple Tv

###### Resolved Issues

- Fixed: Guest Pairing doesn’t work if Apple TV is connected via Ethernet.  (107163191)
- Fixed: If a phone is already a Connected Camera, answering a FaceTime call on that phone and then moving to Apple TV might result in a dropped call.  (107187159)
- Fixed: Moving the FaceTime call from Apple TV to iPhone by tapping “Switch to phone” might result in a dropped call.  (108810085)
- Fixed: Duplicate participants might appear when moving a call from iPhone to Apple TV.  (110087471)
- Fixed: FaceTime call might end suddenly within first minute.   (111099303)

##### Foundation

###### New Features

- Introduced `TermOfAddress` which describes how a person should be addressed in language. This can be used in conjunction with Automatic Grammar Agreement to refer to people in a string using their preferred pronouns and grammatical agreement in English, Spanish, Portuguese, French, Italian, and German.  (99745330)
- Foundation now supports grammatical agreement with a detached phrase using the `agreeWithConcept` markdown attribute.  (102595293)

##### Freeform

###### Resolved Issues

- Fixed: Strokes drawn using Beta 2 might appear distorted when viewed on devices running Beta 1.   (107901155)
- Fixed: The Follow Me feature will only work when collaborators are on the same Beta version.  (110656281)

##### Health App Clinical Health Records

###### Resolved Issues

- Fixed: Upon deletion of a clinical health record account on an iOS device, subsequent sign-ins might fail to sync to other devices signed into the same iCloud Account.  (111468979)

##### Health App on Simulator

###### Resolved Issues

- Fixed: Default simulator locale is set to `en-001`. Clinical Health Records and Sharing with doctor features are missing in Health App on Simulator.  (109408273)

##### Health Clinical Vitals Category Room

###### Resolved Issues

- Fixed: Viewing any Clinical Vitals category rooms from Search has black background in Light mode, making some texts illegible.  (110847243)

##### Health Medications

###### Resolved Issues

- Fixed: Follow up notifications might not display as expected and notifications might unexpectedly disappear from the lock screen.  (109246855)
- Fixed: Previously archived medications might appear unexpecetedly in the active Medication Schedule section and also trigger reminders.  (110029786)
- Fixed: Users are not able to change the shape of an existing Medication.  (111303794)

##### Home

###### Resolved Issues

- Fixed: Pairing the first Matter accessory in a new Home will fail when paired by selecting the accessory from the nearby accessories list.  (109905770)
- Fixed: Existing Home Widget(s) will stop working when users update from Beta 1 to Beta 2 on iOS and macOS.  (110343163)
- Fixed: Media playback controls might not appear in the Home app for some 3rd party AirPlay speakers.  (113282855)

##### Home Widgets

###### Resolved Issues

- Fixed: Users might encounter an issue that results in their Home Widgets showing “No Accessories” even though they are configured properly.  (110424040)
- Fixed: Accessory with multiple services configured are filtered out and not shown on the Widget.  (110547396)

##### Icloud Backups

###### Known Issues

- The first backup on a post beta 4 build when users have been on beta 4 prior might take a longer time to complete if there are a large number of message attachments.  Both automatic and manual backups might take a longer time to complete and get deferred over days which can lead to users seeing that the device has not been backed up in a while.  (110840177)  Turn off and delete iCloud backups and turn it back on: Settings -> iCloud Backup -> Select the device -> Turn off and delete from iCloud To turn it back on Settings -> iCloud Backup -> Toggle on Backup this phone

##### Imageio

###### Resolved Issues

- Fixed: Image corruption might occur when rendering some PNG files that contain a color palette table with a separate alpha.  (110822373)
- Fixed: Some devices might show Health and/or Wallet icon image corruption.  (110906101)

##### Live Voicemail

###### New Features

- Live Voicemail can’t be shared.  (105513708)

###### Resolved Issues

- Fixed: Voicemail notification sound will play even when the device is set to silent mode.  (110112187)

##### Localization

###### Resolved Issues

- Fixed: Some content might appear in English. Some strings might appear clipped.  (109393568)

##### Lockdown Mode

###### Resolved Issues

- Fixed: If 2G cellular service (Settings > Cellular) is selected before enabling Lockdown Mode, it might not be disabled by Lockdown Mode on all cellular networks.  (109406777)

##### Mail

###### Resolved Issues

- Fixed: Mail is unable to fetch new email from IMAP servers using the NAMESPACE extension.  (109102644)
- Fixed: When updating to Beta 3, mail will re-download emails again if an account exceeds 10000 messages.  (110809614)

##### Maps

###### Resolved Issues

- Fixed: When a `LinearGradient` stroke is used with a `MapPolyline` in SwiftUI, the specified gradient color might be ignored.  (106152300)
- Fixed: When using `Map`, Xcode emits a runtime warning that “Publishing changes from within view updates is not allowed.”  (106174743)
- Fixed: At certain zoom levels, the title of a selected `MKMarkerAnnotationView` can overlap other marker titles.  (109491779)

##### Media

###### New Features

- Added support for Managed Media Source on macOS and iPadOS, and added support as a preview on iOS.  (30320350) (FB5689561)

###### Resolved Issues

- Fixed: MP3 files with malformed ID3 tags will fail to play  (110230071)

##### Meshing

###### Resolved Issues

- Fixed: In certain edge cases, for example floors under curved walls, meshing of floor or walls might appear broken.  (110125996)

##### Messages

###### New Features

- iMessage apps might behave unexpectedly in landscape orientation.  (100736697)
- Sticker pack apps appear when the new Stickers app is invoked from outside of Messages. For apps such as Notes and Freeform, the new Stickers app can be invoked from Emoji Keyboard Recents and Markup. For third party apps, Stickers can be invoked from the Emoji Keyboard Recents.  (106685842)

###### Resolved Issues

- Fixed: The transcription for long audio messages is truncated without a way to expand and view the full transcription.  (107174385)
- Fixed: Stickers might disappear after a long press.  (109059570)
- Fixed: Unexpected visual artifacts might appear when the transcription is inserted while sending an audio message.  (109799338)
- Fixed: Messages app might be blank on first unlock after software update.   (112982988)

###### Known Issues

- The Catch up affordance might display incorrectly.  (109468262)  Leave and return to the affected conversation.

##### Metal

###### Resolved Issues

- Fixed: MetalFX `MFXTemporalScalingEffect` class will quit unexpectedly on iPhone 14 and iPhone 14 Pro.   (110191344)

##### Metal Ray Tracing

###### Resolved Issues

- Fixed: The methods `assume_curve_control_point_count`, `assume_curve_basis`, and `assume_curve_type` on `intersection_params` and `intersector`, the methods `get_curve_control_point_count`, `get_curve_basis`, and `get_curve_type` on `intersection_params`, and the related `curve_basis` and `curve_type` enumerations, are not supported in the Metal Shading Language.  (104142182)
- Fixed: After initializing an `intersection_query` with an acceleration structure using `max_levels<Count>` where `Count > 2`, calls to `next()` might cause the GPU to restart.  (108863335)
- Fixed: Reflection returned via the new `{Render|Compute|Tile}PipelineWithDescriptor` API for ray tracing pipelines might be incorrect.  (109850134)

##### Networking

###### New Features

- iPhone and iPad devices running iOS 17 beta support joining wired 802.1X networks. Apple TV devices running tvOS 17 beta also support joining wired 802.1X networks.  (12867782)
- `URLSession` supports resumable uploads in HTTP. Just like download tasks, upload tasks can now be paused and resumed if the server supports the latest protocol draft. To learn more, see [`Resumable Uploads for HTTP`](https://developer.apple.comhttps://www.ietf.org/archive/id/draft-ietf-httpbis-resumable-upload-01.txt).  (68890505)
- Apple devices now support connection to 802.1X networks using EAP-TLS with TLS 1.3 (EAP-TLS 1.3). EAP-TLS 1.3 further improves security and privacy by always providing forward secrecy, never disclosing the peer identity, and by mandating use of revocation checking when compared to EAP-TLS with earlier versions of TLS.  (74526852)

###### Resolved Issues

- Fixed: For apps linked on or after iOS 17 and aligned OS versions, App Transport Security now requires secure connections to external IP addresses by default. For more information on these requirements, see [`Preventing Insecure Network Connections`](https://developer.apple.comhttps://developer.apple.com/documentation/security/preventing_insecure_network_connections). Exceptions can be made using [`NSExceptionDomains`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nsapptransportsecurity/nsexceptiondomains), which now supports exceptions for individual IP addresses and ranges specified in classless inter-domain routing (CIDR) notation.  (101967030)
- Fixed: For apps linked on or after iOS 17 beta, macOS 14 beta, watchOS 10 beta, and tvOS 17 beta, the `Transfer-Encoding` header field of a streamed `HTTP/1` request is set to `chunked` instead of `Chunked`.  (107390029)
- Fixed: Apps which use IPv4 traffic via NAT464 on an IPv6-only network, including certain mobile carriers, might not work.  (109750536)

##### Newsstand

###### Deprecations

- NewsstandKit has been removed.  (101054446)

##### Notes

###### Resolved Issues

- Fixed: Some content might temporarily disappear from notes.   (108843547)

##### Phone

###### Resolved Issues

- Fixed: Phone app may be badged with an incorrect number of unread voicemails.  (113044765)

##### Phone Software Update

###### Resolved Issues

- Fixed: Users who installed prior seed builds may have accumulated high System disk usage related to cached shared names & photos.  (112927795) (FB12759629)

##### Photos

###### New Features

- A new `PHContentEditingOutput.renderedContentURL(for:)` API adds support for `UTType.heic` encoded rendered image content.  (109861295)

###### Known Issues

- Applications providing image content via `PHContentEditingOutput.renderedContentURL` in formats other than `UTType.jpeg` will fail with an `.invalidResource` error.  (110068158)

##### Pre Filled Titles for Events and Reminders

###### New Features

- Messages now supports machine learning based pre-filled titles for English events and reminders. Tap or long-press the highlighted date/time in an SMS or iMessage conversation and select ‘Create Event’ to trigger this feature.  (110889506)

##### Privacy

###### Resolved Issues

- Fixed: When a user clears their Significant Locations history, this change will not be immediately reflected in Photos and it could take up to a week or more for the change to be reflected.  (106171658)
- Fixed: Time in Daylight is supported on Apple Watch Series 5 and later. However, when using a model of Apple Watch which doesn’t support Time in Daylight, the privacy toggle switch is still displayed even though toggling it has no effect. On Apple Watch, the toggle is located in Settings > Privacy & Security > Health > Time in Daylight. On iPhone, the toggle is located in Watch app > Privacy > Time in Daylight.  (108907052)

##### Proximityreader

###### Resolved Issues

- Fixed: Calling the [`prepare(using:)`](https://developer.apple.com/documentation/proximityreader/mobiledocumentreader/prepare(using:)) method on a [`MobileDocumentReader`](https://developer.apple.com/documentation/proximityreader/mobiledocumentreader) instance might fail if the device is set to certain languages and regions.  (110013699)

##### Reactions

###### Resolved Issues

- Fixed: When using iPhone 14 or iPhone 14 Pro as continuity camera, gesture detection can stop working when center stage is enabled.  (109268172)
- Fixed: Reactions aren’t currently available when using video conferencing apps in Safari.  (109789920)

##### Safari

###### Resolved Issues

- Fixed: Safari might offer search suggestions while in Private Browsing by using an on-device model. The search terms are not sent from the device to a search provider.  (105606453)
- Fixed: Safari might quit unexpectedly when focusing the Smart Search field on iPhone in portrait orientation if a search hasn’t previously been done using the Smart Search field.  (109685060)
- Fixed: Setting a profile color might not be reflected in the Start Page background.  (109742827)
- Fixed: When creating a new Safari Profile, extensions might be unexpectedly turned on or off.  (109796433)
- Fixed: Separate Safari profiles might incorrectly display history results in the search UI from other profiles.  (109798974)

##### Screen Time

###### Resolved Issues

- Fixed: Visiting Screen Time > Tapping “See All Activity” > Opening an app, website, or category from the “Most Used” list might lead to a ~25s hang before the usage report for the app, website, or category appears.  (109490608)
- Fixed: Screen Time usage and settings for App Limits, Always Allowed, and Downtime are lost after updating to iOS 17 beta.  (109910575)

##### Settings

###### Resolved Issues

- Fixed: In Settings > General > About, the available storage might be inconsistent with the storage usage reported in Settings > General > [iPhone, iPad] Storage. The storage usage reported in Settings > General > [iPhone, iPad] Storage is accurate.  (109051437)

##### Settings %7c Passcode

###### Resolved Issues

- Fixed: When changing the device passcode, the “Passcode Options” link does not appear and the passcode cannot be changed from a numeric one to an alphanumeric one.  (110705323)

##### Shareplay

###### Resolved Issues

- Fixed: Connecting SharePlay in-car sessions by scanning the QR code might not work.  (109275769)
- Fixed: When user disables the “Discoverable by Nearby Contacts” setting or starts playing something other than Apple Music, it will cause the advertisement to stop and will be unable to resume advertising again for that session.  (111420528)

##### Shazamkit

###### Resolved Issues

- Fixed: `SHManagedSession.State` is unavailable.  (109670750)
- Fixed: `SHLibrary.default.items` is unavailable.  (109670918)

##### Skadnetwork

###### Resolved Issues

- Fixed an issue causing developer copies of postbacks failing to send or containing an incorrect conversion-value or coarse-conversion-value.  (109471751)
- Fixed a bug that allowed conversion values to be negative. Conversion values can now only fall within the expected range of 0-63.  (113361952)

##### Software Migration

###### Resolved Issues

- Fixed: In regions which don’t allow 5GHz band to be used, migrating from an Android device to an iPhone might fail to complete successfully.  (110983759)

##### Software Update

###### Resolved Issues

- Fixed: Certain 2017 model iPads might fail to update to iOS 17, and will revert back to the pre-existing starting OS.   (110281164) (FB12228311)

##### Stage Manager

###### Resolved Issues

- Fixed: The gesture to open the switcher doesn’t work while using Stage Manager.  (109580340)

##### Standby

###### New Features

- The brightness slider isn’t functional while in StandBy.  (106203217)

###### Resolved Issues

- Fixed: If an app is deleted and its widget is in the StandBy widget stack, the deleted app widget isn’t removed.  (105255305)
- Fixed: Widgets in StandBy display content while in DownTime or when restricted by ScreenTime.  (105255640)
- Fixed: While in red mode, Solar Clock isn’t legible.  (108919386)
- Fixed: Widgets in the StandBy widget gallery might appear clipped.  (108924188)
- Fixed: Incoming call alerts aren’t visible while editing widgets in StandBy.  (108924275)
- Fixed: Your device might become unresponsive while in StandBy.  (111607569)

##### Stickers

###### Resolved Issues

- Fixed: Freeform - On iPad and iPhone emoji with skin tone options cannot be inserted onto the canvas.  (110253100)

##### Storekit

###### New Features

- You can use the new [`showManageSubscriptions(in:)`](https://developer.apple.com/documentation/storekit/appstore/3803198-showmanagesubscriptions) API with a subscription group ID to show a user the subscriptions they own within a subscription group, along with the other plan options available in that group.  (87853800)
- Users have access to the new `Product.SubscriptionInfo.Status.all` sequence to get the status for each of your app’s subscription groups. One can use the new `subscriptionStatus` property on the latest [`Transaction`](https://developer.apple.com﻿https://developer.apple.com/documentation/storekit/transaction) value for a subscription to access the full status information.  (102064614)
- StoreKit 2 now provides a collection of UI components to help merchandise in-app purchases. Use `ProductView`, `StoreView` and `SubscriptionStoreView` to add in-app purchases to an app with just a few lines of code.  (102066107)
- Users can access in-app purchase product metadata and entitlement information from a SwiftUI view using new view modifier APIs in StoreKit. Declare a view as dependent on a single product or collection of products using `storeProductTask(for:priority:action:)` or `storeProductsTask(for:priority:action:)` respectively. Declare a view as dependent on the current entitlement for a product using `currentEntitlementTask(for:priority:action:)`. Declare a view as dependent on the status of a subscription group with `subscriptionStatusTask(for:priority:action:)`. All of the modifiers will start a task to load the data before the view appears, and provide your action with the state of the task as it progresses and whenever the data changes.  (102397222)
- User have access to the new `groupLevel` property of [`Product.SubscriptionInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo) to understand the level of service of a subscription plan.  (103885148)
- Users have access to the new `reason`, and `storefront` properties on [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction) to understand the reason why the transaction was created, and which storefront it is for. The new `renewalDate` property on [`RenewalInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo) to understand if and when a subscription will renew next.  (104246730)
- Users have access to new `groupDisplayName` property of [`Product.SubscriptionInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo) to get the localized display name of a subscription plan’s group.  (105689964)
- The [`subscriptionStoreControlBackground(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstorecontrolbackground) view modifier is available when using StoreKit and SwiftUI. Use this modifier to set the background behind controls in [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) instances within a view to a gradient material effect, or any shape style.  (105690554)
- The [`productViewIconBorder()`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/automaticproductplaceholdericon/4278999-producticonborder) view modifier is available when using StoreKit and SwiftUI. Use this modifier on the icons to provide [`ProductView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/productview) and [`StoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/storeview) to add a standard border around the icon.  (106649532)
- You can now customize the button style used for purchase and subscribe buttons in [`ProductView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/productview), [`StoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/storeview) and [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) instances. Use the [`buttonStyle(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/buttonstyle(_:)-7qx1) view modifier to choose any standard button style, or a custom button style.  (107713282)
- StoreKit Views`ProductView` and `StoreView` have initializers have initializers that give you access to the promotional icon as a SwiftUI view and the various phases of the loading operation. Use initializers such as [`init(id:icon:placeholderIcon:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/productview/4202217-init), [`init(_:icon:)]`(https://developer.apple.com/documentation/storekit/productview/4202214-init), [`init(ids:icon:placeholderIcon:)](https://developer.apple.com/documentation/storekit/storeview/4203378-init), and [init(products:icon:)``](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/storeview/4203382-init) to provide an icon view for each phase.  (110470147)
- The following StoreKit types are renamed: • `DefaultProductViewStyle` is renamed to [`AutomaticProductViewStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/automaticproductviewstyle) • `DefaultSubscriptionStoreMarketingContent` is renamed to [`AutomaticSubscriptionStoreMarketingContent`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/automaticsubscriptionstoremarketingcontent) • `DefaultProductPlaceholderIcon` is renamed to [`AutomaticProductPlaceholderIcon`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/automaticproductplaceholdericon)  (111185321)

###### Resolved Issues

- Fixed: When testing in the sandbox environment, the `groupDisplayName` property on [`Product.SubscriptionInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo) might return an empty string if the localization in the current storefront is not in an approved state. When using the `SubscriptionStoreView` without providing a marketing content view, the automatic view might show the name of the app instead of the subscription group’s display name.  (107206601)
- Fixed the loading animation for [`StoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/storeview) instances displaying a single product.  (110414023)
- Fixed issue where [`loadProduct(withParameters:completionBlock:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/1620632-loadproduct) was called from a background thread.  (110640574) (FB12323139)
- Fixed issue where [`StoreView`](https://developer.apple.com﻿﻿https://developer.apple.com/documentation/storekit/storeview) or [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) content might appear in English, or show a localization key, instead of showing localized text for the App Store storefront.  (110734447)
- Fixed an issue which can cause unexpected layouts when providing a tall view as custom marketing content for a [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview).  (112862984) (FB12748731)

##### Swift

###### New Features

- Properties of @Observable and @Model types currently always require default values or optionality.  (109441094)

##### Swift Charts

###### New Features

- Enable scrolling in a chart using view modifier `chartScrollableAxes(_:)`.  (70444254)
- Use `chartXSelection`, `chartYSelection` and `chartAngleSelection` to enable selection on a chart. If needed, use `chartGesture` to override the default gesture for selection.  (79083764)
- Swift Charts now supports creating pie charts and donut charts using the new `SectorMark` API.  (102309263)
- Pass an `AnnotationOverflowResolution` to the `annotation` modifier to specify how to align an annotation when it would otherwise overflow the bounds of the chart or the plot.  (106009062)
- Use `ChartProxy.plotContainerFrame` to obtain the visible portion of the plot in a scrollable chart. ```swift
 Chart { ... }
 .chartScrollableAxes(.horizontal)
 .chartOverlay { proxy in
     GeometryReader { geometry in
         if let plotContainerFrame = proxy.plotContainerFrame {
             let frame = geometry[plotContainerFrame]
             Path(frame)
                 .stroke(.black, lineWidth: 1)
                 .allowsHitTesting(false)
         }
     }
 }
``` (109675790)

###### Resolved Issues

- Fixed a crash with certain combinations of chart content.  (105197081)
- Fixed an issue where frequent updates to a chart caused unexpected growth in memory footprint.  (107611114)
- Fixed: When a selection gesture goes out of bounds, the selection binding will now be clamped to the nearest data value rather than set to `nil`.  (108398019)
- Fixed: Improved performance and CPU usage for charts with selection bindings.  (108954531)
- Fixed: Scrolling charts might behave unexpectedly on right-to-left languages.  (109129343)
- Fixed: Improved animations for charts in a widget.  (110035011)
- Fixed an issue where the `compositingLayer` chart content modifier caused marks with custom symbols to disappear.  (110399956)
- Fixed an issue where the `compositingLayer` chart content modifier caused annotation boundary resolutions to behave unexpectedly.  (112232314)
- Fixed: Improved performance and CPU usage for scrolling charts with scroll position bindings.  (113149095)

###### Known Issues

- Annotations on a scrollable chart might be clipped.  (109164195)

##### Swiftdata

###### New Features

- Existing `@Query` property declarations might not always correctly infer the model type for predicate and sort descriptor parameters. (Note: the `@Query` attribute is now resolved as a macro, instead of as a property wrapper.) For example, specifying a filter predicate as a parameter to the `@Query` attribute will now require explicitly providing the model type used in the predicate, i.e. `#Predicate<ModelType> { … }` instead of `#Predicate { … }`: ```swift
 @Query(filter: #Predicate<Person> { ... }) var people: [Person]
``` Another example: passing a sort descriptor or key path will now require explicitly providing the model type used for the root type of the key path, i.e. `\ModelType.property` instead of `\.property`: ```swift
 @Query(sort: [SortDescriptor(\Person.name)]) var people: [Person]
 
 @Query(sort: \Person.name) var people: [Person]
``` In all cases, the model type used in the `filter:` and `sort:` parameters is still required to be the same type used as the element in the query’s wrapped array type, and will emit a build error if not.  (109433172)

###### Resolved Issues

- Fixed: Properties with default values are not initialized correctly.  (107887871)
- Fixed: @Query results can appear stale or fail to refresh.  (108385553)
- Fixed: Case value is not stored properly for a string rawvalue enumeration.  (108634193)
- Fixed: Schema migration can fail when nesting non-optional properties inside an optional containing struct.  (108854663)
- Fixed: Properties with .externalStorage are not being stored in peripheral files.  (108972391)
- Fixed: Scene modifier isUndoEnabled does not propagate correctly.  (109373617)
- Fixed: Modeled enum properties with default values won’t compile unless they are fully qualified values.  (109421492)
- Fixed: SwiftData queries will not work with #Predicate { true } and #Predicate { false } will cause a crash.  (109425342)
- Fixed: Conflicting writes from other processes sharing the same file can cause a crash.  (109488127)
- Fixed: `#Predicate` does not support UUID, Date, and URL properties.  (109539652)
- Fixed: `@Query` using `SortDescriptors` based on `.reverse` sorting on strings can fail to fetch results.  (109572633)
- Fixed: Creating a @Query with a sortdescriptor that uses a relationship keypath will crash.  (109626376)
- Fixed: `willSet` and `didSet` observers will prevent `@Model` from properly transforming those stored properties and they will not persist.  (109664186)
- Fixed: SwiftData queries don’t support some `#Predicate` `flatmap` and `nil` coalescing behaviors.  (109723704)
- Fixed: Xcode code generation for SwiftData Models from CoreData xcdatamodels will refer to `originalName` instead of `renamingIdentifier`.  (109782236)
- Fixed: Unsigned applications using Document API without a proper app container might overwrite the default container.  (109784405)
- Fixed: After deleting an item, SwiftUI might attempt to reference the deleted content during the animation causing a crash.  (109838173)
- Fixed: Custom schema migrations with SchemaMigrationPlan will fail.  (110114696)
- Fixed in beta 7: Apps using SwiftData that are built with Xcode 15 beta 6 have known issues when running on iOS 17 beta 6.  (113915428)

###### Known Issues

- SwiftData models with implicitly unwrapped optional properties will generate a compiler error that all stored properties were not set.  (114140139)  Set the value of non-relationship stored properties in the initializer, and mark relationship properties as optional.

##### Swiftui

###### New Features

- `RoundedRectangle` now defaults to the continuous corner style.  (63246947)
- `.onChange` has new overloads where the closure takes 0 or 2 arguments, these new versions will call the new version of the closure (i.e. after the specified value has changed), so any captured properties will have up to date values. The previous overload (which calls the old version of the closure) has been deprecated.  (67344857)
- Spring animations will now default to being critically damped (i.e. a bounce of 0).  (75149732)
- Scenes in Catalyst now support the `windowResizability` modifier.  (84203422)
- Added support for `dialogSeverity` in Catalyst applications.  (95918809)
- Use the `springLoadingBehavior(_:)` view modifier to control spring loading behavior of views. Some views, like `TabView`, default to allowing spring loading, while others, like `Button`, do not. Spring loading refers to a view being activated during a drag and drop interaction. On iOS this can occur when pausing briefly on top of a view with dragged content. On macOS this can occur with similar brief pauses or on pressure-sensitive systems by “force clicking” during the drag.  (96569875) (FB10572945)
- `List`s using the `SidebarListStyle` hosted in primary column of a UIKit `UISplitNavigationController` were previously rendering with an `insetGrouped` appearance.  With this change they will render as the expected `sidebar` appearance similar to if the `List` were hosted in a SwiftUI `NavigationSplitView`.  (96909195)
- Previously all `Section`s inside `List`s using the `SidebarListStyle` received outline disclosure indicators at the top of every `Section` even when a developer did not provide a header for the section. This lead to odd looking floating disclosure indicators.  (98001084)
- Use the `buttonRepeatBehavior(_:)` view modifier to make buttons repeatedly trigger their actions on prolonged interactions.  Apply this to buttons that increment or decrement a value or perform some other inherently iterative operation. Interactions such as pressing-and-holding on the button, holding the button’s keyboard shortcut, and holding down the space key while the button is focused trigger this repeat behavior.  (102156410)
- `Animation.default` now uses a spring animation equivalent to `Animation.spring`. In addition, `Animation.default` is now only equal to itself when using `==`, allowing users to differentiate between animations that were intentionally chosen and those that use the `default` animation.  (103169056)
- During gesture change callbacks, velocity will automatically be tracked so that it can be applied to animations that finish when the gesture finishes.  (103371523)
- When two Text are vertically adjacent (for example in a VStack with no spacer in between) SwiftUI will automatically calculate appropriate spacing. To opt-out if this behavior either place a Spacer or specify spacing parameter to the container view.  (104782785)
- For apps built using the macOS 14 SDK, using `DismissAction` to close a window will default to using `DismissBehavior.interactive`.  (105406945)
- A `NavigationSplitView` collapses into a single column in some situations, such as on iPhone, Apple Watch, or iPad in slide-over. When this happens the columns of the split view are arranged into a stack. By default, the split view automatically decides which column appears as the top of this stack based on the contents of the columns. It considers whether any embedded `List` views have selections and whether any embedded `NavigationStack` views have non-empty paths. `NavigationSplitView` provides new initializers that give users control over which column of the split view appears on top. Use initializers like `NavigationSplitView(preferredTopColumn:sidebar:content:detail:)` or `NavigationSplitView(preferredTopColumn:sidebar:detail:)` and provide a binding specifying the column that should be visible when the split view is collapsed into a stack. When using an app pops the stack, SwiftUI updates the binding.  (106241051)
- When using `@Environment(\.self)` to capture an entire `EnvironmentValues`, SwiftUI will now track which properties are accessed to only invalidate the property when those properties change.  (106310433)
- Use the new `navigationDestination(item:destination:)` overload to present a navigation destination when a bound item is non-`nil`, or to dismiss the destination when the bound item becomes `nil` again.  (106319528)
- Shapes now default to mirroring when in a right to left layout direction.   (107405880)
- Changing from one Gradient value to another will now animate, but only once apps are rebuilt against the new SDK.  (107408691)
- All `Section`s inside `List` and `Table` can be configured to be collapsible using new initializers on Section. Previously all `Section`s inside `List`s using the `SidebarListStyle` received outline disclosure indicators in every header.  Section headers will no longer render this control by default.  An outline disclosure will only be provided in the header if the `Section` is initialized with an `isExpanded` binding to a bool.  This bool represents the `isExpanded` state of the `Section`.  Sections created with an `isExpanded` binding inside a `Table` on macOS will now provide a default outline disclosure indicator to collapse or expand the `Section`.  (107592493)
- The `listSectionSpacing` modifier can now be used within Lists.  (109271050)
- `View.onKeyPress(_:action:)` can’t filter key presses when bridged controls have focus.  (109799056)
- Scenes in Catalyst now support the `defaultSize` modifier.  (110038374)

###### Resolved Issues

- Fixed:`Menu` could not be used with `hoverEffect`.  (67879883) (FB8554520)
- Fixed: `NavigationSplitView` reuses view controllers in more cases, resulting in significantly improved performance. This might change the behavior of code that relies on the life cycle messages sent to `UIHostingController` because such controllers will be created less often.  (88880547)
- Fixed an issue where dynamically enabled buttons (e.g. with a `TextField`) were not updated in alerts.  (95917673) (FB10463211)
- Fixed: `menuStyle(.button)` is compatible with custom button style implementations. Applying a custom `buttonStyle` on a `Menu` is supported.  (96156722)
- Fixed: Scroll environment properties like isScrollEnabled and scrollDismissesKeyboardMode are no longer propagated past nested scroll views.  (99195890)
- Fixed: Gestures could be misaligned if an app was backgrounded while a sheet was presented.  (99202394)
- Fixed: Previously it was possible for views animating their removal via a transition to be drawn above a view with the same zIndex that has not yet been removed. This was unintentional and has now been updated: views transitioning out of the view hierarchy are always drawn below non-removed views with the same zIndex.  (101085960)
- Fixed: Table row identifiers in `ForEach` are now derived from their `ForEach` identifier rather than the `TableRow` identifier within the `ForEach`. In this example, from within a `Table`: ```None
 ForEach(myData) { data in
     TableRow(data.someFieldAlsoOfTypeData)
 }
``` the resulting identifiers used by SwiftUI are now `data.id` rather than `data.someFieldAlsoOfTypeData.id`. If user needs to restore prior behavior, specify the ID explicitly using the `id` of the `ForEach`.  (101174261)
- Fixed: Buttons in toolbars on iOS have improved metrics but support fewer customizations.  (102198062)
- Fixed: LazyVGrid or LazyHGrid has an improved layout when used with fixedSize().  (103075945)
- Fixed: A visual artifact around sheets when rotating iPhone.  (106020927)
- Fixed: The new `.navigationDestination(item:content:)` modifier now works correctly both inside a `NavigationStack` and outside a stack but inside a column of a `NavigationSplitView`. Inside a stack, setting the bound item to a non-nil value will push a view onto the stack immediate above the view containing the modifier. Setting the bound item to a nil value will pop the view. Outside a stack but inside a column of a `NavigationSplitView`, setting the bound item to a non-nil value will replace the root view of the subsequent column. Setting the bound item to a nil value will restore the original root view.  (106106406)
- Fixed: In some circumstances, the first view pushed onto a `NavigationStack` or collapsed `NavigationSplitView` might fail to animate.  (106602046)
- Fixed: When a flexible frame modifier (e.g. frame(minHeight: 100, maxHeight: 200)) is used inside a scroll view the modified view could end up truncating content. This would most often be visible with the content view being a VStack with multiline text.  (107014454)
- Fixed: When scrolling to the end of a scroll view using ScrollViewReader, the final offset will be clamped to the scroll view’s total content size and no longer overscroll.  (107558652) (FB12094127)
- Fixed: Removed a spurious warning, “NavigationLink presenting a value must appear inside a NavigationContent-based NavigationView. Link will be disabled.”  (107877668) (FB12111423)
- Fixed: Views in Lists and Lazy Stacks might be improperly displayed after scrolling.  (108021411)
- Fixed: The [`help(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/help(_:)-9lm7l) modifier now displays tooltips in apps built with Mac Catalyst and iOS apps on Mac.  (108063751)
- Fixed: Suggested search tokens will be hidden by default when the search text is not empty  (108381393)
- Fixed: ScrollView when used with the searchable modifier has an improved transition when presenting or dismissing search on iOS and iPadOS.  (109265624)
- Fixed: Two `NavigationSplitView` initializers taking `columnVisibility` as a value rather than a `Binding`.  (109426553)
- Fixed: Content in the inspector modifier is re-rendered consistently when state changes (FB12319435).  (110623855) (FB12319435)
- Fixed: Inspectors within `NavigationSplitView`s handle navigation bars with scrollable content properly. The navigation bar’s translucency now tracks with the main content’s scroll view. Navigation titles are intentionally not rendered in split-view-nested inspectors when presenting as a trailing column to avoid nested navigation bars. The title is shown when the inspector is preseting as a sheet. Consider using the `.safeAreaInset(edge: .top) { ... }` modifier to overlay a title view that respects scrollable content. In this case, it is recommended to apply `.toolbar(.visible, for: .navigationBar)` on the main content to prevent scrolled content from being visible  the custom title view (FB12546918).  (111932922) (FB12546918)
- Fixed: Inspector respects safe areas when dismissed offscreen in landscape iPhone orientations (FB12728304).  (112748296) (FB12728304)

###### Known Issues

- `View.defaultFocus(_:_:)` isn’t reliable with text controls.  (109750983)  Manually update focus state bindings from an action passed to `View.onAppear(perform:)`.
- The `.presentationBackground(_:)` modifier does not work on `.inspector` (FB12326152).  (110656975) (FB12326152)
- Using the `@Environment(\.dismiss)` callable from within an inspector presentation does not dismiss the inspector. This is a bug.  (111643518) (FB12501848)  Use the `Binding` provided to the inspector initializer to dismiss and present the inspector.
- Using a `NavigationStack` within an `.inspector` within a `NavigationSplitView` can interfere with the split view’s navigation. (FB12567417)  (112018368) (FB12567417)  Either move the inspector modifier  of the `NavigationSplitView`, or remove the `NavigationStack` from the inspector. If the goal is to have a navigation title in the inspector, placing the inspector outside of the split view is recommended to avoid nested navigation bars. If the goal is to have a navigation title in the inspector strictly inside a `NavigationSplitView`, consider using the `.safeAreaInset(edge: .top) { ... }` modifier to add a title compatible with scrollable content. Note that the `.navigationTitle(_:)` modifier will add a navigation title in any inspector construction .
- On iOS, using an `Observable` object’s property as a selection value of a `List` inside `NavigationSplitView` may cause a “Simultaneous accesses to …” error when a list selection is made via tap gesture.  (113978783) (FB12981860)  There is no current workaround for `Observable` properties. Alternatives include factoring out the selection value into separate state stored outside the object, or using `ObservableObject` instead.

##### Swiftui Outline

###### Resolved Issues

- Fixed: Leaf views in `OutlineGroup`s (those views where the `children` keyPath argument has a value of `nil`) are no longer wrapped in implicit `HStack`s. If relying on an implicit `HStack` before, users will now see multiple rows when linking against the new SDK. In this example: ```swift
 private struct Node: Identifiable {
     let id = UUID()
     let name: String
     let children: [Node]?
 }
 
 fileprivate let data = [
     Node(name: "One", children: [.init(name: "Two", children: nil)]),
     Node(name: "A", children: [
         .init(name: "B", children: nil),
         .init(name: "C", children: nil),
         .init(name: "D", children: nil),
     ])
 ]
 
 struct OutlineExample: View {
     var body: some View {
         List(data) { node in
             DisclosureGroup("Node \(node.name)", isExpanded: .constant(true)) {
                 OutlineGroup(node, children: \.children) { child in
                     Label("Row:", systemImage: "circle.hexagonpath.fill")
                     Text("Node \(child.name)")
                 }
             }
         }
     }
 }
``` (104751549)

##### Symbol Effects

###### Resolved Issues

- Fixed: In the objective-C API in Symbols.framework, requesting `effectWithWholeSymbol` on `NSSymbolPulseEffect` and `NSSymbolBounceEffect` will result in the effect being configured to animate by layer instead.  (109284710)

##### Turn By Turn Navigation

###### Resolved Issues

- Fixed: In some cases, users in China may hear an incorrect distance spoken for an instruction whilst navigating.  (113131913)

##### Uikit

###### New Features

- When you build your app against iOS 17.0, iPadOS 17.0, or macOS 14.0 SDKs, the evaluted indirect input event support mode will change. Apps built on these SDKs without the `UIApplicationSupportsIndirectInputEvents` key will have indirect input event support enabled. Apps built on these SDKs with the `UIApplicationSupportsIndirectInputEvents` will have that key honored. If indirect input event support is not desired when built against the listed SDKs, add `UIApplicationSupportsIndirectInputEvents` to your info.plist with a boolean value of `NO`.  (68295914)
- `UIDevice.batteryLevel` is rounded to the closest multiple of 0.05.  (107718393)
- The query rects passed in to `-layoutAttributesForElementsInRect:` will be more specific to the collection view’s frame, and the rect might intersect with previously queried frames. If subclassing a UIKit vended layout and modifying the frames of elements by applying offsets, make sure that the same offset is applied to the rect passed in to `-layoutAttributesForElementsInRect:` as well, or the user might see items disappearing when they shouldn’t be.  (108663389)

###### Resolved Issues

- Fixed: The new `UIHoverStyle` API doesn’t currently add any visible hover effects when set on a `UIView`.  (108409077)
- Fixed: Prior to iOS 17 and tvOS 17, `UIGestureRecognizer` would set its `state` to `UIGestureRecognizerStateFailed` in the base implementation of `- (void)pressesBegan:withEvent:` if there are no active touches. In iOS 17 and tvOS 17, this behavior has been fixed. On tvOS, `UIGestureRecognizer` allows `UIPressTypeSelect` by default, thus custom `UIGestureRecognizer`s that do not set `allowedPressTypes` might have been relying on this behavior to put themselves into a terminal state after they receive a `UIPress` of type `UIPressTypeSelect`. `UIGestureRecognizer`s that receive events but do not reach a terminal state will block gesture recognizer dependency graphs from resetting, which can cause an app’s interface to become unresponsive. It is important to for custom `UIGestureRecognizer`s on tvOS 17 to either either set `allowedPressTypes` to an empty array if they do not handle `UIPressTypeSelect`, or to implement the `UIPressesEvent` response methods in `UIGestureRecognizerSubclass.h`, and set themselves to a terminal state as appropriate.  (111175673)

##### Uikit Documents

###### Resolved Issues

- Fixed: `UIDocumentViewController` might cause a crash when being dismissed without an external reference holding on to it.  (109283791)
- Fixed: When a file is renamed, for example via `UIDocument`’s new built-in renaming capabilities, the app might lose access to this file.  (109516057)

##### User Enrollment

###### Resolved Issues

- Fixed: User-enrolled devices with Managed Apple IDs fail to update to iOS 17 beta.  (109830404)

##### Video Effects

###### Resolved Issues

- Fixed: The Video Effects menu bar item might not appear for certain applications.  (110038665)

##### Videotoolbox

###### Resolved Issues

- Fixed: You might receive an error when trying to call the new VideoToolbox Swift APIs.  (109523782)

##### Vision

###### Resolved Issues

- Fixed:  `VNDetectHumanBodyPose3DRequest` now returns results for images/frames of people without depth metadata or camera intrinsics explicitly provided.  (109723859)
- Fixed issue with `cameraOriginMatrix`  so a 180 rotation around x axis is no longer required. Please reference updated sample code for WWDC Session 111241.  (110726503)

##### Voicemail

###### Resolved Issues

- Fixed: Manually deleted voicemails might still appear on a paired Watch.   (110072691)
- Fixed: If Silence Unknown Callers or Do Not Disturb is enabled during Live Voicemail, tapping on the voicemail icon in the status bar or Dynamic Island will open an empty window with no voicemail transcript.  (112165574)

##### Wallet

###### Resolved Issues

- Fixed: The user will be unable to: - withdraw or transfer money to Apple Savings account.
- apply for Pay Later via wallet
- transfer partial balances out of Apple Cash
- add money to transit passes  (110667374)

##### Wallpaper

###### Resolved Issues

- Fixed: Depth effect wallpapers on a 180 degree rotation might result in a distorted image.  (105729379)
- Fixed: Home Screen wallpapers might appear more dim than expected.  (108812409)
- Fixed: iPhone Home Screen Photo wallpaper might appear in the wrong orientation.  (109716224)
- Fixed: Wallpaper on iPad might display in the incorrect orientation.  (109894244)
- Fixed: Under certain circumstances, images might show top level visual treatment.  (109952206)
- Fixed: Images might show a black bar at the top when selected as part of the Smart Shuffle Photos poster.  (109974498)

##### Weather Averages

###### Resolved Issues

- Fixed: Placeholders are displayed in locations where Weather averages data isn’t available.  (110133240)

##### Webkit

###### Known Issues

- External camera previews appear rotated 90 degrees.  (105520083)

##### Wi Fi

###### Resolved Issues

- Fixed: Wi-Fi might not connect automatically to known networks after updating to iOS 17 beta if the device isn’t passcode-protected and isn’t signed into iCloud.  (109813416)
- Fixed: While a Mac has active traffic via Wi-Fi, you might experience difficulty discovering and connecting to Continuity Camera.  (109954955)

##### Widgetkit

###### Resolved Issues

- Fixed: Some configuration intent parameter values might not migrate properly from a SiriKit custom intent to an app intent.  (109228854)
- Fixed: Starting Live Activities from interactive widgets might not work.  (109369422)
- Fixed: Apps that use the `.showsWidgetContainerBackground` environment variable no longer crash.  (113947483) (FB12974903)

##### Widgets

###### Resolved Issues

- Fixed: Dragging Lock Screen widgets to the Lock Screen widget area on iPad and iPhone might not work.  (106379745)
- Fixed: It isn’t possible to use a trackpad to add widgets to a Lock Screen.  (110047943)
- Fixed: Widgets might not appear in the Lock Screen editor after tapping a Lock Screen suggestion.  (113231970)

###### Known Issues

- Manually configured widgets might lose their configuration.  (108616752)  Reconfigure the affected widgets.

##### Wifi

###### Resolved Issues

- Fixed: When disconnecting from certain off-market CarPlay Head Units, your phone may take longer than usual, (~30 seconds) to automatically join home or office WiFI networks.  (113017278)

## See Also

- [iOS & iPadOS 17.6 Release Notes](ios-ipados-17_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.5 Release Notes](ios-ipados-17_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.4 Release Notes](ios-ipados-17_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.3 Release Notes](ios-ipados-17_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.2 Release Notes](ios-ipados-17_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.1 Release Notes](ios-ipados-17_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-17-release-notes)*