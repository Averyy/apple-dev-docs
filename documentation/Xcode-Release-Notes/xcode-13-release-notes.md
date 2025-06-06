# Xcode 13 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 13 includes SDKs for iOS 15, iPadOS 15, tvOS 15, watchOS 8, and macOS Big Sur 11.3. The Xcode 13 release supports on-device debugging for iOS 9 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 13 requires a Mac running macOS 11.3 or later.

##### General

###### New Features

- Xcode 13 includes native support for [`concurrency programming with Swift`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html), support for continuous integration and delivery with [`Xcode Cloud`](https://developer.apple.comhttps://developer.apple.com/xcode-cloud/), integrated support for Git pull requests, the ability to create and view documentation in Swift frameworks using DocC, Vim keybinding support, Swift package collections, and more. For details, see [`What’s Included In Xcode`](https://developer.apple.comhttps://developer.apple.com/xcode/whats-new/). (78887232)

- You can now use `cktool` on the command line to interact with your [`CloudKit`](https://developer.apple.com/documentation/CloudKit) database schema and records. For a list of available commands, run `man cktool` or `xcrun cktool --help`. (68114031)
- You can now use `TextureConverter` on the command line to compress textures to all Metal compressed texture formats. For a list of available commands, run `xcrun TextureConverter --help`. (70481436)
- The Xcode 13’s XIP archive is now approximately 15% smaller for the same content. You can expand the archive using Archive Utility, or with `xip` on the command line. : Other methods of expanding the archive may produce a broken Xcode app. (78714333)

###### Resolved Issues

- Keyboard shortcuts in Xcode now work as expected when the documentation window has more than one tab open or is in full-screen mode. (72209603) (FB8936285)

##### Apple Clang Compiler

###### New Features

- To support the new Swift concurrency model, `clang` can now warn if you call a completion handler more than once or if an execution path doesn’t have a completion handler call. To turn on the new warning, in your project’s Build Settings in the Apple Clang - Warnings - All languages section, select Yes from the Completion Handler Misuse pop-up menu; alternatively,  when invoking `clang` from the command line, pass the `-Wcompletion-handler` flag. You can suppress the warning for a method by adding the `NS_SWIFT_DISABLE_ASYNC` attribute to the method, which also suppresses the translation of this method into an `async` method in Swift. (10708075)
- The new `-fobjc-constant-literals` flag lets you declare declare global constant literals, and performs optimizations for other literals it supports in Objective-C code. You can use this flag to embed static property list literals (`NSDictionary`, `NSNumber`, and `NSArray`) at compile time, placing them in the `CONST` section of the binaries. (44920795, 45380392) For example: ```objc
static NSString * const MyNotificationName = @"MyNotification";
``` And: ```objc
static NSDictionary * const myConstantDictionary = @{ @"something_awesome" : @YES };
static NSArray * const myArray = @[ @1, @2, @3, @4 ];
static NSNumber * const answerToLife = @42
``` When possible the compiler also converts statements that are similar to the above examples but are in a non-global scope. The compiler supports this flag with deployment targets of macOS 11, iOS and iPadOS 14, tvOS 14, watchOS 7 and later. The flag is enabled by default. To disable constant literals completely, use `-fno-objc-constant-literals`. To selectively disable specific constant literal optimizations use `-fno-constant-nsnumber-literals`, `-fno-constant-nsarray-literals`, and `-fno-constant-nsdictionary-literals`. The `plutil` tool, available in macOS 11 and later, can generate source files with constant section objective-c literals. For example, you can generate `.m` files using the following command: ```shell
plutil -convert objc SomePlist.plist
``` To generate an accompanying `.h` header file, add the optional `-header` flag, as shown in the following command: ```shell
plutil -convert objc -header SomePlist.plist
``` : In constant dictionaries, you can only use an `NSString` as a key. Using any other type results in an error: ```objc
static NSDictionary * const myConstantDictionary = @{ @42 : @@"answer to life" }; // This throws an error, the initializer element isn't a compile-time constant.
```
- You can now configure the `C++20` and `GNU++20` C++ language dialects in Xcode’s build settings. (50900425)
- clang now supports C++20 likelihood attributes `[[likely]]` and `[[unlikely]]`. (78316737)

###### Known Issues

- ASAN might cause Swift async functions to crash on x86_64. (80786596)

##### Asset Catalogs

###### New Features

- At runtime, your app can now use iOS app icon assets from its asset catalog as alternate app icons. A new build setting, “Include all app icon assets,” controls whether Xcode includes all app icon sets in the built product. When the setting is disabled, Xcode includes the primary app icon, along with the icons specified in the new setting, “Alternate app icon sets.” The asset catalog compiler inserts the appropriate content into the `Info.plist` of the built product. (33600923)
- The asset catalog allows selecting universal system colors that are available across all platforms, including watchOS. (73257675)

##### Build System

###### New Features

- Configuration settings (.xcconfig) files now support using `\` to break long lists across multiple lines. (4405473) (FB5943765) For example: ```shell
HEADER_SEARCH_PATHS = $(SRCROOT)/include \
    $(SRCROOT)/include/component1 \
    $(SRCROOT)/include/component2
```
- When you pass xcconfig files to `xcodebuild` using the `-xcconfig` command-line flag and `XCODE_XCCONFIG_FILE` environment variable, Xcode parses them using New Build System semantics, which also supports condition parameters. (25001734)
- Configure frameworks to build for multiple platforms in a single build operation by setting the `SUPPORTED_PLATFORMS` build setting to the list of platforms you support and setting `ALLOW_TARGET_PLATFORM_SPECIALIZATION` to `YES`. (45951215)
- You can now use platform filters in build phases and target dependencies for all supported platforms. (72240935)
- `xcodebuild` now shows the target and project name for each failing command in the summary at the end of the build log when a build failure occurs. (75081458)
- The build system now emits a warning when a script phase, or custom build rule, declares an input dependency that isn’t part of the build input and isn’t declared as an output dependency of any other task in the build. (76129954)
- The build options sheet now includes a Dependency Order option, which replaces the Parallelize Build option, and a Manual Order option, which is deprecated, but included for legacy compatibility. (76251439)

###### Resolved Issues

- Fixed an issue that set the `NATIVE_ARCH` build setting to `armv7` when building against the iOS and iPadOS, tvOS, and watchOS SDKs. The `NATIVE_ARCH` build setting now reflects the architecture family of the host Mac — arm64 on Macs with Apple silicon or x86_64 on Intel-based Macs. (5716560)
- Importing XCTest or StoreKitTest in a framework target when building for iOS, tvOS, or watchOS no longer fails with a linker error. (61952138)
- Fixed a dependency ordering issue involving frameworks with public and private module maps which could result in “redefinition of module” errors. (72123120)
- Fixed an issue where clicking on a warning or error in the issue navigator didn’t navigate to the associated C or C++ file. (73582669) (FB8981116)
- Fixed an issue that required closing and re-opening the workspace if the build system service crashed. The workspace now lets you attempt building again. (74124183)

###### Deprecations

- The legacy build system is deprecated and now produces an error when you attempt to use it. (76124672)

##### Core Data

###### New Features

- Use the Allows Cloud Encryption checkbox in the Core Data model editor’s attribute inspector to support the CloudKit Encrypted Record Fields feature. (73670355)

##### Core Ml

###### New Features

- Xcode’s Core ML model editor now supports the new Core ML package format, `.mlpackage`, along with direct editing of its metadata and descriptions. You can upgrade Core ML models from the `.mlmodel` format to the `.mlpackage` format in a model’s Utilities tab. (69867656)
- The Swift generated interface for Core ML models now includes access to multidimensional inputs and outputs via strongly-typed `MLShapedArray` properties when your deployment target is macOS 12, iOS 15, tvOS 15 or watchOS 8. (73627777)

###### Resolved Issues

- Resolved an issue in macOS 11 where the preview tab for CoreML model packages might not respond or might fail with an “Unable to compile model at `<ModelName>.mlpackage`” error. (77794983)
- Resolved an issue where the operation distribution table didn’t appear in the General tab when viewing the model in the Xcode editor for ML Packages in the ML Program format that have no class labels. (78577088)

###### Known Issues

- Create ML app machine learning model training performance may be unexpectedly reduced when running in macOS Monterey. (82415543)
- Quitting the Create ML app or closing a project while training is still running may result in the loss of training progress. (82460651) : Pause training before quitting the app or closing a project.

##### Create Ml

###### New Features

- Two new templates are available for training models to interpret hand poses. (68942553) - Hand Pose Classification trains a model for categorizing a static hand pose in an image.
- Hand Action Classification trains a model for categorizing dynamic hand actions in video.
- The Sound Classification template’s new Audio Feature Print option enables you to train sound classifier models faster with higher accuracy, lower latency, and smaller model size. This is now the default feature extraction option for new model sources. (70558475)

##### Debugging

###### New Features

- Xcode’s console now supports toggling line wrapping through the Editor > Wrap Lines menu item. (3669727)
- To set a column breakpoint on a line, Command-click on an expression then select Set Column Breakpoint from the Actions menu. (10112530)
- If the debugger hasn’t resolved a breakpoint yet, the breakpoint’s icon changes into a placeholder glyph. For some breakpoints, such as a symbolic breakpoint, the icon changes back to the original glyph when the associated shared library is loaded into the process. (11439048)

###### Resolved Issues

- Resolved an issue that caused Xcode to indefinitely display a window saying “Building Memory Graph” when clicking the “debug memory graph” button resulted in a failure. Xcode now promptly displays any error that causes memory graph retrieval to fail. (59479311)
- Choosing Debug > Simulate MetricKit Payloads now works when debugging an app running in a macOS, macOS “Designed for iPad”, or Mac Catalyst run destination. (78026869)

###### Deprecations

- LLDB’s Python scripting no longer supports Python 2. (73956573)

##### Documentation

###### New Features

- Xcode can generate documentation from comments in your Swift code, as well as accompanying articles. (57148915, 57446055, 57447632, 74951110) Use the “Build Documentation” command to generate documentation from your Swift frameworks and packages. Build on the command-line using the `xcodebuild docbuild` command. For more information on building documentation, see [`Documenting apps, frameworks, and packages`](https://developer.apple.com/documentation/Xcode/documenting-apps-frameworks-and-packages). View built documentation in the documentation window, and export using the DocC Archive format. Xcode can open and read DocC Archive packages. For more information, see [`Distributing documentation to other developers`](https://developer.apple.com/documentation/Xcode/distributing-documentation-to-other-developers).
- Code completion provides suggestions when you write your project’s documentation. It provides suggestions both when writing documentation comments in source files, and when writing markup files inside the `.docc` catalog. (57447419)
- Quick Help now uses DocC to present project documentation and renders links to your project’s documentation in the documentation window. (71913824)

###### Resolved Issues

- Links to symbols inherited from protocol conformances now correctly resolve in Quick Help and appear as completion items. (76927387)
- Breadcrumbs in the documentation viewer now consistently reflect the page rendered inside the content view. (78512655) (FB9118964)

###### Known Issues

- Links to Objective-C types exposed to Swift using a bridging header don’t resolve in Quick Help, and don’t appear as completion items. These links resolve as expected in full documentation builds and in Xcode’s documentation window. (77472074)

##### Indexing

###### New Features

- Xcode indexes macro names. They now appear in Open Quickly. (47815401) (FB5667927)

###### Resolved Issues

- Improved the reliability and performance of the source languages service that provides semantic functionality — such as live issues and code completion — in Xcode editors. (71098549) - Improved reliability and addressed instances where the build succeeded, but the editor showed unexpected live issues.
- Fixed an issue that required you to manually build in order to see source file changes from other modules reflected in the current file. Xcode now takes care of propagating the necessary updates in the background.
- Improved performance and significantly reduced the CPU usage by the `XCBBuildService` process, while it’s processing requests from the source languages service.
- Fixed issue where a Swift package with symlinks to source modules would break live issues and code completion in Xcode. (75732781)

##### Instruments

###### New Features

- You can now label a Run using the Run’s Info popover in the toolbar’s Activity viewer. (20823928)
- Call tree views and the extended detail view in Instruments now indicate inlined functions with an “[inlined]” marker. (36153516)
- Different views are more discoverable via the detail view navigation bar. Detail views can now be accessed via shortcuts (Command-1, Command-2, and so on). You can now access the Run Issues and Console views from the View menu. (45734644)
- Export table data from traces containing Allocations, Leaks, and VM Tracker instruments using `xctrace export` on the command line. To see how the table of contents now reflects this ability, run `xctrace export --toc`. (54600972)
- The Instruments extended detail view now shows `os_log` and `os_signpost` messages and backtraces when selecting associated detail view rows. (63098516, 72104089) (FB7697641)
- The Run Information view now appears in the activity view area in the Instruments toolbar. (65694190)
- The CPU Counters template is now more reliable and has better performance. Instruments 13 no longer supports Counters traces recorded with older versions of Instruments. (65812748)
- The `leaks` command has three new modes:  `-referenceTree`, `-autoreleasePools`, and `-debug`. Consult `man leaks` for more details. (68724178)
- The Network template now includes a new Instrument for capturing and analyzing HTTP traffic. This Instrument works on all Apple platforms and shows: - HTTP traffic at the [`CFNetwork`](https://developer.apple.com/documentation/CFNetwork) layer for debuggable processes, including out-of-process background traffic
- Detailed durations for each [`URLSessionTask`](https://developer.apple.com/documentation/Foundation/URLSessionTask), its underlying HTTP transactions, and transaction states
- Backtraces for `URLSessionTasks` to show where tasks start in code
- Headers and bodies of HTTP requests and responses
- Traffic sent over VPN, via Proxies, and using certificate pinning You can export this HTTP data to an HTTP Archive via `xctrace` using the new `--har` export flag. (71444535)
- The Instruments timeline view now uses a Metal-based renderer for a smoother experience, including overall improvements to the timeline usability. (73591705)
- Recording settings for the `os_signpost` Instrument now supports specifying `os_signpost` subsystems for the `dynamicTracing` and `dynamicStackTracing` logging categories during recording. (73694990)
- A new `CPU Profiler` template allows for analyzing CPU workloads using Cycle-based Performance Monitoring Interrupts (PMIs). It provides a more stable measurement for code running on Performance or Efficiency CPUs. (76889185)
- To support the new JSON-format crash logs generated in macOS Monterey and iOS 15, Instruments includes a new `CrashSymbolicator.py` script. This Python 3 script replaces the `symbolicatecrash` utility for JSON-format logs and supports inlined frames with its default options. For more information, see: `CrashSymbolicator.py --help`. `CrashSymbolicator.py` is located in the `Contents/SharedFrameworks/CoreSymbolicationDT.framework/Resources/` subdirectory within Xcode 13. (78891800)

###### Resolved Issues

- Fixed an issue where changing arguments in Xcode and invoking the profile action wasn’t reusing an existing trace document. (41842858)
- Improved the performance of command-line tools like `malloc_history` by up to 300x when targeting processes that were built with large static archives. (63114609) (FB7698032)
- Instruments now more reliably displays inlined frames in backtraces when DWARF data is available. (74351555)
- Improved Instruments’ launch reliability when slow or unresponsive devices are connected. (77151140)
- You can now stop HTTP Traffic recording initiated from Instruments, in tvOS 15’s Control Center. (77274053)

###### Deprecations

- Instruments no longer includes the Energy template; use metrics reporting in the Xcode Organizer instead. (74161279)
- The deprecated `instruments` command-line tool has been removed; instead, use `xctrace`. (74412969)

##### Interface Builder

###### New Features

- You can now manually reorder Storyboard scenes in the outline view. (10103709)
- Storyboards and XIBs for macOS compile using UINibEncoder to reduce file sizes and improve runtime performance. When deploying an App before macOS 10.13, Xcode generates a backward compatible nib for the older OSes. You can opt out of this behavior by applying the `IBC_COMPILER_USE_NIBKEYEDARCHIVER_FOR_MACOS=YES` and `IBSC_COMPILER_USE_NIBKEYEDARCHIVER_FOR_MACOS=YES` user defined overrides in the project’s build setting. (31889616) UINibEncoded nibs are stricter about enforcing the return of self from an [`initWithCoder:`](https://developer.apple.com/documentation/foundation/nsnotification/1412464-initwithcoder) implementation on custom classes. Returning a nonsafe pointer from `initWithCoder:` is unsafe and can lead to dangling pointer references. macOS 12 emits a descriptive warning when this occurs during runtime nib loading. Older macOS versions emit “This coder requires that replaced objects be returned from initWithCoder:”. If necessary, you can bypass the strictness warning by applying the user defined overrides described above.
- You can now select and navigate outline view groups, such as “Constraints,” using the keyboard. Selecting a group is equivalent to selecting all of the items contained in the group. (46607897)
- Interface Builder has a redesigned canvas bottom bar with popovers for changing devices and layout, and toggles for changing device appearance and orientation. (68288315)
- Added support for the `changesSelectionAsPrimaryAction` property on `UIButton` and `UIBarButtonItem`. Use this, along with setting a menu and enabling `showsMenuAsPrimaryAction` to create a Pop-Up button. (69890483)
- Support for authoring and dragging iOS Core Location Buttons from the object library. The Core Location button grants a one-time authorization of the device’s current location when pressed. A project must link the CoreLocationUI framework to use `CLLocationButton`. (70781230)
- Improved reproducibility when compiling binary nibs from iOS storyboards and xibs. (71004831)
- Added support for the new content configuration styles for use on table view cells within static table views. (71258693)
- `UITabBar` and `UIToolbar` inspectors now support configuring `scrollEdgeAppearance`. (71788169)
- Interface Builder now supports `UIButton.menu`. (72059569)
- When editing launch storyboards, Xcode emits a design time warning if the total image resource size exceeds the runtime threshold limits. (72349945)
- The preview pane for Watch Storyboards now displays canvas style bezels instead of photorealistic bezels. (73070504)
- You can now preview the following accessibility settings in Interface Builder scenes: Dynamic Type, Bold Text, Button Shapes, On/Off Labels, Increase Contrast, and Reduce Transparency. You can activate these settings by clicking on the accessibility button in the canvas button bar and setting them in the accessibility popover. (73208721)
- You can now enable `UILabel`’s `showsExpansionTextWhenTruncated` property to show tool tip expansion when the label is truncated. (73581591)
- Customize Mac Catalyst simulated scene sizes from Document Inspector > Simulated Metrics > Scene Sizes. (73587968)
- Specify tooltips on `UIControl` objects through the attributes inspector for apps built with Mac Catalyst. (73594175)
- Interface Builder now supports `UIBarButtonItem.menu`. Use this along with the `UIBarButtonItem.changesSelectionAsPrimaryAction` property to create a pop-up button. (73671137)
- Interface Builder now supports new `UITextContentType` properties, including: `shipmentTrackingNumber`,  `flightNumber`, and `dateTime`. (73769660)
- iOS, iPadOS, macOS, and tvOS scenes support the two new SF Symbol rendering modes: hierarchical and palette. (73774179) When you select an SF Symbol, you can select either of the following modes from the render mode drop-down: - Use hierarchical mode to customize the symbol’s primary layer color. The other layers draw with reduced alpha blended versions of the primary color.
- Use palette mode to specify colors for each individual layer.
- Interface Builder now supports authoring buttons with `UIButtonConfiguration` styles, including `Plain`, `Gray`, `Tinted`, and `Filled`. (73789335)
- `UINavigationBar`, `UITabBar`, and `UIToolbar` inspectors now support configuring a `UIBarAppearance` instance. (74054594)
- `UIButton` and `UISlider` support selecting the preferred behavioral style for apps built with Mac Catalyst. (74260900)
- Storyboard scenes that use Freeform simulated metrics in a view controller’s size inspector are now resizable directly in canvas with resize knobs. (74298762)
- `NSButton` Bevel types support a Bevel Color in macOS 12. (74537793)
- In apps for macOS 12, you can configure the localized key equivalent options on a non-system `NSMenuItem` using the localize property in the attributes inspector. (76168930)
- In apps for iOS 15, you can configure the localized key equivalent options on non-system UI menu commands using the localize property in the attributes inspector. (76622527)

###### Resolved Issues

- Fixed an issue with canvas rendering and storyboard compilation that involved uninstalled constraints that spanned across `UIView` hierarchies. (23319744) (FB5697880)
- Fixed `@IBDesignable` view support for multi-platform targets. (65449051) (FB7964472)
- Fixed an issue that allowed the iPad canvas safe areas to account for the status bar inset. (67828638)
- Fixed an issue where moving items in the outline view could incorrectly reorder them. (69307918) (FB8724081)
- Fixed an issue where `Date Formatter`‘s `Advanced` `Edit Mode` inspector table didn’t properly support Dark Mode. (70051451) (FB8782722)
- Fixed rendering issues for Designables on Macs with Apple silicon. (71782893) (FB8921448)
- Fixed a state restoration issue with outline pane width and visibility. (72184267)
- Fixed issues with Interface Builder and Asset Catalog compatibility with Rosetta enabled on Macs with Apple silicon. (74180445) (FB8999052)
- Improved the Interface Builder inspector’s loading performance. (76425091)
- A font property inspector is now available for the UIButton system configuration styles. (76573915)
- Optional number properties in the inspector no longer have checkboxes to clear values. Instead, a value can be cleared by selecting the value and pressing the delete key. (77109701)
- Fixed a runtime crash issue that occurred when using [`MKMapView`](https://developer.apple.com/documentation/MapKit/MKMapView) in nibs that ran in macOS 10.15 and earlier. (78522530)
- Xcode no longer resets `NSCollectionViewGridLayout.maximumNumberOfRows` and `NSCollectionViewGridLayout.maximumNumberOfColumns` to `0` during document unarchiving. (80157777) (FB9262860)

##### Linking

###### New Features

- The `dyld` shared cache has been split into multiple files. Update any of your tools that inspect the cache to use the new structure. (36378398)
- All programs and `dylibs` built with a deployment target of  macOS 12 or iOS 15 or later now use the chained fixups format. This uses different load commands and LINKEDIT data, and won’t run or load on older OS versions. (49851380)
- `dyld2` and `dyld3` are unified. There’s now only one `dyld` on all platforms. (69400751)
- The DriverKit runtime now has a `dyld` shared cache. (70706923)
- If the `DYLD_PRINT_SEARCHING` environment variable is set to `1` at launch time, `dyld` prints out the paths to all locations it searched to find a `dylib` to load. (76430687)

###### Resolved Issues

- Fixed an issue that allowed editing of the `__DATA_CONST` region in the `dyld` shared cache. It’s now read-only. (22175031)
- Resolved `-pagezero_size` incompatibility in iOS. iOS now ignores `-pagezero_size`. (69436371) (FB8733025)
- Resolved an issue that required an `-image_base` option. When targeting PIE, `ld64` now ignores `-image_base`. (72143464)

###### Deprecations

- The `-whatsloaded` option isn’t supported anymore. (73366865) (FB8975608)

##### Localization

###### New Features

- Xcode can now open Xcode Localization Catalogs (`.xcloc`) for viewing and editing the translations of strings and other localized assets. As part of this feature, `.xcloc` is now a package file-type in Finder. To inspect the contents of the localization catalog, use Show Package Contents in Finder. (30024017)
- The new Use Compiler to Extract Swift Strings build setting invokes the Swift compiler to accurately extract string interpolations and string literals from `Text()`, `String(localized:)`, `AttributedString(localized:)` initializers, SwiftUI’s `LocalizedStringKey`, and Foundation’s `StringLocalizationKey`. Enabling this setting compiles all localized targets in your project when exporting and importing for localization. This build setting is enabled by default on all new projects, but can be opted-in for existing Swift projects. (58023398)
- Added support to `genstrings` and localization import and export for extracting strings that use the new `NSLocalizedAttributedString` macro in Objective-C code. (73067097)
- Errors in multiple localizations are now aggregated into a single alert dialog when exporting for localization. (73562452)
- Xcode automatically extracts `NSGKFriendListUsageDescription`, `NSLocationTemporaryUsageDescriptionDictionary`, and `NSFallDetectionUsageDescription` from the `Info.plist` files when exporting for localization. (75813015)

###### Resolved Issues

- Fixed an issue that may have unnecessarily required you to copy content from one localization into a newly added localization. When adding a new localization, you’re no longer required to copy content from a references language if the development language content doesn’t exist. (46222774) (FB5671738)
- Fixed an issue where `genstrings` extracted all `Text*()` string literals from SwiftUI code, instead of `Text()`. (67694778) (FB8524688)
- Fixed an issue where localized strings in XLIFFs with XML character escape sequences failed to import. (68924128) (FB8695129)
- Fixed an issue were Xcode would non-deterministically export content from a project if multiple projects in a workspace had references to the same file. (71859474)
- Fixed an issue where Xcode crashed when importing localizations where localized files existed in a directory within a `.lproj` directory. (72755034) (FB8958080)

###### Deprecations

- The Localized String SwiftUI Support build setting is deprecated in favor of the new Swift compiler-based string extraction. (80817452)

##### Metal

###### New Features

- Metal Debugger now supports Selective Shader Debugging, which allows you to limit the debugging scope for large Compute shaders. This results in much faster shader-debugger session creation and iteration times. (67747242)
- New Capture Controls in Metal Debugger give you precise control to decide which part of your Metal workload to capture, as well as the option to capture multiple frames or scopes. (68219613)
- Metal Debugger now supports importing `metallibsym` files, which allows you to do Metal shader debugging and profiling in your app without having to embed shader sources in your `metallibs`. (68942327)
- A GPU Timeline is now available for Apple GPUs in Metal Debugger. Use this timeline to visualize and inspect the parallel execution of Metal GPU commands alongside a curated set of GPU Counters. The timeline gives you additional insight and control over the performance analysis of your app. (69178472)
- Metal Pipeline State Objects are now represented as resources in Metal Debugger, including a brand new viewer for Metal Pipeline States and Metal Libraries as well as GPU Memory accounting for Metal Pipeline States in Metal Debugger’s Memory Viewer. (69377133)
- New Consistent GPU Performance State profiling workflows are now available in Instruments’s Metal System Trace, Metal Debugger in Xcode, and as a brand new Condition Inducer. Consistent GPU Performance State profiling allows you to set your device in a consistent GPU performance state so you can do performance analysis of your apps in a consistent and reliable way. (69404088)
- You can now override the GPU performance state in the Metal System Trace template’s recording options. Instruments also adds a new GPU Performance State track when recording on iOS devices. (69523159)
- Metal Debugger now supports Metal ray tracing, alongside a new advanced Acceleration Structure Viewer. (70112081)
- Metal Application recording settings are now specific to the device being profiled. (74116877)

###### Resolved Issues

- Metal Shader Validation has been extended to support the following new Metal APIs: Indirect Command Buffers, Dynamic Libraries, Function Pointers, Visible Function Tables, and Pull Model Interpolation. (78491579)

###### Deprecations

- TextureTool is now deprecated. Transition your texture compression workflow to use the new TextureConverter tool instead. TextureConverter offers a full range of texture compression formats and gives you more control over your compression pipeline. (73370277)

##### Organizer

###### New Features

- Xcode now delivers crash reports in near real time, with longer data retention. Xcode aggregates crash logs by crash signature (“Crash Point”), in a list sorted by unique devices affected. Aggregated Crash Point data is now available for the past year. For any list filter selection, the Crashes Organizer shows a list of up to 1,000 possible Crash Points. Additionally, the new View > Reload Organizer menu item reloads the content in the Organizer. (54901702)

- Xcode now delivers crash reports with more filtering capabilities and more statistics. You can query the ranked list of top Crash Points by the following filter criteria: time period (Last Day, Last Two Weeks, Last Year), any version or a specific historical app version, any build or a specific historical app build, product type like App Clip, app extension, watchOS app, or main app, installation destination like iOS, macOS, or watchOS, and release history for TestFlight, App Store, or both. You can view crash statistics in three new dimensions: time period (Last Day, Last Year), app version, and release history. The time series data in the graph area shows unique devices affected by-hour for the last 24 hours and by-month for the last year. In addition, Xcode crash reporting now supports apps distributed on TestFlight for macOS. (78882594)

- You can now share crash reports by URL. A new button allows sharing of a Crash Point URL. Clicking on a Crash Point URL allows any developer with access to the app to view the Crash Point in the Organizer. (78882655)

- Xcode now shows the TestFlight Feedback for your crashing issues to give better insight into what went wrong. TestFlight Crash Feedback is now viewable in the new TestFlight Feedback Inspector for any selected Crash Point. When viewing TestFlight Crash Feedback in Safari, a new “Open in Xcode” allows opening the Crash Point in the Xcode Organizer. (78882718)

- You can now filter the Energy reports list based on any specific historical app version, any specific historical app build, product type like App Clip, app extension, or main app, and release history for TestFlight or App Store. (78882776)

- New Scroll Hitch Goals in the Xcode Organizer make it easy to analyze the scrolling experience for a version of an app. The bars in the chart appear in red, yellow, or green, depending on the goal level into which they fall. Each color associates with a key to the right of the chart; the key provides more information about the thresholds for each goal level. (62735038)
- When you’re viewing metrics for your app, you now have the option to view metrics for your app’s App Clip. Select the App Clip filtering option to view your App Clip metrics data. (63915380)
- The new Terminations metric in the Xcode Organizer shows foreground and background terminations, broken down by reason. This organization provides granular information about the most prevalent causes of termination for a given app. (64376250)
- Historical data in the Xcode Organizer now shows up to 16 of an app’s latest versions for each metric chart, providing the performance trend of an app over a larger window of time. (64382966)
- Now when you view a metric, the inspector shows your app’s release date information. (64995828)
- Qualitative Insights for Disk Write Reports in the Xcode Organizer show new information called Insights in the inspector. These insights include optimizations to help reduce the Disk Writes in the app. (66926840)
- Smart Insights are now available in the Xcode Organizer to help you discover your app’s power and performance regressions faster than before. For more information, see [`Analyzing the performance of your shipping app`](https://developer.apple.com/documentation/Xcode/analyzing-the-performance-of-your-shipping-app). (71420981)

##### Playgrounds

###### Known Issues

- Importing the TabularData framework in an Xcode Playground targeting macOS may result in missing symbols. (77162151) : If your use case permits, set the playground’s platform to iOS.
- Xcode Playgrounds don’t support Swift Concurrency language constructs. (79408099)

##### Previews

###### New Features

- Previews now supports inspecting a view’s accessibility elements while previewing the view. This support requires macOS 12. (78297929)

###### Deprecations

- Xcode 13 no longer includes a menu item in the Previews canvas for debugging a preview. Instead, use the Debug > Attach to Process menu item to attach the debugger to your previewed app. (73981969)

##### Project Navigator

###### New Features

- The project navigator hides the Products group when it’s in the default location. The Product > Show Build Folder in Finder menu item replaces the most common use. (71561549)
- The Move Focus to Editor command now interprets vim directional movement keys. (71754671) (FB8918700)
- The scheme editing sheet no longer has a maximum size. (73158957) (FB8969432)

###### Resolved Issues

- Fixed an issue where searching through a build log using Command-F would cause Xcode to crash. (52943982)
- By default, the project navigator hides file extensions and document tab titles. Configure this behavior in Xcode’s general preferences. (71203294)
- Fixed the indentation of wireless devices in the run destination menu. (72926304) (FB8964983)
- Moving large folders in Xcode is faster. (77217929)

##### Sanitizers

###### Resolved Issues

- Undefined Behavior Sanitizer can sanitize pre- and post-increment and decrement of types with a bit width smaller than `int`. (60943408)
- Fixed an issue on Macs with Apple silicon where memory allocation might fail while running with Address Sanitizer enabled. (75302812)
- Resolved an issue in macOS 12 where Thread Sanitizer might cause programs to crash or report false positives. (78319076)

##### Signing and Distribution

###### New Features

- `xcodebuild` now supports the use of App Store Connect API keys for authentication with the Apple Developer website. This enables the use of automatic signing via `xcodebuild` in headless environments, such as build machines and continuous integration setups. To use API keys with `xcodebuild`, create an API key on [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/access/api) and pass the key along with its identifier and your team’s issuer identifier to `xcodebuild` using the new parameters `authenticationKeyPath`, `authenticationKeyID`, and `authenticationKeyIssuerID`, respectively. When creating a key, you can assign it a role to control its permissions for performing automatic signing tasks. To learn more about creating and managing keys, see [`Creating API Keys for App Store Connect API`](https://developer.apple.com/documentation/AppStoreConnectAPI/creating-api-keys-for-app-store-connect-api). (51444716)
- Xcode now offers to create an app record the first time you upload a new app to App Store Connect. Before creating the app record, you can configure the name, primary language, and SKU for your app directly within Xcode’s distribution assistant. (57572562) (FB7476283)
- When uploading an app to App Store Connect, the distribution assistant in Xcode detects whether your app has a valid build number (`CFBundleVersion`). If your app has an invalid number (like one that was used previously, or precedes your current build number), the distribution assistant provides an option to automatically increment it to a valid number. In addition, the distribution assistant ensures that the build numbers of all embedded content in your app (such as app extensions, App Clips, or watchOS apps) are in sync with your app. Note that this doesn’t modify your source code or your archive; Xcode updates the build number in a staged copy of your app before packaging and uploading it to App Store Connect. (59826409)
- Automatic signing in the Xcode distribution assistant now supports cloud signing. With cloud signing, Xcode distribution signs your app using signing certificates created and managed on Apple servers, requiring no setup on your local Mac other than signing in to Xcode with your Apple ID. Cloud signing is available when signing for App Store Connect, Ad Hoc, Enterprise, or Developer ID distribution. Cloud signing certificates are stored securely on Apple servers; you can’t transmit or store the private key on your Mac. Similar to standard distribution signing certificates, cloud signing certificates are accessible only to members of your development team with the Admin role (or Account Holder for Developer ID). Use App Store Connect (Users and Access) to set permissions for users with other roles. You don’t need to save or share cloud signing certificates with other developers on your team, as any team member with the necessary permissions can sign them for distribution with cloud signing. If you already have a valid distribution signing certificate and matching provisioning profiles installed on your Mac, Xcode uses those and signs locally rather than using cloud signing. Additionally, cloud signing isn’t available when using manual distribution signing. (70706409)
- Xcode 13 supports provisioning apps for TestFlight on Mac. For your macOS app to be eligible for TestFlight, it must include provisioning profiles. When you upload your Mac app to App Store Connect and use automatic signing in the distribution assistant, the assistant automatically includes the provisioning profiles in your app. If you use manual distribution signing, create provisioning profiles on the Apple Developer website and then select them in the manual distribution signing section of the distribution assistant. (72824383)
- You may now use `notarytool` on the command line to interact with the Apple notary service. For a full description see the manual page with `man notarytool` or view available commands with `xcrun notarytool --help`. For more information about custom notarization workflows, see [`Customizing the notarization workflow`](https://developer.apple.com/documentation/Security/customizing-the-notarization-workflow). (78516542)

###### Resolved Issues

- Resolved an issue where automatic signing was unable to repair provisioning profiles for apps that use Cloud Containers, App Groups, or Apple Pay Merchant Identifiers if your account has the Developer role. (30185440) (FB5641770)
- Resolved an issue in which Xcode fails to `codesign` using a smart card. (58266781) (FB7516556)
- Fixed an issue where Xcode failed to sign a universal Mac Catalyst framework if it was built with bitcode. (71599193)

###### Known Issues

- Running `notarytool submit` with large `.zip` files may result in `notarytool` permanently hanging. (78513932) : Submit your app as a `.pkg` or `.dmg`, submit several small `.zip` files, or use `altool`.
- If you don’t have permission to use a cloud certificate’s type, signing with that certificate fails and presents an error of “<VALID_CERT_TYPE>_Managed is unknown”, even though the certificate type is known. (78538221)
- Xcode may incorrectly try to reuse a build number during the distribution workflow when App Store Connect rejects a build after upload. (78838509) : Manually increment your app’s build number before rebuilding.
- Xcode doesn’t correctly re-sign watchOS apps when exporting them using local signing from the Organizer in macOS 11. (82944652) : Export the app using cloud signing, or export in macOS 12.

##### Simulator

###### Known Issues

- Shazam Catalog recognition doesn’t work in simulated devices. (77564423) : Use a physical device.
- [`MusicKit`](https://developer.apple.com/documentation/MusicKit) functionality, such as loading content with music requests, doesn’t work in simulated devices. (78559381) : Test your app’s MusicKit functionality on a physical device.
- Simulated iPhone mini devices might incorrectly render partial screen updates resulting in visual glitches. (82423740) (FB9569039) : Use a non-mini simulated device.
- Some content may disappear or visual artifacts may appear when the content updates in Always On mode in simulated watchOS devices. (82732227) : Test on device to confirm Always On behavior.

##### Source Control

###### New Features

- You can now create, review, and merge pull requests using Xcode’s source control features, when signed into a GitHub or Bitbucket Server account. (62934369)
- You can now enable code review in any editor (or editor split) from the document tab bar, and it shows comparisons in an inline presentation by default. New commit selectors at the bottom of the editor let you customize the diff that’s displayed. (68880112)

###### Resolved Issues

- Xcode verifies an SSH fingerprint for Source Control operations when a previously trusted fingerprint has changed. (66421452) (FB8234008)

###### Known Issues

- Xcode’s pull request feature doesn’t work with forked repositories. You can’t submit pull requests to an upstream repository. (60009682) : Submit pull requests between branches within a single repository instead.
- When adding a comment to a pull request’s activity view, the layout sometimes visibly re-draws, making the view jump. (75595247)
- Deleting a pull request from its activity view may not update locally to display the deletion. However, the deletion does take place on the server. (76704508) : Close the pull request view. You can also confirm the pull request deletion on your source control provider’s web interface.
- Creating pull request comments for lines outside of diffs throws an error. (78275800)
- Xcode may offer an option to “decline” a pull request hosted on GitHub. This action may not be possible or allowed on a given repository. (78475833) : Use the GitHub website to close the pull request rather than declining it.
- PR code comments may occasionally clip in the PR Activity View. (78484455)
- When multiple remotes are configured on a repository, the target branch selector in a pull request may not populate with available branches. (78491019) : Remove remotes other than `origin`.
- Adding commits to a PR in Xcode doesn’t update the Changes navigator until you re-launch Xcode. (81229110) : Re-launch Xcode.
- Creating a new project with a Git repository sometimes fails to initialize a repo. (81874148) : Remove the hidden .git folder from the root level of the project folder, add author name and email address in the Source Control preferences tab in Xcode, and create a new Git repository from the Source Control menu in Xcode.
- If you close a project with an active and published PR while in a PR view and then re-open the project quickly, Xcode may display an error dialog. (82401004)

##### Source Editor

###### New Features

- Xcode 13 introduces Vim key bindings, emulating a vim experience in the source editor combined with the existing editor functionality. (3716281) Enable Vim key bindings in Preferences, using the Enable Vim key bindings option in Text Editing > Editing.
- You can copy the current location of the selection in the form of “<filename>:<line-number>” to the Clipboard by choosing Edit > Copy Location. (10505001) (FB5931643)
- When expanding a placeholder to a closure in Swift, code completion uses the closure’s argument names instead of `<#Type#>`. (53180195)
- Swift syntax highlighting in Xcode 13 is immediate and flicker free, both while editing and navigating between files. (54536855)
- Swift Jump to Definition now provides a more resilient experience even when your code is incomplete or your project can’t compile. Jump to Definition from Swift class, protocol, or method declarations also provides easy navigation to all subclasses, extensions, and protocol conforming types throughout your whole workspace. (54536865)
- Xcode 13 includes redesigned Swift code completion that maximizes reliability and performance, especially in the presence of structural and logical inconsistencies in project source code. Code completion in Xcode 13 helps you quickly finish your thoughts, even when the surrounding source is broken. Completions come up faster and are more predictive, suggesting the most likely completions after less typing. (54536896) In addition to completing types and methods, code completion in Xcode 13 offers whole statements like `for item in items {`, or `guard let item = item else { return nil }`, and even entire `switch` statements with accompanying `enum` cases. Code completion also searches across properties to offer chained completions like `layer.cornerRadius`, when completing `cornerRadius` in a view. Code completion helps you finish expressions that aren’t correct yet. It finds and identifies types in modules you haven’t imported, and automatically adds the necessary import. When the surrounding source has errors, code completion still infers what you mean. It offers the completion you’re looking for with a message describing how to make it valid.

###### Resolved Issues

- Fixed an issue where URLs in comments with MARKs, TODOs, and FIXMEs weren’t clickable. (10488785)
- Fixed an issue where elements of array and dictionary literals in Objective-C were indented too far to the right. (15964664)
- Fixed an issue where a string literal wouldn’t auto-close when it wasn’t at the end of a line. (34433455) (FB5931169)
- Fixed an issue where typing “///” to start a documentation comment would draw in the wrong font. (53331667)
- Improved Swift code completion for argument labels after defaulted or variadic arguments. (60346573)
- Improved Swift code completion for argument labels in generic initializers. (64168588)
- Fixed an issue where a newline inside a multiline string literal wouldn’t follow the indentation of the literal. (68076453)
- Fixed an issue where the line number was drawn out-of-sync when presenting the find bar. (70554325)
- To improve access to the Vim Mode, Xcode replaced the Enable Vim key bindings preference with an Edit > Vim Mode menu item. (75491567)
- Xcode now supports changing the line wrapping preference on a per-editor basis. (79168822, 79428189) (FB9157365)

##### Static Analyzer

###### New Features

- The static analyzer now warns about assertions with side effects, infinite loops, and more cases of C++11 `std::move` misuse. (34520956)

##### Storekit

###### New Features

- StoreKit Testing in Xcode supports comprehensive testing of in-app purchases built using StoreKit’s new modern Swift-based APIs. For more information about StoreKit 2, see [`StoreKit`](https://developer.apple.com/documentation/StoreKit). (69846798)

##### Swift

###### New Features

- Swift now natively supports concurrency programming using async/await and actors. For more information, see [`What’s new in Swift`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10192), [`Meet async/await in Swift`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10132), and [`Explore structured concurrency in Swift`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10134). ([`SE-0296`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0296-async-await.md), [`SE-0306`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0306-actors.md), 21398040, 78028712, 78029422)

- Functions and properties that should only be accessed from the main thread can be placed on the main actor by annotating them with the @[`MainActor`](https://developer.apple.com/documentation/Swift/MainActor) attribute. When calling a main-actor function, the call must come from a context that is itself on the main actor, or the call must be asynchronous. (70101562) For example: ```swift
@MainActor func f() { }

@MainActor func g() {
  f() // Already on the main actor. OK to call.
}

func h() async {
  f()            // Error: You can't synchronously call f(), because h() isn't on the main actor.
  await f()  // OK: Swift executes the asynchronous call to f() on the main actor.
}
``` Types can be placed on the main actor, which implies that all of their members are also on the main actor: ```swift
@MainActor class MyViewController: UIViewController {
  func method() { } // This method is implicitly on @MainActor.

}
```

- Asynchronous functions can create concurrently executing child tasks with `async let` bindings. The child task begins at the point that the parent declares the `async let`, and the variables the `async let` declares `await` at the point where they’re used. The `async let` waits until the child task completes and returns a value. (70101851) For example: ```swift
func chopVegetables() async throws -> [Vegetables]
func marinateMeat() async -> Meat
func preheatOven(temperature: Int) async -> Oven

func makeDinner() async throws -> Meal {
  async let veggies = chopVegetables()
  async let meat = marinateMeat()
  async let oven = preheatOven(temperature: 350)

  let dish = Dish(ingredients: await [try veggies, meat])
  return try await oven.cook(dish, duration: .hours(3))
}
``` All child tasks complete before the scope in which they are declared exits.

- The “for” loop can be used to traverse asynchronous sequences in asynchronous code. ([`SE-0298`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0298-asyncsequence.md), 78027927) ```swift
for try await line in myFile.lines() {
  // Do something with each line
}
``` Asynchronous for loops use asynchronous sequences, defined by the protocol `AsyncSequence` and its corresponding `AsyncIterator`.

- Swift translates an Obj-C method that delivers its results asynchronously via a completion handler into an `async` method that directly returns the result (or throws). (78028295) For example, Swift translates the following Objective-C method from CloudKit: ```objc
- (void)fetchShareParticipantWithUserRecordID:(CKRecordID *)userRecordID
    completionHandler:(void (^)(CKShareParticipant * _Nullable, NSError * _Nullable))completionHandler;
``` into an `async throws` method that returns the participant instance: ```swift
func fetchShareParticipant(
  withUserRecordID userRecordID: CKRecord.ID
) async throws -> CKShare.Participant
``` Swift callers can invoke this `async` method within an `await` expression: ```swift
guard let participant = try? await container.fetchShareParticipant(withUserRecordID: user) else {
  return nil
}
```

- Read-only computed properties and subscripts can now define their `get` accessor to be `async` and `throws`, by writing one or both of those keywords between the `get` and `{`. (78029522) Thus, these members can now make asynchronous calls or throw errors in the process of producing a value: ```swift
class BankAccount: FinancialAccount {
  var manager: AccountManager?

  var lastTransaction: Transaction {
    get async throws {
      guard manager != nil else { throw BankError.notInYourFavor }
      return await manager!.getLastTransaction()
    }
  }

  subscript(_ day: Date) -> [Transaction] {
    get async {
      return await manager?.getTransactions(onDay: day) ?? []
    }
  }
}

protocol FinancialAccount {
  associatedtype T
  var lastTransaction: T { get async throws }
  subscript(_ day: Date) -> [T] { get async }
}
``` Accessing these members, like `lastTransaction` above, requires appropriate marking with `await` or `try`: ```swift
extension BankAccount {
  func meetsTransactionLimit(_ limit: Amount) async -> Bool {
    return try! await self.lastTransaction.amount < limit
    //                    ^~~~~~~~~~~~~~~~ this access is async & throws
  }
}

func hadWithdrawlOn(_ day: Date, from acct: BankAccount) async -> Bool {
  return await !acct[day].allSatisfy { $0.amount >= Amount.zero }
  //            ^~~~~~~~~ this access is async
}
```

- `#if ... #endif` can now surround explicit member expression suffixes. (51690082) For example, the following code is now valid: ```swift
VStack {
  TextField("email address", text: $emailAddress)
  #if os(iOS)
    .keyboardType(.emailAddress)
  #endif
    .disableAutocorrection(true)
}
```

- Improved performance of overload resolution for generic operators, resulting in fewer “too complex to type check in reasonable time” errors in operator expressions. (65007946)
- You can now apply property wrappers to function and closure parameters. ([`SE-0293`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0293-extend-property-wrappers-to-function-and-closure-parameters.md), 66866426, 78029226) For example: ```swift
@propertyWrapper
struct Wrapper<Value> {
  var wrappedValue: Value

  var projectedValue: Self { return self }

  init(wrappedValue: Value) { ... }

  init(projectedValue: Self) { ... }
}

func test(@Wrapper value: Int) {
  print(value)
  print($value)
  print(_value)
}

test(value: 10)

let projection = Wrapper(wrappedValue: 10)
test($value: projection)
``` The call site can pass a wrapped value or a projected value, initializing the property wrapper using `init(wrappedValue:)` or `init(projectedValue:)`, respectively.
- The Swift compiler’s incremental build mode now considers fine-grained dependency information embedded directly into imported Swift modules. This dramatically improves the rebuild time of large projects with many modules by reducing the number of files that rebuild, even across import boundaries. (69595010)
- Xcode has a new Optimize Object Lifetimes build setting, under Swift Compiler - Code Generation. Enabling this performs more aggressive ARC optimization and shortens object lifetimes, which can help reduce the memory your app uses. This option also helps you find bugs where code makes invalid assumptions about object lifetimes. (73894256, 76671692)
- The `lazy` keyword now works in local contexts. (78028578) For example, the following code is now valid: ```swift
func test(useIt: Bool) {
  lazy var result = getPotentiallyExpensiveResult()
  if useIt {
    doIt(result)
  }
}
```
- Whenever a reference to `Self` doesn’t impede the usage of a protocol as a value type, or a protocol member on a value of protocol type, the same is now true for references to `[Self]` and `[Key : Self]`. (78028842) For example: ```swift
protocol Copyable {
  func copy() -> Self
  func copy(count: Int) -> [Self]
}

func test(c: Copyable) {
  let copy: Copyable = c.copy() // OK
  let copies: [Copyable] = c.copy(count: 5) // also OK
}
```
- It is now possible to use leading-dot syntax in generic contexts to access static members of protocol extensions where `Self` is constrained to a fully concrete type. (78029041) For example: ```swift
public protocol ToggleStyle { ... }

public struct DefaultToggleStyle: ToggleStyle { ... }

extension ToggleStyle where Self == DefaultToggleStyle {
  public static var `default`: Self { .init() }
}

struct Toggle {
  func applyToggle<T: ToggleStyle>(_ style: T) { ... }
}

Toggle(...).applyToggle(.default)
```
- Swift now considers default arguments of `Optional` type when deciding whether a call to a `rethrows` function can throw. (78029306) In Swift 5.4, such default arguments were ignored entirely by `rethrows` checking. As a result, the following example was accepted: ```swift
func foo(_: (() throws -> ())? = nil) rethrows {}
foo()  // No 'try' needed.
``` However, the next example was accepted as well, even though the call to `foo()` can throw and the call site isn’t marked with `try`: ```swift
func foo(_: (() throws -> ())? = { throw myError }) rethrows {}
foo()  // 'try' *should* be required here.
``` In the new behavior, the first example is accepted because the default argument is syntactically written as `nil`, which is known not to throw. The second example is correctly rejected because it’s missing a `try`, since the default argument  throw.
- Swift now supports Task local values. Using the `@TaskLocal` wrapper API, you can now bind and access values related to a running Task. The values are carried implicitly along with the Task’s execution and are inherited by child tasks. ([`SE-0311`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0311-task-locals.md), 78269874)
- Swift has significantly restructured the Task API to account for changes to the design in [`SE-0304`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0304-structured-concurrency.md). (78269970)
- Declarations inside an actor that would normally be actor-isolated can explicitly become non-isolated using the `nonisolated` keyword. You can use declarations to conform to synchronous protocol requirements. (78331401) For example: ```swift
actor Account: Hashable {
  let idNumber: Int
  var balance: Double

  nonisolated func hash(into hasher: inout Hasher) { // okay, non-isolated satisfies synchronous requirement
    hasher.combine(idNumber) // okay: can reference idNumber from outside the let
    hasher.combine(balance) // error: can't synchronously access actor-isolated property
  }
}
```
- You can define a type as a global actor. Global actors extend the notion of actor isolation outside of a single actor type, so that global state (and the functions that access it) can benefit from actor isolation, even if the state and functions are scattered across many different types, functions, and modules. Global actors make it possible to safely work with global variables in a concurrent program, as well as modeling other global program constraints such as code that must only execute on the main thread or UI thread. A new global actor can be defined with the `globalActor` attribute. (79339591) For example: ```swift
@globalActor
struct DatabaseActor {
  actor ActorType { }

  static let shared: ActorType = ActorType()
}
``` You can use global actor types as custom attributes on various declarations, which ensures that those declarations are only accessed on the actor described by the global actor’s `shared` instance. For example: ```swift
@DatabaseActor func queryDB(query: Query) throws -> QueryResult

func runQuery(queryString: String) async throws -> QueryResult {
  let query = try Query(parsing: queryString)
  return try await queryDB(query: query) // 'await' because this implicitly hops to DatabaseActor.shared
}
``` The concurrency library defines one global actor, `MainActor`, which represents the main thread of execution. Use it for any code that must execute on the main thread, e.g., for updating UI.

###### Resolved Issues

- Fixed an issue where capturing local property wrappers in a closure would result in a compiler error. (74457878)
- Converting a non-async function with an actor constraint into an async function without the actor constraint no longer produces an error. The async conversion introduces a hop to the necessary actor on the callee side. (76248452) For example, this code now compiles: ```swift
@MainActor func onMainActor() -> Int { 5 }

func test() {
  let _: () async -> Int = { @MainActor in
    onMainActor()
  }
}
```
- It’s no longer possible to conform a type to the `RandomNumberGenerator` protocol unless it implements the requirement: ```swift
mutating func next() -> UInt64
``` Previously, the compiler would use the defaulted generic `next()` if one wasn’t defined, resulting in a runtime crash. The compiler now detects this error at compile time instead. (76660011)
- Inside a non-async initializer for an actor, the compiler limits the use of `self`. Capturing `self` in a closure or calling a method or computed property generates a warning, because `self` could escape and create a race condition before the initializer is complete. (78790369) ```swift
actor A {
  var x: Int
  func tick() { self.x += 1 }

  init() {
    self.x = 0
    self.tick() // Warning: This use of actor 'self' can only appear in an async initializer.
                // Note: Convenience initializers allow non-isolated use of 'self' once initialized.

    Task.detached { await self.tick() } // Warning: Actor 'self' can only be captured by a closure from an async initializer.
                                        // Note: Convenience initializers allow non-isolated use of 'self' once initialized.
  }
}
``` If your existing code needs to access `self` within the initializer, you can declare a non-async `convenience init` in the actor that delegates to the designated initializer, just like in a class. ```swift
actor A {
  var x: Int
  func tick() { self.x += 1 }

  private init(v: Void) {
    self.x = 0
  }

  convenience init() {
    self.init(v: ())
    await self.tick() // Error: Await in non-async function.
                      // Must rely on the task to call 'tick' from this init.
    Task.detached { await self.tick() } // Closure capture is OK here.
  }
}
```
- When building incrementally, the Swift driver now considers the modification time of the target of a symlink instead of the symlink itself. (78828871)
- The compiler now correctly rejects the application of generic arguments to the special `Self` type. (79051797) For example: ```swift
struct Box<T> {
  // previously interpreted as a return type of Box<T>, ignoring the <Int> part;
  // now we diagnose an error with a fixit suggesting replacing `Self` with `Box`
  static func makeBox() -> Self<Int> {}
}
```
- Apps that contain Swift code referencing [`featureIdentifier`](https://developer.apple.com/documentation/UIKit/UIFontDescriptor/FeatureKey/featureIdentifier) or [`typeIdentifier`](https://developer.apple.com/documentation/UIKit/UIFontDescriptor/FeatureKey/typeIdentifier) now launch in earlier OS releases. (79090498)
- The Swift standard library no longer provides a nonfunctional default implementation of the `subscript(bounds: Range<Index>)` accessor for `Collection` implementors whose `SubSequence` isn’t `Slice`. Define your code’s `subscript(bounds: Range<Index>) -> SubSequence`, or use `Slice` as your `Collection`’s  `SubSequence`. ([`SR-14848`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-14848), 79891982)
- The compiler used to erroneously accept `@available` annotations on enum cases with associated values that were newer than the deployment target. (80238318) For example: ```swift
@available(macOS 12, *)
public struct Crayon {}

public enum Pen {
  case pencil

  @available(macOS 12, *)
  case crayon(Crayon)
}
``` While this worked in some cases, there was no way for the Swift runtime to perform the requisite dynamic layout needed in general, so this could cause crashes at runtime. The compiler now rejects such availability newer than the deployment target on enum cases.
- When declaring a method or function, you can declare an `isolated` parameter of actor type. When you call the function, the system executes it on the provided actor. `isolated` parameters extend the actor-isolated semantics of the `self` parameter of actor methods to arbitrary parameters. ([`SE-0313`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0313-actor-isolation-control.md), 80907464) For example: ```swift
actor MyActor {
  func f() { }
}

func g(actor: isolated MyActor) {
  actor.f()   // OK: This code always executes on "actor".
}

func h(actor: MyActor) async {
  g(actor: actor)        // Error: The call must be asynchronous.
    await g(actor: actor)  // OK: Hops to "actor" before calling g.
}
``` The `self` parameter of an actor method is implicitly `isolated`. The `nonisolated` keyword makes the `self` parameter no longer `isolated`.

###### Known Issues

- Swift Concurrency requires a deployment target of macOS 12, iOS 15, tvOS 15, and watchOS 8 or newer. (70738378)
- Swift libraries may fail to build for iOS targets that use armv7. (74120874) : Increase the platform dependency of the package to [`v12`](https://developer.apple.com/documentation/PackageDescription/SupportedPlatform/IOSVersion/v12) or later.
- `os_activity` APIs don’t track activity in Swift `async` code, and may produce incomplete information about that activity. (76080222)
- Swift tasks won’t have their priority escalated in response to awaiting on their handles. (76127624)
- The Swift compiler might crash when declaring an extension of a generic struct, enum, or class if the type has a `where` clause with a same-type requirement, and the extension has a `where` clause that constrains a generic parameter to a concrete type. (79570734)
- Swift libraries depending on Combine may fail to build for targets including armv7 and i386 architectures. (82183186, 82189214) : Use an updated version of the library that isn’t impacted (if available) or remove armv7 and i386 support (for example, increase the deployment target of the library to iOS 11 or higher).
- In macOS apps, the `free` function takes a non-optional argument, which might break existing code. (83133387) (FB9626044) : Define a wrapper for `free` that forwards the call to the SDK’s `free` only on non-optional arguments. For example: ```None
if let value = value { Darwin.free(value) }
```
- Availability checks in iPhone and iPad apps on a Mac with Apple silicon always return `true`. This causes iOS apps running in macOS 11 Big Sur to see iOS 15 APIs as available, resulting in crashes. This only affects apps available in the Mac App Store built with the “My Mac (Designed for iPhone)” or “My Mac (Designed for iPad)” run destination. It doesn’t affect Mac Catalyst apps. (83378814) : Use the following code to check for iOS 15 availability: ```None
        if #available(iOS 15, *), ProcessInfo.processInfo.operatingSystemVersion.majorVersion >= 15 {
```

###### Deprecations

- Type names are no longer allowed as an argument to a subscript parameter that expects a metatype type. (61749633, 78029595) For example: ```swift
struct MyValue {
}

struct MyStruct {
  subscript(a: MyValue.Type) -> Int { get { ... } }
}

func test(obj: MyStruct) {
  let _ = obj[MyValue]
}
```

##### Swift Packages

###### New Features

- Root packages and branch-based package dependencies can now use `unsafeFlags` in their target settings. (53679279)
- Swift packages can now declare a deployment target for Mac Catalyst, and can now specify Mac Catalyst as a platform in build conditions. Build conditions for macOS no longer apply to Mac Catalyst when the package declares a tools version of 5.5 or later. (60376383)
- Swift Packages now supports DriverKit as a platform. (66656190)
- Xcode now suggests packages from your added collections when you attempt to `import` a module that isn’t yet available locally. (69801540)
- Curated collections of packages can now be added in the Add Packages sheet. (70259327)
- Unit tests can now directly test executable targets. To do this, configure the unit test to depend on the executable target and import the module, exactly as for any library module. Swift Package Manager still builds a product in this case, so that the unit test can also test the executable itself using `Process()`. (75198161)

###### Resolved Issues

- Improved the diagnostic information that Swift Package Manager returns when file paths in package manifests are invalid. Specifying a nonexistent or invalid path for a source file or resource now produces an error. (60708059, 60745311, 64176116)
- Improved target-based dependency resolution. A more intuitive `.product(name:, package:)` syntax is now accepted, where `package` is the package name as defined by the package URL. (65048461)
- Linking Swift packages from application extension targets or watchOS applications no longer emits unresolvable warnings about linking to libraries not safe for use in application extensions. This means that code referencing APIs annotated as unavailable for use in app extensions must now themselves be annotated as unavailable for use in application extensions, in order to allow that code to be used in both apps  app extensions. (66928265)
- Fixed an issue that caused debug symbols to be removed from libraries that were built from Swift packages, making crash logs downloaded from TestFlight difficult to debug if their contents referenced those libraries. (67310056)
- Xcode no longer passes testing search paths to all targets. With this change, Swift package library targets (but not test targets) which import `XCTest` or `StoreKitTest` must now explicitly reference those frameworks in the package manifest using linker settings: ```swift
linkerSettings: [.linkedFramework("XCTest")]
``` This update doesn’t apply to test targets, which can still import test frameworks by default without any explicit mention in linker settings. (75061901)
- Fixed an issue where resolution of packages with binary dependencies failed to extract the binary archive. (77011310) (FB9085487)
- You can now remove recently used packages.(77056983, 79407145)
- Xcode no longer repeatedly reloads the package if you customize settings to store Xcode’s Derived Data directory inside the package source directory. (77208577, 78143803) (FB9109834)
- You can now access the Add Packages panel for Xcode windows hosting a package, and copy package dependencies to the clipboard. (79023046)

###### Known Issues

- Using Swift packages with binary targets may result in a “no such module” error when attempting to import the module of a binary target. (77465707)

##### Swift Refactoring

###### New Features

- New refactorings help migrate to async code. “Convert Call to Async Alternative” is available on calls that take a completion handler as their last argument, and refactors them to use the new async language features, assuming that an async equivalent of that function already exists. “Convert Function to Async” applies to any sync function, adds the `async` keyword to the signature, translates the completion handler argument (and calls to it) if there is one, and converts calls to async where possible. “Add Async Alternative” is similar to “Convert Function to Async” but adds the `async` function rather than converting the synchronous one. (68254700)
- You can now apply a new “Add Async Wrapper” refactoring action to a function with a completion handler. When you apply this wrapper, a new async alternative function is created that forwards to the original function. (77802486)

##### Templates

###### Resolved Issues

- Projects created from several templates no longer require configuration files such as entitlements and `Info.plist` files. Configure common fields in the target’s Info tab, and build settings in the project editor. These files are added to the project when additional fields are used. (68254857)
- New projects created with Xcode 13 use a new project version. Using the new projects with an older version of Xcode requires changing the project version in the File inspector along with manual migration of the configuration settings for `Info.plist` and entitlements you can now specify in the target build settings. (77344653)

##### Testing

###### New Features

- The Source Editor and Test Navigator have two new variants of the Run Test action that run a test selection without building. This is supported for a single test execution or repeated test executions. The Product > Perform Action submenu has a new command for rerunning the last test action without rebuilding. (13486284)
- You can now customize how a performance test’s custom metric’s measurements should be compared against a set baseline, using the `XCTPerformanceMeasurementPolarity` enum. This customization includes marking measurements as preferring them to be smaller (default), unspecified, or larger when compared against the baseline. (49493218)
- XCTest now has the ability to synthesize pointer interactions in UI tests on supported iOS devices. (56389548)
- Xcode now collects code coverage data for processes that crash while running tests. (58496759)
- Performance XCTests now support measuring CPU usage (`XCTCPUMetric`), disk writes (`XCTStorageMetric`), and memory usage (`XCTMemoryMetric`) for application launches. (61112495)
- `xcodebuild` has a new option `-enablePerformanceTestsDiagnostics YES` that collects diagnostics for Performance XCTests. The option collects a ktrace file for non-`XCTMemoryMetrics`, and a series of memory graphs for `XCTMemoryMetrics`. `xcodebuild` attaches diagnostics to the generated `xcresult` bundle. Note that memory graph collection isn’t available in simulated devices. (64495534)
- Test timeouts are now enabled by default in all newly-created test plans. Test plans created by converting a scheme require manually enabling test timeouts to preserve the existing behavior. (64861872)
- [`XCUIAutomation`](https://developer.apple.com/documentation/XCUIAutomation) now support using the `swipeUp`, `swipeDown`, `swipeLeft`, and `swipeRight` family of methods in macOS. (65229961)
- Performance tests now support collecting glitch metrics when using the `XCTOSSignpostMetric` for an animation `os_signpost` interval in macOS. (69345790)
- XCTest now supports test repetition. (69470788, 71428753, 72078437) There are three test repetition modes. Up Until Maximum Repetitions repeats a test up to the specified maximum regardless of the status. Until Failure repeats a test until it fails. Retry on Failure retries a test until it succeeds. Enable test repetition in your test plan, `xcodebuild`, or by running your test from the test diamond by Control-clicking and selecting Run  Repeatedly to bring up the test repetition dialog. When using `xcodebuild`, pass `-test-iterations` with a number to run a test a fixed number of times, or combine it with `-retry-tests-on-failure` or `-run-tests-until-failure` to use one of the other stopping conditions. For example, to run your test with repetition from the command line, start with the base `xcodebuild` command to run your test, and add the flags `-test-iterations` set to 100 and `-run-tests-until-failure`: ```shell
xcodebuild test -project MyProject.xcodeproj -scheme MyProject -destination 'platform=iOS Simulator,name=iPhone 12,OS=15.0' -test-iterations 100 -run-tests-until-failure
``` In a Test Plan, configure your test plan to use test repetitions and go to the test plan. Click Configurations, then under Test Execution, set Test Repetition Mode and also set Maximum Test Repetitions. The options for Test Repetition Mode are: Until Failure, Retry on Failure, and Up until Maximum Repetitions. Maximum Test Repetitions must be a positive integer. Setting test repetitions with `xcodebuild` or the test diamond overrides any test plan setting.
- A new transparent screen overlay indicates the activity while automation is running, and displays text describing how to stop the automation. If you interact with the device while automation is running, the overlay fades away to allow you to better see the screen contents. This new behavior is present in macOS 12, iOS 15, tvOS 15, and watchOS 8. In macOS, or when using automation on devices with a password, you must run the automation from an admin account, and must authenticate to authorize the automation. This authorization is cached for eight hours. You no longer need to authorize the Xcode Helper app to use Accessibility when running in macOS 12. (71297492)
- XCTest now supports resetting the authorization status for the protected resource “user tracking” from the App Tracking Transparency framework. (72452504)
- Test methods written in Swift may be marked `async` or `async throws` to allow calling and awaiting results from async APIs, as part of the Swift Concurrency language feature. This reduces the need to explicitly wait on an `XCTestExpectation` and helps prevent concurrency-related bugs in tests. (72600990) For example: ```swift
// An example async API to test.
func chopVegetables() async throws -> [Vegetable]

func test_chopVegetables() async throws {
    let vegetables = try await chopVegetables()
    XCTAssertEqual(vegetables.count, 3)
}
```
- `XCTestCase` now includes an `addTeardownBlock` method overload whose closure parameter is `async throws`, which allows teardown blocks to natively call throwing APIs or await the results of async APIs. (73156219)
- `xcodebuild` now supports passing certain environment variables to test runner processes. In the environment where `xcodebuild` is invoked, prefix any variable with `TEST_RUNNER_` to pass that variable (with the prefix stripped) to XCTest test runner processes. For example, running `env TEST_RUNNER_Foo=Bar xcodebuild test ...` causes the environment variable `Foo=Bar` to be set in the test runner’s environment. (74104870) Additionally, existing variables may be modified using the special token `__CURRENT_VALUE__` to represent their current value. For example, `TEST_RUNNER_Foo=__CURRENT_VALUE__:Bar` appends the string `:Bar` to any existing value of `Foo`. Note that only test runner processes receive these environment variables. To set them in apps targeted by UI tests, customize the `XCUIApplication.launchEnvironment` dictionary prior to launching the app.
- The `XCTExpectFailure` function now includes Swift overloads for customizing certain options without needing to create an `XCTExpectedFailure.Options` instance, such as `strict`, `enabled`, and `issueMatcher`. (76663874) Here are two examples: ```swift
// This test declares an expected failure in the remainder of the test method body, with strict behavior disabled:
func test_disablingStrict() {
    XCTExpectFailure("https://dev.myco.com/bugs/1234 (Something is non-deterministic)", strict: false)
    // ...Test something expected to fail...
}

// This test declares an expected failure within the scope of its first block parameter, along with a custom issue matcher in the second parameter:
func test_customIssueMatcher() {
    XCTExpectFailure("...") {
        // ...Test something expected to fail...
    } issueMatcher: { issue in
        issue.compactDescription.contains("errorCode: 999")
    }
}
```
- XCTest now has the ability to synthesize Digital Crown rotation in watchOS UI tests. (76816883)
- XCTest now includes `async throws` overloads of the `setUp` and `tearDown` instance methods. XCTest invokes the async `setUp` overload first before `setUpWithError` and non-async `setUp`, but it invokes async `tearDown` last, after non-async `tearDown` and `tearDownWithError`. XCTest records errors thrown by these new overloads as issues. (77610427)
- Tests can now call `XCTestCase.expectation(description:)` — as well as other `XCTestCase` APIs that return an `XCTestExpectation` — from any thread. This removes a previous requirement that tests call these APIs from the main thread, and it allows existing tests using them to adopt `async` without requiring `@MainActor`. (79163972)

###### Resolved Issues

- Improved the performance of working in large workspaces that use many test plans. (56445700)
- XCTest now supports resetting the authorization status of additional protected resources: Network Volumes, Removable Volumes, Apple Events, and Focus. (64937038) (FB7828459)

###### Known Issues

- Attempting to run unit or UI tests for Watch apps crashes Xcode when the Run scheme action’s executable is set to None. (74928871) : Set the Run scheme action’s executable to a valid WatchKit app target built by the scheme.
- UI Test Recording fails to generate code for iOS Simulator targets if recording starts after code execution has stopped at a user-defined breakpoint. (77924295) : With no breakpoint set, place your cursor within a test method and press the record button.
- UI Test Recording fails to generate code for targets in a simulated watchOS device. (78024399)
- UI Test Recording fails on watchOS devices, and presents an alert saying “Unable to install .” (78024956)
- Swift async test methods aren’t executed on the main queue as non-async test methods are. (78176413) : Add the `@MainActor` attribute to affected async test methods or classes.
- UI tests may time out and display the error “Timed out while requesting automation session for ” while starting in watchOS and tvOS simulators that weren’t already booted when the test action initiated. (78475446)
- You can only call XCTest UI automation APIs (such as `XCUIApplication`) from the main thread. XCTest UI automation APIs might fail when used in `async` Swift test methods that don’t include `@MainActor`. (80386414) : Include `@MainActor` on affected test methods or classes.

## See Also

- [Xcode 13.4.1 Release Notes](xcode-13_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.4 Release Notes](xcode-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3.1 Release Notes](xcode-13_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3 Release Notes](xcode-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2.1 Release Notes](xcode-13_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2 Release Notes](xcode-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.1 Release Notes](xcode-13_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-13-release-notes)*