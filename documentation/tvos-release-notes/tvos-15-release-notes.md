# tvOS 15 Release Notes

**Framework**: tvOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The tvOS 15 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 15. The SDK comes bundled with Xcode 13. For information on the compatibility requirements for Xcode 13, see [Xcode 13 Release Notes](../Xcode-Release-Notes/xcode-13-release-notes.md).

### App Store

#### New Features

- The `request(with:)` type method on [`Product`](../StoreKit/product.md) is now renamed to [`products(for:)`](../StoreKit/product/products%28for%29.md). (79410910)

- The [`Transaction`](../StoreKit/transaction.md) `listener` type properties on [`Product.SubscriptionInfo.Status`](../StoreKit/product/subscriptioninfo/status-swift.struct.md) and [`Storefront`](../StoreKit/storefront.md) are now [`updates`](../StoreKit/transaction/updates.md) and [`updates`](../StoreKit/storefront/updates.md), respectively. The nested [`AsyncSequence`](../Swift/asyncsequence.md) conforming structures are now [`Transaction.Transactions`](../StoreKit/transaction/transactions.md), [`Product.SubscriptionInfo.Status.Statuses`](../StoreKit/product/subscriptioninfo/status-swift.struct/statuses.md), and [`Storefront.Storefronts`](../StoreKit/storefront/storefronts.md). Both `TransactionSequence` and `TransactionListener` are now [`Transaction.Transactions`](../StoreKit/transaction/transactions.md). (79034347)

- `StoreKitError.userDidNotAuthenticate` is no longer available; use [`StoreKitError.userCancelled`](../StoreKit/storekiterror/usercancelled.md) instead. (78270199)

- You can now access [`Product`](../StoreKit/product.md) raw JSON data for custom decoding:

  - Multiple [`Product.PurchaseOption`](../StoreKit/product/purchaseoption.md) methods are now allowed. `.custom(_:)` is replaced with several new type methods, namely [`custom(key:value:)`](../StoreKit/product/purchaseoption/custom%28key,value%29-80cvh.md), [`custom(key:value:)`](../StoreKit/product/purchaseoption/custom%28key,value%29-3g3nc.md), [`custom(key:value:)`](../StoreKit/product/purchaseoption/custom%28key,value%29-8tjim.md), and [`custom(key:value:)`](../StoreKit/product/purchaseoption/custom%28key,value%29-7rju9.md).
  - Subscript operators on [`Product`](../StoreKit/product.md), [`Transaction`](../StoreKit/transaction.md), and [`renewalInfo`](../StoreKit/product/subscriptioninfo/status-swift.struct/renewalinfo.md) are removed, along with the nested `Key` enumerations.
  - `BackingValue` and extensions adding initializers from `BackingValue` are removed. (79101606)

- A new type property [`unfinished`](../StoreKit/transaction/unfinished.md) is now available on [`Transaction`](../StoreKit/transaction.md) that returns signed information for any transactions where the app still needs to deliver content to the user. (79620896)

- A new [`onStorefrontChange(shouldContinuePurchase:)`](../StoreKit/product/purchaseoption/onstorefrontchange%28shouldcontinuepurchase%29.md) is available in StoreKit 2. You can use this purchase option to determine whether the transaction continues if the App Store storefront changes during a transaction. The default is `true` if this option isn’t added. (70757789)

- `VerificationResult.unverified(SignedType)` is now `VerificationResult.unverified(SignedType, VerificationError)` to provide a reason for unverified signed values. [`jsonRepresentation`](../StoreKit/transaction/jsonrepresentation.md) is available on [`Transaction`](../StoreKit/transaction.md) and [`jsonRepresentation`](../StoreKit/product/subscriptioninfo/renewalinfo/jsonrepresentation.md) is available on [`renewalInfo`](../StoreKit/product/subscriptioninfo/status-swift.struct/renewalinfo.md); both properties provide the payload JSON as `Data`. [`payloadValue`](../StoreKit/verificationresult/payloadvalue.md) and [`unsafePayloadValue`](../StoreKit/verificationresult/unsafepayloadvalue.md) properties are available on [`VerificationResult`](../StoreKit/verificationresult.md) as a convenience to access the signed value. (80701792)

