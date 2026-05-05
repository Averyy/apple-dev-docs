# Xcode 26.4 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 26.4 includes Swift 6.3 and SDKs for iOS 26.4, iPadOS 26.4, tvOS 26.4, macOS 26.4, and visionOS 26.4. Xcode 26.4 supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 8 and later, and visionOS. Xcode 26.4 requires a Mac running macOS Tahoe 26.2 or later.

##### General

###### New Features

- Xcode source editor extensions display the localized name via the CFBundleName from the Info.plist of the extension bundle.  (139574330) (FB15741224)
- Added the ability to enable package traits on dependencies from the Package Dependencies view.  (141748785)

###### Resolved Issues

- Fixed: In the project editor, holding the Option key while selecting an xcconfig file affects every build configuration.  (139901429)

##### Address Sanitizer

###### Known Issues

- Address Sanitizer and Thread Sanitizer might hang on macOS 26.4, iOS 26.4, tvOS 26.4, watchOS 26.4, and visionOS 26.4 when building with Xcode 26.3 or older.  (171762808) **Workaround:** Use Xcode 26.4 when testing applications with Address Sanitizer or Thread Sanitizer.

##### Apple Clang Compiler

###### New Features

- The following C++26 features have been implemented: - Structured Bindings can introduce a Pack ([`P1061R10 `](https://developer.apple.comhttps://wg21.link/P1061R10))
- Structured binding declaration as a condition ([`P0963R3`](https://developer.apple.comhttps://wg21.link/P0963R3))
- Variadic Friends ([`P2893R3`](https://developer.apple.comhttps://wg21.link/P2893R3))
- constexpr placement new ([`P2747R2`](https://developer.apple.comhttps://wg21.link/P2747R2))
- The Oxford variadic comma ([`P3176R1`](https://developer.apple.comhttps://wg21.link/P3176R1))  (169138392)

##### Build System

###### New Features

- Mergeable libraries that do not need to access resources via standard Bundle APIs can set `SKIP_MERGEABLE_LIBRARY_BUNDLE_HOOK` to avoid extra launch time overhead.  (162620119)

##### C++ Standard Library

###### New Features

- The following C++ papers have been implemented: - Cleaning-up `noexcept` in the Library ([`N4258`](https://developer.apple.comhttps://wg21.link/N4258))
- Deprecate POD ([`P0767R1`](https://developer.apple.comhttps://wg21.link/P0767R1))
- Integration of `chrono` with text formatting ([`P1361R2`](https://developer.apple.comhttps://wg21.link/P1361R2))
- A type trait to detect reference binding to temporary (implemented the type traits only) ([`P2255R2`](https://developer.apple.comhttps://wg21.link/P2255R2))
- Fixing locale handling in `chrono` formatters ([`P2372R3`](https://developer.apple.comhttps://wg21.link/P2372R3))
- `constexpr` Stable Sorting ([`P2562R1`](https://developer.apple.comhttps://wg21.link/P2562R1))
- Put `std::monostate` in `<utility>` ([`P0472R3`](https://developer.apple.comhttps://wg21.link/P0472R3))
- A Standard `flat_set` ([`P1222R4`](https://developer.apple.comhttps://wg21.link/P1222R4))
- `aligned_accessor`: An `mdspan` accessor expressing pointer over-alignment ([`P2897R7`](https://developer.apple.comhttps://wg21.link/P2897R7))
- Deprecate the notion of trivial types ([`P3247R2`](https://developer.apple.comhttps://wg21.link/P3247R2))
- `constexpr` containers and adaptors (`forward_list`, `list`, `priority_queue`, `flat_map`, and `flat_set` are implemented) ([`P3372R3`](https://developer.apple.comhttps://wg21.link/P3372R3))
- `views::join_with` ([`P2441R2`](https://developer.apple.comhttps://wg21.link/P2441R2))
- Making multi-param constructors of views explicit ([`P2711R1`](https://developer.apple.comhttps://wg21.link/P2711R1))
- Stashing stashing iterators for proper flattening ([`P2770R0`](https://developer.apple.comhttps://wg21.link/P2770R0))
- `common_reference_t` of `reference_wrapper` Should Be a Reference Type ([`P2655R3`](https://developer.apple.comhttps://wg21.link/P2655R3)) Performance improvements: - The `std::ranges::{copy, copy_n, copy_backward, move, move_backward, rotate}` algorithms have been optimized for `std::vector<bool>::iterator`, resulting in a performance improvement of up to 2000x.
- The `std::ranges::equal` algorithm has been optimized for `std::vector<bool>::iterator`, resulting in a performance improvement of up to 188x.
- The `std::ranges::swap_ranges` algorithm has been optimized for `std::vector<bool>::iterator`, resulting in a performance improvement of up to 611x.
- The `num_put::do_put` integral overloads have been optimized, resulting in a performance improvement of up to 2.4x.
- The `std::stable_sort` algorithm uses radix sort for floating-point types now, which can improve the performance up to 10x, depending on type of sorted elements and the initial state of the sorted array.
- The segmented iterator optimization for `std::for_each` has been backported to C++11. It was previously only available in C++23 and later.
- The `std::for_each_n`, `std::ranges::for_each` and `std::ranges::for_each_n` algorithms have been optimized for segmented iterators, resulting in major improvements for `std::deque` and `std::join_view`.
- The `bitset::to_string` function has been optimized, resulting in a performance improvement of up to 8.3x for bitsets with uniformly distributed zeros and ones, and up to 13.5x and 16.1x for sparse and dense bitsets, respectively.
- The `flat_map::insert` and flat_set::insert_range have been optimized, resulting in a performance improvement of up to 10x for inserting elements into a flat_map when the input range is a flat_map or a zip_view.
- `ctype::tolower` and `ctype::toupper` have been optimized, resulting in a 2x performance improvement. Miscellaneous improvements: - As an experimental feature, Hardening now supports assertion semantics that allow customizing how a hardening assertion failure is handled. The four available semantics, modeled on C++26 Contracts, are `ignore`, `observe`, `quick-enforce` and `enforce`. The `observe` semantic is intended to make it easier to adopt Hardening in production but should not be used outside of this scenario. Please refer to the Hardening documentation for details.
- Updated formatting library to Unicode 16.0.0.  (171666816)

###### Deprecations

- The following items have been deprecated or removed: - `std::is_pod` and `std::is_pod_v` are deprecated in C++20 and later.
- `std::is_trivial` and `std::is_trivial_v` are deprecated in C++26 and later.
- The `_LIBCPP_VERBOSE_ABORT_NOT_NOEXCEPT` macro has been removed, making `std::__libcpp_verbose_abort` unconditionally `noexcept`.
- libc++ no longer adds `constexpr` to `std::hash<std::vector<bool, A>>::operator()`, as the `constexpr` addition since C++20 was an unintended extension.
- The non-conforming extension `packaged_task::result_type` has been removed. Potentially breaking changes: - The implementation of `num_put::do_put` has been replaced to improve the performance, which can lead to different output when printing pointers.
- User-defined specializations of `std::common_reference` are diagnosed now. To customize the common reference type, use `std::basic_common_reference` instead.
- `std::function` used to have allocator support, which was removed from the Standard by [`P0302R1`](https://developer.apple.comhttp://wg21.link/p0302r1) due to issues with its design and inconsistent support across implementations. Previously, libc++ would provide allocator-aware APIs in `std::function` in C++11 and C++14, but otherwise ignore the allocator argument. Starting in this release, the allocator argument is always ignored. ABI Affecting Changes: - The Known Issue mentioned in the Xcode 26 release notes relating to ABI break in `std::unordered_{map,set,multimap,multiset}` (159096032), expected to happen in rare cases, has been resolved, reverting to the ABI used in Xcode versions before 26.  (171666856)

##### Coding Intelligence

###### Resolved Issues

- Fixed issue where externally configured MCP servers were being overwritten during Codex initialization.  (169570663)
- Fixed: When using external development tools that connect to Xcode, you may see multiple “Allow Connection?” dialogs during normal usage.  (170721057)

##### Instruments

###### New Features

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
- Added a new instrument to help developers track bandwidth and latencies in the Foveated Streaming system.  (169292516)

###### Resolved Issues

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

###### Deprecations

- The “Compress Run Data” setting has been removed. Trace files now always compress their data to reduce disk usage.  (166901106)

##### Localization

###### New Features

- You can now remove languages from the String Catalog editor. When doing so, you can choose between removing the language from just that catalog or from the entire project.  (16787816)
- When adding a new supported language in the Project Editor, you can now pre-fill your project’s String Catalogs with translations from an existing language.  (101444725)
- String Catalogs now support cut, copy, paste, and duplicate operations on strings. This can be used within the same catalog file or between catalogs. When pasting a string, you can choose between adding the pasted string and all its translations as a new key, or pasting its translations onto an existing key.  (105867829)
- Exported strings extracted from code inside static libraries and executables will now be marked as `translate="no"` since those targets do not have resource bundles in which to store strings.  (159158499)
- A new build setting, `BUILD_ONLY_KNOWN_LOCALIZATIONS`, allows limiting built localized content to the set of localizations listed in the Project Editor. When enabled, excluded languages will be displayed less prominently in String Catalogs.  (161096326)
- When removing a supported language from the Project Editor, you now have the option of either removing all localized content in that language or only from the language list. When choosing the former, translations in all String Catalogs will also be removed for that language. You may want to choose the latter if you are using the `BUILD_ONLY_KNOWN_LOCALIZATIONS` build setting.  (161249725)
- Strings will no longer be extracted from code comments by default. If your project relies on this, you can re-enable by setting `LOCALIZED_STRING_CODE_COMMENTS` to `YES`.  (166593358)

###### Resolved Issues

- Fixed: Xcode and `xcstringstool` no longer extract strings from source code when it can prove that they are DEBUG-only or otherwise would never be compiled into a customer product. This also applies to NSLocalizedString extraction in both Swift and Objective-C.  (102888380)
- Fixed: Export Localizations will now wait for any ongoing comment generation to complete so that these comments make it into the exported Localization Catalog.  (119735093)
- Fixed: Xcode is now smarter about removing strings from String Catalogs when they were moved to a different table.  (125499866) (FB13700089)
- Fixed an issue where strings might get deleted from String Catalogs when they are still present in Objective-C code in some target that is not part of the current scheme.  (154802760)
- Fixed: String Catalog format specifier diagnostics are now more reliable for varied strings using substitutions.  (155084336) (FB18619046)
- Fixed: Generated code for String Catalog symbol generation will no longer produce a compiler error for projects that default to MainActor isolation.  (165481673) (FB21179782)
- Fixed: String Catalog refactor operations for converted to and from generated symbols are now more reliable for multi-line string literals.  (168202035)

###### Known Issues

- When removing a language from a String Catalog in a Swift Package, it could re-appear.  (169263836)

##### Signing and Capabilities

###### Resolved Issues

- Fixed: Applications with the Enhanced Security Capability no longer crash on OS versions prior to 26.0. Applications that have already adopted the capability should remove the following existing entitlements from their entitlements file. - `com.apple.security.hardened-process.enhanced-security-version`
- `com.apple.security.hardened-process.platform-restrictions` And add new variants with string values: - `com.apple.security.hardened-process.enhanced-security-version-string` with value `”1”`
- `com.apple.security.hardened-process.platform-restrictions-string` with value `”2”`  (168185600)

##### Simulator

###### Resolved Issues

- Fixed: When exporting simulator runtimes through xcodebuild, Xcode will save an “.exportBundle” directory. This bundle contains metadata for securely importing the simulator when using `xcodebuild --importPlatform`. Example: ```None
 xcodebuild -downloadPlatform iOS -exportPath /tmp/mySimRuntimes/
 // Saves an exported simulator runtime with a similar name: /tmp/mySimRuntimes/iossimulator_<version>.exportedBundle
 
 xcodebuild -importPlatform /tmp/mySimRuntimes/iossimulator_<version>.exportedBundle
``` (166834291)
- Fixed: Simulator runtime dyld shared caches are once again being created automatically to improve boot time performance. Performance will be degraded while runtimes are being scanned and caches being built.  The `simctl runtime dyld_shared_cache update --all` command can be used to ensure that all caching has completed.  (170836966)
- Fixed: Resolved an issue with simdiskimaged jetsam-looping which could manifest as `simctl` or `xcodebuild -runFirstLaunch` hanging or failures to install simulator runtimes from within Xcode.  (172343027)

##### Source Editor

###### New Features

- Improved editor-tab retention behavior when an external program, such as git, removes and/or adds files while Xcode is running.  (144153298)

##### Storekit

###### Resolved Issues

- Fixed: The StoreKit configuration file does not autosave some changes causing undo commands to fail, and spuriously presenting a prompt stating that the file has been changed by another application.  (169182677)

##### Swift Package Manager

###### Resolved Issues

- Fixed: `swift test` can now successfully include sanitizers via the `--sanitize` flag when selecting specific tests to run via the `--filter` flag.  (168234231)

##### Swift Standard Library

###### Resolved Issues

- Fixed: The raw span accessor properties of `Span` and `MutableSpan` (`bytes` and `mutableBytes`) as well as the two generic `append()` methods of `OutputRawSpan` are newly marked with `@unsafe`. These changes are corrections for omissions in the SE-0458, SE-0467 and SE-0485 proposals or their implementations. These `@unsafe` annotations are required because of a permissible compiler optimization involving values of types that contain padding. When the compiler stores such a value to addressable memory, it is free to skip any padding bytes. This can potentially leave those bytes uninitialized. This optimization is safe when the memory is only ever read as the same type as the value stored. However, when reinterpreting the memory as raw bytes, the potentially uninitialized bytes violate the prerequisite that `RawSpan` and `MutableRawSpan` represent fully initialized memory. In the case of `OutputRawSpan`, they violate the postcondition that the memory it has written is fully initialized. It is safe to use `bytes` when the `Element` type of `Span` or `MutableSpan` has neither internal nor trailing padding bytes, as every byte is then known to be initialized. The same constraint applies to the type parameter of `OutputSpan.append(_:as:)`. To safely use `MutableSpan`’s `mutableBytes`, an additional safety constraint applies when the memory is to later be used again as `Element`. In that case, the non-padding bytes of `Element` must allow every bit pattern to be permissible in a valid value of `Element`.  (168547924)

##### Swiftc++ Interoperability

###### New Features

- Warnings are re-enabled for functions annotated with SWIFT_RETURNS_RETAINED or SWIFT_RETURNS_UNRETAINED but do not return a SWIFT_SHARED_REFERENCE type  (154261051)
- You can now use the `SWIFT_COPYABLE_IF(...)` macro to import a type as copyable or non-copyable depending on its template arguments.  (158852663)
- You can now initialize a Swift `String` from a C++ `std::wstring` and vice versa.  (159272493)

###### Resolved Issues

- Fixed: Swift compiler no longer emits extraneous warnings about functions returning a template type variable that are annotated with SWIFT_RETURNS_RETAINED or SWIFT_RETURNS_UNRETAINED  (160862498)

###### Deprecations

- Initializing `std::string` with an optional Swift `String?` has been deprecated.  (148041893)

##### Testing

###### New Features

- Swift Testing now supports attaching images directly to tests. You can attach instances of `CGImage`, `NSImage`, `UIImage`, and `CIImage`.  (154869058)
- Swift Testing adds support for specifying a Severity when recording an Issue.  (164426789)
- If an error occurs while saving an attachment from either XCTest or Swift Testing into a test report, Xcode will now report that error as a runtime issue.  (164584225)
- Crashes from applications that were interacted XCUIApplications(bundleIdentifier:) or XCUIApplications(url:) are reported as warnings with attached crashlog  (166401942)
- When you call an XCTest or Swift Testing assert within a test from the opposite framework, you will see a runtime issue with warning severity if the assertion failed.  (169220281)

###### Resolved Issues

- Fixed: When adding or removing test targets in an Xcode test plan, the file contents maintain a stable sort order.  (132043612)
- Fixed: Attachments are not recorded from within the bodies of exit tests when using Swift Testing.  (149242118)
- Fixed: When a `#require` expectation within a `withKnownIssue()` closure fails, only one issue will be recorded.  (153550847)
- Fixed: The test report now reports more precise duration numbers for Swift Testing test runs, instead of rounding to the nearest second.  (156722522)
- Fixed: If you cancel the current task while running a test written with Swift Testing, the effect was previously undefined. Swift Testing will now treat the test as cancelled. (If the test is parameterized, cancelling the current task will cancel only the current test case.)  (159150449)
- Fixed: Xcode now reports tests as skipped when the `XCTSkip` API is used with an Objective-C override of the class-level `+setUp` method on an XCTestCase subclass.  (159894325)
- Fixed: When running unit test targets with no host application, the test runner is now consistently launched with a default working directory of `/tmp`, from both Xcode and xcodebuild.  (162549425)
- Fixed: XCTest now clears expectations that were created but not waited upon by the end of a test. Previously, an unwaited notification expectation could be invoked in unrelated tests.  (167529925)
- Fixed: When an issue occurs in a Swift Testing test in a detached task or background thread, it may be recorded as a warning instead of as an error.  (170161483)
- Fixed: Interoperability between XCTest and Swift Testing is no longer enabled by default. To enable this experimental feature, set the environment variable `SWIFT_TESTING_XCTEST_INTEROP_MODE` to `limited` in your test plan. ([`ST-0021`](https://developer.apple.comhttps://github.com/swiftlang/swift-evolution/blob/main/proposals/testing/0021-targeted-interoperability-swift-testing-and-xctest.md))  (171360625)

###### Known Issues

- When an XCTest class has the property `continueAfterFailure` set to false, a failure in an test method, `setUp`, or `tearDown` that is also declared `async` will skip any remaining retries for the current test. For example, if an affected test uses the “retry on failure” repetition mode, it will not attempt to re-run the test after failing.  (108565878) **Workaround:** In your test plan, set “Relaunch Tests for Each Repetition” to on.
- Instances of `UIImage` cannot be attached to tests when testing a Mac Catalyst app.  (168320788) **Workaround:** Use the `UIImage.cgImage` property to get the underlying `CGImage` and attach it instead.
- When using Xcode for Apple silicon, tests which use Swift Testing may crash at launch when using a Rosetta run destination.  (170347005) **Workaround:** Use Xcode Universal.

##### Xcode Organizer

###### Resolved Issues

- Fixed: A backend issue affected Xcode Organizer metrics and diagnostics for iOS 26.3.1 users. This issue has been addressed. Developers with significant iOS iOS 26.3.1 user bases will see corrected metrics over the next few weeks.  (172773750)

## See Also

- [Xcode 26.5 RC Release Notes](xcode-26_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.4.1 Release Notes](xcode-26_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
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