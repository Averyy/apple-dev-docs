# visionOS 27 Beta 4 Release Notes

**Framework**: visionOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS 27 SDK provides support to develop apps for Apple Vision Pro devices running visionOS 27 beta 4. The SDK comes bundled with Xcode 27, available from the Mac App Store. For information on the compatibility requirements for Xcode 27, see [`Xcode 27 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-27-release-notes).

##### App Intents

###### New Features

- You can now pass a name parameter of type `AttributedString` to the `notes.createNote` and `notes.updateNote` schemas.  (173431080)

###### Known Issues

- AppEntity instances have a cumulative size limit of 10MB, including all child properties and their values. Your app might crash if an entity exceeds this limit, and the exception is logged.  (181763422)

###### Deprecations

- The `calendar.deleteEvents` schema has been renamed to `calendar.deleteEvent`.  (176751155)

##### Apple Intelligence Report

###### Resolved Issues

- Fixed: When you view Apple Intelligence Report entries for Home Intelligence, some data that was sent to Private Cloud Compute won’t appear in the report.  (176056930)

##### Arkit

###### Resolved Issues

- Fixed: For room anchors delivered by the `RoomTrackingProvider` Swift API, `RoomAnchor.planeAnchorID`s and `RoomAnchor.meshAnchorID`s are always empty. Likewise, for the `room_tracking.h` C API, `ar_room_anchor_get_plane_anchor_identifiers` and `ar_room_anchor_get_mesh_anchor_identifiers` always return an empty list of identifiers.  (173005535)

##### Background Assets

###### New Features

- You can reduce your app’s storage usage with localized asset packs. The system delivers the appropriately localized asset packs based on the user’s preferred languages.  (163944365)

##### Bluetooth

###### Known Issues

- Spatial accessory tracking might not initialize when first paired via Bluetooth.  (181827411) **Workaround:** Turn the accessory off and then on, or turn Bluetooth off and on.

##### Compositor Services

###### Resolved Issues

- Fixed: `RemoteImmersiveSpace` might be unable to discover the remote device, causing immersive content delivered to Apple Vision Pro to fail to display.  (177989580)

##### Eyesight

###### Resolved Issues

- Fixed: The EyeSight privacy indicator animation for screen capture only appears during your first Siri query after you restart your device.  (177984075)

##### Foundation

###### Resolved Issues

- Fixed: `+[NSURL URLWithString:]` no longer double-encodes the `%` of valid percent-escape sequences when encoding other invalid characters.  (161588649) (FB20439045)

##### Foundation Models

###### Resolved Issues

- Fixed: Private Cloud Compute might not work when you use simulators.  (177684296)
- Fixed: `@Generable` on an `enum` produces a deprecation warning about `GenerationError` that cannot be silenced.  (177899620)
- Fixed: Truncating transcript history in the `onPrompt` modifier might cause an unexpected runtime error.  (177901494)
- Fixed: `onPrompt` might not be called when applied to a `Profile` without instructions.  (177902488)
- Fixed: `PrivateCloudComputeLanguageModel` always uses greedy decoding.  (178181782)

###### Known Issues

- When using the on-device Apple Foundation Model for both tool calling and guided generation, some prompts might cause the model to call tools excessively.  (177748926) **Workaround:** Adjust your instructions, prompts, and attachment labels.

##### Foveated Streaming

###### Resolved Issues

- Fixed: `FoveatedStreamingProvider` app extensions cannot access the microphone.  (175954012)

##### Freeform

###### Resolved Issues

- Fixed: When a Freeform board is curved, the back button might become unresponsive after you exit preview mode for a spatial photo, spatial video, or USDZ file.  (172204615)

##### Genmoji

###### Resolved Issues

- Fixed: The Genmoji or Image Playground panel might appear blank when invoked from Safari or Freeform.  (175025165)

##### Hand Ui

###### Resolved Issues

- Fixed: The battery percentage that appears in the status bar when you raise your hand and flip it over might be inconsistent with the percentage displayed in Control Center.  (175742923)

##### Image Playground

###### Resolved Issues

- Fixed: In the Image Playground photo picker, the All and Suggested tabs are missing, which might limit the number of photos available for you to choose from.  (178256174)

##### Mac Virtual Display

###### Resolved Issues

- Fixed: When donning the Apple Vision Pro it may sometimes disconnect instead of resuming the session.  (178359724)

##### Mail

###### Resolved Issues

- Fixed: Emails might display content that doesn’t match their subject line.  (169101671)

##### Metal

###### Resolved Issues

- Fixed: When you use a sampler to read from a texture with clamp-to-edge addressing mode, the result might be clamped to zero.  (172520325)
- Fixed: On devices in the Apple 10 GPU family, using a sampler to read from a texture with clamp-to-edge addressing mode might produce results that are clamped to zero.  (177318505)

##### Network Security

###### New Features

- Starting in 27.0 operating systems, select system processes now enforce stricter network security (TLS) requirements. These new requirements might cause connections to fail if the server does not meet them. The affected processes are those involved in MDM, DDM, Automated Device Enrollment, configuration profile installation, app installation, and software updates. Servers must support TLS 1.2 at minimum, using cipher suites and certificates that meet App Transport Security (ATS) requirements. For additional details on affected processes, requirements, and how to audit and diagnose failures in managed environments, please reference [`Prepare your network environment for stricter security requirements`](https://developer.apple.comhttps://support.apple.com/en-us/126655). For additional details on ATS and the new requirements, please reference [`Preventing Insecure Network Connections`](https://developer.apple.comhttps://developer.apple.com/documentation/Security/preventing-insecure-network-connections) and [`NSRequiresNIAPTLSPackageVersion`](https://developer.apple.comhttps://developer.apple.com/documentation/BundleResources/Information-Property-List/NSRequiresNIAPTLSPackageVersion).  (176055825)

##### On Demand Resources

###### Deprecations

- On Demand Resources and the `NSBundleResourceRequest` API are deprecated. Use Background Assets instead.  (170066290)

##### Persona

###### Known Issues

- Spatial Personas may appear laggy during High Quality Recording.  (178441141)

##### Quick Look

###### Resolved Issues

- Fixed: Buttons in the annotation window might lose focus and become unresponsive on the first pinch.  (172214657)
- Fixed: When in annotation mode, annotations placed inside an object or within the bounding box of a convex object might not be selectable.  (174174518)
- Fixed: Annotation text might become blank, preventing you from creating, selecting, or deleting additional annotations.  (177726175)
- Fixed: In annotation mode, annotations don’t respond to direct touch input and flicker when directly touched.  (178087194)
- Fixed: In annotation mode, the Delete button sometimes switches the annotation to the editing UI.  (178087667)

###### Known Issues

- When at an interior Viewpoint in a USD preview, using drag gestures to move the scene can cause a severe jump of the asset position.  (180152079) **Workaround:** Apply the gesture slowly, avoiding a quick hand motion. Reset the positioning by choosing the desired Viewpoint again.

##### Reality Composer Pro Preview on Visionos

###### Resolved Issues

- Reality Composer Pro Preview, which lets you preview your content on visionOS in real time directly from your Mac, is now available. For more information on the Reality Composer Pro macOS app, see [`Reality Composer Pro Release Notes`](https://developer.apple.comhttps://developer.apple.com/documentation/realitycomposerpro/reality-composer-pro-release-notes).  (179045352)

##### Realitykit

###### Resolved Issues

- Fixed: The `.highlight` hover effect style highlights the entire RealityKit entity hierarchy during direct interactions, rather than only the entity being targeted.  (158462269) (FB19680952)
- Fixed: Soft Shadows and Spotlight Shadow Quality do not work in visionOS Simulator because the feature relies on the clustering system, which is disabled due to restricted tier 2 argument buffer issues.  (169054912)
- Fixed: Content in a portal incorrectly receives outside environment probe lighting contribution.  (175363970)
- RealityRenderer’s `isToneMappingEnabled` property enables and disables tone mapping if apps are rebuilt with the 27.0 SDK. Apps built with earlier versions of the SDK don’t see a behavior change.  (177283932)
- Fixed: `ComputeGraphComponents` stored in a Reality file do not render when loaded.  (177674901)
- Fixed: The behavior tree’s `SetTree` node might not reset the status of nodes belonging to the intended tree when you enter that tree for a second time. Additionally, if the `SetTree` node has adjacent children to its right, the adjacent children might process before the new tree is set. To prevent adjacent children from processing early, ensure the `SetTree node` is the rightmost node in its subtree.  (177688899)
- Fixed: Skinning animation or high subdivision level on complex geometry can cause excessive memory growth and may cause the app to be terminated due to high memory usage.  (177731588)
- Fixed: Opaque ShaderGraph materials appear darker than Physically Based Materials when lit by dynamic lights.  (177974279)
- Fixed: When `OpacityComponent` is applied to an entity with opaque materials, `RealityRenderer` renders the opaque materials with transparency, revealing interior surfaces. Only the frontmost surface should appear with partial transparency.  (177976245)
- Fixed: Shadow rendering memory is not counted against each application’s memory limit, which might prevent apps from consistently using up to 8 shadowed directional and spot lights depending on what other apps are running.  (177984485)

###### Known Issues

- Some MaterialX 1.39 nodes are not supported.  (172875414)
- Shaders using the new RealityKit shader node name of `ND_realitykit_pbr_surfaceshader_2_0` will fail to load in Quick Look or with USDKit.  (181616779)

##### Rekit

###### Resolved Issues

- Fixed: Specular highlights in the PBR shading model do not fade out correctly at low specular values. A visible specular effect persists even when the specular parameter is set to 0, causing materials with zero specular to appear reflective instead of non-reflective.  (178289846)

##### Screen Recording

###### Resolved Issues

- Fixed: With High Quality Recording enabled, capturing a High Quality recording while the device is warm may fail silently. No recording is saved and no error or feedback is shown.  (170105618)
- Fixed: When you switch between High Quality Recording and Standard Recording in Screen Recording settings, the recording subsystem may enter an unrecoverable state; subsequent screen recordings from Control Center might not start.  (178467174)

##### Shadergraph

###### Resolved Issues

- Fixed: The `realitykit_hair_surfaceshader` node does not support `DiffuseLightProbeGroupComponent`. Materials built with this node might not respond to diffuse light probe group lighting.  (177976666)

##### Shortcuts

###### Resolved Issues

- Fixed: The Use Model action might fail to run when using the On-Device option for some output types.  (181071784)

###### Known Issues

- If an app intent uses Duration or `LPLinkMetadata`, creating a shortcut with that intent and then attempting to edit it with “Describe a change” might fail.  (166068090) **Workaround:** If the model discards the action, press “Undo” to recover the unsupported intent.
- When an app intent defines a `UnionValue` parameter with two number-related types (for example, both Int and Double), the number option appears twice in the parameter picker menu and shows as double-selected.  (168315587) **Workaround:** Define only one number-related type in the `UnionValue` parameter (for example, use only Int or only Double, not both).

##### Siri

###### New Features

- You can now activate Siri by looking at the Siri “orb” and speaking, as an alternative to using “Hey Siri” or “Siri”. This feature is enabled in Beta 2.  (177137200)

###### Resolved Issues

- Fixed: Siri ignores custom values for navigation preferences, transport, and incident types in apps that use `maps.startNavigation` or `maps.reportIncident` intent schemas.  (175230813)
- Fixed: If you select the Ask Siri button in context menus or the text edit bar multiple times, multiple instances of Siri might appear and overlap with each other.  (175372716)
- Fixed: On visionOS, when Type to Siri is selected, dragging and dropping an image to Siri might not add the image to the Ask Siri input field.  (176312944)
- Fixed: When you enable Guest User Mode on Apple Vision Pro, Siri becomes unavailable.  (177104604)
- Fixed: When you ask Siri to send a message to a contact that doesn’t exist on your device, Siri might draft a message to an unrelated contact.  (177356158)
- Fixed: Siri might not resolve some entity types when your app has provided only an `EntityStringQuery` for the entity type.  (177464215)
- Fixed: Asking Siri to call short phone numbers, such as “Call 17”, might fail.  (177545828)
- Fixed: Disabling Siri might not delete your Siri and Dictation interaction history from your device.  (177649865)
- Fixed: Siri might not find app-specific contacts that are only indexed in Spotlight and do not appear in the Contacts app.  (177679168)
- Fixed: When you use ChatGPT with Apple Intelligence, some responses used in follow-up queries or when you resume a chat might be logged by Apple.  (177755742)
- Fixed: When you tap the Send button in the Siri message confirmation flow, the message might fail to send.  (178025056)
- Fixed: Asking Siri to generate images will present the images in a UI that is not scrollable.  (178091669)
- Fixed: When the Siri app chat canvas is resized to a narrow width in text entry mode, the thumbs up and thumbs down feedback buttons might be obscured by the text input platter.  (178161357)
- Fixed: The search text field maintains keyboard focus after returning from searching in a list using the back button.  (178191950)
- Fixed: Siri “orb” and UI does not correctly follow the system breakthrough behavior when near another window.  (178265130)
- Fixed: Conversation cards might disappear after you return from a conversation view using the back button.  (178342580)
- Fixed: If you pin the Siri “orb” and then reboot the device, saying “Hey Siri” might summon two “orbs”.  (178383647)
- Fixed: Tapping an inactive Siri “orb” or the microphone button in the Siri app might not turn on Siri.  (180066367)

###### Known Issues

- When you ask Siri for Maps information, the response snippets might appear incomplete or display formatting issues.  (177116121) **Workaround:** Ask Siri to repeat the information, or open Maps directly for complete details.
- Siri commands for Environments aren’t working.  (178082773) **Workaround:** Use gaze and pinch to open environments from the Home View.

##### Siri Setup

###### Resolved Issues

- Fixed: The App Clips navigation button appears in Siri settings, even though the App Clips feature is not supported on visionOS.  (178269460)

##### Spatial Accessories

###### Resolved Issues

- Fixed: During use, Spatial Accessories - such as the Logitech Muse stylus or PSVR2 controllers - might stop registering inputs or being tracked.  (177983488)

##### Spatial Gallery

###### Resolved Issues

- Fixed: Spatial Gallery may freeze when loading panoramas.  (177737702)

##### Spatial Preview

###### Resolved Issues

- Fixed: Some large 3D models with poor mesh connectivity of approximately 750,000 to 3.75 million triangles might not appear when previewing on Apple Vision Pro.  (174366004)

##### Spatial Web

###### Resolved Issues

- Fixed: WebXR might not render when you use Simulator.  (178666073)

##### Status Bar

###### Known Issues

- Battery percentage might not be up-to-date in the status bar.  (174929463) **Workaround:** Open Control Center to update the battery percentage.

##### Storekit

###### New Features

- Offer code redemption APIs now return a `VerificationResult` when redemption completes. If a redemption succeeds, your app receives a `VerificationResult` that contains a `Transaction` object. If a redemption fails, your app receives an error that describes what caused the redemption to fail.  (141012819)
- StoreKit now includes the `Transaction.OwnershipType.assigned` and `Transaction.RevocationType.assignmentRevoked` enum values to support volume purchases. `Transaction` query methods now additionally return transactions assigned to the Managed Apple Account.  (156749517)
- New `Product.ProductType` APIs represent subscription Bundles and subscription Suites. New APIs in `Product.SubscriptionInfo.BundledSubscription` let you fetch merchandising data about subscriptions contained in a Bundle. Transaction and RenewalInfo contain new fields that provide information about purchases and customer status regarding Bundles and Suites.  (160501742)
- `partnerName` and `partnerId` properties for Advanced Commerce API are available in [`Transaction.AdvancedCommerceInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct) and [`RenewalInfo.AdvancedCommerceInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct).  (167808780)

###### Resolved Issues

- Fixed: Displaying the offer code sheet or the manage subscription sheet consecutively might cause the app to hang when using StoreKit Testing in Xcode.  (181171733)

###### Known Issues

- The refund request, offer code redemption, and manage subscriptions sheets might fail to present in TestFlight.  (180999342) (FB23487953)
- Purchases of non-subscription In-App Purchases made using the SKTestSession.buyProduct() method might fail with an invalid product error. The billingPlanType(_:) PurchaseOption isn’t respected for subscription purchases.  (181842500)

##### Storekit Testing in Xcode

###### Resolved Issues

- Fixed: The unified app receipt is not updated after forcing a subscription expiration with `SKTestSession`.  (102093015) (FB11767567)
- Fixed: The `SKTestSession` `disableDialogs` setting is not always respected for all system dialogs.  (154390284) (FB18403150)
- Fixed: Subscription upgrades performed with the Xcode Transaction Manager are not reported in `Transaction.updates`.  (160698598) (FB20269723)
- Fixed: The renewal behavior preference is not respected when using the `purchaseDate(_:renewalBehavior:)` purchase option to make purchases using `SKTestSession`.  (162014134) (FB20537538)
- Fixed: StoreKit UI actions (manage subscriptions, redeem offer code, and refund request) don’t perform the desired action on visionOS when using StoreKit Testing in Xcode.  (172677527)
- Fixed: Re-purchasing a previously refunded non-consumable fails with an already owned error when using StoreKit Testing in Xcode.  (174560379) (FB22475017)
- Fixed: Using `pricingTerms.commitmentInfo.price` in StoreKit Testing in Xcode returns an incorrect price for monthly subscriptions with a 12-month commitment.  (177942756)
- Fixed: Transactions for upgraded subscriptions are immediately marked as expired when using StoreKit Testing in Xcode.  (178441109)
- Fixed: Purchases fail on visionOS when initiated from offer code redemption or from the manage subscriptions sheet.  (180741834)

##### Swift Charts

###### Resolved Issues

- Fixed: When your project has a minimum deployment target lower than 27.0, using conditionals inside a `Chart` closure produces the warning “Conformance of `_ConditionalContent<TrueContent, FalseContent>` to `ChartContent` is only available in ‘’ 27.0 or newer,” and the app might crash at runtime when that content is loaded.  (174168981)

##### Swiftdata

###### Resolved Issues

- Fixed: You might experience a deadlock for @Query when saving a ModelContext on a background actor while scheduling new async tasks for a ModelActor.  (178113288)

##### Swiftui

###### New Features

- `AsyncImage` now automatically caches downloaded images using HTTP caching protocols, allowing servers to control caching behavior via standard headers. You can customize caching for specific images using the new `AsyncImage` initializers that accept `URLRequest` with custom `cachePolicy` settings. Additionally, you can set a custom `URLSession` using the new `View.asyncImageURLSession(_:)` API to control how all child `AsyncImage` views perform data tasks.  (78212597)
- A `@State` declared with an expression as its initial value used to evaluate the expression each time the view struct re-instantiates. In the case of `@State private var model = Model()`, this means `Model.init()` gets called many times throughout the view’s lifetime. Xcode 27 introduces a new `@State` implementation that avoids this repeated evaluation. This new behavior back-deploys to iOS 17 aligned OSes. The new `@State` is implemented with a Swift macro. It is largely source compatible with the property wrapper version, with a few exceptions. If you provide an initial value at `@State` declaration, and also try to assign a value to it in an initializer, the initializer value is discarded. This behavior has not changed because of the macro, but some such cases no longer compile: ```None
 struct StickerPageView: View {
     @State private var page = StickerPage()
     let title: String
 
     init(title: String) {
         // `title` won't have any effect
         // this also won't compile with @State macro
         self.page = StickerPage(title: title)
         self.title = title
     }
 }
``` When assigning initial value via an initializer, do not provide an initial value at the @State declaration. ```None
 struct StickerPageView: View {
     @State private var page: StickerPage // no initial value expression
     let title: String
 
     init(title: String) {
         self.page = StickerPage(title: title) // works!
         self.title = title
     }
 }
``` When all stored members of a struct are private, the compiler synthesizes a private init that can be used in an extension of the same type: ```None
 struct StickerPageView: View {
     @State private var page: StickerPage
     private let title: String
     ...
 }
 
 extension StickerPageView {
     init(title: String, _ page: StickerPage) {
         self.init(page: page, title: title) // using the synthesized init
     }
 }
``` The state macro disables this synthesized initializer. So the code above no longer compiles. To mitigate, assign value to members explicitly: ```None
 extension StickerPageView {
     init(title: String, _ page: StickerPage) {
         self.title = title
         self.page = page
     }
 }
``` In rare situations, the automatic inference of generic arguments of `@State` is less flexible with the macro implementation. Write the type with more specificity. Composing `@State` with other property wrappers or macros is not supported.  (105893279)
- In apps built with the 27.0 SDKs, the new `ReadableDocument` and `WritableDocument` protocols support asynchronous reading and writing, progress reporting, and direct access to document URLs. New `DocumentGroup` initializers that adopt these protocols let you disable document creation for editing-only apps and present custom UI before any document is opened. The initializers expose an `Observable` `URLDocumentConfiguration` and integrate with Swift concurrency and the `Observation` framework. New applications should prefer `ReadableDocument` and `WritableDocument` over `ReferenceFileDocument`, which remains available.  (158441552)
- The `TabsPickerStyle` style is now available for pickers that represent tab-based navigation and content selection. This style is similar to the `.segmented` style, but VoiceOver reads it as “tabs,” and on macOS it has a distinct visual appearance that distinguishes it from pickers that represent value selection — for example, a text alignment picker in an inspector.  (173211711)
- You can now use the `TextInputBorderShape` type to customize the border shape of text input controls like `TextField` with the `textInputBorderShape(_:)` view modifier. The `.squareBorder` and `.roundedBorder` text field styles are soft deprecated — use the new `.bordered` text field style instead.  (173362083)
- In apps built with the 27.0 SDKs, a `LabeledContent` view used inside a `Menu` maps its value to the platform menu item’s subtitle.  (175594929)
- The @Entry macro now warns of potential issues if you store default class instances or closures in the environment. The SwiftUI Specialist skill in Xcode provides guidance for resolving these issues.  (175902616)
- You can now access `concentricCornerRadii` and `concentricCornerRadii(in:)` on `GeometryProxy`. These APIs return the corner radii that are concentric with the view’s container shape as a `RectangleCornerRadii?`. You can use these values to drive custom drawing or layout that responds to the container’s corners without rendering a `ConcentricRectangle` directly.  (177185166)
- You can now use the `Document` protocol for representing documents in `DocumentGroup`. This protocol combines `ReadableDocument` and `WritableDocument` for common read-and-write cases. Use `Document` instead of `ReferenceFileDocument` and `FileDocument`, which are now deprecated.  (177458781)
- `@ContentBuilder` type checking performance is further improved for valid code compared to Beta 1.  (177526032)
- The new data item or error object based `alert` and `confirmationDialog` modifiers can now be used by projects targeting iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, and visionOS 1.0.  (179388848)
- In macOS apps built with the macOS 27 SDK, the action retrieved from the `\.newDocument` environment value accepts an in-memory `ReadableDocument` produced by an autoclosure. SwiftUI presents a new document window populated with the supplied instance, instead of invoking the document group’s default factory. Use this to implement “New from Template” commands and similar flows.  (180300890)
- A new `fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)` modifier exports a collection of values that conform to `WritableDocument` whose `Writer.Destination` is `URL`. The system presents a single export dialog, writes each document to the chosen destination, and reports the resulting URLs through `onCompletion`.  (180301165)
- The `makeFileWrapper` closure of `FileWrapperDocumentWriter` now receives a second argument, `previous: FileWrapper?`, holding the `FileWrapper` from the document’s most recent read or write when one is available. Package documents can mutate `previous` in place and return it so that `FileWrapper` only writes children whose contents changed, avoiding rewriting an entire package on every save. Documents stored as a single file can ignore the second argument and return a fresh `FileWrapper` as before. Existing call sites must update their closures to accept the new parameter.  (180301399)
- `DocumentReader.Source` and `DocumentWriter.Destination` now default to `URL`. Conforming types that read from or write to a file URL no longer need to declare `typealias Source = URL` or `typealias Destination = URL`.  (180301692)

###### Resolved Issues

- Fixed: When you apply both `.fileExporter(_:...)` and `.fileMover(_:...)` modifiers to a view, some dialogs might not present correctly.  (154080867)
- Fixed: In apps built with the 27.0 SDKs, `containerRelativeFrame(_:alignment:)` incorrectly accounts for safe-area insets on a `ScrollView`’s non-scrollable axis, causing the calculated scrollable content size to be too small. For example, a view using `containerRelativeFrame(.vertical)` inside a horizontal `ScrollView` extends into vertical safe-area regions, such as the navigation bar and home indicator, because only the scrollable axis insets are applied.  (165913417)
- Fixed: Certain control-related view modifiers unexpectedly affect sheet and popover content. In apps built with the 27.0 SDKs, the `controlSize`, `buttonSizing`, `buttonRepeatBehavior`, `menuIndicatorVisibility`, and `ButtonBorderShape` environment values are now reset to their default values in sheets and popovers.  (167448274)
- Fixed: `Menu` labels cannot contain controls, views with gestures, or view representables with gesture recognizers.  (169091260)
- Fixed: `@State` variable named using a raw identifier fails to compile.  (179149051) (FB23015259)
- The `read(from:progress:)` and `write(content:to:previous:progress:)` requirements of `DocumentReader` and `DocumentWriter` are declared with `@concurrent` instead of `nonisolated`. With approachable-concurrency defaults that infer `MainActor` isolation, an unannotated `nonisolated` async method runs on the main actor, defeating the intent of off-main reading and writing. Conforming types that previously used `nonisolated` should switch to `@concurrent` to match.  (180302015)
- The `makeDocument:` and `makeReadableDocument:` closures passed to `DocumentGroup` initializers are now `@MainActor`-isolated. SwiftUI invokes these factories on the main actor when constructing a document instance, allowing the closure body to access main-actor state — including the supplied `URLDocumentConfiguration` — without hopping isolation domains.  (180302065)
- `URLDocumentConfiguration` is a `@MainActor`-isolated `@Observable` reference type and no longer conforms to `Sendable`. Code that captured a configuration in a `Sendable` closure or stored it in a `Sendable` value should drop the constraint and access the configuration on the main actor.  (180302075)

###### Deprecations

- The `FileDocument` protocol is deprecated. Use `ReadableDocument` for read-only documents or `Document` for documents that support reading and writing.  (178776840)

##### System

###### New Features

- System now provides Swift APIs for the C `stat`, `lstat`, `fstat`, and `fstatat` system calls. This includes a new `Stat` type with initializers from `FilePath`, `FileDescriptor`, or a C string; `FilePath.stat()` and `FileDescriptor.stat()` instance methods; and supporting types (`FileType`, `FileMode`, `FileFlags`, `UserID`, `GroupID`, `DeviceID`, and `Inode`). See [`SYS-0006`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0006-system-stat.md) for more details.  (160612181)

###### Resolved Issues

- Fixed: Custom `FilePath` or `FileDescriptor` extensions that make unqualified calls to `stat()` or `stat(_)` (without the `Darwin.` qualification) might conflict with the new Swift `stat()` instance methods introduced in [`SYS-0006`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0006-system-stat.md), causing build errors. See [`SYS-0008`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0008-backdeploy-cinterop-stat.md) for more details.  (177911316)

##### Testflight

###### Known Issues

- Apps installed via TestFlight may launch into a blank window with no content. The TestFlight “What to Test” introductory screen may not appear before the app, or the app’s window may render empty.  (179387790) **Workaround:** Close the blank window and relaunch the app from the Home View. The launch typically succeeds within 1–3 attempts. If an app remains stuck, force-quit it (long-press the Digital Crown) and launch again from the Home View.

##### Textkit

###### New Features

- `NSTextTable` and its related objects and types are available to UIKit clients starting with OS 27 releases.  (159870239)

##### Uikit

###### New Features

- When linked on iOS 27, tvOS 27, macCatalyst 27, or visionOS 27 SDKs, you can use `UIScene.extendStateRestoration` and `UIScene.completeStateRestoration` to extend state restoration for `UIScene.ActivationState.background` to `UIScene.ActivationState.foreground` lifecycle transitions.  (161843040)

###### Resolved Issues

- Fixed: `-[UIApplication supportedInterfaceOrientationsForWindow:]` and `-[UIApplicationDelegate application:supportedInterfaceOrientationsForWindow:]` are marked as unavailable in the visionOS SDK rather than deprecated.  (178170882)
- Fixed: Views hosted in a UIHostingController and positioned using Auto Layout might have broken layout due to an overly aggressive fix for a layout feedback loop.  (181943015)

###### Deprecations

- Apps built with the latest SDK must adopt the scene-based life cycle or they fail to launch. For migration guidance, see [`Transitioning to the UIKit scene-based life cycle`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).  (141837548)

##### Usdkit

###### Resolved Issues

- Fixed: Some types of USD attributes cannot be read or modified.  (170653056)
- Fixed: Array, vector, matrix, and quaternion types cannot be authored using USDKit.  (178071414)

###### Deprecations

- Meshes compressed using the USDKit export API or `usdcrush tool` in Beta 1 cannot be decoded by Beta 2, and  meshes from Beta 2 cannot be decoded by Beta 1.  (177417812)

##### Videotoolbox

###### New Features

- `VTLowLatencySuperResolutionScalerConfiguration` now supports a 1.5x scale factor. Call `+supportedScaleFactorsForFrameWidth:frameHeight:` to discover the scale factors available for your source dimensions.  (177635243)
- `VTLowLatencyFrameInterpolationConfiguration` now supports arbitrary source dimensions up to 1080p.  (179040806)

##### Webkit

###### Resolved Issues

- Fixed: Some models embedded in web pages might render off-center within the portal or might be hidden by portal edges.  (174193414)
- Fixed: 3D models hosted in `<model>` HTML elements might appear darker than expected when the system environment is set to Dark Mode.  (175191357)
- Fixed: The `<model>` element renders differently across iOS, macOS and visionOS, primarily as brightness/darkening differences and some color temperature and specular highlight discrepancies.  (177195829)

##### Xcode

###### Resolved Issues

- Fixed: When you use the Debug View Hierarchy tool (View Debugger) to inspect an app that presents RealityKit content with SwiftUI RealityView, the RealityKit scene appears empty: the RealityView’s entities are missing from the captured hierarchy and the RealityKit debugger shows no content. This affects apps running on visionOS, the iOS Simulator, and macOS. Debugging of non-RealityKit content (UIKit, AppKit, and 2D SwiftUI views) is unaffected. The content is still present in your app and renders correctly at runtime; only its visibility to the View Debugger is affected, due to a change in how RealityKit exposes RealityView-hosted entities to the debugging APIs the View Debugger relies on.  (177083261)


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes)*