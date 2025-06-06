# tvOS 17 Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 17 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 17. The SDK comes bundled with Xcode 15, available from the Mac App Store. For information on the compatibility requirements for Xcode 15, see [`Xcode 15 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15-release-notes).

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

##### Camera and Avfoundation Capture

###### Resolved Issues

- Fixed: On iPhone 14 and 14 Plus models third-party camera applications might fail to capture images, and the built-in Camera app and third-party applications using the new Deferred Processing API might fail to process final images.  (113158045)

##### Continuity Camera on Apple Tv

###### Resolved Issues

- Fixed: After pausing and resuming the connection from an iPhone or iPad to the connected Apple TV, FaceTime call participants will see audio and video sync is mismatched for the Apple TV user.  (105464123)
- Fixed: Following a reboot of AppleTV or first launch of FaceTime, the preview video of camera feed while connecting your phone might take extra time to show up on the screen.   (108283141)
- Fixed: Center Stage functionality incorrectly defaults to UltraWide rather than Wide.  (109387427)
- Fixed: When using Center Stage in a group Facetime call, people at the edge of the frame will be cropped out.   (109850731)
- Fixed: Unsupported iPads might recieve a Continuity Camera notificaition.  (110136942)

##### Facetime Handoff

###### Resolved Issues

- Fixed: Facetime handoff to another device might result in call drop or no media.  (110126569)

##### Facetime on Apple Tv

###### Resolved Issues

- Fixed: Guest Pairing doesn’t work if Apple TV is connected via Ethernet.  (107163191)
- Fixed: If a phone is already a Connected Camera, answering a FaceTime call on that phone and then moving to Apple TV might result in a dropped call.  (107187159)
- Fixed: Cannot handoff a call that has a FaceTime link on the Apple TV. FaceTime on tvOS will crash.  (108109894)
- Fixed: Moving the FaceTime call from Apple TV to iPhone by tapping “Switch to phone” might result in a dropped call.  (108810085)
- Fixed: Moving from Split View to PIP during a call on Apple TV results in video being lost and privacy indicator not showing correct state.    (109537754)
- Fixed: Moving call from iPhone to Apple TV can result in failure in congested network environments.     (109841121)
- Fixed: Video effects buttons on self-view during a FaceTime call might not work.  (110801792)
- Fixed: FaceTime call might end suddenly within first minute.   (111099303)

##### Facetime on Appletv

###### Resolved Issues

- Fixed: Duplicate participants might appear when moving a call from iPhone to AppleTV.  (110036697)

##### Localization

###### Resolved Issues

- Fixed: Some content might appear in English. Some strings might appear clipped.  (109393568)

##### Manual Framing

###### Resolved Issues

- Fixed: If the user adjusted the zoom factor manually with controls in Control Center, the modified video factor will get incorrectly reset to 1.0 when the user enters the Group FaceTime mode.  (110809840)

##### Maps

###### Resolved Issues

- Fixed: When using `Map`, Xcode emits a runtime warning that “Publishing changes from within view updates is not allowed.”  (106174743)

##### Media

###### Resolved Issues

- Fixed: MP3 files with malformed ID3 tags will fail to play  (110230071)

##### Networkextension

###### Deprecations

- Algorithms DES, 3DES, SHA1-96 and SHA1-160 as well as Diffie-Hellman groups less than 14 are deprecated for IKEv2 VPNs.  (109427094)
- The enum values NEVPNIKEv2EncryptionAlgorithmDES, NEVPNIKEv2EncryptionAlgorithm3DES, NEVPNIKEv2IntegrityAlgorithmSHA96, NEVPNIKEv2IntegrityAlgorithmSHA160, NEVPNIKEv2DiffieHellmanGroup1, NEVPNIKEv2DiffieHellmanGroup2, and NEVPNIKEv2DiffieHellmanGroup5 in NEVPNProtocolIKEv2.h will be deprecated.  (109680935)

##### Networking

###### New Features

