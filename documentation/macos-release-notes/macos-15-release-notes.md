# macOS Sequoia 15 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 15 SDK provides support to develop apps for Mac computers running Sequoia 15. The SDK comes bundled with Xcode 16, available from the Mac App Store. For information on the compatibility requirements for Xcode 16, see [`Xcode 16 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16-release-notes).

##### Accessibility

###### Resolved Issues

- Fixed: User might be unable to play newly added background sounds (Fire and Night).  (128898875)

##### Accessorysetupkit

###### Resolved Issues

- Fixed: Resolved an issue where iPhone and iPad apps on Apple Silicon Macs quit unexpectedly if AccessorySetupKit is linked.  (99817447)

##### Adattributionkit

###### Resolved Issues

- Fixed: Resolved an issue where iPhone and iPad apps on Apple Silicon Macs quit unexpectedly if AdAttributionKit is linked.  (121731262)

##### App Intents

###### Resolved Issues

- Fixed: EntityURLRepresentation allows arbitrary custom URLs without validation.   (119524801)
- Fixed: Resolved an issue where iPhone and iPad apps on Apple Silicon Macs quit unexpectedly when SiriTipUIView is referenced.  (128038651)
- Fixed: Parameterless `@Parameter` and `@Property` wrappers might cause protocol conformance failures.  (130219933)

###### Known Issues

- `@UnionValue` types currently only work as intent results. Attempting to use a `@UnionValue` as the type of an intent parameter or entity property results in failure to compile.  (128069844)

##### App Store

###### New Features

- Starting in macOS 15, the App Store no longer needs twice the space free for an initial app download and install. The free space requirement will now be the final install size of the app, plus a small buffer. Developers should consider this change in any messaging they might have around size requirements.  (123838124)

##### Appkit

###### New Features

- Added API to request a window share when the user performs some action in the app. Presenter who starts a presentation while on a video conferencing call can now be given an option to share that presentation with other call participants. This addresses an issue where the presenter might not want to share all application windows, and might not have an affordance to start sharing the presentation once it has begun. The API allows one NSWindow to request sharing of another existing window, or of a window to be provided in a callback. ```None
 public func requestSharingOfWindow(_ window: NSWindow) async throws
 
 public func requestSharingOfWindow(usingPreview image: NSImage, title: String) async throws
``` (115318870)

###### Resolved Issues

- Fixed: AppKit’s “warn once” logs have been moved to os_log_error() with a “WarnOnce” logging category, in order to increase their visibility to developers.  (75992959)

##### Application Firewall

###### Deprecations

- Application Firewall settings are no longer contained in a property list. If your app or workflow relies on changing Application Firewall settings by modifying /Library/Preferences/com.apple.alf.plist, then you need to make changes to use the socketfilterfw command line tool instead.  (124405935)

##### Arkit

###### Resolved Issues

- Fixed: iPhone and iPad apps on Apple Silicon Macs quit unexpectedly when initializing `ARSkeletonDefinition`.  (128038936)

##### Automation

###### New Features

- To improve security, the process of allowing an application to control Finder has changed. Instead of a modal “Allow/Don’t Allow” dialog, the attempt to control Finder fails, and a notification appears that directs the user to allow control in System Settings > Security & Privacy > Automation.  (129086419)

##### Backup

###### Resolved Issues

- Fixed: Attempting to create a new encrypted Time Machine backup on a Time Capsule or other AFP file server will fail.  (129082348)

##### Camera

###### Resolved Issues

- Fixed: Using presenter overlay in full-size mode with a single shared window and reactions at the same time can result in glitching.  (128586125)

##### Cfnetwork

###### Resolved Issues

- Fixed: `CFNetworkExecuteProxyAutoConfigurationScript` and `CFNetworkExecuteProxyAutoConfigurationURL` have always returned a +1 retained CF type object, but the function declarations were not decorated with the `CF_RETURNS_RETAINED` attribute until iOS 18, macOS 15, tvOS 18, and visionOS 2. For C-based languages, the clang static analyzer might note if the object is leaked. No source code changes are required, but they are encouraged to fix the leak. For Swift, this changes the return type of these functions from `Unmanaged<>` to the actual CF type returned, which will require a source change to fix when compiling with newer SDKs. However, Swift programs compiled with older SDKs will continue to work on the new OSes, though the returned CF type object will continue to leak as it did prior to this change.  (126154509)

##### Contactprovider

###### Resolved Issues

- Fixed: Resolved an issue where iPhone and iPad apps on Apple Silicon Macs quit unexpectedly if ContactProvider is linked.  (124717115)

##### Core Location

###### Resolved Issues

- Fixed: Resolved an issue where iPhone and iPad apps on Apple Silicon Macs quit unexpectedly when invoking -[CLLocationManager startMonitoringLocationPushesWithCompletion:].  (128038918)

##### Core Ml

###### Resolved Issues

- Fixed: Core ML Model Deployment API is unavailable (`MLModelCollection` and `MLModelCollectionEntry`). Consider using Background Assets or `NSURLSession` instead.  (122955353)
- Fixed: Inference time for large Core ML models is slower than expected on a subset of M-series SOCs (e.g. M1, M1 max) on macOS.  (129682801)

