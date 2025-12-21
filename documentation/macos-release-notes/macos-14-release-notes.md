# macOS Sonoma 14 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 14 SDK provides support to develop apps for Mac computers running Sonoma 14. The SDK comes bundled with Xcode 15 RC, available from the Mac App Store. For information on the compatibility requirements for Xcode 15 RC, see [`Xcode 15 RC Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15-release-notes).

##### General

###### Resolved Issues

- Fixed: Users might experience a blank screen with an active cursor for an indefinite period of time when attempting to update to Sonoma Beta 6.  (114166127)

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

- Fixed: VoiceOver might not speak inline predictive text in some text fields.  (109225941)
- Fixed: VoiceOver users might not be able to move focus to enter Recovery mode. Instead users will hear “Accessibility Visuals Agent has no windows.”  (109588439)

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

##### Appkit

###### New Features

- See [`AppKit Release Notes for macOS Sonoma 14`](appkit-release-notes-for-macos-14.md).  (110084217)

##### Ats and Atsui

###### Deprecations

- Starting macOS 14 Sonoma, whenever the OS detects the usage of ATS or ATSUI APIs, the user will be presented a dialog stating that the application needs to be updated. Once the dialog is dismissed by the user, the application will exit.  (100521621)

##### Authentication Services and Passkeys

###### New Features

- The Credential Provider API for password managers has been expanded to support passkeys. Credential providers can save and offer passkeys for apps and websites across the system.  (83501802) (FB9651656)
- `ASSettingsHelper` allows password manager apps to directly open the Settings view where the Credential Provider Extension for system-wide Password AutoFill and passkey sign-in can be enabled. `ASSettingsHelper` also allows verification code (TOTP) apps to directly open the Settings view where you can configure which app opens verification code setup links.  (106351958) (FB12039478)

##### Camera and Avfoundation Capture

###### Resolved Issues

- Fixed: On iPhone 14 and 14 Plus models third-party camera applications might fail to capture images, and the built-in Camera app and third-party applications using the new Deferred Processing API might fail to process final images.  (113158045)

##### Continuity Camera

###### Resolved Issues

- Fixed: In Control Center’s Video Effects Menu, clicking on the zoom button should reset the zoom level to the default value. If you’re using a Continuity Camera device with only one camera, or the Apple Studio Display camera, it does not reset.  (109541385)

##### Control Center Video Preview

###### Resolved Issues

- Fixed: Zoom slider in Control Center video preview might be missing for apps when Center Stage is OFF.  (110818198)

##### Createml

###### Known Issues

- Create ML may crash or hang on launch on devices with macos 14.0 beta 7.  (113703568)  Use macos 14 beta 6 or earlier

##### Documentation

###### Resolved Issues

- Fixed: Xcode crashes on macOS Sonoma Beta 1 and Beta 2 when scrolling documentation in Quick Help, the documentation window, and the Swift Package dependency manager.  (109810157)

##### Facetime Handoff

###### Resolved Issues

- Fixed: Facetime handoff to another device might result in call drop or no media.  (110126569)

##### Facetime on Apple Tv

###### Resolved Issues

- Fixed: When an Apple TV calls a Mac, a non-human readable string might appear in the calling notification.  (110021693)

##### File System

###### New Features

- The implementations of the `exfat` and `msdos` file systems on macOS have changed; these file systems are now provided by services running in user-space instead of by kernel extensions. If the application has explicit checks or support for either the `exfat` or `msdos` file systems, validate the applications with those file systems and report any issues.  (110421802)

##### Find My

###### Resolved Issues

- Fixed: The Find My application on macOS might quit unexpectedly while enabling Lost Mode on a device.  (109379261)

##### Foundation

###### New Features

- Introduced `TermOfAddress` which describes how a person should be addressed in language. This can be used in conjunction with Automatic Grammar Agreement to refer to people in a string using their preferred pronouns and grammatical agreement in English, Spanish, Portuguese, French, Italian, and German.  (99745330)
- Foundation now supports grammatical agreement with a detached phrase using the `agreeWithConcept` markdown attribute.  (102595293)

