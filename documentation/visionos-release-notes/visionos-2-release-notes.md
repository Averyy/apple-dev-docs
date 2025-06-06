# visionOS 2 Release Notes

**Framework**: Visionos Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS 2 SDK provides support for developing apps for Apple Vision Pro devices running visionOS 2. The SDK comes bundled with Xcode 16, available from the Mac App Store. For information on the compatibility requirements for Xcode 16, see [`Xcode 16 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16-release-notes).

##### General

###### Notes

- Developing for visionOS requires a Mac with Apple silicon.  (114799042)

##### Accessibility

###### Resolved Issues

- Fixed: Full Keyboard Access is unable to interact with modal popups, including the prompt for disabling the feature.  (128698154)
- Fixed: Switch Control and VoiceOver users might be unable to select elements in the Accessibility menu on the OpticID screen of Setup.  (130029914)

##### Animations

###### Known Issues

- `rotation3DEffect` does not animate along the shortest path.  (125529696)  Use `Rotation3D.slerp(from: ___, to:___, t: 1.0, along: .shortest)` to animate along the shortest path.

##### App Intents

###### Resolved Issues

- Fixed: EntityURLRepresentation allows arbitrary custom URLs without validation.   (119524801)
- Fixed: Parameterless `@Parameter` and `@Property` wrappers might cause protocol conformance failures.  (130219933)

###### Known Issues

- `@UnionValue` types currently only work as intent results. Attempting to use a `@UnionValue` as the type of an intent parameter or entity property results in failure to compile.  (128069844)

##### App Placement

###### New Features

- Maximum placement distance for apps has been increased. Users will now be able to reposition apps in a more flexible layout, without having to move closer to the desired placement position.  (124564336)
- Volumetric window applications updated with visionOS 2 SDK now automatically tilt to face the user when user repositions a volume upwards. This will allow users to interact with the volumetric window content while in a reclined position. Developers can opt out of this new default behavior for volumetric windows whose content is meant to be aligned with gravity. `volumeWorldAlignment` scene modifier can be used to control this behavior. Volumetric window applications not updated with visionOS 2 SDK will continue to get the existing default gravity alignment behavior from visionOS 1.  (124620395)

##### App Store

###### New Features

- On-demand resources limits were increased for iOS 18, iPadOS 18, tvOS 18 and visionOS 2. See [`On-demand resources size limits`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/on-demand-resources-size-limits/) for more information.  (122163236)

##### Apps

###### Resolved Issues

- Fixed: When applications are relaunched or recentered, the app does not reposition in front of user (either not facing forward or being within usable distance).  (122443480)
- Fixed: In Pages, the Document Manager sheet might be presented on top of the Getting Started sheet.  (126873212)
- Fixed: Compatible iPhone and iPad apps with a deployment target lower than iOS 18 might fail availability checks for iOS 18.  (129027935)
- Fixed: When applications request .ultraDark dimming and are in a non-immersive scene, the amount of dimming will be constrained to .dark. The .ultraDark dimming is still available when an App is immersive.  (129526922)

##### Arkit

###### Resolved Issues

- Fixed: QR Codes of versions 25 and 40 might be difficult to detect.  (125919605)
- Fixed: In certain instances, such as when detecting small barcodes, the BarcodeAnchor extent contains the wrong values and can change unexpectedly between updates.  (128150286)
- Fixed: Object tracking will not track objects the very first time it is authorized, even after the user “allows” world sensing.  (130072459)
- Fixed: RoomAnchors will not be updated once user exits Travel Mode.  (130112804)
- Fixed: The client app might crash and object tracking might cease to function if a reference object with an outdated format is supplied. The client app might also crash if an app runs multiple ARKitSessions that either request to run with more than 10 reference objects in total between them or request to run with different TrackingConfiguration parameters configured.  (131629145)
- Fixed: When detecting codes of Aztec symbology, the anchor point and resulting bounding box might be offset.  (133314532)

##### Audio

###### Resolved Issues

- Fixed: After each reboot of the device, reverb will not adapt to the room and default to a reverb that is equivalent to a small non-reflective space. This reverb state will persist until the user speaks for a few seconds. Once speech is detected, the reverb will adapt to simulate the space. Developers mixing audio should execute workaround to update reverb.  (130243264)

##### Avkit

###### Known Issues

- AVPlayerViewControllers that have an AVPlayer with a mute state equal to true will automatically be unmuted when the volume is adjusted by the user through the system-provided volume controls.  (133892428)  If one or more AVPlayerViewControllers are active at the same time, video playback must be managed accordingly to avoid audio overlapping between AVPlayers. Otherwise, no workaround is required.

##### Cfnetwork

###### Resolved Issues

- Fixed: `CFNetworkExecuteProxyAutoConfigurationScript` and `CFNetworkExecuteProxyAutoConfigurationURL` have always returned a +1 retained CF type object, but the function declarations were not decorated with the `CF_RETURNS_RETAINED` attribute until iOS 18, macOS 15, tvOS 18, and visionOS 2. For C-based languages, the clang static analyzer might note if the object is leaked. No source code changes are required, but they are encouraged to fix the leak. For Swift, this changes the return type of these functions from `Unmanaged<>` to the actual CF type returned, which will require a source change to fix when compiling with newer SDKs. However, Swift programs compiled with older SDKs will continue to work on the new OSes, though the returned CF type object will continue to leak as it did prior to this change.  (126154509)

##### Compatible Apps

###### New Features

- Apps can now be moved outside of the Compatible Apps folder and be positioned alongside apps designed for visionOS.  (119016133)

###### Resolved Issues

- Fixed: Compatible apps installed to simulator from Xcode might incorrectly get placed into the Compatible Apps folder. Correct behavior is that the app is placed outside of the folder when installed directly from Xcode.  (129410611)

##### Compositor Services

###### Resolved Issues

- Fixed: The new chirality property in `SpatialEventCollection.Event` will be `nil` when using CompositorServices.  (129226738)

##### Contacts

###### Known Issues

- When setting up a device, the list of blocked contacts might take an extended time to download after erase install. Communications from blocked contacts might still be received during that time.  (128491917)

##### Developer Settings

###### New Features

- Finding performance issues in apps with Hang Detection is now available on visionOS.  (128020450)

##### Environments

###### Resolved Issues

- Fixed: Once low light mode prompt is accepted, the environment disappears when watching media.  (128095202)
- Fixed: Environments might not appear immediately after device is put back on in low light or after loss of tracking.  (128955092)

##### Files

###### Known Issues

- Creating local files in the Files app fails in the visionOS 2 and iOS 18 simulators if the host is not upgraded to macOS Sequoia Beta.  (132561244)

##### Foundation

###### New Features

- JSONEncoder.OutputFormatting.sortedKeys will now sort keys with a different ordering. Previously, keys were sorted using a numeric, case-insensitive, or localized ordering. Beginning in beta 4, keys are sorted lexicographically based on the keys’ UTF-8 contents.  (126874437)

###### Resolved Issues

- Fixed: [`Date.ComponentsFormatStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/date/componentsformatstyle) was incorrectly producing strings like `"1m"` with the `Date.ComponentsFormatStyle.Style.condensedAbbreviated` style and strings like `"1min"` with the `.narrow` style instead of the other way around. The behavior was corrected to match the behavior of [`Duration.UnitsFormatStyle.UnitWidth`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct).  (125790342)

