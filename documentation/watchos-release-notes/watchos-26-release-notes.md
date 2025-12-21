# watchOS 26 Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 26 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 26. The SDK comes bundled with Xcode 26, available from the Mac App Store. For information on the compatibility requirements for Xcode 26, see [`Xcode 26 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26-release-notes).

##### General

###### Resolved Issues

- After updating to watchOS 26, your Apple Watch Series 7 or Apple Watch SE 2 will recalibrate and then estimate its maximum battery capacity more accurately.  (144885837)

##### App Store

###### New Features

- A new Accessibility section has been added to the App Store product pages that highlights accessibility features within apps and games. These Accessibility Nutrition Labels give users a new way to learn if an app will be accessible to them before they download it, and give developers the opportunity to better inform and educate their users on features their app supports.  (138344118)

##### Apple Intelligence

###### Resolved Issues

- Fixed: Model quality output degrades after extended, repeated inferences of the same adapter.  (152468267)

##### Apple Watch Herm%c3%a8s

###### Resolved Issues

- Fixed: Apple Watch Hermès crashes continuously if updated to watchOS 26 beta 2. It is advised that these users do not update to beta 2.  (152604139)

##### Assistantschemas

###### Resolved Issues

- Fixed: If you have adopted any of the following email AssistantSchemas, you will experience a compilation error due to a parameter type change: `createDraft`, `updateDraft`, `replyMail`, `forwardMail`, `message`, and `draft`.  (148633307)

##### Cloudkit

###### Resolved Issues

- Fixed: CloudKit sharing URLs do not launch third-party apps.  (151778655)

##### Contacts

###### Resolved Issues

- Fixed: Resolved an issue where some contacts with outsized images might fail to sync to Apple Watch until Reset Sync Data is performed. After updating to watchOS 26 beta 4, perform a reset sync (Watch app > General > Reset > Reset Sync Data) to enable these contacts to sync again.  (155535527)

##### Control Center

###### Resolved Issues

- Fixed: User cannot exit the Cellular Data Options pane by tapping the back arrow.  (152248850)
- Fixed: Button symbols sometimes disappear upon reboot.  (157942636)

##### Coredata

###### Resolved Issues

- Fixed: In beta 5 SDK, CoreData changed several `Sendable` annotations to resolve compatibility issues with Swift 6’s new `MainActor` default isolation feature. These changes include marking `NSManagedObject` as `NS_SWIFT_NONISOLATED NS_SWIFT_NONSENDABLE`, marking `NSManagedObjectContext` as `NS_SWIFT_NONISOLATED NS_SWIFT_SENDABLE`, and requiring `NS_SWIFT_SENDABLE` closures for the family of `perform`, `performBlock`, `performBlockAndWait` and similar methods. These changes are ABI compatible with past releases but might introduce new warnings while building source code that violates the longstanding CoreData concurrency guidelines. `NSManagedObject` are mutable reference types inextricably related to others in a graph and cannot be made `Sendable`. They are expected to be isolated to the scope of the `NSManagedObjectContext` that creates or fetches them. `NSManagedObjectContext` is a style of actor which encapsulates its own dispatch queue. While it’s impermissible to use many methods on `NSManagedObjectContext` from other threads, it is permissible to pass references around to invoke the `performBlock` family of methods, for the purpose of routing a `Sendable` closure to its managed dispatch queue. CoreData supports a user default `-com.apple.CoreData.ConcurrencyDebug 1` which can be used to enable additional assertions.  (153848710) (FB18216198)

##### Foundation

###### New Features

- Interpolating non-localized types into a `LocalizedStringResource/String(localized:)/AttributedString(localized:)` value will now display a deprecation warning instead of potentially falling back to a fully-unlocalized string. Provide a localized value to interpolate into the text instead, or silence the warning by wrapping the unlocalized value in a call to `String(describing:)`.  (126876158)

###### Resolved Issues

- Fixed: Functions that initialize a string from a C-string pointer do not validate that the provided encoding is a valid encoding for C-strings.  (143756086) (FB16417968)
- Fixed: `Locale.preferredLocale` API availability for tvOS and watchOS is specified incorrectly.  (151205096)

