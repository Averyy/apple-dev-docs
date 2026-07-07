# watchOS 27 Beta 3 Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 27 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 27 beta 3. The SDK comes bundled with Xcode 27, available from the Mac App Store. For information on the compatibility requirements for Xcode 27, see [`Xcode 27 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-27-release-notes).

##### Av Conference Telephony

###### Known Issues

- Outgoing FaceTime Audio calls from Apple Watches set up for family members to iOS devices running beta releases (27.0) might fail. Incoming FaceTime calls and cellular calls work correctly, as do calls to devices running iOS 26.0 or later.  (178187431)

##### Cellular

###### Known Issues

- Cellular Incoming and Outgoing calls may fail on Verizon network if the user upgrade from previous WatchOS release to Watch OS 27.0 Beta 2 or performs an erase/clean install of WatchOS 27.0 Beta 2. Text-to-911 may also fail on Verizon network.  (180062521) **Workaround:** If performing erase install, users are encouraged to install Watch OS 27.0 Beta 1 before upgrading to Beta 2.

##### Complications

###### Known Issues

- Some complications might be missing in the Watch app’s Face Gallery.  (177840928)

##### Foundation

###### Resolved Issues

- Fixed: `+[NSURL URLWithString:]` no longer double-encodes the `%` of valid percent-escape sequences when encoding other invalid characters.  (161588649) (FB20439045)

##### Foundation Models

###### Resolved Issues

- Fixed: Truncating transcript history in the `onPrompt` modifier might cause an unexpected runtime error.  (177901494)
- Fixed: `onPrompt` might not be called when applied to a `Profile` without instructions.   (177902488)
- Fixed: Using `@Generable` on an `enum` fails to compile for watchOS.  (178244470)
- Fixed: Passing an `any LanguageModel` to the `model(_:)` modifier will lead to a compiler error.  (178545978)

###### Known Issues

- Private Cloud Compute might not work when you use simulators.   (177684296) **Workaround:** Use a physical device running OS 27.0.
- `PrivateCloudComputeLanguageModel` always uses greedy decoding.  (178181782) **Workaround:** Specify `samplingMode` in `GenerationOptions` with a custom seed, e.g. `GenerationOptions(samplingMode: .randomThreshold(0.95, seed: 42))`.
- Foundation Models framework cannot be imported when building for watchOS in Xcode 27 beta 2.  (179949809)

##### Health

###### Resolved Issues

- When a third-party heart rate monitor is active, Apple Watch pauses background heart rate measurements and heart rate notifications (irregular rhythm, high heart rate, and low heart rate) for the duration of the session.  (162788761)

##### Healthkit

###### New Features

- HealthKit now supports heart rate and cycling power zones.  (135746152)

##### Network Security

###### New Features

