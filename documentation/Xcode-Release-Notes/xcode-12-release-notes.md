# Xcode 12 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 12 includes SDKs for iOS 14, iPadOS 14, tvOS 14, watchOS 7, and macOS Catalina 10.15.6. The Xcode 12 release supports on-device debugging for iOS 9 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 12 requires an Intel-based Mac running macOS Catalina 10.15.4 or later.

##### General

###### New Features

- Documents can now be opened in their own tab, making it easy to quickly switch between files while maintaining the rest of Xcode’s configuration. Option-click or double-click to open a document in a tab. The tab bar appears when you have more than one document open, or you choose View > Always Show Tab Bar. (7954451)
- Xcode now supports previewing widgets, App Clips, and content in Swift packages. For more seamless live previewing on device, Xcode installs the new Xcode Previews app for iOS 14 and iPadOS 14. (56388008)
- The new [`LibraryContentProvider`](https://developer.apple.com/documentation/DeveloperToolsSupport/LibraryContentProvider) protocol gives you the ability to show your views and modifiers in Xcode’s library. (56423420)
- Code completions have a new, focused user interface, making it easier to find a completion. Completions are also more accurate and up to 15 times faster in Xcode 12. (56087948, 58010475)

###### Resolved

- Compilable code completions for SwiftUI APIs now correctly handle overloaded methods. (64037686)
- Fixed an issue in Xcode 12 build 12A7208 which could cause build failures for iOS or tvOS apps using [`StoreKit`](https://developer.apple.com/documentation/StoreKit) or [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices) with SwiftUI, when targeting simulated devices or using SwiftUI Previews. (68252534)

##### Apple Clang Compiler

###### New Features

- Clang now warns about incorrect format strings that are specified in an [`NSLocalizedString`](https://developer.apple.com/documentation/Foundation/NSLocalizedString) macro. (23622446) (FB5412403)
- The `std::is_scalar` trait is now true for Block types. This allows using blocks in new places like `std::optional`. (57892832)

###### Resolved

- `@dynamic` on a property is ignored if the property is redeclared in a protocol that inherits from another protocol. (45503561)
- Clang now reports an error when you use a function without an explicit declaration when building C or Objective-C code for macOS (`-Werror=implicit-function-declaration` flag is on). This additional error detection unifies Clang’s behavior for iOS/tvOS and macOS 64-bit targets for this diagnostic. (49917738)
- Fixed type checking for block parameters using `id` with protocols. The compiler now emits an error for method calls with a block that uses parameters more specific than the arguments with which it will be called. (57980961)

###### Deprecations

- The stand-alone system assemblers for i386, x86_64, and arm are deprecated. Using the `as` command with the `-Q` flag shows a warning that instructs you to transition to Clang’s integrated assembler and the `-q` flag. The `as(1)` driver will remain, as a standard way to invoke Clang’s integrated assembler, as well as any assemblers installed by the developer. (61299833)

##### Asset Catalogs

###### New Features

- Added support for Scalable Vector Graphic (SVG) image assets. These preserve their vector representation with deployment targets of macOS 10.15 or later, iOS 13 or later, and iPadOS 13 or later. (18389814)
- The required pixel size is now shown for complication placeholder images. (21135944)
- Adding a new color now includes a Dark Appearance variant by default. If you leave this empty, Xcode will use the Any Appearance color value for both Light Appearance and Dark Appearance. You can use the asset’s Attribute inspector to hide the unused variant. (55720623)
- The “Mac Catalyst” asset variant is now named “Mac Scaled”. Xcode will use this asset in targets that build with Mac Catalyst when “Scale Interface to Match iPad” is selected (including on macOS 10.15). When “Optimize Interface for Mac” is selected, Xcode will prefer the Mac asset variant. (58883008)
- The “New Asset” menu now organizes asset types by platform. (59233882)

###### Resolved

- Resolved an issue where hidden folders inside an Asset Catalog could cause Xcode to repeatedly reload the catalog. (35275782) (FB5390092)
- Xcode normalizes Asset Catalog `Contents.json` files when modifying them, for better stability and compatibility with future edits. A normalized file contains keys in alphabetical order and a newline character at the end of the file. (53886564)

##### Build System

###### New Features

- You can now use `momc` on the command line to generate Core Data code from your models. (58713955) For a list of available arguments, run: ```shell
xcrun momc
```
- XCFrameworks can now include `.dSYM` and `.bcsymbolmap` debugging symbol files in your library bundle with the `-debug-symbols` flag. Run the command `xcodebuild -create-xcframework -help` for additional usage information. (64910707)

###### Resolved

- Fixed a bug where a regenerated dSYM file isn’t copied with the product in an incremental build if `DWARF_DSYM_FILE_SHOULD_ACCOMPANY_PRODUCT` is enabled. (44696736)
- Restored support for `PRODUCT_DEFINITION_PLIST` in the new build system. (45800765) (FB5711777)
- Fixed a race condition where multiple targets using the same XCFramework could result in non-deterministic build failures. (53911952) (FB6878988)
- When using `USE_RECURSIVE_SCRIPT_INPUTS_IN_SCRIPT_PHASES` with `XCFileLists`, the items within are now properly treated as recursive inputs. (54635196) (FB7109342)
- Fixed a bug that could cause tagged On-Demand Resources to be included in both an asset pack and the product. These resources are now only included in the asset pack. (59008757)
- Input files for Run Script Phases are now tracked as inputs to code-signing tasks, allowing modifications to those files to properly trigger code signing on incremental builds. (59353913)
- Fixed an issue that caused [`LSMinimumSystemVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/LSMinimumSystemVersion) in a macOS application’s `Info.plist` and [`MinimumOSVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/MinimumOSVersion) on other platforms to be set to an earlier value than the deployment target of the build target. (62617478) (FB7681463)

###### Known Issues

- A newly-created iOS project using the Swift language may no longer build after enabling Mac Catalyst. (67885114) : Replace the  `@main` annotation on the App Delegate with `@UIApplicationMain`.

###### Deprecations

- The Build Settings editor no longer includes the Valid Architectures build setting (`VALID_ARCHS`), and its use is discouraged. Instead, there is a new Excluded Architectures build setting (`EXCLUDED_ARCHS`). If a project includes `VALID_ARCHS`, the setting is displayed in the User-Defined section of the Build Settings editor. (15145028)
- The legacy build system is deprecated, and will be removed in a future release. (62742902)

##### Core Data

###### Resolved

- When you create a multi-platform app project with Core Data, Xcode now correctly uses the name of the project for its data model. (67534882) (FB8483330)

##### Core Ml

###### Known Issues

- The Core ML editor’s Preview tab for sound classifier models doesn’t show a classification result when you click on ‘Listen’. In addition, when you add an audio file, clicking the Play button doesn’t update the audio timeline as the audio plays. This issue also occurs in the Create ML app. (67515312)

###### Deprecations

- The default initializer on an auto-generated model interface in Xcode is deprecated in favor of `init(configuration:)`. Use `init(configuration:)` or the newly introduced `.load()` method on the auto generated model interface instead, and handle model-load errors appropriately. (62875309)

##### Debugging

###### New Features

- When a process pauses at a breakpoint, Xcode displays the hit count for that particular breakpoint location as part of the breakpoint’s annotation in the editor. An example is “Breakpoint 2.1 (7)”, where the “(7)” represents 7 hits at location 2.1. (3836838)
- When a process crashes under the debugger, Xcode prints the crash messages in the Console. These messages are similar to the ones displayed in CrashReporter. (8931901)
- Reorder breakpoint actions by dragging and dropping them into a different position in the Breakpoint Editor. (9777468)
- The new Enable Breakpoint at Current Line and Disable Breakpoint at Current Line menu item lets you toggle an existing breakpoint in your code. In addition, you can bind a keyboard shortcut to that menu item to toggle the breakpoint quickly. (17924697)
- You can now name a breakpoint, and reference it by name from another breakpoint’s action. For example, to enable a previously disabled breakpoint called “MyBreakpoint”, type `break enable MyBreakpoint` in an action’s Debugger Command field. (25739693)
- When paused in the debugger, stepping out of a block will unwind and land in a frame with debug symbol. To land in disassembly, hold the control key while clicking on the Step Over or Step Out control. (29482033)
- Besides showing you the paused line in the editor, Xcode indicates the column where the process is paused. This is helpful in knowing when to step in, analyzing crash reports, and locating yourself in code with multiple closures. (31197308)
- You can now specify a path for the LLDB init file to use in a Run and Test action. Configure this path in the Info tab of a scheme’s Run or Test action. The path can contain a build settings macro such as `${SRCROOT}`, so the file can be part of a project. (38677796) (FB5425738)
- Xcode debugger annotations will highlight source code with greater opacity to improve visibility in several Xcode themes. (53463745)
- The view debugger identifies runtime issues and presents optimization opportunities to improve the efficiency and responsiveness of the UI. The Debug navigator presents the suggestions when you debug the view hierarchy of an app. (56552710)
- To debug a Widget Extension, run the extension’s scheme. Set environment variables in the Arguments pane of the widget extension’s scheme to configure the debugging session. Widgets support one or more families, or sizes. To select the family to use when debugging, set the `_XCWidgetFamily` environment variable to `small`, `medium`, or `large`. If the extension uses [`WidgetBundle`](https://developer.apple.com/documentation/SwiftUI/WidgetBundle) to support multiple widgets, you can choose which one to debug by setting the `_XCWidgetKind` environment variable to match the `kind` property of the widget’s configuration. On macOS, you can specify the WidgetKit Simulator’s default view by setting the `_XCWidgetDefaultView` environment variable to `timeline`, `snapshot`, `placeholder`, or `info`. (57059772, 63777618)
- The view debugger now supports saving and reopening view hierarchy snapshots. After you capture a view hierarchy with the Debug View Hierarchy button in the debug bar, you can choose File > Export View Hierarchy to save it as a `.viewhierarchy` file. You can reopen the saved `.viewhierarchy` in Xcode to inspect the state of the view hierarchy as captured. (57933113)
- When a [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) is selected in the view debugger, the Object inspector now displays explanatory tooltips on Offscreen Flags and Group Flags. (58647887)
- If you have disabled breakpoints in the Breakpoint Navigator, you can use the contextual menu to delete all the disabled breakpoints. (59164503)
- Debug App Clips using the scheme created for the App Clip. In the scheme the environment variable `_XCAppClipURL` can be used to set the App Clip experience URL for the debugging session. (59404002)
- The view debugger now generates runtime issues for performance Optimization Opportunities for [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer). Choose Editor > Show Layers to view CALayers in the view debugger. Choose Editor > Show Optimization Opportunities to show or hide performance runtime issues. (60103476)
- Xcode 12 now encrypts the connection between Xcode and paired devices, protecting against an attacker in a privileged network position executing arbitrary code on connected iOS, iPadOS, watchOS, or tvOS devices during a remote debug session. (60386733) These security benefits are available when Xcode 12 connects to devices running iOS 14, iPadOS 14, watchOS 7, tvOS 14, or later versions. These OS versions also refuse debugger connections from older Xcode releases. Xcode 12 continues to support debugging for older OS versions, but without the new encryption. If you’re unable to upgrade to Xcode 12 or need to continue development on devices running older OS versions, you can help protect yourself with either of the following measures: - Connect Xcode to your devices over private and secured networks (including a direct connection); or
- Physically connect your device to the Mac running Xcode using a cable, and ensure that the “Connect via Network” checkbox in the Xcode Devices and Simulators Window is unselected for these devices. For more information about the security content of this update, see [`Apple security updates`](https://developer.apple.comhttps://support.apple.com/en-us/HT201222).
- Debug > Attach to Process and Debug > Detach are now in the middle of the menu, closer to the rest of the debug menu items. (60390611)
- View hierarchies captured with Xcode can now be exported to `.viewhierarchy` files. (61065771)
- The ClockKit framework generates Runtime Issues in Xcode, to help you analyze runtime bugs. (61346475)

###### Resolved

- Resolved an issue where clicked buttons in the debug bar didn’t suitably change their appearance in Dark Mode. (46294176)
- Fixed a crash that could occur when you select the memory browser in the Debug navigator. (54767689)
- When debugging with `lldb`, `po self` now displays the address of a pointer in Swift code on a simulated tvOS device. (58477904, 65150335)
- Xcode persists the Malloc Stack Logging choice in the Scheme Editor’s Diagnostics tab in a more timely manner. (59154142)
- Xcode now launches applications with Launch Services to better reflect a real application running environment. (59478437)
- Resolved an issue which caused the view debugger to show no content when the user selects “Focus on View” in the view hierarchy of the debugged process. (60255111)

###### Known Issues

- Xcode may crash when opening a debug gauge. (64181692)
- Debugging a Widget on iOS 14 doesn’t launch the extension, or the debugger doesn’t attach to the Widget. (64274027, 66920094) : Delete the Widget from the Home screen, clean the project, then build and run again.

##### Devices

###### New Features

- The “Add Device” sheet in the Devices and Simulators window is now resizable. (59611308)
- The Devices and Simulators window permits selecting multiple devices in the navigator, so they can be unpaired together. This makes it easier for you to clean up old records for devices you aren’t using anymore. (63290367)

###### Known Issues

- You can’t debug a WatchKit App when an App Clip is added to its paired iOS App, if that iOS App isn’t installed. (65784374) (FB8065876) : Set “Supports Running Without iOS App Installation” in the General settings for the WatchKit App Extension’s build target.
- On macOS 11, Xcode may crash when you click the “View Device Logs” button for a device you select in the Devices and Simulators window. (66303792) : Xcode copies logs from connected mobile devices to a local directory. For information about how to manually retrieve crash and energy logs, see [`Find device crash and energy logs on a Mac or Windows computer`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev0f3181c2c). To retrieve other types of logs, use the workflows described in [`Acquiring crash reports and diagnostic logs`](https://developer.apple.com/documentation/Xcode/acquiring-crash-reports-and-diagnostic-logs).
- On macOS 11, Xcode may crash when you open the Devices and Simulators window. (66932201, 67336055) : Make sure that you have trusted all mobile devices paired with the Mac, physically disconnect any devices that you don’t wish to use for development, and set “Show scroll bars” to Always in the General pane of System Preferences.
- Xcode may crash when unpairing a device in the Devices and Simulators window. (68156364)
- Downloading watchOS symbols may take longer than expected. (68316765) : If the symbol data isn’t populating, quit and restart Xcode to retry downloading.

##### Documentation Viewer

###### New Features

- The Developer Documentation window has a new Featured page with an overview of Apple’s latest developer documentation. (59319966)

##### Instruments

###### New Features

- You can now export Analysis Core Tables from existing Instruments `.trace` files using the `xctrace` command. See the `xctrace` man page for more details. (12491801)
- Instruments now supports better expansion of inlined functions in call trees and event backtraces when a dSYM is present. (16252965)
- Instruments now annotates applicable CPUs as Efficient or Performance. Selecting a CPU will show relevant details, including call trees with data constrained to that CPU. (38031506)
- Instruments can now import data from `.logarchive` files. Instruments imports these files using the new Logging template that contains the `os_signpost` and `os_log` tools. To customize which template to use during import, use File > Import To Template… (38422518)
- The `xctrace` command can now attach to an existing process by name using the `--attach` flag. (47649439) (FB5645940)
- The File Activity template now provides aggregate statistics for logical reads and writes, in addition to individual detail views for Disk Reads and Disk Writes. (52148749)
- The System Trace template is significantly more performant on new recordings and imported files. (55037273)
- Files with symbol-heavy recordings are now 80-90% smaller, because of optimized `.trace` symbol storage. (56048324)
- Instruments includes a new Animation Hitches template for detecting scrolling and animation issues, to help you visualize and investigate an application’s graphics pipeline. (56553023)
- Double-clicking events in the track view will now switch to a detail view that shows the underlying data at the inspected time so you can further investigate. (59173526)

###### Resolved

- Fixed an issue where double-clicking on a Call Tree node to move to source failed for any track without an instrument. (32751506)
- Thread names in Instruments now reflect values set by developers utilizing thread-naming APIs. (51279758)
- Significantly improved trace saving and loading performance. Saves are now up to 40% faster. Opening trace files is up to 80% faster. (51597633)
- Fixed an issue where the `<slice>` attribute for a `<calltree>` detail was ignored on Custom instruments. (61944832)

###### Known Issues

- The Animation Hitches template doesn’t show hitch intervals when instrumenting macOS apps. (61082729)

###### Deprecations

- The `instruments` command is now deprecated in favor of its replacement: `xctrace`. Use `xctrace` to record, import, and export data from Instruments `.trace` files. (36641078)

##### Interface Builder

###### New Features

- Added support for the new [`safeAreaLayoutGuide`](https://developer.apple.com/documentation/AppKit/NSView/safeAreaLayoutGuide) on [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) introduced in macOS 11. (16915977)
- Interface Builder’s canvas has a new minimap. You can show and hide the minimap with Editor > Canvas > Minimap. Drag the minimap to any corner of the canvas. You can also double-click or command-click in the minimap to focus on a specific scene. (19218249, 63831585) (FB5891904)
- Find and Replace now includes matches in attributed string literals. (21508424)
- Interface Builder now has a Current Date option for [`NSDatePicker`](https://developer.apple.com/documentation/AppKit/NSDatePicker). (56048031)
- Interface Builder now supports the two-column and three-column styles for [`UISplitViewController`](https://developer.apple.com/documentation/UIKit/UISplitViewController) introduced in iOS 14. (57025285)
- Standard spacing constraints are now created by default when items are positioned a standard distance from each other. (57057604)
- Added support for SF Symbols in macOS 11. (58480276)
- Added support for the new [`isNavigational`](https://developer.apple.com/documentation/AppKit/NSToolbarItem/isNavigational) toolbar item property in macOS 11. (58584394)
- Added support for [`UIButton.ButtonType.close`](https://developer.apple.com/documentation/UIKit/UIButton/ButtonType-swift.enum/close). (59211094)
- Added support for [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView) and [`NSTextField`](https://developer.apple.com/documentation/AppKit/NSTextField) new content type property in macOS 11. (59273897)
- Added support for the new [`toolbarStyle`](https://developer.apple.com/documentation/AppKit/NSWindow/toolbarStyle-swift.property) in macOS 11. (59274307)
- Added support for the new [`subtitle`](https://developer.apple.com/documentation/AppKit/NSWindow/subtitle) property in macOS 11. (59274358)
- Added support for the new [`NSSearchToolbarItem`](https://developer.apple.com/documentation/AppKit/NSSearchToolbarItem) in macOS 11. (59277905)
- Added support for selecting text styles in macOS 11. (59297807)
- You can now edit the Render Mode and Symbol Scale of SF Symbols for storyboard and `.xib` files. When you select an SF Symbol in the image picker, two additional properties expand below the image name. To display SF Symbols that support full color, set the Render Mode to Original. (61844681, 63280118)
- Added support for the new  [`NSTableView.Style`](https://developer.apple.com/documentation/AppKit/NSTableView/Style-swift.enum) with Automatic, Full Width, Inset, and Source List options. (61958249)
- Added support for new UISwitch properties, [`preferredStyle`](https://developer.apple.com/documentation/UIKit/UISwitch/preferredStyle) and [`title`](https://developer.apple.com/documentation/UIKit/UISwitch/title). (62320185)
- Added support for the new [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) Layout Margins Guide. (62908200)
- The Objects library contains a new Window Controller with Sidebar object, composed of a window controller and split view controller configured to provide a toolbar, sidebar, and full-size content view with safe area layout guides enabled. (63045604)

###### Resolved

- Fixed a bug where `IBDesignable` views weren’t using the intrinsic content size the first time Interface Builder displays the storyboard or `.xib`. (23234553) (FB5797024)
- Fixed an issue that would sometimes omit iOS text styles from the inspectors. (51854358) (FB6169763)
- When an `IBDesignable` view fails to build, there is now an error directly on the view in canvas. Clicking the error icon on the IBDesignable property in the Identity inspector, now provides a popup that displays the error for easier debugging. (56408987)
- Storyboards and `.xib` files will now use the intrinsic content size provided by an `IBDesignable` view when overriding [`intrinsicContentSize`](https://developer.apple.com/documentation/AppKit/NSView/intrinsicContentSize) on an `NSView`. (56419405)
- Fixed a bug where the Spell Checking property was ignored on [`UITextView`](https://developer.apple.com/documentation/UIKit/UITextView). (60750116) (FB7636246)
- Fixed an issue where images with Preserves Vector Representation enabled wouldn’t correctly display light or dark variants in the canvas. (61243894) (FB7649981)
- Improved options of the Layout property of a View in the Size inspector, for greater clarity. (61561405) - The Automatic option is now named Inferred, and indicates whether the view is using constraints or an autoresizing mask. A view whose Layout is Inferred uses Translates Autoresizing Mask Into Constraints of `false` when the view is using constraints or is in an Auto Layout container, such as an [`NSStackView`](https://developer.apple.com/documentation/AppKit/NSStackView) or [`UIStackView`](https://developer.apple.com/documentation/UIKit/UIStackView). Otherwise, it uses autoresizing masks and Translates Auto Resizing Mask Into Constraints of `true`.
- Translates Auto Resizing Mask Into Constraints is always `true` for a view whose Layout is Autoresizing Masks.
- Fixed a crash that could happen when using Image Stacks in tvOS storyboards. (62113733) (FB7671430)
- Fixed some performance issues with [`NSTabView`](https://developer.apple.com/documentation/AppKit/NSTabView) and hidden views in a storyboard or `.xib` canvas. (63008369, 64314634)

###### Known Issues

- On macOS Big Sur, Interface Builder displays macOS storyboards with the new look and feel. However, when you build and run an app with the macOS Catalina SDK in Xcode 12, split views, table views, toolbars, and window titles may not match the storyboards. (66612224)

###### Deprecations

- Interface Builder no longer provides access to the Can Draw Concurrently property. You may still configure this behavior in code with [`canDrawConcurrently`](https://developer.apple.com/documentation/AppKit/NSView/canDrawConcurrently). (42437767)
- QTCaptureView and QTMovieView are deprecated and no longer supported. Remove these views from storyboards and `.xib` files. (64263402)

##### Linking

###### New Features

- The linker now supports `@filename` response files. The contents of the file are substituted into the argument list in place of the file name. The linker is typically invoked through Clang, which already supports response files. To have the linker parse a response file instead of Clang, use `-Wl,@filename`. (54356464) (FB7037642)
- The linker now reports a warning if you link with a dylib but don’t use any symbols from it. If you really mean to do this, you can either suppress all such warnings with `-Wl,-warn_unused_dylibs` or mark unused frameworks individually as needed, using `-needed_framework Foo` instead of `-framework Foo`. For example, in Other Linker Flags, add `-Wl,-needed_framework,Foo`. (60936600)

###### Resolved

- When using the `-map file` option, functions and data from `.o` files built for Link Time Optimization are now tracked more accurately. (50031245)
- When encountering an error about misaligned pointers, the linker now shows all such pointers, instead of just the first. (61019996)

##### Metal

###### New Features

- The new Summary Page in Metal Debugger provides an overview of captured command buffers, performance metrics, and memory usage. Xcode analyzes the commands and provides a list of insights that describe potential issues you may want to investigate. From the summary screen, you can navigate to more detailed information about each topic area. (53887141)
- When capturing data on a device with A11 or newer GPUs, Metal System Trace tracks start and end times for individual shaders, which provides more granular insights into how the GPU executes your code. (54615187)
- In Instruments, GPU Counters are now available for macOS in addition to iOS. Use GPU Counters to get more information about how the GPU runs your shader code, such as whether the shader code is underutilizing the GPU or bottlenecked in a particular part of the GPU. (55966447)
- Shader Validation detects common shader bugs. Turn on Shader Validation when debugging your app to look for illegal memory access and other problems that can otherwise be difficult to debug. (56194992)
- The GPU Counter view in Metal Debugger has a new user interface, making it easier to filter and sort through the GPU counter data. Create your own counter sets to see the exact data you need to diagnose your app’s performance. (56792744)

###### Known Issues

- Metal Debugger may show empty Summary and Memory reports when debugging a macOS Catalina App. (68599136)

##### Organizer

###### New Features

- Metrics Charts in Xcode Organizer are now interactive, allowing developers to compare and contrast metrics associated with different versions of their applications. (49305896)
- Xcode Organizer now displays scroll-hitch metrics. Use these metrics to help identify perceptible animation delays you encounter while scrolling in your application. To view the Scroll Hitch bar graph, click on the Scrolling section in the Metrics Organizer window. (53514128)
- Xcode Organizer now provides Disk Writes diagnostic reports. Use these reports to optimize the disk-write performance of your apps. To view the reports, click on the Disk Writes item in the Reports section of the Organizer. (53514182)
- Metrics in the Xcode Organizer now include data from app versions with limited field usage. App versions that don’t meet the previous year’s usage threshold are badged with a gauge icon next to the version number, and display a margin of error. As customer usage increases, the margin of error decreases until it is low enough that it can be omitted from the UI. (53514245)

###### Known Issues

- Exporting a watchOS application for ad-hoc or development distribution may fail when using Xcode 12 and thinning for “all compatible device variants.” (66637482) : Don’t thin, or choose a specific target device.

##### Playgrounds

###### New Features

- Xcode’s Report Navigator now includes Playground build logs. (56351128)
- Xcode Playgrounds now build the active scheme’s targets and make them importable when Build Active Scheme is enabled in the File inspector. (60089627)
- Xcode Playgrounds can now import and use Swift packages and frameworks. Select the Build Active Scheme checkbox in the playground’s File inspector and ensure that the active scheme builds the package or framework target. (60612584)

###### Resolved

- Live views are now accessible to VoiceOver. (40548790)
- Resolved an issue causing the LLDB RPC server to crash while using Xcode Playgrounds. (59271354)
- Live views in iOS and tvOS Playgrounds now use the view’s intrinsic content size if the view receives a zero size. (61068790)
- Playgrounds now support asset catalogs. (61110861)
- The live view of a macOS Playground falls back to a sensible default size, if the view has no inherent size. (62065321) (FB7670503)
- If a Playground live view has a size of zero, a banner now indicates why the live view isn’t visible. (63033441)
- An Xcode Playground now automatically compiles Core ML models in its Resources folder and Playground code can access the generated ML model interface. (63109576)

###### Known Issues

- Xcode may show the text “No Editor”, instead of opening the source editor of a Playground immediately after creating it. (56484197) : Use View > Navigators > Project to reveal the Project Navigator, then select the Playground manually.

##### Previews

###### New Features

- Xcode now considers edited files and open previews when selecting which app renders previews. Files contained in an application-linked framework now preview inside of the application, picking up any resources and entitlements provided by the application. (46057388)
- Each preview now has buttons to start Live Preview, Preview on Device, Inspect Preview, and Duplicate Preview. (47472549)
- The canvas has a new integrated experience for adding modifiers. Click the Inspect Preview button to see modifier recommendations for the selected view and search for the modifier you want to apply. (51696163)
- Code completion now inserts a compilable completion and example for SwiftUI views and modifiers. (55455037)
- Xcode supports previewing widgets. For an example of how to configure a widget preview, see [`WidgetPreviewContext`](https://developer.apple.com/documentation/WidgetKit/WidgetPreviewContext). (56390347)
- The Attributes inspector now offers quick actions for editing the name, device, layout, preferred color scheme, and accessibility text size of a selected preview. (56413241)
- Xcode Previews now supports previewing views in frameworks on-device if the framework is linked by an app in the selected scheme. (57025579)
- Xcode now supports previewing SwiftUI watchOS complications by adding the [`previewContext(_:)`](https://developer.apple.com/documentation/SwiftUI/View/previewContext(_:)) modifier to a watchOS complication. (57848297)
- Xcode now supports previews for App Clips. (59227941)
- Xcode now connects with the new Xcode Previews app for iOS 14 and iPadOS 14 for greatly improved on-device previews. The Xcode Previews app seamlessly displays changes from Xcode Previews on devices. The first time you use on-device previews, the Xcode Previews app appears on your device’s Home screen. Launching Xcode Previews on a device after disconnecting from Xcode restores the last-displayed preview. (59631753)
- Double-clicking a view in a preview now selects the corresponding code and moves keyboard focus to the source editor, allowing for quick editing of a view’s contents. (60171349)
- The bottom bar of the canvas now contains a button for quickly inspecting the selected view. (62990297)
- Add custom SwiftUI views and modifiers to the Xcode library using the new [`LibraryContentProvider`](https://developer.apple.com/documentation/DeveloperToolsSupport/LibraryContentProvider) protocol. (63154504)

###### Resolved

- Packages that contain previews can now update without fully rebuilding the active scheme. (51030302)
- Rebuilding against the iOS 14, macOS 11, watchOS 7, and tvOS 14 SDKs changes uses of [`GeometryReader`](https://developer.apple.com/documentation/SwiftUI/GeometryReader) to reliably top-leading align the views inside the [`GeometryReader`](https://developer.apple.com/documentation/SwiftUI/GeometryReader). This was the previous behavior,  when it wasn’t possible to detect a single static view inside the [`GeometryReader`](https://developer.apple.com/documentation/SwiftUI/GeometryReader). (59722992) (FB7597816)

###### Known Issues

- You can’t select views in widgets in the Previews canvas. (62517078)
- Animations may not work in live SwiftUI previews. (63333795)
- Live SwiftUI previews for macOS may not appear when making changes until you click the Bring Forward button on the canvas. (63865018)
- Previewing a widget extension for iPad devices may show an excess blank bar at the top. (64277772)
- A widget extension preview doesn’t adapt to the dark appearance when you apply a `.preferredColorScheme(.dark)` appearance modifier. (64277915)

##### Project Editor

###### New Features

- The Document Types, Exported Type Identifiers, and Imported Type Identifiers panes support the new templated document icons in macOS 11. (59314567)

##### Project Navigator

###### New Features

- The selection in the Project navigator, Source Control navigator, Debug navigator (for View Debugger and Memory Graph) and Reports navigator now tracks the contents of the active editor. (9546415) (FB5634395)
- Xcode’s navigators now respect the System “sidebar icon size” and also allow it to be changed independently of that setting. (11619444)
- File results in the Find navigator are now adorned with a path showing their workspace location. (47196462)
- The Project navigator now allows control over text-matching style (“contains”, “does not contain”, “begins with”, or “ends with”) when typing a filter term and pressing enter. (56474089)
- Open Quickly matches are now more targeted and focused. Open Quickly is better at finding discontiguous word matches. Typing “resetDownload” matches “resetDocumentDownload” as you’d expect. The improved accuracy focuses on the best matches, and excludes the worst. (59065704)
- Text filtering in the jump bar, scheme menu, and run destination chooser is significantly improved. It shows the best matches, and suppresses the worst. Filtering for frequently occurring characters like ‘init’ will show just init methods, instead of every symbol that contains i, n, i, t. (59597035)

###### Resolved

- Resolved crashes when adding and moving items in the project structure. (48644008, 57752303)
- Improved performance of Project navigator, in particular “Reveal in Project Navigator” and recursive expand or collapse operations on groups. (49189414, 60245991, 60925755)
- Improved stability and accuracy of results when filtering the project structure for text and SCM status. Note that results now require all filter terms to match, instead of any term. (57708582, 58099589, 62128435)

##### Reality Composer

###### Deprecations

- Reality files created by Xcode 12 can only be loaded in macOS 10.15.4 or later, iOS and iPadOS 13.4 or later, and Reality Composer 1.4 or later. (58825031)

##### Refactoring

###### New Features

- Editor > Refactor > Rename now handles renaming symbols with a definition or references that are escaped with backticks. (46409010)

##### Sanitizers

###### Resolved

- Xcode now supports Thread Sanitizer when debugging on simulated watchOS devices. (54654296, 64421085)

##### Server

###### Resolved

- You can select which branch to use for integrations on the Repositories tab of an Xcode Server bot. (58615215, 59068222)

##### Signing and Distribution

###### New Features

- App Clips can use the [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension) framework and [`Hotspot Configuration Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.HotspotConfiguration) to configure Wi-Fi networks. (64966949)
- Xcode 12 lets you build your iOS app for running on Macs with Apple silicon. Make sure you’ve registered your Mac with Apple silicon’s hardware identifier (available in the System Information app’s Hardware > Provisioning UDID field) in your account on [`https://developer.apple.com/account`](https://developer.apple.comhttps://developer.apple.com/account), find the archive in the Organizer window, click on Distribute App, select either “Ad Hoc” or “Development,” choose your distribution options, select “Automatically manage signing,” and proceed through the remainder of the distribution assistant to create an IPA. Once you’ve created the IPA, you can transfer it to your Mac with Apple silicon, and double-click on it to install. During the app’s first launch, you will be prompted to open the Security & Privacy preferences pane to enable the app. To see the launch button in the preferences pane, make sure your Mac is configured to only allow apps from the App Store and identified developers. (68513041, 68528315).

###### Known Issues

- App Clips can’t access Wallet passes with the Pass Type IDs Entitlement. However, App Clips can determine whether a specific pass is already present in Wallet and prompt the user to add a pass if necessary. If you’ve already added the Wallet capability to an App Clip target, you may not be able to build or submit your app to App Store Connect. Remove the Wallet capability in the target editor’s Signing & Capabilities pane and disable or delete any code that makes use of this removed feature. (65244156)
- Xcode automatic signing may not automatically include Macs with Apple silicon in your provisioning profile when exporting an archive. (66857321) : If Xcode produces an IPA that doesn’t install on your registered Macs, remove any Ad Hoc Distribution or Development provisioning profiles from the ~/Library/MobileDevice/Provisioning Profiles directory before exporting your archive.
- Open source software you previously built on the Apple silicon Developer Transition Kit may no longer run, due to code-signing errors. (68226054) : Re-build the software with Xcode 12, or re-sign the software with `codesign -s - --preserve-metadata=identifier,entitlements,flags,runtime -f <path to mach-O>`.

##### Simulator

###### New Features

- Simulator can display a simulated device in full-screen mode, or tile its window alongside Xcode. (32866357)
- Simulated watchOS 7 devices support 64-bit processes. To verify watchOS projects are 64-bit clean in Simulator, make sure `ARCHS` is set to its default value. (54654060, 66352876) > **Note**: Projects must be 64-bit clean in Simulator on Macs with Apple silicon, which don’t support 32-bit code. Projects must be 64-bit clean in Simulator on Macs with Apple silicon, which don’t support 32-bit code.
- Window > Stay On Top keeps device windows in front of other application windows. (57060945) (FB7439463)
- When a device window loses focus, it pauses capturing input events from Send Pointer to Device and Send Keyboard Input to Device until Simulator regains focus. (57351155)
- Simulator defaults to the internal microphone unless you explicitly choose a different audio source. This avoids triggering phone call mode on Bluetooth headsets, which degrades audio quality while listening to music. (59338925, 59803381)
- Simulator supports simulating Nearby Interaction for devices that support the feature. Dragging the device window around on the screen will update the simulated distance between the two devices. The farther apart the windows are on screen the greater the reported distance. (62227375)

###### Resolved

- The Download Components preferences pane now prompts once for authentication to download and install legacy simulators, rather than prompting for authentication on each install. (22993731)
- CoreSimulatorService doesn’t use as much CPU when clients rapidly connect and disconnect. (53220616)
- Simulator now allows selecting the Physical Size, Point Accurate, and Pixel Accurate size options, even if the chosen option causes part of the window to be off-screen. (56163353) (FB7366108)
- Simulator runtimes now persist when updating Xcode from the app store, moving Xcode, or renaming Xcode. (58100481)
- When entering keyboard- or pointer-capture mode with keys held down Simulator no longer leaves those keys stuck in macOS. When exiting capture mode the correct left or right key-up event is delivered to the guest to prevent it from thinking a modifier key is stuck. (60174685)
- Simulator no longer creates default devices in custom device sets, restoring the behavior of Xcode 11.3. (63750578) (FB7717786)
- Fixed a bug where launching apps in Simulator while Simulator is already running sometimes failed with an error of “Timed out waiting for Simulator.app to become ready”. (64508635)
- Fixed an issue which prevented Xcode from compiling a project for a simulated watchOS device if the project used [`SignInWithAppleButton`](https://developer.apple.com/documentation/AuthenticationServices/SignInWithAppleButton). The error message was “Cannot find ‘SignInWithAppleButton’ in scope”. This occured even if the project imported [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) and [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices). (67817241)

###### Known Issues

- When simulating a push notification in Simulator with the `content-available` key set, the system calls [`application(_:performFetchWithCompletionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:performFetchWithCompletionHandler:)) instead of [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didReceiveRemoteNotification:fetchCompletionHandler:)). (60426170, 60974170) (FB7625283)
- Activating Display Zoom on a simulated 12.9” iPad Pro distorts the simulated device’s display. (67455180) : Restart the simulated device to return to normal display.
- If you enable or disable zoom mode while CarPlay is enabled, attempts to interact with CarPlay will cause a partial restart of the simulated iOS device. (67534104) : Close the CarPlay window, then re-enable or re-disable CarPlay.

###### Deprecations

- When running on macOS 11, Simulator supports iOS 11.4 or later. (59938106)

##### Source Control

###### New Features

- You can now specify the default branch name for new repositories in the Source Control pane of Xcode’s Preferences. This preference uses the `init.defaultBranch` Git config option available in Git version 2.28. (66232985)

##### Source Editor

###### New Features

- Repeated code completion invocations inside Swift function bodies are now up to 15 times faster compared to Xcode 11.5. (59830963)

###### Resolved

- Fixed a crash that could occur with large amounts of log output in the debug console. (49261867)
- The editor now preserves the relative indentation of pasted text, rather than re-indenting the text. This can be controlled in Preferences > Text Editing > Indentation. (52348424)
- Fixed an issue where the `com.apple.dt.SKAgent` process would consume a lot of memory in large projects with mostly flat hierarchies of source files. (53835770)
- Fixed an issue where code completion sometimes suggests a class name rather than a variable name. (56887185)
- Fixed a problem where incorrect content would show up in the jump bar for system headers. (57509269)
- Fixed a problem where pasting into multiple insertions points would reset the selection to a single insertion point. (57572639)
- Fixed an issue where code completion suggests a case-insensitive match candidate in the most recently used list, instead of a lowercase, case-sensitive match candidate. (57962108) (FB7495633)
- Fixed an issue where typing a backtick in documentation, with the Text Editing preference Enable type-over completions unchecked, would insert an extra backtick. (58011556)
- Fixed an issue where editing a file outside of Xcode would cause Xcode to crash on launch. (58272739)
- Fixed issues where Xcode wouldn’t properly save edits to `Date` and `Data` values in property list files. (58836269)
- Improved the display order in code completion to prioritize symbols matching parameter types. (59066628)
- [`Callable values of user-defined nominal types`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0253-callable.md) is now supported in Swift code completion. Code completion shows the calling signature after a base expression followed by an opening parenthesis. (59302416)
- A breakpoint hidden within multiple code folds now correctly expands the folded code when the debugger hits it or when it’s selected in the Breakpoint navigator. (59445409)
- Fixed an issue where folding code would sometimes cause a crash. (60170676)
- Fixed an issue where Xcode would hang after multiple large refactors. (61749114)
- Fixed an issue where editing an Objective-C category name would sometimes cause a crash. (61860583)
- Fixed an issue where folding code with trailing whitespace would sometimes cause a crash. (62218489) (FB7673070)

###### Known Issues

- A new Xcode Source Editor Extension target doesn’t automatically set up embedding `XcodeKit.framework` in the extension. (59274389) : Embed `XcodeKit.framework` in the extension manually.

###### Deprecations

- For compatibility with new security features in macOS 11, Xcode extensions must be built using Xcode 12 and must embed `XcodeKit.framework`. An Xcode extension rebuilt with these tools remains compatible with older versions of Xcode and macOS. (51822755)

##### Storekit

###### New Features

- Xcode 12 supports testing in-app purchases directly in Simulator or on a connected device, using a new local [`StoreKit`](https://developer.apple.com/documentation/StoreKit) test environment. Configure in-app purchase information locally for testing, before setting it up in App Store Connect and without a connection to App Store servers. For more information on getting started, see [`Testing In-App Purchases in Xcode`](https://developer.apple.com/documentation/StoreKit/testing-in-app-purchases-in-xcode) and [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode). The test environment supports early development, unit testing, and debugging in-app purchases, as described in [`Testing at all stages of development with Xcode and the sandbox`](https://developer.apple.com/documentation/StoreKit/testing-at-all-stages-of-development-with-xcode-and-the-sandbox). Use the [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest) framework to create and automate tests for handling in-app purchase transactions. [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest) supports comprehensive testing of in-app purchase scenarios, including changes in subscription status, subscription offers, restore purchases, ask to buy, interrupted purchases, and more. Control the test environment, including clearing purchase history, resetting offer eligibility, and speeding up the renewal rate of time for testing subscriptions. (56504988)

###### Known Issues

- Xcode crashes when selecting “Subscription Options” in the [`StoreKit`](https://developer.apple.com/documentation/StoreKit) transaction manager. (68354368) : Use the [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest) framework to test downgrading, cross-grading, or upgrading a subscription.

##### Swift

###### New Features

- Improved indentation for chained method calls, especially those that involve nested or trailing closures. (25519439) (FB5472851)
- Improved the error message when using SwiftUI’s [`List`](https://developer.apple.com/documentation/SwiftUI/List) initializer that takes a collection of identifiable data with an element type that doesn’t conform to [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable). (51519565) (FB6130940) For example, the following code: ```swift
import SwiftUI

struct NotIdentifiable {}

let data: [NotIdentifiable] = []

List(data) { _ in
    Text("Row")
}
``` now produces the error message: ```text
error: initializer 'init(_:rowContent:)' requires 'NotIdentifiable' conform to 'Identifiable'
List(data) { _ in
^
```
- Swift indentation now column-aligns conditions in `guard` and `if` statements. (53131527) (FB6688335) For example: ```swift
guard let x = someOptional,
      let y = anotherOptional else {
  // ...
}
```
- The compiler now diagnoses exclusivity violations within code that computes the `default` argument during [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary) access. ([`SR-11700`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-11700), 56378713) ```swift
struct Container {
  static let defaultKey = 0

  var dictionary = [defaultKey:0]

  mutating func incrementValue(at key: Int) {
    dictionary[key, default: dictionary[Container.defaultKey]!] += 1
  }
}
// error: overlapping accesses to 'self.dictionary', but modification requires exclusive
// access; consider copying to a local variable
//     dictionary[key, default: dictionary[Container.defaultKey]!] += 1
//     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// note: conflicting access is here
//     dictionary[key, default: dictionary[Container.defaultKey]!] += 1
//                              ~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~
``` The exclusivity violation can be avoided by precomputing the `default` argument using a local variable. ```swift
struct Container {
  static let defaultKey = 0

  var dictionary = [defaultKey:0]

  mutating func incrementValue(at key: Int) {
    let defaultValue = dictionary[Container.defaultKey]!
    dictionary[key, default: defaultValue] += 1
  }
}
// No error.
```
- Swift now allows the implicit use of `self` in `@escaping` closures when reference cycles are unlikely to occur. ([`SE-0269`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0269-implicit-self-explicit-capture.md), 56408426) First, implicit use of `self` in `@escaping` closures is now allowed if the user has explicitly captured `self` in the closure’s capture list, so the following code is now valid: ```swift
class Test {
  var x = 0
  func execute(_ work: @escaping () -> Void) {
    work()
  }
  func method() {
    execute { [self] in
      x += 1
    }
  }
}
``` Second, implicit `self` is available in `@escaping` closures when `self` is a value type, making the following code valid: ```swift
struct Test {
  var x = 0
  func execute(_ work: @escaping () -> Void) {
    work()
  }
  func method() {
    execute {
      x += 1
    }
  }
}
```
- A property with an attached property wrapper can now rely on type inference to infer the wrapped value type when using default initialization without empty parentheses on the wrapper attribute. (59471019) For example: ```swift
@propertyWrapper
struct IntWrapper {
  var wrappedValue: Int { 0 }
}

struct UseWrapper {
  @IntWrapper var value
}
``` The wrapped property `UseWrapper.value` uses default initialization of `IntWrapper`, and relies on type inference to deduce the type-wrapped value type to be `Int`.
- In order to shorten incremental compilations, Swift now keeps separate fingerprints for each type- (and protocol-) body. These  mean that if you change the body of a `struct`, `enum`, `class`, or `protocol` in a file that also defines other `struct`, `enum`, `class`, `protocols`, only the changed entity will be counted as “dirty” for the purpose of recompiling other files. (59954707) For example, suppose you have a file that defines two `structs`: ```swift
struct A {
}
struct B {
}
``` and you add a member to `A`: ```swift
struct A {
  var x = 17
}
struct B {
}
``` Before this change, the compiler would have recompiled any file using either `A` or `B`. Now, the compiler doesn’t recompile files that use only `B`. If you experience problems with this feature, disable it by passing `-disable-type-fingerprints` into the Swift compiler via the `Other Swift Flags` build setting. If you still experience problems, disable the new dependency infrastructure by passing `-disable-fine-grained-dependencies` into the Swift compiler via the `Other Swift Flags` build setting.
- Xcode 12 includes support for using `@main` in place of `@UIApplicationMain` or `@NSApplicationMain` in UIKit- or AppKit-based apps. (60502727, 60502804, 63291088)
- Declarations inside generic contexts can now have `where` clauses even when the declaration itself doesn’t have additional generic parameters. ([`SE-0267`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0267-where-on-contextually-generic.md), 64228492) For example: ```swift
struct Box<Wrapped> {
    func boxes() -> [Box<Wrapped.Element>] where Wrapped: Sequence { ... }
}
```
- `lazy` properties may now have `didSet` and/or `willSet` observers. (64229062)
- Swift 5.3 introduces a `#fileID` identifier which produces a shorter string than `#file`. The `#fileID` string contains the filename and module name, but leaves out the rest of the path to the file; this saves space, improves performance, and avoids accidentally embedding private information like the developer’s home directory name in binaries. Compiler-generated error messages (like force-unwraps) and standard library assertions like `precondition` and `fatalError` now use `#fileID` strings, and we recommend you use them instead of `#file` in production code. ([`SE-0285`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0285-ease-pound-file-transition.md), 65514304)
- Trailing closures are now matched to function parameters starting from the first closure parameter and moving forward. This allows defaulted closure parameters to more naturally work with multiple trailing closures ([`SE-0286`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0286-forward-scan-trailing-closures.md), [`SE-0279`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0279-multiple-trailing-closures.md), 65615074) For example, the function: ```swift
func animate(
    duration: Double,
    animations: @escaping () -> Void,
    completion: ((Bool) -> Void)? = nil
)
``` when called as: ```swift
animate(duration: 0.25) {
  // animations
}
``` matches the trailing closure to the `animations` parameter. You can then specify a completion handler using the new “multiple trailing closures” feature: ```swift
animate(duration: 0.25) {
  // animations
} completion: { finished in {
  // completion handler
}
``` A new warning identifies cases where the new, trailing-closure-matching rules differ from the old ones. For example: ```swift
func f(a: () -> Int = { 17 }, b: () -> Int = { 42 }) { }

f {
  0
}
``` In such cases, the compiler still applies the old (backward) rule (the trailing closure will match parameter `b`), but the compiler produces a warning and Fix-It that indicates the code will change behavior in a future language version: ```text
backward matching of the unlabeled trailing closure is deprecated; label the argument with 'b' to suppress this warning
```

###### Resolved

- Swift now supports unapplied references to protocol methods. Previously this only worked for methods defined in structs, enums, and classes. (21289579) (FB5819096) For example: ```swift
protocol Cat {
func play(catToy: Toy)
}

let fn = Cat.play(catToy:)
fn(myCat)(myToy)
```
- Swift indentation no longer under-indents multi-line expressions that appear within call arguments, parameter lists, array and dictionary literals, or tuples when their elements are column-aligned. (48934744)
- Fixed a compiler crash that happened in expressions involving `super` when the type of `super` had an error. (50819554)
- The experimental function builder feature is now correctly applied to a single-expression closure. (56340587) For example: ```swift
@_functionBuilder
struct ArrayBuilder<T> {
    static func buildBlock(_ values: T…) -> [T] {
        values
    }
}

func array(@ArrayBuilder<Int> builder: () -> [Int]) -> [Int] {
    builder()
}

array { 0 }
``` These closures already worked in SwiftUI, because they were just returning a single [`View`](https://developer.apple.com/documentation/SwiftUI/View), which is all that applying the [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder) transform to them would have made them do. However, not all function builder transforms have this property, and now they should work in general.
- Fixed a compiler crash that happened when using a property wrapper whose wrapped value has a mutating getter and non-mutating setter. (56467140)
- The Swift compiler no longer prints imports in the compatibility header for empty extensions or extensions with only private members and no public conformances. Objective-C/C source files relying on those transitive imports may raise errors about missing declarations and need to be updated with an explicit importation to compile as expected. (57133517)
- Fixed a crash caused by importing Objective-C interfaces that use the `objc_runtime_name` into Swift. (59306590) (FB7571694)
- Fixed a compiler crash that happened when overriding a property with an attached property wrapper in a subclass to implement property observers. (60093232) (FB7615016)
- Fixed an issue where initializing a property wrapper could invoke property observers before all of `self` is initialized. (60832285)
- Fixed an issue where global rename could alter SDK headers (62607314) (FB7681195)
- Widgets no longer crash when built for release. If you previously disabled `DEAD_CODE_STRIPPING` to work around such a crash, you can re-enable it. (65862827)
- Widgets no longer crash when bitcode is enabled or “Strip Style” is set to “All Symbols”. If you turned off `ENABLE_BITCODE` and unset `STRIP_STYLE` from “All Symbols” in the Widget target’s build settings, you can revert those workarounds. (66402358)

###### Known Issues

- The compiler may crash when a function builder body contains an empty switch statement. This issue can also cause a SourceKit crash while typing a switch statement in a SwiftUI view body. (65983237) (FB8111944)

##### Swift Packages

###### New Features

- You can now declare conditions for a Swift package’s target dependencies, such as limiting the dependencies by platform. This gives you more flexibility to describe complex target dependencies that support multiple platforms. (40237402)
- Swift packages can now contain resources such as images, asset catalogs, storyboards, and other files. When Xcode builds an app that depends on a package, it adds the package’s code and resources to the app bundle for use at runtime. For more information see [`Bundling resources with a Swift package`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package). (54361843)
- Swift packages can now vend prebuilt libraries distributed as XCFrameworks, allowing dependencies on libraries that can’t be distributed as source code. When Xcode builds an app that uses such a package, it embeds the libraries into the app bundle. For more information see [`Distributing binary frameworks as Swift packages`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/distributing-binary-frameworks-as-swift-packages). (56592977)
- Swift packages can now contain localized content for any resource in the package. In addition to localized content in asset catalogs, Xcode supports separate localization files in `.lproj` folders. For more information see [`Localizing package resources`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/localizing-package-resources). (56925255)

###### Known Issues

- A package resolution error with the message “database is locked” may occur when opening a workspace that contains package references. (61113361) : Close and reopen the workspace.

##### Testing

###### New Features

- [`XCTAssert`](https://developer.apple.com/documentation/XCTest/XCTAssert) and related assertion macros in Objective-C can now be used in contexts other than instance methods of [`XCTestCase`](https://developer.apple.com/documentation/XCTest/XCTestCase) subclasses. (4176422)
- Xcode now captures backtraces for test failures which occur outside of test methods and lists the failure callstack frames in the Issue navigator, the source editor, and the test report. (9955893)
- UI Tests will now implictly handle banner notifications on iOS that block the navigation bar during UI testing. (24920246)
- [`XCTest`](https://developer.apple.com/documentation/XCTest) now provides an [`XCTIssue`](https://developer.apple.com/documentation/XCTest/XCTIssue-swift.struct) type for richer modeling of test failures and other issues, along with associated APIs for working with these issues, including a new [`record(_:)`](https://developer.apple.com/documentation/XCTest/XCTestCase/record(_:)) method on [`XCTestCase`](https://developer.apple.com/documentation/XCTest/XCTestCase) which supersedes [`recordFailure(withDescription:inFile:atLine:expected:)`](https://developer.apple.com/documentation/XCTest/XCTestCase/recordFailure(withDescription:inFile:atLine:expected:)). (28547702)
- If the test process fails to launch or load the test bundle, for example if dynamic linking fails, or some other system failure prevents testing from starting, the error is presented in the test report under a section titled “System Failures”. (36926043)
- The number of passing, failing, and skipped tests is now surfaced in the test report UI. (49672520)
- When building for testing in a test plan-enabled scheme, Xcode now only builds test targets which are referenced by the active test plan. If the scheme references multiple test plans, then test targets which aren’t referenced by the currently-active test plan aren’t built. This change doesn’t affect `xcodebuild`: it builds all test targets referenced by all of the scheme’s test plans, unless one or more `-testPlan <name>` arguments are specified. (49737598)
- [`XCTApplicationLaunchMetric`](https://developer.apple.com/documentation/XCTest/XCTApplicationLaunchMetric) can now measure application launch to first frame. This new metric measures the time it takes for an application to launch and be ready to respond to a touch event. The following shows an example of using [`XCTApplicationLaunchMetric`](https://developer.apple.com/documentation/XCTest/XCTApplicationLaunchMetric) to measure how long it takes for an application to become responsive. (54721394) ```swift
func testAppLaunchToResponsive() throws {
    measure(metrics: [XCTApplicationLaunchMetric(waitUntilResponsive: true)]) {
        app.launch()
    }
}
```
- Xcode now excludes static library targets when computing the list of built product directories to include in the DYLD_FRAMEWORK_PATH and DYLD_LIBRARY_PATH environment variables when running tests. (55254152) (FB7249507)
- Performance XCTests now support animation performance testing when using  [`XCTOSSignpostMetric`](https://developer.apple.com/documentation/XCTest/XCTOSSignpostMetric) coupled with an animation `os_signpost` interval. The performance measurements returned include duration, three hitch-related metrics, and frame rate. To create an animation `os_signpost` interval, create a custom interval or use one of the provided UIKit intervals. The following shows an example performance test that measures the animation performance of scrolling an application. (55644042) ```swift
func testScrollingAnimationPerformance() throws {
  let table = app.tables.firstMatch
  measure(metrics: [XCTOSSignpostMetric.scrollDecelerationMetric]) {
    table.swipeUp(velocity: .fast)
  }
}
```
- If the test process stalls while waiting on an expectation, such as during [`waitForExpectations(timeout:handler:)`](https://developer.apple.com/documentation/XCTest/XCTestCase/waitForExpectations(timeout:handler:)) or a similar [`XCTWaiter`](https://developer.apple.com/documentation/XCTest/XCTWaiter) method, Xcode captures a spindump of the test process and attaches it to the test report. Previously, Xcode killed the test process and restarted execution with the next test. To continue to protect against stalled tests, enable the Test Timeouts setting in the test plan. (57163494)
- Xcode 12 expands on the ability to reset the authorization status of protected resources, introduced in Xcode 11.4. Health resources can be reset using the new constant [`XCUIProtectedResource.health`](https://developer.apple.com/documentation/XCTest/XCUIProtectedResource/health) which is available in iOS 14.0 and later. (57852954)
- [`XCUIElement`](https://developer.apple.com/documentation/XCTest/XCUIElement) and [`XCUICoordinate`](https://developer.apple.com/documentation/XCTest/XCUICoordinate) now allow specifying a velocity when performing swipe and drag interactions. (58059937)
- Screenshots taken during UI tests are now encoded as HEIC files instead of JPEGs where possible. This can considerably reduce the file size of result bundles. (58468642)
- [`XCTAssertEqual(_:_:accuracy:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTAssertEqual(_:_:accuracy:_:file:line:)-4epu5) and [`XCTAssertNotEqual(_:_:accuracy:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTAssertNotEqual(_:_:accuracy:_:file:line:)-326vc) now accept any [`Numeric`](https://developer.apple.com/documentation/Swift/Numeric) value instead of requiring a [`FloatingPoint`](https://developer.apple.com/documentation/Swift/FloatingPoint) value. This allows passing non-floating point numeric types such as [`Int`](https://developer.apple.com/documentation/Swift/Int), either as expression values or as the `accuracy` parameter. (58481784)
- Running an individual test in a test-plan-enabled scheme now skips configurations in that test plan which are disabled. Option- or Control-clicking a test diamond now denotes any configurations in the active test plan are disabled, and includes a “Run in All Enabled Configurations” option if some are disabled. (58547265)
- If you click the diamond next to a test or test class in the source editor, and that test is outside of the active scheme or test plan, Xcode will present a sheet allowing you to select the specific scheme or test plan that contains the test you want to run. (59223004)
- The Failed and Skipped scope bar buttons in the Test Report now show tests where any runs failed or were skipped, instead of only showing tests where all runs failed or were skipped. (59401757)
- The Test navigator now supports filtering skipped tests, in addition to failed tests and tests only contained in the active scheme. (59519058)
- When running tests in a test-plan-enabled scheme, Xcode now honors the “Debug XPC services” setting from the Options tab of the scheme’s Run action. (60439063)
- It is now possible to customize Default Execution Time Allowance and Maximum Execution Time Allowance in the Test Plan Editor. These settings apply when Test Timeouts is enabled. (61607966)
- XCTest now attaches a spindump diagnostic during UI testing when a UI query times out or the target app doesn’t become idle promptly. (62076023)

###### Resolved

- The Test navigator now correctly remembers its selection state and scroll offset when switching to and from other navigators, as well as when changing filters and schemes. (16308307, 24918098)
- UI target queries can now target all cells in the iOS Share Sheet. (49961747)
- Resolved a bug which prevented diamonds from appearing next to test methods and classes in the source editor when the Test navigator isn’t open. (54216504)
- When a test failure is recorded without any source code location, Xcode now displays a failure annotation in the source editor and a link to jump to that test method from the Issue navigator. (58118593)
- Resolved an issue that could cause keyboard modifiers to persist after a call to [`perform(withKeyModifiers:block:)`](https://developer.apple.com/documentation/XCTest/XCUIElement/perform(withKeyModifiers:block:)) if the block threw an unhandled exception. (58376575)
- XCTest APIs which include a `file: StaticString = #file` parameter now use the `#filePath` literal introduced in Swift 5.3 as the default parameter value. XCTest requires complete file paths to source files for error reporting and jumping to failures within Xcode. For more information, see notes on [`SE–0274`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0274-magic-file.md)   and `#filePath` in the Swift section. (58496553)
- Moving test plan files between directory levels in the Project navigator now updates references to those files in schemes properly. (59171975)
- Xcode will reinstall the app under test if it was deleted in a UI test. (60159203) (FB7616398)
- XCTest now supports using [`XCTSkip`](https://developer.apple.com/documentation/XCTest/XCTSkip-swift.struct) in [`tearDown()`](https://developer.apple.com/documentation/XCTest/XCTest/tearDown()) and [`tearDownWithError()`](https://developer.apple.com/documentation/XCTest/XCTest/tearDownWithError()) to mark a test as skipped. Although the test method may already have run to completion by the time the teardown methods are invoked, this may be useful to “retroactively” mark that a test wasn’t eligible to run or that its results may be invalid. (60634152)
- Resolved an issue where `xcodebuild` wouldn’t respect the `-enableCodeCoverage` option if the scheme uses a test plan. (62605817)
- `xcodebuild` no longer ignores the `-parallel-testing-worker-count` option when running tests in parallel. (64495567)

###### Known Issues

- Simulated devices don’t support animation performance metrics (total number of hitches, hitches total duration, hitch time ratio, frame rate, and frame count) when using an animation `os_signpost` coupled with the [`XCTOSSignpostMetric`](https://developer.apple.com/documentation/XCTest/XCTOSSignpostMetric). (63766090) : Use [`XCTSkip`](https://developer.apple.com/documentation/XCTest/XCTSkip-swift.struct) to skip over performance tests on simulated devices.

###### Deprecations

- Xcode now supports debugging apps and running tests on iOS devices running iOS 9.0 and above. (59561001)
- [`XCTAssert`](https://developer.apple.com/documentation/XCTest/XCTAssert) and related assertion macros in Objective-C and Objective-C++ no longer include a reference to `self` to access the current test case. With the `-Wunused-variable` or `-Wunused-lambda-capture` flag set, the compiler may now emit new warnings about code which declares an explicit variable or lambda capture for `self`. Remove the `self` variable or lambda capture, because it’s no longer required by [`XCTAssert`](https://developer.apple.com/documentation/XCTest/XCTAssert). (60017011)

## See Also

- [Xcode 12.5.1 Release Notes](xcode-12_5_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.5 Release Notes](xcode-12_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.4 Release Notes](xcode-12_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.3 Release Notes](xcode-12_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.2 Release Notes](xcode-12_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.1 Release Notes](xcode-12_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.0.1 Release Notes](xcode-12_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-12-release-notes)*