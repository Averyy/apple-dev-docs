# Xcode 14 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 14 includes Swift 5.7 and SDKs for iOS 16, iPadOS 16, tvOS 16, watchOS 9, and macOS Monterey 12.3. The Xcode 14 release supports on-device debugging in iOS 11 and later, tvOS 11 and later, and watchOS 4 and later. Xcode 14 requires a Mac running macOS Monterey 12.5 or later.

##### General

###### New Features

- Xcode 14 enables a single target to support multiple platforms and conditionally include dependencies, code, resources, and build settings for specific platforms. (74664328)
- Xcode 14 supports development of DriverKit drivers for iPadOS. (81117498)
- Xcode 14 includes a default template for watchOS apps that combines the WatchKit App and WatchKit App Extension targets into a single Watch App target, simplifying code, asset, and localization management. You can deploy single-target watchOS apps to watchOS 7 and later. (83222217)

###### Resolved Issues

- Fixed: When a storyboard is open and watchOS or tvOS content is deleted from Xcode Settings, the storyboard won’t close. (87471381)

###### Known Issues

- If a `Package.swift` file is added to the containing folder while that folder is open in Xcode, the package will not be recognized. (85075018) : Quit and relaunch Xcode.
- `CGFLOAT_EPSILON` is no longer always type `Float` on watchOS, and it may cause compile issues. (88698530) : Convert it first to `CGFloat` by using the initializer `CGFloat(CGFLOAT_EPSILON)`. `CGFloat` is now supported on both 32- and 64-bit platforms.
- Xcode 14 can fail to find tools using `xcodebuild -find` (which is used by `xcrun` and the wrappers in `/usr/bin` such as `/usr/bin/clang`) if first launch content isn’t installed. (98008921) : Run `xcodebuild -runFirstLaunch`, or launch Xcode.app first.
- Xcode can sometimes consider the platform sim runtime missing when performing a user Log Out and Log In. (99200503) : Restart the machine.
- When running in macOS 13 beta, AppIntents code may fail to build with Xcode 14. (99661742) (FB11470314) : Build AppIntents code with Xcode 14 beta 6, or on a Mac running macOS Monterey 12 with Xcode 14.
- Xcode 14 cannot be used with iOS 15.7 for development. (99847608) : Use Xcode 13.4.1 with iOS 15.7.

##### Apple Clang Compiler

###### New Features

- New C++ projects you create in Xcode use C++20 language dialect by default. (93456065)
- Several C++20 and C++2b papers have been implemented: - C++20 papers that have been implemented: - P0692R1 - Access checking on specializations
- P0388R4 - Permit conversions to arrays of unknown bound
- C++2b papers that have been implemented: - P1938R3 - `if consteval`
- P1401R5 - Narrowing contextual conversions to `bool`
- P1949R7 - C++ identifier syntax using Unicode Standard Annex 31
- P2360R0 - Extend `init` statement to allow alias declaration (93898598)

###### Resolved Issues

- Fixed: Xcode doesn’t provide semantic highlighting and jump-to-definition support for C++20 concept declarations and the requires clauses in templates. (93046529)

###### Deprecations

- Starting with Xcode 14, bitcode is no longer required for watchOS and tvOS applications, and the App Store no longer accepts bitcode submissions from Xcode 14. Xcode no longer builds bitcode by default and generates a warning message if a project explicitly enables bitcode: “Building with bitcode is deprecated. Please update your project and/or target settings to disable bitcode.” The capability to build with bitcode will be removed in a future Xcode release. IPAs that contain bitcode will have the bitcode stripped before being submitted to the App Store. Debug symbols can only be downloaded from App Store Connect / TestFlight for existing bitcode submissions and are no longer available for submissions made with Xcode 14. (86118779)

##### Asset Catalogs

###### New Features

