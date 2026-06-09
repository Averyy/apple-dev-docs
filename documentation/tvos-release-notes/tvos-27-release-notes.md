# tvOS 27 Beta Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 27 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 27 beta. The SDK comes bundled with Xcode 27, available from the Mac App Store. For information on the compatibility requirements for Xcode 27, see [`Xcode 27 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-27-release-notes).

##### Apple Tv

###### Known Issues

- When launching the Apple TV app, the sidebar focus highlight might briefly appear flat on the right side.  (177389941)

##### Avkit Video Playback

###### Known Issues

- When a video is muted or unmuted during playback, subtitles may not be automatically enabled or disabled as expected. The subtitles-on-mute logic has not yet been updated to account for the new system behavior.  (177086166) **Workaround:** Manually enable or disable subtitles using the subtitle option in the player’s playback controls menu, or adjust the system-wide setting in Settings > Accessibility > Subtitles & Captioning

##### Background Assets

###### New Features

- You can reduce your app’s storage usage with localized asset packs. The system delivers the appropriately localized asset packs based on the user’s preferred languages.  (163944365)

##### Foundation

###### Resolved Issues

- Fixed: `+[NSURL URLWithString:]` no longer double-encodes the `%` of valid percent-escape sequences when encoding other invalid characters.  (161588649) (FB20439045)

##### Game Center

###### Resolved Issues

- Fixed: When you trigger the Access Point, it’s completion handler is never invoked.  (172683368)

##### Homekit

###### New Features

- When Apple Intelligence in the Home app is enabled, your HomeKit Secure Video recordings are processed on-device and through Private Cloud Compute for video descriptions and search.  (178858470)

##### Metal

###### Known Issues

- When you use a sampler to read from a texture with clamp-to-edge addressing mode, the result might be clamped to zero.  (172520325)
- On devices in the Apple 10 GPU family, using a sampler to read from a texture with clamp-to-edge addressing mode might produce results that are clamped to zero.  (177318505)

##### Network Security

###### New Features