##### Core Motion

###### Resolved Issues

- Fixed: Resolved an issue where iPhone and iPad apps on Apple Silicon Macs quit unexpectedly when invoking +[CMAltimeter isAbsoluteAltitudeAvailable].  (128038968)

##### Core Spotlight

###### Resolved Issues

- Fixed: iPhone and iPad apps on Apple Silicon Macs quit unexpectedly when invoking `-[CSSearchableItemAttributeSet setActionIdentifiers:]`.  (128039095)

##### Create Ml

###### Known Issues

- 3D object views in Create ML might stop rendering correctly, causing occasional flickering or appearing fully blacked out. This will not negatively impact training.  (132026726)  To view object and object dimensions in viewport again, restart Create ML.

##### Directoryservice

###### Deprecations

- DirectoryService plug-in support has been removed. Developers should migrate to Platform SSO.  (119515880)

##### Finder

###### Resolved Issues

- Fixed: Home Videos unexpectedly sync as Music Videos to iPod nano (7th generation).  (94899119)

##### Foundation

###### New Features

- JSONEncoder.OutputFormatting.sortedKeys will now sort keys with a different ordering. Previously, keys were sorted using a numeric, case-insensitive, or localized ordering. Beginning in beta 4, keys are sorted lexicographically based on the keys’ UTF-8 contents.  (126874437)

###### Resolved Issues

