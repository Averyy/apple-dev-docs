# iOS & iPadOS 16.4 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 16.4 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 16.4. The SDK comes bundled with Xcode 14.3, available from the Mac App Store. For information on the compatibility requirements for Xcode 14.3, see [`Xcode 14.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14_3-release-notes).

##### Backup and Restore

###### Known Issues

- Watch migration might fail when restoring a backup to a new phone. (105416351)  Unpair the watch from the source phone, then pair it to the destination phone.

##### Beta Enrollment for Iphone and Ipad

###### New Features

- Beginning with iOS & iPadOS 16.4 beta, members of the Apple Developer Program will see a new option to enable developer betas directly from Software Update in Settings. This new option will be automatically enabled on devices already enrolled in the program that update to the latest beta release. Your iPhone or iPad must be signed in with the same Apple ID you used to enroll in the Apple Developer Program in order to see this option in Settings. In future iOS and iPadOS releases, this new setting will be the way to enable developer betas and configuration profiles will no longer grant access. (101692915)

##### Core Ml

###### Deprecations

- Core ML Model Deployment is being deprecated. Consider using Background Assets or `NSURLSession` instead. (102993813)

##### Core Telephony

###### Deprecations

- `CTCarrier`, a deprecated API, returns static values for apps that are built with the iOS 16.4 SDK or later. (76283818)

##### Developer Settings

###### New Features

- Hang Detection stays enabled after rebooting. (105618983)

##### Home

###### New Features

- Both manual and automatic Software Update support is now available for Matter Accessories. (102727759)

###### Known Issues

- The iOS device that initiates the pairing needs to be on the same iCloud account with the home hub. Only the owner of a home, not an invited user, can pair Matter accessories. (76012945)
- You might receive an error when pairing a Matter accessory using the 11 digit setup code. (101554366)  Pair the accessory using the QR code instead.
- When a manual software update is attempted on a Matter accessory with an available update, Home might not indicate that the update has been requested and continue to indicate an update is available. (104902918)  Check the Software Update pane in Home Settings at a later time, as the update might be taking place in the background. 
- The software update screen for Matter accessories might display the incorrect version number while an update is in progress. (105031569)
- Right after pairing, an available firmware update is not offered in the Home app. (105757029)  Reboot all residents.
- When there are multiple of the same accessory type updating to the same firmware or if there are back-to-back firmware versions for one accessory (during an incremental update), the new firmware update might not be offered. (105787380)  Reboot all residents or unpair the accessory and re-pair by clicking the “More options…” link to pair the accessory from there.
- Software updates for Matter accessories might be offered again, even though the update already completed successfully.
(106073031)  Restart your HomePod and Apple TV devices.

##### Icloud Drive

###### Known Issues

- Filesystem APIs such as `NSFileManager` might trigger materialization of dataless files and/or directory structures in iCloud Drive, leading to hangs or performance problems for the calling application. (105009536)  Avoid calling anything which performs I/O on the main thread. Adopt `UICollectionViewDataSourcePrefetching` and load cells asynchronously. I/O should be wrapped under `-[NSFileCoordinator coordinateAccessWithIntents:queue:byAccessor:]` to avoid blocking a thread on a synchronous call. Alternatively, opt out of this behavior by setting your IO policy to `IOPOL_MATERIALIZE_DATALESS_FILES_OFF` but expect that I/O might fail with `EDEADLK`, if any component of the path is dataless (`SF_DATALESS`).
- iCloud Drive might become unresponsive when opened from the Files app. (105438692)  Restart your device.
- A loading indicator might appear, and the contents of iCloud Drive might be inaccessible within the Files app. (106232492)

##### Keyboards

###### New Features

- Updates to Keyboards include: - Support for new Unicode 15.0 Emoji.
- Autocorrect for the Korean keyboard is enabled by default for testing and feedback.
- Ukrainian keyboard now supports predictive text.
- Gujarati, Punjabi, and Urdu keyboards add support for transliteration layouts.
- New keyboard layouts are available for Choctaw and Chickasaw. (105243233)

##### Mapkit

###### Resolved Issues

- Fixed: Improved performance of `MKOverlay` objects. (102187262)

##### Pages Numbers and Keynote

###### Known Issues

- When Advanced Data Protection for iCloud is turned on, Pages, Numbers, and Keynote might unexpectedly require collaborative documents to be closed. (103463223)  Close the affected document, spreadsheet, or presentation and reopen it after a few minutes.

##### Passkeys and Authentication Services

###### New Features

