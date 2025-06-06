# watchOS 8 Release Notes

**Framework**: Watchos Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 8 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 8. The SDK comes bundled with Xcode 13, available from the Mac App Store. For information on the compatibility requirements for Xcode 13, see [`Xcode 13 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-13-release-notes).

##### General

###### Known Issues

- Your watch might repeatedly disconnect unexpectedly from your phone. (80733338)  Restart your phone.

##### App Store

###### New Features

- [`StoreKit`](https://developer.apple.com/documentation/StoreKit) 2 introduces a modern Swift-based API that takes advantage of new language features like Swift concurrency. Use this API to load product information, display in-app purchases in your store, allow customers to make purchases, manage access to content and subscriptions, and receive transaction information signed by the App Store in JSON Web Signature (JWS) format. (66587964)

- The `request(with:)` type method on [`Product`](https://developer.apple.com/documentation/StoreKit/Product) has been renamed to [`products(for:)`](https://developer.apple.com/documentation/StoreKit/Product/products(for:)). (79410910)

- The [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction) `listener` type properties on [`Product.SubscriptionInfo.Status`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/Status-swift.struct) and [`Storefront`](https://developer.apple.com/documentation/StoreKit/Storefront) are now [`updates`](https://developer.apple.com/documentation/StoreKit/Transaction/updates) and [`updates`](https://developer.apple.com/documentation/StoreKit/Storefront/updates), respectively. The nested [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) conforming structures are now [`Transaction.Transactions`](https://developer.apple.com/documentation/StoreKit/Transaction/Transactions), [`Product.SubscriptionInfo.Status.Statuses`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/Status-swift.struct/Statuses), and [`Storefront.Storefronts`](https://developer.apple.com/documentation/StoreKit/Storefront/Storefronts). Both `TransactionSequence` and `TransactionListener` are now [`Transaction.Transactions`](https://developer.apple.com/documentation/StoreKit/Transaction/Transactions). (79034347)

- `StoreKitError.userDidNotAuthenticate` is no longer available; use [`StoreKitError.userCancelled`](https://developer.apple.com/documentation/StoreKit/StoreKitError/userCancelled) instead. (78270199)

- You can now access [`Product`](https://developer.apple.com/documentation/StoreKit/Product) raw JSON data for custom decoding: - Multiple [`Product.PurchaseOption`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption) methods are now allowed. `.custom(_:)` is replaced with several new type methods, namely [`custom(key:value:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/custom(key:value:)-80cvh), [`custom(key:value:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/custom(key:value:)-3g3nc), [`custom(key:value:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/custom(key:value:)-8tjim), and [`custom(key:value:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/custom(key:value:)-7rju9).
- Subscript operators on [`Product`](https://developer.apple.com/documentation/StoreKit/Product), [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction), and [`renewalInfo`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/Status-swift.struct/renewalInfo) are removed, along with the nested `Key` enumerations.
- `BackingValue` and extensions adding initializers from `BackingValue` are removed. (79101606)

- A new [`onStorefrontChange(shouldContinuePurchase:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/onStorefrontChange(shouldContinuePurchase:)) is available in StoreKit 2. You can use this purchase option to determine whether the transaction continues if the App Store storefront changes during a transaction. The default is `true` if this option isn’t added. (70757789)

- `VerificationResult.unverified(SignedType)` is now `VerificationResult.unverified(SignedType, VerificationError)` to provide a reason for unverified signed values. [`jsonRepresentation`](https://developer.apple.com/documentation/StoreKit/Transaction/jsonRepresentation) is available on [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction) and [`jsonRepresentation`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo/jsonRepresentation) is available on [`renewalInfo`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/Status-swift.struct/renewalInfo); both properties provide the payload JSON as `Data`. [`payloadValue`](https://developer.apple.com/documentation/StoreKit/VerificationResult/payloadValue) and [`unsafePayloadValue`](https://developer.apple.com/documentation/StoreKit/VerificationResult/unsafePayloadValue) properties are available on [`VerificationResult`](https://developer.apple.com/documentation/StoreKit/VerificationResult) as a convenience to access the signed value. (80701792)

###### Resolved Issues

- Fixed an issue where purchases performed in the Sandbox environment returned `VerificationResult.unverified(_:_:)`. (71949674)

Resolved Issues Fixed issue where `jwsRepresentation` and other validation related properties were not available on `VerificationResult`. (81517650)

###### Known Issues

- The [`unfinished`](https://developer.apple.com/documentation/StoreKit/Transaction/unfinished) property might return `VerificationResult<Transaction>` for transactions that have already finished. (81346114)

##### Focus

###### Known Issues

- Apps installed only on your watch aren’t available in the Focus settings allow list. (76064919)

###### Deprecations

- [`MKPinAnnotationView`](https://developer.apple.com/documentation/MapKit/MKPinAnnotationView) and [`MapPin`](https://developer.apple.com/documentation/MapKit/MapPin) are marked as deprecated in this beta. (78536295)

##### Music

###### New Features

- The Radio app has merged into the Music app. (67836373)

###### Known Issues

- When using Watch apps, [`MusicKit`](https://developer.apple.com/documentation/MusicKit) might be unable to generate a developer token. (78478620)  Register the bundle identifier of your [`WatchKit`](https://developer.apple.com/documentation/WatchKit) Extension target as a separate App ID in the Developer portal, and enable the MusicKit App Service for the new App ID.

##### Networking

###### New Features

- The default `Accept-Language` header that [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) sends has an updated format and corrected values for multiple locales. In addition to the preferred language, the header also includes the current system language as a fallback if it differs from the preferred language. This behavior affects apps that link against macOS 12, iOS 15, tvOS 15, and watchOS 8 SDKs. (38772422)

###### Deprecations

- Support for cleartext HTTP URL schemes for Proxy Automatic Configuration (PAC) is now deprecated. Use only HTTPS URL schemes for PAC. This affects all PAC configurations, including, but not limited to, configurations set via Settings, System Preferences, profiles, and `URLSession` APIs such as [`connectionProxyDictionary`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411499-connectionproxydictionary) and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](https://developer.apple.com/documentation/CFNetwork/CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)). If you configure a cleartext HTTP PAC URL, the system may upgrade it to HTTPS during PAC file loads. Web Proxy Auto-Discovery (WPAD) Protocol via DNS isn’t affected. Dynamic Host Configuration Protocol (DHCP) Option 252 WPAD may attempt to upgrade cleartext HTTP URLs to HTTPS during PAC file loads. (61981845)

##### Pairing

###### Known Issue

- The Watch app might crash when pairing through the camera. (80804790)  Pair the Watch using the “Pair Manually” button.

##### Shazam

###### Known Issues

- [`ShazamKit`](https://developer.apple.com/documentation/ShazamKit) might be unable to generate a developer token in apps using Shazam Catalog. (78589082)  Register the bundle identifier of your [`WatchKit`](https://developer.apple.com/documentation/WatchKit) Extension target as a separate App ID in the developer portal, then enable the ShazamKit App Service for this new App ID.

##### Swiftui

###### New Features

- [`LocalizedStringKey`](https://developer.apple.com/documentation/SwiftUI/LocalizedStringKey) can now contain Markdown syntax. The system parses Markdown strings when you create a [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) view from a `LocalizedStringKey`, including `Text` views created with a string literal. The system styles `Text` according to Markdown constructs. (74515884)

- You can create [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) from an [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString) structure. `Text` respects the styles you provide through attributes within the SwiftUI attribute scope; these styles take precedence over styles you provide through view modifiers. (74841755)

- Specific kinds of animations now execute off the main thread, so there are new thread-safety requirements. (70524799) Ensure the following functions and types are thread-safe: - All methods and accessors of types conforming to these protocols: [`AlignmentID`](https://developer.apple.com/documentation/SwiftUI/AlignmentID), [`Animatable`](https://developer.apple.com/documentation/SwiftUI/Animatable), [`EnvironmentKey`](https://developer.apple.com/documentation/SwiftUI/EnvironmentKey), [`EnvironmentValues`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues), [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable), [`GeometryEffect`](https://developer.apple.com/documentation/SwiftUI/GeometryEffect), [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable), [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable), [`PreferenceKey`](https://developer.apple.com/documentation/SwiftUI/PreferenceKey), [`Shape`](https://developer.apple.com/documentation/SwiftUI/Shape), [`VectorArithmetic`](https://developer.apple.com/documentation/SwiftUI/VectorArithmetic).
- Any closures you pass to the following types and functions, but only if the views that created them don’t have references to [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) types: [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach), [`GeometryReader`](https://developer.apple.com/documentation/SwiftUI/GeometryReader), doc://com.apple.documentation/documentation/swiftui/hstack/backgroundpreferencevalue(_:_:), doc://com.apple.documentation/documentation/swiftui/emptyview/overlaypreferencevalue(_:_:), doc://com.apple.documentation/documentation/swiftui/hstack/transformpreference(_:_:), doc://com.apple.documentation/documentation/swiftui/hstack/anchorpreference(key:value:transform:), doc://com.apple.documentation/documentation/swiftui/hstack/transformanchorpreference(key:value:transform:), doc://com.apple.documentation/documentation/swiftui/hstack/transformenvironment(_:transform:), doc://com.apple.documentation/documentation/swiftui/form/transaction(_:).

- A [`TextField`](https://developer.apple.com/documentation/SwiftUI/TextField) provided an [`NSFormatter`](https://developer.apple.com/documentation/foundation/nsformatter) now updates its binding as the user types. `NSFormatter` formats the text of the field when the user submits the field, or when focus moves away from the field. (67899823)

- You can now initialize [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) with a [`FormatStyle`](https://developer.apple.com/documentation/Foundation/FormatStyle). (72159423)

- While searching, if you tap a suggestion that uses the doc://com.apple.documentation/documentation/swiftui/anyview/searchcompletion(_:) modifier, the suggestion list now disappears rather than displaying the single suggestion you selected. (76965399)

- You can now customize the prompt of a search field that a searchable modifier configures using the `prompt` parameter instead of the previous `title` parameter. (77988967)

- Added `buttonBorderShape`, which can be used to control the shape of bordered buttons. (79456465)

- New [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString) attributes [`underlineStyle`](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes/3862794-underlinestyle) and [`strikethroughStyle`](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes/3862793-strikethroughstyle) were added to [`AttributeScopes.SwiftUIAttributes`](https://developer.apple.com/documentation/Foundation/AttributeScopes/SwiftUIAttributes). (78437803)

- Types conforming to the [`Animatable`](https://developer.apple.com/documentation/SwiftUI/Animatable) protocol and also conforming to either the [`View`](https://developer.apple.com/documentation/SwiftUI/View) or [`ViewModifier`](https://developer.apple.com/documentation/SwiftUI/ViewModifier) protocols now apply animations when their values change. Consequently, the [`AnimatableModifier`](https://developer.apple.com/documentation/SwiftUI/AnimatableModifier) protocol is soft-deprecated. Use `Animatable` directly when targeting the latest OS versions; for example, use `struct CustomModifier: ViewModifer, Animatable` rather than `struct CustomModifier: AnimatableModifier`. (76971100)

- The [`contentShape(_:eoFill:)`](https://developer.apple.com/documentation/SwiftUI/View/contentShape(_:eoFill:)) modifier now allows fine-grained control over different kinds of shapes. For drag previews, hover effects, and context menus, the matching `ContentShapeKinds` is required to affect the shape of previews when linked on iOS 15.0 or newer. The default behavior is to set the `interaction` kind. (60792377)

The [`openURL`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/openURL) environment value can now be set and used to customize URL handling in the view hierarchy, including URL handling in [`Link`](https://developer.apple.com/documentation/SwiftUI/Link) views and links embedded in [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) views. (78551237)

- [`Task`](https://developer.apple.com/documentation/Swift/Task) allows you to pass the priority to be used when spawning a new `Task`. (80599258)

- [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) views that contain excessive line height characters now have a larger default size to avoid clipping or overlapping of oversized characters. (80665315)

###### Known Issues

- You can’t push to a third screen after popping from a third screen in the navigation stack. (79076444)

###### Deprecations

- `controlProminence` is deprecated. Use the new `.borderedProminent` [`ButtonStyle`](https://developer.apple.com/documentation/SwiftUI/ButtonStyle) instead. (78908460)

##### Tabulardata

###### New Features

- [`TabularData`](https://developer.apple.com/documentation/TabularData) is a new Swift framework you use to analyze and manipulate tabular data. You can use [`DataFrame`](https://developer.apple.com/documentation/TabularData/DataFrame) to read CSV and JSON files, as well as join, group, and aggregate data. (69982458)

##### Xcode

###### Known Issues

- [`MusicKit`](https://developer.apple.com/documentation/MusicKit) functionality, such as loading content with music requests, doesn’t work in simulated devices. (78559381) : Test your app’s `MusicKit` functionality on a physical device.

## See Also

- [watchOS 8.7 Release Notes](watchos-8_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.6 Release Notes](watchos-8_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.5 Release Notes](watchos-8_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.4 Release Notes](watchos-8_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.3 Release Notes](watchos-8_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.1 Release Notes](watchos-8_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-8-release-notes)*