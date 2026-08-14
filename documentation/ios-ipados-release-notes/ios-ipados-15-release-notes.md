# iOS & iPadOS 15 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 15 SDK provides support to develop apps for iPhone, iPad, and iPod touch devices running iOS & iPadOS 15. The SDK comes bundled with Xcode 13, available from the Mac App Store. For information on the compatibility requirements for Xcode 13, see [`Xcode 13 Release Notes`](https://developer.apple.com/documentation/xcode-release-notes/xcode-13-release-notes).

##### App Store

###### New Features

- [`StoreKit`](https://developer.apple.com/documentation/storekit) 2 introduces a modern Swift-based API that takes advantage of new language features like Swift concurrency. Use this API to load product information, display in-app purchases in your store, allow customers to make purchases, manage access to content and subscriptions, and receive transaction information signed by the App Store in JSON Web Signature (JWS) format. (66587964)

- The `request(with:)` type method on [`Product`](https://developer.apple.com/documentation/storekit/product) is now renamed to [`products(for:)`](https://developer.apple.com/documentation/storekit/product/products(for:)). (79410910)

- The [`Transaction`](https://developer.apple.com/documentation/storekit/transaction) `listener` type properties on [`Product.SubscriptionInfo.Status`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct) and [`Storefront`](https://developer.apple.com/documentation/storekit/storefront) are now [`updates`](https://developer.apple.com/documentation/storekit/transaction/updates) and [`updates`](https://developer.apple.com/documentation/storekit/storefront/updates), respectively. The nested [`AsyncSequence`](https://developer.apple.com/documentation/swift/asyncsequence) conforming structures are now [`Transaction.Transactions`](https://developer.apple.com/documentation/storekit/transaction/transactions), [`Product.SubscriptionInfo.Status.Statuses`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/statuses), and [`Storefront.Storefronts`](https://developer.apple.com/documentation/storekit/storefront/storefronts). Both `TransactionSequence` and `TransactionListener` are now [`Transaction.Transactions`](https://developer.apple.com/documentation/storekit/transaction/transactions). (79034347)

- `StoreKitError.userDidNotAuthenticate` is no longer available; use [`StoreKitError.userCancelled`](https://developer.apple.com/documentation/storekit/storekiterror/usercancelled) instead. (78270199)

- You can now access [`Product`](https://developer.apple.com/documentation/storekit/product) raw JSON data for custom decoding: - Multiple [`Product.PurchaseOption`](https://developer.apple.com/documentation/storekit/product/purchaseoption) methods are now allowed. `.custom(_:)` is replaced with several new type methods, namely [`custom(key:value:)`](https://developer.apple.com/documentation/storekit/product/purchaseoption/custom(key:value:)-80cvh), [`custom(key:value:)`](https://developer.apple.com/documentation/storekit/product/purchaseoption/custom(key:value:)-3g3nc), [`custom(key:value:)`](https://developer.apple.com/documentation/storekit/product/purchaseoption/custom(key:value:)-8tjim), and [`custom(key:value:)`](https://developer.apple.com/documentation/storekit/product/purchaseoption/custom(key:value:)-7rju9).
- Subscript operators on [`Product`](https://developer.apple.com/documentation/storekit/product), [`Transaction`](https://developer.apple.com/documentation/storekit/transaction), and [`renewalInfo`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/renewalinfo) are removed, along with the nested `Key` enumerations.
- `BackingValue` and extensions adding initializers from `BackingValue` are removed. (79101606)

- A new type property [`unfinished`](https://developer.apple.com/documentation/storekit/transaction/unfinished) is now available on [`Transaction`](https://developer.apple.com/documentation/storekit/transaction) that returns signed information for any transactions where the app still needs to deliver content to the user. (79620896)

- A new [`onStorefrontChange(shouldContinuePurchase:)`](https://developer.apple.com/documentation/storekit/product/purchaseoption/onstorefrontchange(shouldcontinuepurchase:)) is available in StoreKit 2. You can use this purchase option to determine whether the transaction continues if the App Store storefront changes during a transaction. The default is `true` if this option isn’t added. (70757789)

- `VerificationResult.unverified(SignedType)` is now `VerificationResult.unverified(SignedType, VerificationError)` to provide a reason for unverified signed values. [`jsonRepresentation`](https://developer.apple.com/documentation/storekit/transaction/jsonrepresentation) is available on [`Transaction`](https://developer.apple.com/documentation/storekit/transaction) and [`jsonRepresentation`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/jsonrepresentation) is available on [`renewalInfo`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/renewalinfo); both properties provide the payload JSON as `Data`. [`payloadValue`](https://developer.apple.com/documentation/storekit/verificationresult/payloadvalue) and [`unsafePayloadValue`](https://developer.apple.com/documentation/storekit/verificationresult/unsafepayloadvalue) properties are available on [`VerificationResult`](https://developer.apple.com/documentation/storekit/verificationresult) as a convenience to access the signed value. (80701792)

###### Resolved Issues

- Fixed an issue where purchases performed in the Sandbox environment returned `VerificationResult.unverified(_:_:)`. (71949674)

###### Known Issues

- The [`unfinished`](https://developer.apple.com/documentation/storekit/transaction/unfinished) property might return `VerificationResult<Transaction>` for transactions that have already finished. (81346114)

##### Audio Units

###### New Features

- Audio Units now provides custom views that Audio Unit hosts can display in iOS. Use the [`providesUserInterface`](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/providesuserinterface) property to determine if an [`AUAudioUnit`](https://developer.apple.com/documentation/audiotoolbox/auaudiounit) has a user interface. Use the [`requestViewController(completionHandler:)`](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/requestviewcontroller(completionhandler:)) method to get the [`AUViewController`](https://developer.apple.com/documentation/coreaudiokit/auviewcontroller) for the [`view`](https://developer.apple.com/documentation/uikit/uiviewcontroller/view). The custom view supports setting the tint color of the view via the [`tintColor`](https://developer.apple.com/documentation/uikit/uiview/tintcolor) property. This can be used to set the color of the view to a different color for each track or to match the look of the app. (74183251)

##### Avfoundation

###### New Features

- iPadOS apps can now continue using the camera while presenting multiple windows and being the only application onscreen. (77522226)

###### Deprecations

- [`supportedPhotoPixelFormatTypes(for:)`](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/supportedphotopixelformattypes(for:)) and [`supportedRawPhotoPixelFormatTypes(for:)`](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/supportedrawphotopixelformattypes(for:)) now return `[OSType]` instead of `[NSNumber]` in Swift. (64822071)
- [`recommendedVideoSettings(forVideoCodecType:assetWriterOutputFileType:)`](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:)) now returns `nullable NSDictionary<NSString *, id> *` instead of `nullable NSDictionary *` in Objective-C and `[String: Any]?` instead of `[AnyHashable: Any]?` in Swift. (33784279)
- [`cgImageRepresentation()`](https://developer.apple.com/documentation/avfoundation/avcapturephoto/cgimagerepresentation()) and [`previewCGImageRepresentation()`](https://developer.apple.com/documentation/avfoundation/avcapturephoto/previewcgimagerepresentation()) now return `CGImage?` instead of `Unmanaged<CGImage>?` in Swift. (44734827)
- [`recommendedAudioSettingsForAssetWriter(writingTo:)`](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/recommendedaudiosettingsforassetwriter(writingto:)) now returns `nullable NSDictionary<NSString *, id> *` instead of `nullable NSDictionary *` in Objective-C and `[String: Any]?` instead of `[AnyHashable: Any]?` in Swift. (50450334)

##### Core Haptics

###### New Features

- Events of type [`audioContinuous`](https://developer.apple.com/documentation/corehaptics/chhapticevent/eventtype/audiocontinuous), [`hapticContinuous`](https://developer.apple.com/documentation/corehaptics/chhapticevent/eventtype/hapticcontinuous), and [`audioCustom`](https://developer.apple.com/documentation/corehaptics/chhapticevent/eventtype/audiocustom) now resume playback mid-event if a paused [`CHHapticAdvancedPatternPlayer`](https://developer.apple.com/documentation/corehaptics/chhapticadvancedpatternplayer) resumes. These events don’t begin mid-event if [`seek(toOffset:)`](https://developer.apple.com/documentation/corehaptics/chhapticadvancedpatternplayer/seek(tooffset:)) starts the player at a specific time offset. (29274583)
- You can now control whether to apply a volume envelope to [`type`](https://developer.apple.com/documentation/corehaptics/chhapticevent/type) resources. By default, these resources play back with a built-in volume envelope that ramps the signal in at the beginning and ramps out at the end, to avoid clicks. (75491090) You can apply a volume envelope in one of the following ways: - If you’re importing custom audio assets by registering audio resource IDs for them, you can specify this behavior via a new key value argument, [`CHHapticAudioResourceKeyUseVolumeEnvelope`](https://developer.apple.com/documentation/corehaptics/chhapticaudioresourcekeyusevolumeenvelope), that the system passes to [`registerAudioResource(_:options:)`](https://developer.apple.com/documentation/corehaptics/chhapticengine/registeraudioresource(_:options:)).
- If you’re referencing audio assets using an AHAP file or the [`init(dictionary:)`](https://developer.apple.com/documentation/corehaptics/chhapticpattern/init(dictionary:)) of [`CHHapticPattern`](https://developer.apple.com/documentation/corehaptics/chhapticpattern), you can control this behavior with the `CHHapticPatternKeyEventWaveformUseVolumeEnvelope` pattern key.

##### Core Ml

###### Known Issues

- In automatic reference counting (ARC) mode, the compiler may extend the lifetime of `MLMultiArray` longer than expected when the `.dataPointer` property is used. This may increase memory usage. (80895213) **Workaround:** Enclose `.dataPointer` access in an `@autoreleasepool {... }` block.

##### Create Ml

###### New Features

- The [`Create ML`](https://developer.apple.com/documentation/createml) framework is now available in iOS & iPadOS 15, unlocking new opportunities for building dynamic app experiences that leverage on-device ML. Task-focused APIs for image classification, sound classification, text classification, and hand pose and hand action classification are available, along with APIs for classical tabular classification and regression. (37087332)

- The Audio Feature Print-based [`MLSoundClassifier`](https://developer.apple.com/documentation/createml/mlsoundclassifier) algorithm trains sound classifier models faster, with higher accuracy, lower latency, and a smaller model size. This algorithm is now the default option for the `MLSoundClassifier` in Create ML. (70106630)

##### Debugging

###### Known Issues

- Using dispatch semaphores in an iOS app running in a device simulator on a Mac with Apple silicon running macOS 11 causes the app to crash. (81783378) **Workaround:** In Xcode, select Product > Scheme > Edit Scheme, then deselect Run > Options > Queue Debugging > “Enable backtrace recording.”

##### Find My

###### Known Issues

- When your iOS device needs to be charged, text indicating that the Find My network is active only displays if the device language is set to English. (78547946)

##### Guided Access

###### Known Issues

- When using Guided Access with VoiceOver, you might be unable to enter the Guided Access passcode to end Guided Access. (79370792) **Workaround:** If a device passcode is set, force restart your device to end Guided Access.

##### Home

###### Known Issues

- You can’t pair with Matter accessories that use Thread. (80991829)
- You can’t pair a third-party app with Matter accessories through the app paring flow if the accessory is already paired with another app. (80059432) **Workaround:** Remove accessory pairing from other apps, then pair the third-party app.
- You can’t add a flow to a third-party app with Matter accessories if you haven’t created an Apple Home. (80058744) **Workaround:** Launch the Home app to create a Home before you add a flow.
- Matter accessories aren’t reachable while Apple TV is connected via Wi-Fi. (79582629) **Workaround:** Connect Apple TV via Ethernet.
- Matter accessories might enter a No Response state after pairing. (76019163) **Workaround:** Remove the accessory from Home, reset the accessory, and add it back to Home. If the issue persists, remove your Home hub from Home and re-add it. If the issue still persists, remove the home and create a new one.
- The initial pairing attempt with a Matter accessory might take an unexpectedly long time and eventually fail. (77967587) **Workaround:** Retry pairing the accessory.
- You can only pair up to five Matter accessories in a home. (77967671)
- Only the owner of a home, not an invited user, can pair Matter accessories. (76012945)

##### Home Screen

###### Known Issues

- After canceling a search in the widget gallery, the cancel button remains visible, which might blank out the widget gallery. (78572049) **Workaround:** Dismiss and reopen the widget gallery.

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

- [`Foundation`](https://developer.apple.com/documentation/foundation) now includes an automatic grammar agreement engine. This simplifies your code and reduces the number of localized strings you provide by automatically inflecting localized strings to account for pluralization, grammatical gender agreement, and agreement with the user’s term of address. It’s available for English and Spanish. (70210115)
- Formatting APIs are now available, which focus on the format and remove the need to create, configure, and cache a formatter instance. Each [`Formatter`](https://developer.apple.com/documentation/foundation/formatter) type has a `formatted` function. These functions have arguments that allow for configuration and customization of the style. (70220307)
- [`JSONSerialization`](https://developer.apple.com/documentation/foundation/jsonserialization) and [`JSONDecoder`](https://developer.apple.com/documentation/foundation/jsondecoder) now support decoding from JSON5. (73954652)
- [`SortDescriptor`](https://developer.apple.com/documentation/foundation/sortdescriptor), [`KeyPathComparator`](https://developer.apple.com/documentation/foundation/keypathcomparator), and [`SortComparator`](https://developer.apple.com/documentation/foundation/sortcomparator) APIs provide a Swift interface to express archivable rules for sorting values. (74264359)

##### Logging

###### New Features

- [`os_signpost(_:dso:log:name:signpostID:)`](https://developer.apple.com/documentation/os/os_signpost(_:dso:log:name:signpostid:)-2oz8u) from Swift is part of the framework OS on all platforms: - Instantiate [`OSSignposter`](https://developer.apple.com/documentation/os/ossignposter) using a subsystem and category, an existing [`OSLog`](https://developer.apple.com/documentation/oslog) object, or an existing [`Logger`](https://developer.apple.com/documentation/os/logger) object.
- The OSSignposter API provides methods for emitting signposts. [`beginInterval(_:id:)`](https://developer.apple.com/documentation/os/ossignposter/begininterval(_:id:)) emits `begin` signposts, [`endInterval(_:_:)`](https://developer.apple.com/documentation/os/ossignposter/endinterval(_:_:)) emits `end` signposts, and [`emitEvent(_:id:)`](https://developer.apple.com/documentation/os/ossignposter/emitevent(_:id:)) emits `event` signposts. These replace the existing `os_signpost` calls based on `String` and `varargs`.
- The APIs support `String` interpolations for the metadata parameter. The `String` interpolations are the same as those accepted by the [`Logger APIs`](https://developer.apple.comhttps://developer.apple.com/documentation/os/osloginterpolation).
- The OSSignposter API supports all formatting and privacy options — previously offered by the `os_signpost` functions — and follows the same syntax as the Logger APIs.
- The APIs provide performance improvements over the legacy APIs.
- The `OSSignposter type` provides a new scoped API for surrounding a block of code by `begin` and `end` signposts, [`withIntervalSignpost(_:id:_:around:)`](https://developer.apple.com/documentation/os/ossignposter/withintervalsignpost(_:id:_:around:)). **Note:** These APIs are unavailable in iOS 14 and iPadOS 14 and earlier; however, the existing `os_signpost` API remains available. (54756831)

##### Maps

###### Known Issues

- Rounded building corners might disappear. (80468151)

###### Deprecations

- [`MKPinAnnotationView`](https://developer.apple.com/documentation/mapkit/mkpinannotationview) and [`MapPin`](https://developer.apple.com/documentation/mapkit/mappin) are marked as deprecated in this beta. (78536295)

##### Networking

###### New Features

- The default `Accept-Language` header that [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession) sends has an updated format and corrected values for multiple locales. In addition to the preferred language, the header also includes the current system language as a fallback if it differs from the preferred language. This behavior affects apps that link against macOS 12, iOS 15, tvOS 15, and watchOS 8 SDKs. (38772422)
- `URLSession` now includes `async` functions. (68890254) For example, a one-shot fetch: ```swift
let (data, response) = try await URLSession.shared.data(from: URL(string: "https://www.apple.com")!)
if let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 {
   // Use data.
}
``` And support for an [`AsyncSequence`](https://developer.apple.com/documentation/swift/asyncsequence) stream of bytes: ```swift
let (bytes, response) = try await URLSession.shared.bytes(with: URL(string: "https://www.apple.com")!)
if let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 {
    for try await line in bytes.lines() {
        // Parse line.
    }
}
```

###### Deprecations

- Support for cleartext HTTP URL schemes for Proxy Automatic Configuration (PAC) is now deprecated. Use only HTTPS URL schemes for PAC. This affects all PAC configurations, including, but not limited to, configurations set via Settings, System Preferences, profiles, and `URLSession` APIs such as [`connectionProxyDictionary`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/connectionproxydictionary) and [`CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)`](https://developer.apple.com/documentation/cfnetwork/cfnetworkexecuteproxyautoconfigurationurl(_:_:_:_:)). If you configure a cleartext HTTP PAC URL, the system may upgrade it to HTTPS during PAC file loads. Web Proxy Auto-Discovery (WPAD) Protocol via DNS isn’t affected. Dynamic Host Configuration Protocol (DHCP) Option 252 WPAD may attempt to upgrade cleartext HTTP URLs to HTTPS during PAC file loads. (61981845)

##### Privacy

###### New Features

- To download a file that shows the app content in the App Privacy Report, choose Settings > Privacy > Record App Activity. (77758720)

##### Reality Composer

###### Known Issues

- You might be unable to create new projects in Reality Composer. (79418400) **Workaround:** Create a new project in Reality Composer on macOS and transfer the `.rcproject` file to your device via AirDrop or Mail.

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

- Media items added to the default instance of [`SHMediaLibrary`](https://developer.apple.com/documentation/shazamkit/shmedialibrary) don’t appear in Shazam. (77785557) **Workaround:** Touch and hold the Music Recognition Control Center module to view [`SHMediaLibrary`](https://developer.apple.com/documentation/shazamkit/shmedialibrary) contents.

##### Siri

###### Known Issues

- VoiceOver and Spoken Content users might not initially see all available voice options. Voice options should populate after some time. (79463000)
- On-device speech recognition only supports the following languages: Chinese (Mandarin - China mainland), English (Australia), English (Canada), English (United Kingdom), and English (US). (78483609)

##### Skadnetwork

###### New Features

- If a developer opts-in to receive the winning postback, devices can now send a copy of the winning postback to the advertised app’s developer. (75054513)

##### Swift

###### New Features

- A new Swift value type [`AttributedString`](https://developer.apple.com/documentation/foundation/attributedstring) is now available with the same character-counting behavior as a Swift string. It’s fully localizable, and also includes support for Markdown, Codable, strongly typed attributes, and more. (27227292)
- [`NotificationCenter`](https://developer.apple.com/documentation/foundation/notificationcenter) includes a new [`AsyncSequence`](https://developer.apple.com/documentation/swift/asyncsequence) API for receiving notifications using async/await. (74401384) ```swift
for await note in NotificationCenter.default.notifications(named: .MyNote) {
    // Use note.
}
```

###### Known Issues

- Swift libraries depending on Combine may fail to build for targets including ARMv7 and i386 architectures. (82183186, 82189214) **Workaround:** Use an updated version of the library that isn’t impacted (if available) or remove ARMv7 and i386 support (for example, increase the deployment target of the library to iOS 11 or higher).

- Applications linking to RealityKit with the iOS 15 or macOS 12 SDKs will fail to launch on a previous OS. (79584511) **Workaround:** Add `OTHER_LD_FLAGS = -weak_framework RealityFoundation` to your Xcode Project settings to allow running RealityKit apps on an older OS.

##### Settings

###### Known Issues

- While the Sound Actions feature work as part of Switch Control, sounds aren’t detected in the area marked Practice in Settings app. (82411537)

##### Swiftui

###### New Features

- [`LocalizedStringKey`](https://developer.apple.com/documentation/swiftui/localizedstringkey) can now contain Markdown syntax. The system parses Markdown strings when you create a [`Text`](https://developer.apple.com/documentation/swiftui/text) view from a `LocalizedStringKey`, including `Text` views created with a string literal. The system styles `Text` according to Markdown constructs. (74515884)

- You can create [`Text`](https://developer.apple.com/documentation/swiftui/text) from an [`AttributedString`](https://developer.apple.com/documentation/foundation/attributedstring) structure. `Text` respects the styles you provide through attributes within the SwiftUI attribute scope; these styles take precedence over styles you provide through view modifiers. (74841755)

- Specific kinds of animations now execute off the main thread, so there are new thread-safety requirements. (70524799) Ensure the following functions and types are thread-safe: - All methods and accessors of types conforming to the protocols [`AlignmentID`](https://developer.apple.com/documentation/swiftui/alignmentid), [`Animatable`](https://developer.apple.com/documentation/swiftui/animatable), [`EnvironmentKey`](https://developer.apple.com/documentation/swiftui/environmentkey), [`EnvironmentValues`](https://developer.apple.com/documentation/swiftui/environmentvalues), [`Equatable`](https://developer.apple.com/documentation/swift/equatable), [`GeometryEffect`](https://developer.apple.com/documentation/swiftui/geometryeffect), [`Hashable`](https://developer.apple.com/documentation/swift/hashable), [`Identifiable`](https://developer.apple.com/documentation/swift/identifiable), [`PreferenceKey`](https://developer.apple.com/documentation/swiftui/preferencekey), [`Shape`](https://developer.apple.com/documentation/swiftui/shape), [`VectorArithmetic`](https://developer.apple.com/documentation/swiftui/vectorarithmetic).
- Any closures you pass to the following types and functions, but only if the views that created them don’t have references to [`ObservableObject`](https://developer.apple.com/documentation/combine/observableobject) types: [`ForEach`](https://developer.apple.com/documentation/swiftui/foreach), [`GeometryReader`](https://developer.apple.com/documentation/swiftui/geometryreader), [`backgroundPreferenceValue(_:_:)`](https://developer.apple.com/documentation/swiftui/view/backgroundpreferencevalue(_:_:)), [`overlayPreferenceValue(_:_:)`](https://developer.apple.com/documentation/swiftui/view/overlaypreferencevalue(_:_:)), [`transformPreference(_:_:)`](https://developer.apple.com/documentation/swiftui/view/transformpreference(_:_:)), [`anchorPreference(key:value:transform:)`](https://developer.apple.com/documentation/swiftui/view/anchorpreference(key:value:transform:)), [`transformAnchorPreference(key:value:transform:)`](https://developer.apple.com/documentation/swiftui/view/transformanchorpreference(key:value:transform:)), [`transformEnvironment(_:transform:)`](https://developer.apple.com/documentation/swiftui/view/transformenvironment(_:transform:)), [`transaction(_:)`](https://developer.apple.com/documentation/swiftui/view/transaction(_:)).

- A [`TextField`](https://developer.apple.com/documentation/swiftui/textfield) provided an [`Formatter`](https://developer.apple.com/documentation/foundation/formatter) now updates its binding as the user types. `NSFormatter` formats the text of the field when the user submits the field, or when focus moves away from the field. (67899823)
- A [`DisclosureGroup`](https://developer.apple.com/documentation/swiftui/disclosuregroup) now toggles its expansion when tapping the row. (62208702)
- The default [`ListStyle`](https://developer.apple.com/documentation/swiftui/liststyle) is now [`insetGrouped`](https://developer.apple.com/documentation/swiftui/liststyle/insetgrouped). (75072988)
- [`TextField`](https://developer.apple.com/documentation/swiftui/textfield) labels don’t appear next to the field in a form. Use the `prompt` parameter to specify an explicit placeholder for the field. (61260160)

- You can now initialize [`Text`](https://developer.apple.com/documentation/swiftui/text) with a [`FormatStyle`](https://developer.apple.com/documentation/foundation/formatstyle). (72159423)

- While searching, if you tap a suggestion that uses the [`searchCompletion(_:)`](https://developer.apple.com/documentation/swiftui/view/searchcompletion(_:)) modifier, the suggestion list now disappears rather than displaying the single suggestion you selected. (76965399)

- You can now customize the prompt of a search field that a searchable modifier configures using the `prompt` parameter instead of the previous `title` parameter. (77988967)
- SwiftUI now supports `textSelection` modifiers. (77827592)

- Added `buttonBorderShape`, which can be used to control the shape of bordered buttons. (79456465)

- Added new [`AttributedString`](https://developer.apple.com/documentation/foundation/attributedstring) attributes [`underlineStyle`](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes/underlinestyle) and [`strikethroughStyle`](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes/strikethroughstyle) to [`AttributeScopes.SwiftUIAttributes`](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes). (78437803)

- Types conforming to the [`Animatable`](https://developer.apple.com/documentation/swiftui/animatable) protocol and also conforming to either the [`View`](https://developer.apple.com/documentation/swiftui/view) or [`ViewModifier`](https://developer.apple.com/documentation/swiftui/viewmodifier) protocols now apply animations when their values change. Consequently, the [`AnimatableModifier`](https://developer.apple.com/documentation/swiftui/animatablemodifier) protocol is soft-deprecated. Use `Animatable` directly when targeting the latest OS versions; for example, use `struct CustomModifier: ViewModifer, Animatable` rather than `struct CustomModifier: AnimatableModifier`. (76971100)

- The [`contentShape(_:eoFill:)`](https://developer.apple.com/documentation/swiftui/view/contentshape(_:eofill:)) modifier now allows fine-grained control over different kinds of shapes. For drag previews, hover effects, and context menus, the matching `ContentShapeKinds` is required to affect the shape of previews when linked on iOS 15.0 or newer. The default behavior is to set the `interaction` kind. (60792377)

- The [`openURL`](https://developer.apple.com/documentation/swiftui/environmentvalues/openurl) environment value can now be set and used to customize URL handling in the view hierarchy, including URL handling in [`Link`](https://developer.apple.com/documentation/swiftui/link) views and links embedded in [`Text`](https://developer.apple.com/documentation/swiftui/text) views. (78551237)

- [`Task`](https://developer.apple.com/documentation/swift/task) allows you to pass the priority to be used when spawning a new `Task`. (80599258)

- [`Text`](https://developer.apple.com/documentation/swiftui/text) views that contain excessive line height characters now have a larger default size to avoid clipping or overlapping of oversized characters. (80665315)
- A [`NavigationLink`](https://developer.apple.com/documentation/swiftui/navigationlink) in a sidebar on iPad that uses `isDetailLink(false)` correctly pushes onto the sidebar rather than the detail area. (80919171)

###### Known Issues

- Providing a binding to an [`OutlineGroup`](https://developer.apple.com/documentation/swiftui/outlinegroup) might require including [`wrappedValue`](https://developer.apple.com/documentation/swiftui/binding/wrappedvalue) in the [`init(_:children:content:)`](https://developer.apple.com/documentation/swiftui/outlinegroup/init(_:children:content:)-2galq) key path parameter, and isn’t available in iOS & iPadOS 14 and earlier. (77890799)

- Focusing a view in a newly added [`List`](https://developer.apple.com/documentation/swiftui/list) row using [`FocusState`](https://developer.apple.com/documentation/swiftui/focusstate) requires deferring the focus state property update to the next time the main runloop runs. (78607356)
- [`List`](https://developer.apple.com/documentation/swiftui/list) no longer respects SwiftUI’s safe area insets. (82295913)

###### Deprecations

- `controlProminence` is deprecated. Use the new `.borderedProminent` [`ButtonStyle`](https://developer.apple.com/documentation/swiftui/buttonstyle) instead. (78908460)

- The Function (`Fn`) shortcut modifier is deprecated and reserved for system usage. (78627099)

##### Tabulardata

###### New Features

- [`TabularData`](https://developer.apple.com/documentation/tabulardata) is a new Swift framework you use to analyze and manipulate tabular data. You can use [`DataFrame`](https://developer.apple.com/documentation/tabulardata/dataframe) to read CSV and JSON files, as well as join, group, and aggregate data. (69982458)

##### Uikit

###### New Features

- For apps compiled against the iOS 15 beta SDK, key commands no longer intercept text input and text editing commands while typing into text views and text fields. For example, pressing the Delete key always deletes a character and doesn’t trigger a Delete key command if one is present. To have a key command intercept text input, set the [`wantsPriorityOverSystemBehavior`](https://developer.apple.com/documentation/uikit/uikeycommand/wantspriorityoversystembehavior) property to `true` on the key command. This is also required to have key commands take priority over focus keyboard navigation commands, such as arrow and tab key presses. (55118263)
- In iOS 14 and iPadOS 14 and earlier, when [`autocorrectionType`](https://developer.apple.com/documentation/uikit/uitextinputtraits/autocorrectiontype) is set to [`UITextAutocorrectionType.no`](https://developer.apple.com/documentation/uikit/uitextautocorrectiontype/no), the QuickType bar is disabled. For apps linked against iOS 15 and iPadOS 15 or later, the QuickType bar is enabled and shows spellchecking candidates. If the new behavior isn’t desirable for your use case, set [`spellCheckingType`](https://developer.apple.com/documentation/uikit/uitextinputtraits/spellcheckingtype) to [`UITextSpellCheckingType.no`](https://developer.apple.com/documentation/uikit/uitextspellcheckingtype/no) to hide the QuickType bar. (68874861)
- When compiling with the iOS 15 beta SDK, several key window-related properties, methods, and notifications change behavior: - [`isKeyWindow`](https://developer.apple.com/documentation/uikit/uiwindow/iskeywindow) returns `true` if the window is key in its scene instead of the app.
- [`becomeKey()`](https://developer.apple.com/documentation/uikit/uiwindow/becomekey()) is called when the window becomes key in its scene instead of the app.
- [`didBecomeKeyNotification`](https://developer.apple.com/documentation/uikit/uiwindow/didbecomekeynotification) posts when the window becomes key in its scene instead of the app.
- [`resignKey()`](https://developer.apple.com/documentation/uikit/uiwindow/resignkey()) is called when the window resigns key window status in its scene instead of the app.
- [`didResignKeyNotification`](https://developer.apple.com/documentation/uikit/uiwindow/didresignkeynotification) posts when the window resigns key window status in its scene instead of the app. (72873846)

##### Xcode

###### Known Issues

- [`MusicKit`](https://developer.apple.com/documentation/musickit) functionality, such as loading content with music requests, doesn’t work in simulated devices. (78559381)

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