#### Resolved Issues

- Fixed an issue where purchases performed in the Sandbox environment returned `VerificationResult.unverified(_:_:)`. (71949674)

#### Known Issues

- The [`unfinished`](../StoreKit/transaction/unfinished.md) property might return `VerificationResult<Transaction>` for transactions that have already finished. (81346114)

### Logging

#### Deprecations

- Support for cleartext HTTP URL schemes for Proxy Automatic Configuration (PAC) is now deprecated. Use only HTTPS URL schemes for PAC. This affects all PAC configurations, including, but not limited to, configurations set via Settings, System Preferences, profiles, and `URLSession` APIs such as [`connectionProxyDictionary`](../Foundation/urlsessionconfiguration/connectionproxydictionary.md) and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](../CFNetwork/cfnetworkexecuteproxyautoconfigurationurl%28_,_,_,_%29.md). If you configure a cleartext HTTP PAC URL, the system may upgrade it to HTTPS during PAC file loads. Web Proxy Auto-Discovery (WPAD) Protocol via DNS isn’t affected. Dynamic Host Configuration Protocol (DHCP) Option 252 WPAD may attempt to upgrade cleartext HTTP URLs to HTTPS during PAC file loads. (61981845)

### MapKit

#### Deprecations

- [`MKPinAnnotationView`](../MapKit/mkpinannotationview.md) and [`MapPin`](../MapKit/mappin.md) are deprecated in this beta. (78536295)

### Networking

#### New Features

- The default `Accept-Language` header that [`URLSession`](../Foundation/urlsession.md) sends has an updated format and corrected values for multiple locales. In addition to the preferred language, the header also includes the current system language as a fallback if it differs from the preferred language. This behavior affects apps that link against macOS 12, iOS 15, tvOS 15, and watchOS 8 SDKs. (38772422)

### SharePlay

#### Deprecations

