# Xcode 27 Beta 3 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 27 beta 3 includes Swift 6.4 and SDKs for iOS 27, iPadOS 27, tvOS 27, watchOS 27, macOS 27, and visionOS 27. Xcode 27 beta 3 supports on-device debugging in iOS 17 and later, tvOS 17 and later, watchOS 10 and later, and visionOS. Xcode 27 beta 3 requires a Mac running macOS Tahoe 26.4 or later.

See [`Xcode Support`](https://developer.apple.comhttps://developer.apple.com/support/xcode/) to learn more about compatible platforms and deployment targets.

##### General

###### Known Issues

- When streaming `stdout` and `stderr` from multiple processes at the same time (for example: in parallel testing scenarios), the results may be significantly delayed.  (165098287)

##### Address Sanitizer

###### Known Issues

- Address Sanitizer might fail to launch on iOS 27.0, tvOS 27.0, watchOS 27.0, and visionOS 27.0 when building with Xcode 26.4 or older.  (178072780) **Workaround:** Use Xcode 26.5 or later when testing applications with Address Sanitizer.

##### Background Assets

###### Resolved Issues

- Fixed: The packaging tool, ba-package, may generate an invalid asset-pack archive when you specify an on-demand download policy.  (179168553) (FB23020247)

##### Carplay Simulator

###### Resolved Issues

- Fixed: Cannot start a CarPlay connection with CarPlay Simulator when accessed via Device Hub.  (179523697)

##### Coding Intelligence

###### New Features

- Xcode build and test MCP tools now send dynamic activity status instead of static text to external MCP clients.  (181078347)

###### Known Issues

- If the plan-mode confirmation bar (“Implement the plan?” with Yes/No buttons) appears while the agent is still streaming a response, clicking either button may trigger a new agent turn on top of the in-flight one, leaving the conversation in an inconsistent state. As a workaround, wait for the agent to finish responding before confirming or dismissing the plan.  (178673449)

##### Core Ai

###### Known Issues

- The option to extract inputs from prediction events in the Core AI gauge in Xcode may not work reliably.  (172502576)

##### Device Hub

###### Resolved Issues

- Fixed: The ‘VoiceOver’ toggle in the appearance settings inspector does not enable voiceover on the device.  (173507341)
- Fixed: The “Text Size” in the appearance inspector disappears if one of larger text sizes from Accessibility is being used.  (175365925)
- Fixed: In some circumstances, when using “Simulate Mouse or Trackpad” with an iPad, physical or simulated, the mouse pointer can appear at a different place on the screen than the Mac pointer.  (178575823)
- Fixed: The ‘Color Filter’ option in the appearance settings inspector works for simulators.  (178854926)
- Fixed: Device Hub allows you to enter resize mode with an app linked against an iOS 26 or earlier SDK, which is unsupported and may result in Device Hub showing a black screen for the device.  (179416769)
- Fixed: If you exit Device Hub’s resize mode through means other than the toolbar button or menu item (e.g. if your resized app crashes or is backgrounded) the device’s screen content will be incorrectly sized until it is rebooted.  (179991750)

###### Known Issues

- Connecting a game controller to a simulator or device is only supported for the visionOS simulator.  (109362811)
- Viewing the video from, or sending inputs to, a physical Apple Vision Pro is not supported in Device Hub 27. All other Device Hub features, like changing settings, DeviceFS, and so forth, are supported.  (142582218) **Workaround:** Use AirPlay from the Apple Vision Pro to view the video remotely.
- Device Hub doesn’t currently support sending a two-finger touch to a device or simulator.  (169537162)
- The Controls->Shake menu item does not work.  (171282777)
- Sound Output and Input for simulators cannot be set to None.  (175714711)
- When the tab bar is visible, controls at the very top of the inspector might not respond to clicks.  (176507876)
- When running parallel testing in simulators, devices may not be visible in Device Hub but are still actively running tests.  (176809181) **Workaround:** Disable parallelized test runs if you want to watch UI tests executing in simulators.
- When a color filter is set on a physical device, the filter is not visible in Device Hub.  (178121876)
- The “Simulate Hardware Keyboard” menu item does not work correctly. In some instances, the software keyboard will appear, or the suggestions bar will not appear.  (178196115)
- With iPad Simulators running iOS 27.0, the “Toggle Software Keyboard” menu item does not work.  (178432770)
- After switching to Device Hub’s compact view, a visionOS simulator may show a black screen until Device Hub is relaunched.  (178567811)
- With Apple Watch - simulator or physical - scrolling with the mouse pointer over the watch face does not emulate rotating the digital crown.  (179079031) (FB22992052) **Workaround:** Move the pointer over the crown in the device bezel.
- visionOS simulator takes longer to boot than expected and may stall when deploying an app.  (180078336) **Workaround:** Please reboot your machine.

##### Devicectl

###### Resolved Issues

- Fixed: The –show flag has been removed from the ‘devicectl device info details’ command. Instead we will always provide the full set of device properties in the textual output and JSON (under the ‘properties’ dictionary).  (179880477)

##### Instruments

###### New Features

- Runs and Comparisons can now be bulk-deleted by using multi-selection and the `Delete` menu item or context menu.  (179565486) (FB23120864)
- `xctrace export` allows for specifying files like .atrc and .logarchive as input, removing the need for two-step process of running `xctrace import` followed by `xctrace export`.  (179742657)

###### Resolved Issues

- Fixed: Resolved a bug where swift concurrency backtraces often included completeTaskAndRelease (or similar concurrency mechanics) at the end of the backtrace.  (142883863)
- Fixed an issue where the resize cursor would sometimes not appear when resizing the sidebar or inspector.  (172306622)

##### Interface Builder

###### Resolved Issues

- Fixed: A `TVCardView` loaded from a storyboard or xib may render incorrectly at runtime.  (179781291) (FB23188951)
- Fixed: Compiled documents with text input views containing a non-nil “Password Rule” value fail to load at runtime.  (180420035) (FB23351677)
- Fixed: `ibtool` fails to compile documents with non-adaptive “Popover” or “Replace” segues.  (180632487) (FB23399800)

##### Localization

###### New Features

- You can now annotate translations in String Catalog artifacts when using agents to translate strings.  (176407208)
- Strings newly added to String Catalogs now appear as artifacts when agents use the “Prepare Project for Localization” tool.  (176497701)

###### Resolved Issues

- Fixed an issue where strings inside availability-constrained `#Preview` macros would not be excluded from String Catalogs.  (176188980) (FB22696182)
- Fixed: Resolved an issue where Xcode may not have been able to reference the usage location for newly-extracted strings during agentic translation.  (179729079)

##### Previews

###### Resolved Issues

- Fixed an issue where the crash screen for a watchOS preview appeared with a light background instead of the expected dark appearance.  (146868878)

###### Deprecations in Xcode 27 Beta 3

- PreviewProvider and its family of preview modifiers  (144168701)

##### Previews Playgrounds

###### Resolved Issues

- Fixed: A clearer error message is now shown when building a preview times out.  (178756436)
- Fixed: Reduced number of canvas errors that would be flagged as potentially caused by a crash.  (179124669)
- Fixed: Errors encountered when using RenderPreview and ExecuteSnippet MCP tools now include full diagnostic details from the underlying failure.  (179318912)
- Fixed a rare display setup-related issue where the first update to a preview could fail immediately after the preview launched.  (179411046)

###### Known Issues

- Standalone Swift files opened by double-clicking in Finder may fail to run #Playground or #Preview blocks.  (177587795) **Workaround:** Open Swift files using File>Open… or drag them directly onto the Dock icon.

##### Security

###### New Features

- The new “adopt-c-bounds-safety” Code Intelligence skill can help you adopt the bounds safety extension for C (-fbounds-safety) with a file-by-file adoption workflow. For more information about the C bounds safety extension, see https://developer.apple.com/documentation/xcode/enabling-enhanced-security-for-your-app#Adopt-bounds-checking-in-C.  (177739344)
- The new “audit-xcode-security-settings” Code Intelligence skill can help you audit your app to suggest enabling additional security-oriented build settings and entitlements. For more information on these settings, see https://developer.apple.com/documentation/xcode/enabling-enhanced-security-for-your-app  (181104536)

##### Simulator

###### New Features

- The simulator runtimes now contain a pre-built dyld cache. This will make first launch of a simulator much faster.  (179846743)

###### Resolved Issues

- Fixed: Accessibility Inspector cannot inspect elements in simulators.    (179033881) (FB22976268)

###### Known Issues

- An extra control for keyboard capture mode appears in the Device Hub toolbar under the view for the visionOS simulator.  (177082480)
- An extra control for Simulate Trackpad or Mouse mode appears in the Device Hub toolbar under the view for the visionOS simulator.  (177086926)
- The simulator sometimes does not get cleared after deletion.   (178661525) **Workaround:** Restart the machine and re-attempt to remove it.

##### Storekit Testing in Xcode

###### Resolved Issues

- Fixed: Inspecting transaction details for a subscription suite purchase in the Transaction Manager displays incorrect product information.  (179413970)

##### System

###### Resolved Issues

- Fixed: Custom `FilePath` or `FileDescriptor` extensions that make unqualified calls to `stat()` or `stat(_)` (without the `Darwin.` qualification) might conflict with the new Swift `stat()` instance methods introduced in [`SYS-0006`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0006-system-stat.md), causing build errors. See [`SYS-0008`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0008-backdeploy-cinterop-stat.md) for more details.  (177911316)

##### Testing

###### Resolved Issues

- Fixed: Test issues with warning severity now appear in the console.  (161919593)
- Fixed: An expected Swift Testing exit test process termination may cause a test failure to be recorded incorrectly during a UI test.  (174032826)

##### Themes

###### New Features

- Customized and imported themes are now stored on disk alongside legacy theme files.  (177747192)

##### Xcode

###### Known Issues

- If you installed Xcode 27 beta on macOS Tahoe 26.5.1 and earlier, macOS virtual machine installation will fail due to a known bug. To restore virtual machine installation functionality follow the [`How to reinstall macOS guide.`](https://developer.apple.comhttps://support.apple.com/en-us/102655)  (179068335)

##### Xctest

###### New Features

- XCTest now includes XCUIVoiceOverService, a new UI testing API for verifying VoiceOver behavior in your app. Use it to drive VoiceOver from UI tests and validate focus, spoken output, and navigation across supported platforms.  (175858549)

#### Updates in Xcode 27 Beta 2

##### App Intents

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: Siri might generate unexpected responses when attempting to trigger an AppShortcut phrase with an App enum value.  (174869053)

##### Coding Intelligence

###### New Features in Xcode 27 Beta 2

- The Preview Snapshot MCP tool now returns information about the platform, device type, and operating system version of the Simulator that rendered the preview.  (177076406)

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: ACP agents added as part of agent plug-ins may not be removed from Xcode’s UI until relaunching Xcode.  (178771195)
- Fixed: If a deep link targeting the new beta is invoked on a system where an older version is set as the active developer tool, the link will be claimed by the older installation rather than the beta.  (179126594)
- Fixed: Apple-authored agent skills may not be available to Codex.  (179171480)

##### Console

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: Console may fail to scroll fully to the bottom while output is streaming.  (175800015)

##### Core Ai

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: The number of parameters displayed in the Core AI model view in Xcode is inaccurate for models with multiple functions that share parameters.  (177784390)
- Fixed: When Metal API Validation is enabled, CoreAI models might fail to execute.  (177991751)

##### Debugging

###### New Features in Xcode 27 Beta 2

- LLDB now ships with an MCP server (lldb-mcp). See https://lldb.llvm.org/use/mcp.html for examples.  (176901842)

##### Developer Documentation

###### New Features in Xcode 27 Beta 2

- You can now use natural language to search the developer documentation. Matching documents will be returned based on semantic matching.  (165476491)

##### Device Hub

###### New Features in Xcode 27 Beta 2

- Common Mac mouse and trackpad gestures such as scrolling, pinching, and rotating now work with standard UIKit components on iOS devices, either physical or simulated. When scrolling with a pointing device, `UIEvent.EventType.scroll` is emitted. When pinching or rotating with a trackpad, `UIEvent.EventType.transform` is emitted. As a result of these pointer-based events being emitted, you may see `UIPointerInteraction` effects applied based on where the pointer is located in your app. Additionally, clicking with a mouse or trackpad produces a simulated finger touch of type `UITouch.TouchType.direct` rather than `UITouch.TouchType.indirectPointer`. This hybrid behavior has been added for ease of use for Device Hub, and does not reflect functionality available on physical devices. To validate your app’s full pointer behavior, select “Simulate Trackpad or Mouse” from the Device menu, test on a physical iPad with a paired pointing device, or use iPhone Mirroring.  (48372360) (FB5341466)
- Device Hub adds a new way to pair iPhone, iPad and Apple Watch running iOS 27/iPadOS 27/watchOS 27 and later over a network. This allows you to pair iPhones and iPads without requiring a cable, and provides a more reliable experience for pairing watches. To get started, click the + button in Device Hub’s sidebar then select “Pair Nearby Device…”, or refer to the documentation at https://developer.apple.com/documentation/xcode/managing-your-simulated-and-physical-devices-in-device-hub  (179418483)

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: Renaming a device in Device Hub may cut off the renaming prematurely.  (178477422)
- Fixed: Renaming a device now works properly if the sidebar is not visible  (178538834)
- Fixed: Added a preference to control whether key combos are sent to Device Hub or to the remote device: ```None
 defaults -container com.apple.dt.Devices write com.apple.dt.Devices hostKeybindingPolicy -int <value>
``` - 0 - Device Hub uses rich key combos shortcuts - 1 - Minimized when interacting with device
- 2 - Device Hub uses minimal key combo shortcuts  (178920247)
- Fixed: When pasteboard data takes longer than 5s to transfer (eg: misbehaving apps serving data, data taking a long time to process, or large data taking a long time to transfer), resolution will now only block apps attempting to paste for up to 5s.  After the 5s timeout, the paste will fail but data will continue to be transferred in the background such that the paste can be retried and will succeed after the data has been transferred.  (179132581)
- Fixed: Improved reliability of pasteboard synchronization  (179200521)
- Fixed: Device Hub synchronization no longer attempts to synchronize pasteboard data provided by Universal Clipboard  (179287395)
- Fixed: If the user specified a location to save screenshots from Simulator, Device Hub will honor that location before falling back to the global default screenshot location. Preference order: com.apple.dt.devices screenCaptureLocation com.apple.iphonesimulator ScreenShotSaveLocation com.apple.screencapture location  (179402694)

##### Devicectl

###### New Features in Xcode 27 Beta 2

- –json-output now fully supports passing JSON output to stdout. See devicectl –help for more details.  (63583278)

##### Instruments

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: Instruments crashes when opening ‘Task Creation Calltree’ view in the ‘Swift Tasks’ instrument or ‘Change Call Trees’ view in the ‘SwiftUI’ instrument.  (178067883)
- Fixed an issue where the instrument library popover would not be large enough to show the full descriptions of all instruments. (FB23116314)  (178280966)
- Fixed a crash that occurred when opening a trace document while a run was zoomed to the maximum zoom level.  (178444923)

##### Interface Builder

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: Xcode Settings > Components incorrectly showed a ‘Get’ button for simulators already downloaded and used with Rosetta.  (179042726) (FB22978644)

##### Metal

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: An app may crash when run from Xcode with both Hardware Memory Tagging and GPU Frame Capture enabled.  (178488388)

##### Musickit

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: `MusicPlayer.Queue` and `MusicPlayer.State` might not always update when using `@State` in SwiftUI.  (176947544)

##### Previews

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: When a RenderPreview fails because of an earlier and cached failure, the original error is now returned.  (176817467)
- Fixed: Attempting to Preview with an uninstalled runtime now shows a placeholder view rather than silently and incorrectly falling back to macOS.  (177007609)
- Fixed: Code inside #Preview now explicitly runs on the main actor, so it can call main-actor-isolated APIs without producing concurrency warnings or runtime check failures.  (177394870)
- Fixed: iOS previews in Resizable Canvas mode no longer constrained to specific size ratios.  (177448190)
- Fixed an issue where keyboard input was not delivered to previews running in the iOS Simulator in certain configurations.  (177679215)
- Fixed an incorrect error banner that could appear while using macOS’s Run as App preview feature (via the Live canvas mode button menu).  (178092213)

##### Previews Playgrounds

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: A clearer error is now shown when the canvas can’t access files in restricted macOS locations (such as Desktop, Documents, or Downloads) because Xcode has not been granted access.  (176989186)
- Fixed: Failed previews due to crashes now more frequently contain complete diagnostic information.  (177011651)
- Fixed an issue where previews could fail to build for targets that use the swiftc linker driver.  (177021285)
- Fixed a rare crash that could occur while updating a preview.  (178097583)

##### Simulator

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: CoreSimulator logs are now rotated continually rather than only at CoreSimulatorService process start, preventing unbounded log growth on systems with long uptime.  (177785650)
- Fixed: After rebooting a running visionOS simulator, the ability to interact with the simulator is lost.  (178635793)

##### Storekit Testing in Xcode

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: StoreKit Testing in Xcode configurations that sync with App Store Connect display incorrect commitmentInfo for monthly subscriptions with a 12-month commitment.  (178269160)

##### Testing

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: When running tests with the swift CLI, cross-framework issues from XCTest are not surfaced when running Swift Testing tests in Swift Package projects.  (177970158)
- Fixed: watchOS Unit and UI tests may not run on device.  (178874363)

##### Usdkit

###### Deprecations in Xcode 27 Beta 2

- Meshes compressed using the USDKit export API or `usdcrush tool` in Beta 1 cannot be decoded by Beta 2, and  meshes from Beta 2 cannot be decoded by Beta 1.  (177417812)

##### Wi Fi Aware

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: `wifiAware` and `wifiAware(_:)` extensions on NWParameters are unavailable for configuring Wi-Fi Aware properties.  (178019157)

##### Xcode

###### Resolved Issues in Xcode 27 Beta 2

- Fixed: Devices used for development on a Mac without Xcode 27 installed remain compatible for development on Macs which have not upgraded to Xcode 27 without needing to reboot.  (179359489) (FB23066098)

#### Updates in Xcode 27 Beta

##### General

###### Resolved Issues in Xcode 27 Beta

- Fixed: The scheme action toolbar button now treats ‘without building’ variants, obtained by holding the Control key, as a one-shot operation and reverts to the normal build-then-perform action when no modifiers are used.  (12239704)
- Fixed: Due to a timing issue with the installation package, Simulator devices may not appear in Device Hub.  (179040327) (FB22978070)

##### Apple Clang Compiler

###### New Features in Xcode 27 Beta

- You can now annotate C++ operators declared within classes using API Notes. For example: ```None
 Tags:
 - Name: MyTag
   Methods:
   - Name: operator+
     Availability: none
``` (148534260)

##### Background Assets

###### New Features in Xcode 27 Beta

- Asset-pack manifests now support path wildcards, file exclusion, hard-coded source roots, and custom destination subpaths.  (163943159)
- You can reduce your app’s storage usage with localized asset packs. The system delivers the appropriately localized asset packs based on the user’s preferred languages.  (163944365)
- Use the new Steam Asset Converter to convert your Steam “depots” into asset packs.  (163953178)

###### Resolved Issues in Xcode 27 Beta

- Fixed: Xcode can now serve asset packs to your app while debugging on devices by setting a Background Asset Packs folder in the Run scheme action’s Options tab.  (165230494)

##### C++ Standard Library

###### New Features in Xcode 27 Beta

- The following C++ papers have been implemented: - Hashing support for `std::chrono` value classes ([`P2592R3`](https://developer.apple.comhttps://wg21.link/P2592R3))
- `zip` ([`P2321R2`](https://developer.apple.comhttps://wg21.link/P2321R2))
- `std::optional<T&>` ([`P2988R12`](https://developer.apple.comhttps://wg21.link/P2988R12))
- sub-`string_view` from `string` ([`P3044R2`](https://developer.apple.comhttps://wg21.link/P3044R2))
- Making `std::istream::ignore` less surprising ([`P3223R2`](https://developer.apple.comhttps://wg21.link/P3223R2))
- Add `std::views::indices(n)` ([`P3060R3`](https://developer.apple.comhttps://wg21.link/P3060R3))
- Move-only types for `equality_comparable_with`, `totally_ordered_with`, and `three_way_comparable_with` ([`P2404R3`](https://developer.apple.comhttps://wg21.link/P2404R3))
- Checking if a `union` alternative is active ([`P2641R4`](https://developer.apple.comhttps://wg21.link/P2641R4)(`std::is_within_lifetime`))
- Expose `std::atomic_ref`’s object address ([`P2835R7`](https://developer.apple.comhttps://wg21.link/P2835R7))
- Comparisons for `reference_wrapper` ([`P2944R3`](https://developer.apple.comhttps://wg21.link/P2944R3))
- Give `std::optional` Range Support (guarded by `-fexperimental-library`) ([`P3168R2`](https://developer.apple.comhttps://wg21.link/P3168R2))
- Fixes to `flat_map` and `flat_set` ([`P3567R2`](https://developer.apple.comhttps://wg21.link/P3567R2))
- Make `optional<T&>` trivially copyable ([`P3836R2`](https://developer.apple.comhttps://wg21.link/P3836R2))
- Library Support for Expansion Statements ([`P1789R3`](https://developer.apple.comhttps://wg21.link/P1789R3)) Performance improvements: - The performance of associative and unordered containers has been significantly improved, with some functions showing improvement of up to 11x.
- The performance of many algorithms has been improved (including `std::find`, `std::for_each`|`ranges::for_each` for associative containers, `std::rotate`), resulting in a performance improvement of up to 3x.
- `{std,ranges}::{generate, generate_n}`, `{std,ranges}::{fill, fill_n}` and `{std,ranges}::distance` have been specifically optimized for segmented iterators, resulting in a performance improvement of up to 10x (and even up to 1600x for `distance` on non-random-access iterators).
- `std::search_n` for random access iterators now tries to skip elements, resulting in a significant performance improvement (up to 70,000x in contrived cases).
- The `vector<bool>::reserve()` algorithm has been optimized, resulting in a performance improvement of up to 2x.
- `num_get::do_get` integral overloads have been optimized, resulting in a performance improvement of up to 2.8x.
- Some reallocations are now avoided in `std::filesystem::path::lexically_relative`, resulting in a performance improvement of up to 1.7x.
- `ofstream::write` now passes large strings to system calls directly instead of copying them in chunks into a buffer. Miscellaneous improvements: - Multiple internal types have been refactored to use `[[no_unique_address]]`, resulting in faster compile times and reduced debug information.
- `std::align` is now an inline function, which allows the compiler to better optimize calls to it.
- `std::atomic::wait` has been refactored to accept more types to use platform native wait functions directly. This is guarded behind the ABI Macro `_LIBCPP_ABI_ATOMIC_WAIT_NATIVE_BY_SIZE`.  (178191000)

###### Deprecations in Xcode 27 Beta

- The following items have been deprecated or removed: - The minimum supported deployment target on macOS for the C++ standard library has been increased to 11.0. Potentially breaking changes: - The algorithm for `multi{map,set}::find` has been modified so that it doesn’t necessarily return an iterator to the first equal element in the container. This was never guaranteed by the Standard, but libc++ previously happened to always return the first equal element. Starting with this release, code relying on the first element being returned from `find` will be broken, and `lower_bound` or `equal_range` should be used instead.
- The algorithms for `std::{map,set}` `lower_bound` and `upper_bound` operations were modified so that their result changed for comparators that are not a strict weak order. Being a strict weak order was always a requirement of the Standard and still is, however in this release libc++ changes the behavior of `std::{map,set}` for such comparators. Since this may be tricky to work around in some cases, an escape hatch is provided in this release: defining `_LIBCPP_ENABLE_LEGACY_TREE_LOWER_UPPER_BOUND` will revert to the historical implementation of these operations. That escape hatch will be removed in an upcoming release (likely in the next release).
- The ABI flag `_LIBCPP_ABI_NO_REVERSE_ITERATOR_SECOND_MEMBER` has been split off from `_LIBCPP_ABI_NO_ITERATOR_BASES`. If you are using this flag and require ABI stability, you should set `_LIBCPP_ABI_NO_REVERSE_ITERATOR_SECOND_MEMBER` as well. ABI-affecting changes: - The ABI flag `_LIBCPP_ABI_NO_REVERSE_ITERATOR_SECOND_MEMBER` has been split off from `_LIBCPP_ABI_NO_ITERATOR_BASES`. If you are using this flag and require ABI stability, you should set `_LIBCPP_ABI_NO_REVERSE_ITERATOR_SECOND_MEMBER` as well.
- The internal types `__map_value_compare`, `__unordered_map_hasher`, `__unordered_map_equal`, `__hash_map_hasher` and `__hash_map_equal` have been refactored to use `_LIBCPP_COMPRESSED_ELEMENT` instead of potentially inheriting from the types they wrap. At this point in time we are not aware of any ABI changes caused by this.
- `ranges::iota_view` is now aware of `__int128`. This causes `iota_view::difference_type` to change from `long long` to `__int128` in some cases.
- `std::allocator` is now trivially default-constructible. The behaviour can be reverted by defining `_LIBCPP_DEPRECATED_ABI_NON_TRIVIAL_ALLOCATOR`. This compatibility macro is going to be removed in an upcoming release.
- `bitset::operator[]` now returns `bool`, making libc++ conform to the Standard. The behaviour can be reverted by defining `_LIBCPP_DEPRECATED_ABI_BITSET_CONST_SUBSCRIPT_RETURN_REF`. This compatibility macro is going to be removed in an upcoming release.  (178191050)

##### Coding Intelligence

###### New Features in Xcode 27 Beta

- Google Gemini is now available in the coding assistant.  (171990272)
- Planning with agents is now first class in Xcode. Plans appear as editable Markdown artifacts next to the conversation. You can use dedicated UI to review, annotate, discuss changes to the plan, and approve before the agent proceeds.  (172857081)
- The Coding Assistant sidebar is now dedicated to displaying and organizing your conversations with real-time status and unread indicators, drag-and-drop grouping, archiving, and renaming. See at a glance which conversations are active or waiting for user input, and jump between them without losing context. Select multiple conversations to group, archive, or delete them in bulk. The context menu allows for opening conversations in new tabs, windows, or editor panes.  (172926345)
- The Preview Snapshot MCP tool can now render variants such as light/dark appearance, portrait/landscape orientation, and various type size overrides. It also supports specifying timelines for Widgets and toggle states for Live Activities. Taken together, this gives agents more flexibility in how they render previews in your codebase.  (172961797)
- Agents can now boot simulators, install and launch apps, synthesize touch events, and capture screenshots to verify UI behavior.  (175179787)
- Added new MCP tools to read, plan, and edit translations in String Catalog files.  (176376425)
- The toolbar now has a “New Conversation” button that lets you start a fresh conversation from anywhere in Xcode. When conversations are active, it shows a status indicator for easy monitoring at a glance. Click the status indicator to jump directly to the next conversation that needs attention.  (176385678)
- The Xcode MCP server has been updated with new tools that allow agents to debug projects by manipulating the active run state, interacting with and reading the contents of the debugger console; listing and switching between available schemes and run destinations and inspecting and modifying build settings, compiler flags, entitlements, and Info.plist keys.  (176935844)
- Agents in Xcode now have access to insights about your projects, such as crashes, disk writes, energy, hangs and launch issues impacting your app, helping reduce the time it takes to ship a fix.  (177568662)
- The coding assistant has moved out of the navigator into the editor area, with a completely redesigned conversation transcript. Agent-generated artifacts, like code diffs, plans, and SwiftUI preview snapshots, appear alongside the transcript, and annotations on code snippets and plan documents let you give targeted inline feedback without leaving context.  (178288550)
- Xcode now ships with Apple-built specialists for targeted tasks, like localization, UIKit resizing and accessibility.  (178289150)
- Agents in Xcode can now be extended with plugins that contain skills, MCP servers, and ACP agent configurations. Skills are invokable as slash commands with completion support.  (178289210)
- Coding Intelligence now includes a new security layer that monitors and controls filesystem access by coding agents and any processes they spawn. This can be enabled in Coding Intelligence settings.  (178289431)
- Xcode adds support for the Agent Client protocol.  (178294840)
- Agent Plug-ins can show custom icons and tool names for MCP servers they define by adding additional _meta fields to their JSON definitions. ```None
 {
   "name": "MyGreatPlugin",
   "description": "An awesome MCP server configuration.",
   "version": "1.0.0",
   "mcpServers": {
     "MyGreatMCP": {
       "type": "http",
       "url": "...",
       "tools": [
         "*"
       ],
       "_meta": {
         "ideToolIconPath": "./icon.svg",
         "ideToolIconRendersAsTemplate": true,
         "ideToolTitles": {
           "whoami": "Who Am I",
                 "get-current-email": "Get Current Email Message" 
         }
       }
     }
   }
 }
``` (178470032)

###### Resolved Issues in Xcode 27 Beta

- Fixed: Buttons in the Coding Assistant’s prompt area now use more accessible labels and descriptions.  (177462284)
- Fixed VoiceOver getting trapped in the Coding Assistant prompt area.  (177462397)

##### Debugging

###### New Features in Xcode 27 Beta

- In projects using bridging headers, LLDB can now directly import explicitly built Swift modules and PCH from DerivedData. This can dramatically speed up the first expression or `po` in a debug session involving a bridging header. (168272248)
- LLDB now provides a `language swift task tree` command, which prints a tree of all the Swift Tasks the debugger knows about. For more information, see the output of `help language swift task tree`.  (169471480)

##### File Template for Launch Tests

###### New Features in Xcode 27 Beta

- Added a file template for launch tests that opts into `runsForEachTargetApplicationUIConfiguration`, so the test runs across every combination of orientation, localization, and appearance your app supports.  (168770106)

##### Foundation

###### Resolved Issues in Xcode 27 Beta

- Fixed: `+[NSURL URLWithString:]` no longer double-encodes the `%` of valid percent-escape sequences when encoding other invalid characters.  (161588649) (FB20439045)

##### Icon Composer

###### New Features in Xcode 27 Beta

- Icon Composer 2.0 supports a new sharper rendering mode for upcoming 2027 operating systems with support for refractivity, outside specular, and deeper shadows. Use the group inspector to edit the new properties, and the toolbar to preview in either the new or original design generation. When your icon looks great in both design generations, add it to your Xcode project and it will be used for all OS versions.  (172404678)

##### Instruments

###### New Features in Xcode 27 Beta

- `xctrace record` allows you to pass recording options for Instruments from within the CLI. Use `--show-recording-options` to print available options for a template or instrument as a JSON. Pass a modified JSON file with customized options using `--recording-options <json path>`.  (47649405) (FB5336460)
- Summary views in Instruments allows you to select multiple rows and copy the content.  (50558735)
- Instruments no longer rescales graphs to reflect the local maximum when the visible timeline region changes to simplify comparison of data across the tracks. To trigger manual rescaling to the current viewport, use View → Rescale menu item.  (60970746)
- Instruments now restores pinned tracks from the previous run when recording a new run. You can also save and restore pinned tracks explicitly using View → Track States menu actions.  (69098114)
- System Trace now unifies system calls, VM faults, and thread states into a single plot. When zoomed out, a new blending algorithm summarizes activity so dense regions remain readable. You can follow the chain of scheduling events for a thread using left/right key navigation. The inspector panel shows details about each event, providing quick actions like pinning a thread that made another thread runnable.  (163589543)
- Foundation Models Instrument now helps you trace and debug Foundation Models usage in your app with quick inspection of instructions, prompts, responses, token usage, and inference performance.  (164223804)
- A new inspector displays information about the selected event and provides quick actions for pinning or filtering tracks and filtering the detail view.  (165724281)
- Swift Concurrency: Tasks, Collections, Actors and Executors now have a detail option “Profile” which displays Call Tree made of profiling data captured while in state Running. This detail is only visible when recording with the Swift Concurrency instrument alongside Time Profiler or CPU Profiler.  (168542912)
- When recording os_log Instrument together with an Instrument that creates process or thread tracks (like Time Profiler, CPU Profiler, or others), you can now overlay logging information on these tracks by enabling “os_log” graph in the “Track Graph Display” popover.  (170113899)
- A new Swift Executors instrument is now available. It displays tracks for the Cooperative Thread Pool, the Main Actor, and any types conforming to TaskExecutor or SerialExecutor. Instruments properly captures and displays on iOS 27, iPadOS 27, macOS 27, tvOS 27, watchOS 27, visionOS 27. On older systems, executor names fall back to “Unknown executor”.  (171189428)
- Swift Concurrency Task tracks now appear in new “Swift Task Collection” tracks. Instruments sorts Tasks into Collections based on their name or place of creation. You can switch Collection tracks between displaying task lifetimes and task states.  (173885662)
- When opening files like `.atrc` or `.logarchive`, you can now specify a preferred template using ‘Settings → General → Templates for Import’  (58151217)
- New setting in the ‘General’ tab allows for overriding preferred template used for opening files such as .atrc or .logarchive.  (73868296)
- Call Tree and Top Functions tables now persist selected rows.  (120794625)
- Individual backtraces shown in the inspector now offer improved collapsing logic and are more consistent with the call tree’s “Heaviest Stack Trace” view.  (130279660)
- When a profiled process terminates, the timeline view displays a flag showing the termination reason and exit code.  (130528710)
- SwiftUI instrument adds a “Summary of Updates” focus action to the View Hierarchy detail view that makes it easier to see details about what updates a view in the view hierarchy is performing.  (147328805)
- Allocations instrument now visualizes tagged allocations when a process is running with Memory Integrity Enforcement with a ‘(tagged)’ suffix.  ‘Statistics’ view contains opt-in columns to view the count and total size of these allocations in aggregate.  (149409607)
- States annotated with the StateReporting API are visible in Instruments as part of the Points of Interest instrument track. Expand top level track to inspect all captured domains and state transitions.  (159709795)
- The SwiftUI instrument now records additional information about layout passes and the reasons a layout computation wasn’t cached.  (162137231)
- Animation Hitches instrument now supports visionOS on devices running visionOS 27.0 or later.  (163315840)
- You can now drag and drop files such as `.atrc`, `.logarchive`, or `.sample` onto the Instruments sidebar. This action creates a run for each of the imported files.  (167697855)
- The interface to enable and disable graphs on tracks in the Instruments timeline now uses checkboxes to quickly toggle graph visibility on or off.  (168232126)
- Swift Concurrency: When recording all processes, Tasks and Executors are now grouped in process hierarchies.  (168542643)
- Swift Concurrency: Selecting a bar chart interval in an Actor or Executor Queue plot now displays the list of waiting tasks in the Inspector. Tasks enqueued before the trace started aren’t displayed.  (169113107)
- You can now pin threads displayed in call tree views using the context menu.  (169208779)
- os_signpost Instrument now displays a track for each signpost name, nested below the category level in the track hierarchy.  (170272998)
- Swift Concurrency Tasks and Actors are now displayed even if their lifetime began before the trace. Instruments makes a best effort to display as much data as possible. Tasks now can have “Unknown” state. Tasks and Actors names may depend on order of incoming data.  (171187553)
- `xctrace export` allows you to restrict time range of an export using `time-start`, `time-end`, `duration` arguments.  (171320057)
- When you open a `.tracetemplate` file that isn’t saved in the Instruments user templates folder, the template is now copied into that location and subsequently accessible in the “User” tab.  (172516226)
- System Trace template now graphs thread priority over time to help you understand issues related to resource starvation.  (173463486)
- `xctrace export` of traces containing Allocations Instrument now contains a backtrace for each row element in the ‘Allocations List’ detail. Backtraces appear only when captured in the trace data.  (173791067)
- The View menu has been reordered to clarify the function of each menu item.  (177008275)

###### Resolved Issues in Xcode 27 Beta

- Fixed an issue where the Hangs instrument would flag false-positive responsiveness issues in non-UI processes like daemons.  (110146539)
- Fixed an issue where profiling an iOS app that was already open would close the app instead of relaunching it.  (150320702)
- Fixed an issue where Instruments uses significant amount of memory when importing .atrc files. The memory footprint of the application in these scenarios is on average 1.5GB smaller.  (162707266)
- Fixed an issue where the detail filter was not saved or restored when switching details in the Allocations, Leaks, and VM Tracker instruments.  (167717200)
- Fixed a performance issue where the timeline would blink or animate unnecessarily when zooming into content.  (168081396)
- Fixed an issue where time selection would be cleared when starting a new recording.  (172327572)
- Fixed an issue where the Cause & Effect graph in the SwiftUI instrument could use large amounts of memory when zoomed into a very small time range.  (172983697) (FB22288896)
- Fixed issues in the App Lifecycle graph: removed the inaccurate ‘Process Creation’ phase and fixed an issue where the ‘System Interface Initialization’ phase appeared twice.  (174190644)
- Fixed an issue where Instruments target chooser would always resolve symlinks to binaries, preventing BusyBox binary profiling from working.  (176476530)
- Fixed an issue where warnings and errors toolbar icon appeared clipped.  (151921162)
- Fixed an issue where tooltips for events would sometimes show incorrect duration when zoomed out.  (154788572)
- Fixed an issue where the last few libraries in the Symbols window were hidden behind the bottom bar.  (171009409)
- Fixed an issue where the pinned view would resize to fit its content after you had already resized it to your preferred size.  (173461626)
- Fixed an issue where ‘Auto Expand’ option in call tree ‘Find’ wouldn’t be enabled by default.  (174513327)
- Fixed an issue where Allocations instrument graph constantly rescaled when recording in the immediate mode.  (177577222) (FB22824426)

###### Deprecations in Xcode 27 Beta

- Instruments now requires target iOS, watchOS and tvOS devices with versions of at least iOS 17, watchOS 10, or tvOS 17.  (166097304)

##### Intel Deprecation

###### New Features in Xcode 27 Beta

- Build targets with a min deployment target set to macOS 27.0 or DriverKit 27.0 will not build Universal by default. The `ARCHS_STANDARD` build setting will no longer include x86_64 when `MACOSX_DEPLOYMENT_TARGET` or `DRIVERKIT_DEPLOYMENT_TARGET` >= 27.0. The x86_64 architecture can be added to the `ARCHS` build setting if this is needed.  (161837535)

###### Deprecations in Xcode 27 Beta

- Xcode 27 will only install and run on Apple silicon Macs. The macOS 27 SDK supports back deploying Universal (Intel and Apple Silicon) apps to macOS 12 and later. Intel development is still possible with macOS versions that support Rosetta like macOS 27.  (162138432)

##### Interface Builder

###### New Features in Xcode 27 Beta

- Introducing a new Interface Builder compilation mode, `toolchain`, for UIKit (Cocoa Touch) based documents. Enabled by default, `toolchain` allows compiling IB documents without the need to download a simulator, which is especially useful for build servers. Should you experience issues during this transition period, you can opt out via the `IBC_COCOATOUCH_COMPILER_MODE = simulator` build setting or using `--cocoatouch-compiler-mode simulator` when manually invoking `ibtool`. If you opt out, please file Feedback and include any errors you may have received from `ibtool` so we can investigate.  (114401122)

##### Linking

###### Deprecations in Xcode 27 Beta

- The ld64 linker has been removed and the `-ld_classic` option is no longer supported.  (165165518)

##### Localization

###### New Features in Xcode 27 Beta

- Exporting localizations now extracts `NSLocalizedString` and similar macros from header files in addition to implementation files.  (19191207) (FB5500560)
- Agents in Xcode can now be used to translate strings in String Catalogs. You can ask an agent to translate strings ranging from a single feature to an entire project, into one or more languages. Xcode will add languages to your project settings, create missing String Catalogs, and provide guidance and context to agents as they translate.  (111514130) (FB12479690)
- Strings in code with a localization comment of “do not translate” will be automatically marked as “Don’t Translate” in String Catalogs and `translate="no"` in exported XLIFFs.  (111715368)
- Exported XLIFFs will use `state-qualifier="leveraged-mt"` to indicate strings that were translated using machine translation.  (161775544)
- The String Catalog editor now includes a Generate Translations button as a shortcut to ask an agent to translate strings. You can also use the context menu to translate specific strings.  (169559347)

###### Resolved Issues in Xcode 27 Beta

- Fixed an issue where automatic strings could get removed from String Catalogs when declared using AppIntent APIs that take table parameters.  (174776249)
- Fixed a crash that could occur when `BUILD_ONLY_KNOWN_LOCALIZATIONS` is used in a target with multiple Asset Catalogs.  (176827483)

##### Metal

###### New Features in Xcode 27 Beta

- The Diagnostics Panel in the Scheme Editor exposes more Metal validation options including logging non-fatal actions, validating load and store actions, logging resource allocation stack traces, and controlling GPU stack overflow detection.  (162401628)
- The Metal Performance HUD exposes more MetalFX related metrics such as jitter sequence length and motion vector scale. The configuration panel includes a new “Overrides” panel when MetalFX is enabled, and allows customization of jitter multiplier, motion vector scale and exposure visualization for debugging purposes.  (162557993)
- The Metal Capture popover includes a new “Include MetalFX temporal scaler history” advanced option that improves texture quality during replay when your app uses MetalFX temporal scaling.  (169816556)
- The Metal Capture popover includes a new “Optimize shared memory capture” advanced option that improves capture performance and reduces GPU trace size on disk.  (170023938)

###### Resolved Issues in Xcode 27 Beta

- Fixed: The Queue Debugging setting to Enable Backtrace Recording is off by default. To view the process grouped by dispatch queues in the debug navigator, or to get recorded backtraces indicating the originating dispatch operation when viewing the process grouped by thread, please enable the setting in the scheme editor under Run > Options > Queue Debugging > Enable Backtrace Recording  (164183224)

##### On Demand Resources

###### Deprecations in Xcode 27 Beta

- On Demand Resources and the `NSBundleResourceRequest` API are deprecated. Use Background Assets instead.  (170066290)

##### Organizer

###### New Features in Xcode 27 Beta

- The Insights Overview summarizes high-impact performance regressions for metrics and diagnostic reports for your app. Use it to plan and prioritize performance engineering work.  (159975360)
- The new Hitches metric replaces the Scrolling metric in the Organizer, now displaying animation hitches for all animations in your app. Use it to get a comprehensive view of animation performance.  (160333794)
- Storage metrics are now available in Xcode Organizer, allowing you to monitor their app’s Documents & Data and App Size across releases and catch regressions in cache usage and bundle size.  (160837780)
- AI-driven analysis is now available for diagnostics in Xcode Organizer, enabling expert analysis of power and performance issues and seamless integration with source code and the Coding Assistant. Quickly resolve the highest-impact performance issues in your app by using Generate Recommendations for Crash, Energy, Disk Write, Hang and Launch diagnostics.  (177568727)
- Metric goals are now available for Battery Usage, Disk Writes, Hang Rate, Hitches, Memory, and Storage metrics, allowing you to prioritize performance engineering across more areas. Similar-app goals are now supported for Hang Rate, On-screen Battery Usage, Disk Writes, and Storage. Launch Time similar-app goals have been refined for improved accuracy, establishing new baselines.  (177572744)

##### Previews

###### New Features in Xcode 27 Beta

- Canvas can now display a grid of previews for each argument passed to the new `#Preview(arguments:)` syntax. Clicking on a preview in argument or variant grids opens the preview in the Interactive mode.  (167544057)
- Holding command will cause the input events (zooming and scrolling) to be handled by the canvas. This can be disabled with the new ‘Send Command-Modified Input to Canvas’ toggle in the Editor > Canvas menu.  (170072429)
- iOS previews have a new Resizable Canvas mode that enables viewing the preview in arbitrarily sized containers  (171013421)

##### Previews Playgrounds

###### New Features in Xcode 27 Beta

- Each #Preview and #Playground tab can now be pinned independently in the canvas.  (167543928)

###### Resolved Issues in Xcode 27 Beta

- Fixed an issue where there was a long delay before Canvas showed an error when a likely crash occurred.  (168097944)

##### Simulator

###### New Features in Xcode 27 Beta

- `simctl` and `devicectl` now support rebooting a simulator using the reboot command.  (172303413)

##### Source Editor

###### New Features in Xcode 27 Beta

- All new Markdown editor. View markdown files in your project and from agents in rendered form. Create and edit markdown using familiar formatting tools. View markdown as source code and see the rendered preview by activating Xcode’s canvas.  (175022151)

###### Resolved Issues in Xcode 27 Beta

- Fixed an issue in macOS 27 where clicking the close button in an expanded macro added a breakpoint rather than closing the expansion. You can use Editor > Hide Macro Expansion to close the expansion.  (174376098)

##### Storekit Testing in Xcode

###### New Features in Xcode 27 Beta

- New StoreKit configuration UI to configure In-App Purchase offer codes, and new off-device purchase options to test purchases with IAP offer codes via the Transaction Manager.  (141012907)
- Subscription Bundles can be configured for local testing in the StoreKit Configuration.  (164203930)
- Subscription Suites can be configured for local testing in the StoreKit Configuration.  (166899262)
- Add support for creating volume purchase transactions for 1-month and 1-year auto-renewing subscriptions through the Xcode Transaction Manager.  (169041777)

##### Swift Compiler

###### New Features in Xcode 27 Beta

- The Swift dependency scanner has been optimized to avoid redundant setup work and header searches when looking up Clang modules during a single dependency-scan action, substantially improving scanning performance. As a consequence of this change, every Clang module reachable from a single Swift dependency-scan action must have a unique module name. If two module maps visible to the same scan declare a Clang module with the same name, the scan may report an error. Previously, the scanner may have tolerated duplicating names. The most common cases are projects or SDKs that vend the same Clang module name from more than one location on the header search path, and vendored third-party sources that ship a module.modulemap redeclaring an SDK module.  (136303612)

##### Swift Package Manager

###### New Features in Xcode 27 Beta

- When one or more test targets in a package experience a test failure, `swift test` summarizes them at the end.  (168311253)
- `swift test` now supports repeating test cases until a condition is met. Pass `--maximum-repetitions` and `--repeat-until [pass|fail]` to `swift test` to repeat your tests until they pass or fail. Only those test cases that match the repeat condition will be repeated.  (177561078)

##### Swiftc++ Interoperability

###### New Features in Xcode 27 Beta

- When calling a C++ constructor that has parameters with default expressions, you no longer have to pass all arguments explicitly in Swift.  (118987713)
- You can now convert Swift closures to instances of `std::function`. For example: ```None
 // C++
 void processNumbers(const std::vector<int> &numbers, std::function<void(int)> op);
``` ```None
 // Swift
 processNumbers([1, 2, 3], .init { print($0) })
``` (133777029)
- You can now annotate constructors of foreign reference types as SWIFT_RETURNS_RETAINED or SWIFT_RETURNS_UNRETAINED.  (135368369)
- Mapping `__counted_by` and `std::span` parameters annotated with `__noescape` to Swift Span no longer requires the SafeInteropWrappers experimental feature flag. Mapping return values to Span using `__lifetimebound` is still guarded by the experimental feature flag. For more information, see https://www.swift.org/documentation/cxx-interop/safe-interop/#safe-overloads-for-annotated-spans-and-pointers  (148994016)
- Raw pointers to intrusively reference counted types (annotated with `SWIFT_SHARED_REFERENCE`) are imported as Swift classes. Starting with this release you can now annotate smart pointer types pointing to such reference counted types with `SWIFT_REFCOUNTED_PTR` macro to bridge their instances to Swift classes. For example: ```None
 struct SWIFT_SHARED_REFERENCE(...) SharedObj {};
 
 template <class T>
 struct SWIFT_REFCOUNTED_PTR(.getPtr) Ptr {
     Ptr(T* ptr);
     T *_Nullable getPtr() const { return ptr; }
 };
 
 using ObjPtr = Ptr<SharedObj>;
 
 void takesSmartPtr(ObjPtr p);
``` The function `takesSmartPtr` is imported to Swift as: ```None
 func takesSmartPtr(_ p: SharedObj?)
``` (156521316)
- Previously, safe wrappers could not be generated for functions where the signature contained template instantiations. Any template instantiation would have to be referred to using a typedef instead. Safe wrappers can now be generated for functions without wrapping `std::span` parameter types in typedefs, if they are annotated with `__noescape`. Any other template instantiation in the signature still prevents generating a safe wrapper, unless hidden behind a typedef. Example: ```c++
 // Already supported:
 using IntSpan = std::span<int>;
 void foo(IntSpan x __noescape);
 
 // Now this also works:
 void bar(std::span<int> y __noescape);
 
 // The return type template instantiation here still prevents generating a safe wrapper:
 std::span<int> baz(std::span<int> z __noescape);
``` (167712240)

##### System

###### New Features in Xcode 27 Beta

- System now provides Swift APIs for the C `stat`, `lstat`, `fstat`, and `fstatat` system calls. This includes a new `Stat` type with initializers from `FilePath`, `FileDescriptor`, or a C string; `FilePath.stat()` and `FileDescriptor.stat()` instance methods; and supporting types (`FileType`, `FileMode`, `FileFlags`, `UserID`, `GroupID`, `DeviceID`, and `Inode`). See [`SYS-0006`](https://developer.apple.comhttps://github.com/apple/swift-system/blob/main/Proposals/0006-system-stat.md) for more details.  (160612181)

##### System Trace Quality of Service

###### New Features in Xcode 27 Beta

- Thread Activity Instrument now displays Quality of Service of individual threads. Effective QoS is displayed by default, Requested QoS is hidden by default (use the track dropdown menu of Thread items in order to reveal it).  (173043672)

##### Testing

###### New Features in Xcode 27 Beta

- In your Test Plan, you can control how the system responds to target application crashes during UI testing by choosing one of four severity levels: off, warning, failure (default), or fatal failure.  (168107814)
- Added a filter to the test plan configurations tab.  (168608491)
- Added recent tests and open tests filters to the Test Navigator.  (168608830)
- When you call an XCTest or Swift Testing assertion within a test from the opposite framework, you will see a runtime issue with warning severity if the assertion failed. Control this behavior with the new Swift Testing and XCTest Interoperability setting in your test plan.  (170335449)
- Updated the test plan JSON to sort tags, making it easier to review changes.  (174178766)

###### Resolved Issues in Xcode 27 Beta

- Fixed an issue where adding an attachment to a test case during the `XCTestObservation` callbacks `testCaseWillStart(_:)` or `testCaseDidFinish(_:)` by calling `XCTestCase.add(_:)` did not persist the attachment in the results.  (89059895)
- Fixed: The ‘Test Repetition Mode’ setting now only repeats individual Swift Testing test cases, rather than repeating the entire test plan.  (130508488)
- Fixed: Swift Testing is now better-able to associate recorded issues with the tests that generated them when they occur in detached Swift tasks, on dispatch queues, or on background threads.  (169036231)
- Fixed: Large Swift Testing test suites with many parameterized test cases have significantly better performance in Xcode 27.  (171415950)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)*