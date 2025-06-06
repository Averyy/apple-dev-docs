# visionOS Release Notes

**Framework**: Visionos Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS SDK provides support for developing apps for Apple Vision Pro devices running visionOS. The SDK comes bundled with Xcode 15.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 15.2, see [`Xcode 15.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15_2-release-notes).

##### General

###### Notes

- Developing for visionOS requires a Mac with Apple silicon.  (114799042)

###### New Features

- visionOS automatically checks if display adjustment is required the first time you put on Apple Vision Pro.  Press and hold the Digital Crown until you see a green check mark. If you’re unable to complete adjustment, contact your Apple representative. You can readjust your displays in Settings > Eyes & Hands > Adjust Display Alignment.  (109802097)
- To Force Quit an app, hold both the Digital Crown and top button for 2 seconds. Select the desired app from the list which appears, then select the Force Quit button.  (111057029)
- To quickly re-enroll eye or hand tracking, press the top button 4 times.  (111057263)

###### Resolved Issues

- Fixed: The virtual keyboard might be unusable when attempting to unlock a device following restore from iCloud Backup or Software Update.  (109851688)

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

- Fixed: The VoiceOver cursor might not display when expected.  (106775145)
- Fixed: It might not be possible to skip Interpupillary distance (IPD) adjustment during setup while using VoiceOver.  (108008719)
- Fixed: Dynamic Text might displace and break layouts at large sizes.  (109052641)
- Fixed: Sound Actions and Sound Recognition might not function.  (109233749)
- Fixed: VoiceOver might not invoke or allow interaction with elements in Control Center.  (109479644)

###### Known Issues

- Hearing aid volume might be too low.  (109911780)

##### App Launch

###### Resolved Issues

- Fixed: Apps that use a volumetric style window as initial scene don’t launch at the correct position unless launched from the Home Screen.  (116022772)

##### App Store Submission

###### Known Issues

- Apps built for visionOS are unable to use the front-facing-camera UI Required Device Capability.   (121465787)  Remove the front-facing-camera UIRDC for apps built for visionOS.

##### Apple Pay

###### Resolved Issues

- Fixed: Apple Pay payments don’t complete if cards are added during restore from iCloud backup.  (104921490)
- Fixed: You might be unable to continue past the Apple Pay setup screen during Setup Assistant.  (108868427)

##### Arkit

###### Resolved Issues

- Fixed: When the usage description for world sensing `NSWorldSensingUsageDescription` and hand tracking `NSHandsTrackingUsageDescription` is missing in the app’s `Info.plist`, no data is surfaced and no error appears.  (109215187)
- Fixed: Loading existing ARKit anchors might take longer than expected after first putting on the device.  (109370432)
- Fixed: ARKit anchors and device pose might not automatically update to the Space’s coordinate system, causing content to appear at the wrong location.  (109734515)

###### Known Issues

- You might experience difficulty working with large models in QuickLook or third-party apps.  (109805525)  Walk outside of the object, and force quit the affected app.

##### Asset Catalogs

###### Resolved Issues

- Fixed: The asset catalog editor doesn’t have an option to provide high contrast versions of Reality-idiom images and colors.  (109360733)

##### Aswebauthenticationsession

###### Resolved Issues

- Fixed: Due to an incorrect visual effect on the bottom bar of the login view, some text and buttons might be illegible.  (109737808)

##### Audio

###### Resolved Issues

- Fixed: Connecting an LEA device might cause the system to crash in a loop.  (115394125)

##### Authentication

###### Resolved Issues

- Fixed: Authentication views might appear in unexpected locations when using `SFSafariViewController`.  (108971604)

##### Capture

###### Resolved Issues

- Fixed: Environment might be present while using Capture.  (106426026)
- Fixed: The dimming capability might not function while viewing media in Capture.  (109783101)
- Fixed: Expanded view isn’t currently available when viewing spatial videos.  (109984097)

##### Compatible Apps

###### Resolved Issues

- Fixed: Applications designed for iPad might use the wrong accent color for images after selecting items in a sidebar.  (105790997)

##### Compositorservices

###### Resolved Issues

- Fixed: Running a full immersion app with CompositorServices and using Control Center will result in head-locked content.  (112439100)
- Fixed: Having Spotlight or Siri in the background behind an immersive app might cause an app to quit unexpectedly.  (115861906)

##### Dictation

###### Resolved Issues

- Fixed: The Look to Dictate overlay doesn’t appear over search bars in third-party apps. You can still speak to search even though the overlay isn’t visible.  (108800840)
- Fixed: When using Simulator, no dictation button is shown on the virtual keyboard.  (109471503)
- Fixed: When you invoke Dictation and Look to Dictate for the first time, it might take some time for the dictation asset download to complete. This also affects Simulator each time the host Mac is restarted.  (110026867)
- Fixed: Look to Dictate doesn’t work in Compatible Apps.  (114120795)

##### Eyes and Hands Setup

###### Resolved Issues

- Fixed: Removing Apple Vision Pro from your head before completing eyes and hands setup prevents you from being able to continue setup after putting the device back on your head.  (108493280)
- Fixed: Having multiple App Clip Codes in the field of view at the time of prescription lens enrollment might lead to incorrect calibration.  (110139295)
- Fixed: During device setup, attaching Zeiss optical inserts and transferring User’s optical prescription data from iPhone during QuickStart might result in poor gaze accuracy.  (112429318)

##### Eyes and Hands Tracking

###### Known Issues

- Tracking Failure alerts might appear in unexpected positions.  (113142690)

##### Facetime

###### Resolved Issues

- Fixed: Environments might erroneously invoke when joining a FaceTime call.  (109798544)

###### Deprecations

- Calls from visionOS beta 4 aren’t compatible with calls to earlier versions of visionOS beta.  (115669717)

##### Feedback Assistant

###### Notes

- Feedback Assistant app does not appear on Home View for visionOS. To file feedback, click on this link from your visionOS device: [`applefeedback://new`](https://developer.apple.comapplefeedback://new).   (119262359)

##### Game Center

###### Resolved Issues

- Fixed: Games running as Compatible iPad and iPhone Apps might exhibit legibility issues due to Game Center screens displaying at an incorrect size.  (110483022)

##### Game Controller

###### Resolved Issues

- Fixed: Game controllers might not function after interacting with Control Center.  (101399998)

##### Ipados and Ios Compatibility

###### Resolved Issues

- Fixed: The rotation button might appear or disappear unexpectedly in an app, due to orientations being derived using only `UISupportedInterfaceOrientations`.  (103041565)
- Fixed: Gaze highlighting might appear unexpectedly on the play button in media controllers.  (109407558)
- Fixed: FamilyControls framework isn’t included and can cause an app linking against it to quit unexpectedly.  (110422697)

###### Known Issues

- Game controllers might stop working after interacting outside the game window or on incoming notification.   (112147453)  Tap inside app window again to return game controller focus.

##### Keyboard

###### Resolved Issues

- Fixed: When using the virtual keyboard for emoji search, URL entry, or other usage where the return key displays a label other than “return”, the key might not render, although it remains functional.  (108168932)
- Fixed: Immediately after restoring from iCloud backup, the virtual keyboard might not appear upon entering a text field.  (109738103)
- Fixed: The input accessory view appears correctly.  (110473976)
- Fixed: Compatible iPad and iPhone Apps receive notifications in the `UIKeyboard*Notification` family in the wrong order, and with incorrect information.  (112211118)
- Fixed: The dictation button might be missing from the virtual keyboard.  (112615002)
- Fixed: For Compatible iPad and iPhone Apps running on visionOS, the toolbar might change from a floating white bar to a gray rectangle when the keyboard is active.  (115504523)
- Fixed: Software Keyboard might become invisible if repositioned in front of an app window.  (115962380)

###### Known Issues

- In Compatible iPad and iPhone Apps, keyboard-related UI doesn’t animate as expected when appearing into view. However, the animation is correct when the keyboard-related UI disappears.  (114573647)  Depending on UI layout needs, it might be preferable to remove animation from the layout to match the keyboard behavior in visionOS. If the preference is to continue animating the layout changes, you’ll need to determine the timing and animation curve to produce the desired appearance.
- In Compatible iPad and iPhone Apps, when keyboard-related UI disappears, notifications sent on appearance are unexpectedly repeated, followed immediately by the expected notifications for disappearance.  (114573814)  If your app experiences an issue, change your code to ignore appearance-related notifications which repeat information previously received.

##### Location

###### Resolved Issues

- Fixed: Swift apps linking `CoreLocationUI` and using `LocationButton` might quit unexpectedly.  (109181676)

##### Mac Virtual Display

###### Resolved Issues

- Fixed: Mac Virtual Display requires a Mac running macOS Sonoma beta 2 or later.  (111056854)

##### Mail

###### Resolved Issues

- Fixed: When selecting text within a draft, the edit menu that appears blocks the selection controls, making it difficult to adjust the range of highlighted text.  (114092104)
- Fixed: Software Keyboard might become invisible if repositioned in front of an app window.  (116284567)

##### Maps

###### Resolved Issues

- Fixed: When a `LinearGradient` stroke is used with a `MapPolyline` in SwiftUI, the specified gradient color might be ignored.  (106152300)
- Fixed: When using `Map`, Xcode emits a runtime warning that “Publishing changes from within view updates is not allowed”.  (106174743)
- Fixed: At certain zoom levels, the title of a selected `MKMarkerAnnotationView` can overlap other marker titles.  (109491779)
- Fixed: Map views and snapshots might appear blank.  (116137765)

##### Materials

###### Resolved Issues

- Fixed: Some material shader nodes might return an unexpected vector with a length that is not one. The affected nodes are: View Direction (RealityKit), Surface View Direction (RealityKit), Tangent, Transform Normal.  (109213630)
- Fixed: Under some circumstances, the `View Direction` (RealityKit) and `Surface View Direction` (RealityKit) nodes return an incorrect direction.  (109214481)
- Fixed: `Position` material shader node `world` space output is incorrect.  (110040016)

##### Messages

###### Resolved Issues

- Fixed: Messages might quit unexpectedly if a voice message is closed during recording.  (108237487)
- Fixed: Messages might quit unexpectedly after sending an effect.  (109681600)

##### Metal

###### Resolved Issues

- Fixed: Your app might get head-locked while it’s connected to the Xcode debugger.  (116192406)

##### Music

###### Resolved Issues

- Fixed: Turning off Autoplay might cause Music to quit unexpectedly.  (104996449)
- Fixed: Music content in your Library which was added from external sources might not play.  (108533542)
- Fixed: The volume slider animation might be erratic when adjusting volume.  (108844267)
- Fixed: Play and shuffle buttons might become unresponsive when playing songs from a playlist.  (109282061)
- Fixed: Music purchase flows might result in a loading progress spinner in the Listen Now window.  (109409882)
- Fixed: Detail pages might not load in Listen Now and Library.  (112273860)
- Fixed: Missing content or gaps might appear when scrolling up and down.  (114225882)

##### Optic Id

###### Resolved Issues

- Fixed: Optic ID is limited to two Rx enrollments and one non-Rx enrollment.  (106454427)
- Fixed: Optic ID enrollment will be reset after updating to visionOS beta 2.   (110910654)
- Fixed: Even though Optic ID appears in Simulator, it isn’t possible to simulate Optic ID enrollment.  (112460069)
- Fixed: Optic ID enrollment will be reset after updating to visionOS beta 4.  (115137451)

##### Photos

###### Resolved Issues

- Fixed: Some keyboard shortcuts in Photos don’t function, and shortcut guidance overlays aren’t available.  (106832804)
- Fixed: Spatial photos and videos are square and don’t adapt to the aspect ratio of the media.  (107770753)
- Fixed: When using drag and drop to import a spatial photo or video into Notes from Photos, it’s transcoded into a 2D derivative.  (108581403)
- Fixed: Memories generation isn’t available.  (109371117)
- Fixed: Photo Picker `.compact` layout isn’t available.  (109910778)

##### Reality Composer Pro

###### Known Issues

- Audio playback in Reality Composer Pro might stop after switching audio devices, for example from speakers to headphones.  (109911988)  This issue is resolved in macOS Ventura 13.4. When using previous versions of macOS, save the project and quit Reality Composer Pro, then reload the project after switching audio devices.
- Reality Composer Pro might quit unexpectedly after switching audio devices from a Studio Display to another device, such as AirPods or built-in speakers.  (109912081)  Save the project and quit Reality Composer Pro, switch the audio output device, then reload the project.

##### Realitykit

###### Resolved Issues

- Fixed: `HoverEffectComponent` will only apply a hover effect to the RealityKit [`Entity`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/entity) object to which it is directly added.  (105618166)
- Fixed: Reality files with entity trigger actions might collide with dynamic rigid bodies if the trigger flag on the collision component isn’t set. Entity trigger actions are created by Reality Composer Pro for collision components to trigger animations and other effects when two 3D volumes intersect each other. Dynamic rigid bodies previously didn’t interact with colliders if there wasn’t a rigid body component present on the entity with the collider. This behavior changed so that rigid bodies could interact with all colliders that aren’t explicitly flagged as a trigger.  (108760431)
- Fixed: The new `Entity.playAnimation()` function now exposes a user-defined handoff type. The default behavior differs slightly from the default behavior of the existing `Entity.playAnimation()` functions.  In the previous version of `Entity.playAnimation()`, where handoff type wasn’t exposed, the default handoff type was set to `.snapshotAndReplace(applyToAllLayers: true)` unless the `blendLayerOffset` was not `0`, in which case the handoff type was set to `.compose`. The default handoff type for the new `Entity.playAnimation()` function is `.snapshotAndReplace(applyToAllLayers: true)`.  (108908429)
- Fixed: For physics simulations in shared applications, `PhysicsSimulationComponent.nearestSimulationEntity` will return `nil` by default rather than the root physics entity.  (109239347)
- Fixed: Calling `context.entities(matching:updatingSystemWhen:)` in the `update()` function of a type conforming to the `System` protocol is now required for your system to update at frame rate.  (109682743)
- Fixed: Errors and warnings emitted by `realitytool` don’t appear as top-level entries in the build log.  (109692127)
- Fixed: `Scene.convexCast` and `Scene.contact` incorrectly returns positions in physics space rather than scene space when `referenceEntity` is `nil`. `CollisionEvent.Began.position` and `CollisionEvent.Updated.position` are also in physics space rather than scene space.  (109734592)

###### Known Issues

- In a physics simulation, collision shape extents that fall below 2mm are forced to be 2mm in size.  (107999189)  Ensure collision shape extents are 2mm or larger.
- Negative scaling colliders and rigid bodies in physics simulations might result in undefined behavior.  (112628900)  You can negatively scale meshes before passing them to physics.

##### Screen Recording

###### Resolved Issues

- Fixed: It might take at least 20 seconds before screen recordings appear in Photos.  (113361230)

###### Known Issues

- Third-party apps incorrectly allow resizing during screen recording.  (108008626)

##### Settings

###### Resolved Issues

- Fixed: The close button in the top-left corner of the Verify Lenses screen when switching between Zeiss Optical Inserts might not function.  (109379738)
- Fixed: Settings might quit unexpectedly when opening the News or Freeform settings.  (110813777)

##### Setup Assistant

###### Resolved Issues

- Fixed: Selecting incorrect Zeiss Optical Inserts might cause eye enrollment to fail.  (106069159)
- Fixed: Removing the device and placing it back on your head might cause unexpected placement for the setup assistant.  (108206322)
- Fixed: The Shut Down option in Setup Assistant isn’t functional.  (108619197)
- Fixed: Text might overlap and appear clipped after enabling large text in Accessibility options.  (108763778)
- Fixed: The back button in the Data and Privacy pane might not function as expected.  (109364114)
- Fixed: If you switch away from 6-digit passcode  creation mode while setting up a passcode, you won’t be able to switch back.  (112432795)

##### Simulator

###### Resolved Issues

- Fixed: In ARKit, `.worldTransformOfTopLevelEntity(forSceneID:)` returns undefined data.  (108963142)
- Fixed: When using Look To Dictate in Simulator, the dwell button animation completes but doesn’t successfully invoke Look To Dictate.  (109168370)
- Fixed: Launching an app using Xcode’s Build & Run fails if Simulator isn’t already running.  (109514561)
- Fixed: iOS apps using the `#Preview` macro might quit unexpectedly when targeting `Apple Vision Pro (Designed for iPad)`.  (110801867)
- Fixed: Unsupported Language & Region options appear in Settings > General. This functionality isn’t supported in Simulator.  (110812274)
- Fixed: The menu to control immersion levels is available only for apps which use Progressive Immersion.  (112167061)
- Fixed: Support for Dictation might get stuck while downloading.  (112426901)
- Fixed: 3D content might appear darker than expected in the Simulator and Xcode live preview.  (116014698)
- Fixed: Software Keyboard might stop responding if repositioned in front of an app window.  (116261118)

###### Known Issues

- It isn’t possible to view both eyes in Simulator.  (100422901)
- It isn’t possible to perform a direct touch when using Simulator.  (106957500)
- Portable Mac computers don’t enter Sleep mode while Simulator is running.  (107511201)
- Simulator doesn’t support all features of Spatial Audio. You can use Simulator to test a subset of audio features; however, final testing should be performed on device.  (109912117)

##### Siri

###### Resolved Issues

- Fixed: When speaking “Hey Siri, FaceTime him”, ‘him’ is mistaken for ‘Kim’.  (108555952)
- Fixed: When gazing and saying “Hey Siri, FaceTime him”, or “Hey Siri, FaceTime her” the wrong conversation is presented.  (110172520)

##### Storekit

###### New Features

- The [`productViewIconBorder()`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/automaticproductplaceholdericon/4278999-producticonborder) view modifier is available when using StoreKit and SwiftUI. Use this modifier on the icons to provide [`ProductView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/productview) and [`StoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/storeview) to add a standard border around the icon.  (106649532)
- You can now customize the button style used for purchase and subscribe buttons in [`ProductView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/productview), [`StoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/storeview) and [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) instances. Use the [`buttonStyle(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/buttonstyle(_:)-7qx1) view modifier to choose any standard button style, or a custom button style.  (107713282)
- The following StoreKit types are renamed: • `DefaultProductViewStyle` is renamed to [`AutomaticProductViewStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/automaticproductviewstyle) • `DefaultSubscriptionStoreMarketingContent` is renamed to [`AutomaticSubscriptionStoreMarketingContent`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/automaticsubscriptionstoremarketingcontent) • `DefaultProductPlaceholderIcon` is renamed to [`AutomaticProductPlaceholderIcon`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/automaticproductplaceholdericon)  (111185321)

###### Resolved Issues

- Fixed: Calling [`display`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/message/3963915-display) on a [`message`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/message) might not display the message.  (106523068)
- Fixed: Loading animation for [`StoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/storeview) instances displaying a single product.  (110414023)
- Fixed: The following StoreKitTest APIs are now available when testing on iOS 17 beta, watchOS 10 beta, tvOS 17 beta, and visionOS beta: [`setSimulatedError(_:forAPI:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/4196369-setsimulatederror), [`simulatedError(forAPI:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/4196370-simulatederror), and [`buyProduct(identifier:options:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/4196368-buyproduct).  (110547289)
- Fixed: [`StoreView`](https://developer.apple.com﻿﻿https://developer.apple.com/documentation/storekit/storeview) or [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) content might appear in English, or show a localization key, instead of showing localized text for the App Store storefront.  (110734447)

##### Swiftdata

###### Resolved Issues

- Fixed: SwiftData isn’t available in the visionOS SDK included in Xcode 15 beta 1.   (110546453)
- Fixed: visionOS projects that use the `@Observable` property wrapper will fail to build in Xcode 15 beta 3.  (111494849)

##### Swiftui

###### Resolved Issues

- Fixed: Secondary foreground styles might render incorrectly inside Buttons.  (105108416)
- Fixed: Sliders initialized with a step parameter might exhibit a misaligned thumb.   (107659511)
- Fixed: `glassBackgroundDisplayMode.implicit` should handle z offset case.  (108344855)
- Fixed: Inspector isn’t available.  (108908316)
- Fixed: The upper limb visibility API might fail when changed more than once per immersive scene.  (108912873)
- Fixed: Using the `preferredSurroundingsEffect(:)` API doesn’t result in a change to the surroundings (video passthrough) effect.  (109472410)
- Fixed: Content depth is rounded down which can cause placement issues on the z-axis for some thin views.  (109822255)
- Fixed: The searchable modifier, when used in a list component, might cause scrolling and padding issues.  (110124946)
- Fixed: WindowResizability modifier with `.contentSize` doesn’t correctly restrict maximum size. `.contentSize` behaves the same as `.contentMinSize`.  (112299265)

###### Known Issues

- Content depth doesn’t propagate when using `UIViewRepresentable` or `UIViewControllerRepresentable`.  (108052196)
- Applying the `.volumetric` window style on a `DocumentGroup` has no effect.  (115562954)  Use a regular `WindowGroup` or use a `DocumentGroup` with no volumetric window style applied.
- Volumes using the `defaultSize(_: Rect3D, in: UnitLength)` modifier to specify size, will only be the specified physical size at default (large) display zoom. At smaller display zooms the Volume will be smaller and clip content.  (116579319) (FB13240946)  Specify a size for the Volume about 1.5x larger than necessary, and ensure content is not clipped at smallest display zoom setting.

##### Swiftui and Uikit

###### Resolved Issues

- Fixed: Plain style buttons don’t have hover effects.  (101029905)
- Fixed: Full-screen presentations from Ornaments show in the Ornament, rather than in the window to which the Ornament is attached.  (101080752)
- Fixed: Some coordinate space conversions aren’t accurate between Ornaments and the window to which they are attached.  (104293729)
- Fixed: Drag previews might not appear when performing a drag-and-drop operation.  (105029557)
- Fixed: Ornaments appearance and disappearance can’t be animated when they are added or removed.  (105086210)
- Fixed: In some cases, resizing a popover or an Ornament containing a tooltip might result in a crash.  (108918373)
- Fixed: When using the `.onDrop` or `.droppable` modifiers, the callback for `dropEntered` and `dropExited` might not function as expected.  (109062202)
- Fixed: It’s possible to present an invalid presentation from a popover which should assert.  (109386548)

###### Known Issues

- You might notice an extra `UIWindowScene` is connected to your application when using `ImmersiveScene`.  (107361984)
- Some buttons might not play sound.  (108579439)
- State restoration might restore an incorrect scene of an app.  (109120808)  Ensure that a secondary scene isn’t the last one to be closed.

##### Swiftui Scenes

###### Resolved Issues

- Fixed: SwiftUI won’t match to the Preferred Default Scene Session Role as documented in the Immersive Space documentation. Instead, only the first declared Scene in the app body is checked.  (101961210)

##### Travel Mode

###### Resolved Issues

- Fixed: When turning off Travel Mode via Control Center, the confirmation prompt might be hidden behind Control Center.  (105143478)
- Fixed: Travel Mode is optimized for a stationary experience. If you activate Travel Mode in Control Center and start walking, you might experience unexpected behavior.  (113340825)
- Fixed: Apps do not properly re-appear after entering or exiting Travel Mode.  (115860473)

##### Tv

###### Resolved Issues

- Fixed: You might receive a “Something went wrong” error when using third-party streaming apps.  (109584031)
- Fixed: Descriptive audio alternatives don’t currently appear in the audio selection dialog for Apple Immersive Video.  (111066857)
- Fixed: Adjusting the volume using the player controls while watching Apple Immersive Video might not function.  (112293929)
- Fixed: Selecting “Learn More” in the “Check for Objects” dialog which appears when launching Apple Immersive Video might cause the TV app to behave unexpectedly.  (112442054)
- Fixed: Adjusting immerison level immediately before playing Apple Immersive Video might prevent video from playing even though audio can be heard.  (112468705)
- Fixed: A loading spinner might appear indefinitely if you remove Apple Vision Pro and put it back on during playback of Apple Immersive Video.  (112498955)
- Fixed: If you remove Apple Vision Pro and put it back on during playback of Apple Immersive Video, content might appear transparent on one side.  (113525684)
- Fixed: If you remove Apple Vision Pro and put it back on during playback of Apple Immersive Video, the content might unexpectedly appear within an Environment.  (113641927)
- Fixed: Selecting the expand button for a movie or TV show preview doesn’t present the video full screen.  (114210418)

##### Ui Frameworks

###### Resolved Issues

- Fixed: In previous releases, date picker background hover effect was a square but is now circular, as expected. When accessibility settings are enabled, it’s displayed as a rounded rectangle.  (97425729)
- Fixed: Wheel pickers now display a per-column hover effect.  (103281179)
- Fixed: The Cut, Copy, and Paste menu items in third-party applications might not function as expected.  (110426316)

##### Uikit

###### New Features

- The default value of `UISearchController.obscuresBackgroundDuringPresentation` is true in visionOS. Specify a results controller, or set this property to `false` and use your existing view controller for search results.  (104143018)

###### Resolved Issues

- Fixed: Subclasses of `UISlider` don’t get calls to `beginTracking` or `endTracking`.  (103964958)
- Fixed: `UISlider` APIs which take a `UIImage` (minimum track, maximum track, minimum value, maximum value, and thumb) might not function under certain circumstances.  (107386054)
- Fixed: `UISlider` might emit a `UIControlEventTouchCancel` immediately following a `UIControlEventTouchDown`.  (108268934)
- Fixed: The new `UIHoverStyle` API doesn’t currently add any visible hover effects when set on a `UIView`.  (108409077)
- Fixed: Tooltips don’t appear on `UIButton`.  (112605961)

###### Deprecations

- `UISplitViewController.presentsWithGesture` and related display modes are deprecated.  (104141508)

##### Uiviewcontroller

###### Resolved Issues

- Fixed: Presentations don’t respect `ViewController.preferredBackgroundContainerStyle`.  (106122535)

##### Usdz Textures

###### Deprecations

- In accordance with the USDZ specification, only `PNG` and `JPEG` textures are supported.  (106470055)

## See Also

- [visionOS 1.3 Release Notes](visionos-1_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 1.2 Release Notes](visionos-1_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 1.1 Release Notes](visionos-1_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-release-notes)*