- SharePlay development in beta 7 and upcoming beta releases requires the installation of an updated [SharePlay Development Profile](https://developer.apple.com/download/). This profile enables successful creation and reception of GroupSessions via the Group Activities API in iOS 15, iPadOS 15 and tvOS 15 beta 7, as well as macOS Monterey beta 6. (81816137)

### StoreKit

#### New Features

- [StoreKit](../StoreKit/StoreKit.md) 2 introduces a modern Swift-based API that takes advantage of new language features like Swift concurrency. Use this API to load product information, display in-app purchases in your store, allow customers to make purchases, manage access to content and subscriptions, and receive transaction information signed by the App Store in JSON Web Signature (JWS) format. (66587964)

### SwiftUI

#### New Features

- [`LocalizedStringKey`](../SwiftUI/localizedstringkey.md) can now contain Markdown syntax. The system parses Markdown strings when you create a [`Text`](../SwiftUI/text.md) view from a `LocalizedStringKey`, including `Text` views created with a string literal. The system styles `Text` according to Markdown constructs. (74515884)

- You can create [`Text`](../SwiftUI/text.md) from an [`AttributedString`](../Foundation/attributedstring.md) structure. `Text` respects the styles you provide through attributes within the SwiftUI attribute scope; these styles take precedence over styles you provide through view modifiers. (74841755)

- Specific kinds of animations now execute off the main thread, so there are new thread-safety requirements. (70524799) Ensure the following functions and types are thread-safe:

  - All methods and accessors of types conforming to these protocols: [`AlignmentID`](../SwiftUI/alignmentid.md), [`Animatable`](../SwiftUI/animatable.md), [`EnvironmentKey`](../SwiftUI/environmentkey.md), [`EnvironmentValues`](../SwiftUI/environmentvalues.md), [`Equatable`](../Swift/equatable.md), [`GeometryEffect`](../SwiftUI/geometryeffect.md), [`Hashable`](../Swift/hashable.md), [`Identifiable`](../Swift/identifiable.md), [`PreferenceKey`](../SwiftUI/preferencekey.md), [`Shape`](../SwiftUI/shape.md), [`VectorArithmetic`](../SwiftUI/vectorarithmetic.md).
  - Any closures you pass to the following types and functions, but only if the views that created them don’t have references to [`ObservableObject`](../Combine/observableobject.md) types: [`ForEach`](../SwiftUI/foreach.md), [`GeometryReader`](../SwiftUI/geometryreader.md), `backgroundPreferenceValue(_:_:)`, `overlayPreferenceValue(_:_:)`, `transformPreference(_:_:)`, `anchorPreference(key:value:transform:)`, `transformAnchorPreference(key:value:transform:)`, `transformEnvironment(_:transform:)`, `transaction(_:)`.

- A [`TextField`](../SwiftUI/textfield.md) provided an [`Formatter`](../Foundation/formatter.md) now updates its binding as the user types. `NSFormatter` formats the text of the field when the user submits the field, or when focus moves away from the field. (67899823)

- You can now initialize [`Text`](../SwiftUI/text.md) with a [`FormatStyle`](../Foundation/formatstyle.md). (72159423)

- While searching, if you tap a suggestion that uses the `searchCompletion(_:)` modifier, the suggestion list now disappears rather than displaying the single suggestion you selected. (76965399)

- Added `buttonBorderShape`, which can be used to control the shape of bordered buttons. (79456465)

- New [`AttributedString`](../Foundation/attributedstring.md) attributes [`underlineStyle`](../Foundation/attributescopes/swiftuiattributes/underlinestyle.md) and [`strikethroughStyle`](../Foundation/attributescopes/swiftuiattributes/strikethroughstyle.md) were added to [`AttributeScopes.SwiftUIAttributes`](../Foundation/attributescopes/swiftuiattributes.md). (78437803)

- Types conforming to the [`Animatable`](../SwiftUI/animatable.md) protocol and also conforming to either the [`View`](../SwiftUI/view.md) or [`ViewModifier`](../SwiftUI/viewmodifier.md) protocols now apply animations when their values change. Consequently, the [`AnimatableModifier`](../SwiftUI/animatablemodifier.md) protocol is soft-deprecated. Use `Animatable` directly when targeting the latest OS versions; for example, use `struct CustomModifier: ViewModifer, Animatable` rather than `struct CustomModifier: AnimatableModifier`. (76971100)

- The [`contentShape(_:eoFill:)`](../SwiftUI/view/contentshape%28_,eofill%29.md) modifier now allows fine-grained control over different kinds of shapes. For drag previews, hover effects, and context menus, the matching `ContentShapeKinds` is required to affect the shape of previews when linked on iOS 15.0 or newer. The default behavior is to set the `interaction` kind. (60792377)

The [`openURL`](../SwiftUI/environmentvalues/openurl.md) environment value can now be set and used to customize URL handling in the view hierarchy, including URL handling in [`Link`](../SwiftUI/link.md) views and links embedded in [`Text`](../SwiftUI/text.md) views. (78551237)

- [`Task`](../Swift/task.md) allows you to pass the priority to be used when spawning a new `Task`. (80599258)

- [`Text`](../SwiftUI/text.md) views that contain excessive line height characters now have a larger default size to avoid clipping or overlapping of oversized characters. (80665315)

#### Deprecations

- `controlProminence` is deprecated. Use the new `.borderedProminent` [`ButtonStyle`](../SwiftUI/buttonstyle.md) instead. (78908460)

### Xcode

#### Known Issues

- [MusicKit](../MusicKit/MusicKit.md) functionality, such as loading content with music requests, doesn’t work in simulated devices. (78559381)

  **Workaround**: Test your app’s `MusicKit` functionality on a physical device.

## See Also

### tvOS 15
- [tvOS 15.6 Release Notes](./tvos-15_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.5 Release Notes](./tvos-15_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.4 Release Notes](./tvos-15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.3 Release Notes](./tvos-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.2 Release Notes](./tvos-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.1 Release Notes](./tvos-15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-15-release-notes)*