##### Healthkit

###### Resolved Issues

- Fixed: An app that was granted Read-only authorization for certain data types (e.g. workout routes) might lose its ability to read the data type without the user explicitly turning it off in Settings > Health.  (149024236)

##### Maps

###### Known Issues

- Custom tap gesture callbacks registered using `onTapGesture` might not work as expected on a SwiftUI Map.  (157612948) (FB19394663)  Use `simultaneousGesture(TapGesture().onEnded {})` to register the callback.

##### Memory Tools

###### Known Issues

- Leaks might be falsely reported by memory analysis tools when a target has instances of types that use Obj-C properties implemented in Swift using bridged types with `@objc @implementation`. Memory analysis tools include the `leaks` CLI tool, Leaks instrument, and Xcode memory graph debugger.  (157798911)

##### Notes

###### Resolved Issues

- Fixed: When creating a note on watchOS with Siri, you might get an error from Siri saying something went wrong. However, the note will still get created.  (155658052)

##### Nslog

###### New Features

- Dynamic string data in format arguments for `NSLog` will be redacted to `\<private\>` in the Unified Logging System. This specifically targets data that enters the Unified Logging System via `NSLog`, and will not impact the Xcode console or `NSLog`’s `stdout` output. If you wish to log un-redacted data to the Unified Logging System please use the “os_log” or “Logger” interfaces.  (137129180)

##### Phone

###### Resolved Issues

- Fixed: Users are not able to send custom or default Live Replies from Apple Watch when the companion iPhone sends an unknown call to Call Screening.  (151414166)

##### Security

###### Deprecations

- For apps linked on or after iOS 26 and macOS 26, the default minimum TLS version of `URLSession` and Network frameworks has changed from 1.0 to 1.2. If your process connects only to your servers, verify that they support TLS 1.3 or TLS 1.2. If your process needs to connect to 3rd-party servers which cannot be updated to support newer versions of TLS, restore the previous behavior through `URLSession` and Security framework APIs: `URLSessionConfiguration.tlsMinimumSupportedProtocolVersion` and `sec_protocol_options_set_min_tls_protocol_version`.  (135996267)

##### Speech

###### Known Issues

- The `Speech` framework is not available in the tvOS or watchOS SDKs.  (151319670)

##### Storekit

###### New Features

- There is a new option for the `Transaction.Offer.PaymentMode` API called `oneTime`. This new case supports the method of payment for In-App Purchase offer codes.  (142501142)
- Subscription promotional offers can now be signed using JWS and attached to a purchase using the new `PurchaseOption.promotionalOffer(_:compactJWS:)` API. There are also new corresponding SwiftUI APIs in StoreKit to attach a signed promotional offer or a signed introductory offer override to a view.  (143395736)

###### Resolved Issues

- Fixed: Subscription status updates might not be reported correctly if the subscription went into billing retry in StoreKit Testing in Xcode.  (133799135) (FB14789854)
- Fixed: Price of offers is not displayed in the payment sheet when making a purchase to a subscription with a higher level of service in StoreKit Testing in Xcode.  (140635780) (FB15980635)
- Fixed: Renewal transactions might be created regardless of the Ask to Buy status of the purchase request in StoreKit Testing in Xcode.  (145242611)
- Fixed: `SKProduct` from the original StoreKit API fails to decode products when using StoreKit Testing in Xcode.  (150851879)
- Fixed an issue causing the buy button label in StoreKit views on watchOS to appear identical if the component is enabled or disabled when the app’s [`accentColor`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/color/accentcolor) is missing.  (153218311)
- Fixed: Transactions might not finish, resulting in subsequent purchases of the same product failing.  (155449267)

##### Swift Charts

###### Resolved Issues

- Fixed: Annotations on a scrollable chart might be clipped.  (109164195)

##### Swiftui

###### New Features