- Fixed: [`Date.ComponentsFormatStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/date/componentsformatstyle) was incorrectly producing strings like `"1m"` with the `Date.ComponentsFormatStyle.Style.condensedAbbreviated` style and strings like `"1min"` with the `.narrow` style instead of the other way around. The behavior was corrected to match the behavior of [`Duration.UnitsFormatStyle.UnitWidth`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct).  (125790342)

##### Fskit

###### Resolved Issues

- Fixed: Users with connected MSDOS volumes might receive an intermittent error on system startup saying the internal MSDOS partition cannot be repaired and needs to be reformatted.  (130011123)

##### Headphone Accommodations

###### Resolved Issues

- Fixed: Headphone Accommodations won’t be applied to headphones.  (128964879)

##### Icloud Drive

###### Resolved Issues

- Fixed: Frequently changed files syncing over iCloud Drive will use more data than expected.  (128771010)

##### Iphone Mirroring

###### Resolved Issues

- Fixed: Universal Clipboard might not to work during iPhone Mirroring.  (128165996)
- Fixed: Scrolling with a scroll wheel with Logitech mice or typing with a Bluetooth keyboard might not work with iPhone Mirroring.  (129403645)
- Fixed: The space bar does not work when Full Keyboard Access is enabled.  (130535985)

###### Known Issues

- If you have a device using iOS 18.0 beta 3 and one using macOS 15.0 beta 4, clicking a notification on your iPhone might result in timeout of a new iPhone Mirroring connection or interruption of an existing connection.  (131780502)  Update both iPhone and Mac to beta 4 or higher.

##### Logging

###### New Features

- By default, the `sudo` command in macOS does not have logging enabled. To enable logging for `sudo`, simply remove the line `Defaults  !log_allowed` from `sudoers` configuration file.  (126771963)

##### Mac Catalyst

###### New Features

- When building against the macOS 15.0 Catalyst SDK or newer, UIWindowScene systemFrame changes using UIWindowScene.GeometryPreferences.Mac can be animated by wrapping the request in the existing UIView animation API ( animate(withDuration duration:…) ). Mixing such systemFrame animations with animations of individual UIViews is not recommended - instead, rely on autolayout constraints to reposition scene contents during the systemFrame animation.  (121456766)

###### Resolved Issues

- Fixed: Starting with macOS 15.0, the activationState of all attached UIScenes in Mac Catalyst apps will now also be changed to UIScene.ActivationState.background when the machine and/or the attached displays go to sleep, as an indication that the scenes are not producing user-visible pixels.  (104518600)
- Fixed: When building against the macOS 15.0 Catalyst SDK or newer, the TrueValue and FalseValue for toggle switch elements (PSToggleSwitchSpecifier) in your Settings Bundle will be respected, when reading/writing User Defaults.  (118947907) (FB13425114)

##### Maps

###### New Features

- Introduced Place ID, a unique and persistent identifier.  (129071038)
- Added new resultTypes to MKLocalSearch.Request and additional PointofInterestCategory values.  (129073725)
- Introduced Place Card API to show Maps Place Card UI.  (129073922)

###### Resolved Issues

- Fixed: The Place Card API fails to load place details.  (128231815)
- Fixed: In searches that use MKLocalSearch.Request, the result type option physicalFeature is ignored.  (128961972)
- Fixed: Satellite map images might not appear for users on Intel Macs.  (130466174)

###### Known Issues

- Conversion between a point in the map view and a physical location (CLLocationCoordinate2D) might be imprecise at high zoom levels.  (129042241)

##### Marketplacekit

###### Resolved Issues

- Fixed: Resolved an issue where iPhone and iPad apps on Apple Silicon Mac and Apple Vision Pro quit unexpectedly if MarketplaceKit is linked.  (132598608)

##### Music

###### Resolved Issues

- Fixed: Artwork for the currently playing song might be incorrectly displayed in the Music window.  (128688400)

##### Networking

###### Resolved Issues

- Fixed: For apps linked on macOS 15 / iOS 18 or newer, the default User-Agent request header field value generated by URLSession now includes the unlocalized bundle name instead of the localized bundle name.  (117380285)

##### Notifications

###### Resolved Issues

- Fixed: User might be unable to snooze Calendar notifications.  (128564243)

##### Nstoolbar

###### New Features

- The new `-removeItemWithItemIdentifier:` method allows removing an item with the specified `itemIdentifier`. Note that all items matching the specified identifier will be removed when using this method (i.e. specifying `NSToolbarFlexibleSpaceItemIdentifier` will remove all flexible space items). To remove only a single space item, use `-removeItemAtIndex:` instead.  (2823286)
- The `NSToolbar.allowsDisplayModeCustomization` property allows a toolbar to enable display mode customization independently of item customization. Some users have an easier time finding items when they are labeled so it’s important to support them with the choice of display modes. This property is enabled by default for apps linked on macOS 15.0 or later, otherwise it follows the value of `allowsUserCustomization`. Make sure to verify all your items provide labels using the `NSToolbarItem.label` property to support Icon and Text mode. Note that Text Only mode is omitted automatically when one or more items don’t provide sufficient `menuFormRepresentations`.  (2858103)
- `NSToolbarItem` gains a new `hidden` property. A hidden item will not be visible in the toolbar, but will be visible during user customization so that users can specify where the item should appear when it is shown. For apps that support multiple windows with synchronized toolbars (NSToolbars with shared identifiers), use the `hidden` property to display a particular item in one window but not another. Note that there is an important difference between an `enabled` item and a `hidden` item. Typically on macOS, a user interface element that does not currently apply will be disabled but remains visible (main menu items, context menu items, toolbar items). The introduction of this new `hidden` property does not indicate that toolbar items should be hidden when they don’t apply. An item should only be hidden in very special circumstances such as the Downloads button in Safari which only shows when there are downloads present, or the Displays popup button in Screen Sharing which is only visible when viewing a remote machine with multiple displays.  (114109109)
- When responding to an `NSToolbarWillAddItemNotification` the `userInfoDictionary` now contains a value specifying the item’s new index which can be accessed via the `NSToolbarNewIndexKey`. This value is only available on macOS 15.0 or later.  (114661283)
- The new `itemIdentifiers` property allows for easy access to an identifier-only representation of items in the toolbar which is useful when implementing `NSToolbarDelegate` methods such as `-toolbar:itemIdentifier:canBeInsertedAtIndex:`. Assigning a new array of itemIdentifiers will replace all items in the toolbar with the new configuration by doing the minimal amount of insert/remove operations necessary. This property is also key value observable. Note, set new values to this property with caution when the toolbar is customizable. The user might find it disruptive to have their curated items moved or removed unexpectedly. The new value will also replace any saved customization defaults.  (115908180)

###### Deprecations

- The `-setConfigurationFromDictionary:` and `-configurationDictionary` methods are now deprecated. The same values might be obtained from the `itemIdentifiers`, `displayMode`, and `visible` properties.  (31540854)
- The `NSToolbarItem.allowsDuplicatesInToolbar` property is now deprecated. The only items that are allowed to have shared identifiers are system space items. On apps linked against macOS 15.0 or later, an exception will be thrown if a new item is added to the toolbar when an item with that identifier already exists (excluding space items).  (115908214)

##### Object Tracker

###### Resolved Issues

- Fixed: Training Object Tracker reference objects might fail without warning for unsupported USDZ inputs.  (129721127)

##### Photos

###### Resolved Issues

- Fixed: Photos and videos might stop syncing via iCloud Photo Library.  (128325085)

##### Platform

###### New Features

- On Apple Silicon based devices with M3 or later, and A16 Bionic or later, the values returned by reading the CNTFRQ_EL0 and CNTVCT_EL0 registers have been updated to 1 GHz, instead of the prior value of 24 MHz. It is still recommended for apps to use libsystem APIs like `mach_absolute_time()` for timekeeping. Your app will not be impacted by this change if it uses Apple’s timekeeping APIs. For compatibility purposes, this change will only be visible when using the SDK associated with this release or later. On macOS, applications running inside a Virtualization.framework VM will continue to receive the legacy behavior.  (84639494)
- The firmware image for iBoot will be made available in cleartext in the PCC image. To reduce the overhead imposed by firmware encryption and align policies where appropriate, firmware encryption has been disabled for iBoot on iOS, macOS, watchOS, tvOS, and visionOS. See [`Private Cloud Compute`](https://developer.apple.comhttps://security.apple.com/blog/private-cloud-compute/) for more details.  (125171074)

##### Power

###### Resolved Issues

- Fixed: Users with default wallpaper (macOS Beta) on Intel laptops with an AMD GPU might see elevated battery drain, device temperatures, and fan noise.  (128623427)

##### Quick Look

###### Deprecations

- Support for deprecated Quick Look Generator plugins is being removed. To provide previews and thumbnails for your custom file types, migrate to Quick Look Preview Extension and Thumbnail Extension API.  (116791365)

##### Realitykit

###### New Features

- USD files which use Catmull-Clark subdivision now render using subdivision in RealityKit. Meshes which produce less than 35,000 patches can render using subdivision. This can increase memory consumption and reduce rendering performance.  (129016034)
- Virtual objects now render using the Display P3 color gamut. When using a `DrawableQueue` connected to a `TextureResource` with the `.color` semantic, render using the Display P3 color space.  (129017592)

###### Resolved Issues

- Fixed: Resolved an issue where iPhone and iPad apps on Apple Silicon Macs quit unexpectedly when using ObjectCaptureSession.  (117112309)
- In iOS & iPadOS 17, macOS 14, visionOS 1 and earlier, UnlitMaterials’ blending modes inconsistently respond to `.blending`, `.color`, and `.baseColor` setters. In applications building against RealityKit from iOS & iPadOS 18, macOS 15, or visionOS 2, alpha-blending enablement should be configured explicitly with `.blending = .transparent(opacity:)`. Developers are advised to check that their code-configured materials are alpha-blending as intended, and use the `.blending` setting where appropriate.  (118210191)
- In iOS & iPadOS 17, macOS 14, visionOS 1 and earlier, transparent materials’ apparent final opacities respond inconsistently to `.blending`, `.color`, and `.baseColor` setters. In applications building against RealityKit from iOS & iPadOS 18, macOS 15, or visionOS 2, the final opacity of transparent materials is computed as a multiplication of its `.color` or `.baseColor`’s alpha and `.blending = .transparent(opacity:)`. Developers are advised to check that their code-configured transparent materials render with the intended final opacities, and update their usages of `.color`, `.baseColor` and/or `.blending = .transparent(opacity:)` when necessary.  (125431647)
- Fixed: Using an `Image 2D Array` Shader Graph node in Reality Composer Pro might result in corruption or a system crash.  (127122590)
- Fixed: Reality files written by beta versions of RealityKit might not load in later versions.  (128424173)
- Fixed: Physics simulation behavior is different from previous releases.  (128435086)
- Fixed: Emphasize actions are always additive and should be played with `separateAnimatedValue` set to `true`.  (128622689)
- Fixed: In the Swift 6 language mode, subclasses of the `Entity` class fail to compile.  (128787131)
- Fixed: The `.trigger` mode of CollisionComponent no longer generates CollisionEvents when both involved collision shapes use the `.trigger` mode.  (129016567)

###### Deprecations

- In previous versions, the order of child entities was sometimes preserved. Now, the order of an `Entity`’s children might not be reliable and can change unexpectedly when any child is reparented.  (129015381)

##### Screen Time

###### Resolved Issues

- Fixed: When an Apple Watch is upgraded to 11.0 from an earlier Beta, Screen Time App Limits might be deleted for both the parent and child. If this occurs, parent will need to add back the app limits.  (130981807)

##### Screencapturekit

###### New Features

- Windows recorded using the new SCRecordingOutputConfiguration API will now have a new “Stop Recording This Window” menu item in the purple window menu to stop the window’s recording stream.  (125112908)

###### Deprecations

- Applications utilizing deprecated APIs for content capture such as `CGDisplayStream` & `CGWindowListCreateImage` can trigger system alerts indicating they might be able to collect detailed information about the user. Developers need to migrate to `ScreenCaptureKit` and `SCContentSharingPicker`.  (120910350)

##### Security Privacy

###### New Features

- When attempting to change home directory of a user, dscl and dsimport will trigger privacy prompts. Previously this did not happen when a device was under MDM management.  (121868524)

##### Setup Assistant

###### Resolved Issues

- Fixed: FileVault pane is shown and is automatically enabled with recovery key when iCloud is signed in.  (128770548)
- Fixed: End of Setup Assistant might only show a blurred background with no text or buttons.  (128771559)

##### Shortcuts

###### Resolved Issues

- Fixed: The Shortcuts editor might offer some new actions that are not yet ready for use. If you save a shortcut with one of these actions, you might need to correct it after a future update with the corrected actions.  (128841105)
- Fixed: Some actions are missing from the Actions Drawer, but are still available for use.  (128908702)

##### Storekit

###### New Features

- macOS now supports in-app [`Offer Code`](https://developer.apple.com﻿https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes/) redemption. Use [`StoreKit Testing in Xcode`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode/) to ensure your app responds correctly when customers redeem a Mac App Store Offer Code.  (60096251)
- The [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) now supports custom control styles. To create a custom control style, declare a type that conforms to [`SubscriptionStoreControlStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle) and implement `makeBody(configuration:)` method.  (106819454)
- New standard styles are available for laying out subscription store view controls with a compact height. Use `pagedPicker` and `pagedProminentPicker` for a platform appropriate paging effect, or `compactPicker` to place options in a horizontal stack. For watchOS, the new `pagedPicker` style is available for laying out [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) controls with a compact height.  (110286601)
- Use types such as `SubscriptionOptionGroup` and `SubscriptionPeriodGroupSet` to declare a hierarchical structure for your [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview). You can use the `subscriptionStoreOptionGroupStyle(_:)` to choose between presenting groups as a tab view or as navigation links.  (110429924) (FB12264937)
- The subscription status [`RenewalInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/status/3822294-renewalinfo) object now supports new properties `renewalPrice` and `currency` to indicate the price at which the subscription will renew, and its currency. There is also a new `offer` property containing the information of the offer that will be applied to the next renewal, if there is any. This includes the offer ID, the offer type, and the payment mode.  (114217892)
- Finished consumables can now be included when using the [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction) APIs. Users can enable this feature by setting `SKInAppPurchaseHistoryIncludesConsumables` to true in app’s Info.plist.  (115079880)
- When configuring the control style for a [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview), users can specify a placement for the controls using the `subscriptionStoreControlStyle(_:placement:)` view modifier. For tvOS, by default [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) will place the controls trailing the marketing content.  (115319543)
- When building an app with Xcode 16, [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) instances using the picker control style have an updated appearance. Use `subscriptionStorePickerItemBackground(_:in:)` to configure a different background color and shape for the picker items.  (120558960)
- Users can now use APIs like monthly or yearly to get common [`Product.SubscriptionPeriod`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptionperiod) values when comparing subscription periods.  (122684230)

###### Resolved Issues

- Fixed an issue where StoreKit APIs could unexpectedly fail with a system error.  (111689346) (FB12509606)
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

##### Swiftui

###### New Features

- `TabView`s declared at the root of a `Scene` use a new style that hosts the tabs in the toolbar of the `Scene`. To achieve the prior behavior, apply a `.tabViewStyle(.grouped)` modifier: ```swift
 TabView { ... }.tabViewStyle(.grouped)
``` (61410733)
- Pickers now can have keyboard shortcuts attached to their individual options, by attaching the `keyboardShortcut()` modifier to the individual views in the picker content.  (67682762) (FB8522629)
- macOS clients can now get the macOS seamless scrolling appearance (like the Mail app) with `Form` and `ScrollView`. The seamless appearance was already available with `List`. `Form` gets a seamless appearance by default, opt out with `.scrollContentBackground(.hidden)`. `ScrollView` is opt-in with `.scrollContentBackground(.visible)`. See the docs of `scrollContentBackground` more.  (115563289)
- Added the ability to request sharing of a newly opened window. A presenter who starts a presentation while on a video conferencing call can now be given an option to share that presentation with other call participants. This addresses an issue where the presenter might not want to share all application windows, and might not have an affordance to start sharing the presentation once it has begun. This is supported by a new ‘sharingBehavior’ argument to the ‘openWindow’ callable.  If the `sharingBehavior` is `requested`, the window is opened and then shared if possible.  If the `sharingBehavior` is `required`, the window is opened only if the sharing request succeeds.    (115806658)
- For `ObservableObject` subclasses used with `@EnvironmentObject`, `@ObservedObject`, and `@StateObject`, SwiftUI will now only call `objectWillChange` once per property per object instance. If you use `@Published` and the default `ObservableObjectPublisher`, you do not need to change anything. If you override `objectWillChange`, ensure the lifetime of the publisher you return matches the lifetime of its enclosing `ObservableObject`.  (116197689)
- SwiftUI sheets presented with the `.sheet` modifier now use `.automatic` sizing by default. `.automatic` resolves to `.form` or `.form.fitted(horizontal:false, vertical: true)` depending on the platform (see the symbol’s documentation for more). Platforms prior to iOS 18 and aligned releases used different, non-customizable default sheet sizing. iOS 17 and earlier used what is now called `.page` presentation sizing. macOS 14 and earlier used what is now called `.fitted` sizing. visionOS 1 used `.fitted` sizing. When linking apps against iOS 18 and aligned SDKs, audit your sheet presentations and pick the sizing best for you. Apply a `.presentationSizing` modifier to sheet contents: ```swift
 ContentView().sheet(isPresented: $present) {
   SheetView().presentationSizing(.form)
 }
``` (117551515)
- Types conforming to the View protocol, and other similar SwiftUI protocols, are now isolated to the `@MainActor` by default. SwiftUI’s runtime behavior with respect to actor isolation has not changed: SwiftUI views and similar types have always been evaluated on the main actor at runtime; this change improves compile-time diagnostics for potential data-race safety issues. To opt out of the new default main actor isolation and restore the previous default isolation, add the nonisolated keyword to methods and properties as needed, or move the protocol conformance to an extension to opt out the entire type.  (120815051)
- [`Text(_:format:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(_:format:)) now automatically injects `FormatStyle` known to SwiftUI with the `TimeZone` and `Calendar` from the environment.  (123662780)
- `@Entry` macro can now be used to simplify declarations of custom `EnvironmentValues`, `FocusedValues`, `Transaction`, and `ContainerValues` properties.  (125568810)
- Added the ability to give a gesture a name, which gets surfaced to UIGestureRecognizers when establishing dependencies.  (126527559)

###### Resolved Issues

- Fixed: `List` on macOS 15 does not use `NSTableView` for showing non-outline content anymore.  (77273697)
- Fixed: The [`.tint`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/tint(_:)-23xyq) view modifier can be used to customize the color of a `TextField` and `TextEditor` text insertion indicator and selection highlight on macOS, in addition to iOS and iPadOS.  (85523172) (FB9766312)
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
- Fixed: The `scenePhase` environment property and `onAppear`/`onDisappear` callbacks behave in a more predictable manner when using the `Window` and `WindowGroup` scene types.  (94004478)
- Fixed: Toolbar items with the principal placement will now be centered within the column they are applied to, when applied to a child of a `NavigationSplitView`.  (96895871)
- Fixed: Drag now supports file promises. Dragged items can be successfully dropped on a Finder window.  (98710028) (FB11275037)
- Fixed: Sliders now adapt appropriately when the environment’s `layoutDirection` is `.rightToLeft`.  (99664719)
- Fixed: The `scenePhase` environment property and `onAppear`/`onDisappear` callbacks now behave in a more predictable manner when using the window style for menu bar extras.  (103575895)
- Fixed an issue where searchable suggestions automatically filter out completion options that have a `searchCompletion` matching the current search text. Exact matches should be explicitly elided from the suggestions if desired.  (107706241)
- Fixed: `View._printChanges` now outputs key path of mutated observable properties instead of “@dependencies”.  (111392797)
- Fixed: Using the `scrollClipDisabled()` view modifier with a `ScrollView` with a `LazyHStack` or `LazyVStack` will use the containing window to determine what content the lazy stack should render.  (111796138)
- Fixed: macOS applications that previously linked with macOS 14 or older SDK had `.swipeActions` applied in reversed order for the trailing edge. For macOS 15 this behavior is fixed to align with `.swipeActions` on iOS (no longer reversed). This means the  placement of buttons will follow the order in SwiftUI view construction, starting from the originating edge of swipe actions.  (112891121) (FB12753741)
- Fixed: SwiftUI will now assert that types conforming to the `App` protocol are value types.  (113634782)
- Fixed: When compiled with macOS 15 SDK, `safeAreaInset` applied on `Table` will now be used as the insets on the content view instead of the insets on `Table ` itself. This aligns with how `List` behaves with `safeAreaInset` modifier attached.  (114998212)
- Fixed: In macOS, a Toggle of the `.switch` style now animates when its `isOn` state is changed programatically, matching the existing behavior on iOS and iPadOS. The animation can be disabled in all platforms by setting the transaction’s `disablesAnimations` property when updating a Toggle’s state.  (115071023)
- Fixed: Automatically updating `Text` created via [`Text(_:style:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(_:style:)) or [`Text(timerInterval:pauseTime:countsDown:showsHours:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:)) was causing increased battery drain when used in long running Live Activities. They now no longer animate changes in digits that signal the seconds value, keeping the power impact to a minimum.  (115906895)
- Fixed: SwiftUI no longer overrides a nil `scrollTargetAnchor` when using the `scrollPosition(id:anchor:)` modifier with a nil anchor. Specify a `topLeading` anchor to restore the previous behavior.  (116124988)
- Fixed: Writing `.toolbar(.hidden, for: .windowToolbar)` will result in different behaviors depending if the application was linked with macOS 15 SDK. On prior SDKs, `.toolbar(.hidden, for: .windowToolbar)` will hide the toolbar items. On new SDKs, the same writing will hide the entire toolbar including the window controls, the title, the toolbar items, and the toolbar background. To hide only toolbar items again, please write `.toolbar(.hidden, for: .automatic)`.  (116618483)
- Fixed: App scenePhase now reports as active when at least one scene is active.  (117864591)
- Fixed: Scroll views can now accept interaction in their content insets.  (117928468)
- Fixed: `.navigationDestination(for:destination)` modifiers inside of lazy containers are no longer evaluated. `.navigationDestination(isPresented:destination:)` and `navigationDestination(item:destination)` will log warning when used in lazy containers. Lazy containers in this context include: `List`, `LazyVGrid`, `LazyHGrid`, `LazyHStack`, `LazyVStack` `Table`, and `TabView`. If using `navigationDestination`s in lazy containers, users will see logged errors at runtime. Lift the modifiers higher up in the view hierarchy so they are outside of the lazy containers. Allowing navigation destination modifiers in lazy containers had two significant costs: (1) app navigation state could be undefined if a navigationDestination had been scrolled off screen (2) The navigation system had to explore all list contents to ensure navigation destinations remained up to date. Only allowing these modifiers outside of lazy containers improves app navigation reliability and performance.  (117998693)
- Fixed: When linked against the macOS 15 SDK, `NSHostingView` will no longer eagerly size its associated window immediately upon being added to it.  (118586136)
- Fixed: Views at the root of a `NavigationStack` will now always have matching `onAppear` and `onDisappear` callbacks.  (119737698)
- Fixed: The order of `ShapeStyle` compositing modifiers is now honored with respect to shadows. Previously in `fill(style.blendMode(…).shadow(…))` the added blend mode would also apply to the shadow, that is no longer the case. The blend mode modifier must be added after the shadow modifier to affect it. As a consequence, the fill and any shadows added can now use different blend modes. Similar rules apply to `ShapeStyle.opacity()` except that outer `opacity()` modifiers multiply with inner modifiers, e.g. in `fill(style.opacity(0.5).shadow(…).opacity(0.5))` the shadow is drawn with 50% opacity (of whatever `style` draws) and `style` itself draws with 25% opacity.  (119738072)
- Fixed: The meaning of the boolean value passed to the `ContentTransition.numericText(countsDown:)` function has been flipped for apps deployed prior to iOS 18 aligned releases.  (120561508)
- Fixed: Gestures might not pick up a modified content shape, such as when increasing the tappable area of a button.  (120938385)
- Fixed an issue when a `sheet` modifier is removed from a view hierarchy. This can happen if the `sheet` modifier is in one branch of an `if` statement and the statement’s condition changes. For apps linked on or after iOS 18 and aligned releases, when a `sheet` modifier is completely removed from the hierarchy, the binding associated with the sheet will not be reset.  (123742063)
- Fixed: `ForEach` child views are no longer re-evaluated unconditionally, only when a parameter of the `ForEach` view might have changed.  (123902210)
- Fixed: Scroll views have improved behavior in right to left languages when the size of their content is smaller than the size of their container.  (124008045)
- Fixed: Elements along a `NavigationPath` or the data structure passed to the `path` parameter of `NavigationStack(path:root:)` are now compared more efficiently. Any side-effects from setting a `path` equal to itself are no longer reliable and likely will not occur.  (125093883)
- Fixed: `SceneBuilder`, `WidgetBundleBuilder`, `TableColumnBuilder`, `TableRowBuilder`, `CommandsBuilder`, and `ToolbarContentBuilder` now diagnose unsupported `if #available` conditions at compile time instead of crashing at run time.  (125379937)
- Fixed: `UIViewRepresentable`, `NSViewRepresentable` and their view controller variants no longer create a layer with `allowsGroupOpacity` set to true.  (125561916)
- Fixed: In TabViews in the Mac idiom of Mac Catalyst, section actions in the sidebar sometimes do not appear.  (125876373)
- Fixed: In certain scenarios, [`Text(_:style:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(_:style:)) produced suboptimal output, such as choosing an unnecessarily small calendar unit, showing zero values for large calendar units instead of omitting them, or showing seconds in Always On Display.  (125885307)
- Fixed: [`Text(timerInterval:pauseTime:countsDown:showsHours:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:)) was redacting the seconds value even when the timer was paused, had not started yet, or had already reached its end.  (125885429)
- Fixed: When applying a `searchable()` modifier to a `TabView`, the tab view will reset the search state when switching tabs.  (125926765)
- Fixed: [`Swipe actions`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/swipeactions(edge:allowsfullswipe:content:)) with icon-only labels now appear as expected on macOS. (Note: For improved accessibility, provide a text label even if it won’t be displayed. Use the [`.labelStyle(.iconOnly)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/labelstyle/icononly) view modifier to visually hide the label’s text.)  (125939243)
- Fixed: Resolved an issue where scroll views would not receive touches if placed near a tappable control. When rebuilt with the newer SDK, make sure that small buttons and tap targets are correctly enlarged. You can use the `contentShape` modifier.  (126232279)
- Fixed: Navigation constructions that relied on a List selection binding driving transient navigation state might behave differently. Prior to macOS 15.0, this was undefined behavior. For applications linked on and after macOS 15.0, this is still undefined behavior and should not be relied upon. This is also undefined behavior on all other platforms. ```swift
 struct ContentView: View {
     @State private var selection: Set<Int> = [5]
     var body: some View {
         NavigationSplitView {
             List(selection: $selection) {
                 ForEach(1...6, id: \.self) { num in
                     NavigationLink("\(num)", value: num)
                 }
             }
             .navigationDestination(for: Int.self) { number in
                 // The List selection binding above should not be used
                 // to drive this navigationDestination modifier
                 Text("\(number)")
             }
         } detail: {
             ContentUnavailableView("Make a selection", systemImage: "dice")
         }
     }
 }
``` (127626852)
- Fixed: The lifecycle of windows for apps using the SwiftUI App Lifecycle has been adjusted to better match platform conventions.  (127697378)
- Fixed: Some NavigationLinks in the deprecated `NavigationView` might not work.  (128358023)
- Fixed: `NavigationSplitView` on macOS fails to clear the path when selection changes in a subsequent column.  (128548564)
- Fixed: Sheets presented with the `.sheet` modifier will have `FittedPresentationSizing` by default. This can cause sheets to appear too narrow or too large, depending on their contents. This is incorrect. The default presentation sizing should be `.form`.  (128902804)
- Fixed: Deprecated `NavigationLinks` links with an `isActive` argument that are wrapped with a get/set `Binding` derived from another `Binding` might not update the destination view if the derived binding updates too late.  (129018685)
- Fixed: In the Swift 6 language mode, the `@Entry` macro now works with non-`Sendable` types if the type of the entry is declared explicitly.  (129073803)
- Fixed: Changes to a view’s `pointerStyle(_:)` value, such as in response to modifier key presses or other state changes, might not be reflected on screen until the mouse is moved.  (129740140) (FB13878258)
- Fixed an issue where the pointer did not update when it exited a view with the `.pointerStyle(_:)` modifier.  (129741260) (FB13878385)

###### Known Issues

- On macOS views presented on a stack with `navigationDestination(for:destination)` might fail to update contents.  (110118681)  Use a different style of navigation link to present the view that must update like `.navigationDestination(isPresented:destination)` or `NavigationLink(_:destination)`.
- SwiftUI Animations in AppKit - `NSAnimationContext.animate(using:change:completion:)` might not work for some keypaths and might not merge correctly.  (129178630)

##### System Integrity Protection

###### New Features

- To protect users’ privacy, app group containers (in `~/Library/Group Containers`) are now protected by System Integrity Protection. This is similar to the protection added to app data containers in macOS Sonoma. An app that’s properly entitled for an app group continues to have access to the app group container. Specifically, the app must use [`FileManager`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/filemanager/1412643-containerurl) to get the app group container path and meet one of the following requirements: the app is deployed through Mac App Store; the app group identifier is prefixed with the app’s Team ID; or the app group identifier is authorised by a provisioning profile embedded within the app. If the app doesn’t meet these requirements, the system might present the user a prompt to authorize the app’s use of the app group container. If granted, that consent applies only for the duration of that app instance. This restriction also applies to app extensions, although in that case the system won’t prompt the user for consent but will instead just deny the access.  (114586798)

###### Resolved Issues

- Fixed: Users might be incorrectly prompted when an app attempts to access an application group container that is authorized by an embedded provisioning profile.  (129667695) (FB13860644)

###### Known Issues

- Users might be incorrectly prompted to approve access to other app’s data when an app that is distributed through TestFlight attempts to access its own application group container. The incorrect prompt might happen even if the app would otherwise not prompt in local development or when distributed on Mac App Store.  (132449491)

##### Translation

###### New Features

- Users can translate text and display results in app. See the `TranslationSession` class, and learn more in the WWDC24 video “Meet the Translation API.”  (112844581)
- Translation now supports translating Hindi in the Translate app, System-wide translation, Safari translation, and the new Translation APIs.  (116622913)

##### Uikit

###### Resolved Issues

- Fixed: Resolved an issue where iPhone and iPad apps on Apple Silicon Macs quit unexpectedly when invoking `-[UIInputViewController hasFullAccess]`.  (128039254)

##### Video Subscriber Account

###### Resolved Issues

- Fixed: iPhone and iPad apps on Apple Silicon Macs quit unexpectedly if `VSOpenTVProviderSettingsURLString` is referenced.  (113562872)

##### Video Toolbox

###### Resolved Issues

- Fixed: On Apple Silicon, AVC (H.264) content at level 5.2 or lower can be handled by the hardware decoder. Content that otherwise conforms to level 5.2 but is high frame rate (e.g. 4k at 100 or 120 fps) and labelled level 6, 6.1 or 6.2 is also handled by hardware. However, if width or height is greater than 4096 columns or rows and content uses 4:2:0 chroma subsampling and 8 bit depth, the hardware decoder driver will reject it and a software decoder will be automatically selected to ensure artifact-free decoding. Now, if content is 10 bit, 4:2:2 or 4:4:4, the hardware decoder will be used.  (127003443)

##### Virtualization

###### Resolved Issues

- Fixed: Users will not be able to sign-in to iCloud and related applications.  (128924562)
- Fixed: Rosetta: Intel binaries fail to run in a Virtual Machine on Apple Silicon Macs.  (131773319)

###### Known Issues

- Installing the latest beta of macOS in a virtual machine on a host Mac running macOS Sonoma might fail.  (109234128)  Install the latest beta of Xcode prior to installing the latest beta of macOS.
- Users will not be able to use Mail App on macOS VMs.  (127248244)

##### Voiceover

###### Resolved Issues

- Fixed: Users might not be able to complete some stages of Setup Assistant.  (127445421)

##### Wallet

###### Resolved Issues

- Fixed: Disbursement requests on Mac cannot be handed off to an Apple Watch.  (123278621)
- Fixed: Disbursement requests on Mac might appear as regular payments requests when handed off to iPhone.  (124172945)

##### Widgetkit

###### Resolved Issues

- Fixed: WidgetKit Simulator is not available.  (126989860)

##### Workoutkit

###### Resolved Issues

- Fixed: Resolved an issue where iPhone and iPad apps on Apple Silicon Macs quit unexpectedly if WorkoutKit is linked.  (108256454)

## See Also

- [macOS Sequoia 15.6 Release Notes](macos-15_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.5 Release Notes](macos-15_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.4 Release Notes](macos-15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.3 Release Notes](macos-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.2 Release Notes](macos-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.1 Release Notes](macos-15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-15-release-notes)*