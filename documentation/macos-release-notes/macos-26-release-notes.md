# macOS Tahoe 26 Beta Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 26 SDK provides support to develop apps for Mac computers running Tahoe 26 beta. The SDK comes bundled with Xcode 26, available from the Mac App Store. For information on the compatibility requirements for Xcode 26, see [`Xcode 26 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26-release-notes).

##### App Store

###### New Features

- A new Accessibility section has been added to the App Store product pages that highlights accessibility features within apps and games. These Accessibility Nutrition Labels give users a new way to learn if an app will be accessible to them before they download it, and give developers the opportunity to better inform and educate their users on features their app supports.  (138344118)

##### Appkit

###### Resolved Issues

- Fixed: With TextKit, the `textRangeByIntersectingWithTextRange` method in `NSTextRange` does not return nil for non-intersecting ranges.  (138067979)

##### Apple Intelligence

###### New Features

- The Foundation Models framework provides you with direct access to the on-device large language model at the core of Apple Intelligence.  (139996377)

###### Known Issues

- Xcode features like Predictive Code Completion and the coding assistant might require Apple Intelligence to be enabled.   (150889516)  Enable Apple Intelligence in System Settings.
- In Image Playground and Genmoji, the new modifiers to customize appearance do not work for Japanese-language users. Generation is blocked when attempting to add modifiers to their appearance.  (151833204)  Removing any modifiers from the dropdowns in Customize Appearance options will allow generations. Users can also use the “Additional description” text field for modifications.
- Model quality output degrades after extended, repeated inferences of the same adapter.  (152468267)

##### Assistantschemas

###### Known Issues

- If you have adopted any of the following email AssistantSchemas, you will experience a compilation error due to a parameter type change: `createDraft`, `updateDraft`, `replyMail`, `forwardMail`, `message`, and `draft`.  (148633307)  Revise the relevant schema implementations to accept an optional `AttributedString` instead of an optional `String` for the body parameter or property, and rebuild your app.

##### Avfoundation

###### Resolved Issues

- Fixed: `AVPlayerLayer` does not ensure a valid video frame is always displayed during item replacement, as the `isReadyForDisplay` property does not remain true during transitions.  (151902458)

##### Background Assets

###### Known Issues

- The system might not update downloaded asset packs as frequently as is expected for apps that internal testers install from TestFlight.   (143281558)  Call `checkForUpdates()` on the shared asset pack manager in your app’s code.
- Asset pack downloads might fail unexpectedly or stall indefinitely, including across reboots.   (151498902)  If your app receives a download status update for a stalled asset pack with a `Progress` object, then call `cancel()` on that object before rescheduling the download. Alternatively, you can fetch and cancel the object that represents the stalled download by calling `currentDownloads` on the shared download manager, extracting the relevant download object from the returned array, and passing the object to a call to `cancel(_:)` on the shared download manager.
- The system might not deliver status updates to your app for ongoing asset pack downloads.   (151647839)  Force Quit and restart your app while testing it.
- An iOS or iPadOS app on an Apple silicon Mac might appear openable in TestFlight even while its essential assets are still being downloaded.  (151709449)  Wait a few minutes to give time for the essential assets to finish being downloaded before attempting to open the app.
- Pausing and resuming an app installation or update while the system is downloading essential asset packs might cause the installation or update to stall indefinitely.  (151942388)  Delete the stalled app from the Home Screen (on iOS, iPadOS, or tvOS), from the Home View (on visionOS), or from the Finder (on macOS) and reinstall it.

##### Catalyst

###### New Features

- For Catalyst apps built with the latest SDK, `UINavigationItem.title` is the window title rather than the window subtitle.  (142423319)
- For Catalyst apps built with the latest SDK, `UIBarButtonSystemItem.fixedSpace` and `.flexibleSpace` are now bridged to `NSToolbar`. The system no longer ignores fixed and flexible spaces when `UIBarButtonItems` are automatically converted to the window toolbar in the Mac idiom. However, the width specified via `fixedSpaceItem(ofWidth:)` is ignored.  (145262754)

##### Cloudkit

###### Known Issues

- CloudKit sharing URLs do not launch third-party apps.  (151778655)

##### Disk Images

###### New Features

