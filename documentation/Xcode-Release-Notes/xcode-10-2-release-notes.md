# Xcode 10.2 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 10.2 includes SDKs for iOS 12.2, watchOS 5.2, macOS 10.14.4, and tvOS 12.2. Xcode 10.2 supports on-device debugging for iOS 8 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 10.2 requires a Mac running macOS 10.14.3 or later.

##### General

###### New Features

- Xcode now supports downloading using macOS content caching. For information about macOS content caching, see [`About content caching on Mac`](https://developer.apple.comhttps://support.apple.com/guide/mac-help/about-content-caching-on-mac-mchl9388ba1b/mac). (12926899)

###### Resolved Issues

- Resolved an issue where uploads to the App Store wouldn’t include symbol information. (46242083)

##### Apple Clang Compiler

###### New Features

- `-Watomic-implicit-seq-cst` is a new warning, off by default, that warns when C `_Atomic` or `__sync_*` are used with the implicit, sequentially-consistent ordering. Most codebases use sequential consistency by default, but some demand that developers use explicit ordering everywhere. This warning is for the latter group. (28172966)
- A new diagnostic identifies framework headers that use quote includes instead of framework style includes. The warning is off by default but you can enable it by passing `-Wquoted-include-in-framework-header` to `clang`. (37077034)
- `-Wmemset-transposed-args` is a new warning that diagnoses calls to `memset` that have the second and third arguments transposed. For example, the following call is diagnosed with the new warning: `memset(buf, sizeof(buf), 0)`. (42360478)
- The constructors for `std::pair` are now marked `noexcept` conditionally on whether the corresponding constructors of its members are `noexcept`. This is a conforming extension that has potential performance benefits in case an operation can be made faster for types that don’t throw exceptions on construction. (29537079)
- The warning for using a non-const callable predicate in a `std::map` or a `std::set` now shows the point of instantiation of the faulty container instead of an unrelated implementation detail. (41370747)
- The `<experimental/any>` and `<experimental/optional>` headers are deprecated in favor of their C++17 counterparts: `<any>` and `<optional>`. They will be removed in a future release of Xcode, and you shouldn’t rely on their presence. (46903112)
- The usage of inlining macros to control the visibility of symbols in libc++ headers has been removed in favor of a better solution. This should result in code size and performance improvements in code that includes libc++ headers, and a dramatic improvement of the debugging experience when using libc++. (47259325)
- Public headers in a framework might mistakenly `#import` or `#include` private headers, which causes layering violations and potential module cycles. There’s a new diagnostic that reports such violations. It’s `OFF` by default in `clang` and is controlled by the `-Wframework-include-private-from-public`  flag. (38712182)
- The use of `@import` in framework headers prevent headers being used without modules. A new diagnostic detects the use of `@import` in framework headers when you pass the `-fmodules` flag. The diagnostic is `OFF` by default in `clang` and is controlled using the `-Watimport-in-framework-header` flag. (39192894)
- Previously, omitting the `framework` keyword when declaring a module for a framework didn’t affect compilation but silently did the wrong thing. A new diagnostic, `-Wincomplete-framework-module-declaration`, and a new fix-it suggests adding the appropriate keyword. This warning is on by default when you pass the `-fmodules` flag to `clang`. (39193062)

###### Resolved Issues

- Fixed a data race condition that occurred when checking whether a future has been attached to a promise in `std::async`. The issue was resolved for `std::async` returning a non-void future, however the issue remains for calls that return `std::future<void>`. (42548261)
- Linking is successful even if Incremental LTO is enabled using `-flto=thin` when you invoke `clang` from the command line to compile and link in a single invocation. (47297739)
- Inverted character classes in `std::regex`, such as `[\S]`, are now handled correctly. (43060054)
- `dsymutil` no longer exhausts system memory on large projects. (41422573)

##### Asset Catalog

###### Resolved Issues

- Resolved an issue that affected app compatibility with iOS 9.0, 9.1, and 9.2 when distributing an app for local or enterprise distribution. App asset catalogs built using Xcode 10 with a deployment target of iOS 9.0, 9.1 or 9.2 produced content incompatible with the runtimes of those iOS versions when distributed using local or enterprise distribution. Rebuilding the app with Xcode 10.2 resolves this issue. (46893768, 44535967)
- Image slicing mode is improved in Dark Mode. (39388416)

##### Build System

###### New Features

- Implicit Dependencies now supports finding dependencies in Other Linker Flags for linked frameworks and libraries specified with `-framework`, `-weak_framework`, `-reexport_framework`, `-lazy_framework`, `-weak-l`, `-reexport-l`, `-lazy-l`, and `-l`. (7879587)

###### Known Issues

- If you’re building a framework containing Swift code and using `lipo` to create a binary that supports both device and simulator platforms, you must also combine the generated `Framework-Swift.h` headers for each platform to create a header that supports both device and simulator platforms. (48635615) For example, if you’ve built: - `iOS/Framework.framework`
- `iOS Simulator/Framework.framework` Take:
- `iOS/Framework.framework/Headers/Framework-Swift.h`
- `iOS Simulator/Framework.framework/Framework-Swift.h` Create a new:
- `iOS + iOS Simulator/Framework.framework/Headers/Framework-Swift.h` The contents of the new `Framework-Swift.h` should be: ```objc
#if TARGET_OS_SIMULATOR
<contents of original iOS Simulator/Framework.framework/Framework-Swift.h>
#else
<contents of original iOS/Framework.framework/Framework-Swift.h>
#endif
```

###### Resolved Issues

- External targets are properly ordered when used as a target dependency. (44775299)
- Resolved an issue that caused Xcode to process PNG and JPEG files as TIFF files when the `COMBINE_HIDPI_IMAGES` and `APPLY_RULES_IN_COPY_FILES` settings were enabled. (44623214)
- The `OTHER_INPUT_FILE_FLAGS` build setting—which propagates custom flags for source files—is now available to custom rule scripts when using the new build system. (46067251)
- A recursive inclusion cycle in `.xcconfig` files no longer crashes the build system. (42023748)
- Per-file flags defined for Core Data model files in a target build phase are now passed to the Core Data compiler. (42919919)

##### Clang Static Analyzer

###### Resolved Issues

- The static analyzer now warns when a C++ object is used after its contents are moved unless the object is reset to a known state before it’s used. (41349073)
- The static analyzer now checks for violations of IOKit and libkern reference counting rules. These violations can lead to leaks and use-after-free issues. (46359592)

##### Debugging

###### New Features

- [`UIStackView`](https://developer.apple.com/documentation/UIKit/UIStackView) properties are now presented in the view debugger object inspector. (36351873)
- Xcode can now automatically capture a memory graph if a memory resource exception is encountered while debugging. You can enable memory graph captures in the Diagnostics tab of the scheme’s run settings. (45285932)
- On iOS and watchOS, Xcode shows the memory limit for running apps in the Memory Report as you approach the limit. Use Instruments and Xcode Memory Debugging to optimize your app to have the smallest possible memory footprint. (40556954)
- The view debugger presents a more compact 3D layout. (43523921)

###### Resolved Issues

- The speed of showing disassembly in the Assistant Editor is improved. (31633031)

##### Documentation Viewer

###### New Features

- Documentation for symbols can be filtered by SDK availability, introduced version, and deprecation. Documentation can also be filtered to show only articles or sample code. For example, you can filter the documentation to show all of the sample code in a framework like UIKit. (45236860)

##### Instruments

###### Known Issues

- Instruments may crash when you profile Swift code in a watchOS app. (47368181)

##### Interface Builder

###### New Features

- Double-clicking in a storyboard no longer zooms. Instead, zoom using a pinch gesture on the trackpad or hold Option and scroll. (29139870)
- Interface Builder for Apple TV supports user interface elements exposed by the [`TVUIKit`](https://developer.apple.com/documentation/TVUIKit) framework. (35868606)

###### Resolved Issues

- Fixed a crash that could occur when checking the “Bind to” checkbox in the Bindings inspector after reopening a storyboard. (33348238)
- The rotate button in the Interface Builder preview is visible in Dark Mode. (42396497)
- Actions in Swift files are now correctly parsed by Interface Builder when annotated with `@objc @IBAction`. (25465675)
- Images with an alignment rectangle specified in the asset catalog correctly render in the Interface Builder canvas. (46595020)
- Improved the intrinsic size of images in 2x and 3x slots in the Interface Builder canvas if the file name inside the asset catalog doesn’t end in `@2x` or `@3x`. (44759471)
- Changes to [`NSImageView`](https://developer.apple.com/documentation/AppKit/NSImageView) made using the inspector are now reliably reflected in the canvas without a delay. (30196881)
- `ibtool --export-string-file` includes localizer hints that are specified on controls with instances of [`NSCell`](https://developer.apple.com/documentation/AppKit/NSCell). (24421623)
- Resolved an issue that caused images to display as question marks in storyboards. (42475635)
- Images rendered in the Interface Builder canvas render with the scale factor matching the chosen device. (18703159)
- Images marked with the template rendering mode in the asset catalog correctly render in the Interface Builder canvas. (29049562)

##### Linking

###### Resolved Issues

- Swift libraries are now found in the `dyld` cache when the main project isn’t written in Swift. (48385698)
- Resolved an issue that caused linker errors to display in the issue navigator as “Linker command failed with exit code 1” rather than displaying the actual error message. (39141740)

##### Lldb Debugger

###### New Features

- You can now use `$0`, `$1`, … shorthands in LLDB expression evaluation inside closures. (20719448)
- C variable length arrays are now supported in LLDB. (39606394)
- The LLDB debugger has a new command alias, `v`, for the “frame variable” command to print variables in the current stack frame. Because it bypasses the expression evaluator, `v` can be a lot faster and should be preferred over `p` or `po`. (40066460)

###### Resolved Issues

- The debugger now resolves the type of generic variables that are bound to private types. (38231646)
- Using `po` in Swift while debugging a watchOS app now returns correct results. (47162433)
- Generic variables in inlined generic contexts are now correctly supported by the debugger. (28859432)
- Data formatters for Swift dictionaries and sets are more reliable. (43045289)

##### Localization

###### New Features

- Opening a project that uses any deprecated localization identifiers now produces a warning for each one used. Selecting one of these warnings presents an assistant for migrating files in the associated legacy “lproj” directories to “lproj” directories named for the equivalent modern identifier. If necessary, this process also updates the project’s development region to a modern identifier. Migrated projects are compatible with older versions of Xcode. (9777671)
- You can now export and import localizations for a project’s development region. (41878212)

###### Resolved Issues

- Xcode now more carefully distinguishes between legacy localization identifiers such as “English” and modern localization identifiers such as “en” and represents them both in both project files and the user interface. (45469882)
- Enabling Base Internationalization is recommended for all projects, and any projects that don’t currently use Base Internationalization are offered an upgrade even if they only have a single localization. The upgraded projects are backward-compatible with previous releases of Xcode. (15160454)
- You can now add localizations to a project that doesn’t have any localizable files, and you aren’t prompted for files to copy to the new localization. (42771349)

##### Playgrounds

###### New Features

- Playgrounds now perform memory safety checks at runtime. Code that violates exclusive access to memory traps with the diagnostic message: “Simultaneous accesses to […], but modification requires exclusive access.” ([`SR-8126`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-8126)) (33820622) For more information, see [`Memory Safety`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/MemorySafety.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book).

###### Resolved Issues

- Resolved an issue that prevented playgrounds from executing. (47226381)
- Fixed a crash that could occur when editing playgrounds that use auxiliary sources. (42097728)
- Fixed a crash that could occur when editing snippets that contain placeholders. (43242401)
- Fixed an issue that could prevent changes in Interface Builder documents from being reflected in a playground without closing the workspace window. (46830864)

##### Refactoring

###### Resolved Issues

- The rename refactoring now correctly renames functions that take a single parameter with an external argument label, and that have a call site that passes the corresponding argument as a trailing closure. (42162571)
- Using Refactoring > Rename to rename a document now updates the app’s `Info.plist` file to match. (41327509)

##### Simulator

###### Resolved Issues

- Improved the performance and responsiveness of interactions with simulated devices. (47864185)
- Resolved an issue that prevented booting a simulated device on a Mac with a large number of simulated devices. (47712686)
- Resolved a failure that occurred when dragging multiple contact, photo, or video items onto a simulated device window at the same time. (46736098)
- Pasteboard synchronization between macOS and simulated iOS devices is more reliable. (46817121)
- You’re now only prompted once to authorize microphone access to all simulator devices. (45715977)
- Performance and responsiveness when interacting with simulated iPhone XR devices has been improved. (44657262)

##### Source Control

###### New Features

- Xcode uses SSH configuration output to determine which SSH key pair should be used for authenticating a given remote repository. (47302670)

###### Resolved Issues

- Xcode now supports the use of SSH private keys in the OpenSSH format in addition to the PEM format for connecting to Git servers. (40867126)
- Resolved an issue that caused keychain lookups for an SSH key passphrase to fail. (47578552)

##### Source Editor

###### New Features

- The “Fold Methods & Functions” editor menu item folds computed properties in Swift. (43428274)
- Code completion offers `get`, `set`, `didSet`, and `willSet` as possible completions inside computed property declarations. (20957182)
- In the context of an optional enumeration type, code completion suggests the enumeration’s cases in addition to [`Optional.none`](https://developer.apple.com/documentation/Swift/Optional/none) and [`Optional.some(_:)`](https://developer.apple.com/documentation/Swift/Optional/some(_:)). (23549753)

###### Resolved Issues

- Code completion doesn’t suggest duplicated delegate method names when overriding [`UITableViewController`](https://developer.apple.com/documentation/UIKit/UITableViewController) methods. (21161476)
- Fix-its that reference different files won’t apply to the current file. (31371021)
- Text being dragged is shown as a transparent image. (31890166)
- The source editor now uses the system accent color for placeholders. (32307338)
- The editor won’t fill in a placeholder when typing a newline character directly before the placeholder. (32853933)
- Fixed a crash in Swap with Mark if the line containing the mark had been edited. (41874263)
- Improved typing and scrolling performance in the editor when the folding ribbon is turned on. (42941556)
- Fixed the consistency of line wrapping. (44520372)
- Fixed a crash that occurred when showing three assistant editors. (45230485)
- Fixed a crash that occurred when entering a newline with multiple cursors. (45601228)
- Improved the speed of scrolling a source file with folded code when line wrapping is turned off. (45712602)
- Improved the display of warnings and issues when using dark themes. (44925116)
- Find and Replace using a pattern token replaces the matched text with the replacement text instead of the regular expression of the pattern token. (35439088)
- Resolved issue that caused a text find to also perform the same find in background windows. (38269600)
- Jump to Definition now navigates to the definition of a symbol when the cursor is at the end of that symbol. (33203746)
- Highlighting many instances of the same symbol is faster. (40698496)
- Fixed a crash in Redo with whitespace trimming enabled. (41519769)
- Resolved an issue that caused source code colors to flash during a build. (42749446)
- Jump to Definition displays the file name when listing items from generated system headers. (43581521)
- Fixed crash when that occurred when editing code during the code folding animation. (44555624)
- Resolved a crash that occurred when using Behaviors > File > Unlock > Run script. (44826462)

##### Swift

See [`Swift 5 Release Notes for Xcode 10.2`](swift-5-release-notes-for-xcode-10_2.md).

##### Testing

###### New Features

- `xccov` supports merging multiple coverage reports—and their associated archives—together into an aggregate report and archive. When merging reports together, the aggregate report may be inaccurate for source files that changed in between the time that the original reports were generated. If there were no source changes, the aggregate report and archive will be accurate. For more information, see the `xccov` manual page. (38050969)
- `xccov` now supports diffing Xcode coverage reports, which can be used to calculate coverage changes over time. For example, to diff the coverage reports `before.xccovreport` and `after.xccovreport`, invoke `xccov` as follows: `xccov diff --json before.xccovreport after.xccovreport`. For more information about the format of the diff, see the `xccov` manual page. (43439165)
- Static library and framework targets now appear in the coverage report as top-level entries, with line coverage values that are aggregated across all targets that include the static library or framework. This also resolves an issue where the source files for a static library or framework target would be included in the coverage report even if the target itself was excluded from code coverage in the scheme. (22578123)

###### Known Issues

- Swift initializers appear in the coverage report with no name. (47467864)
- Recording doesn’t work from Clones when Parallelization is on. (43699252)
- The wrong test host app is chosen for a test target when there are multiple test host targets with the same `PRODUCT_NAME`. (46475115)
- Profiling tests don’t behave correctly when test parallelization is enabled. (44836817)  Disable parallel testing while profiling by navigating to Product > Scheme > Edit Scheme > Test > Info, selecting Options next to your test target, and disabling “Execute in parallel”.

###### Resolved Issues

- Resolved an issue that caused methods in a Swift source file to be named “Definition at :” in the coverage report. (46432533)
- [`XCUIScreen`](https://developer.apple.com/documentation/XCTest/XCUIScreen) now properly implements `isEqual:` and `hash`. (32179407)
- When clicking the source editor gem for a test method or class that’s present in more than one test target, or for a test method that’s inherited by subclasses, Xcode now shows a menu that allows choosing an individual target or class (or all) to run the selected tests in. (45975871)
- Resolved an issue that could prevent expanding a file in the coverage report view. (44458167)
- If a test bundle can’t be loaded during testing for some reason—such as a runtime linking failure—Xcode now reports a descriptive error message that describes the cause of the failure. This failure is present in the test activity log and appears in `stdout` if you’re using `xcodebuild`. The error is also present in the structured logs contained in the result bundle. (45242409)
- If testing fails due to the test runner crashing on launch, Xcode attempts to generate a rich error message that describes the failure. This failure is present in the test activity log and appears in `stdout` if you’re using `xcodebuild`. The error is also present in the structured logs contained in the result bundle. (29148418)
- If `xcodebuild` is terminated by a `SIGINT` signal while tests are running, a valid result bundle is written to disk and contains the results from the tests that completed before the termination. Similarly, if you cancel running tests in Xcode, a valid result bundle is generated that contains the results of the already-completed tests. (45022325)
- Second instances of `xcodebuild` or Xcode don’t delete simulator clones created during parallel distributed testing. (40738122)
- Test targets that don’t specify a test host app and use the `xctest` command line tool to run tests now honor customized language and region settings in a scheme’s Test action. (43139603)
- Resolved an issue that could cause incorrect code coverage for a file included in multiple targets. (40409346)
- Crash reports collected during testing no longer omit important fields such as the termination reason and description. (44405884)
- Headers that aren’t explicitly included in a target’s Headers Build Phase no longer appear in the target’s entry in the coverage report. This resolves an issue where unwanted headers could appear in the coverage report for a target—such as from a linked framework or library. If you notice that a coverage report is missing headers, make sure they’re included in the corresponding target’s Headers Build Phase. (36187447)
- Projects with multiple test targets that each contain a test class that inherits from a shared [`XCTestCase`](https://developer.apple.com/documentation/XCTest/XCTestCase) subclass no longer show nonexistent runtime (“rT”) tests for test methods from other targets. (46042417)

## Topics

### Release Notes
- [Swift 5 Release Notes for Xcode 10.2](swift-5-release-notes-for-xcode-10_2.md)
  Update your code to use new language features and test your apps against changes.

## See Also

- [Xcode 10.3 Release Notes](xcode-10_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10.2.1 Release Notes](xcode-10_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10.1 Release Notes](xcode-10_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10 Release Notes](xcode-10-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-10_2-release-notes)*