- iPhone and iPad devices running iOS 17 beta support joining wired 802.1X networks. Apple TV devices running tvOS 17 beta also support joining wired 802.1X networks.  (12867782)
- `URLSession` supports resumable uploads in HTTP. Just like download tasks, upload tasks can now be paused and resumed if the server supports the latest protocol draft. To learn more, see [`Resumable Uploads for HTTP`](https://developer.apple.comhttps://www.ietf.org/archive/id/draft-ietf-httpbis-resumable-upload-01.txt).  (68890505)
- Apple devices now support connection to 802.1X networks using EAP-TLS with TLS 1.3 (EAP-TLS 1.3). EAP-TLS 1.3 further improves security and privacy by always providing forward secrecy, never disclosing the peer identity, and by mandating use of revocation checking when compared to EAP-TLS with earlier versions of TLS.  (74526852)

###### Resolved Issues

- Fixed: For apps linked on or after iOS 17 and aligned OS versions, App Transport Security now requires secure connections to external IP addresses by default. For more information on these requirements, see [`Preventing Insecure Network Connections`](https://developer.apple.comhttps://developer.apple.com/documentation/security/preventing_insecure_network_connections). Exceptions can be made using [`NSExceptionDomains`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nsapptransportsecurity/nsexceptiondomains), which now supports exceptions for individual IP addresses and ranges specified in classless inter-domain routing (CIDR) notation.  (101967030)
- Fixed: For apps linked on or after iOS 17 beta, macOS 14 beta, watchOS 10 beta, and tvOS 17 beta, the `Transfer-Encoding` header field of a streamed `HTTP/1` request is set to `chunked` instead of `Chunked`.  (107390029)

##### Shareplay

###### Resolved Issues

- Fixed: Starting SharePlay content between two Apple TVs results in one TV receiving a notification with “pseud…” as the name for the other TV.  This only occurs on first attempt and subsequent SharePlay actions are correct.  (108926589)

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
- StoreKit Views`ProductView` and `StoreView` have initializers have initializers that give you access to the promotional icon as a SwiftUI view and the various phases of the loading operation. Use initializers such as [`init(id:icon:placeholderIcon:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/productview/4202217-init), [`init(_:icon:)]`(https://developer.apple.com/documentation/storekit/productview/4202214-init), [`init(ids:icon:placeholderIcon:)](https://developer.apple.com/documentation/storekit/storeview/4203378-init), and [init(products:icon:)``](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/storeview/4203382-init) to provide an icon view for each phase.  (110470147)
- The following StoreKit types are renamed: • `DefaultProductViewStyle` is renamed to [`AutomaticProductViewStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/automaticproductviewstyle) • `DefaultSubscriptionStoreMarketingContent` is renamed to [`AutomaticSubscriptionStoreMarketingContent`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/automaticsubscriptionstoremarketingcontent) • `DefaultProductPlaceholderIcon` is renamed to [`AutomaticProductPlaceholderIcon`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/automaticproductplaceholdericon)  (111185321)

###### Resolved Issues

- Fixed: When testing in the sandbox environment, the `groupDisplayName` property on [`Product.SubscriptionInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo) might return an empty string if the localization in the current storefront is not in an approved state. When using the `SubscriptionStoreView` without providing a marketing content view, the automatic view might show the name of the app instead of the subscription group’s display name.  (107206601)
- Fixed issue where [`StoreView`](https://developer.apple.com﻿﻿https://developer.apple.com/documentation/storekit/storeview) or [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) content might appear in English, or show a localization key, instead of showing localized text for the App Store storefront.  (110734447)

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
- Fixed: The default platform container directory is not available on tvOS and accessing it will result in a sandbox violation that causes a crash.  (109487314)
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
- Fixed in beta 7: Apps using SwiftData that are built with Xcode 15 beta 6 have known issues when running on tvOS 17 beta 6.  (113971504)

###### Known Issues

- SwiftData models with implicitly unwrapped optional properties will generate a compiler error that all stored properties were not set.  (114140139)  Set the value of non-relationship stored properties in the initializer, and mark relationship properties as optional.

##### Swiftui

###### New Features

- `RoundedRectangle` now defaults to the continuous corner style.  (63246947)
- `.onChange` has new overloads where the closure takes 0 or 2 arguments, these new versions will call the new version of the closure (i.e. after the specified value has changed), so any captured properties will have up to date values. The previous overload (which calls the old version of the closure) has been deprecated.  (67344857)
- Spring animations will now default to being critically damped (i.e. a bounce of 0).  (75149732)
- `List`s using the `SidebarListStyle` hosted in primary column of a UIKit `UISplitNavigationController` were previously rendering with an `insetGrouped` appearance.  With this change they will render as the expected `sidebar` appearance similar to if the `List` were hosted in a SwiftUI `NavigationSplitView`.  (96909195)
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

###### Resolved Issues

- Fixed: `NavigationSplitView` reuses view controllers in more cases, resulting in significantly improved performance. This might change the behavior of code that relies on the life cycle messages sent to `UIHostingController` because such controllers will be created less often.  (88880547)
- Fixed: Scroll environment properties like isScrollEnabled and scrollDismissesKeyboardMode are no longer propagated past nested scroll views.  (99195890)
- Fixed: Previously it was possible for views animating their removal via a transition to be drawn above a view with the same zIndex that has not yet been removed. This was unintentional and has now been updated: views transitioning out of the view hierarchy are always drawn below non-removed views with the same zIndex.  (101085960)
- Fixed: LazyVGrid or LazyHGrid has an improved layout when used with fixedSize().  (103075945)
- Fixed: The new `.navigationDestination(item:content:)` modifier now works correctly both inside a `NavigationStack` and outside a stack but inside a column of a `NavigationSplitView`. Inside a stack, setting the bound item to a non-nil value will push a view onto the stack immediate above the view containing the modifier. Setting the bound item to a nil value will pop the view. Outside a stack but inside a column of a `NavigationSplitView`, setting the bound item to a non-nil value will replace the root view of the subsequent column. Setting the bound item to a nil value will restore the original root view.  (106106406)
- Fixed: In some circumstances, the first view pushed onto a `NavigationStack` or collapsed `NavigationSplitView` might fail to animate.  (106602046)
- Fixed: When a flexible frame modifier (e.g. frame(minHeight: 100, maxHeight: 200)) is used inside a scroll view the modified view could end up truncating content. This would most often be visible with the content view being a VStack with multiline text.  (107014454)
- Fixed: When scrolling to the end of a scroll view using ScrollViewReader, the final offset will be clamped to the scroll view’s total content size and no longer overscroll.  (107558652) (FB12094127)
- Fixed: Removed a spurious warning, “NavigationLink presenting a value must appear inside a NavigationContent-based NavigationView. Link will be disabled.”  (107877668) (FB12111423)
- Fixed: ScrollView when used with the searchable modifier has an improved transition when presenting or dismissing search on iOS and iPadOS.  (109265624)
- Fixed: Two `NavigationSplitView` initializers taking `columnVisibility` as a value rather than a `Binding`.  (109426553)

###### Known Issues

- On iOS, using an `Observable` object’s property as a selection value of a `List` inside `NavigationSplitView` may cause a “Simultaneous accesses to …” error when a list selection is made via tap gesture.  (113978783) (FB12981860)  There is no current workaround for `Observable` properties. Alternatives include factoring out the selection value into separate state stored outside the object, or using `ObservableObject` instead.

##### Symbol Effects

###### Resolved Issues

- Fixed: In the objective-C API in Symbols.framework, requesting `effectWithWholeSymbol` on `NSSymbolPulseEffect` and `NSSymbolBounceEffect` will result in the effect being configured to animate by layer instead.  (109284710)

##### Tipkit

###### Resolved Issues

- Fixed: Tips and TipKit views will not display on Apple TV hardware.  (108286122)

##### Uikit

###### New Features

- The query rects passed in to `-layoutAttributesForElementsInRect:` will be more specific to the collection view’s frame, and the rect might intersect with previously queried frames. If subclassing a UIKit vended layout and modifying the frames of elements by applying offsets, make sure that the same offset is applied to the rect passed in to `-layoutAttributesForElementsInRect:` as well, or the user might see items disappearing when they shouldn’t be.  (108663389)

###### Resolved Issues

- Fixed: Prior to iOS 17 and tvOS 17, `UIGestureRecognizer` would set its `state` to `UIGestureRecognizerStateFailed` in the base implementation of `- (void)pressesBegan:withEvent:` if there are no active touches. In iOS 17 and tvOS 17, this behavior has been fixed. On tvOS, `UIGestureRecognizer` allows `UIPressTypeSelect` by default, thus custom `UIGestureRecognizer`s that do not set `allowedPressTypes` might have been relying on this behavior to put themselves into a terminal state after they receive a `UIPress` of type `UIPressTypeSelect`. `UIGestureRecognizer`s that receive events but do not reach a terminal state will block gesture recognizer dependency graphs from resetting, which can cause an app’s interface to become unresponsive. It is important to for custom `UIGestureRecognizer`s on tvOS 17 to either either set `allowedPressTypes` to an empty array if they do not handle `UIPressTypeSelect`, or to implement the `UIPressesEvent` response methods in `UIGestureRecognizerSubclass.h`, and set themselves to a terminal state as appropriate.  (111175673)

##### Vision

###### Resolved Issues

- Fixed:  `VNDetectHumanBodyPose3DRequest` now returns results for images/frames of people without depth metadata or camera intrinsics explicitly provided.  (109723859)
- Fixed issue with `cameraOriginMatrix`  so a 180 rotation around x axis is no longer required. Please reference updated sample code for WWDC Session 111241.  (110726503)

##### Wi Fi

###### Resolved Issues

- Fixed: While a Mac has active traffic via Wi-Fi, you might experience difficulty discovering and connecting to Continuity Camera.  (109954955)

## See Also

- [tvOS 17.6 Release Notes](tvos-17_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.5 Release Notes](tvos-17_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.4 Release Notes](tvos-17_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.3 Release Notes](tvos-17_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.2 Release Notes](tvos-17_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.1 Release Notes](tvos-17_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-17-release-notes)*