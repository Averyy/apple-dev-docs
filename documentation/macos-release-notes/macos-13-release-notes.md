# macOS Ventura 13 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 13 SDK provides support to develop apps for Mac computers running macOS Ventura 13. The SDK comes bundled with Xcode 14.1 RC, available from [`Beta Software Downloads`](https://developer.apple.comhttps://developer.apple.com/download/). For information on the compatibility requirements for Xcode 14.1, see [`Xcode 14.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14_1-release-notes).

##### General

###### Known Issues

> ❗ **Important**: Update to macOS Ventura 13 beta 6 or later before installing firmware updates for Apple Studio Display. (97624990)

Update to macOS Ventura 13 beta 6 or later before installing firmware updates for Apple Studio Display. (97624990)

##### Appkit

- See [`AppKit Release Notes for macOS Ventura 13`](appkit-release-notes-for-macos-13.md).

##### Accessory Security

###### New Features

- On portable Mac computers with Apple silicon, new USB and Thunderbolt accessories require user approval before the accessory can communicate with macOS for connections wired directly to the USB-C port. This doesn’t apply to power adapters, standalone displays, or connections to an approved hub. Devices can still charge if you choose Don’t Allow. You can change the security configuration in System Settings > Security and Privacy > Security. The initial configuration is Ask for new accessories. Configuring an accessibility Switch Control sets the policy to always allow accessory use. Approved devices can connect to a locked Mac for up to three days. Accessories attached during software update from prior versions of macOS are allowed automatically. New accessories attached prior to rebooting the Mac might enumerate and function, but won’t be remembered until connected to an unlocked Mac and explicitly approved. (43338666)

##### Endpoint Security

###### Known Issues

- Third-party security products using the Endpoint Security API might lose Full Disk Access authorization and stop functioning, even though the product remains visible in System Settings. This issue doesn’t affect authorization granted via MDM. (100857507)  Go to System Settings > Privacy & Security > Full Disk Access, select the security product, use the minus (-) button to remove, and then use the plus (+) button to re-add the affected security product. A system restart might be required to restore expected functionality.

##### File System

###### New Features

- There’s a change to the implementation of the `msdos` and `exfat` file systems. Apps that check for those specific file system formats might not detect them. Please file feedback if this impacts your app. (90768681)
- The `asr` utility won’t perform a volume replication of the booted macOS volume group without having the invoking app augmented with Full Disk Access privileges (or if SIP is disabled). The new requirement is to turn on Full Disk Access for the app in System Settings > Privacy & Security. (91764517)

##### Coregraphics

###### Deprecations

- To improve security, `CGImageCreate` enforces parameter correctness on macOS Ventura 13, iOS 16, iPadOS 16, watchOS 9, and tvOS 16. Passing an incorrect `CGImageByteOrderInfo` is no longer supported, and will result in images failing to load. (94855401)

##### Devicediscoveryui

###### Known Issues

- Devices running beta 4 or later aren’t backwards compatible with devices running earlier beta versions. (95233878)

##### Game Controller

###### New Features

- Many additional Bluetooth and USB game controllers are supported by the Game Controller framework on macOS 13, iOS 16, and tvOS 16 and later. (82409809)

##### Mail

###### Known Issues

- Moving a Remind Me message to another mailbox doesn’t remove the Remind Me banner. (93685824)

##### Memory Allocation

###### Known Issues

- In apps built with the macOS 13 SDK or later, the system memory allocator `free` operation zeroes out most deallocated blocks in macOS 13 beta or later. Invalid accesses to free memory might result in new crashes or corruption, including: - Read-after-free bugs that previously observed the old contents of a block may now observe zeroes instead
- Write-after-free bugs may now cause subsequent calls to `calloc` to return non-zero memory To debug these issues, use Address Sanitizer and Guard Malloc (see `libgmalloc(3)`). (97449075)

##### Metal

###### Known Issues