- Simplify an app icon with a single 1024x1024 image that is automatically resized for its target. Choose the Single Size option in the app icon’s Attributes inspector in the asset catalog. You can still override individual sizes with the All Sizes option. (18475136) (FB5503050)
- You can now paste copied images from the Finder directly into the asset catalog outline. (58980721)
- You can now double-click an image slot to show the open file panel and choose a replacement asset. (81365822)
- You can specify the default rendering mode for custom symbols in an Asset Catalog. Set the Render As attribute to automatic, template, multicolor, or hierarchical. The system then uses the default rendering mode for the symbol, unless you explicitly override it. For more information on custom symbols, see [`Creating custom symbol images for your app`](https://developer.apple.com/documentation/UIKit/creating-custom-symbol-images-for-your-app). (84513859)

###### Resolved Issues

- The “All Sizes” mode for app icons has been made more flexible and includes some additional sizes not used before. The “All Sizes” mode doesn’t require that all slots are filled, sizes can be provided only as needed. App icons created with Xcode 13 and earlier can be converted from “All Size (Xcode 13)” mode to either “All Sizes” or “Single Size”. (93682080)

###### Known Issues

- Apps using a single-size app icon can fail App Store validation if the deployment target is older than iOS 12 or watchOS 4. (98471456)

##### Build System

###### New Features

- Xcode provides a new assistant editor for build logs that focuses on parallelism to help identify build performance issues. This visualization displays events as a grid of colored blocks where the vertical axis represents level of parallelism and the horizontal axis represents time. (47858322)
- Xcode 14 can now compile targets in parallel with their Swift target dependencies. (57116972)
- Swift driver, the component that orchestrates Swift front-end invocations, is now integrated into Xcode’s build system, allowing for more fine-grained dependencies to other build system tasks and explicit scheduling. (72440175)
- In the Build Phases pane, you can now batch edit files in the multi-select table view. When you edit the platform filters column of that table, the system applies changes to all files in the selection. (80683128) (FB9340886)
- Swift-only framework and dynamic library targets can opt into a new build system optimization using the `EAGER_LINKING` build setting. When you enable this, Xcode emits additional artifacts during Swift compilation, which allows Xcode to unblock linking of downstream targets earlier, increasing parallelism in builds. (82396635)
- The build system runs tasks from different build phases in parallel when input and output dependencies don’t enforce their ordering. You can opt into this new behavior for run script build phases using the `FUSE_BUILD_SCRIPT_PHASES` build setting. (82396977)
- The App Store now supports app thinning for precompiled Metal shaders. (82902821)
- Xcode builds for watchOS devices now include the arm64 architecture by default. (83319300)
- Added a new `:relativeto=` macro replacement operator for build settings, which you can use to compute the relative path from one path to another; for example: ```None
 $(INSTALL_PATH:relativeto=/usr/lib)
``` where `INSTALL_PATH` is “`/usr/bin`”, and evaluates to “`../lib`”. You can use this in a build rule to copy a series of file references while preserving their directory hierarchy under the destination directory, or to compute a target’s expected `rpaths` using the relative path between its own install path and the known install paths of its dependencies. (88293015)
- Xcode now provides `RECOMMENDED_MACOSX_DEPLOYMENT_TARGET`, `RECOMMENDED_IPHONEOS_DEPLOYMENT_TARGET`, `RECOMMENDED_TVOS_DEPLOYMENT_TARGET`, `RECOMMENDED_WATCHOS_DEPLOYMENT_TARGET`, and `RECOMMENDED_DRIVERKIT_DEPLOYMENT_TARGET` build settings that indicate the recommended minimum deployment versions for each supported Xcode platform. (90464341)
- You can now enable sandboxing for shell script build phases using the `ENABLE_USER_SCRIPT_SANDBOXING` build setting. Sandboxing blocks access to files inside the source root of the project as well as the Derived Data directory unless you list those files as inputs or outputs. When enabled, the build fails with a sandbox violation if a script phase attempts to read from or write to an undeclared dependency, preventing incorrect builds. (90506067)

###### Resolved Issues

- Fixed an issue where multiple Xcode projects referencing the same `xcconfig` file (which in turn included another `xcconfig` file) incorrectly computed the same build settings across both projects. (84319288) (FB9707003)
- Fixed: watchOS device run destinations no longer appear twice in the run destination menu. (85635959)
- Improved the loading speed of large workspaces that have many targets that share `.xcconfig` files. (85985712)
- Fixed: When you archive a watchOS app with the [`arm64e`](https://developer.apple.comhttps://developer.apple.com/documentation/security/preparing_your_app_to_work_with_pointer_authentication) architecture enabled, it fails to build. (93550623)

###### Known Issues

- Crash reports from Mac Catalyst apps aren’t fully symbolicated in the Xcode Organizer. (94820955)

###### Deprecations

- Because bitcode is now deprecated, builds for iOS, tvOS, and watchOS no longer include bitcode by default. (87590506)
- Added a new build setting, SWIFT_TOOLS_DIR, which replaces SWIFT_EXEC as the recommended mechanism to use a custom swift-frontend executable. SWIFT_TOOLS_DIR should be set to the path of the directory which contains swift-frontend and related tools. Note that because the Swift driver is now integrated in the Xcode build system,  SWIFT_TOOLS_DIR and SWIFT_EXEC cannot be used to specify a custom driver binary unless SWIFT_USE_INTEGRATED_DRIVER is set to NO. (88967344)
- The legacy build system has been removed. (90801041)
- Building iOS projects with deployment targets for the armv7, armv7s, and i386 architectures is no longer supported. (92831716)
- Building for deployment to OS releases older than macOS 10.13, iOS 11, tvOS 11, and watchOS 4 is no longer supported. (92834476)
- When removing a condition from the variant editor, the value will not be persisted. (98149034) : Use the Build Settings Editor to remove the condition.

##### Debugging

###### New Features

- The memory graph debugger now displays all the incoming and outgoing references in the memory graph. You can adjust the set of visible nodes in the new popover. (69454709)
- LLDB now shows progress updates in Xcode and the command line for long running operations. (73511008)
- You can now invoke LLDB’s crash log script with `xcrun crashlog <path/to/crash>`. (79991815)
- The Thread Performance Checker shows runtime performance issues in the Issue navigator and the source editor while debugging an app. Select the Thread Performance Checker checkbox in your app target’s Run Scheme to enable this feature. (80048810)
- It’s now possible to open a `.xcresult` bundle for a launch scheme action. (88932007)
- Xcode now shows a new launch log in the Report navigator. The log indicates the actions Xcode takes to install, launch, and debug. (90859910)

###### Resolved Issues

- Improved the performance when debugging Swift programs on iOS devices. Instead of copying the reflecting metadata from the iOS device, Xcode can now read the metadata from disk. (73179144)
- Xcode now groups log items for the same launch scheme action in the Report navigator. (87216988)
- Fixed: Stepping into a Swift async function in LLDB finishes the current function instead. (88142757)

###### Known Issues

- Unable to attach a debugger to Lock Screen Widget Extension. (93941779) : Edit the Extension scheme - under Run action, Arguments tab, set the environment variable ‘_XCWidgetKind’ to be one of your class/struct names implementing the widget.

##### Documentation

###### New Features

- Swift-DocC in Xcode now supports writing and building documentation for Objective-C and C APIs. (58760015)
- The Swift-DocC documentation websites Xcode 14 produces include a new navigation sidebar for exploring and filtering the documentation. (89031049)
- The Swift-DocC documentation Xcode 14 produces is now, by default, compatible with most managed hosting services, including GitHub Pages. (91173450)

###### Resolved Issues

- Fixed: Swift-DocC incorrectly emits diagnostics about directives not being supported in symbol source documentation when building documentation for Objective-C projects that include Doxygen commands. (90953916)
- Fixed: Objective-C documentation for multi-language APIs show Swift symbol relationships instead of Objective-C relationships. (91627374)
- Fixed: Swift-DocC incorrectly emits diagnostics about unresolvable symbol links for documentation inherited from symbols in other modules. (92185538)
- Fixed: Building documentation for types that conform to the Swift Charts `ChartContent` protocol failed. (93610106)

##### Instruments

###### New Features

- Aggregation functions operating on intervals now more accurately calculate their results when a time filter is active, based only on the portion of the overall interval that intersects the current time filter. (32330648)
- The Detail Filter now allows filters to be applied to a specific column when viewing a List View. These typed filters can be added by using contextual menus on displayed values or by typing in a token and then selecting a token type. (56080914)
- Main Thread tracks are now ordered first when showing tracks in the Instruments timeline. (59876638)
- Instruments has a new Hang Tracing instrument that shows when an app’s main thread is unable to handle incoming events for an extended period of time, potentially causing the UI to hang. In addition, the Time Profiler and CPU Profiler instruments also display potential hangs. (65694830)
- Histogram graphs in Instruments now show the duration of the time range used for data aggregation in the hover-over tooltip. (65684291)
- Instruments’ list views now show a status label at the bottom, reporting on how many rows are present and selected in the current view. (82652407)
- A new Core ML template is available in Instruments. This template includes new Core ML and Neural Engine Instruments along with GPU and Time Profiler tools. Use this template to help profile Core ML usage and understand how your models are running on device. Combining information from the Core ML, Neural Engine, and GPU Instruments can help to track what operations are executed on accelerated hardware. Aggregate timing data is available for each event, model, and submodel. (83123510)
- You can open a new contextual menu by Control-clicking intervals in the timeline. The menu provides actions for setting the time filter to the chosen interval or revealing the corresponding information in the detail area. (86728567)
- Instruments’ Run Information view now includes the architecture of the target binary when recording a single process trace. (89733709)
- Instruments has a new Runloop instrument that shows runloop usage and individual iterations, and visually differentiates runloop sleeps and busy intervals for all runloops in a process. (89746568)
- Values in aggregation or list detail view now become highlighted when you point the cursor over them, and you can Control-click on a value to see a contextual menu. This menu shows actions for copying the value, setting the detail filter, and adding or pinning a track if the value has a track representation. (90817779)
- Instruments now includes a new Swift Concurrency template for tracing the usage and behavior of Swift’s concurrency primitives. The template contains: - A new Swift Tasks instrument that shows task states over time, summarizes task states, provides a detailed task narrative, illustrates structured concurrency relationships, and constructs call trees of task creation callstacks.
- A new Swift Actors instrument for tracking task behavior across actors that shows task queuing for each actor and helps diagnose issues with actor-isolated code and contention. These instruments require instrumentation in the Swift concurrency runtime that’s first available in macOS 13, iOS 16, tvOS 16, and watchOS 9 or later. (69852855)
- `heap`, `leaks`, and Instruments’ leaks tool now report fewer false references originating from Swift concurrency-related allocations and identify these as Swift AsyncTask allocations. (72907112)
- `leaks --atExit -- <command>` now automatically sets `MallocStackLogging=lite` in the environment for the specified command so that Instruments can show stack backtraces for leaked allocations. To use a different setting of that environment variable (such as YES or NO), set the environment variable prior to running `leaks`. (73779272)
- `xctrace` now sends a Darwin notification when tracing starts, which should be preferred instead of reading the command’s standard output.  To use it, specify the `notify-tracing-started` option with the desired notification name and use `notify_register_dispatch` to receive the asynchronous notification in your scripts. (75745933)
- Improved the performance of the System Trace template’s analysis. Instruments now presents recordings to the user more quickly; however, when tracing a single process, you can’t see the thread states for other processes. To see the states of other processes, trace “All Processes” instead. (79904471)
- For processes running with `MallocStackLogging` enabled, `heap`, `leaks`, and the Xcode memory debugger display type names for nonobject allocations in the form `malloc in <function name>` where “function name” is the first nonallocation stack frame. This feature helps to better identify the purpose of nonobject memory. (85598783)
- `heap -addresses=all` now displays the descriptions of CFData objects that contain binary `.plist` files in a more human-readable way. (88466642)

###### Resolved Issues

- `heap` , `leaks`, and `stringdups` now include the contents of some types of heap-allocated Swift strings in descriptions about those strings’ allocations. (14902403)
- The GCD Performance instrument now properly interprets events with codes “7” and “9.” (69721960)
- The source viewer design in Instruments includes improvements to better display performance data: - There is a new Interleave mode for viewing source code and associated disassembly together, making it easier to associate the instructions generated for each source code line.
- The source viewer now shows sampled values attributed to a line of code or disassembly in a separate column instead of as line annotations.
- The source viewer now displays CPU Counters, PMC events, and dynamic formulas configured in the recording options next to source and disassembly. (80232392)
- Fixed an issue where Source View in Instruments sometimes failed to present performance annotations when opened from the Call Tree view. (80501587)
- When using Instruments Source Viewer in split view mode, selecting disassembly now also selects the corresponding source on the left. (82642041)
- Fixed an issue where `xctrace export` would sometimes output UTF-16 string values instead of UTF-8, leading to rendering errors in Terminal. (87594987)
- Fixed an issue where some recorded events after a reboot would be lost when importing log archives spanning device reboots. (89003393)
- Fixed a bug where `xctrace list devices` sometimes didn’t include all physically connected devices in its output. (89142775) (FB9913864)
- `heap`, `leaks`, and Instruments now correctly recognize side tables of deallocated Swift objects as being side tables. (89459805)
- Fixed an issue where Instruments wouldn’t allow recording tvOS devices connected over WiFi. (89592418) (FB9935783)
- Fixed an issue where a custom Instruments package build could fail when the same variable was used more than once in the expression field. (89653878)
- `heap`, `leaks`, and Instruments now show better human-readable names for additional Foundation and Swift standard library types. (90441836)
- `xctrace` no longer returns an error status when tracing only causes warnings. Issues are now attributed with the appropriate severity. (90560207) (FB9963155)
- Fixed an issue during `xctrace export` where allocations and VM tracker data was sometimes exported with missing data rows. (90560947) (FB9963169)
- Fixed an issue where Instruments would forget command-line arguments after opening and closing the target editor when arguments were already present. (90666084)
- Fixed an issue where moving the inspection head in the track ruler would also scroll the Y axis of the timeline. (90810506)
- Fixed: Runloop intervals for run, iteration, waiting, and busy periods have incorrect labels and length when displayed in a process track. (91130163)
- Fixed an intermittent Instruments crash when recording traces with the Allocations or Leaks templates. (93916110)
- Fixed: Creating a Core ML Performance Report may fail after enabling Developer Mode on the device. (93923607)

###### Known Issues

- Symbolication of user code with a `dSYM` may fail for tailspin files imported into Instruments. Symbols for system libraries also aren’t appearing when these files are loaded. (93261223) : Symbolicate hang logs in Terminal with `spindump -i <UIKit-runloop*.ips>`.
- Disable the Thread Performance Checker through the Diagnostics tab in the Scheme Editor if your iOS or macOS App uses Fishhook to hook calls to `libSystem` for debugging/tracing purposes. (94724380) (FB10131267)

##### Interface Builder

###### New Features

- `UISplitViewController` now supports sidebars in Mac apps built with Mac Catalyst. To enable sidebars, set the Primary Style in the split view controller’s attributes inspector. (82004740)
- Interface Builder now supports new center item groups on `UINavigationItem`. (83252931)
- Added a checkbox in the Attributes inspector to enable the standard find and replace UI for `UITextView`. (83726669)
- Interface Builder now updates scenes asynchronously. (83786577)
- Interface Builder now supports authoring `NSComboButton`. (85583290)
- Interface Builder now supports authoring `MKMapView` with `MKMapConfiguration`, including, `standard`, `imagery`, and `hybrid`. (85607049)
- Toggle the keyboard from the `UIViewController`’s attribute inspector to understand how the keyboard affects the layout guides in canvas. (87975498)
- A new checkbox appears on `WKWebView` to enable standard find and replace UI. (88049266)
- You can now edit an SF Symbol’s default configuration (including font, scale and weight) with NSButton and NSImageView by choosing the symbol through the control’s image inspector. (88400241)
- Support for `UIPasteControl` for iOS to allow pasting content with a single tap without a paste notification or alert. The control can target any object conforming to `UIPasteConfigurationSupporting` (e.g., `UIResponder`) to receive pasted content. (88648426)
- Access and search for SF Symbols through the symbols library tab. Open the library (Xcode > View > Show Library) and click the Symbols tab. You can drag the symbols to the source editor. (88726368)
- Interface builder includes new `NSColorWell` default, minimal, and expanded styles in macOS 13. (89051231)
- Interface Builder now supports authoring `MKPointOfInterestFilter`. (89368386)
- Interface Builder now supports authoring `MKLookAroundViewController`. (90994596)
- Interface Builder now supports authoring `RoomCaptureView`. (91640003)

###### Resolved Issues

- `UIBarButtonItemGroup` has been added to the Interface Builder object library. It can be dragged into a `UINavigationItem` to provide Center Items. (19160962)
- The `UIColorWell` is now available in the object library. When tapped, the control presents a color picker. (67016855)
- You can now enable the keyboard layout guide on a scene’s `UIView` through the size inspector. Constrain views to the layout guide so they adjust during layout when the keyboard shows on screen. (81959069) (FB9514618)
- Made outline visibility for new documents match last user toggled state. (82857926) (FB9607879)
- Fixed an issue with outlet and action connections to AppleScript-based AppDelegates. (83373726) (FB9643535)
- Fixed an issue where saving a document with more than one Look Around View Controller would crash Xcode. (92304543)
- WatchKit storyboards are deprecated in watchOS 7.0 and later. Please migrate to SwiftUI and the SwiftUI Lifecycle. (94058186)
- The Interface Builder outline view now saves and restores visibility/width state globally instead of per document. (97084370)

###### Known Issues

- The font size doesn’t change to match the control size for `NSComboButton`. (94610724) (FB10094813)

##### Linking

###### Known Issues

- Swift apps built with Xcode 14 may fail to link against `libswiftFoundation.dylib`. This can cause the app to misbehave when running on operating systems prior to macOS 13 Ventura and iOS 16, including strings not printing correctly and exceptions being thrown for missing methods on Foundation data types. (99457165) : Explicitly reference a symbol from `libswiftFoundation` in code, for example by adding `_ = JSONDecoder()` in a function.

##### Localization

###### New Features

- You can now export local Swift packages for localization. Xcode generates a single localizations catalog for all projects and Swift packages contained in a project or workspace. You can also use `xcodebuild -importLocalizations` and `xcodebuild -exportLocalizations` to export or import a Swift package. (56355281)

###### Resolved Issues

- Localized strings that explicitly specify a `table` parameter that isn’t a string literal are no longer extracted when running `genstrings` or exporting for localization. Previously, `genstrings` defaulted to a table named `Localizable.strings`. (65063595)
- Fixed an issue where Xcode sometimes didn’t raise an error when exporting a malformed `.strings` file for localization. (85278818)
- Fixed an issue where Xcode silently ignored malformed XLIFFs when importing localizations. (86849358) (FB9819403)
- `xcodebuild -importLocalizations` and `xcodebuild -exportLocalizations` now include timestamps for localization operations. (89373526)
- Xcode automatically extracts `NSHumanReadableDescription` from Info.plist files when exporting for localization. (89591666) (FB9935770)
- Keys in `.strings` files that exist in a `.stringsdict` with `NSStringDeviceSpecificRuleType` are no longer marked as `translate="no"` in the exported XLIFF, because these also fall back to the `.strings` file value at runtime. (90785024)
- Fixed an issue where Xcode raised warnings for untranslated units marked as `translate="no"` when importing localizations. (91692843) (FB9982115)

##### Metal

###### New Features

- TextureConverter 2.0 adds support for decompressing textures, advanced texture error metrics, and support for reading and writing KTX2 files. The new AppleTextureConverter library makes TextureConverter available for integration into third-party engines and tools. (82244472)

###### Known Issues

- Profiling Metal captures containing mesh pipelines is disabled. (93255574)

##### Organizer

###### New Features

- TestFlight Screenshot Feedback is now available in the Xcode Organizer. You can now view screenshot and textual feedback for iOS and macOS in Xcode by selecting the “Feedback” item in the reports section of the sidebar. To get started, sign-in with the Apple Developer account associated with your TestFlight app, and open the Organizer by selecting Window > Organizer in the menu bar. In addition to viewing feedback, you can reach out directly to testers, and share feedback with members of your development team. (56519107)
- TestFlight Screenshot Feedback can now be opened in the Xcode Organizer via the “Open in Xcode 14” button in App Store Connect. (83599827)

##### Previews

###### New Features

- Xcode Previews now resume automatically when creating new projects. (50474683)
- Xcode Previews no longer pauses after editing a file and switching back to a preview and resuming, or when projects modify the source directory during a build. (71593736)
- Errors from widget and complication previews are now exposed in the canvas. (76966327)
- Xcode Previews now uses data from StoreKit Configuration files if one is set in the scheme’s run options. Previews only supports a subset of StoreKit APIs. (82312384)
- Preview diagnostics are now accessible using Xcode’s Editor > Canvas > Diagnostics menu item. (92620156)

###### Resolved Issues

- Xcode Previews now correctly displays string literals that contain Swift unicode escape sequences. (32722474)
- Xcode Previews can now run on physical devices without requiring a containing application, making it easy to preview on-device for frameworks and Swift packages. Xcode automatically prepares a proper signed application for your default signing identity to host the preview. (50206641)
- The Xcode Previews canvas now supports and defaults to zoom-to-fit. (51146527)
- Fixed several issues when using watchOS previews in Xcode. Previews now correctly work when navigating between files in the containing iOS app or the embedded watchOS app or frameworks and packages included by one or more of those targets. (53183015)
- Fixed several cases where making edits in a particular order would cause previews to fail with a missing symbol error (53740398)
- Xcode Previews can now use the scheme’s runnable when deciding which app to use for hosting a preview. For example, in a project with a framework that both the full and beta versions of an app share, Xcode Previews automatically picks the app to launch for previews based on the selection in the scheme. (60251198)
- Fixed an issue where using multiple previews would cause a timeout error in Xcode Previews. (68939151)
- Fixed an issue causing Xcode Previews to fail for files with two closing braces on the same line. (74035344) (FB8992136)
- Xcode Previews no longer pauses on large edits. Instead, Previews continues auto-building by detecting the kinds of changes being made and dynamically adjusting the update frequency to balance battery life and latency. (77799105)
- Fixed an issue in Xcode Previews causing frequent pausing when using Swift Playgrounds projects opened in Xcode. (79206975)
- Fixed an issue in some projects where a package loading error never went away in Xcode Previews. (79207076)
- Fixed an issue where Xcode Previews might not render correctly after closing and opening the canvas. (83789694)
- Fixed cases of Xcode Previews not reflecting changes made to files in Swift Packages. (84529522)
- Fixed an issue where the Xcode Previews canvas wasn’t properly showing when using `@_implementationOnly` imports. (86214393)
- Xcode now displays each preview on its own dedicated page that includes new controls that allow you to change common settings such as color scheme, orientation, or dynamic type size without writing any code. (87357785)
- Xcode Previews are now interactive by default. You can use the mode switcher along the bottom of the canvas to switch between interactive, selection, and variant modes. (87358985)
- Xcode Previews now supports preview variants: automatically generated previews that let you see your view in multiple appearances, type sizes, or orientations at the same time without writing any configuration code. (88937848)
- Previews now work in modules using `@_spi`. (89653122)
- Crashes in previews are now properly reflected for Swift Playgrounds projects opened in Xcode. (91716026)
- Changing the active run destination now correctly updates the Xcode Previews canvas. (92152617)
- Improved battery life when using Xcode Previews. (92179785)
- Changes to literal values in initializers are now correctly reflected in Xcode Previews. (92599456)
- The “Automatically Refresh Canvas” menu item in the Xcode Previews canvas has been changed to pause the new auto-building behavior. This allows manually refreshing the preview at the desirable cadence. (93261715)
- Fixed several issues with Xcode Previews not reflecting the expected code changes when navigating to non-SwiftUI files or when closing the canvas and re-opening. (93785410)
- Xcode Previews now supports watchOS complications inside of standalone watchOS apps. (95311509)
- Xcode Previews now works with packages containing resources that aren’t also contained in an app. (96828503)

###### Deprecations

- Support for previewing widgets created for macOS apps and apps built with Mac Catalyst has been removed. (92531529) : Use the macOS WidgetKit Simulator.

##### Project Navigator

###### Resolved Issues

- Fixed: When you use the File Inspector to change the type of a file, the file may be reopened in a different editor. (91784648)
- Fixed: The Issue Navigator doesn’t list issues generated when building Swift code in the emit module phase. (92430695)

###### Known Issues

- Option+Clicking the close button for an unselected editor tab closes all the other tabs (as expected) and also navigates to the clicked tab using optional navigation. This navigation is unintentional. (96958005)
- Opening result bundles with large build logs can take 30 seconds or more. (97328772)
- Option+Clicking an editor tab doesn’t perform “optional navigation” as configured in Xcode’s preferences. (97690500)

##### Refactoring

###### New Features

- Added a refactor action to add an explicit `Codable` implementation. (87904700)

###### Known Issues

- Convert to Regex Builder doesn’t correctly handle patterns with Unicode escape sequences. For example a regex literal containing `\u{0}` will be converted to `""` in the result. (95465206) (FB10343998)

##### Server

###### Known Issues

- Xcode Server is no longer supported. (73888675)

##### Signing and Distribution

###### New Features

- Automatic signing is now supported for development-signed DriverKit drivers. Distribution still requires approval from Apple and manual configuration of the additional capabilities on the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com/account). (81215709)
- The Game Center entitlement `com.apple.developer.game-center` is now available for apps on iOS, watchOS, and tvOS. If your app makes use of Game Center, it automatically receives this entitlement when you regenerate your provisioning profile.  If you use automatic signing, Xcode automatically generates a new provisioning profile for you. If you use manual signing, you need to [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com/account) and regenerate your provisioning profile. If you plan to continue using Game Center in your app, add the `com.apple.developer.game-center` entitlement to your entitlements file in Xcode. If not, remove the capability in Xcode and disable Game Center on your app ID in your [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com/account). (90667072)

###### Known Issues

- `xcodebuild -exportArchive` returns a session expired error message if you use authentication keys to upload your app to App Store Connect. (76036452) : Authentication keys are only supported for signing and provisioning. To upload apps from `xcodebuild`, first sign into Xcode with your Apple ID.
- `xcodebuild` invocations may occasionally crash in DVTPortalEntitlementsManager. (98678163) (FB11267326) : You can disable Xcode’s entitlements filtering logic to work around this, either by running `defaults write com.apple.dt.Xcode DVTEnableMultiPlatformEntitlementFiltering -bool NO` in Terminal or by adding `-DVTEnableMultiPlatformEntitlementFiltering=NO` to your `xcodebuild` command line invocation.

###### Resolved Issues

- Fixed: When editing the iCloud, App Groups, Apple Pay, or Wallet capability, Xcode may offer to select a team if you don’t choose a team. Selecting a team causes Xcode to crash. (93914533)

##### Simulator

###### New Features

- Simulator now supports remote notifications in iOS 16 when running in macOS 13 on Mac computers with Apple silicon or T2 processors. Simulator supports the Apple Push Notification Service Sandbox environment. Your server can send a remote notification to your app running in that simulator by connecting to the APNS Sandbox (api.sandbox.push.apple.com). Each simulator generates registration tokens unique to the combination of that simulator and the Mac hardware it’s running on. See [`User Notifications`](https://developer.apple.comhttps://developer.apple.com/documentation/usernotifications/) for more information. Remote Notifications support more features (like Notification Service Extensions) than locally simulated notifications using `.apns` payload files or the `simctl` push command. Device Registration Tokens are of variable length. Tokens in Simulator may be larger than current physical device tokens. Don’t hardcode any specific length or format for these tokens. (60974170)
- `simctl` now supports controlling simulated location, including running scenarios and interpolating between a list of waypoints. See `xcrun simctl location` for more information. (59422559) (FB7577924)
- Simulator now supports runtime disk images in addition to the existing runtime bundle format. Disk images are added to a system-managed storage location protected by System Integrity Protection and mounted at system-managed mount points. See `xcrun simctl` runtime for more information. (84169585)
- `simctl addmedia` has been updated to support many additional image formats (including many popular RAW formats). (87103990) (FB9832655)
- You can now boot simulator devices using universal runtimes as x86_64 on a Mac with Apple silicon by using the new `--arch` command-line argument to `simctl boot`. (88278366) (FB9860747)

###### Known Issues

- If you manually unmount or detach a simulator runtime disk image (such as by using `diskutil eject` or `umount`), Simulator and Xcode may not be able to determine whether the runtime is installed or not. Attempts to re-download the runtime results in failure with a duplicate runtime error. (89589210) : Restarting causes Simulator to re-mount the runtime disk image. Alternately you can use `xcrun simctl runtime` to locate the affected runtime disk image, delete it, then use Xcode to re-download it.
- Simulator runtime disk images in `/tmp` that you add using `xcrun simctl runtime add` are deleted. (93858264) : Place the simulator runtime disk image somewhere other than `/tmp/` before passing it into `xcrun simctl runtime add`.

##### Siri Intents

###### Known Issues

- Generated Swift code that the Intent definition compiler produces emits a warning when compiled: ```None
method 'handle(intent:)' with Objective-C selector 'handleIntent:completion:' conflicts with method 'handle(intent:completion:)' with the same Objective-C selector; this is an error in Swift 6
```

(91852710)

##### Source Control

###### Resolved Issues

- Various bugs impacting the accuracy and latency of git file status in the Project and Changes navigators have been resolved. Changes to files in the working copy are accurately reflected in the navigators and the commit sheet without significant delay. Additionally, files that display change bars when presented in an editor receive a modified status as soon as a change is made in memory that would cause it to have a modified status when persisted to disk. (49909533)
- Xcode now supports generating and using externally-generated ED25519 and ECDSA keys to perform `git` SSH operations. (85009643)

###### Known Issues

- Configuring a new application in Xcode Cloud will fail when a developer team has no existing apps in App Store Connect. (94199091) : Create the app in App Store Connect first, then onboard the product in Xcode.

##### Source Editor

###### New Features

- Xcode now pins elements of your code structure to the top of the editor as you scroll through a document. To toggle this behavior, use “Show: Code structure while scrolling” in Xcode’s Text Editing preferences. (10582250)
- Errors in Swift files now provide fix-its for adding missing imports. (21533417) (FB5562997)
- Wrapping code with an if statement now automatically reindents the block. (29215201)
- Initializers are now presented as global code completions in Swift. (60399329)
- The user interface for jumping to symbol definitions or callers now gives you a code sample from each location. (69467155)
- Code completion now collapses overloaded functions into one row. (81338102)
- Added syntax highlighting and editing support for Swift Regular Expressions. You can now convert regular expression literals to their regex builder equivalent using Editor > Refactoring > Convert to Regex Builder. When moving the insertion point inside a regular expression literal, the enclosing substructure of the regular expression is highlighted. (82540073)
- Xcode now provides a file template for opting into touch alternatives for your iOS app. You can use touch alternatives to interact with your app on a Mac with Apple silicon - for example, press and hold the Option key to use a trackpad as a virtual touch screen. To enable, select File > New File > iOS > Resource > Touch Alternatives, and configure the newly added `com.apple.uikit.inputalternatives.plist` file to choose the touch alternatives for your app. (84271952)
- Code completion in Swift now provides memberwise initializer snippets. (84348512)
- Code completion in Swift now provides snippets for `if case` statements. (84381718)
- You can now select any combination of default parameters in code completion by typing to match the parameter names. (84906871)
- Improved accuracy of code completion in Swift. (85090778)
- When editing code, the Edit > Duplicate menu item and its corresponding keyboard shortcut now duplicate the selected text — or the line that currently contains the insertion point, if no text is selected. (8614499) (FB5618491)
- Code completion in Swift now provides snippets for adding an explicit `Codable` implementation. (87904617)
- Xcode now localizes keyboard shortcuts for all international hardware keyboards for better accessibility. You can further customize this in Key Bindings settings. (88397421)
- Code completion in Swift now provides snippets for `map`, `filter`, and `contains`, based on variable names. (89717471)
- Code structure pinned to the top of the editor with Xcode 14’s new “Show: Code structure while scrolling” option now includes additional information for line-wrapped declarations. (93591165)

###### Resolved Issues

- Fixed: Code completion at function call sites in Swift now inserts missing arguments. (9293666)
- A number of performance improvements have been made for viewing and editing large files. The issues most often appeared in autogenerated source files and test files with large numbers of tests, and could be worse when showing the code folding ribbon. (57789416)
- Performance when using the Minimap in HTML files with very long lines has been improved. (58893150)
- Fixed an issue that caused degraded performance when typing in files with a large number of errors or warnings. (59084580)
- The Quick Help inspector now displays the descriptions of build settings in the build settings editor as rich text with clickable links. (60067884)
- Code completion no longer automatically imports modules. (78136559)
- Xcode now now prefers types that can be used as attributes when invoking code completion after `@`. (78239501)
- Fixed an issue that caused whitespace to appear after some folded regions of code. (78333320) (FB9114110)
- Fixed an issue where Source Editor erroneously inserted `*` when creating a new line after a block-style documentation comment. (79415983)
- Added a new user interface for jumping to symbol definitions or callers that focuses on the distinguishing information about each location. (81366453)
- Improved speed and correctness of code completion in complex expressions and SwiftUI. (83435550)
- Xcode prioritizes SwiftUI View types when you type inside SwiftUI view builders. (83846531)
- Fixed an issue where hovering over text in a Code Review editor might crash Xcode. (85239396)
- Fixed an issue where stale warnings or errors incorrectly underlined parts of the line they were attached to. (86225773)
- Dynamic code completion snippets related to `for` loops no longer suggest naming iterated-over elements identically to their container. (87167378)
- Folding a Swift file using the Fold Methods and Functions menu item or its associated keyboard shortcut now also folds computed properties and subscripts. (87692952) (FB9849362)
- Code completion in SwiftUI now provides snippets for `List` and `ForEach`. (87904499)
- Fixed an issue that could lead to degraded performance over time when editing long files with the Minimap enabled. (89916018)
- Fixed an issue where using Xcode 14’s new “Show: Code structure while scrolling” feature with a block cursor could lead to visual artifacts. (89973125)
- Swift actor declarations now appear in the Minimap alongside class and struct declarations. (90279950)
- Fixed an issue where code completion in Swift showed inaccessible symbols. (90404828)
- Fixed various issues where system symbols weren’t syntax highlighted in Swift files. (91654823)
- Code completion in Swift now better prioritizes popular system APIs. (91977150)
- Fixed an issue that could lead to crashes when jumping to a symbol definition in a GPU trace. (93434935)
- The syntax coloring of regex literals has been updated to support the latest swift evolution proposal [`SE-0354 Regex Literals`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0354-regex-literals.md). In particular it now correctly handles what looked like unclosed literals followed by a comment, literals used in `try` and `await` expressions, and does better disambiguation with prefix operators that contain a `/`. (93673226, 92355356, 94661164) (95146866)

###### Known Issues

- Convert to Regex Builder doesn’t correctly handle patterns using lookahead. For example, `/foo(?=bar)/` should produce `Lookahead("bar")` in the result, but only produces `"bar"`. (97208700)

##### Storekit

###### Resolved Issues

- Xcode now has the ability to sync in-app purchase products from App Store Connect into StoreKit configuration files for faster StoreKit testing in Xcode setup. There’s also an updated transaction manager with filtering and a transaction inspector. (83863948)
- Fixed an issue where calling the [`‘clearTransactions()’`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/3579476-cleartransactions) method on [`SKTestSession`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession) didn’t clear all transactions from the [`SKPaymentQueue`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skpaymentqueue) when testing apps using the original API for in-app purchase. (86696132) (FB9814502)
- Fixed: The transaction manager no longer shows an unfinished warning for transactions that it can’t finish when using StoreKit testing in Xcode. (89419046) (FB9927448)

###### Known Issues

- Using the following StoreKit properties and methods on apps with a minimum deployment target below iOS 16, macOS 13, watchOS 9, and tvOS 16 will cause the app to crash at launch when running on systems earlier than iOS 16, macOS 13, watchOS 9 and tvOS 16: - `priceFormatStyle` and `subscriptionPeriodFormatStyle` on `Product` values
- `environmentStringRepresentation` and `recentSubscriptionStartDate` on `Product.SubscriptionInfo.RenewalInfo` values
- `environmentStringRepresentation` on `Transaction` values
- `dateRange(referenceDate:)` and `formatted(_:referenceDate:)` on `Product.SubscriptionPeriod` values (99962885) (FB11516463) : For each target using a StoreKit API listed above, navigate to the “Build Phases” tab in the project editor with the target selected and add StoreKit.framework under “Link Binary With Libraries” if it isn’t already present. Set the “Status” column to “Optional.”

##### Swift 57

###### New Features

- The standard library has a new `Regex<Output>` type. This type represents an , allowing more fluent string processing operations. You can create a `Regex` by [`initialization from a string`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0355-regex-syntax-run-time-construction.md): ```swift
let pattern = "a[bc]+" // matches "a" followed by one or more instances
                       // of either "b" or "c"
let regex = try! Regex(pattern)
``` Or via a [`SE-0354 Regex Literals`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0354-regex-literals.md): ```None
let regex = #/a[bc]+/#
``` There are [`new string-processing algorithms`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0357-regex-string-processing-algorithms.md) that support `String`, `Regex`, and arbitrary `Collection` types. ([`SE-0350`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0350-regex-type-overview.md), 93923512)
- Xcode 14 enables Swift 5.7 “bare slash” syntax for the newly introduced regular expression literals. In some cases, existing code that uses `/` as an operator doesn’t compile as a result. You can disambiguate this by adding parentheses `(/)`. You can also disable support for this literal syntax by unchecking “Enable Bare Slash Regex Literals” (`SWIFT_ENABLE_BARE_SLASH_REGEX = NO`) in your project’s build settings. (93460568)
- String operations in version 5.7 of the Swift Standard Library implement improved validation for string indices, fixing a number of edge cases that previously resulted in spurious runtime errors. However, Swift now diagnoses attempts to use an out-of-bounds index more reliably, and this may expose previously undetected indexing bugs when you recompile code using Xcode 14. If you see new “String index is out of bounds” errors after rebuilding your code, then double check that you aren’t applying an old index to a mutated string value. In previous releases, such cases may have silently resulted in corrupt or nonsensical values, while in Swift 5.7 they now reliably trigger a runtime error. (89482809)
- Swift can now infer the type of placeholder types written in many top-level positions. The inferred type is now suggested in a fixit. ```swift
// error: type placeholder may not appear in function return type
func replaceMe() -> _ { // note: replace the placeholder with the inferred type ‘Array<Int>’
  [ 42 ]
}
```

(82837146)

- Xcode 13 provided a Swift build setting called “Optimize Object Lifetimes” that’s not available in Xcode 14. If your project already customized this build setting, it now becomes a user-defined setting. It has no effect and you can remove it. Xcode 14 now consistently optimizes object lifetimes. (91971848)
- Xcode 14 introduces a new feature for C interoperability: “SE-0324 Relax diagnostics for pointer arguments to C functions.” The relaxed diagnostics apply only to pointer-type arguments, not `inout` arguments. Now diagnostics are relaxed for `inout` arguments under the same conditions as pointer arguments. For example, this conversion from an `inout Int` argument to a C parameter of type `const char *` is now allowed: ```None
  // C declaration:
  // long read_long(const char *input);

  func test() -> Int {
    var x = 3
    return read_long(&x)
  }
``` Previously Swift diagnosed the `inout`-to-pointer conversion as an error: ```None
  error: cannot convert value of type 'UnsafePointer<Int>' to expected argument type
    'UnsafePointer<CChar>' (aka 'UnsafePointer<Int8>')
    return read_long(&x)
                     ^
  note: arguments to generic parameter 'Pointee' ('Int' and 'CChar' (aka 'Int8'))
  are expected to be equal
    return read_long(&x)
                     ^
```

(92583588)

- Swift now supports references to `optional` methods on a protocol metatype, as well as references that are dynamically looked up on the `AnyObject` metatype. These references always have the type of a function that accepts a single argument and returns an optional value of function type: ```swift
class Object {
  @objc func getTag() -> Int
}

@objc protocol P {
  @objc optional func didUpdateObject(withTag tag: Int)
}

let getTag: (AnyObject) -> (() -> Int)? = AnyObject.getTag

let didUpdateObject: (any P) -> ((Int) -> Void)? = P.didUpdateObject
```

(93653702)

- Loading data from raw memory represented by `UnsafeRawPointer`, `UnsafeRawBufferPointer`, and their mutable counterparts now supports unaligned accesses. This previously required a workaround involving an intermediate copy: ```swift
let result = unalignedData.withUnsafeBytes { buffer -> UInt32 in
  var storage = UInt32.zero
  withUnsafeMutableBytes(of: &storage) {
    $0.copyBytes(from: buffer.prefix(MemoryLayout<UInt32>.size))
  }
  return storage
}
``` Now: ```swift
let result = unalignedData.withUnsafeBytes { $0.loadUnaligned(as: UInt32.self) }
``` Additionally, the counterpart `storeBytes(of:toByteOffset:as:)` had its alignment restriction lifted, so that storing to arbitrary offsets of raw memory can now succeed.  ([`SE-0349`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0349-unaligned-loads-and-stores.md), 93654008)
- `UnsafeRawPointer` and `UnsafeMutableRawPointer` have new functionality for pointer arithmetic, adding functions to obtain a pointer advanced to the next or previous alignment boundary: ```None
```swift
extension UnsafeRawPointer {
  public func alignedUp<T>(for: T.type) -> UnsafeRawPointer
  public func alignedDown<T>(for: T.type) -> UnsafeRawPointer
  public func alignedUp(toMultipleOf alignment: Int) -> UnsafeRawPointer
  public func alignedDown(toMultipleOf alignment: Int) -> UnsafeRawPointer
}
```
``` You can now use a pointer to `struct` to obtain a pointer to one of its stored properties: ```None
```swift
withUnsafeMutablePointer(to: &myStruct) {
  let interiorPointer = $0.pointer(to: \.myProperty)!
  return myCFunction(interiorPointer)
}
```
``` Swift has simplified comparisons between pointers. Since pointers are representations of memory locations within a single pool of underlying memory, Swift now allows comparing pointers without requiring type conversions with the `==`, `!=`, `<`,`<=`,`>`, and `>=` operators. ([`SE-0334`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0334-pointer-usability-improvements.md), 93667321)
- You can now use the `withMemoryRebound<T>()` method on raw memory, including `UnsafeRawPointer`, `UnsafeRawBufferPointer`, and their mutable counterparts. Additionally, Swift has clarified the semantics of `withMemoryRebound<T>()` when used on typed memory (`UnsafePointer<Pointee>`, `UnsafeBufferPointer<Pointee>` and their mutable counterparts). Whereas Swift previously required `Pointee` and `T` to have the same stride, you can now rebind in cases where `Pointee` is an aggregate of `T` or vice versa. For example, given an `UnsafeMutableBufferPointer<CGPoint>`, you can now use `withMemoryRebound` to operate temporarily on a `UnsafeMutableBufferPointer<CGFloat>`, because `CGPoint` is an aggregate of `CGFloat`. ([`SE-0333`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0333-with-memory-rebound.md), 93668889)
- You can now call a generic function with a value of protocol type in places that previously failed because `any` types don’t conform to their protocols. For example: ```swift
protocol P {
  associatedtype A
  func getA() -> A
}

func takeP<T: P>(_ value: T) { }

func test(p: any P) {
  takeP(p) // was an error "type 'any P' cannot conform to 'P'", now accepted
}
``` This operates by opening the value of the protocol type and passing the underlying type directly to the generic function. ([`SE-0352`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0352-implicit-open-existentials.md), 93669112)
- You can now use a default value expression with a generic parameter type to default the argument and its type: ```swift
func compute<C: Collection>(_ values: C = [0, 1, 2]) {
  ...
}
``` The compiler now accepts a call to `compute()` and `[Int]` is inferred for `C` at call sites that don’t provide the argument explicitly. ([`SE-0347`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0347-type-inference-from-default-exprs.md), 93669409)
- You can now use protocols with associated types and `Self` requirements as the types of values with the `any` keyword. You can call protocol methods that return associated types on an `any` type; the result is type-erased to the associated type’s upper bound, which is another `any` type with the same constraints as the associated type. For example: ```swift
protocol Surface {...}
  
protocol Solid {
  associatedtype SurfaceType: Surface
  func boundary() -> SurfaceType
}
  
let solid: any Solid = ...
  
// Type of 'boundary' is 'any Surface'
let boundary = solid.boundary()
``` You can’t use protocol methods that take an associated type or `Self` with `any`; however, in conjunction with [`SE-0352`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0352-implicit-open-existentials.md), you can pass the `any` type to a function that takes a generic parameter constrained to the protocol. Within the generic context, type relationships are explicit, and you can use all protocol methods. ([`SE-0309`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0309-unlock-existential-types-for-all-protocols.md), 93928911)
- Protocols can now declare a list of one or more , which enable writing same-type requirements on those associated types using angle bracket syntax: ```swift
protocol Graph<Vertex, Edge> {
  associatedtype Vertex
  associatedtype Edge
}
``` You can now write a protocol name followed by type arguments in angle brackets, like `Graph<Int, String>`, anywhere that a protocol conformance requirement may appear: ```swift
  func shortestPath<V, E>(_: some Graph<V, E>, from: V, to: V) -> [E]

  extension Graph<Int, String> {...}

  func build() -> some Graph<Int, String> {}
``` A protocol name followed by angle brackets is shorthand for a conformance requirement, together with a same-type requirement for the protocol’s primary associated types. The first two examples above are equivalent to the following: ```swift
  func shortestPath<V, E, G>(_: G, from: V, to: V) -> [E]
    where G: Graph, G.Vertex == V, G.Edge == E

  extension Graph where Vertex == Int, Edge == String {...}
``` The `build()` function returning `some Graph<Int, String>` can’t be written using a `where` clause; this is an example of a constrained opaque result type, which is new expressivity in Swift 5.7. ([`SE-0346`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0346-light-weight-same-type-syntax.md), 93929372)
- You can use protocols that adopt primary associated types with the `any` keyword to enable constrained existential types. For example: ```None
let strings: any Collection<String> = [ "Hello" ]
``` This makes writing type-erasing wrappers for generic code much simpler because a separate wrapper type is no longer required: ```None
protocol Producer<T> {
  associatedtype T
  func produce() -> T
}

typealias AnyProducer<T> = any Producer<T>

/*
struct AnyProducer<T> {
  var wrappedProduce: () -> T
}
*/
```

(92044231)

- You can now use protocols with primary associated types in existential types, enabling same-type constraints on those associated types. ```swift
let strings: any Collection<String> = [ "Hello" ]
``` Note that language features requiring runtime support like dynamic casts (`is`, `as?`, `as!`), as well as generic usages of parameterized existentials in generic types (e.g. `Array<any Collection<Int>>`) involve additional availability checks to use. You can now back-deploy usages in generic positions with a generic type-erasing wrapper struct, which is now much simpler to implement: ```swift
struct AnyCollection<T> {
  var wrapped: any Collection<T>
}

let arrayOfCollections: [AnyCollection<T>] = [ /**/ ]
``` ([`SE-0353`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0353-constrained-existential-types.md), 93929537)
- You can now use opaque types in the parameters of functions and subscripts when they provide a shorthand syntax for the introduction of a generic parameter. For example, the following: ```swift
func horizontal(_ v1: some View, _ v2: some View) -> some View {
  HStack {
    v1
    v2
  }
}
``` is equivalent to: ```swift
func horizontal<V1: View, V2: View>(_ v1: V1, _ v2: V2) -> some View {
  HStack {
    v1
    v2
  }
}
``` With this, `some` in a parameter type provides a generalization where the caller chooses the parameter’s type as well as its value, whereas `some` in the result type provides a generalization where the caller chooses the resulting type and value. ([`SE-0341`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0341-opaque-parameters.md), 93675336)
- You can now infer parameter and result types from the body of a multistatement closure. There’s no longer a distinction between single- and multi-statement closures. Use of closures becomes less cumbersome by removing the need to constantly specify explicit closure types, which can sometimes be fairly large (e.g., when there are multiple parameters or a complex tuple result type). For example: ```swift
func map<T>(fn: (Int) -> T) -> T {
  return fn(42)
}

func computeResult<U: BinaryInteger>(_: U) -> U { /* processing */ }

let _ = map {
  if let $0 < 0 {
     // Do some processing.
  }

  return computeResult($0)
}
``` You can now infer the result type of `map` from the body of the trailing closure passed as an argument. ([`SE-0326`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0326-extending-multi-statement-closure-inference.md), 93669647)
- You can now unwrap optional variables with a shorthand syntax that shadows the existing declaration. For example, the following: ```swift
let foo: String? = "hello world"

if let foo {
  print(foo) // Prints "hello world”.
}
``` is equivalent to: ```swift
let foo: String? = "hello world"

if let foo = foo {
  print(foo) // Prints "hello world”.
}
```

([`SE-0345`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0345-if-let-shorthand.md), 93673835)

- You can now make declarations unavailable from use in asynchronous contexts with the `@available(*, noasync)` attribute. This protects the consumers of an API against undefined behavior that can occur when the API uses or encourages using thread-local storage across suspension points. It also protects developers against holding locks across suspension points, which may lead to undefined behavior, priority inversions, or deadlocks. ([`SE-0340`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0340-swift-noasync.md), 93673989)
- Top-level scripts now support asynchronous calls. Using an `await` by calling an asynchronous function or accessing an isolated variable transitions the top level to an asynchronous context. As an asynchronous context, top-level variables are `@MainActor`-isolated and the top level is run on the `@MainActor`. Note that the transition affects function overload resolution and starts an implicit run loop to drive the concurrency machinery. Unmodified scripts aren’t affected by this change unless `-warn-concurrency` is passed to the compiler invocation. With `-warn-concurrency`, variables in the top level are isolated to the main actor, and the top-level context is isolated to the main actor but isn’t an asynchronous context. ([`SE-0343`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0343-top-level-concurrency.md), 93674157)
- Swift now natively supports distributed programming with the introduction of distributed actors. For more information, see [`SE-0336`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0336-distributed-actor-isolation.md), [`SE-0344`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0344-distributed-actor-runtime.md). (70840120)
- You can now declare `distributed actor` and `distributed func` inside of a `distributed actor`. Distributed actors provide stronger isolation guarantees than “local” actors, and they enable additional checks to be made on return types and parameters of distributed methods, for example, checking if they conform to `Codable`. You can call distributed methods on “remote” references of distributed actors, turning those invocations into remote procedure calls, by means of pluggable and user-extensible distributed actor-system implementations. Swift doesn’t provide any specific distributed actor system by itself; however, packages in the ecosystem fulfill the role of providing those implementations. ```swift
distributed actor Greeter { 
  var greetingsSent = 0
  
  distributed func greet(name: String) -> String {
    greetingsSent += 1
    return "Hello, \(name)!"
  }
}

func talkTo(greeter: Greeter) async throws {
  // The isolation of distributed actors is stronger. You can't refer to
  // any stored properties of distributed actors from outside of them.
  greeter.greetingsSent // You can't access the distributed actor-isolated property 'name' from a non-isolated context.
  
  // Remote calls are implicitly throwing and async, 
  // to account for the potential networking involved.
  let greeting = try await greeter.greet(name: "Alice")
  print(greeting) // Hello, Alice!
}
```

([`SE-0336`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0336-distributed-actor-isolation.md), 93674913)

- The deinitializer, most initializers for `actor` types, and types constrained by a global actor like the `@MainActor` have revised rules about what expressions are permitted in their body. As part of SE-327, the goal of these revisions is to improve language expressiveness and safety. Many more programming patterns are now permitted in these initializers. For example, a non-async initializer of an `actor` prior to Swift 5.7 raised a diagnostic any time `self` escaped the initializer before returning. That diagnostic’s purpose was to protect against a possible data race when accessing isolated stored properties, but it was emitted even if there was no dangerous racy access. In Swift 5.7, the compiler now checks these initializers for dangerous access to isolated stored properties that occur after an escape of `self`: ```swift
actor Database {
  // ... other properties ...
  var rows: Int = 0

  init(_ world: DataUser) {
    defer { 
      print("last = \(self.rows)") // ❌ This access to 'rows' is illegal.
    }
    
    print("before = \(self.rows)") // ✅ This access to 'rows' is OK.
    world.publishDatabase(self)    // ✅ Passing 'self' is OK in Swift 5.7+.
    print("after = \(self.rows)")  // ❌ This access to 'rows' is illegal. 
    
    Task { [weak self] in          // ✅ Capturing 'self' is OK in Swift 5.7+.
      while let db = self { await db.prune() }
    }
  }
}
``` This is a control-flow sensitive check, meaning an illegal access doesn’t necessarily appear on a source line after an escape of `self` (in the example above, consider  the `defer` is executed). The compiler always points out one of the escapes of `self` that’s causing an access to become illegal. In addition, delegating initializers of an actor are no longer always non-isolated. This means an `async` delegating initializer can do the same things as a non-delegating one. (84476555)
- Actor initializers no longer require writing the `convenience` keyword to delegate (SE-327). Prior to Swift 5.7, adding or removing `convenience` for a public `init` of an actor was a non-resilient change, with respect to libraries compiled with evolution enabled. Those libraries compiled for Swift 5.7+ are now resilient to changes in the implementation of such initializers to delegate or not, and existing programs compiled for Swift 5.7+ won’t require recompilation. (87567878)
- New types representing time and clocks are now available. This includes a protocol `Clock` for defining clocks, which allows you to define a concept of “now” and a way to wake up after a given instant. A new protocol `InstantProtocol` for defining instants in time is also available. And a new protocol `DurationProtocol` for defining an elapsed duration between two given `InstantProtocol` types is also available. The `Clock` types for general use are most commonly `SuspendingClock` and `ContinuousClock`, which represent the most fundamental clocks for the system. The `SuspendingClock` type doesn’t progress while the machine is suspended, whereas the `ContinuousClock` progresses no matter the state of the machine. ```swift
func delayedHello() async throws {
  try await Task.sleep(until: .now + .milliseconds(123), clock: .continuous)
  print("hello delayed world")
}
``` `Clock` also has methods to measure the elapsed duration of the execution of work. In the case of the `SuspendingClock` and `ContinuousClock` this measures with high resolution and is suitable for benchmarks. ```swift
let clock = ContinuousClock()
let elapsed = clock.measure {
  someLongRunningWork()
}
``` ([`SE-0329`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0329-clock-instant-duration.md), 93928740)
- The compiler now emits a warning when a non-final class conforms to a protocol that imposes a same-type requirement between `Self` and an associated type. This kind of requirement makes the conformance unsound for subclasses. For example, Swift 5.6 allows the following code, which at runtime would construct an instance of `C` and not `SubC` as expected: ```swift
protocol P {
  associatedtype A : Q where Self == Self.A.B
}

protocol Q {
  associatedtype B

  static func getB() -> B
}

class C : P {
  typealias A = D
}

class D : Q {
  typealias B = C

  static func getB() -> C { return C() }
}

extension P {
  static func getAB() -> Self {
    // This is well-typed because `Self.A.getB()` returns
    // `Self.A.B`, which is equivalent to `Self`.
    return Self.A.getB()
  }
}

class SubC : C {}

// P.getAB() declares a return type of `Self`, so it should
// return `SubC`, but it actually returns a `C`.
print(SubC.getAB())
``` To make the above example correct, either the class `C` needs to become `final` (in which case `SubC` can’t be declared) or protocol `P` needs to be redesigned to not include the same-type requirement `Self == Self.A.B`. (93675134)
- The compiler now correctly emits warnings for more expressions where a protocol conformance is used and may be unavailable at runtime. Previously, member-reference expressions and type-erasing expressions that use potentially unavailable conformances weren’t diagnosed, leading to potential crashes at runtime. ```swift
struct Pancake {}
protocol Food {}

extension Food {
  var isGlutenFree: Bool { false }
}

@available(macOS 12.0, *)
extension Pancake: Food {}

@available(macOS 11.0, *)
func eatPancake(_ pancake: Pancake) {
  if (pancake.isGlutenFree) { // Warning: Conformance of 'Pancake' to 'Food' is only available in macOS 12.0 or newer.
    eatFood(pancake) // Warning: Conformance of 'Pancake' to 'Food' is only available in macOS 12.0 or newer.
  }
}

func eatFood(_ food: Food) {}
```

(93675504)

- Opaque types (expressed with `some`) can now be used in structural positions within a result type, including having multiple opaque types in the same result. For example: ```swift
func getSomeDictionary() -> [some Hashable: some Codable] {
  return [ 1: "One", 2: "Two" ]
}
``` ([`SE-0328`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0328-structural-opaque-result-types.md), 93675646)
- Various protocols in the standard library now declare primary associated types, for example `Sequence` and `Collection` declare a single primary associated type `Element`. For example, this allows writing down the types `some Collection<Int>` and `any Collection<Int>`. ([`SE-0358`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0358-primary-associated-types-in-stdlib.md), 93929895)

###### Resolved Issues

- Stored properties in Swift can’t have type information that is potentially unavailable at runtime. However, prior to Swift 5.7 the compiler incorrectly accepted `@available` attributes on stored properties when the property had either the `lazy` modifier or an attached property wrapper. This could lead to crashes for apps running on older operating systems. The Swift compiler now consistently rejects `@available` on all stored properties. (82713248) (FB9594187)
- The async version of the `addTeardownBlock` method in `XCTestCase` is now available. (85453819) (FB9762503)
- The diagnostic about non-isolated default-value expressions introduced for Swift 5.6 in the Xcode 13.3 release is no longer available. The proposed rule in [`SE-0327`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0327-actor-initializers.md) wasn’t precise enough to avoid flagging an innocuous yet common pattern in SwiftUI code involving `@StateObject` properties and `@MainActor`. (88971160)
- The “Generate Memberwise Initializer” refactoring correctly adds parameters for variables that are marked with a property wrapper. (89057767) (FB9910083)
- String operations in version 5.7 of the Swift Standard Library implement improved validation for string indices, fixing a number of edge cases that previously resulted in spurious runtime errors. However, Swift now diagnoses attempts to use an out-of-bounds index more reliably, and this may expose previously undetected indexing bugs when you recompile code using Xcode 14. If you see new “String index is out of bounds” errors after rebuilding your code, then double check that you aren’t applying an old index to a mutated string value. In previous releases, such cases may have silently resulted in corrupt or nonsensical values, while in Swift 5.7 they now reliably trigger a runtime error. (89482809)
- When constructing String instances from C strings, Swift now strictly enforces the input buffer’s null termination if you pass an argument by pointer conversion. Furthermore, `inout`-to-pointer conversion is now deprecated for String construction. The affected functions are `String.init(cString:)`, `String.init?(validatingUTF8:)`, `String.decodeCString(_:as:repairingInvalidCodeUnits:)`, and `String.init(decodingCString:as:)`. (90336023)
- Edit all in Scope correctly renames all occurrences of variables captured using the shorthand closure capture syntax `[capturedVariable]` or the shorthand `if let optionalVariable` syntax. (91311033)
- You can use protocols that adopt primary associated types with the `any` keyword to enable constrained existential types. For example: ```None
let strings: any Collection<String> = [ "Hello" ]
``` This makes writing type-erasing wrappers for generic code much simpler because a separate wrapper type is no longer required: ```None
protocol Producer<T> {
  associatedtype T
  func produce() -> T
}

typealias AnyProducer<T> = any Producer<T>

/*
struct AnyProducer<T> {
  var wrappedProduce: () -> T
}
*/
```

(92044231)

- The Swift compiler no longer warns about redundant requirements in generic declarations. For example, in beta 1 the following code diagnosed a warning about the `T.Iterator : IteratorProtocol` requirement being redundant, because it is implied by `T : Sequence`: ```swift
func firstElement<T: Sequence>(_: T) -> T.Element where T.Iterator: IteratorProtocol {...}
``` A redundant requirement doesn’t indicate a coding error, and sometimes it is desirable to spell them out for documentation purposes. For this reason these warnings are now disabled by default. You can get the previous behavior and re-enable these warnings by setting the `OTHER_SWIFT_FLAGS` build option in Xcode to “`-Xfrontend -warn-redundant-requirements`”. (92092635)
- Dynamic casts (`is`, `as!`, `as?`) to and from parameterized existential types now correctly check the constraints on these types. (92197049)
- Fixed: Certain complex `switch` statements in multi-statement closures may cause the compiler to crash if they contain a `fallthrough` statement that requires type inference at its destination, for example, a destination `case` that uses pattern matching with `let` bindings such as `case (let ..., let ...)`. (93796211)
- Swift doesn’t perform Sendable checking when exiting an actor to call into non-isolated, async code.  For example: ```swift
func f(_: NS) async { }

actor A {
  func g(_ ns: NS) async {
    await f(ns) // Warn about passing non-Sendable type 'NS' to a non-isolated async function.
  }
}
```

(93930900)

###### Known Issues

- `#if canImport(AudioVideoBridging)` doesn’t compile on Mac Catalyst. (89289575) : Use `#if os(macOS)` to restrict `AudioVideoBridging` code to supported platforms.
- `~=` and cases in switches succeed if the entire string matches, rather than if there’s a match inside the string. This may change depending on the result of Swift Evolution for [`new string-processing algorithms`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0357-regex-string-processing-algorithms.md). (93918632)
- In Swift, some Foundation typealiases for function types (such as `NSItemProvider.CompletionHandler`) will see `@Sendable` function types, which may result in unexpected warnings in code that has not adopted Swift Concurrency. To eliminate the warnings, replace a reference to the typealias in Swift source code with its underlying type without the `@Sendable`. (98343624) For example, replace: ```None
var completion: NSItemProvider.CompletionHandler
``` with ```None
var completion: (NSSecureCoding?, Error?) -> Void
```

##### Swift Packages

###### New Features

- Modules that collide due to having the same name can now be disambiguated by aliasing. The package manifest introduces a new parameter ‘moduleAliases’; it allows a user to define unique names for the conflicting modules and builds them under the new names without requiring any source code changes. Below is an example of using the `moduleAliases` parameter: ```None
  targets: [
  .executableTarget(
    name: "App",
    dependencies: [
     .product(name: "Game",
              package: "swift-game",
              moduleAliases: ["Utils": "GameUtils"]),
     .product(name: "Utils",
              package: "swift-draw"),
   ])
 ]
``` The `Utils` module from `swift-game` (or its dependency package) is aliased as `GameUtils` (user-provided value) to be disambiguated from `Utils` from `swift-draw`. If `App` wants to use the `Utils` from `swift-game`, it needs to directly reference the new name, for example, `import GameUtils`. The `Utils` module being aliased needs to be a pure Swift module and not a prebuilt binary. (82458975)
- You can now use Swift Package command plugins in Xcode, by using the File > Packages menu or the contextual menu in Xcode’s file navigator. Any command plugins provided by a package’s dependencies are available. You can choose which targets of the package to apply the command to, and you can pass custom arguments to the plugin. The Report Navigator shows the results of running the command. If the command indicates that it needs to write to the package’s source files, Xcode asks for permission and lets you inspect the source code of the plugin before running it. (87988220)
- Xcode 14’s new XcodeProjectPlugin API extends Swift Package Manager’s PackagePlugin API, and provides a simplified description of the structure of an Xcode project. Plugins using this new API can be used with projects and packages. Plugins using only the PackagePlugin API can only be used with packages. (88196725)
- Build tool plugins can now use the `XcodeBuildToolPlugin` protocol in the `XcodeProjectPlugin` module to generate sources and resources for Xcode targets.  The Xcode target editor lets a target be configured to use a build tool plugin provided by any of the project’s package dependencies. (92415898)

###### Resolved Issues

- Fixed: Long-running Swift Package plugins can’t be cancelled. (75740831)
- Remote packages are updated during package resolution when using xcodebuild, even if `-onlyUsePackageVersionsFromResolvedFile` is being passed (the default on Xcode Cloud). This resolves an issue where the package resolved file references commits that are newer than existing local working copies. (82163698) (FB9539493)
- When a package is selected in Xcode’s file navigator, the inspector now lists any command plugins and build tool plugins that are defined in the package and lets you navigate to the plugin’s source code. (88249626)
- Fixed: The new `xcodebuild` option `-skipPackageUpdates` skips updating any remote packages during package resolution. (89163856)
- If a plugin generates a non-source file as one of its outputs, it’s automatically treated as a resource to process. This rule is only applied to targets in packages with a tools version of at least 5.7. (89693335)
- Dependencies of package plugins always build for the host, regardless of what platform the client of the package the plugin is being applied to is building for. (91438186)
- Fixed: Xcode may emit the warning “Usage of …/Library/org.swift.swiftpm/registries.json has been deprecated” many times for the same workspace. (92806533)
- Fixed: In some cases when a package resolution error is resolved, the issue remains showing in the Issue Navigator. (92886176)
- Fixed an issue where build description creation was slow for builds with very large SwiftPM package dependency graphs. (93041521) (FB10014448)

###### Known Issues

- On rare occasions, Xcode shows a package resolution error when a project that has package dependencies is opened for the first time. (75025949) (FB9028752)

:  Close the project and open it again.

- Xcode Previews can fail when previewing inside of a dynamic package that depends on other dynamic packages. (88826023) (FB9898927) : If possible, change the dependent packages to build statically.
- If a package target has no source files but uses a build tool plugin that generates source files, an error occurs at build time. (92858144)

:  Add an empty source file to the target that uses the build tool plugin.

- Source files generated by Swift Package Build Tool Plugins are generated when the plugin runs, so Xcode cannot index their contents before the first build.  Therefore Xcode may show Live Issues indicating missing symbols for source code that references the generated code. (95239175)

:  Build the project. Xcode will index the generated source files once they have been generated.

##### Templates

###### Resolved Issues

- The Cocoa AppleScript application template has been removed in Xcode 14. (20633478)

##### Testing

###### New Features

- `XCTAssertThrows()` and related macros now provide richer diagnostic information when they catch thrown exceptions other than `NSException` (including C++ exceptions.) (15363879)
- XCTest includes a new Swift-only expectation type, `XCTKeyPathExpectation`, that you can use instead of `XCTKVOExpectation` for observing changes to Swift keypaths. (38074735) (FB5724526)
- Test targets that have parallelization enabled in the active scheme or test plan now execute in parallel with respect to each other. Previously, each target executed serially, and the test classes within each target executed in parallel. Now, Xcode executes both the targets and the classes within them in parallel, preferring to fan out across targets first. For suites with a larger number of targets, this may result in a substantial speedup (results vary depending on hardware and suite composition). Test targets that don’t have parallelization enabled continue to execute in isolation with respect to other targets. (46048340)
- It is now possible to view coverage highlights and execution counts for source files that are represented in a result bundle’s coverage report. To do so, follow these steps: 1. Open the result bundle in Xcode.
2. In the Report Navigator, right-click the entry with the result bundle’s name, and select “Open in Workspace.”
3. Choose the project or workspace that the result bundle was ultimately derived from (even if the result bundle was produced from a copy of the workspace or project at a different filesystem location or on a different machine).
4. After the result bundle has been re-opened in the workspace, select a source file whose coverage data you want to view in the coverage report.
5. Open the Assistant Editor (Editor > Assistant) and make sure that “Referenced Files” is selected in the jump bar. The execution counts will be visible in the coverage ribbon next to the source code. Note that if the source file on-disk differs from the version at compile-time, the coverage information displayed may no longer be accurate. (53989182)
- Diagnostic screenshots for macOS now show the mouse cursor. (59296710)
- XCTest captures a sysdiagnose once testing has finished and an error or failure is encountered. This behavior is controllable from a Test Plan or the `xcodebuild` command line interface. (87787968)
- There is a new XCTest API `XCUIDevice.current.press(.action)` for the new Apple Watch Action button. (93394912)

###### Resolved Issues

- XCTest now generates result bundles when testing fails to begin. (56313666)
- A duplicate but empty entry for a Swift package target should no longer appear in the code coverage report. Additionally, if a Swift package target is selected for code coverage via the “Some Targets” UI in the scheme or test plan editor, the package target is now included in the generated report. (63983853) (FB7724987)
- Fixed: If an Objective-C or C++ exception is thrown from any of the XCTest `setUp` methods, then all subsequent `setUp` methods are still invoked. This matches how exceptions thrown from `tearDown` methods or Swift errors thrown from either `setUp` or `tearDown` methods are handled. (74408809)
- The test report includes a new context menu action for extracting sysdiagnoses and log archives. (90395050)
- The `XCTestExpectation` class and its descendants now conform to `Sendable` in Swift. (90927894)
- When creating a new project with tests, test bundles will enable parallel test execution by default. (91776591)

## See Also

- [Xcode 14.3.1 Release Notes](xcode-14_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14.3 Release Notes](xcode-14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14.2 Release Notes](xcode-14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14.1 Release Notes](xcode-14_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14.0.1 Release Notes](xcode-14_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)*