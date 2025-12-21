# iOS & iPadOS 15 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 15 SDK provides support to develop apps for iPhone, iPad, and iPod touch devices running iOS & iPadOS 15. The SDK comes bundled with Xcode 13, available from the Mac App Store. For information on the compatibility requirements for Xcode 13, see [`Xcode 13 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-13-release-notes).

##### App Store

###### New Features

- [`StoreKit`](https://developer.apple.com/documentation/StoreKit) 2 introduces a modern Swift-based API that takes advantage of new language features like Swift concurrency. Use this API to load product information, display in-app purchases in your store, allow customers to make purchases, manage access to content and subscriptions, and receive transaction information signed by the App Store in JSON Web Signature (JWS) format. (66587964)

- The `request(with:)` type method on [`Product`](https://developer.apple.com/documentation/StoreKit/Product) is now renamed to [`products(for:)`](https://developer.apple.com/documentation/StoreKit/Product/products(for:)). (79410910)

- The [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction) `listener` type properties on [`Product.SubscriptionInfo.Status`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/Status-swift.struct) and [`Storefront`](https://developer.apple.com/documentation/StoreKit/Storefront) are now [`updates`](https://developer.apple.com/documentation/StoreKit/Transaction/updates) and [`updates`](https://developer.apple.com/documentation/StoreKit/Storefront/updates), respectively. The nested [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) conforming structures are now [`Transaction.Transactions`](https://developer.apple.com/documentation/StoreKit/Transaction/Transactions), [`Product.SubscriptionInfo.Status.Statuses`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/Status-swift.struct/Statuses), and [`Storefront.Storefronts`](https://developer.apple.com/documentation/StoreKit/Storefront/Storefronts). Both `TransactionSequence` and `TransactionListener` are now [`Transaction.Transactions`](https://developer.apple.com/documentation/StoreKit/Transaction/Transactions). (79034347)

- `StoreKitError.userDidNotAuthenticate` is no longer available; use [`StoreKitError.userCancelled`](https://developer.apple.com/documentation/StoreKit/StoreKitError/userCancelled) instead. (78270199)

- You can now access [`Product`](https://developer.apple.com/documentation/StoreKit/Product) raw JSON data for custom decoding: - Multiple [`Product.PurchaseOption`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption) methods are now allowed. `.custom(_:)` is replaced with several new type methods, namely [`custom(key:value:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/custom(key:value:)-80cvh), [`custom(key:value:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/custom(key:value:)-3g3nc), [`custom(key:value:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/custom(key:value:)-8tjim), and [`custom(key:value:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/custom(key:value:)-7rju9).
- Subscript operators on [`Product`](https://developer.apple.com/documentation/StoreKit/Product), [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction), and [`renewalInfo`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/Status-swift.struct/renewalInfo) are removed, along with the nested `Key` enumerations.
- `BackingValue` and extensions adding initializers from `BackingValue` are removed. (79101606)

- A new type property [`unfinished`](https://developer.apple.com/documentation/StoreKit/Transaction/unfinished) is now available on [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction) that returns signed information for any transactions where the app still needs to deliver content to the user. (79620896)

- A new [`onStorefrontChange(shouldContinuePurchase:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/onStorefrontChange(shouldContinuePurchase:)) is available in StoreKit 2. You can use this purchase option to determine whether the transaction continues if the App Store storefront changes during a transaction. The default is `true` if this option isn’t added. (70757789)

- `VerificationResult.unverified(SignedType)` is now `VerificationResult.unverified(SignedType, VerificationError)` to provide a reason for unverified signed values. [`jsonRepresentation`](https://developer.apple.com/documentation/StoreKit/Transaction/jsonRepresentation) is available on [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction) and [`jsonRepresentation`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo/jsonRepresentation) is available on [`renewalInfo`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/Status-swift.struct/renewalInfo); both properties provide the payload JSON as `Data`. [`payloadValue`](https://developer.apple.com/documentation/StoreKit/VerificationResult/payloadValue) and [`unsafePayloadValue`](https://developer.apple.com/documentation/StoreKit/VerificationResult/unsafePayloadValue) properties are available on [`VerificationResult`](https://developer.apple.com/documentation/StoreKit/VerificationResult) as a convenience to access the signed value. (80701792)

###### Resolved Issues

- Fixed an issue where purchases performed in the Sandbox environment returned `VerificationResult.unverified(_:_:)`. (71949674)

###### Known Issues

- The [`unfinished`](https://developer.apple.com/documentation/StoreKit/Transaction/unfinished) property might return `VerificationResult<Transaction>` for transactions that have already finished. (81346114)

##### Audio Units

###### New Features

- Audio Units now provides custom views that Audio Unit hosts can display in iOS. Use the [`providesUserInterface`](https://developer.apple.com/documentation/AudioToolbox/AUAudioUnit/providesUserInterface) property to determine if an [`AUAudioUnit`](https://developer.apple.com/documentation/AudioToolbox/AUAudioUnit) has a user interface. Use the [`requestViewController(completionHandler:)`](https://developer.apple.com/documentation/AudioToolbox/AUAudioUnit/requestViewController(completionHandler:)) method to get the [`AUViewController`](https://developer.apple.com/documentation/CoreAudioKit/AUViewController) for the [`view`](https://developer.apple.com/documentation/UIKit/UIViewController/view). The custom view supports setting the tint color of the view via the [`tintColor`](https://developer.apple.com/documentation/UIKit/UIView/tintColor) property. This can be used to set the color of the view to a different color for each track or to match the look of the app. (74183251)

##### Avfoundation

###### New Features

- iPadOS apps can now continue using the camera while presenting multiple windows and being the only application onscreen. (77522226)

###### Deprecations

- [`supportedPhotoPixelFormatTypes(for:)`](https://developer.apple.com/documentation/AVFoundation/AVCapturePhotoOutput/supportedPhotoPixelFormatTypes(for:)) and [`supportedRawPhotoPixelFormatTypes(for:)`](https://developer.apple.com/documentation/AVFoundation/AVCapturePhotoOutput/supportedRawPhotoPixelFormatTypes(for:)) now return `[OSType]` instead of `[NSNumber]` in Swift. (64822071)
- [`recommendedVideoSettings(forVideoCodecType:assetWriterOutputFileType:)`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput/recommendedVideoSettings(forVideoCodecType:assetWriterOutputFileType:)) now returns `nullable NSDictionary<NSString *, id> *` instead of `nullable NSDictionary *` in Objective-C and `[String: Any]?` instead of `[AnyHashable: Any]?` in Swift. (33784279)
- [`cgImageRepresentation()`](https://developer.apple.com/documentation/AVFoundation/AVCapturePhoto/cgImageRepresentation()) and [`previewCGImageRepresentation()`](https://developer.apple.com/documentation/AVFoundation/AVCapturePhoto/previewCGImageRepresentation()) now return `CGImage?` instead of `Unmanaged<CGImage>?` in Swift. (44734827)
- [`recommendedAudioSettingsForAssetWriter(writingTo:)`](https://developer.apple.com/documentation/AVFoundation/AVCaptureAudioDataOutput/recommendedAudioSettingsForAssetWriter(writingTo:)) now returns `nullable NSDictionary<NSString *, id> *` instead of `nullable NSDictionary *` in Objective-C and `[String: Any]?` instead of `[AnyHashable: Any]?` in Swift. (50450334)

##### Core Haptics

###### New Features

- Events of type [`audioContinuous`](https://developer.apple.com/documentation/CoreHaptics/CHHapticEvent/EventType/audioContinuous), [`hapticContinuous`](https://developer.apple.com/documentation/CoreHaptics/CHHapticEvent/EventType/hapticContinuous), and [`audioCustom`](https://developer.apple.com/documentation/CoreHaptics/CHHapticEvent/EventType/audioCustom) now resume playback mid-event if a paused [`CHHapticAdvancedPatternPlayer`](https://developer.apple.com/documentation/CoreHaptics/CHHapticAdvancedPatternPlayer) resumes. These events don’t begin mid-event if [`seek(toOffset:)`](https://developer.apple.com/documentation/CoreHaptics/CHHapticAdvancedPatternPlayer/seek(toOffset:)) starts the player at a specific time offset. (29274583)
- You can now control whether to apply a volume envelope to [`type`](https://developer.apple.com/documentation/CoreHaptics/CHHapticEvent/type) resources. By default, these resources play back with a built-in volume envelope that ramps the signal in at the beginning and ramps out at the end, to avoid clicks. (75491090) You can apply a volume envelope in one of the following ways: - If you’re importing custom audio assets by registering audio resource IDs for them, you can specify this behavior via a new key value argument, [`CHHapticAudioResourceKeyUseVolumeEnvelope`](https://developer.apple.com/documentation/CoreHaptics/CHHapticAudioResourceKeyUseVolumeEnvelope), that the system passes to [`registerAudioResource(_:options:)`](https://developer.apple.com/documentation/CoreHaptics/CHHapticEngine/registerAudioResource(_:options:)).
- If you’re referencing audio assets using an AHAP file or the [`init(dictionary:)`](https://developer.apple.com/documentation/CoreHaptics/CHHapticPattern/init(dictionary:)) of [`CHHapticPattern`](https://developer.apple.com/documentation/CoreHaptics/CHHapticPattern), you can control this behavior with the `CHHapticPatternKeyEventWaveformUseVolumeEnvelope` pattern key.

##### Core Ml

###### Known Issues

- In automatic reference counting (ARC) mode, the compiler may extend the lifetime of `MLMultiArray` longer than expected when the `.dataPointer` property is used. This may increase memory usage. (80895213)  Enclose `.dataPointer` access in an `@autoreleasepool {... }` block.

##### Create Ml

###### New Features

- The [`Create ML`](https://developer.apple.com/documentation/CreateML) framework is now available in iOS & iPadOS 15, unlocking new opportunities for building dynamic app experiences that leverage on-device ML. Task-focused APIs for image classification, sound classification, text classification, and hand pose and hand action classification are available, along with APIs for classical tabular classification and regression. (37087332)

- The Audio Feature Print-based [`MLSoundClassifier`](https://developer.apple.com/documentation/CreateML/MLSoundClassifier) algorithm trains sound classifier models faster, with higher accuracy, lower latency, and a smaller model size. This algorithm is now the default option for the `MLSoundClassifier` in Create ML. (70106630)

##### Debugging

###### Known Issues

- Using dispatch semaphores in an iOS app running in a device simulator on a Mac with Apple silicon running macOS 11 causes the app to crash. (81783378)  In Xcode, select Product > Scheme > Edit Scheme, then deselect Run > Options > Queue Debugging > “Enable backtrace recording.”

##### Find My

###### Known Issues

- When your iOS device needs to be charged, text indicating that the Find My network is active only displays if the device language is set to English. (78547946)

##### Guided Access

###### Known Issues

- When using Guided Access with VoiceOver, you might be unable to enter the Guided Access passcode to end Guided Access. (79370792)  If a device passcode is set, force restart your device to end Guided Access.

##### Home

###### Known Issues

- You can’t pair with Matter accessories that use Thread. (80991829)
- You can’t pair a third-party app with Matter accessories through the app paring flow if the accessory is already paired with another app. (80059432)  Remove accessory pairing from other apps, then pair the third-party app.
- You can’t add a flow to a third-party app with Matter accessories if you haven’t created an Apple Home. (80058744)  Launch the Home app to create a Home before you add a flow.
- Matter accessories aren’t reachable while Apple TV is connected via Wi-Fi. (79582629)  Connect Apple TV via Ethernet.
- Matter accessories might enter a No Response state after pairing. (76019163)  Remove the accessory from Home, reset the accessory, and add it back to Home. If the issue persists, remove your Home hub from Home and re-add it. If the issue still persists, remove the home and create a new one.
- The initial pairing attempt with a Matter accessory might take an unexpectedly long time and eventually fail. (77967587)  Retry pairing the accessory.
- You can only pair up to five Matter accessories in a home. (77967671)
- Only the owner of a home, not an invited user, can pair Matter accessories. (76012945)

##### Home Screen

###### Known Issues

- After canceling a search in the widget gallery, the cancel button remains visible, which might blank out the widget gallery. (78572049)  Dismiss and reopen the widget gallery.

##### Icloud

###### New Features

- iCloud Private Relay will be released as a public beta to gather additional feedback and improve website compatibility. (82150385)

###### Known Issues

- Legacy Contacts has been removed from iOS & iPadOS 15 beta 5 and will return in a future release. (81292885)

- Custom Email Domain addresses with delimiters like “+” or “-” can’t be configured. (82425376)

- Custom Email Domain addresses that are associated with a separate iTunes account can’t be configured. (82358431)

- Some accounts may not yet be eligible for Custom Email Domain. (82421769)

##### Foundation

###### New Features

- [`Foundation`](https://developer.apple.com/documentation/Foundation) now includes an automatic grammar agreement engine. This simplifies your code and reduces the number of localized strings you provide by automatically inflecting localized strings to account for pluralization, grammatical gender agreement, and agreement with the user’s term of address. It’s available for English and Spanish. (70210115)
- Formatting APIs are now available, which focus on the format and remove the need to create, configure, and cache a formatter instance. Each [`Formatter`](https://developer.apple.com/documentation/Foundation/Formatter) type has a `formatted` function. These functions have arguments that allow for configuration and customization of the style. (70220307)
- [`JSONSerialization`](https://developer.apple.com/documentation/Foundation/JSONSerialization) and [`JSONDecoder`](https://developer.apple.com/documentation/Foundation/JSONDecoder) now support decoding from JSON5. (73954652)
- [`SortDescriptor`](https://developer.apple.com/documentation/Foundation/SortDescriptor), [`KeyPathComparator`](https://developer.apple.com/documentation/Foundation/KeyPathComparator), and [`SortComparator`](https://developer.apple.com/documentation/Foundation/SortComparator) APIs provide a Swift interface to express archivable rules for sorting values. (74264359)

##### Logging

###### New Features

- [`os_signpost(_:dso:log:name:signpostID:)`](https://developer.apple.com/documentation/os/os_signpost(_:dso:log:name:signpostID:)-2oz8u) from Swift is part of the framework OS on all platforms: - Instantiate [`OSSignposter`](https://developer.apple.com/documentation/os/OSSignposter) using a subsystem and category, an existing [`OSLog`](https://developer.apple.com/documentation/OSLog) object, or an existing [`Logger`](https://developer.apple.com/documentation/os/Logger) object.
- The OSSignposter API provides methods for emitting signposts. [`beginInterval(_:id:)`](https://developer.apple.com/documentation/os/OSSignposter/beginInterval(_:id:)) emits `begin` signposts, [`endInterval(_:_:)`](https://developer.apple.com/documentation/os/OSSignposter/endInterval(_:_:)) emits `end` signposts, and [`emitEvent(_:id:)`](https://developer.apple.com/documentation/os/OSSignposter/emitEvent(_:id:)) emits `event` signposts. These replace the existing `os_signpost` calls based on `String` and `varargs`.
- The APIs support `String` interpolations for the metadata parameter. The `String` interpolations are the same as those accepted by the [`Logger APIs`](https://developer.apple.comhttps://developer.apple.com/documentation/os/osloginterpolation).
- The OSSignposter API supports all formatting and privacy options — previously offered by the `os_signpost` functions — and follows the same syntax as the Logger APIs.
- The APIs provide performance improvements over the legacy APIs.
- The `OSSignposter type` provides a new scoped API for surrounding a block of code by `begin` and `end` signposts, [`withIntervalSignpost(_:id:_:around:)`](https://developer.apple.com/documentation/os/OSSignposter/withIntervalSignpost(_:id:_:around:)).  These APIs are unavailable in iOS 14 and iPadOS 14 and earlier; however, the existing `os_signpost` API remains available. (54756831)

##### Maps

###### Known Issues

- Rounded building corners might disappear. (80468151)

###### Deprecations

- [`MKPinAnnotationView`](https://developer.apple.com/documentation/MapKit/MKPinAnnotationView) and [`MapPin`](https://developer.apple.com/documentation/MapKit/MapPin) are marked as deprecated in this beta. (78536295)

##### Networking

###### New Features

- The default `Accept-Language` header that [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) sends has an updated format and corrected values for multiple locales. In addition to the preferred language, the header also includes the current system language as a fallback if it differs from the preferred language. This behavior affects apps that link against macOS 12, iOS 15, tvOS 15, and watchOS 8 SDKs. (38772422)
- `URLSession` now includes `async` functions. (68890254) For example, a one-shot fetch: ```swift
let (data, response) = try await URLSession.shared.data(from: URL(string: "https://www.apple.com")!)
if let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 {
   // Use data.
}
``` And support for an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) stream of bytes: ```swift
let (bytes, response) = try await URLSession.shared.bytes(with: URL(string: "https://www.apple.com")!)
if let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 {
    for try await line in bytes.lines() {
        // Parse line.
    }
}
```

###### Deprecations

- Support for cleartext HTTP URL schemes for Proxy Automatic Configuration (PAC) is now deprecated. Use only HTTPS URL schemes for PAC. This affects all PAC configurations, including, but not limited to, configurations set via Settings, System Preferences, profiles, and `URLSession` APIs such as [`connectionProxyDictionary`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/connectionProxyDictionary) and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](https://developer.apple.com/documentation/CFNetwork/CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)). If you configure a cleartext HTTP PAC URL, the system may upgrade it to HTTPS during PAC file loads. Web Proxy Auto-Discovery (WPAD) Protocol via DNS isn’t affected. Dynamic Host Configuration Protocol (DHCP) Option 252 WPAD may attempt to upgrade cleartext HTTP URLs to HTTPS during PAC file loads. (61981845)

##### Privacy

###### New Features

- To download a file that shows the app content in the App Privacy Report, choose Settings > Privacy > Record App Activity. (77758720)

##### Reality Composer

###### Known Issues

- You might be unable to create new projects in Reality Composer. (79418400)  Create a new project in Reality Composer on macOS and transfer the `.rcproject` file to your device via AirDrop or Mail.

##### Safari

###### New Features

- The bottom tab bar is redesigned to appear below page content. An option to show the address bar at the top is also available. (81118141)

###### Known Issues

- When tapping in an input field in a Safari Web Extension popover on iPhone, the Extension UI might not move upward to make room for the keyboard. (81676564)

##### Shareplay

###### Deprecations

- SharePlay development in beta 7 and upcoming beta releases requires the installation of an updated [`SharePlay Development Profile`](https://developer.apple.comhttps://developer.apple.com/download/). This profile enables successful creation and reception of GroupSessions via the Group Activities API in iOS 15, iPadOS 15 and tvOS 15 beta 7, as well as macOS Monterey beta 6. (81816137)

##### Shazamkit

###### Known Issues

- Media items added to the default instance of [`SHMediaLibrary`](https://developer.apple.com/documentation/ShazamKit/SHMediaLibrary) don’t appear in Shazam. (77785557)  Touch and hold the Music Recognition Control Center module to view [`SHMediaLibrary`](https://developer.apple.com/documentation/ShazamKit/SHMediaLibrary) contents.

##### Siri

###### Known Issues

- VoiceOver and Spoken Content users might not initially see all available voice options. Voice options should populate after some time. (79463000)
- On-device speech recognition only supports the following languages: Chinese (Mandarin - China mainland), English (Australia), English (Canada), English (United Kingdom), and English (US). (78483609)

##### Skadnetwork

###### New Features

- If a developer opts-in to receive the winning postback, devices can now send a copy of the winning postback to the advertised app’s developer. (75054513)

##### Swift

###### New Features

- A new Swift value type [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString) is now available with the same character-counting behavior as a Swift string. It’s fully localizable, and also includes support for Markdown, Codable, strongly typed attributes, and more. (27227292)
- [`NotificationCenter`](https://developer.apple.com/documentation/Foundation/NotificationCenter) includes a new [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) API for receiving notifications using async/await. (74401384) ```swift
for await note in NotificationCenter.default.notifications(named: .MyNote) {
    // Use note.
}
```

###### Known Issues

- Swift libraries depending on Combine may fail to build for targets including ARMv7 and i386 architectures. (82183186, 82189214)  Use an updated version of the library that isn’t impacted (if available) or remove ARMv7 and i386 support (for example, increase the deployment target of the library to iOS 11 or higher).

- Applications linking to RealityKit with the iOS 15 or macOS 12 SDKs will fail to launch on a previous OS. (79584511)  Add `OTHER_LD_FLAGS = -weak_framework RealityFoundation` to your Xcode Project settings to allow running RealityKit apps on an older OS.

##### Settings

###### Known Issues

- While the Sound Actions feature work as part of Switch Control, sounds aren’t detected in the area marked Practice in Settings app. (82411537)

##### Swiftui

###### New Features

- [`LocalizedStringKey`](https://developer.apple.com/documentation/SwiftUI/LocalizedStringKey) can now contain Markdown syntax. The system parses Markdown strings when you create a [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) view from a `LocalizedStringKey`, including `Text` views created with a string literal. The system styles `Text` according to Markdown constructs. (74515884)

- You can create [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) from an [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString) structure. `Text` respects the styles you provide through attributes within the SwiftUI attribute scope; these styles take precedence over styles you provide through view modifiers. (74841755)

- Specific kinds of animations now execute off the main thread, so there are new thread-safety requirements. (70524799) Ensure the following functions and types are thread-safe: - All methods and accessors of types conforming to the protocols [`AlignmentID`](https://developer.apple.com/documentation/SwiftUI/AlignmentID), [`Animatable`](https://developer.apple.com/documentation/SwiftUI/Animatable), [`EnvironmentKey`](https://developer.apple.com/documentation/SwiftUI/EnvironmentKey), [`EnvironmentValues`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues), [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable), [`GeometryEffect`](https://developer.apple.com/documentation/SwiftUI/GeometryEffect), [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable), [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable), [`PreferenceKey`](https://developer.apple.com/documentation/SwiftUI/PreferenceKey), [`Shape`](https://developer.apple.com/documentation/SwiftUI/Shape), [`VectorArithmetic`](https://developer.apple.com/documentation/SwiftUI/VectorArithmetic).
- Any closures you pass to the following types and functions, but only if the views that created them don’t have references to [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) types: [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach), [`GeometryReader`](https://developer.apple.com/documentation/SwiftUI/GeometryReader), [`backgroundPreferenceValue(_:_:)`](https://developer.apple.com/documentation/SwiftUI/View/backgroundPreferenceValue(_:_:)), [`overlayPreferenceValue(_:_:)`](https://developer.apple.com/documentation/SwiftUI/View/overlayPreferenceValue(_:_:)), [`transformPreference(_:_:)`](https://developer.apple.com/documentation/SwiftUI/View/transformPreference(_:_:)), [`anchorPreference(key:value:transform:)`](https://developer.apple.com/documentation/SwiftUI/View/anchorPreference(key:value:transform:)), [`transformAnchorPreference(key:value:transform:)`](https://developer.apple.com/documentation/SwiftUI/View/transformAnchorPreference(key:value:transform:)), [`transformEnvironment(_:transform:)`](https://developer.apple.com/documentation/SwiftUI/View/transformEnvironment(_:transform:)), [`transaction(_:)`](https://developer.apple.com/documentation/SwiftUI/View/transaction(_:)).

- A [`TextField`](https://developer.apple.com/documentation/SwiftUI/TextField) provided an [`Formatter`](https://developer.apple.com/documentation/Foundation/Formatter) now updates its binding as the user types. `NSFormatter` formats the text of the field when the user submits the field, or when focus moves away from the field. (67899823)
- A [`DisclosureGroup`](https://developer.apple.com/documentation/SwiftUI/DisclosureGroup) now toggles its expansion when tapping the row. (62208702)
- The default [`ListStyle`](https://developer.apple.com/documentation/SwiftUI/ListStyle) is now [`insetGrouped`](https://developer.apple.com/documentation/SwiftUI/ListStyle/insetGrouped). (75072988)
- [`TextField`](https://developer.apple.com/documentation/SwiftUI/TextField) labels don’t appear next to the field in a form. Use the `prompt` parameter to specify an explicit placeholder for the field. (61260160)

- You can now initialize [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) with a [`FormatStyle`](https://developer.apple.com/documentation/Foundation/FormatStyle). (72159423)

- While searching, if you tap a suggestion that uses the [`searchCompletion(_:)`](https://developer.apple.com/documentation/SwiftUI/View/searchCompletion(_:)) modifier, the suggestion list now disappears rather than displaying the single suggestion you selected. (76965399)

- You can now customize the prompt of a search field that a searchable modifier configures using the `prompt` parameter instead of the previous `title` parameter. (77988967)
- SwiftUI now supports `textSelection` modifiers. (77827592)

- Added `buttonBorderShape`, which can be used to control the shape of bordered buttons. (79456465)

- Added new [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString) attributes [`underlineStyle`](https://developer.apple.com/documentation/Foundation/AttributeScopes/SwiftUIAttributes/underlineStyle) and [`strikethroughStyle`](https://developer.apple.com/documentation/Foundation/AttributeScopes/SwiftUIAttributes/strikethroughStyle) to [`AttributeScopes.SwiftUIAttributes`](https://developer.apple.com/documentation/Foundation/AttributeScopes/SwiftUIAttributes). (78437803)

- Types conforming to the [`Animatable`](https://developer.apple.com/documentation/SwiftUI/Animatable) protocol and also conforming to either the [`View`](https://developer.apple.com/documentation/SwiftUI/View) or [`ViewModifier`](https://developer.apple.com/documentation/SwiftUI/ViewModifier) protocols now apply animations when their values change. Consequently, the [`AnimatableModifier`](https://developer.apple.com/documentation/SwiftUI/AnimatableModifier) protocol is soft-deprecated. Use `Animatable` directly when targeting the latest OS versions; for example, use `struct CustomModifier: ViewModifer, Animatable` rather than `struct CustomModifier: AnimatableModifier`. (76971100)

- The [`contentShape(_:eoFill:)`](https://developer.apple.com/documentation/SwiftUI/View/contentShape(_:eoFill:)) modifier now allows fine-grained control over different kinds of shapes. For drag previews, hover effects, and context menus, the matching `ContentShapeKinds` is required to affect the shape of previews when linked on iOS 15.0 or newer. The default behavior is to set the `interaction` kind. (60792377)

- The [`openURL`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/openURL) environment value can now be set and used to customize URL handling in the view hierarchy, including URL handling in [`Link`](https://developer.apple.com/documentation/SwiftUI/Link) views and links embedded in [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) views. (78551237)

- [`Task`](https://developer.apple.com/documentation/Swift/Task) allows you to pass the priority to be used when spawning a new `Task`. (80599258)

- [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) views that contain excessive line height characters now have a larger default size to avoid clipping or overlapping of oversized characters. (80665315)
- A [`NavigationLink`](https://developer.apple.com/documentation/SwiftUI/NavigationLink) in a sidebar on iPad that uses `isDetailLink(false)` correctly pushes onto the sidebar rather than the detail area. (80919171)

###### Known Issues

- Providing a binding to an [`OutlineGroup`](https://developer.apple.com/documentation/SwiftUI/OutlineGroup) might require including [`wrappedValue`](https://developer.apple.com/documentation/SwiftUI/Binding/wrappedValue) in the [`init(_:children:content:)`](https://developer.apple.com/documentation/SwiftUI/OutlineGroup/init(_:children:content:)-2galq) key path parameter, and isn’t available in iOS & iPadOS 14 and earlier. (77890799)

- Focusing a view in a newly added [`List`](https://developer.apple.com/documentation/SwiftUI/List) row using [`FocusState`](https://developer.apple.com/documentation/SwiftUI/FocusState) requires deferring the focus state property update to the next time the main runloop runs. (78607356)
- [`List`](https://developer.apple.com/documentation/SwiftUI/List) no longer respects SwiftUI’s safe area insets. (82295913)

###### Deprecations

- `controlProminence` is deprecated. Use the new `.borderedProminent` [`ButtonStyle`](https://developer.apple.com/documentation/SwiftUI/ButtonStyle) instead. (78908460)

- The Function (`Fn`) shortcut modifier is deprecated and reserved for system usage. (78627099)

##### Tabulardata

###### New Features

- [`TabularData`](https://developer.apple.com/documentation/TabularData) is a new Swift framework you use to analyze and manipulate tabular data. You can use [`DataFrame`](https://developer.apple.com/documentation/TabularData/DataFrame) to read CSV and JSON files, as well as join, group, and aggregate data. (69982458)

##### Uikit

###### New Features

- For apps compiled against the iOS 15 beta SDK, key commands no longer intercept text input and text editing commands while typing into text views and text fields. For example, pressing the Delete key always deletes a character and doesn’t trigger a Delete key command if one is present. To have a key command intercept text input, set the [`wantsPriorityOverSystemBehavior`](https://developer.apple.com/documentation/UIKit/UIKeyCommand/wantsPriorityOverSystemBehavior) property to `true` on the key command. This is also required to have key commands take priority over focus keyboard navigation commands, such as arrow and tab key presses. (55118263)
- In iOS 14 and iPadOS 14 and earlier, when [`autocorrectionType`](https://developer.apple.com/documentation/UIKit/UITextInputTraits/autocorrectionType) is set to [`UITextAutocorrectionType.no`](https://developer.apple.com/documentation/UIKit/UITextAutocorrectionType/no), the QuickType bar is disabled. For apps linked against iOS 15 and iPadOS 15 or later, the QuickType bar is enabled and shows spellchecking candidates. If the new behavior isn’t desirable for your use case, set [`spellCheckingType`](https://developer.apple.com/documentation/UIKit/UITextInputTraits/spellCheckingType) to [`UITextSpellCheckingType.no`](https://developer.apple.com/documentation/UIKit/UITextSpellCheckingType/no) to hide the QuickType bar. (68874861)
- When compiling with the iOS 15 beta SDK, several key window-related properties, methods, and notifications change behavior: - [`isKeyWindow`](https://developer.apple.com/documentation/UIKit/UIWindow/isKeyWindow) returns `true` if the window is key in its scene instead of the app.
- [`becomeKey()`](https://developer.apple.com/documentation/UIKit/UIWindow/becomeKey()) is called when the window becomes key in its scene instead of the app.
- [`didBecomeKeyNotification`](https://developer.apple.com/documentation/UIKit/UIWindow/didBecomeKeyNotification) posts when the window becomes key in its scene instead of the app.
- [`resignKey()`](https://developer.apple.com/documentation/UIKit/UIWindow/resignKey()) is called when the window resigns key window status in its scene instead of the app.
- [`didResignKeyNotification`](https://developer.apple.com/documentation/UIKit/UIWindow/didResignKeyNotification) posts when the window resigns key window status in its scene instead of the app. (72873846)

##### Xcode

###### Known Issues

- [`MusicKit`](https://developer.apple.com/documentation/MusicKit) functionality, such as loading content with music requests, doesn’t work in simulated devices. (78559381)

## See Also

- [iOS & iPadOS 15.6 Release Notes](ios-ipados-15_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.5 Release Notes](ios-ipados-15_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.4 Release Notes](ios-ipados-15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.3 Release Notes](ios-ipados-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.2 Release Notes](ios-ipados-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.1 Release Notes](ios-ipados-15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes)*