##### Game Controller

###### New Features

- Game controllers can be used to interact with system UI on visionOS. Apps built with the visionOS 2 SDK that use the Game Controller framework for input in one or more of their views must add an instance of `GCEventInteraction` to those views (UIKit) or apply a `handlesGameControllerEvents(matching: .gamepad)` modifier to those views (SwiftUI).  (121478652)

##### Healthkit

###### Resolved Issues

- Fixed: HealthKit access is not available for iPhone or iPad applications built against iOS 17- and visionOS 1-aligned SDKs.  (125629611)
- Fixed: Selecting the “About Health & Privacy” link in Settings or in the clinical records permission sheet does not present any content.  (127744394)

##### Home View

###### New Features

- Application icons can now be re-arranged by long-pinching on any icon to enter an “edit” mode.  (81856035)
- Environment icons are now rendered in stereo when expanded.  (100035298)
- Environments can now be offloaded from the Home View by long pressing an environment icon to enter editing mode and tapping the remove button for an environment. Offloaded environments remain visible in the Home View, and users can tap them to re-download them later.  (119642769)

##### Icloud Drive

###### Resolved Issues

- Fixed: Frequently changed files syncing over iCloud Drive will use more data than expected.  (128771010)
- Fixed: iCloud Drive in the VisionOS 2 beta 3 simulator requires a Mac running macOS 15 beta 3.  (129584419)
- Fixed: Due to an upgrade of iCloud Drive to be an FPFS File Provider, iCloud Drive will not be available on the simulator if the simulator is running on host and the host is not using the latest macOS Sequoia. In beta 3, when a user signs into an iCloud account, iCloud Drive might seem to be enabled in the Settings UI but is not enabled on Files, and therefore cannot be used.  (130783277)