- `ControlSize` now conforms to `Comparable`, and `View/controlSize(_:)` can now be used to clamp the environment’s `controlSize` to a given range.  (99633360) (FB11465757)
- Text, TextEditor, and TextField now by default use string contents to determine the appropriate base writing direction for each paragraph, instead of relying on layout directionality. To specify the writing direction explicitly on a per-paragraph basis, use Foundation’s `AttributedString.writingDirection` attribute. To make the base writing direction follow the layout direction for an entire view, apply the view modifier `.writingDirection(strategy: .layoutBased)`.  (134821288)
- When linking news SDKs, `NavigationLink`s produce a single view, rather than a list of views in view list contexts. This change improves performance of many `NavigationLink`s in lazy containers like `List`. However, if you are relying on `ContainerValues` propagating out of the `label` view of a `NavigationLink`, or similarly relying on `ContainerValues` of a `ButtonStyle` used to style a link, the `containerValue(_:,_:)` modifier should be moved outside of the link. Below is a minimal example that demonstrates the behavior difference: ```swift
 import SwiftUI
 
 struct ContentView: View {
     @State private var presentPopover = false
     var body: some View {
         NavigationLink("Custom Link", value: 84)
             .buttonStyle(MyButtonStyle(containerValue: "Eighty-four"))
     }
 }
 
 struct ParentView: View {
     var body: some View {
         Group(subviews: ContentView()) { subviews in
             ForEach(subviews) { subview in
                 Text(subview.containerValues.myCustomValue)
             }
         }
         .frame(minWidth: 100, minHeight: 100)
     }
 }
 
 struct MyButtonStyle: PrimitiveButtonStyle {
     var containerValue: String
     func makeBody(configuration: Configuration) -> some View {
         Button(configuration)
             .buttonBorderShape(.circle)
             .containerValue(\.myCustomValue, containerValue)
     }
 }
 
 private struct MyContainerValueKey: ContainerValueKey {
     static let defaultValue: String = "Default value"
 }
 
 extension ContainerValues {
     var myCustomValue: String {
         get { self[MyContainerValueKey.self] }
         set { self[MyContainerValueKey.self] = newValue }
     }
 }
 
 #Preview {
     ParentView()
 }
``` (140283584)
- In `NavigationSplitView` and `TabView`s configured as `sidebarAdaptable`, the view trailing the sidebar’s safe area is inset in the width of the sidebar. It can display content outside its safe area, underneath the sidebar.  (141222137)
- In apps that adopt the new design, the `buttonBorderShape(_:)` view modifier can be used to customize the shape of bordered buttons. Previously this modifier only affected buttons in Widgets in macOS.  (145773436)
- The `buttonSizing(_:)` view modifier specifies the sizing behavior of `Button`, `Picker`, `Menu`, and other button-producing controls. If you are using `Spacer` views or an infinite-width frame in your `Button` label to create a flexible button, apply `buttonSizing(.flexible)` to the `Button` instead.  (146327046)

###### Resolved Issues

- Fixed: `TextEditor`’s undo stack might contain invalid operations for applications with multiple `TextEditor` views.  (83650197) (FB9662463)
- Fixed: The menu content of some `Menu` views does not update as the result of a state change.  (106878937)
- Fixed: [`View.onHover(perform:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/onhover(perform:)) and [`View.onContinuousHover(coordinateSpace:perform:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)) affect hit-testing for gestures. Gestures are not received if one of these view modifiers is used within an overlay.  (108560020)
- Fixed: Section views without `isExpanded` binding are collapsible in a sidebar-styled List on macOS.  (115797465) (FB13192271)
- Fixed: `listSectionSpacing` does not work correctly for sections that have headers and footers. For more control over the list section layout, use the `listSectionMargins` modifier.  (140929163)
- Fixed: On iOS, `navigationSplitViewColumnWidth()` does not respect the specified minimum and maximum column widths.  (143529326)
- Fixed: Multiple title views in sidebar list labels on iOS are not styled hierarchically as title and subtitle.  (144253754)
- Fixed: In custom layouts that do not implement `explicitAlignment(of:in:proposal:subviews:cache:)`, alignment guides do not work correctly for a right-to-left layout direction.  (145073832)
- Fixed: Applying a `bold` modifier to `Text` resets the `weight` configuration. The interaction of `bold` and `weight` is not consistent between Text and Font.  (147270079)
- Fixed: On platforms supporting edge-attached and non-edge-attached sheets, non-edge-attached sheets present erroneously as full-screen covers when `.navigationTransition(.zoom...)` is specified. If you wish to keep the full-screen cover in compact size classes, configure a sheet with: ```swift
 .sheet(...) {
    ContentView()
     .navigationTransition(.zoom...)
     .presentationSizing(.page)
     .presentationCompactAdaptation(.fullScreen)
``` (150455117)
- Fixed: If Default Actor Isolation is set to `MainActor`, `@Animatable` macro emits concurrency warnings in Swift 5 language mode and does not compile in Swift 6 language mode.  (152524435)
- Fixed: On visionOS, tvOS, and watchOS, sheets presented within toolbar items might fail to present if the toolbar item’s label view is a `Label`.  (157326248)