##### Freeform

###### Resolved Issues

- Fixed: Strokes drawn using Beta 2 might appear distorted when viewed on devices running Beta 1.   (107901155)
- Fixed: The Follow Me feature will only work when collaborators are on the same Beta version.  (110656281)

##### Icloud

###### Resolved Issues

- Fixed: Users with iCloud Drive sync disabled are unable to access settings for some apps using iCloud.  (105284675)
- Fixed: The System Settings application might become unresponsive after creating a new account and then signing out of iCloud.  (109789130)
- Fixed: Non-local files in iCloud Drive might fail to download and open after using Migration Assistant to set up a new volume.  (109798846)

##### Icloud Drive

###### Resolved Issues

- Fixed: iCloudDrive folders owned by root or other local users might be inaccessible after upgrade to Sonoma.   (109204311)
- Fixed: Enabling desktop and documents sync might fail after upgrade to Sonoma.   (109507087)
- Fixed: Finder or Apps might hang when accessing App created folder with .folder extension.  (112600553)

##### Icloud Settings

###### Resolved Issues

- Fixed: Users might not be able to view Apps Syncing to Drive in iCloud Drive Settings.  (110732437)

##### Imovie Theater Icloud Drive

###### Known Issues

- “Copy to File” to iCloud Drive destination might not work as expected.  (113644592)

##### Installation

###### Resolved Issues

- Fixed: Updates to macOS 14 beta will freeze if installing to a HFS formatted volume on intel machines.  (112165783)

##### Iphone Widgets on Mac

###### New Features

- iPhone Widgets on Mac might appear duplicated if switching between more than one supported iPhone as source.  (108567555)
- iPhone Widgets on Mac might not be removed when disabling iPhone Widgets On Mac in System Settings.  (109236950)
- iPhone Widgets on Mac might not populate on the Edit Widgets add sheet until after a reboot post sign in.  (109479534)
- iPhone Widgets on Mac might not be removed when signing out of iCloud.  (109527436)
- iPhone Widgets on Mac might not update upon wake from sleep. They will update at the next cadence when the Mac and iPhone are nearby and awake.  (109691143)
- iPhone widgets on Mac allow XL widgets from iPhone to be available. If assets are not available on the iPhone, the assets will be missing.  (109782417)
- iPhone Widgets on Mac that contain drop down sortable lists in their configurations might fail to configure.  (109976067)
- iPhone Widgets on Mac might not update upon wake from sleep. They will update at the next cadence when the Mac and iPhone are nearby and awake.  (109978135)
- iPhone Widgets on Mac might not be removed when disabling iPhone Widgets On Mac in System Settings.  (110804620)
- Widget App icons might appear blank in the Add Sheet if Mac is updated from Beta 2 to Beta 3 before iPhone is updated.   (111334099)
- iPhone widgets on Mac might not be available if 2 users are signed into the same Mac at the same time.   (111336466)

###### Resolved Issues

- Fixed: iPhone Widgets on Mac might lead to additional power draw on iPhone if a Mac signed into the same iCloud account is present.  (110074764)

##### Localization

###### Resolved Issues

- Fixed: Some content might appear in English. Some strings might appear clipped.  (109393568)

##### Lockdown Mode

###### Resolved Issues

- Fixed: When erasing a Mac that has Lockdown Mode turned on, the Lockdown Mode state might inadvertently persist in NVRAM.  (109470608)

##### Login Window

###### Resolved Issues

- Fixed: Users will be missing or duplicated when the multi-user layout is shown.  (108899565)
- Fixed: When using a smart card, the multi-user layout can be accessed.  (109425371)
- Fixed: The password field might not show the PIN placeholder text when using a smart card.  (109428156)
- Fixed: The “Your password is required to enabled Touch ID” message might be shown when smart card is in use.  (109429083)

##### Mac App Store

###### Resolved Issues

- Fixed: Users are unable to create new Apple IDs in the Mac App Store.   (108293571)

##### Mac Catalyst

###### Resolved Issues