##### Immersivespace

###### Resolved Issues

- Fixed: immersionStyle can now transition directly from .mixed to .progressive if the app disables animations on the surrounding transaction.  (118408995)

##### Keyboard

###### Resolved Issues

- Fixed: Keyboard does not automatically switch back to the default non-English language in a new input session if it was previously used in an English-only text field.  (126062098)

##### Mac Virtual Display

###### New Features

- Developers can use Mac Virtual Display in applications with ImmersiveSpaces by turning on “Allow Mac Virtual Display” in Settings > Developer. This improves the immersive app and webXR experience when developing immersive content in visionOS.  (111140451)

##### Mail

###### Resolved Issues

- Fixed: The Mail badge count might not update until Mail is launched.  (129914323)

##### Maps

###### New Features

- Introduced Place ID, a unique and persistent identifier.  (129071038)
- Added new resultTypes to MKLocalSearch.Request and additional PointofInterestCategory values.  (129073725)
- Introduced Place Card API to show Maps Place Card UI.  (129073922)

###### Resolved Issues

- Fixed: In searches that use MKLocalSearch.Request, the result type option physicalFeature is ignored.  (128961972)

###### Known Issues

- Conversion between a point in the map view and a physical location (CLLocationCoordinate2D) might be imprecise at high zoom levels.  (129042241)

##### Marketplacekit

###### Resolved Issues

- Fixed: Resolved an issue where iPhone and iPad apps on Apple Silicon Mac and Apple Vision Pro quit unexpectedly if MarketplaceKit is linked.  (132598608)

##### Media Playback

###### New Features

- When watching fullscreen video in an Environment such as Mount Hood, users can now recline and recenter by holding the Digital Crown, or by lifting the video to the desired angle before activating the environment via video controls. These actions will recenter the video into the sky, allowing for a more comfortable viewing angle when in a reclined position.  (124620911)

##### Menus

###### Resolved Issues

- Fixed: Edit Menus and the PencilKit Palette appear clipped in UI Extensions when the Window Size is set to Small or Medium.  (124498168)

##### Mobile Device Management

###### New Features

