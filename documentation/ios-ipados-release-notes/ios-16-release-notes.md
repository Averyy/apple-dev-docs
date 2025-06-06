# iOS 16 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS 16 SDK provides support to develop apps for iPhone and iPad running iOS 16. The SDK comes bundled with Xcode 14, available from the Mac App Store. For information on the compatibility requirements for Xcode 14, see [`Xcode 14 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14-release-notes).

##### Avfoundation

###### New Features

- `AVCaptureSession.isMultitaskingCameraAccessSupported` returns `true` on iPads that support Stage Manager. (88345287)

##### Backup

###### New Features

- Customers using iOS 16 can now back up their device over an LTE cellular connection, as well as a 5G or Wifi connection. (95276719)

##### Coregraphics

###### Deprecations

- To improve security, `CGImageCreate` enforces parameter correctness on macOS 13 Ventura, iOS 16, iPadOS 16, watchOS 9, and tvOS 16. Passing an incorrect `CGImageByteOrderInfo` is no longer supported, and will result in images failing to load. (94855401)

##### Devicediscoveryui

###### Known Issues

- Devices running beta 4 or later aren’t backwards compatible with devices running earlier beta versions. (95233878)

##### Emoji

###### Known Issues

- The search field for the emoji Lock Screen editor is missing. (88603664)

##### Game Controller

###### New Features

- Many additional Bluetooth and USB game controllers are supported by the Game Controller framework on macOS 13, iOS 16, and tvOS 16 and later. (82409809)

##### Healthkit

###### New Features

- HealthKit workout APIs now support multisport workouts with activities of swimming, cycling, and running. (82588168)