- Fixed: * - SwiftUI `ToolbarContent` in Catalyst apps Optimized for Mac was previously bridged into the Mac toolbar (`NSToolbar`) dependent on whether the view containing the toolbar content filled the entire scene (width and height matched within a small floating point margin). In macOS 14.0 and later, toolbar content is now bridged into the Mac toolbar if the heights approximately match . In practice this might change a Catalyst app that had two `NavigationStack`s side by side with toolbar content. Prior to macOS 14.0, neither stack would have its toolbar content bridged into the Mac toolbar and all toolbar content would be in the toolbar of the `NavigationStack`s themselves. On and after macOS 14.0, the leading stack will have its toolbar content bridged, while the trailing stack’s content will stay in the stack’s toolbar.  (108519092)

##### Maps

###### Resolved Issues

- Fixed: When a `LinearGradient` stroke is used with a `MapPolyline` in SwiftUI, the specified gradient color might be ignored.  (106152300)
- Fixed: When using `Map`, Xcode emits a runtime warning that “Publishing changes from within view updates is not allowed.”  (106174743)
- Fixed: At certain zoom levels, the title of a selected `MKMarkerAnnotationView` can overlap other marker titles.  (109491779)
- Fixed: For non-Catalyst SwiftUI apps, some Maps controls like the legal link and compass appear outside the safe area.  (109611122)

##### Media

###### Resolved Issues

- Fixed muting capture in all other tabs when Safari starts camera and/or microphone capture in a tab.  (109896538)
- Fixed: MP3 files with malformed ID3 tags will fail to play  (110230071)

##### Messages

###### Resolved Issues

- Fixed: The transcription for long audio messages is truncated without a way to expand and view the full transcription.  (107174385)
- Fixed: Unexpected visual artifacts might appear when the transcription is inserted while sending an audio message.  (109799338)

###### Known Issues

- The Catch up affordance might display incorrectly.  (109468262)  Leave and return to the affected conversation.

##### Metal Ray Tracing

###### Resolved Issues

- Fixed: The methods `assume_curve_control_point_count`, `assume_curve_basis`, and `assume_curve_type` on `intersection_params` and `intersector`, the methods `get_curve_control_point_count`, `get_curve_basis`, and `get_curve_type` on `intersection_params`, and the related `curve_basis` and `curve_type` enumerations, are not supported in the Metal Shading Language.  (104142182)
- Fixed: After initializing an `intersection_query` with an acceleration structure using `max_levels<Count>` where `Count > 2`, calls to `next()` might cause the GPU to restart.  (108863335)
- Fixed: Reflection returned via the new `{Render|Compute|Tile}PipelineWithDescriptor` API for ray tracing pipelines might be incorrect.  (109850134)

##### Networking

###### New Features

