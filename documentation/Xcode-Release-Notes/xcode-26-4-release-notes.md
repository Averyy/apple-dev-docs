# Xcode 26.4 Beta 2 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 26.4 beta 2 includes Swift 6.3 and SDKs for iOS 26.4, iPadOS 26.4, tvOS 26.4, macOS 26.4, and visionOS 26.4. Xcode 26.4 beta 2 supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 8 and later, and visionOS. Xcode 26.4 beta 2 requires a Mac running macOS Tahoe 26.2 or later.

##### Apple Clang Compiler

###### New Features

- The following C++26 features have been implemented: - Structured Bindings can introduce a Pack ([`P1061R10 `](https://developer.apple.comhttps://wg21.link/P1061R10))
- Structured binding declaration as a condition ([`P0963R3`](https://developer.apple.comhttps://wg21.link/P0963R3))
- Variadic Friends ([`P2893R3`](https://developer.apple.comhttps://wg21.link/P2893R3))
- constexpr placement new ([`P2747R2`](https://developer.apple.comhttps://wg21.link/P2747R2))
- The Oxford variadic comma ([`P3176R1`](https://developer.apple.comhttps://wg21.link/P3176R1))  (169138392)

##### Coding Intelligence

###### Known Issues

- When using external development tools that connect to Xcode, you may see multiple “Allow Connection?” dialogs during normal usage.  (170721057)

##### Instruments

###### New Features

- Added a new instrument to help developers track bandwidth and latencies in the Foveated Streaming system.  (169292516)

##### Localization

###### Known Issues

- When removing a language from a String Catalog in a Swift Package, it could re-appear.  (169263836)

##### Source Editor

###### New Features

- Improved editor-tab retention behavior when an external program, such as git, removes and/or adds files while Xcode is running.  (144153298)

##### Storekit

###### Resolved Issues

- Fixed: The StoreKit configuration file does not autosave some changes causing undo commands to fail, and spuriously presenting a prompt stating that the file has been changed by another application.  (169182677)

##### Testing

###### Resolved Issues

- Fixed: When an issue occurs in a Swift Testing test in a detached task or background thread, it may be recorded as a warning instead of as an error.  (170161483)

###### Known Issues

- When an XCTest class has the property `continueAfterFailure` set to false, a failure in an test method, `setUp`, or `tearDown` that is also declared `async` will skip any remaining retries for the current test. For example, if an affected test uses the “retry on failure” repetition mode, it will not attempt to re-run the test after failing.  (108565878) **Workaround:** In your test plan, set “Relaunch Tests for Each Repetition” to on.
- Instances of `UIImage` cannot be attached to tests when testing a Mac Catalyst app.  (168320788) **Workaround:** Use the `UIImage.cgImage` property to get the underlying `CGImage` and attach it instead.
- When using Xcode for Apple silicon, tests which use Swift Testing may crash at launch when using a Rosetta run destination.  (170347005) **Workaround:** Use Xcode Universal.

#### Updates in Xcode 264 Beta

##### General

###### New Features in Xcode 264 Beta

- Xcode source editor extensions display the localized name via the CFBundleName from the Info.plist of the extension bundle.  (139574330) (FB15741224)
- Added the ability to enable package traits on dependencies from the Package Dependencies view.  (141748785)

###### Resolved Issues in Xcode 264 Beta

- Fixed: In the project editor, holding the Option key while selecting an xcconfig file affects every build configuration.  (139901429)

##### Build System

###### New Features in Xcode 264 Beta

- Mergeable libraries that do not need to access resources via standard Bundle APIs can set `SKIP_MERGEABLE_LIBRARY_BUNDLE_HOOK` to avoid extra launch time overhead.  (162620119)

##### Coding Intelligence

###### Resolved Issues in Xcode 264 Beta

- Fixed issue where externally configured MCP servers were being overwritten during Codex initialization.  (169570663)

##### Instruments

###### New Features in Xcode 264 Beta

- New Run Comparison feature allows to compare call trees with other runs using View → Detail Area → Compare With… or the ⇆ button in the jump bar. After selecting which run you want to compare with, the comparison view allows you to view which functions took more or less time between the runs. Call tree filtering operations like “Charge to callers” allow you to focus in on the functions that are faster or slower.  (160223363)
- Top Functions is a new, top-level mode of a Call Tree view allowing to quickly identify the most expensive functions in the trace, no matter where they’re called from. To access Top Functions, select rightmost button in the Call Tree navigation bar.  (123702178)
- The new summary appears in the Call Tree in the bottom right corner, and selections made in the Call Tree will be summarized according to the parameter used to sort the call tree.  (130524732)
- A new “Hide Inlined Functions” option in the “Call Tree” menu at the bottom of the window hides inlined functions and charges their samples to the functions they were inlined into.  (136686776)
- When selecting Call Tree nodes marked as “deduplicated_symbol”, extended detail view will now present a list of candidate symbols that were merged together by the linker.  (139236366)
- CPU samples that exceeded the kernel tracing limit will now be prefixed by a frame labeled “Partial Backtrace”.  (148380087)
- Opened Power Profiler trace captured on a device now features a breakdown of CPU activity by a CPU Core.  (156099947)
- Files that Instruments imports (.atrc, logarchive, …) can now be imported into the same trace document using File -> Import As Run… workflow. Each file will be represented as a separate run in the sidebar.  (160231616)
- `xctrace import` now allows for importing multiple files into the same trace document by using –append-run argument and specifying existing trace path.  (160231771)
- When pasting text to token fields, new lines can be used to separate tokens.  (167801826)
- The context path control has been redesigned to increase discoverability of click areas.  (167877589)

###### Resolved Issues in Xcode 264 Beta

- Fixed an issue where adding instrument for a next recording would cause empty instrument track to be visible for previous precordings.  (60606472)
- Fixed: Double-clicking a function in the flame graph did not open the source viewer.  (118585471)
- Fixed: Expansion state would not be restored when changing the selected time range, or after saving and reopening a trace.  (124091434)
- Fixed: Context menus in the flame graph would only show options for a single node if multiple were selected  (127676581)
- Fixed: Some system processes could not be attached to and profiled.  (132692578) (FB14533469)
- Fixed: The flame graph only showed a percentage for each function call, not the actual weight.  (132833803)
- Fixed: The flame graph did not automatically resize when its content and the window size changed (FB16461572, FB16461629, FB16461652)  (144391013) (FB16461572)
- Fixed: Source Viewer would start out sorting by the first weight column rather than the selected sort order in the call tree.  (153854565)
- Fixed: When a dSYM is applied, Instruments will now resymbolicate all the recorded runs instead of only the currently selected one.  (156646808)
- Fixed: View and view controller representables would sometimes show up as “Other Updates”  (157683632)
- Fixed an issue where Instruments would become unresponsive when opening trace files from long recording sessions or processes with high thread activity.  (158238232)
- Fixed: Low color contrast in the flame graph made it difficult to read function names.  (159136212)
- Fixed a crash that occasionally occurred when recording in immediate mode.  (162787157)
- Fixed: Detail Filter resets when using Call Tree “Focus on Subtree” feature  (163147651)
- Fixed: When Invert Call Tree was enabled, self weight would show on the root frame (like `main`) instead of the leaf frame.  (163359511)
- Fixed an issue where recording Animation Hitches Instrument with Metal Performance Overview would result in an unrecoverable error.  (163798878)
- Fixed a bug where the static initializers were missing the module name in the dyld activity instrument.  (164533028)
- Fixed: SwiftUI updates categorized under “unknown view” are now labeled with “Root View” and the type of the root view they belong to.  (165167491)
- Fixed: Find was not available in the source viewer  (166171514)
- Fixed: Resolved an issue where the source viewer may not show disassembly when the selected function was inlined into a different function in several ranges.  (166330190)
- Fixed: Plot titles now utilize all available space instead of being aggressively truncated.  (167625819)

###### Deprecations in Xcode 264 Beta

- The “Compress Run Data” setting has been removed. Trace files now always compress their data to reduce disk usage.  (166901106)

##### Localization

###### New Features in Xcode 264 Beta

- You can now remove languages from the String Catalog editor. When doing so, you can choose between removing the language from just that catalog or from the entire project.  (16787816)
- When adding a new supported language in the Project Editor, you can now pre-fill your project’s String Catalogs with translations from an existing language.  (101444725)
- String Catalogs now support cut, copy, paste, and duplicate operations on strings. This can be used within the same catalog file or between catalogs. When pasting a string, you can choose between adding the pasted string and all its translations as a new key, or pasting its translations onto an existing key.  (105867829)
- Exported strings extracted from code inside static libraries and executables will now be marked as `translate="no"` since those targets do not have resource bundles in which to store strings.  (159158499)
- A new build setting, `BUILD_ONLY_KNOWN_LOCALIZATIONS`, allows limiting built localized content to the set of localizations listed in the Project Editor. When enabled, excluded languages will be displayed less prominently in String Catalogs.  (161096326)
- When removing a supported language from the Project Editor, you now have the option of either removing all localized content in that language or only from the language list. When choosing the former, translations in all String Catalogs will also be removed for that language. You may want to choose the latter if you are using the `BUILD_ONLY_KNOWN_LOCALIZATIONS` build setting.  (161249725)
- Strings will no longer be extracted from code comments by default. If your project relies on this, you can re-enable by setting `LOCALIZED_STRING_CODE_COMMENTS` to `YES`.  (166593358)

###### Resolved Issues in Xcode 264 Beta

- Fixed: Xcode and `xcstringstool` no longer extract strings from source code when it can prove that they are DEBUG-only or otherwise would never be compiled into a customer product. This also applies to NSLocalizedString extraction in both Swift and Objective-C.  (102888380)
- Fixed: Export Localizations will now wait for any ongoing comment generation to complete so that these comments make it into the exported Localization Catalog.  (119735093)
- Fixed: Xcode is now smarter about removing strings from String Catalogs when they were moved to a different table.  (125499866) (FB13700089)
- Fixed an issue where strings might get deleted from String Catalogs when they are still present in Objective-C code in some target that is not part of the current scheme.  (154802760)
- Fixed: String Catalog format specifier diagnostics are now more reliable for varied strings using substitutions.  (155084336) (FB18619046)
- Fixed: Generated code for String Catalog symbol generation will no longer produce a compiler error for projects that default to MainActor isolation.  (165481673) (FB21179782)
- Fixed: String Catalog refactor operations for converted to and from generated symbols are now more reliable for multi-line string literals.  (168202035)

##### Signing and Capabilities

###### Resolved Issues in Xcode 264 Beta

- Fixed: Applications with the Enhanced Security Capability no longer crash on OS versions prior to 26.0. Applications that have already adopted the capability should remove the following existing entitlements from their entitlements file. - `com.apple.security.hardened-process.enhanced-security-version`
- `com.apple.security.hardened-process.platform-restrictions` And add new variants with string values: - `com.apple.security.hardened-process.enhanced-security-version-string` with value `”1”`
- `com.apple.security.hardened-process.platform-restrictions-string` with value `”2”`  (168185600)

##### Simulator

###### Resolved Issues in Xcode 264 Beta

- Fixed: When exporting simulator runtimes through xcodebuild, Xcode will now save them out as a .exportBundle to included metadata to help with secure importing. That bundle can be directly imported with xcodebuild’s importPlatform command. ```None
 xcodebuild -downloadPlatform iOS -exportPath /tmp/mySimRuntimes/
 // Saves an exported simulator runtime with a similar name: /tmp/mySimRuntimes/iossimulator_<version>.exportedBundle
 
 xcodebuild -importPlatform /tmp/mySimRuntimes/iossimulator_<version>.exportedBundle
``` (166834291)

##### Swift Package Manager

###### Resolved Issues in Xcode 264 Beta

- Fixed: `swift test` can now successfully include sanitizers via the `--sanitize` flag when selecting specific tests to run via the `--filter` flag.  (168234231)

##### Swiftc++ Interoperability

###### New Features in Xcode 264 Beta

- Warnings are re-enabled for functions annotated with SWIFT_RETURNS_RETAINED or SWIFT_RETURNS_UNRETAINED but do not return a SWIFT_SHARED_REFERENCE type  (154261051)
- You can now use the `SWIFT_COPYABLE_IF(...)` macro to import a type as copyable or non-copyable depending on its template arguments.  (158852663)
- You can now initialize a Swift `String` from a C++ `std::wstring` and vice versa.  (159272493)

###### Resolved Issues in Xcode 264 Beta

- Fixed: Swift compiler no longer emits extraneous warnings about functions returning a template type variable that are annotated with SWIFT_RETURNS_RETAINED or SWIFT_RETURNS_UNRETAINED  (160862498)

###### Deprecations in Xcode 264 Beta

- Initializing `std::string` with an optional Swift `String?` has been deprecated.  (148041893)

##### Testing

###### New Features in Xcode 264 Beta

- Swift Testing now supports attaching images directly to tests. You can attach instances of `CGImage`, `NSImage`, `UIImage`, and `CIImage`.  (154869058)
- Swift Testing adds support for specifying a Severity when recording an Issue.  (164426789)
- If an error occurs while saving an attachment from either XCTest or Swift Testing into a test report, Xcode will now report that error as a runtime issue.  (164584225)
- Crashes from applications that were interacted XCUIApplications(bundleIdentifier:) or XCUIApplications(url:) are reported as warnings with attached crashlog  (166401942)
- When you call an XCTest or Swift Testing assert within a test from the opposite framework, you will see a runtime issue with warning severity if the assertion failed.  (169220281)

###### Resolved Issues in Xcode 264 Beta

- Fixed: When adding or removing test targets in an Xcode test plan, the file contents maintain a stable sort order.  (132043612)
- Fixed: Attachments are not recorded from within the bodies of exit tests when using Swift Testing.  (149242118)
- Fixed: When a `#require` expectation within a `withKnownIssue()` closure fails, only one issue will be recorded.  (153550847)
- Fixed: The test report now reports more precise duration numbers for Swift Testing test runs, instead of rounding to the nearest second.  (156722522)
- Fixed: If you cancel the current task while running a test written with Swift Testing, the effect was previously undefined. Swift Testing will now treat the test as cancelled. (If the test is parameterized, cancelling the current task will cancel only the current test case.)  (159150449)
- Fixed: Xcode now reports tests as skipped when the `XCTSkip` API is used with an Objective-C override of the class-level `+setUp` method on an XCTestCase subclass.  (159894325)
- Fixed: When running unit test targets with no host application, the test runner is now consistently launched with a default working directory of `/tmp`, from both Xcode and xcodebuild.  (162549425)
- Fixed: XCTest now clears expectations that were created but not waited upon by the end of a test. Previously, an unwaited notification expectation could be invoked in unrelated tests.  (167529925)

## See Also

- [Xcode 26.3 Release Notes](xcode-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.2 Release Notes](xcode-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.1.1 Release Notes](xcode-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.0.1 Release Notes](xcode-26_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26 Release Notes](xcode-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-26_4-release-notes)*