- The MDM restriction for allowFingerprintModification will not prevent users from modifying their Optic ID settings. See [`Restrictions`](https://developer.apple.comhttps://developer.apple.com/documentation/devicemanagement/restrictions).  (130595604)
- Automated Device Enrollment (ADE) devices skip the “Awaiting Configuration” state if ADE has Modern Authentication enabled. You can test the “Awaiting Configuration” state by not using authentication during ADE enrollments.  (130911423)
- The MDM payload for Global Proxy might result in a loss of internet connectivity if the credentials in the Global HTTP Proxy payload are missing or need to be updated. See [Global HTTP Proxy]https://developer.apple.com/documentation/devicemanagement/globalhttpproxy).  (131416507)

##### Multiview

###### Resolved Issues

- Fixed: A collection of symbols in the AVExperienceController API surface have been re-named as following: - AVMultiVideoManager → AVMultiviewManager
- Experience.multiVideo → Experience.multiview
- experienceController(_ controller: AVExperienceController, prepareForTransition context: AVExperienceController.TransitionContext) → func experienceController(_ controller: AVExperienceController, prepareForTransitionUsing context: AVExperienceController.TransitionContext)
- experienceController(_ controller: AVExperienceController, didChangeTransition context: AVExperienceController.TransitionContext) → experienceController(_ controller: AVExperienceController, didChangeTransitionContext context: AVExperienceController.TransitionContext)
- addContentToMultiVideo(contentIndex: Int) → addContentToMultiview(contentIndex: Int)
- The following symbol will be replaced by a new protocol that will account for each enum case:
- enum Experience → protocol Experience: Hashable  (127689785)
- Fixed: Introduced enum Experience to replace protocol Experience and remove type erasure API surface.  (130246748)
- Fixed: When AVPlayerViewController is not in the view hierarchy of a UIWindow, it might not be possible to transition into expanded view.  (130246891)
- Multiview related symbols are no longer camel-cased for the Multiview prefix. The upper case `V` in the prefix has been replaced by a lower case `v` for the following symbols: - AVMultiViewManager  → AVMultiviewManager
- Experience.multiView → Experience.multiview  (130778277)
- Fixed: When a video is added into the multiview, the window briefly flickers with a black frame.  (131616301)

##### Networking

###### Resolved Issues

- Fixed: For apps linked on macOS 15 / iOS 18 or newer, the default User-Agent request header field value generated by URLSession now includes the unlocalized bundle name instead of the localized bundle name.  (117380285)

##### Object Tracking

###### Resolved Issues

- Fixed: Reference objects should be retrained on macOS Beta 2.0 or later to ensure they adopt the fix for a known persistent-object-anchor issue that impacts objects whose position and/or visibility changes.  (128569382)

##### Photos Shareplay

###### Resolved Issues

- Fixed: SharePlay participants might get stuck in a loading state on shared videos during subsequent SharePlay sessions.  (122363463)

##### Platform

###### New Features

- The firmware image for iBoot will be made available in cleartext in the PCC image. To reduce the overhead imposed by firmware encryption and align policies where appropriate, firmware encryption has been disabled for iBoot on iOS, macOS, watchOS, tvOS, and visionOS. See [`Private Cloud Compute`](https://developer.apple.comhttps://security.apple.com/blog/private-cloud-compute/) for more details.  (125171074)

##### Previews

###### Resolved Issues

- Fixed: Triggering an on-device preview might fail.  (129150211)

##### Reality Composer Pro

###### New Features

- The number of texcoords has been extended from 2 to 8. The 6 new buffers support `float2`, `float3` and `float4` data.  The first 2 buffers continue to support only `float2` data.  (123364636)

###### Known Issues

- For nested timelines with Play Audio actions, the audio playback might not stop on pause, and scrubbing the timeline restarts the audio from scratch.  (131845717)

##### Realitykit

###### New Features

- USD files which use blend shapes now render using blend shape animation in RealityKit. Use of this mesh animation technique comes with a higher memory and performance footprint. The additional memory footprint is proportional to the number of blend shapes used, the geometric complexity of the blend shapes, and the animation duration.  (115068837)
- USD files which use Catmull-Clark subdivision now render using subdivision in RealityKit. Meshes which produce less than 35,000 patches can render using subdivision. This can increase memory consumption and reduce rendering performance.  (129016034)

###### Resolved Issues

- Fixed: When a hover effect requested by a `HoverEffectComponent` is displayed, other hover effects from parents of the `Entity` with less specific `HoverEffectComponent`s are also displayed.  (115299316)
- Fixed: `ViewAttachmentComponent.bounds` property failed to update in some circumstances.  (116580467) (FB13241127)
- Fixed: Updates to LowLevelMesh and LowLevelTexture might appear out-of-sync relative to changes made to Entities in the same frame.  (117234258)
- Fixed: In visionOS 1.0, UnlitMaterials’ blending modes inconsistently respond to `.blending`, `.color`, and `.baseColor` setters. In applications building against RealityKit from visionOS 2.0, alpha-blending enablement should be configured explicitly with `.blending = .transparent(opacity:)`. Developers are advised to check that their code-configured materials are alpha-blending as intended, and use the `.blending` setting where appropriate.  (118210191)
- Fixed: [`Occlusion`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/occlusionmaterial) materials in `.mixed` spaces in visionOS 1.X occasionally fail to occlude virtual content and UI in the host application. Starting in visionOS 2.0 Beta 2, Occlusion materials always occlude `.mixed` space virtual content and other UI rendered behind the materials in the same application. Developers are encouraged to check the behavior of Occlusion materials in their `.mixed` spaces, as the rendered appearance may be affected by this bug fix.  (118594533)
- Fixed: The `MeshResource.generateText(_:textOptions:extrusionOptions:)` function does not convert between meters and points.  (124978549)
- Fixed: Converting to or from the `.scene` coordinate space using `convert(_:from:to:)` functions ignores the position of the RealityView in the SwiftUI Scene.  (125052393)
- Fixed: In visionOS 1.0, transparent materials’ apparent final opacities respond inconsistently to `.blending`, `.color`, and `.baseColor` setters. In applications building against RealityKit from visionOS 2.0, the final opacity of transparent materials is computed as a multiplication of its `.color` or `.baseColor`’s alpha and `.blending = .transparent(opacity:)`. Developers are advised to check that their code-configured transparent materials render with the intended final opacities, and update their usages of `.color`, `.baseColor` and/or `.blending = .transparent(opacity:)` when necessary.  (125431647)
- Fixed: When using a `Play Audio` timeline action in Reality Composer Pro or using the `PlayAudioActions` API, the action does not repeat non-looping audio files.  (126929814)
- Fixed: Using an `Image 2D Array` Shader Graph node in Reality Composer Pro might result in corruption or a system crash.  (127122590)
- Fixed: Shader Graph materials which use the `Hover State` node as part of a `Geometry Modifier` do not work correctly.  (127884791)
- Fixed: Video light spill might flicker after docking video, and reflection/specular light spill might appear to pop.  (128226179)
- Fixed: Calling `SpatialTrackingSession.run()` on simulator will cause the app to crash.  (128275165)
- Fixed: Reality files written by beta versions of RealityKit might not load in later versions.  (128424173)
- Fixed: Physics simulation behavior is different from previous releases.  (128435086)
- Fixed: The `stop` function on SpatialTrackingSesssion has no effect.  (128559666)
- Fixed: Emphasize actions are always additive and should be played with `separateAnimatedValue` set to `true`.  (128622689)
- Fixed: Using `LowLevelMesh` together with `ShaderGraphMaterial` might cause a corrupted rendering of incorrect colors or material parameters for a short period of time.  (128623607)
- Fixed: In the Swift 6 language mode, subclasses of the `Entity` class fail to compile.  (128787131)
- Fixed: When using `AnchorEntity` or `AnchoringComponent` with `TrackingMode.continuous` and a `SpatialTrackingSession`, anchor updates might arrive at inconsistent intervals which could display as choppiness or judder.  (128809287)
- Fixed: Billboard action might not end properly in the animation timeline when using “Send to Device” feature in Reality Composer Pro.  (129013023)
- Fixed: The `.trigger` mode of CollisionComponent no longer generates CollisionEvents when both involved collision shapes use the `.trigger` mode.  (129016567)
- Fixed: The `PlaybackCompleted` animation event is delivered one frame after the animation reaches its final value. Additionally, the `time` property of the `AnimationPlaybackController` returns 0 for completed animations. This matches the behavior of RealityKit on other platforms.  (129017192)
- Fixed: Looping PlayAnimationActions might not automatically retrigger the animation when it loops.  (129423233)
- Fixed: When using the RealityKit or Reality Composer Pro object tracking feature alongside the new `SpatialTrackingSession` API, the tracking might look laggy or completely lost.  (129858206)
- Fixed: Negative damping values on `PhysicsBodyComponent` are not automatically set to zero, which might cause instability in physics animations.  (131167971)
- Fixed: Calling `TextureResource(cubeFromEquirectangular:)` might crash.  (131197201)

###### Known Issues

- Using `.shadow` in SpatialTrackingSession does not work on devices without LIDAR sensors.  (132124802)  Enable `.plane` as well as `.shadow`.
- The AudioGeneratorController might not immediately begin playback if the RealityKit.Scene doesn’t receive an update.  (133335897)  Trigger an update to the RealityKit.Scene by modifying a @State variable, or calling `entities(matching:when:)` in the context of custom System’s update method.
- RealityRenderer might be missing material inputs.  (133999846) (FB14818360)

###### Deprecations

- In previous versions, the order of child entities was sometimes preserved. Now, the order of an `Entity`’s children might not be reliable and can change unexpectedly when any child is reparented.  (129015381)

##### Scenes

###### New Features

- Application scenes are now reopened in their previous state and relative placement after restarting Apple Vision Pro. Implement SwiftUI or UIKit state restoration to restore the appropriate content within scenes. Preferences are available in General settings to enable/disable the feature.  (124560652)

##### Screen Time

###### Resolved Issues

- Fixed: Parent approving remotely from the parent device will always grant 1 hour, regardless of whether a child asks for a 15-minute, 1-hour, or all-day exception for an app or website.   (129084141)

##### Settings

###### Resolved Issues

- Fixed: Incorrect prescription value might be displayed in Settings.  (129684844)
- Fixed: The General > About pane might show an incorrect value for the storage capacity of the device.  (130929019)
- Fixed: When navigating to Settings > General > Storage, the Settings app might crash if you have not opened Podcasts prior.  (131180865)
- Fixed: In Settings > General > Apple Vision Pro Storage, viewing app storage details is not available.  (132768086)

##### Shortcuts

###### Resolved Issues

- Fixed: The Shortcuts editor might offer some new actions that are not yet ready for use. If you save a shortcut with one of these actions, you might need to correct it after a future update with the corrected actions.  (128841105)
- Fixed: Actions might take some time before appearing in the Actions Drawer.  (129021226)

##### Storekit

###### New Features

- The [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) now supports custom control styles. To create a custom control style, declare a type that conforms to [`SubscriptionStoreControlStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle) and implement `makeBody(configuration:)` method.  (106819454)
- New standard styles are available for laying out subscription store view controls with a compact height. Use `pagedPicker` and `pagedProminentPicker` for a platform appropriate paging effect, or `compactPicker` to place options in a horizontal stack. For watchOS, the new `pagedPicker` style is available for laying out [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) controls with a compact height.  (110286601)
- Use types such as `SubscriptionOptionGroup` and `SubscriptionPeriodGroupSet` to declare a hierarchical structure for your [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview). You can use the `subscriptionStoreOptionGroupStyle(_:)` to choose between presenting groups as a tab view or as navigation links.  (110429924) (FB12264937)
- The subscription status [`RenewalInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/status/3822294-renewalinfo) object now supports new properties `renewalPrice` and `currency` to indicate the price at which the subscription will renew, and its currency. There is also a new `offer` property containing the information of the offer that will be applied to the next renewal, if there is any. This includes the offer ID, the offer type, and the payment mode.  (114217892)
- Finished consumables can now be included when using the [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction) APIs. Users can enable this feature by setting `SKInAppPurchaseHistoryIncludesConsumables` to true in app’s Info.plist.  (115079880)
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

##### Swift

###### Resolved Issues

- Fixed: Pre-compiled apps that contain custom types conforming to the `AsyncSequence` protocol can hit infinite recursion in the `swift_getAssociatedTypeWitness()` function in the Swift runtime on new OS versions.  (129605725)

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

##### Swiftui

###### New Features

- When using a `TabView`, tapping on the current tab now pops any embedded navigation stack.  (50924017)
- If `Label` is used inside of a `List` with multiple views as its title, it will now stack them vertically and apply subtitle treatments to every view after the first.  (115528544)
- SwiftUI sheets presented with the `.sheet` modifier now use `.automatic` sizing by default. `.automatic` resolves to `.form` or `.form.fitted(horizontal:false, vertical: true)` depending on the platform (see the symbol’s documentation for more). Platforms prior to iOS 18 and aligned releases used different, non-customizable default sheet sizing. iOS 17 and earlier used what is now called `.page` presentation sizing. macOS 14 and earlier used what is now called `.fitted` sizing. visionOS 1 used `.fitted` sizing. When linking apps against iOS 18 and aligned SDKs, audit your sheet presentations and pick the sizing best for you. Apply a `.presentationSizing` modifier to sheet contents: ```swift
 ContentView().sheet(isPresented: $present) {
   SheetView().presentationSizing(.form)
 }
``` (117551515)
- Apps using the `progressive` immersion style can now control the initial, minimium, and maximum immersion amount.  These apps can now also access the current immersion level as the user changes it with the Reality Dial.  (118316795)
- Types conforming to the View protocol, and other similar SwiftUI protocols, are now isolated to the `@MainActor` by default. SwiftUI’s runtime behavior with respect to actor isolation has not changed: SwiftUI views and similar types have always been evaluated on the main actor at runtime; this change improves compile-time diagnostics for potential data-race safety issues. To opt out of the new default main actor isolation and restore the previous default isolation, add the nonisolated keyword to methods and properties as needed, or move the protocol conformance to an extension to opt out the entire type.  (120815051)
- The ornament modifier is now supported inside Volumes.  (121121550)
- [`Text(_:format:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(_:format:)) now automatically injects `FormatStyle` known to SwiftUI with the `TimeZone` and `Calendar` from the environment.  (123662780)
- If content is clipped differently on visionOS 2, please check the bounds to ensure they are set to be large enough to accommodate this content.  (125038726)
- `@Entry` macro can now be used to simplify declarations of custom `EnvironmentValues`, `FocusedValues`, `Transaction`, and `ContainerValues` properties.  (125568810)
- Added the ability to give a gesture a name, which gets surfaced to UIGestureRecognizers when establishing dependencies.  (126527559)
- Starting in visionOS 2, the `PhysicalMetric` and `PhysicalMetricsConverter` types can now return metrics that take into account the scale applied by the system to the corresponding scene. The system might apply a scale to windows and volumes as they are repositioned by the user, or when using certain features that modify scene size, like Window Zoom. While scaled, one unit within a default `RealityView` in that scene might be longer or shorter than 1 m as measured in the user’s surroundings. If your app is built against the visionOS 2 SDK, these APIs now default to returning values that also take that scale into account, and thus will match the coordinate system of that `RealityView` without the need for further conversion. Those values could be used with SwiftUI modifiers or containers in a way that matches the positioning of entities within that view, for example. If you need true-to-size measurements that match the user’s physical space, as these APIs provided in previous versions of visionOS, please see the documentation for `PhysicalMetric` and `PhysicalMetricsConverter` to learn how to compensate for this scale.  (128212851)
- Nesting a TabSection within a TabSection is supported in the `.sidebarAdaptable` TabViewStyle on iPadOS and visionOS.  (128237671)

###### Resolved Issues

- Fixed: Outline Lists do not animate correctly.  (106239318)
- Fixed: `View._printChanges` now outputs key path of mutated observable properties instead of “@dependencies”.  (111392797)
- Fixed: SwiftUI will now assert that types conforming to the `App` protocol are value types.  (113634782)
- Fixed: Automatically updating `Text` created via [`Text(_:style:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(_:style:)) or [`Text(timerInterval:pauseTime:countsDown:showsHours:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:)) was causing increased battery drain when used in long running Live Activities. They now no longer animate changes in digits that signal the seconds value, keeping the power impact to a minimum.  (115906895)
- Fixed: In apps built against the visionOS 2 SDK, the `upperLimbVisibility` modifier now differentiate properly between the three possible `Visibility` values `automatic`, `visible` and `hidden`, both when applied as a `View` modifier and as a `Scene` modifier.  (117220285)
- Fixed: App scenePhase now reports as active when at least one scene is active.  (117864591)
- Fixed: Scroll views can now accept interaction in their content insets.  (117928468)
- Fixed: `.navigationDestination(for:destination)` modifiers inside of lazy containers are no longer evaluated. `.navigationDestination(isPresented:destination:)` and `navigationDestination(item:destination)` will log warning when used in lazy containers. Lazy containers in this context include: `List`, `LazyVGrid`, `LazyHGrid`, `LazyHStack`, `LazyVStack` `Table`, and `TabView`. If using `navigationDestination`s in lazy containers, users will see logged errors at runtime. Lift the modifiers higher up in the view hierarchy so they are outside of the lazy containers. Allowing navigation destination modifiers in lazy containers had two significant costs: (1) app navigation state could be undefined if a navigationDestination had been scrolled off screen (2) The navigation system had to explore all list contents to ensure navigation destinations remained up to date. Only allowing these modifiers outside of lazy containers improves app navigation reliability and performance.  (117998693)
- Fixed: Gestures might not pick up a modified content shape, such as when increasing the tappable area of a button.  (120938385)
- Fixed: When using the visionOS 2 SDK to build a `TextField` aligned along the vertical axis, it will feature a vertical margin of 2.0 pts and a horizontal margin of 16.0 pts if the style is set to `.roundedRect`.  (124638409)
- Fixed: Elements along a `NavigationPath` or the data structure passed to the `path` parameter of `NavigationStack(path:root:)` are now compared more efficiently. Any side-effects from setting a `path` equal to itself are no longer reliable and likely will not occur.  (125093883)
- Fixed: The state of the root view of `UIHostingConfiguration` is now reset before the associated cell is displayed.  (125100960)
- Fixed: `SceneBuilder`, `WidgetBundleBuilder`, `TableColumnBuilder`, `TableRowBuilder`, `CommandsBuilder`, and `ToolbarContentBuilder` now diagnose unsupported `if #available` conditions at compile time instead of crashing at run time.  (125379937)
- Fixed: `UIViewRepresentable`, `NSViewRepresentable` and their view controller variants no longer create a layer with `allowsGroupOpacity` set to true.  (125561916)
- Fixed: In certain scenarios, [`Text(_:style:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(_:style:)) produced suboptimal output, such as choosing an unnecessarily small calendar unit, showing zero values for large calendar units instead of omitting them, or showing seconds in Always On Display.  (125885307)
- Fixed: [`Text(timerInterval:pauseTime:countsDown:showsHours:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:)) was redacting the seconds value even when the timer was paused, had not started yet, or had already reached its end.  (125885429)
- Fixed: Resolved an issue where scroll views would not receive touches if placed near a tappable control. When rebuilt with the newer SDK, make sure that small buttons and tap targets are correctly enlarged. You can use the `contentShape` modifier.  (126232279)
- Fixed: When programmatically resizing a volume or window, content might temporarily get misaligned and cropped during the transition and the transition animation can’t be modified. Testing notes: In XRCatalog scenes -> volume -> content sized volume, check that the non-animated resize isn’t animated and that the animated resize animates smoothly.  (126874356)
- Fixed: Opening volumes off the main thread will correctly throw an error.  (128094868)
- Fixed: Apps using the `progressive` immersion style start with a smaller initial amount of immersion than they did on visionOS 1.  (128546226)
- Fixed: Sheets presented with the `.sheet` modifier will have `FittedPresentationSizing` by default. This can cause sheets to appear too narrow or too large, depending on their contents. This is incorrect. The default presentation sizing should be `.form`.  (128902804)
- Fixed: In the Swift 6 language mode, the `@Entry` macro now works with non-`Sendable` types if the type of the entry is declared explicitly.  (129073803)
- Fixed: In Volumes, scene contents might be positioned higher and farther away, and the app might be difficult to reposition.  (129249967)
- Fixed: SwiftUI apps built from Xcode 16 Beta will crash when run on the visionOS 1.2 simulator.  (129589372) (FB13841000)
- Fixed: The reported amount of immersion might be wrong after having transitioned among different immersion styles prior to opening the immersive space.  (130010129)

###### Known Issues

- When using the new `.handPointerBehavior(.drawing)` modifier, pointer shapes set with the new `.pointerStyle()` modifier are not respected while a modal presentation such as a popover is presented.  (125272950)
- Apps using the `progressive` immersion style do not receive a callback with their initial level of immersion.  (128684013)  Use the new variants of `progressive` to manually define an initial amount of immersion.

###### Deprecations

- The TabContent popover modifier is now unavailable on visionOS.  (131408356)

##### Swiftui and Uikit

###### New Features

- The SwiftUI `ToolbarTitleMenu` API and the UIKit `titleMenuProvider` API now create menus above the window. This only applies when the title is not rename-able and does not have a document header.  (121880025)

###### Resolved Issues

- Fixed: Presentations will assert when the presenting view controller’s window isn’t part of a scene. Presentations include, but aren’t limited to: In UIKit, a call to `presentViewController:animated:completion:` In SwiftUI, usage of the `sheet(isPresented:onDismiss:content:)`, `fullScreenCover(isPresented:onDismiss:content:)` or `alert(_:isPresented:actions:)` modifiers, along with their alternatives. On visionOS, when a `UIWindow` is closed, either by the user or programmatically, its associated `UIWindowScene` is invalidated and any reference to the window is released within UIKit. This is provided that the window isn’t the last visible window from a given app. If the window remains in memory past this point, it won’t have an associated scene and will trigger the assertion on presentation. Reasons why a window might remain in memory can be retain cycles, especially within the application’s `UISceneDelegate`, or keeping a strong reference to the window somewhere in the app and not releasing it at the right time.  (117425831)

##### Tabview

###### Known Issues

- Navigation configurations that include TabView must have the TabView as the root for the TabBar to appear.   (132595251)  Reconfigure your navigation stack to ensure TabViews are not contained within other Navigation Controllers.

##### Travel Mode

###### Resolved Issues

- Fixed: Travel Mode Hint and On/Off Notifications copy are not localized. Copy will be displayed in English. Never use Apple Vision Pro while operating a moving vehicle or when attention to safety is required.  (130987053)

##### Uikit

###### Resolved Issues

- Fixed: If UIAlertController is reused, the alert might not get dismissed when presented a second time. No changes are necessary if any of the SwiftUI alert methods are used.  (129718567)
- Fixed: Tab titles are missing in iPad tab bars for RTL languages.  (130154177)

##### Video Playback

###### Known Issues

- Fullscreen video player does not dock in mixed immersive spaces.  (124177690)  Present video fullscreen in an immersive space with a progressive or full immersion style.

##### Vision Framework

###### Deprecations

- `faceCaptureQuality` is now replaced by `captureQuality.score` on `FaceObservation`.  (132508104)

##### Volume Adjustment

###### New Features

- Users can now restore volume control to Digital Crown by default. Top-level settings pane has been added to set default crown control (immersion or volume).  (130442740)

##### Volumetric Scenes

###### New Features

- Volumetric scenes are now provided with an optional system-defined baseplate to guide users toward affordances for resizing.  (121208804)

##### Webxr

###### Resolved Issues

- Fixed: Immersive WebXR content might fail to render on the visionOS simulator.  (132107276)

##### Window Resizing

###### New Features

- Users can now resize volumetric style windows with the resize controls that show up at the corner of a volume, similar to how plain style windows can be resized in visionOS 1.  (118580633)

## See Also

- [visionOS 2.5 Release Notes](visionos-2_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.4 Release Notes](visionos-2_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.3 Release Notes](visionos-2_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.2 Release Notes](visionos-2_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.1 Release Notes](visionos-2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-2-release-notes)*