###### Known Issues

- `toolbarForegroundStyle` no longer tints toolbar button labels on watchOS.  (151487439)  Tint the button label directly, using `Text("foo").foregroundStyle(...)`.
- `.toolbarVisibility(_:for:)` does not hide the navigation bar on watchOS.  (152326250)

###### Deprecations

- `Text` concatenation using the `+` operator is deprecated because it makes it hard to create localized strings that are correct across all languages. Use `Text` interpolation instead. See documentation on `Text` for more info on how to produce localized strings.  (128144043)

##### Textkit

###### New Features

- iOS 26, tvOS 26, visionOS 26, watchOS 26, and macOS Tahoe 26 have two methods for resolving the natural alignment `NSTextAlignment.natural` and the last line of `NSTextAlignment.justified` into concrete alignments, `left` and `right`. The first approach utilizes the UI language, which is determined by passing nil-language to `NSParagraphStyle.defaultWritingDirection(forLanguage: )`. This behavior was employed prior to this release. The second method is new and dynamically utilizes the base writing direction for the paragraph. When the base writing direction is set to `NSWritingDirection.rightToLeft`, the text is aligned to `right`, and vice versa. The behavior is selected by API introduced in this major release: `NSTextLayoutManager.resolvesNaturalAlignmentWithBaseWritingDirection`, `NSStringDrawingOptionsResolvesNaturalAlignmentWithBaseWritingDirection`, `UITraitCollection.resolvesNaturalAlignmentWithBaseWritingDirection`, and `NSTextField.resolvesNaturalAlignmentWithBaseWritingDirection`.  (152045248)

###### Resolved Issues

- Fixed: The directionality of `NSParagraphStyle` indentation properties (`firstLineHeadIndent`, `headIndent`, and `tailIndent`) is determined by inconsistent hidden rules implemented by the TextKit typesetting engine. With iOS 26, macOS 26, tvOS 26, watchOS 26, and visionOS 26, the TextKit 2 typesetting engine has been standardized to utilize the resolved writing direction for the paragraph when linked with the OS 26 versions of the corresponding SDKs. For binary compatibility, applications developed with prior SDK versions will use the UI language in a subset of API interfaces. Specifically, for `UILabel`, `NSTextField`, `SwiftUI.Text`, and `NSStringDrawing`, the indentation directionality is determined by the UI language queried by passing nil to `NSParagraphStyle. defaultWritingDirection()` in applications built with prior SDK versions.  (155893102)

##### Translation

###### Known Issues

- Downloading languages for translation might display incomplete indicators on the download screen resulting in translation features being unavailable.  (148923222)  Reboot the device.

##### Workout

###### Known Issues

- Users might be unable to end a workout that has been auto-paused.  (155970593)  Resume the Workout, then tap End.

##### Workout Buddy

###### Resolved Issues

- Fixed: Workout Buddy might appear as unavailable in the watchOS Workout app after installing beta 1.  (152691503)

###### Known Issues

- Workout Buddy announcements play only on AirPods with H1 or later when connected to Apple Watch or iPhone, and on third-party bluetooth headphones when connected to iPhone.  (152316444)

## See Also

- [watchOS 26.3 Beta Release Notes](watchos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.2 Release Notes](watchos-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.1 Release Notes](watchos-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-26-release-notes)*