- Starting in 27.0 operating systems, select system processes now enforce stricter network security (TLS) requirements. These new requirements might cause connections to fail if the server does not meet them. The affected processes are those involved in MDM, DDM, Automated Device Enrollment, configuration profile installation, app installation, and software updates. Servers must support TLS 1.2 at minimum, using cipher suites and certificates that meet App Transport Security (ATS) requirements. For additional details on affected processes, requirements, and how to audit and diagnose failures in managed environments please reference [`Prepare your network environment for stricter security requirements`](https://developer.apple.comhttps://support.apple.com/en-us/126655). For additional details on ATS and the new requirements please reference [`Preventing Insecure Network Connections`](https://developer.apple.comhttps://developer.apple.com/documentation/Security/preventing-insecure-network-connections) and [`NSRequiresNIAPTLSPackageVersion`](https://developer.apple.comhttps://developer.apple.com/documentation/BundleResources/Information-Property-List/NSRequiresNIAPTLSPackageVersion).  (176055825)

##### Siri

###### Known Issues

- Siri might not resolve some entity types when your app has provided only an `EntityStringQuery` for the entity type.  (177464215) **Workaround:** Index the entity in Spotlight, or provide an `IntentValueQuery` if applicable.

##### Sleep Focus

###### Known Issues

- Sleep Focus may not automatically toggle on/off after a reboot or update until the user unlocks the device.  (179960164) **Workaround:** Toggle Sleep Focus manually in Control Center after unlocking the device.

##### Smart Stack

###### Known Issues

- Tapping the Now Playing “Suggestions” widget in Smart Stack does not start playback.  (178464737) **Workaround:** Play media from the Now Playing app instead.

##### Status Bar

###### Known Issues

- When Apple Watch is in the Always On state,the time in the status bar may not update.  (178633015)

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
- Fixed: Re-purchasing a previously refunded non-consumable fails with an already owned error when using StoreKit Testing in Xcode.  (174560379) (FB22475017)
- Fixed: Using `pricingTerms.commitmentInfo.price` in StoreKit Testing in Xcode returns an incorrect price for monthly subscriptions with a 12-month commitment.  (177942756)
- Fixed: Transactions for upgraded subscriptions are immediately marked as expired when using StoreKit Testing in Xcode.  (178441109)
- Fixed: Purchases made with the original StoreKit API fail with an unknown error on watchOS.  (178760994)

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
- You can now use the `TextInputBorderShape` type to customize the border shape of text input controls like `TextField` with the `textInputBorderShape(_:)` view modifier. The `.squareBorder` and `.roundedBorder` text field styles are soft deprecated — use the new `.bordered` text field style instead.  (173362083)
- In apps built with the 27.0 SDKs, a `LabeledContent` view used inside a `Menu` maps its value to the platform menu item’s subtitle.  (175594929)
- The @Entry macro now warns of potential issues if you store default class instances or closures in the environment. The SwiftUI Specialist skill in Xcode provides guidance for resolving these issues.  (175902616)
- You can now access `concentricCornerRadii` and `concentricCornerRadii(in:)` on `GeometryProxy`. These APIs return the corner radii that are concentric with the view’s container shape as a `RectangleCornerRadii?`. You can use these values to drive custom drawing or layout that responds to the container’s corners without rendering a `ConcentricRectangle` directly.  (177185166)
- `@ContentBuilder` type checking performance is further improved for valid code compared to Beta 1.  (177526032)
- The new data item or error object based `alert` and `confirmationDialog` modifiers can now be used by projects targetting iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, and visionOS 1.0.  (179388848)

###### Resolved Issues

- Fixed: When you apply both `.fileExporter(_:...)` and `.fileMover(_:...)` modifiers to a view, some dialogs might not present correctly.  (154080867)
- Fixed: In apps built with the watchOS 27.0 SDK, `TabView.selection` updates only after the user has scrolled or rotated the Digital Crown past the 50% threshold between two pages, rather than as soon as the offset begins to change.  (163517317)
- Fixed: In apps built with the 27.0 SDKs, `containerRelativeFrame(_:alignment:)` incorrectly accounts for safe-area insets on a `ScrollView`’s non-scrollable axis, causing the calculated scrollable content size to be too small. For example, a view using `containerRelativeFrame(.vertical)` inside a horizontal `ScrollView` extends into vertical safe-area regions, such as the navigation bar and home indicator, because only the scrollable axis insets are applied.  (165913417)
- Fixed: Certain control-related view modifiers unexpectedly affect sheet and popover content. In apps built with the 27.0 SDKs, the `controlSize`, `buttonSizing`, `buttonRepeatBehavior`, `menuIndicatorVisibility`, and `ButtonBorderShape` environment values are now reset to their default values in sheets and popovers.  (167448274)
- Fixed: A Button containing both an icon and a title placed inside a `List` `Section` header or footer has incorrect spacing between its icon and title.  (175681345)
- Fixed: `@State` variable named using a raw identifier fails to compile.  (179149051) (FB23015259)

##### System

###### New Features

- System now provides Swift APIs for the C `stat`, `lstat`, `fstat`, and `fstatat` system calls. This includes a new `Stat` type with initializers from `FilePath`, `FileDescriptor`, or a C string; `FilePath.stat()` and `FileDescriptor.stat()` instance methods; and supporting types (`FileType`, `FileMode`, `FileFlags`, `UserID`, `GroupID`, `DeviceID`, and `Inode`). See [`SYS-0006`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0006-system-stat.md) for more details.  (160612181)

###### Resolved Issues

- Fixed: Custom `FilePath` or `FileDescriptor` extensions that make unqualified calls to `stat()` or `stat(_)` (without the `Darwin.` qualification) might conflict with the new Swift `stat()` instance methods introduced in [`SYS-0006`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0006-system-stat.md), causing build errors. See [`SYS-0008`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0008-backdeploy-cinterop-stat.md) for more details.  (177911316)

##### Textkit

###### New Features

- `NSTextTable` and its related objects and types are available to UIKit clients starting with OS 27 releases.  (159870239)

##### Watch Connectivity

###### Resolved Issues

- Fixed: The `WCSession.transferCurrentComplicationUserInfo` method does not work with complications built using WidgetKit on watchOS.  (113202790) (FB12819178)

##### Watchkit

###### Deprecations

- `WKExtension` and `WKExtensionDelegate`  are deprecated for apps with a minimum deployment target of watchOS 9.2 or later  (70031637)

##### Workout Playback

###### Known Issues

- Mirrored Playback might not start on iPhone when started on Apple Watch.   (176497682) **Workaround:** Open Podcasts on iPhone and tap Play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes)*