- New data types for running workout metrics like running power, ground contact time, vertical oscillation, running speed, and stride length. (82974514)
- A new data type is available to track AFib History. (95315701)
- The [`HealthKit`](https://developer.apple.com/documentation/HealthKit) framework has a new Vision Prescription data type that allows developers and users to store prescription information received from eye care professionals. This feature includes a new set of [`HKSample`](https://developer.apple.com/documentation/HealthKit/HKSample) subclasses that allow developers to encapsulate prescriptions for glasses and contact lenses. Users of iPhone can directly store their prescription information from the Health app as well. Because most regions require the actual prescription document to purchase glasses and contacts, this feature also allows the storage of attachment files in `HealthKit`. Due to the potential privacy concerns around sharing unintended additional details from the prescription, the `HealthKit` framework has a new authorization API to allow users to authorize prescriptions on a per-sample basis. See header documentation in `HealthKit` and watch the WWDC HealthKit session for more information. (82940646)

##### Home

###### Known Issues

- The device that initiates the pairing needs to use the same iCloud account as the home hub. Only the owner of a home, not an invited user, can pair Matter accessories. (76012945)

##### Mail

###### New Features

- Remind Me messages that have fired won’t show at the top of the message list until the message list is refreshed. (94046413)

###### Known Issues

- Moving a Remind Me message to another mailbox doesn’t remove the Remind Me banner. (93671992)

##### Maps

###### Deprecations

- Don’t use `MKMapLandscape`, `MKStandardMapConfigurationMapMode`, `[MKMapView configuration]`, and `[MKStandardMapConfiguration showsBuildings]`. Use their functional equivalents [`MKMapConfiguration.ElevationStyle`](https://developer.apple.com/documentation/MapKit/MKMapConfiguration/ElevationStyle-swift.enum), [`MKStandardMapConfiguration.EmphasisStyle`](https://developer.apple.com/documentation/MapKit/MKStandardMapConfiguration/EmphasisStyle-swift.enum), and [`preferredConfiguration`](https://developer.apple.com/documentation/MapKit/MKMapView/preferredConfiguration), instead. Additionally, `showsBuildings` is now deprecated. (93449747)

##### Messages

###### New Features

- Allows developers to classify incoming SMS from unknown numbers into 12 new sub-categories within `Transaction` and `Promotion` categories for improved organization. (95276296)
- For Indian users, Messages now supports event extraction from SMS. These event and appointment messages are presented as Siri suggestions and also are presented to users in Messages thread and in Calendar Inbox. (95276513)
- For selected US Carriers, Messages extends the “Report Junk” feature to enable users to report SMS/MMS junk to Carriers. The option is visible inside Messages from Unknown Senders. (95276623)
- Messages now supports the ability for customers with a dual SIM iPhone to filter their messages based on their SIMs. (95276784)

##### Metal

###### Known Issues

- When using the new Metal mesh shaders feature, render pipeline state objects (PSOs) created with a mesh shader stage but without a object shader stage can fail to compile or fail to work correctly on some devices. (89836551)  When creating render PSOs with a mesh shader stage, also include a (potentially trivial pass-through) object shader stage.

###### Deprecations

- The `MTLResource.gpuHandle` is deprecated. Use [`gpuResourceID`](https://developer.apple.com/documentation/Metal/MTLAccelerationStructure/gpuResourceID) instead, which functions as a replacement. (92862429)

##### Metal Offline Compiler

###### Known Issues

- `MetalFX` effect outputs aren’t designed to be consumed by the CPU. Outputting to a texture that is read only by the CPU might result in synchronization issues. (91515075)  If a CPU reading of the `MetalFX` output is desired, instead of encoding the `MetalFX` effect as the last item in a command buffer, encode a placeholder blit that consumes the `MetalFX` output texture (a 1-pixel region blit is fine) in the command buffer. After the command buffer with the placeholder blit is finished, reading of the `MetalFX` effect output texture with CPU synchronizes correctly.

##### Networking

###### New Features

- Added `NSURLSession` support for client-certificate based authentication. (24523955)

- Added `URLSession` support for Private Access Tokens. (82937526)

###### Deprecations

- FTP is deprecated for `URLSession` and related APIs. Please adopt modern secure networking protocols such as HTTPS. (92623659)

##### Roomplan

###### New Features

- The [`RoomPlan`](https://developer.apple.com/documentation/RoomPlan) framework is now available in iOS 16, enabling 3D parametric model creation of an interior room. The framework uses a device’s sensors, trained machine learning models, and [`RealityKit`](https://developer.apple.com/documentation/RealityKit) rendering capabilities to capture the physical surroundings of an interior room. APIs are available for end-to-end scanning experience, real-time data structures for custom UI creation, and both USD and USDZ generation of 3D room models. (84170837)

##### Storekit

###### New Features

- A property `recentSubscriptionStartDate` is included in `RenewalInfo`. It represents the date that marks the start of the most recent period of continuous subscription. A period is considered a continuous subscription if there is no more than a 60-day gap between any two subscribed periods. (86599570)

- `Product` has new properties for localizing prices and subscription periods. For iOS 15, iPadOS 15, macOS 12, tvOS 15, and watchOS 8 or later use `priceFormatStyle` to format numbers derived from `price`. Use `subscriptionPeriodFormatStyle` to format durations of time relating to a subscription period. On iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9 or later use `subscriptionPeriodUnitFormatStyle` to format single units of a subscription period. (93780442)

- A property environment is included in [`Product.SubscriptionInfo.RenewalInfo`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo) and [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction). It represents the server environment in which the `RenewalInfo` and `Transaction` occurred, respectively. (85988753)

- [`AppTransaction`](https://developer.apple.com/documentation/StoreKit/AppTransaction) allows developers to cryptographically verify that the app was purchased on the App Store. (86739279)

- The `recentSubscriptionStartDate` property is included in [`Product.SubscriptionInfo.RenewalInfo`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo). It represents the date that marks the start of the most recent period of continuous subscription. A period is considered a continuous subscription if there’s no more than a 60-day gap between any two subscribed periods. (86599570)

- The [`priceLocale`](https://developer.apple.com/documentation/StoreKit/SKProduct/priceLocale) property is included in [`Product`](https://developer.apple.com/documentation/StoreKit/Product). Use this property to format price values deriving from the product’s decimal price. (81480683)

- Present the offer code redemption sheet with the [`offerCodeRedemption(isPresented:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:)) view modifier in your SwiftUI apps. (85321941)

- The StoreKit Messages API allows you to control when App Store messages are displayed in your app. (85321880)

- Read the [`requestReview`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/requestReview) environment value to get an instance of a [`RequestReviewAction`](https://developer.apple.com/documentation/StoreKit/RequestReviewAction). Then, call this instance to request to display a review prompt from your SwiftUI apps. (86739003)

- All [`StoreKit`](https://developer.apple.com/documentation/StoreKit) APIs are now annotated for sendability and main actor isolation. (84157048)

###### Deprecations

- Deprecated the SKDownload API and removed the option to upload nonconsumable in-app purchase assets for Apple to host. In addition, support for managing these assets in App Store Connect is no longer available as of April 2022. (89764253)

##### Swiftui

###### New Features

- Added `View.scrollContentBackground`, which permits customization of background colors for scrollable views like `List`. (45928055)
- Added `View.focusedObject(_:)` and `View.focusedSceneObject(_:)` modifiers to be used in conjunction with the new `@FocusedObject` to allow an `ObservableObject` to be vended by the focused view or scene. (83637876)

- Custom types conforming to `ToolbarContent` now support dynamic properties like `@Environment`. (94117842)

- You can now place a [`TextField`](https://developer.apple.com/documentation/SwiftUI/TextField) in an [`Alert`](https://developer.apple.com/documentation/SwiftUI/Alert) by using `alert` modifiers that accept a [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder). (64819930)

- For `control`, [`Section`](https://developer.apple.com/documentation/SwiftUI/Section), or other views that have a [`Label`](https://developer.apple.com/documentation/SwiftUI/Label), the [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder) content now automatically arranges and styles multiple views as hierarchical elements, such as `title` and `subtitle`. If the `label` views are intended to be arranged horizontally rather than hierarchically, wrap the views within an [`HStack`](https://developer.apple.com/documentation/SwiftUI/HStack). (85184563)

- A `TextField` supports multiline text. Use a [`Axis.vertical`](https://developer.apple.com/documentation/SwiftUI/Axis/vertical) axis on a text field to allow rendering of multiple lines in contexts like forms, where text is expected to be short to medium length. For long-form text editing, continue to use a [`TextEditor`](https://developer.apple.com/documentation/SwiftUI/TextEditor). (51463718)
- Navigation bars have new default behaviors. A navigation bar defaults to an inline title display mode, if no title is provided. If a title is provided, the default remains large. Use the [`navigationBarTitleDisplayMode(_:)`](https://developer.apple.com/documentation/SwiftUI/View/navigationBarTitleDisplayMode(_:)) modifier to change this. By default, a navigation bar only renders if it has content to display. If a navigation bar has no title, toolbar items, or search content, it’s automatically hidden. Use the [`navigationBarHidden(_:)`](https://developer.apple.com/documentation/SwiftUI/View/navigationBarHidden(_:)) or the new `.toolbar(.visible)` modifier to explicitly show an empty navigation bar. (84996257)

- A `list` supports Section footers. (78462739)
- When the toolbar modifier is applied at multiple levels of a hierarchy, items from a child are appended to those from the parent that have the same placement. (65619097)
- When using `.windowResizability(.contentSize)`, windows created with SwiftUI set their resizable and fullscreen flags based on the size of their contents. (65791490)
- [`List`](https://developer.apple.com/documentation/SwiftUI/List) separator insets can now be customized using  [`HorizontalEdge.leading`](https://developer.apple.com/documentation/SwiftUI/HorizontalEdge/leading) and [`HorizontalEdge.trailing`](https://developer.apple.com/documentation/SwiftUI/HorizontalEdge/trailing) alignment guides. (74192080)
- The implementation of `list` no longer uses [`UITableView`](https://developer.apple.com/documentation/UIKit/UITableView). (81571203)
- SwiftUI now enforces at runtime that view and view controller representables are value types. (82982458)
- Symbol images now use an automatically determined symbol-rendering mode by default. To have a symbol image always use monochrome rendering, use the [`SymbolRenderingMode`](https://developer.apple.com/documentation/SwiftUI/SymbolRenderingMode) modifier. (85524479)
- A Picker with a menu style in a `list` displays its `label` by default. To hide the `label`, use the `labelsHidden()` modifier. (88228016)
- Pickers in `list` default to the menu style. (89186618)
- Changes to `text` and `image` views now animate by default. Use `.contentsTransition(.identity)` to disable this behavior. (89558882)
- Lists and forms automatically dismiss the software keyboard, if present, when a scroll gesture begins. Use `.scrollDismissesKeyboard(.never)` to restore the old behavior. (89588639)

###### Known Issues

- Providing actions to a `navigationTitle` modifier has been deprecated. Use the `toolbarTitleActions()` modifier or `ToolbarTitleActions` type in a toolbar modifier instead. (93658035)
- Lists and tables might not clear their selection when exiting Edit Mode. (94093589)

##### Uikit

###### New Features

- iOS apps can now request rotation using `[UIWindowScene requestGeometryUpdate:errorHandler:]` and providing a `UIWindowSceneGeometryPreferencesIOS` object containing the desired orientations. (95229615)

###### Deprecations

- `[UIViewController shouldAutorotate]` has been deprecated is no longer supported. `[UIViewController attemptRotationToDeviceOrientation]` has been deprecated and replaced with `[UIViewController setNeedsUpdateOfSupportedInterfaceOrientations]`.  Apps relying on `shouldAutorotate` should reflect their preferences using the view controllers `supportedInterfaceOrientations`. If the supported orientations change, use `-[UIViewController setNeedsUpdateOfSupportedInterface

##### Wallet

###### Known Issues

- American Express cards might need to be removed and re-added to Wallet after updating to iOS 16 beta 6 or later. (97990752)

## See Also

- [iOS & iPadOS 16.6 Release Notes](ios-ipados-16_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.5 Release Notes](ios-ipados-16_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.4 Release Notes](ios-ipados-16_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.3 Release Notes](ios-ipados-16_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.2 Release Notes](ios-ipados-16_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS 16.1 Release Notes](ios-16_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iPadOS 16 Release Notes](ipados-16-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-16-release-notes)*