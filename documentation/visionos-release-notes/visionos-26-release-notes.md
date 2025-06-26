# visionOS 26 Beta 2 Release Notes

**Framework**: visionOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS 26 SDK provides support for developing apps for Apple Vision Pro devices running visionOS 26 beta 2. The SDK comes bundled with Xcode 26, available from the Mac App Store. For information on the compatibility requirements for Xcode 26, see [`Xcode 26 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26-release-notes).

##### Airdrop

###### Resolved Issues

- Fixed: Any 2D video or spatial video received via AirDrop will be saved and opened in the Files app instead of the Photos app.  (152265301)

##### Alarmkit

###### Resolved Issues

- Fixed: Attempting to import AlarmKit for a visionOS Simulator project will fail as this API is not available on AlarmKit.  (152339959)

##### App Store

###### New Features

- A new Accessibility section has been added to the App Store product pages that highlights accessibility features within apps and games. These Accessibility Nutrition Labels give users a new way to learn if an app will be accessible to them before they download it, and give developers the opportunity to better inform and educate their users on features their app supports.  (138344118)

###### Known Issues

- `iphone-performance-gaming-tier` apps on visionOS are not available via TestFlight.  (141472382)

##### Apple Intelligence

###### New Features

- The Foundation Models framework provides you with direct access to the on-device large language model at the core of Apple Intelligence.  (139996377)

###### Resolved Issues

- Fixed: In Image Playground and Genmoji, the new modifiers to customize appearance do not work for Japanese-language users. Image creation is blocked when attempting to add modifiers to its appearance.  (151833204)
- Fixed: Model quality output degrades after extended, repeated inferences of the same adapter.  (152468267)

##### Apple Vision Pro Setup

###### Known Issues

- iCloud syncing for Apple Vision Pro Setup data is not enabled by default on Apple Vision Pro and iOS devices.  (153339405)  On both iOS and visionOS devices, manually enable the iCloud sync toggle in Settings > Apple Account > iCloud > Apple Vision Pro Setup.

##### Arkit

###### Resolved Issues

- Fixed: The C API is unavailable on macOS, which limits rendering spatial macOS applications to a Swift implementation.  (152269768)
- Fixed: For Accessory Tracking, the “grip” POI (Point of Interest) for GCController is missing a rotation.  (152304770)
- Fixed: For Accessory Tracking, in order to get the aim POI (Point of Interest) for GCStylus, use the string “tip” in place of “aim”.  (152335557)

###### Known Issues

- Accessory Tracking does not work in Travel Mode. The user might not get notified of this behavior for some connected accessories.  (152264297)

###### Deprecations

- `ARQuickLookPreviewItem.h` has been moved to the Quicklook framework and is no longer available via ARKit. If your code imports `ARKit/ARQuickLookPreviewItem.h` directly, change it to import `QuickLook/QuickLook.h` instead. Swift clients should import Quicklook instead of ARKit.  (152081500)
- `NSEnterpriseMCAMUsageDescription` is now deprecated. Use `NSMainCameraUsageDescription` instead.  (152098891)

##### Assistantschemas

###### Resolved Issues

- Fixed: If you have adopted any of the following email AssistantSchemas, you will experience a compilation error due to a parameter type change: `createDraft`, `updateDraft`, `replyMail`, `forwardMail`, `message`, and `draft`.  (148633307)

##### Avfoundation

###### Resolved Issues

- Fixed: `AVPlayerLayer` does not ensure a valid video frame is always displayed during item replacement, as the `isReadyForDisplay` property does not remain true during transitions.  (151902458)

##### Avkit

###### Resolved Issues

- Fixed: When using the AVPlayerViewController API, Dynamic Mask is not supported in visionOS simulator.  (152602013)

##### Background Assets

###### Resolved Issues

- Fixed: The system might not update downloaded asset packs as frequently as is expected for apps that internal testers install from TestFlight.  (143281558)
- Fixed: Asset pack downloads might fail unexpectedly or stall indefinitely, including across reboots.  (151498902)
- Fixed: The system might not deliver status updates to your app for ongoing asset pack downloads.  (151647839)
- Fixed: Pausing and resuming an app installation or update while the system is downloading essential asset packs might cause the installation or update to stall indefinitely.  (151942388)

###### Known Issues

- The installation of large asset packs might fail.  (153128086)

##### Cloudkit

###### Resolved Issues

- Fixed: CloudKit sharing URLs do not launch third-party apps.  (151778655)

##### Compositorservices

###### Resolved Issues

- Fixed: When turning off hover effects using the tracking areas API, spatial events might provide an incorrect location.  (151504311)
- Fixed: Immersive Spaces using CompositorServices with the Progressive style do not display correctly on the visionOS simulator.  (151925874)
- Fixed: CompositorServices API hover effects and tracking areas do not work in the visionOS simulator.  (152101959)
- Fixed: When opening an immersive space, there might be a delay before the system has the correct immersion style. This might cause errors for functions that require specific immersion styles, since they may be called before the selected immersion style is propagated.  (152523347)

###### Known Issues

- Partially-occluded objects might be more difficult to target with tracking areas compared to RealityKit colliders.  (149224443)

##### Controller Tracking

###### Resolved Issues

- Fixed: While using controller tracking, the Hand Tracking API via ARKit still provides updates for hand holding the controller at 1Hz. This means that if an app is using controller tracking and hand tracking at the same time, it will get sporadic hand tracking results. The intended behavior is for hand tracking to stop when controller is held.   (151882645)
- Fixed: User might not be able to close or reposition app windows with a game controller or with hand gestures after using a game controller.  (152673502)

##### Facetime

###### Known Issues

- Testing SharePlay experiences in the simulator using FaceTime might cause the simulator to crash.  (153776177)

##### Foundation

###### New Features

- Interpolating non-localized types into a `LocalizedStringResource/String(localized:)/AttributedString(localized:)` value will now display a deprecation warning instead of potentially falling back to a fully-unlocalized string. Provide a localized value to interpolate into the text instead, or silence the warning by wrapping the unlocalized value in a call to `String(describing:)`.  (126876158)

###### Resolved Issues

- Fixed: Functions that initialize a string from a C-string pointer do not validate that the provided encoding is a valid encoding for C-strings.  (143756086) (FB16417968)

##### Foundation Models Framework

###### Resolved Issues

- Fixed: When you pass `includeSchemaInPrompt: false` to `respond` or `streamResponse`, it is not respected.  (151926006)
- Fixed: In an Xcode Playground, requests made to the model might receive a “rate limit exceeded” error.  (152325506)
- Fixed: The Foundation Models framework cannot be imported when building for Mac Catalyst.  (153255533) (FB18004324)

###### Known Issues

- Custom `@Generable` types named `Number` or `Boolean` might not function reliably in guided generation.  (152280144)  Use a different type name.
- Some instructions and prompts to the model might not lead to expected responses. Use Feedback Assistant to report satisfactory or unsatisfactory cases. When applicable, you can use the `LanguageModelFeedbackAttachment` API to serialize the feedback to a file and attach it to Feedback Assistant.  (152318091)  Refine your instructions and prompts using `#Playground` in Xcode. When applying guided generation with a `@Generable` type, add `@Guide` with a custom description on properties to steer the model’s responses.
- Tool calling might not function properly if primitive types such as `Int`, `String`, or `Bool` are used as the argument.  (152318534)  Define a custom `@Generable` type.
- Model requests in macOS command line tools might experience rate limiting.  (152681332)  When you need to make many requests to the model, use a UI app instead.
- `Generable` types cannot be made public due to a bug in the `Generable` macro.  (153216183) (FB17990794)  When you intend to expose a `Generable` type in your library, expand the macro using Xcode, insert the macro expansion content into your code, and make the `id` property public.
- Requests to the model might experience rate limiting, even when the device is connected to power.  (153216632)

##### Game Controller

###### Known Issues

- You might not be able to reposition app windows with a game controller after playing an Arcade game using controllers.  (152130313)  Turn off Bluetooth, turn it on again, and re-connect the controllers.

##### Healthkit

###### Resolved Issues

- Fixed: The authorization screen prompted by the Medications Authorization API cannot be dismissed if the user has no available medications needing authorization.  (152094574)

##### Icloud

###### Resolved Issues

- Fixed: Prescription assets created on visionOS might not sync to iOS.  (152119040)

##### Image Playground

###### Known Issues

- The UI becomes locked when attempting to interact with the generic person panel noted in popover for bincompat Playground API presentation.  (152095114)  Force quit and restart the app.

##### Immersivespace

###### Resolved Issues

- Fixed: Observable view models in an ImmersiveSpace do not get de-initialized when the ImmersiveSpace is closed. Additionally, ImmersiveSpace content is evaluated eagerly instead of lazily.  (147699733)

##### Keyboards

###### Known Issues

- For Chinese, Japanese, and Korean keyboards, expanding and collapsing the candidate bar might cause the bottom row of full-size keyboards and bottom two rows of 10-key keyboards to register the wrong input.  (152120249)  Resize the keyboard by dragging the corner.

##### Lists

###### Resolved Issues

- Fixed: For platform-compatible first-party apps like Calendar, Voice Memos, and Reminders, list rows with multi-selection buttons might fail to render those buttons.  (152510946)

##### Look to Scroll

###### Resolved Issues

- Fixed: If Look to Scroll is disabled in Settings and the user has not encountered the feature before, a Tip notification for Look to Scroll will still appear.  (146418079)

##### Mac Virtual Display

###### Known Issues

- Users might see sharp edges around keyboards and MacBooks when viewing in passthrough.  (153668146)  Disconnect then reconnect the Mac Virtual Display, or reboot the Apple Vision Pro.

##### Maps

###### Known Issues

- Curated guides do not scroll on iOS, iPadOS, or visionOS when the iPhone is in landscape mode.  (152123749)  On iPhone, view curated guides in portrait mode.

##### Messages

###### Resolved Issues

- Fixed: Sent translated messages do not get re-translated after editing.  (149401758)
- Fixed: In regions where Screen Unknown Senders is on by default, notifications for message categories are erroneously off by default.  (149450560)
- Fixed: When scrolling through a conversation that contains messages that failed to send, translucent circles might appear to the right of the transcript, not connected to any message.  (149575551)

###### Known Issues

- In one-to-one conversations, background changes might be attributed incorrectly after quitting and re-opening the Messages app.  (150548773)
- When setting a photo as a background in conversations, the photo appears larger than the preview shows.  (151730462)  Set the photo background from an iPhone.
- Transaction or Promotion messages filtered by a Message Filter App Extension might be badged as “Unknown” in the conversation list rather than “Transaction” or “Promotion”.  (151869409)

##### Metal

###### New Features

- Metal 4 is now supported. See [`Metal`](https://developer.apple.comhttps://developer.apple.com/metal/) for additional details.  (113781091)

###### Resolved Issues

- Fixed: Metal Shader Validation might not work with shaders that use Metal Performance Primitives.  (149263281)

###### Known Issues

- If you’re using Metal 4 command encoders, you should add render and compute pipelines that support indirect command buffers to your residency sets. The Metal device driver currently does not enforce this requirement.  (145066238)
- Metal Shader Validation might not work with Metal 4 ray tracing pipelines.  (152520367)  Selectively disable Shader Validation for pipelines using ray tracing. See [`documentation`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/validating-your-apps-metal-shader-usage/#Selectively-enable-Shader-Validation).

##### Metalfx

###### Known Issues

- Temporal upscaling for MTL4CommandBuffer’s `MTL4FXTemporalScaler` does not work.  (146436741)

##### Mobile Device Management

###### Resolved Issues

- Fixed: Apps installed via Declarative Device Management might not get preserved correctly during Rapid Return to Service flow.  (148849851)

##### Music

###### Known Issues

- Switching audio routes during playback of a music video or advancing to the next video in a playlist might cause the Music app to return to the playlist view, stop responding, or close unexpectedly.  (152145901)  Maintain existing audio routes during playback of videos. Play music videos individually, rather than as part of a playlist or queue.

##### Networkextension

###### Deprecations

- Algorithms DES, 3DES, SHA1-96 and SHA1-160 as well as Diffie-Hellman groups less than 14 are no longer supported for IKEv2 VPNs.  (148767790)

##### Nslog

###### New Features

- Dynamic string data in format arguments for `NSLog` will be redacted to `\<private\>` in the Unified Logging System. This specifically targets data that enters the Unified Logging System via `NSLog`, and will not impact the Xcode console or `NSLog`’s `stdout` output. If you wish to log un-redacted data to the Unified Logging System please use the “os_log” or “Logger” interfaces.  (137129180)

##### Quick Look

###### Known Issues

- Opening a side-by-side stereo 180° video on Apple Vision Pro from Files and opting to convert it to Apple Projected Media Profile might stall indefinitely during conversion.  (146349661)  Convert the 180° video to APMP on macOS before copying it to Apple Vision Pro by right-clicking on the file in Finder and choosing “Encode Selected Video Files”, or convert the video with the `avconvert` command-line tool.

##### Realitykit

###### New Features

- SwiftUI modal presentations are now permitted in RealityViewAttachments.  (129033264)
- You can use `PresentationComponent` with `.popover` configuration to show a SwiftUI popover anchored to a RealityKit entity. When presented, the popover will start off billboarded towards the user. To billboard continuously, use a `BillboardComponent` alongside the `PresentationComponent`.  (132603872)

###### Resolved Issues

- Fixed: Entities with a PortalComponent ignore any ModelSortGroupComponent and instead use a fixed rendering order. In case of sorting rendering issues with portal surface, explicitly add a ModelSortGroupComponent using a `.planarUIAlwaysBehind` sort group.  (149899345)
- Fixed: When using RealityKit API to retrieve the transform value of an accessory-anchored entity in a shared space, the result might be offset from its true value.  (151163403)
- Fixed: App will crash if an entity is removed while presenting an `ImagePresentationComponent.Spatial3DImage` that has not yet finished generating.  (151960494)
- Fixed: The `animate` functions on `Entity` and `RealityViewContent` do not start animations.  (152456435)

###### Known Issues

- Synchronous-loading APIs block the main actor and should not be used in async contexts.  (117170643)  Use `init(...)` async instead.
- Simple Views using RealityView that modify a `@State` in the `make` closure and use it only in the `update` closure sometimes read an old value in the `update` closure.  (145771388)  Explicitly capture state properties in the `update` closure: ```None
 struct ContentView: View {
     @State var entity: Entity?
     var body: some View {
         RealityView { content in
             entity = Entity(...)
             content.add(entity!)
         } update: { [entity] content in
             // modify the captured Entity
             entity.transform = ...
         }
     }
 }
```
- Some properties and components do not update SwiftUI Views when accessed through the `.observable` property on Entity.  (147063698)
- When a `PresentationComponent` is created with a `Binding` from an `ObservableObject`’s published property, changes to the property might not result in the popover presenting correctly.  (151346044)
- When using ManipulationComponent with `dynamics.translationBehavior = .none`, `releaseBehavior = .reset` does not reset rotation.  (151648417)  Apply rotation after `ManipulationEvents.WillEnd`.
- When using the VideoPlayerComponent API, Dynamic Mask is not supported in the visionOS simulator.  (152725380)

##### Remoteimmersivespace

###### Resolved Issues

- Fixed: When using the RemoteImmersiveSpace API to stream spatial content from Mac to Apple Vision Pro, transitioning between the Full immersion style and Progressive does not work during an active stream.  (149590532)
- Fixed: When using the RemoteImmersiveSpace API to stream spatial content from Mac to Apple Vision Pro, the app on Mac will crash if an Immersive Space is already open on Apple Vision Pro.  (151897819)
- Fixed: When using the RemoteImmersiveSpace API to stream spatial content from Mac to Apple Vision Pro, users might get stuck in immersion that transitions between black and passthrough, based on whether hands are visible in the field of view.  (151951590)

###### Known Issues

- When using the RemoteImmersiveSpace API to stream spatial content from Mac to Apple Vision Pro, there might be visual artifacts around objects of high depth disparity, such as near objects overlapping far objects.  (147999474)
- When using the RemoteImmersiveSpace API to stream spatial content from Mac to Apple Vision Pro, an app session might end due to poor Wi-Fi connection, if a user’s Mac freezes, or during transition from wired USB connection to Wi-Fi.   (149237275)  Restart the RemoteImmersiveSpace app.
- When using the RemoteImmersiveSpace API that streams spatial content from Mac to Apple Vision Pro, visionOS 26 beta 2 and macOS 26 beta 2 are not backwards compatible with visionOS 26 beta 1 and macOS 26 beta 1.  (149579399)  Use both visionOS 26 beta 2 and macOS 26 beta 2.
- When using the RemoteImmersiveSpace API to stream spatial content from Mac to Apple Vision Pro, an app session might have video stalls, blurry content, and black rendering on the sides if running on a Mac computer with Apple silicon.  (151322584)  Profile your application and leverage the -renderQuality API new to visionOS and macOS.
- A blank Sharing UI might be shown and get stuck when trying to connect Mac to Apple Vision Pro and starting spatial content streaming using RemoteImmersiveSpace API.  (151503720)  Reboot the Apple Vision Pro and start a new session.
- A blank UI window is shown and gets stuck when using the RemoteImmersiveSpace API to stream spatial content while using Mac Virtual Display.  (151899171)  Start the RemoteImmersiveSpace session without using Mac Virtual Display for the first session on every boot.
- When using the RemoteImmersiveSpace API to stream spatial content from Mac to Apple Vision Pro while in a FaceTime video call, the spatial stream might stall and end.  (151936085)  End the FaceTime video call before using RemoteImmersiveSpace API-enabled apps.
- When using the RemoteImmersiveSpace API to stream spatial content from Mac to Apple Vision Pro while in Travel mode, spatial stream might stall and end.  (151941176)  End Travel Mode while using RemoteImmersiveSpace API-enabled apps.
- If you port an app using Xcode template or Metal 4 with `ProgressiveImmersionStyle` for macOS spatial rendering, the app will crash on macOS.  (153574517)  Use `FullImmersionStyle`.

##### Safari

###### Resolved Issues

- Fixed: The history section in the sidebar does not have the “Clear” button.  (152536922)

##### Scenes and Windows

###### Known Issues

- Calling `openWindow` back-to-back with the same ID and value results in duplicate windows being opened.  (138659891)

##### Security

###### Deprecations

- For apps linked on or after iOS 26 and macOS 26, the default minimum TLS version of `URLSession` and Network frameworks has changed from 1.0 to 1.2. If your process connects only to your servers, verify that they support TLS 1.3 or TLS 1.2. If your process needs to connect to 3rd-party servers which cannot be updated to support newer versions of TLS, restore the previous behavior through `URLSession` and Security framework APIs: `URLSessionConfiguration.tlsMinimumSupportedProtocolVersion` and `sec_protocol_options_set_min_tls_protocol_version`.  (135996267)

##### Storekit

###### New Features

- There is a new option for the `Transaction.Offer.PaymentMode` API called `oneTime`. This new case supports the method of payment for In-App Purchase offer codes.  (142501142)
- Subscription promotional offers can now be signed using JWS and attached to a purchase using the new `PurchaseOption.promotionalOffer(_:compactJWS:)` API. There are also new corresponding SwiftUI APIs in StoreKit to attach a signed promotional offer or a signed introductory offer override to a view.  (143395736)
- SubscriptionOfferView is a new SwiftUI view to merchandise auto-renewable subscriptions. It is designed to capture customers’ attention about the app’s service.  (145251635)

###### Resolved Issues

- Fixed: Subscription status updates might not be reported correctly if the subscription went into billing retry in StoreKit Testing in Xcode.  (133799135) (FB14789854)
- Fixed: Price of offers is not displayed in the payment sheet when making a purchase to a subscription with a higher level of service in StoreKit Testing in Xcode.  (140635780) (FB15980635)
- Fixed: Renewal transactions might be created regardless of the Ask to Buy status of the purchase request in StoreKit Testing in Xcode.  (145242611)

##### Swift Charts

###### Known Issues

- The `.chart3DRenderingStyle` modifier is not functional.  (150430199)

##### Swiftui

###### New Features

- `ControlSize` now conforms to `Comparable`, and `View/controlSize(_:)` can now be used to clamp the environment’s `controlSize` to a given range.  (99633360) (FB11465757)
- Popovers now support customization of their corner radius, through the `presentationCornerRadius(_:)` modifier.  (112938038)
- Confirmation dialogs presented with the `.confirmationDialog` modifier now appear as popovers, anchored to the source of the presentation. When using the `.confirmationDialog` modifier, ensure this is applied to the view to which the dialog should be anchored. When presenting alerts with the `UIAlertController.Style.actionSheet` `preferredStyle`, ensure a `sourceView` is set on the alert controller’s `popoverPresentationController`.  (132598527)
- Text, TextEditor, and TextField now by default use string contents to determine the appropriate base writing direction for each paragraph, instead of relying on layout directionality. To specify the writing direction explicitly on a per-paragraph basis, use Foundation’s `AttributedString.writingDirection` attribute. To make the base writing direction follow the layout direction for an entire view, apply the view modifier `.writingDirection(strategy: .layoutBased)`.  (134821288)
- When linking news SDKs, `NavigationLink`s produce a single view, rather than a list of views in view list contexts. This change improves performance of many `NavigationLink`s in lazy containers like `List`. However, if you are relying on `ContainerValues` propagating out of the `label` view of a `NavigationLink`, or similarly relying on `ContainerValues` of a `ButtonStyle` used to style a link, the `containerValue(_:,_:)` modifier should be moved outside of the link. Below is a minimal example that demonstrates the behavior difference: ```swift
 import SwiftUI
 
 struct ContentView: View {
     @State private var presentPopover = false
     var body: some View {
         NavigationLink("Custom Link", value: 84)
             .buttonStyle(MyButtonStyle(containerValue: "Eighty-four"))
     }
 }
 
 struct ParentView: View {
     var body: some View {
         Group(subviews: ContentView()) { subviews in
             ForEach(subviews) { subview in
                 Text(subview.containerValues.myCustomValue)
             }
         }
         .frame(minWidth: 100, minHeight: 100)
     }
 }
 
 struct MyButtonStyle: PrimitiveButtonStyle {
     var containerValue: String
     func makeBody(configuration: Configuration) -> some View {
         Button(configuration)
             .buttonBorderShape(.circle)
             .containerValue(\.myCustomValue, containerValue)
     }
 }
 
 private struct MyContainerValueKey: ContainerValueKey {
     static let defaultValue: String = "Default value"
 }
 
 extension ContainerValues {
     var myCustomValue: String {
         get { self[MyContainerValueKey.self] }
         set { self[MyContainerValueKey.self] = newValue }
     }
 }
 
 #Preview {
     ParentView()
 }
``` (140283584)
- `List` no longer ignores the vertical insets of rows with a height close to the default minimum height on iOS and visionOS. Use `listRowInsets(_:_:)` to change the vertical row insets.  (141160852)
- In `NavigationSplitView` and `TabView`s configured as `sidebarAdaptable`, the view trailing the sidebar’s safe area is inset in the width of the sidebar. It can display content outside its safe area, underneath the sidebar.  (141222137)
- SwiftUI views and presentations now support breakthrough effects. Breakthrough is an effect allowing elements to be visible to the user even when other app content (3D models, UI elements) is occluding it. To add a breakthrough effect to a SwiftUI view, add the `breakthroughEffect(_:)` modifier. To customize the breakthrough effect of a popover in a volumetric context, use the `presentationBreakthroughEffect(_:)` modifier.  (142705695)
- In apps that adopt the new design, the `buttonBorderShape(_:)` view modifier can be used to customize the shape of bordered buttons. Previously this modifier only affected buttons in Widgets in macOS.  (145773436)
- The `buttonSizing(_:)` view modifier specifies the sizing behavior of `Button`, `Picker`, `Menu`, and other button-producing controls. If you are using `Spacer` views or an infinite-width frame in your `Button` label to create a flexible button, apply `buttonSizing(.flexible)` to the `Button` instead.  (146327046)
- `Button`s using a custom `ButtonStyle` now play system interaction sounds in apps built against visionOS 26 SDK or later. `Button`s using `PrimitiveButtonStyle` do not play sounds.  (150862851)

###### Resolved Issues

- Fixed: `TextEditor`’s undo stack might contain invalid operations for applications with multiple `TextEditor` views.  (83650197) (FB9662463)
- Fixed: The menu content of some `Menu` views does not update as the result of a state change.  (106878937)
- Fixed: [`View.onHover(perform:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/onhover(perform:)) and [`View.onContinuousHover(coordinateSpace:perform:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)) affect hit-testing for gestures. Gestures are not received if one of these view modifiers is used within an overlay.  (108560020)
- Fixed: For an `ImmersiveSpace` scene, the value for defining a custom scene class via the app’s `Info.plist` is ignored.  (129389802)
- Fixed: `listSectionSpacing` does not work correctly for sections that have headers and footers. For more control over the list section layout, use the `listSectionMargins` modifier.  (140929163)
- Fixed: On iOS, `navigationSplitViewColumnWidth()` does not respect the specified minimum and maximum column widths.  (143529326)
- Fixed: Popovers presented from a view positioned at `z != 0` appear at the wrong depth.  (143571112)
- Fixed: Multiple title views in sidebar list labels on iOS are not styled hierarchically as title and subtitle.  (144253754)
- Fixed: In custom layouts that do not implement `explicitAlignment(of:in:proposal:subviews:cache:)`, alignment guides do not work correctly for a right-to-left layout direction.  (145073832)
- Fixed: Applying a `bold` modifier to `Text` resets the `weight` configuration. The interaction of `bold` and `weight` is not consistent between Text and Font.  (147270079)
- Fixed: On platforms supporting edge-attached and non-edge-attached sheets, non-edge-attached sheets present erroneously as full-screen covers when `.navigationTransition(.zoom...)` is specified. If you wish to keep the full-screen cover in compact size classes, configure a sheet with: ```swift
 .sheet(...) {
    ContentView()
     .navigationTransition(.zoom...)
     .presentationSizing(.page)
     .presentationCompactAdaptation(.fullScreen)
``` (150455117)
- Fixed: Standard gesture precedence and failure requirements do not work with `.manipulable`. Nested gestures always take precedence even if they fail.  (150773003)
- Fixed: When presenting a context menu from an ornament or attachment in a Volume, the context menu might not appear relative to origin.  (151803598)
- Fixed: When using the `.hoverEffectDisabled(true)` and `.manipulable` modifiers on the same view, the hover effect glow will still be visible.  (151810879)
- Fixed: If Default Actor Isolation is set to `MainActor`, `@Animatable` macro emits concurrency warnings in Swift 5 language mode and does not compile in Swift 6 language mode.  (152524435)

###### Known Issues

- When a popover is presented from a SwiftUI view within a volume, moving around the volume might cause the popover to become detached from its source content.  (147066605)
- When a background is set for a table view, the header does not adopt the color. This results in the table having the specified color but the header having a transparent background.  (150483611)  Refrain from setting a background on table views.
- When using `.manipulable` modifier on content within a `ScrollView`, if the user is looking at the manipulable item when trying to perform an indirect scroll gesture, manipulation will take precedence over scrolling.  (151659525)
- The detailed surface information classification API might unexpectedly be “none”.  (151820408)
- The `breakthroughEffect(_:)` and `presentationBreakthroughEffect(_:)` modifiers have no effect in the simulator.  (152112050)

###### Deprecations

- `Text` concatenation using the `+` operator is deprecated because it makes it hard to create localized strings that are correct across all languages. Use `Text` interpolation instead. See documentation on `Text` for more info on how to produce localized strings.  (128144043)

##### Tabletopkit

###### New Features

- Using the `CustomAction` API, you can implement custom actions that previously required multiple built-in actions (for example, setting the board for a game of chess). This can reduce network traffic and allow you to define a behavior that is either executed or rolled back atomically on all peers.  (150326238)
- Equipment states can now have custom data via the new `CustomEquipmentState` API.  (150762229)

###### Deprecations

- `interactionWasUpdated` has been deprecated because only some of the provided information is reliably available for remote interactions. The preferred alternative is polling the cursors in the `onUpdate` function of the `TabletopGame.RenderDelegate`.  (150762273)

##### Textkit

###### New Features

- iOS 26, tvOS 26, visionOS 26, watchOS 26, and macOS Tahoe 26 have two methods for resolving the natural alignment `NSTextAlignment.natural` and the last line of `NSTextAlignment.justified` into concrete alignments, `left` and `right`. The first approach utilizes the UI language, which is determined by passing nil-language to `NSParagraphStyle.defaultWritingDirection(forLanguage: )`. This behavior was employed prior to this release. The second method is new and dynamically utilizes the base writing direction for the paragraph. When the base writing direction is set to `NSWritingDirection.rightToLeft`, the text is aligned to `right`, and vice versa. The behavior is selected by API introduced in this major release: `NSTextLayoutManager.resolvesNaturalAlignmentWithBaseWritingDirection`, `NSStringDrawingOptionsResolvesNaturalAlignmentWithBaseWritingDirection`, `UITraitCollection.resolvesNaturalAlignmentWithBaseWritingDirection`, and `NSTextField.resolvesNaturalAlignmentWithBaseWritingDirection`.  (152045248)

##### Ui Frameworks

###### Resolved Issues

- Fixed: Non-SF Symbol images in TabBars and TabViews default to template rendering.  (142894523)
- Fixed: `.hoverEffectsDisabled()` does not disable highlight effects on links within `SwiftUI.Text` views.  (148559710)

###### Known Issues

- Text Effect Windows might be partially cut off when triggered from SwiftUI text fields that are positioned in an ornament at `.topTrailingBack`.  (142326671)
- Apps might receive activation and deactivation notifications when viewing Apple Immersive Video.  (148774882)
- Gaze hover effects might not appear on controls when occluded by another object.  (149493534)

##### Uikit

###### New Features

- Confirmation dialogs presented with the `UIAlertController.Style.actionSheet` `preferredStyle` now appear as popovers, anchored to the source of the presentation. When using the `.confirmationDialog` modifier, ensure this is applied to the view to which the dialog should be anchored. When presenting alerts with the `UIAlertController.Style.actionSheet` `preferredStyle`, ensure a `sourceView` is set on the alert controller’s `popoverPresentationController`.  (152537984)

###### Known Issues

- Popovers, action sheets, and context menus from within a `RealityView` attachment might cause the presented content to appear at the wrong location.  (147613953)
- UIKit non-interactive table view rows might respond to gaze, potentially leading users to perceive them as unresponsive and challenging to navigate.  (150958738)  Use SwiftUI or CollectionViews.

##### Video Toolbox

###### Resolved Issues

- Fixed: Decoding errors in MV-HEVC videos might crash the controlling process, causing the user-facing app to close or video playback to pause. The user can resume playback if the player supports it as the controlling process could relaunch video playback.   (152060939)

##### Webkit

###### Resolved Issues

- Fixed: Non-2D video in Media Source Extensions (MSE) might render incorrectly or cause Safari to hang.  (149733671)

###### Known Issues

- A site will crash when using a 3D model with audio in `<model>`.  (146899549)  Use a 3D model without audio.

##### Widgetkit

###### Resolved Issues

- Fixed: If the `.widgetTexture` modifier is set to `.paper`, the property does not take effect when rendering widgets.  (151808588)
- Fixed: The `.supportedMountingStyles` modifier does not take effect when displaying the widget configuration UI.  (151808744)

##### Widgets

###### Known Issues

- iOS widgets do not appear in the visionOS Widgets app while using visionOS simulator.  (150067581)
- In the Widgets app, app icons in Widget Library might appear as placeholders when running on simulator.  (150547965)
- A visionOS app project might not auto-select the built widget, and the widget will be left in the Suggested section in the Widgets app.  (153326762)  You might need to manually select the widget in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-26-release-notes)*