- `URLSession` supports resumable uploads in HTTP. Just like download tasks, upload tasks can now be paused and resumed if the server supports the latest protocol draft. To learn more, see [`Resumable Uploads for HTTP`](https://developer.apple.comhttps://www.ietf.org/archive/id/draft-ietf-httpbis-resumable-upload-01.txt).  (68890505)
- Apple devices now support connection to 802.1X networks using EAP-TLS with TLS 1.3 (EAP-TLS 1.3). EAP-TLS 1.3 further improves security and privacy by always providing forward secrecy, never disclosing the peer identity, and by mandating use of revocation checking when compared to EAP-TLS with earlier versions of TLS.  (74526852)

###### Resolved Issues

- Fixed: For apps linked on or after iOS 17 and aligned OS versions, App Transport Security now requires secure connections to external IP addresses by default. For more information on these requirements, see [`Preventing Insecure Network Connections`](https://developer.apple.comhttps://developer.apple.com/documentation/security/preventing_insecure_network_connections). Exceptions can be made using [`NSExceptionDomains`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nsapptransportsecurity/nsexceptiondomains), which now supports exceptions for individual IP addresses and ranges specified in classless inter-domain routing (CIDR) notation.  (101967030)
- Fixed: For apps linked on or after iOS 17 beta, macOS 14 beta, watchOS 10 beta, and tvOS 17 beta, the `Transfer-Encoding` header field of a streamed `HTTP/1` request is set to `chunked` instead of `Chunked`.  (107390029)

##### Photos

###### New Features

- A new `PHContentEditingOutput.renderedContentURL(for:)` API adds support for `UTType.heic` encoded rendered image content.  (109861295)

###### Known Issues

- Applications providing image content via `PHContentEditingOutput.renderedContentURL` in formats other than `UTType.jpeg` will fail with an `.invalidResource` error.  (110068158)

##### Pre Filled Titles for Events and Reminders

###### New Features

- Messages now supports machine learning based pre-filled titles for English events and reminders. Tap or long-press the highlighted date/time in an SMS or iMessage conversation and select ‘Create Event’ to trigger this feature.  (110889506)

##### Presenter Overlay

###### Resolved Issues

- Fixed: Moving small Presenter Overlay while a Keynote presentation is played in fullscreen mode temporarily stops the presentation from being shared.  (110033699)

##### Printing

###### Deprecations

- macOS has removed the functionality for converting PostScript and EPS files to PDF format. As a result, CoreGraphics’ CGPSConverter returns an error when invoked, ImageIO no longer converts EPS files, NSEPSImageRep does not display EPS files, and PMPrinterPrintWithFile does not accept a PostScript file for non-PostScript print queues.  (110019863)

##### Reactions

###### Resolved Issues

- Fixed: Reactions aren’t currently available when using video conferencing apps in Safari.  (109789920)

##### Rosetta

###### Resolved Issues

- Fixed: Intel applications might quit unexpectedly on launch under Rosetta.  (110021755)

##### Safari

###### Resolved Issues

- Fixed: Safari might offer search suggestions while in Private Browsing by using an on-device model. The search terms are not sent from the device to a search provider.  (105606453)

##### Screen Sharing

###### New Features

- A High Performance connection requires a network that supports at least 75Mbps for one 4K virtual display and at least 150Mbps for two 4K virtual displays. Low network latency is also required for responsiveness.  (110068856)

###### Resolved Issues

- Fixed: When the viewer window in Screen Sharing.app is made full screen with Dynamic Resolution enabled in a High Performance connection, the video content might not resize to fill the window.  (109683500)
- Fixed: During screen sharing sessions using the new High Performance mode, the display connected to the server Mac might not be blank. Activity in the screen sharing session will be visible on the server Mac’s display during and after the session ends.  (109837767)
- Fixed: The video and cursor might lag during a High Performance connection with two 4K virtual displays to an M1 or M1 Pro server  (110342712)

##### Screen Time Settings

###### Resolved Issues

- Fixed: Selecting a family member in Screen Time causes an error to occur in iCloud accounts with Family Sharing enabled and a family member that is under 18.  (110736804)

##### Screensharing

###### Deprecations

- Use of legacy CGDisplayStream APIs to capture screen content will result in additional consent alerts.  (110529324)

##### Shazamkit

###### Resolved Issues

- Fixed: `SHManagedSession.State` is unavailable.  (109670750)
- Fixed: `SHLibrary.default.items` is unavailable.  (109670918)

##### Storekit

###### New Features

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
- Fixed: New StoreKitTest APIs are now available when testing on macOS: [`setSimulatedError(_:forAPI:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/4196369-setsimulatederror), [`simulatedError(forAPI:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/4196370-simulatederror), and [`buyProduct(identifier:options:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/4196368-buyproduct)  (110547347)
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
- Fixed: If major alignment is specified for scroll behavior, scrolling charts always align to the major unit and skip minor units.  (107644532)
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
- Fixed in beta 7: Apps using SwiftData that are built with Xcode 15 beta 6 have known issues when running on macOS Sonoma 14 beta 6.  (113971288)

###### Known Issues

- SwiftData models with implicitly unwrapped optional properties will generate a compiler error that all stored properties were not set.  (114140139)  Set the value of non-relationship stored properties in the initializer, and mark relationship properties as optional.

##### Swiftui

###### New Features

- Adds `.accessoryBar` and `.accessoryBarAction` button styles on macOS for buttons used in the context of an accessory toolbar (sometimes referred to as a “scope bar”). Buttons of the `.accessoryBar` style typically narrow the focus of a search or other operation. Buttons of the `.accessoryBarAction` style perform extra actions releative to the accessory toolbar’s main functions, like adding or editing filters. Both styles affect other view types that you can apply a button style to, like `Toggle`, `Picker`, and `Menu`, in addition to `Button`.  (44351471)
- Bordered buttons on macOS now support flexibly large heights for larger label sizes. If the label has no preferred size or a small size, the button will be the standard macOS button height. However, if the button label has a larger minimum size, the button will also now grow larger instead of clipping the label.  (56652012) (FB7411612)
- Adds new view modifiers to customize alerts and other dialogs within a view. - Use `dialogIcon(_:)` to customize the icon. In macOS, this icon replaces the default icon of the app. This modifier has no effect in other platforms.
- Use `dialogSeverity(_:)` to set the severity of confirmation dialogs and alerts, which can help indicate that extra care should be taken when choosing a particular action in the dialog.
- Use `dialogSuppressionToggle` to enable user supression of dialogs and alerts in macOS.  (62920817)
- `RoundedRectangle` now defaults to the continuous corner style.  (63246947)
- `.onChange` has new overloads where the closure takes 0 or 2 arguments, these new versions will call the new version of the closure (i.e. after the specified value has changed), so any captured properties will have up to date values. The previous overload (which calls the old version of the closure) has been deprecated.  (67344857)
- Spring animations will now default to being critically damped (i.e. a bounce of 0).  (75149732)
- Scenes in Catalyst now support the `windowResizability` modifier.  (84203422)
- Added support for `dialogSeverity` in Catalyst applications.  (95918809)
- Use the `springLoadingBehavior(_:)` view modifier to control spring loading behavior of views. Some views, like `TabView`, default to allowing spring loading, while others, like `Button`, do not. Spring loading refers to a view being activated during a drag and drop interaction. On iOS this can occur when pausing briefly on top of a view with dragged content. On macOS this can occur with similar brief pauses or on pressure-sensitive systems by “force clicking” during the drag.  (96569875) (FB10572945)
- `List`s using the `SidebarListStyle` hosted in primary column of a UIKit `UISplitNavigationController` were previously rendering with an `insetGrouped` appearance.  With this change they will render as the expected `sidebar` appearance similar to if the `List` were hosted in a SwiftUI `NavigationSplitView`.  (96909195)
- The `toolbar` and `navigationTitle` modifiers now work outside of the SwiftUI App Lifecycle on macOS. Use `NSHostingView.sceneBridgingOptions` to enable or disable this functionality.  (101092365)
- The `SceneStorage` dynamic property now works when using an `NSHostingView`, provided the view and its window have been configured for state restoration via AppKit. See `NSUserInterfaceItemIdentification` and `NSWindowRestoration` for more information regarding state restoration in AppKit.  (101097013)
- `DismissAction` can now be used to programmatically close an `NSWindow` when its `contentView` is an `NSHostingView`.  (101097410)
- `ProgressView` labels can be hidden with the `labelsHidden` view modifier.  (101517619)
- The `badge` view modifier now works on views within a menu in macOS. Use a badge to convey optional, supplementary information about a menu item.  (102025014)
- Use the `buttonRepeatBehavior(_:)` view modifier to make buttons repeatedly trigger their actions on prolonged interactions.  Apply this to buttons that increment or decrement a value or perform some other inherently iterative operation. Interactions such as pressing-and-holding on the button, holding the button’s keyboard shortcut, and holding down the space key while the button is focused trigger this repeat behavior.  (102156410)
- `Animation.default` now uses a spring animation equivalent to `Animation.spring`. In addition, `Animation.default` is now only equal to itself when using `==`, allowing users to differentiate between animations that were intentionally chosen and those that use the `default` animation.  (103169056)
- During gesture change callbacks, velocity will automatically be tracked so that it can be applied to animations that finish when the gesture finishes.  (103371523)
- `View.focusable()` now opts in to keyboard focus whether or not keyboard navigation is enabled in System Settings. For the previous behavior, pass `.activate` for the modifier’s `interactions` argument.  (104616966)
- When two Text are vertically adjacent (for example in a VStack with no spacer in between) SwiftUI will automatically calculate appropriate spacing. To opt-out if this behavior either place a Spacer or specify spacing parameter to the container view.  (104782785)
- For apps built using the macOS 14 SDK, using `DismissAction` to close a window will default to using `DismissBehavior.interactive`.  (105406945)
- When an `NSHostingView` is the `contentView` of an `NSWindow`, its `sceneBridgingOptions` property will default to `.all`, unless otherwise specified.  (106216343)
- When using `@Environment(\.self)` to capture an entire `EnvironmentValues`, SwiftUI will now track which properties are accessed to only invalidate the property when those properties change.  (106310433)
- Use the new `navigationDestination(item:destination:)` overload to present a navigation destination when a bound item is non-`nil`, or to dismiss the destination when the bound item becomes `nil` again.  (106319528)
- The sidebar toggle toolbar item in `NavigationSplitView` was moved from over the detail column to over the sidebar column for apps linked on Ventura or later. If the new position is amenable, ensure that items previously in the sidebar column are not inadvertently hidden due to limited space. Either move these items into the detail/content column view builder, or set a minimum width on the sidebar column that allows these items to show with `navigationSplitViewColumnWidth(min:ideal:)`. If the prior behavior is desired, remove the toggle button with `toolbar(removing: .sidebarToggle)` and place your own sidebar toggle toolbar item. Note that `SidebarCommands()` is orthogonal to the button. ```swift
 struct ContentView: View {
     @State private var visibility = NavigationSplitViewVisibility.all
 
     var body: some View {
         NavigationSplitView(columnVisibility: $visibility) {
             Color.red
                 .toolbar(removing: .sidebarToggle)
         } detail: {
             Color.blue
                 .toolbar {
                     ToolbarItem(placement: .navigation) {
                         Button {
                             withAnimation {
                                 visibility = visibility == .all ? .detailOnly : .all
                             }
                         } label: {
                             Label("Toggle Sidebar", systemImage: "sidebar.leading")
                         }
                     }
                 }
         }
     }
 }
``` (107148514)
- Shapes now default to mirroring when in a right to left layout direction.   (107405880)
- Changing from one Gradient value to another will now animate, but only once apps are rebuilt against the new SDK.  (107408691)
- All `Section`s inside `List` and `Table` can be configured to be collapsible using new initializers on Section. Previously all `Section`s inside `List`s using the `SidebarListStyle` received outline disclosure indicators in every header.  Section headers will no longer render this control by default.  An outline disclosure will only be provided in the header if the `Section` is initialized with an `isExpanded` binding to a bool.  This bool represents the `isExpanded` state of the `Section`.  Sections created with an `isExpanded` binding inside a `Table` on macOS will now provide a default outline disclosure indicator to collapse or expand the `Section`.  (107592493)
- The `listSectionSpacing` modifier can now be used within Lists.  (109271050)
- `View.onKeyPress(_:action:)` can’t filter key presses when bridged controls have focus.  (109799056)
- Scenes in Catalyst now support the `defaultSize` modifier.  (110038374)

###### Resolved Issues

- Fixed:`Menu` could not be used with `hoverEffect`.  (67879883) (FB8554520)
- Fixed an issue where dynamically enabled buttons (e.g. with a `TextField`) were not updated in alerts.  (95917673) (FB10463211)
- Fixed: `menuStyle(.button)` is compatible with custom button style implementations. Applying a custom `buttonStyle` on a `Menu` is supported.  (96156722)
- Fixed: `DatePicker` on macOS now maintains a fixed ideal size instead of filling the width of its container.  (98798881)
- Fixed: Scroll environment properties like isScrollEnabled and scrollDismissesKeyboardMode are no longer propagated past nested scroll views.  (99195890)
- Fixed: Previously it was possible for views animating their removal via a transition to be drawn above a view with the same zIndex that has not yet been removed. This was unintentional and has now been updated: views transitioning out of the view hierarchy are always drawn below non-removed views with the same zIndex.  (101085960)
- Fixed: Table row identifiers in `ForEach` are now derived from their `ForEach` identifier rather than the `TableRow` identifier within the `ForEach`. In this example, from within a `Table`: ```None
 ForEach(myData) { data in
     TableRow(data.someFieldAlsoOfTypeData)
 }
``` the resulting identifiers used by SwiftUI are now `data.id` rather than `data.someFieldAlsoOfTypeData.id`. If user needs to restore prior behavior, specify the ID explicitly using the `id` of the `ForEach`.  (101174261)
- Fixed: Table supports triggering primaryAction of contextMenu with return key.  (101194950)
- Fixed: LazyVGrid or LazyHGrid has an improved layout when used with fixedSize().  (103075945)
- Fixed: `List` and `Table` on macOS now have visible separators by default, unless unspecified or unless alternating row backgrounds are enabled. Separators can be explicitly hidden using the existing `listRowSeparator(.hidden)` modifier on the rows views.  (103687472)
- Fixed: `fileImporter` and `fileMover` view modifiers now require calling `URL.startAccessingSecurityScopedResource()` before accessing the provided URL, and `URL.stopAccessingSecurityScopedResource()`  when user no longer needs access to a file or directory pointed to by a security-scoped URL.  (104448864)
- Fixed: The new `.navigationDestination(item:content:)` modifier now works correctly both inside a `NavigationStack` and outside a stack but inside a column of a `NavigationSplitView`. Inside a stack, setting the bound item to a non-nil value will push a view onto the stack immediate above the view containing the modifier. Setting the bound item to a nil value will pop the view. Outside a stack but inside a column of a `NavigationSplitView`, setting the bound item to a non-nil value will replace the root view of the subsequent column. Setting the bound item to a nil value will restore the original root view.  (106106406)
- Fixed: When a flexible frame modifier (e.g. frame(minHeight: 100, maxHeight: 200)) is used inside a scroll view the modified view could end up truncating content. This would most often be visible with the content view being a VStack with multiline text.  (107014454)
- Fixed: When scrolling to the end of a scroll view using ScrollViewReader, the final offset will be clamped to the scroll view’s total content size and no longer overscroll.  (107558652) (FB12094127)
- Fixed: Removed a spurious warning, “NavigationLink presenting a value must appear inside a NavigationContent-based NavigationView. Link will be disabled.”  (107877668) (FB12111423)
- Fixed: Views in Lists and Lazy Stacks might be improperly displayed after scrolling.  (108021411)
- Fixed: Suggested search tokens will be hidden by default when the search text is not empty  (108381393)
- Fixed: ScrollView when used with the searchable modifier has an improved transition when presenting or dismissing search on iOS and iPadOS.  (109265624)
- Fixed an issue where `NSHostingView` would not appear when printed using `NSPrintOperation`.  (109412691)
- Fixed: Two `NavigationSplitView` initializers taking `columnVisibility` as a value rather than a `Binding`.  (109426553)
- Fixed: macOS under-toolbar/full-height inspectors now behave as presented in the WWDC23 inspector session. Notably the full-height appearance was previously used incorrectly sometimes.  (109532401)
- Fixed: Clicking on a button can errantly warn about updating state during a view update.  (109610945)
- Fixed: Inspector presentations no longer have an animation glitch. Inspector presentations no longer increase window size on first presentation unless the window is forced to grow larger by `navigationSplitColumnWidth` modifiers.  (111577034) (FB12488754)

###### Known Issues

- `View.defaultFocus(_:_:)` isn’t reliable with text controls.  (109750983)  Manually update focus state bindings from an action passed to `View.onAppear(perform:)`.
- On iOS, using an `Observable` object’s property as a selection value of a `List` inside `NavigationSplitView` may cause a “Simultaneous accesses to …” error when a list selection is made via tap gesture.  (113978783) (FB12981860)  There is no current workaround for `Observable` properties. Alternatives include factoring out the selection value into separate state stored outside the object, or using `ObservableObject` instead.

##### Swiftui Navigation

###### Resolved Issues

- Fixed: Animations inside `Navigation*` structures are no longer disabled.  (107771283)

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

##### System Ui Languages

###### Resolved Issues

- Fixed: There are some strings left in English for people running macOS 14.0 Beta in other languages.  (109520700)

##### Trusted Execution

###### New Features

- `/usr/bin/syspolicy_check` is a new command line tool to help determine if the provided macOS application will pass the current running configurations’ system policy. This includes the same checks performed by the Apple notary service and other macOS Trusted Execution layers such as codesign, Gatekeeper, XProtect, and more. Please see the main page for additional details.  (108737781)
- `/usr/bin/gktool` is a new command line tool to assess Gatekeeper Policy on applications. `gktool` can be called to pre-warm the system cache so users do not see the ‘Verifying…’ dialog on first launch of an application.  (109793778)

##### Uikit

###### New Features

- The query rects passed in to `-layoutAttributesForElementsInRect:` will be more specific to the collection view’s frame, and the rect might intersect with previously queried frames. If subclassing a UIKit vended layout and modifying the frames of elements by applying offsets, make sure that the same offset is applied to the rect passed in to `-layoutAttributesForElementsInRect:` as well, or the user might see items disappearing when they shouldn’t be.  (108663389)

##### Update

###### Resolved Issues

- Fixed: T2 Macs might receive an error in the Software Update Preferences pane when attempting to update to macOS Ventura 13.6 Beta 1 or macOS Monterey 12.7 Beta 1.  (113829185)

##### Video Effects

###### Resolved Issues

- Fixed: Changing video effects settings for an application that accepts camera input changes the settings for other applications that also accept camera input.  (108229728)
- Fixed: The Video Effects menu bar item might not appear for certain applications.  (110038665)

##### Virtualization

###### Resolved Issues

- Fixed: Installing the macOS Seed in a virtual machine might fail on a host Mac.  (109234128)

##### Vision

###### Resolved Issues

- Fixed:  `VNDetectHumanBodyPose3DRequest` now returns results for images/frames of people without depth metadata or camera intrinsics explicitly provided.  (109723859)
- Fixed issue with `cameraOriginMatrix`  so a 180 rotation around x axis is no longer required. Please reference updated sample code for WWDC Session 111241.  (110726503)

##### Weather Averages

###### Resolved Issues

- Fixed: Placeholders are displayed in locations where Weather averages data isn’t available.  (110133240)

##### Web Apps

###### Resolved Issues

- Fixed: When the system is set to dark mode, the title bar for web apps now appear correctly.  (99514840)
- Fixed: Clicking a notification activates the web app on the current page instead of opening the expected URL.  (107906244)
- Fixed: After allowing permission access, the web app correctly appears in System Settings > Privacy & Security > Location Services.  (109499769)

##### Wi Fi

###### Resolved Issues

- Fixed: While a Mac has active traffic via Wi-Fi, you might experience difficulty discovering and connecting to Continuity Camera.  (109954955)

##### Widgetkit

###### Resolved Issues

- Fixed: Some widgets on macOS, especially those that use App Intents for Configuration, might not work properly the first time the system is started.  (109518265)
- Fixed: Apps that use the `.showsWidgetContainerBackground` environment variable no longer crash.  (113947483) (FB12974903)

##### Wkwebview

###### New Features

- Added support for inline predictions for autocomplete.  (105197136)

##### Xcode

###### Resolved Issues

- Fixed: Xcode might crash when creating a new file.  (112337760)

## See Also

- [macOS Sonoma 14.6 Release Notes](macos-14_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.5 Release Notes](macos-14_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.4 Release Notes](macos-14_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.3 Release Notes](macos-14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.2 Release Notes](macos-14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.1 Release Notes](macos-14_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-14-release-notes)*