- Web browsers on iOS with the `com.apple.developer.web-browser` entitlement now have passkey AutoFill within their `WKWebView`. This capability works without requiring any code changes or needing to rebuild. (97576198)
- A new [`AuthorizationController`](https://developer.apple.com/documentation/authenticationservices/authorizationcontroller) API allows you to perform passkey and other types of authorization requests from SwiftUI views. (97576703)
- A new [`WebAuthenticationSession`](https://developer.apple.com/documentation/authenticationservices/webauthenticationsession) API allows you to perform `OAuth` and other types of web-based authentication flows from SwiftUI views. (101259868)

###### Resolved Issues

- Fixed: Conditional mediation requests (passkey AutoFill) in web content don’t abort when their `AbortSignal` is fired. (99535627)
- Fixed: AutoFill, including AutoFill for passkeys and passwords, now works with input elements contained in a Shadow DOM in web content. (103859657)
- Fixed: Calling `PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable()` or `PublicKeyCredential.isConditionalMediationAvailable()` from a web page in a `WKWebView` now correctly returns whether passkeys can be used, based on the Associated Domains of the calling app. (104094169)

##### Pencil

###### New Features

- Apple Pencil hover now provides Tilt and Azimuth support. (105412781)

##### Safari Web Extensions

###### New Features

- Added support for `modifyHeaders` action type for `declarativeNetRequest` rules. (71867709)
- Added support for `browser.storage.session` to store up to 10MB of data in-memory. (79283961)
- Added support for persistent content scripts via `browser.scripting.registerContentScript`, `browser.scripting.getRegisteredContentScripts`, `browser.scripting.unregisterContentScripts`, and `scripting.updateContentScripts`. (91261369)

###### Resolved Issues

- Fixed `browser.webNavigation` events firing for hosts where the extension didn’t have access. Extensions should request host permissions for sites to receive events. (100204850)

##### Skadnetwork

###### Resolved Issues

- Fixed an issue where `SKAdNetwork` for Web Ads didn’t accept ad impressions. (104839712)

##### Storekit

###### New Features

- New StoreKit 2 APIs are available for promoted in-app purchases. Apps can receive promoted product purchase data from the App Store with `PurchaseIntent.intents` and can manage promoted order and visibility with `Product.PromotionInfo`. (85321849)

##### Swiftui

###### New Features

- A family of new view modifiers lets you build even richer resizable sheet experience with SwiftUI. Use these new modifiers to make the view behind a sheet interactive, provide a translucent background, control scrolling and expansion behavior, and even adjust the corner radius of the sheet. To let people interact with the content behind a sheet, use the `.presentationBackgroundInteraction(_:)` modifier. The following example enables people to interact with the view behind the sheet when the sheet is at the smallest detent, but not at the other detents: ```swift
   struct ContentView: View {
       @State private var showSettings = false

       var body: some View {
           Button("View Settings") {
               showSettings = true
           }
           .sheet(isPresented: $showSettings) {
               SettingsView()
                   .presentationDetents(
                       [.height(120), .medium, .large])
                   .presentationBackgroundInteraction(
                       .enabled(upThrough: .height(120)))
           }
       }
   }
``` Give your sheet a translucent background with the new `presentationBackground(_:)` modifier. The following example uses the thick material as the sheet background: ```swift
  struct ContentView: View {
      @State private var showSettings = false
  
      var body: some View {
          Button("View Settings") {
              showSettings = true
          }
          .sheet(isPresented: $showSettings) {
              SettingsView()
                  .presentationBackground(.thickMaterial)
           }
       }
   }
``` Add a custom view as the background of your sheet with the `presentationBackground(alignment:content:)` modifier. By default, when a person swipes up on a scroll view in a resizable presentation, the presentation grows to the next detent. A scroll view embedded in the presentation only scrolls after the presentation reaches its largest size. Use the new `presentationContentInteraction(_:)` modifier to control which action takes precedence. For example, you can request that swipe gestures scroll content first, resizing the sheet only after hitting the end of the scroll view, by passing the `.scrolls` value to this modifier: ```swift
   struct ContentView: View {
       @State private var showSettings = false

       var body: some View {
           Button("View Settings") {
               showSettings = true
           }
           .sheet(isPresented: $showSettings) {
               SettingsView()
                   .presentationDetents([.medium, .large])
                   .presentationContentInteraction(.scrolls)
           }
       }
   }
``` (101565636)
- Apply the new `.presentationCompactAdaptation(_:)` modifier to the content of a modal presentation to control how it adapts to compact size classes on iPad and iPhone. For example, the `popover` modifier presents a popover on iPad. By default, a popover adapts to the narrow horizontal size class on iPhone by showing as a sheet. In the example below, the `.presentationCompactAdaptation(.none)` modifier asks SwiftUI to show this as a popover on iPhone as well. ```swift
  struct PopoverExample: View {
      @State private var isShowingPopover = false
  
      var body: some View {
          Button("Show Popover") {
              self.isShowingPopover = true
          }
          .popover(isPresented: $isShowingPopover) {
              Text("Popover Content")
                  .padding()
                  .presentationCompactAdaptation(.none)
          }
      }
  }
``` Use `.presentationCompactAdaptation(horizontal:vertical:)` to adapt differently in horizontally and vertically compact size classes. (103257577)

###### Resolved Issues

- Fixed: `ScrollView` has improved support for right to left languages by default. If you have a `ScrollView` that shouldn’t change its behavior in right to left languages, use the `.environment(\.layoutDirection, .leftToRight)` modifier to ensure the `ScrollView` always sees a left to right layout direction. (65108729)
- Fixed: Presentations in SwiftUI using the ‘sheet’ or ‘fullScreenCover’ modifier can now be dynamically presented again while a dismiss animation is in progress. Previously, attempting to present again in this case would do nothing. Note: A data race in app code that was previously ignored might cause a sheet to be presented again with this change. If this happens, check that your state isn’t triggering a new presentation. (101487810)
- Fixed: Refreshable modifiers applied to lists will no longer also apply to lists or scroll views within the content of that list. Re-apply a refreshable modifier to the content of the list if this is desired behavior. (102052575)
- Fixed: The no-argument `presentationBackground()` modifier has been removed. Use one of the overloads taking an explicit ShapeStyle or View instead. (105598868)

###### Deprecations

- TimelineView initializers that pass an instance of `TimelineView<_, _>.Context` into its content closure have been deprecated in this release, and replaced with equivalent versions that pass an instance of `TimelineViewDefaultContext` instead. In TimelineView code that does not generate a warning, no action is needed: code that does not explicitly annotate the context type will use the new API when recompiled, without any change in functionality. In TimelineView code that does show this new deprecation warning, changing type annotations from `TimelineView<_, _>.Context` to `TimelineViewDefaultContext` will resolve the warning. This change improves the performance of compiling Swift and SwiftUI code. The new initializer uncouples the generic type of the TimelineView being instantiated from the generic type of the context passed into its content closure, avoiding the need for the compiler to reconcile those types during compilation. (100641618)
- Several table initializers that were previously deprecated and replaced in iOS 16.2 and macOS 13.1 have now been removed from the API. Using these initializers will now generate a build error, with a Fix-It to switch to the replacement initializer API. For code that doesn’t generate this error, no action is needed. This change, along with other improvements in the Swift compiler, improve the performance of compiling Swift and SwiftUI code. The new, replacement API adds a parameter, `of:`, that identifies the type of the Table’s row values separately from the initializer’s row and column content closure parameters. This improves compilation performance in two ways. First, by knowing the row value type up-front, the compiler doesn’t need to infer that type from the body implementations of each closure. Second, the compiler can immediately enforce that each closure uses the same row value type in its body implementation, instead of needing to verify that the inferred types are equal after evaluating each closure. The following examples show code for creating a Table before and after adoption of the new API: ```swift
// before (will now produce an error):
Table {
  TableColumn("Name", value: \.name)
  TableColumn("Email", value: \.email)
} rows: {
  ForEach(people) { person in
      TableRow(person)
  }
}

// after:
Table(of: Person.self) {
  TableColumn("Name", value: \.name)
  TableColumn("Email", value: \.email)
} rows: {
  ForEach(people) { person in
      TableRow(person)
  }
}
``` (102910184)

##### Swiftui Navigation

###### Resolved Issues

- Fixed: Navigation destinations nested within `NavigationStack` and `NavigationSplitView` are detected more performantly and reliably, no longer logging update cycles. (97597634)
- Fixed: Navigation destinations that present a new view on top of a `NavigationSplitViewColumn` (rather than pushing a view onto a stack in that column) no longer cause an assertion failure on iOS or infinite loop on macOS when the destination view is itself a `NavigationStack`. For example, the below construction is functional ```swift
NavigationSplitView { 
    SidebarView()
    .navigationDestination(isPresented: $present) {
        NavigationStack { ... }
    }
} detail: { ... }
``` (103278180)
- Fixed: Navigation destinations with data dependencies captured from ancestor views update more reliably. ```swift
struct DataDependentNavigation: View {
  @State var changeColor: Bool = false
  @State var present: Bool = false

  var body: some View {
  NavigationSplitView {
    Color.blue
      .navigationDestination(isPresented: $present) {
           // This is a data dependency from an ancestor view
            changeColor ? Color.green : Color.yellow
      }
  } detail: {
    Color.teal
  }
}
``` (103429535)

##### Wallet

###### Known Issues

- An error might occur when adding or presenting an ID card. (105302759)

## See Also

- [iOS & iPadOS 16.6 Release Notes](ios-ipados-16_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.5 Release Notes](ios-ipados-16_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.3 Release Notes](ios-ipados-16_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.2 Release Notes](ios-ipados-16_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS 16.1 Release Notes](ios-16_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS 16 Release Notes](ios-16-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iPadOS 16 Release Notes](ipados-16-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16_4-release-notes)*