- The `MTLResource.gpuHandle` is deprecated. (92862429)  Use [`gpuResourceID`](https://developer.apple.com/documentation/Metal/MTLAccelerationStructure/gpuResourceID) instead, which functions as a replacement.

##### Metal Offline Compiler

###### Known Issues

- `MetalFX` effect outputs aren’t designed to be consumed by the CPU. Outputting to a texture that is read only by the CPU might result in synchronization issues. (91515075)  If a CPU reading of the `MetalFX` output is desired, instead of encoding the `MetalFX` effect as the last item in a command buffer, encode a dummy blit that consumes the `MetalFX` output texture (a 1-pixel region blit is fine) in the command buffer. After the command buffer with the dummy blit is finished, reading of the `MetalFX` effect output texture with CPU synchronizes correctly.

##### Networking

###### New Features

- Added `NSURLSession` support for client-certificate based authentication. (24523955)

- Added `URLSession` support for Private Access Tokens. (82937526)

###### Deprecations

- FTP is deprecated for `URLSession` and related APIs. Please adopt modern secure networking protocols such as HTTPS. (92623659)

##### Storekit

###### New Features

- All [`StoreKit`](https://developer.apple.com/documentation/StoreKit) APIs are now annotated for sendability and main actor isolation. (84157048)

- `Product` has new properties for localizing prices and subscription periods. For iOS 15, iPadOS 15, macOS 12, tvOS 15, and watchOS 8 or later use `priceFormatStyle` to format numbers derived from `price`. Use `subscriptionPeriodFormatStyle` to format durations of time relating to a subscription period. On iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9 or later use `subscriptionPeriodUnitFormatStyle` to format single units of a subscription period. (93780442)

- A property environment is included in [`Product.SubscriptionInfo.RenewalInfo`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo) and [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction). It represents the server environment in which the `RenewalInfo` and `Transaction` occurred, respectively. (85988753)

- [`AppTransaction`](https://developer.apple.com/documentation/StoreKit/AppTransaction) allows developers to cryptographically verify that the app was purchased on the App Store. (86739279)

- The `recentSubscriptionStartDate` property is included in [`Product.SubscriptionInfo.RenewalInfo`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo). It represents the date that marks the start of the most recent period of continuous subscription. A period is considered a continuous subscription if there’s no more than a 60-day gap between any two subscribed periods. (86599570)

- Present the offer code redemption sheet with the [`offerCodeRedemption(isPresented:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:)) view modifier in your SwiftUI apps. (85321941)

- The StoreKit Messages API allows you to control when App Store messages are displayed in your app. (85321880)

- Read the [`requestReview`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/requestReview) environment value to get an instance of a [`RequestReviewAction`](https://developer.apple.com/documentation/StoreKit/RequestReviewAction). Then, call this instance to request to display a review prompt from your SwiftUI apps. (86739003)

###### Deprecations

- Deprecated the SKDownload API and removed the option to upload nonconsumable in-app purchase assets for Apple to host. In addition, support for managing these assets in App Store Connect is no longer available as of April 2022. (89764253)

##### Swift

###### Known Issues

- `Network.framework` resolved an issue that could cause `NWBrowser`, `NWConnection`, `NWConnectionGroup`, `NWEthernetChannel`, `NWListener`, and `NWPathMonitor` to trigger a retain cycle when various Handler blocks are set. Starting with macOS 13, iOS 16, watchOS 9, and tvOS 16, if software using `Network.framework` targets these releases as the minimum OS, the object releases any blocks they captured once cancelled, breaking the retain cycle. (89677097)  For software targeting older versions, the retain cycle can be broken by setting the handler blocks to `nil` after canceling the object.

##### Swiftui

###### New Features

- Custom types conforming to `ToolbarContent` now support dynamic properties like `@Environment`. (94117842)

- You can now place a [`TextField`](https://developer.apple.com/documentation/SwiftUI/TextField) in an [`Alert`](https://developer.apple.com/documentation/SwiftUI/Alert) by using `alert` modifiers that accept a [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder). (64819930)

- For `control`, [`Section`](https://developer.apple.com/documentation/SwiftUI/Section), or other views that have a [`Label`](https://developer.apple.com/documentation/SwiftUI/Label), the [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder) content now automatically arranges and styles multiple views as hierarchical elements, such as `title` and `subtitle`. If the `label` views are intended to be arranged horizontally rather than hierarchically, wrap the views within an [`HStack`](https://developer.apple.com/documentation/SwiftUI/HStack). (85184563)

- A `TextField` supports multiline text. Use a [`Axis.vertical`](https://developer.apple.com/documentation/SwiftUI/Axis/vertical) axis on a text field to allow rendering of multiple lines in contexts like forms, where text is expected to be short to medium length. For long-form text editing, continue to use a [`TextEditor`](https://developer.apple.com/documentation/SwiftUI/TextEditor). (51463718)

- A `list` supports Section footers. (78462739)
- When presenting a `sheet` or `window`, SwiftUI now uses focus state bindings to determine where focus should be placed by default. Clients can specify a custom binding assignment using the new  `View.defaultFocus(_:_:)` modifier. (81837128)
- Applying `View.focusable(false)` to a container now also disables focus for the container’s contents. (89362190)
- An alert presented using an `Error` displays as a critical alert, which shows a caution symbol with the app icon overlaid. (82014147)
- Lists and tables automatically support type-to-select, using the first `Text` content in each cell. (85956291)
- Windows created using SwiftUI no longer have a maximum size by default. The user can resize them to fill the screen. To enforce a maximum size, use the `.windowResizability(.contentSize)` modifier. (92634133)

###### Known Issues

- Providing actions to a `navigationTitle` modifier has been deprecated. Use the `toolbarTitleActions()` modifier or `ToolbarTitleActions` type in a toolbar modifier instead. (93658035)

##### Texts and Fonts

###### Deprecations

- ATS and ATSUI APIs are fully deprecated. Code using these APIs will fail to compile and link when the deployment target is set to 13. Code targeting earlier versions of macOS will continue to compile, link, and run. macOS 13 is the last release where code depending on ATS or ATSUI will run. All runtime functionality will be removed in next major release of macOS. (83581159)

##### Wallet

###### Known Issues

- American Express cards might need to be removed and re-added to Wallet after updating to macOS 13 beta 6 or later. (97990752)

## See Also

- [macOS Ventura 13.5 Release Notes](macos-13_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.4 Release Notes](macos-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.3 Release Notes](macos-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.2 Release Notes](macos-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.1 Release Notes](macos-13_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-13-release-notes)*