- Starting in 27.0 operating systems, select system processes now enforce stricter network security (TLS) requirements. These new requirements might cause connections to fail if the server does not meet them. The affected processes are those involved in MDM, DDM, Automated Device Enrollment, configuration profile installation, app installation, and software updates. Servers must support TLS 1.2 at minimum, using cipher suites and certificates that meet App Transport Security (ATS) requirements. For additional details on affected processes, requirements, and how to audit and diagnose failures in managed environments please reference [`Prepare your network environment for stricter security requirements`](https://developer.apple.comhttps://support.apple.com/en-us/126655). For additional details on ATS and the new requirements please reference [`Preventing Insecure Network Connections`](https://developer.apple.comhttps://developer.apple.com/documentation/Security/preventing-insecure-network-connections) and [`NSRequiresNIAPTLSPackageVersion`](https://developer.apple.comhttps://developer.apple.com/documentation/BundleResources/Information-Property-List/NSRequiresNIAPTLSPackageVersion).  (176055825)

##### On Demand Resources

###### Deprecations

- On Demand Resources and the `NSBundleResourceRequest` API are deprecated. Use Background Assets instead.  (170066290)

##### Realitykit

###### Resolved Issues

- Fixed: When `OpacityComponent` is applied to an entity with opaque materials, `RealityRenderer` renders the opaque materials with transparency, revealing interior surfaces. Only the frontmost surface should appear with partial transparency.  (177976245)

###### Known Issues

- Some MaterialX 1.39 nodes are not supported.  (172875414)
- `ComputeGraphComponents` stored in a Reality file do not render when loaded.  (177674901)

##### Shadergraph

###### Known Issues

- The `realitykit_hair_surfaceshader` node does not support `DiffuseLightProbeGroupComponent`. Materials built with this node might not respond to diffuse light probe group lighting.  (177976666)

##### Siri

###### Known Issues

- Siri might not resolve some entity types when your app has provided only an `EntityStringQuery` for the entity type.  (177464215) **Workaround:** Index the entity in Spotlight, or provide an `IntentValueQuery` if applicable.

##### Storekit

###### New Features

- StoreKit now includes the `Transaction.OwnershipType.assigned` and `Transaction.RevocationType.assignmentRevoked` enum values to support volume purchases. `Transaction` query methods now additionally return transactions assigned to the Managed Apple Account.  (156749517)
- New `Product.ProductType` APIs represent subscription Bundles and subscription Suites. New APIs in `Product.SubscriptionInfo.BundledSubscription` let you fetch merchandising data about subscriptions contained in a Bundle. Transaction and RenewalInfo contain new fields that provide information about purchases and customer status regarding Bundles and Suites.  (160501742)
- `partnerName` and `partnerId` properties for Advanced Commerce API are available in [`Transaction.AdvancedCommerceInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct) and [`RenewalInfo.AdvancedCommerceInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct).  (167808780)

##### Storekit Testing in Xcode

###### Resolved Issues

- Fixed: The unified app receipt is not updated after forcing a subscription expiration with `SKTestSession`.  (102093015) (FB11767567)
- Fixed: The `SKTestSession` `disableDialogs` setting is not always respected for all system dialogs.  (154390284) (FB18403150)
- Fixed: Subscription upgrades performed with the Xcode Transaction Manager are not reported in `Transaction.updates`.  (160698598) (FB20269723)
- Fixed: The renewal behavior preference is not respected when using the `purchaseDate(_:renewalBehavior:)` purchase option to make purchases using `SKTestSession`.  (162014134) (FB20537538)

###### Known Issues

- When using StoreKit Testing in Xcode, `pricingTerms.commitmentInfo.price` returns an incorrect price for monthly subscriptions billed as a 12-month commitment.  (177942756)

##### Swift Charts

###### Known Issues

- When your project has a minimum deployment target lower than 27.0, using conditionals inside a `Chart` closure produces the warning “Conformance of ‘_ConditionalContent<TrueContent, FalseContent>’ to ‘ChartContent’ is only available in  27.0 or newer,” and the app might crash at runtime when that content is loaded.  (174168981) **Workaround:** Extract the conditional chart content into a separate function or computed property annotated with `@ChartContentBuilder`. For example, replace: ```None
 Chart(dataPoints, id: \.index) { dataPoint in
   if selectedMetric == "Rate" {
       LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.rate))
           .foregroundStyle(.blue)
   } else {
       LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.signal))
           .foregroundStyle(.green)
   }
 }
``` with: ```None
 Chart(dataPoints, id: \.index) { dataPoint in
   marks(for: dataPoint)
 }
 
 @ChartContentBuilder 
 private func marks(for dataPoint: DataPoint) -> some ChartContent {
   if selectedMetric == "Rate" {
       LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.rate))
           .foregroundStyle(.blue)
   } else {
       LineMark(x: .value("X", dataPoint.index), y: .value("Y", dataPoint.signal))
           .foregroundStyle(.green)
   }
 }
```

##### Swiftui

###### New Features

- `AsyncImage` now automatically caches downloaded images using HTTP caching protocols, allowing servers to control caching behavior via standard headers. You can customize caching for specific images using the new`AsyncImage` initializers that accept `URLRequest` with custom `cachePolicy` settings. Additionally, you can set a custom `URLSession` using the new `View.asyncImageURLSession(_:)` API to control how all child `AsyncImage` views perform data tasks.  (78212597)
- A `@State` declared with an expression as its initial value used to evaluate the expression each time the view struct re-instantiates. In the case of `@State private var model = Model()`, this means `Model.init()` gets called many times throughout the view’s life time. Xcode 27 introduces a new `@State` implementation that avoids this repeated evaluation. This new behavior back-deploys to iOS 17 aligned OSes. The new `@State` is implemented with a Swift macro. It is largely source compatible with the property wrapper version, with a few exceptions. If you provide an initial value at `@State` declaration, and also try to assign a value to it in an initializer, the initializer value is discarded. This behavior has not changed because of the macro, but some such cases no longer compiles: ```None
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
``` When all stored member of a struct is private, the compiler synthesizes a private init that can be used in extension of the same type: ```None
 struct StickerPageView: View {
     @State private var page: StickerPage
     private let title: String
     ...
 }
 
 extension StickerPageView {
     init(title: String, _ page: StickerPage) {
         self.init(page: page, title: title) // using the sythesized init
     }
 }
``` The state macro disables this synthesized initializer. So the code above no longer compiles. To mitigate, assign value to members explicitly: ```None
 extension StickerPageView {
     init(title: String, _ page: StickerPage) {
         self.title = title
         self.page = page
     }
 }
``` In rare situations, the automatic inference of generic argument of `@State` is less flexible with the macro implementation. Write the type with more specificity. Composing `@State` with other property wrappers or macros is not supported.  (105893279)
- The `TabsPickerStyle` style is now available for pickers that represent tab-based navigation and content selection. This style is similar to the `.segmented` style, but VoiceOver reads it as “tabs,” and on macOS it has a distinct visual appearance that distinguishes it from pickers that represent value selection — for example, a text alignment picker in an inspector.  (173211711)
- In apps built with the 27.0 SDKs, a `LabeledContent` view used inside a `Menu` maps its value to the platform menu item’s subtitle.  (175594929)

###### Resolved Issues

- Fixed: When you apply both `.fileExporter(_:...)` and `.fileMover(_:...)` modifiers to a view, some dialogs might not present correctly.  (154080867)
- Fixed: In apps built with the 27.0 SDKs, `containerRelativeFrame(_:alignment:)` incorrectly accounts for safe-area insets on a `ScrollView`’s non-scrollable axis, causing the calculated scrollable content size to be too small. For example, a view using `containerRelativeFrame(.vertical)` inside a horizontal `ScrollView` extends into vertical safe-area regions, such as the navigation bar and home indicator, because only the scrollable axis insets are applied.  (165913417)
- Fixed: In apps built with the 27.0 SDKs, the `controlSize`, `buttonSizing`, `buttonRepeatBehavior`, `menuIndicatorVisibility`, and `ButtonBorderShape` environment values are not reset to their default values in sheets and popovers.  (167448274)
- Fixed: A Button containing both an icon and a title placed inside a `List` `Section` header or footer has incorrect spacing between its icon and title.  (175681345)

###### Known Issues

- Buttons on tvOS no longer automatically use the accent color from an app’s asset catalog as a label tint color when building against the tvOS 27 SDK.  (171830912) **Workaround:** To get accent-tinted buttons, use `.tint(.accentColor)` to adopt your accent color as a button’s complete tint. `.bordered` and `.borderedProminent` use the tint in more and less subtle ways, respectively.

##### System

###### New Features

- System now provides Swift APIs for the C `stat`, `lstat`, `fstat`, and `fstatat` system calls. This includes a new `Stat` type with initializers from `FilePath`, `FileDescriptor`, or a C string; `FilePath.stat()` and `FileDescriptor.stat()` instance methods; and supporting types (`FileType`, `FileMode`, `FileFlags`, `UserID`, `GroupID`, `DeviceID`, and `Inode`). See [`SYS-0006`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0006-system-stat.md) for more details.  (160612181)

###### Known Issues

- Custom `FilePath` or `FileDescriptor` extensions that make unqualified calls to `stat()` or `stat(_:_:)` (without the `Darwin.` qualification) might conflict with the new Swift `stat()` instance methods introduced in [`SYS-0006`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0006-system-stat.md), causing build errors.   (177911316) **Workaround:** Migrate to the new Swift `stat()` methods, or disambiguate using `Darwin.stat()` and `Darwin.stat(_:_:)`. See [`SYS-0008`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0008-backdeploy-cinterop-stat.md) for more details.

##### Textkit

###### New Features

- `NSTextTable` and its related objects and types are available to UIKit clients starting with OS 27 releases.  (159870239)

##### Uikit

###### New Features

- When linked on iOS 27, tvOS 27, macCatalyst 27, or visionOS 27 SDKs, you can use `UIScene.extendStateRestoration` and `UIScene.completeStateRestoration` to extend state restoration for `UIScene.ActivationState.background` to `UIScene.ActivationState.foreground` lifecycle transitions.  (161843040)

###### Deprecations

- Apps built with the latest SDK must adopt the scene-based life cycle or they fail to launch. For migration guidance, see [`Transitioning to the UIKit scene-based life cycle`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).  (141837548)

##### Usdkit

###### Known Issues

- Some types of USD attributes cannot be read or modified.  (170653056)
- Array, vector, matrix, and quaternion types cannot be authored using USDKit.  (178071414)

##### Videotoolbox

###### New Features

- `VTLowLatencySuperResolutionScalerConfiguration` now supports a 1.5x scale factor. Call `+supportedScaleFactorsForFrameWidth:frameHeight:` to discover the scale factors available for your source dimensions.  (177635243)
- `VTLowLatencyFrameInterpolationConfiguration` now supports arbitrary source dimensions up to 1080p.  (179040806)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes)*