- macOS now supports the Apple Sparse Image Format (ASIF). These space-efficient images can be created with the `diskutil image` command-line tool or the Disk Utility application and are suitable for various uses, including as a backing store for virtual machines storage via the Virtualization framework. See [`VZDiskImageStorageDeviceAttachment`](https://developer.apple.comhttps://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment).  (152040832)

##### Finder

###### Known Issues

- Users who enable path bar or status bar in Finder and use list view might be unable to access the last item in the list.  (151917092)  Disable path bar or status bar temporarily.
- Finder does not display Dark Mode app icons or tinted folder colors when the Folder Color setting in System Settings > Appearance is set to Automatic.  (152193702)

##### Foundation

###### New Features

- Interpolating non-localized types into a `LocalizedStringResource/String(localized:)/AttributedString(localized:)` value will now display a deprecation warning instead of potentially falling back to a fully-unlocalized string. Provide a localized value to interpolate into the text instead, or silence the warning by wrapping the unlocalized value in a call to `String(describing:)`.  (126876158)
- `ISO8601FormatStyle` now allows fractional seconds, regardless of the setting of `includingFractionalSeconds`. Additionally, `ISO8601FormatStyle` now allows hours-only time zone offsets.  (136950769)

###### Resolved Issues

- Fixed: Functions that initialize a string from a C-string pointer do not validate that the provided encoding is a valid encoding for C-strings.  (143756086) (FB16417968)

##### Foundation Models Framework

###### Known Issues

- When you pass `includeSchemaInPrompt: false` to `respond` or `streamResponse`, it is not respected.  (151926006)
- Custom `@Generable` types named `Number` or `Boolean` might not function reliably in guided generation.  (152280144)  Use a different type name.
- Some instructions and prompts to the model might not lead to expected responses. Use Feedback Assistant to report satisfactory or unsatisfactory cases. When applicable, you can use the `LanguageModelFeedbackAttachment` API to serialize the feedback to a file and attach it to Feedback Assistant.  (152318091)  Refine your instructions and prompts using `#Playground` in Xcode. When applying guided generation with a `@Generable` type, add `@Guide` with a custom description on properties to steer the model’s responses.
- Tool calling might not function properly if primitive types such as `Int`, `String`, or `Bool` are used as the argument.  (152318534)  Define a custom `@Generable` type.
- In an Xcode Playground, requests made to the model might receive a “rate limit exceeded” error.  (152325506)  Close and reopen the playground tab in the canvas.

##### Full Screen

###### Known Issues

- You might experience layout issues when going full screen with certain apps on a Mac.  (151266898)

##### Game Controller

###### New Features

- For supported game controllers, pressing the Home button once opens the Game Overlay. Set `preferredSystemGestureState` to receive additional Home button press events.  (137780853)

##### Intel Macs

###### Known Issues

- Safe and Recovery modes on Intel Macs have performance and graphical issues, though the modes are still functionally usable. Various elements on the screen, such as menus, alerts, and Control Center, might partially display. Scrolling and other operations in some apps cause visual glitches.  (149419875)

##### Keyboard

###### New Features

- In the “ABC – India” keyboard layout, the ₹ (rupee) symbol has replaced the ``` (back tick) symbol. To type the back tick symbol that’s commonly used in Markdown and some programming contexts, you can use the ⌥ (option) modifier in conjunction with the same key or you can use an alternative layout like “ABC”.  (149026394)

##### Maps

###### Known Issues

- Users cannot plan a route that leaves at or arrives by a future time.  (150947515)
- If you tap to expand the “Recents” section and there are more recent places than can fit in the view, the Terms & Conditions link will disappear, making it inaccessible.  (152197565)  Tap again on “Recents”. The recents list will fold and the Terms & Conditions link will be displayed.

##### Menu Customization

###### Known Issues

- Menu customization in apps like Notes and Mail might have some visual glitches.  (148472167)

##### Messages

###### Known Issues

- Users on older devices won’t see compatibility messages for polls, so they might be unaware a poll was sent.  (148545742)
- Sent translated messages do not get re-translated after editing.  (149401758)  Send the message again instead of editing the original.
- Expanding Conversation Details causes the list of conversations to collapse.  (149436051)  Closing Conversation Details will bring back the list.
- In regions where Screen Unknown Senders is on by default, notifications for message categories are erroneously off by default.  (149450560)  In Messages settings, manually enable notifications for the categories with the Allow Notifications setting of the Unknown Senders section.
- Transaction or Promotion messages filtered by a Message Filter App Extension might be badged as “Unknown” in the conversation list rather than “Transaction” or “Promotion”.  (151869409)
- Scrolling through a Messages conversation might be sluggish.  (152453655)  Quit and relaunch Messages.

##### Metal

###### New Features

- Metal 4 is now supported. See [`Metal`](https://developer.apple.comhttps://developer.apple.com/metal/) for additional details.  (113781091)

###### Known Issues

- If you’re using Metal 4 command encoders, you should add render and compute pipelines that support indirect command buffers to your residency sets. The Metal device driver currently does not enforce this requirement.  (145066238)
- Metal Shader Validation might not work with shaders that use Metal Performance Primitives.  (149263281)
- Metal Shader Validation might not work with Metal 4 ray tracing pipelines.  (152520367)  Selectively disable Shader Validation for pipelines using ray tracing. See [`documentation`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/validating-your-apps-metal-shader-usage/#Selectively-enable-Shader-Validation).

##### Metalfx

###### Known Issues

- Denoised temporal upscaling for MTL4CommandBuffer’s `MTL4FXTemporalDenoisedScaler` does not work.  (146436460)
- Temporal upscaling for MTL4CommandBuffer’s `MTL4FXTemporalScaler` does not work.  (146436741)

##### Networkextension

###### Deprecations

- Algorithms DES, 3DES, SHA1-96 and SHA1-160 as well as Diffie-Hellman groups less than 14 are no longer supported for IKEv2 VPNs.  (148767790)

##### Notifications

###### Known Issues

- The icons for Calendar notifications might appear washed out.  (151658533)

##### Nslog

###### New Features

- Dynamic string data in format arguments for `NSLog` will be redacted to `\<private\>` in the Unified Logging System. This specifically targets data that enters the Unified Logging System via `NSLog`, and will not impact the Xcode console or `NSLog`’s `stdout` output. If you wish to log un-redacted data to the Unified Logging System please use the “os_log” or “Logger” interfaces.  (137129180)

##### Nstextview

###### New Features

- NSTextView supports sound files, such as QuickTime Audio, attached via NSTextAttachment, by utilizing AVPlayer for playback inline.  (140224296)

##### Photos Photos Picker

###### Known Issues

- Invoking search in the Photos picker causes the picker to crash. Or invoking Search in a collection in Photos causes Search to crash.  (152403781)  Use the Photos app to search for the content. Once you’ve found it, you can share or copy it to continue with the workflow. Use Search in the Library tab to find the content.

##### Photos Picker

###### Known Issues

- On macOS, the Options menu is missing in the Photos picker. Ability to exclude Location and Captions information cannot be set when using the Photos picker.  (152336867)  Use iOS device to share instead.

##### Realitykit

###### Resolved Issues

- Fixed: Entities with a PortalComponent ignore any ModelSortGroupComponent and instead use a fixed rendering order. In case of sorting rendering issues with portal surface, explicitly add a ModelSortGroupComponent using a `.planarUIAlwaysBehind` sort group.  (149899345)

###### Known Issues

- Some properties and components do not update SwiftUI Views when accessed through the `.observable` property on Entity.  (147063698)
- `ParticleEmitterComponent` does not render properly on iOS, macOS, and tvOS.  (152201501)
- The `animate` functions on `Entity` and `RealityViewContent` do not start animations.  (152456435)

##### Rtl

###### Known Issues

- You might experience layout issues with RTL languages.  (151009428)

##### Secure Text Fields

###### Known Issues

- On a Mac with a Touch Bar, a secure text field swallows keyboard events in some contexts. For example, this might occur when creating a new user in the Users & Groups settings pane.  (151268030)  Click a window in another app, then go back to the original window.

##### Security

###### Deprecations

- For apps linked on or after iOS 26 and macOS 26, the default minimum TLS version of `URLSession` and Network frameworks has changed from 1.0 to 1.2. If your process connects only to your servers, verify that they support TLS 1.3 or TLS 1.2. If your process needs to connect to 3rd-party servers which cannot be updated to support newer versions of TLS, restore the previous behavior through `URLSession` and Security framework APIs: `URLSessionConfiguration.tlsMinimumSupportedProtocolVersion` and `sec_protocol_options_set_min_tls_protocol_version`.  (135996267)

##### Settings

###### Known Issues

- Users who enable Reduce Transparency might encounter flickering in background windows or the Dock.  (152060485)

##### Setup Assistant

###### Known Issues

- 802.1X Wi-Fi networks are not saved during initial device setup.  (147787689)
- On Intel Macs, the background on the Hello or Welcome screens might be black.  (152107967)  Click Get Started or anywhere on the screen to proceed to the next step.
- Visual pairing for Quickly Set Up Mac does not work.  (152326903)  Use manual pairing.
- On the 13” MacBook Air, Hello might be offset from the wallpaper during initial device setup.  (152447100)  Click Get Started or anywhere on the screen to proceed to the next step.

##### Siri

###### Known Issues

- Siri Visual Responses might be illegible behind certain backgrounds.  (151682699)

##### Storekit

###### New Features

- There is a new option for the `Transaction.Offer.PaymentMode` API called `oneTime`. This new case supports the method of payment for In-App Purchase offer codes.  (142501142)
- Subscription promotional offers can now be signed using JWS and attached to a purchase using the new `PurchaseOption.promotionalOffer(_:compactJWS:)` API. There are also new corresponding SwiftUI APIs in StoreKit to attach a signed promotional offer or a signed introductory offer override to a view.  (143395736)

###### Resolved Issues

- Fixed: Subscription status updates might not be reported correctly if the subscription went into billing retry in StoreKit Testing in Xcode.  (133799135) (FB14789854)
- Fixed: Price of offers is not displayed in the payment sheet when making a purchase to a subscription with a higher level of service in StoreKit Testing in Xcode.  (140635780) (FB15980635)
- Fixed: Renewal transactions might be created regardless of the Ask to Buy status of the purchase request in StoreKit Testing in Xcode.  (145242611)
- Resolved an issue with the `Identifiable` conformance of the `PurchaseIntent` API. Conformance to this protocol now begins starting with iOS 18.0 and macOS 15.0.  (148751460) (FB17151889)

##### Swift Compiler

###### Known Issues

- The Swift compiler might crash when building a project that initializes a `UISymbolContentTransition`.  (150858005)

##### Swift Standard Library

###### Known Issues

- The `span` properties of `InlineArray` and `CollectionOfOne` trap at runtime.   (147500528)
- `mutating` members of `MutableSpan` and `MutableRawSpan` are unavailable.  (152467655)  Add “-enable-experimental-feature InoutLifetimeDependence” to the “swift-module-flags” line of the swiftinterface file.

##### Swiftui

###### New Features

- On macOS, an animated SwiftUI.Transaction that changes a `Window`‘s size animates the window’s frame, alongside the frame of the hosting view.  (61158194)
- You can now use `View/findNavigator(isPresented:)`, `View/findDisabled(_:)`, and `View/replaceDisabled(_:)` to control the presentation of the Find Bar in `TextEditor` on macOS 26.  (85308161)
- `ControlSize` now conforms to `Comparable`, and `View/controlSize(_:)` can now be used to clamp the environment’s `controlSize` to a given range.  (99633360) (FB11465757)
- In apps built with the macOS 26 SDK, `Section` footers within a `Form` of the `GroupedFormStyle` now have leading alignment, default font, and foreground styles. Use the `sectionActions(content:)` view modifier on your `Section` to supply section actions, which maintain a trailing placement in macOS. In iOS and iPadOS, each section action displays as its own form row.  (129868475)
- Text, TextEditor, and TextField now by default use string contents to determine the appropriate base writing direction for each paragraph, instead of relying on layout directionality. To specify the writing direction explicitly on a per-paragraph basis, use Foundation’s `AttributedString.writingDirection` attribute. To make the base writing direction follow the layout direction for an entire view, apply the view modifier `.writingDirection(strategy: .layoutBased)`.  (134821288)
- In apps built with the macOS 26 and iOS 26 SDKs, a `Picker` view of a style that produces a button-like control now has a fitted sizing behavior by default. If needed, use the `buttonSizing(_:)` view modifier to make the `Picker` flexible and fill the available width of its container.  (136649748)
- The default label style for macOS menu content is now `.titleAndIcon`.  (137306701)
- The implementation of some macOS buttons no longer uses `NSButton`.  (139105246)
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
- In macOS, a `Form` of the `.grouped` style now has a more compact appearance when placed within a sidebar or inspector.  (141534926)
- Reuse existing AppKit gesture recognizers in SwiftUI using [`NSGestureRecognizerRepresentable`](https://developer.apple.comhttps://developer.apple.com/documentation/SwiftUI/NSGestureRecognizerRepresentable), and refer to them by name using [`name`](https://developer.apple.comhttps://developer.apple.com/documentation/AppKit/NSGestureRecognizer/name).  (142918018)
- On macOS, after linking new SDKs, the style of search fields with `SearchFieldPlacement.sidebar` is now fixed to the toolbar. Previously the search field would scroll as the first element in the list.  (143546967)
- In apps that adopt the new design, the `buttonBorderShape(_:)` view modifier can be used to customize the shape of bordered buttons. Previously this modifier only affected buttons in Widgets in macOS.  (145773436)
- The `buttonSizing(_:)` view modifier specifies the sizing behavior of `Button`, `Picker`, `Menu`, and other button-producing controls. If you are using `Spacer` views or an infinite-width frame in your `Button` label to create a flexible button, apply `buttonSizing(.flexible)` to the `Button` instead.  (146327046)
- In macOS apps that adopt the new design, buttons of the `.bordered` style can  be tinted with the `tint(_:)` view modifier.  (150127133)

###### Resolved Issues

- Fixed: `TextEditor`’s undo stack might contain invalid operations for applications with multiple `TextEditor` views.  (83650197) (FB9662463)
- Fixed: In macOS, `Button` inherits its environment’s font instead of using a default font appropriate for its `controlSize`. Apply view modifiers to the button’s label to customize its font.  (92434021)
- Fixed: In macOS, the value label of `MenuPickerStyle` does not truncate when it is long enough to cause the button to be wider than its container.  (93843377)
- Fixed: The menu content of some `Menu` views does not update as the result of a state change.  (106878937)
- Fixed: [`View.onHover(perform:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/onhover(perform:)) and [`View.onContinuousHover(coordinateSpace:perform:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)) affect hit-testing for gestures. Gestures are not received if one of these view modifiers is used within an overlay.  (108560020)
- Fixed: Section views without `isExpanded` binding are collapsible in a sidebar-styled List on macOS.  (115797465) (FB13192271)
- Fixed: `listSectionSpacing` does not work correctly for sections that have headers and footers. For more control over the list section layout, use the `listSectionMargins` modifier.  (140929163)
- Fixed: On iOS, `navigationSplitViewColumnWidth()` does not respect the specified minimum and maximum column widths.  (143529326)
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

###### Known Issues

- If Default Actor Isolation is set to `MainActor`, `@Animatable` macro emits concurrency warnings in Swift 5 language mode and does not compile in Swift 6 language mode.  (152524435)  Use Swift 5 language mode or set Default Actor Isolation to `nonisolated` in project’s build settings.

###### Deprecations

- `Text` concatenation using the `+` operator is deprecated because it makes it hard to create localized strings that are correct across all languages. Use `Text` interpolation instead. See documentation on `Text` for more info on how to produce localized strings.  (128144043)

##### Textkit 2

###### New Features

- A new property, `includesTextListMarkers`, is introduced to `NSTextList`, `NSTextContentStorage`, and `NSWritingToolsCoordinator`. This property controls whether to include the text list marker string in the contents of `NSAttributedString` for paragraphs associated with `NSTextList`. TextKit 1 expects the marker string, while TextKit 2 does not. The TextKit 2 behavior was adopted by UIKit starting with iOS 18 (`includesTextListMarkers=NO`). AppKit is also adopting the TextKit 2 text list behavior starting with macOS 26.  (128479184)

##### Translation

###### Known Issues

- For Catalyst apps using `.translationTask()`, buttons in the download approval UI might not work.  (151313115)  Either manually download the languages you need beforehand from System Settings, or build your Catalyst app with the “Optimize for Mac” setting.

##### Uikit

###### New Features

- In TextKit 2, the `includesTextListMarkers` property has been introduced to `NSTextList`, `NSTextContentStorage` and `NSWritingToolsCoordinator`. For paragraphs associated with `NSTextList`, the property controls whether to include the text list marker string in the `NSAttributedString` contents. The classes within TextKit 1 expect the marker string, while the classes within TextKit 2 do not.  (144903293)

##### Virtual Machines

###### Known Issues

- When playing Apple TV+ content from the beginning in VMs, users will see a black video during the recap portion.   (151316651)  Wait until the recap portion is done, or scrub to the point where the recap is done.
- Virtual machine networking fails if you start a bridge mode VM while a shared or host mode VM is running, and vice versa. The networking of the existing VM is not affected.  (151477625)  Do not use shared or host mode VM and bridge mode VM at the same time.
- When playing protected content in a VM in Safari or Apple TV+, the app will hang and UI might flicker.  (151945328)  Skip playing protected content in a VM. If you encounter a hang, restart the VM.

##### Weather

###### Known Issues

- Users might see a blank white button on some tips for Weather features. The button will be operable.  (152088799)

##### Webkit Api

###### Known Issues

- `WKPreferences.isLookToScrollEnabled` is not available on non-visionOS platforms.  (152106377)


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-26-release-notes)*