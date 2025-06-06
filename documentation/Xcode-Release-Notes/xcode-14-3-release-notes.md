# Xcode 14.3 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 14.3 includes Swift 5.8 and SDKs for iOS 16.4, iPadOS 16.4, tvOS 16.4, watchOS 9.4, and macOS Ventura 13.3. The Xcode 14.3 release supports on-device debugging in iOS 11 and later, tvOS 11 and later, and watchOS 4 and later. Xcode 14.3 requires a Mac running macOS Ventura 13.0 or later.

##### General

###### New Features

- Xcode 14.3 includes a new module verifier that generates diagnostics for issues in a framework’s modules. (97345247)

###### Resolved Issues

- Fixed: Crash logs from App Extensions and extension-based Watch apps weren’t being delivered to the Xcode Organizer. This issue is resolved in iOS 16.4, macOS 13.3, watchOS 9.4 and tvOS 16.4. (90882288)
- Fixed: You can now use Xcode’s documentation viewer to view Xcode documentation or view it on the web at [`https://developer.apple.com/documentation/Xcode`](https://developer.apple.comhttps://developer.apple.com/documentation/Xcode). (102522035)

###### Deprecations

- Xcode isn’t supported under Rosetta.  See Developer Technote [`“Resolving architecture build errors on Apple silicon“`](https://developer.apple.comhttps://developer.apple.com/documentation/technotes/tn3117-resolving-build-errors-for-apple-silicon) for more information. (92772361)

##### Apple Clang Compiler

###### New Features

- Clang and the build system support a new mode for building module dependencies called explicit modules which improves build performance, reliability, and correctness. The new mode is opt-in, and can be enabled by setting `_EXPERIMENTAL_CLANG_EXPLICIT_MODULES` as a user-defined build setting in C and Objective-C projects which build with modules enabled. (104438594)
- The following C++23 features have been implemented: - New support for multidimensional subscript operator. (P2128R6)
- Relaxed restrictions on the presence of non-literal variables (and labels and gotos) in constexpr functions (P2242R3).
- Introduce auto(x) for decay-copy in the language (P0849R8). (104887755)
- The `-ffp-model=strict` is fully supported for the ARM architecture. The generated code adheres to the IEEE-754 standard. Specifically, floating point exceptions and rounding modes are handled according to the standard. `#pragma STDC FENV ACCESS` is supported.  By default, `-ffp-contract=ON` is set. This option enables shorter and faster floating-point code by fusing floating point operations like multiplies and adds, but it may impact the accuracy of numerically sensitive applications. (105573336)

###### Resolved Issues

- Fixed: The compiler no longer emits erroneous warnings for images included into Objective-C documentation comments using the `<img/>` tag. (91464292)
- Fixed: Standard C++ modules are disabled in ObjectiveC++ with the C++ language mode set to C++20. This doesn’t impact Clang modules. (104670658)

##### Build System

###### New Features

- Xcode now prompts a user prior to performing a clean action. This prompt can be bypassed by holding the option key while performing a clean, or by permanently hiding the prompt by enabling the “Don’t Ask Me” setting within the prompt. (98914489)

###### Resolved Issues

- Fixed: UI test targets no longer force `SWIFT_SERIALIZE_DEBUGGING_OPTIONS` to `YES` at build time, and respect that setting being overridden in the project. (94845934)
- Fixed: Run scripts in a scheme’s pre-actions and post-actions for the Build section now cause the build to fail if any run script exits with a non-zero exit code, instead of reporting a false-positive successful build. (102896200)

###### Known Issues

- Previews in packages can fail when previewing inside of a package that is both the dependent of a package and the dependency of a package when used by an app. (103716225)  Create and select a scheme targeting just that package when using SwiftUI previews for a file in that package.
- When a pre-build scheme action (such as compiling a package plugin) encounters an error, the status message at the top of Xcode’s workspace window sometimes doesn’t update.  This leaves the previous status showing, possibly causing confusion if the previous status was “Build Succeeded.” (104306342)
- Previews in packages can fail when previewing inside of a package that is both the dependent of a package and the dependency of a package when used by an app. (104683595)  Create and select a scheme targeting just that package when using SwiftUI previews for a file in that package.

##### C++ Standard Library

###### New Features

- The following new features have been implemented: - P0896R4 - The One Ranges Proposal
- P1004R2 - Making `std::vector` constexpr
- P0627R6 - Function to mark unreachable code
- P1165R1 - Make stateful allocator propagation more consistent for `operator+(basic_string)`
- P0674R1 - Support arrays in `make_shared` and `allocate_shared`
- P0980R1 - Making `std::string` constexpr
- LWG3659 - Consider `ATOMIC_FLAG_INIT` undeprecation
- P1423R3 - `char8_t` backward compatibility remediation
- `std::pop_heap` now uses an algorithm known as “bottom-up heapsort” or “heapsort with bounce” to reduce the number of comparisons, and rearranges elements using move-assignment instead of `std::swap`.
- `std::boyer_moore_searcher` and `std::boyer_moore_horspool_searcher` have been implemented. (104702784)

###### Deprecations

- The following items have been deprecated: - The `<experimental/filesystem>` header has been removed. Instead, use the `<filesystem>` header. The associated macro `_LIBCPP_DEPRECATED_EXPERIMENTAL_FILESYSTEM` has been removed too.
- The C++14 function `std::quoted(const char*)` is no longer supported in C++03 or C++11 modes.
- `std::function` has been removed in C++03. If you are using it, please remove usages or upgrade to C++11 or later.
- `std::unary_function` and `std::binary_function` are no longer available in C++17 and C++20. They can be re-enabled by defining `_LIBCPP_ENABLE_CXX17_REMOVED_UNARY_BINARY_FUNCTION`. They are also marked as `[[deprecated]]` in C++11 and later. To disable deprecation warnings you have to define `_LIBCPP_DISABLE_DEPRECATION_WARNINGS`. Note that this disables all deprecation warnings.
- The contents of `<codecvt>`, `std::wstring_convert` and `std::wbuffer_convert` have been marked as deprecated. To disable deprecation warnings you have to define `_LIBCPP_DISABLE_DEPRECATION_WARNINGS`. Note that this disables all deprecation warnings.
- The integer distributions `std::binomial_distribution`, `std::discrete_distribution`, `std::geometric_distribution`, `std::negative_binomial_distribution`, `std::poisson_distribution`, and `std::uniform_int_distribution` now conform to the Standard by rejecting template parameter types other than `short`, `int`, `long`, `long long`, and the unsigned versions thereof. As an extension, `int8_t`, `__int128_t` and their unsigned versions are supported too. In particular, instantiating these distributions with non-integer types like `bool` and `char` won’t compile anymore. (105097623)

##### Debugging

###### Resolved Issues

- Fixed: When stopped in a C++11 lambda body in an enclosing class method, LLDB now supports evaluating expressions containing members of the captured ‘this’ pointer. (50140179)
- Fixed: LLDB is now more resilient against Swift module deserialization failures that previously would have ended the the debug session. (64511878)

##### Documentation

###### New Features

- The documentation toolchain for Objective-C has migrated to the open-source Clang extract-api tool. (101761719)

##### Driverkit

###### New Features

- Clang now automatically initializes uninitialized local variables on the stack to zero for DriverKit extensions. (99166509)

##### Instruments

###### New Features

- When attempting to launch an application using Instruments on a locked target device, Instruments now prompts the user and waits for the unlock to happen instead of presenting an error. (41464216)
- `xctrace export` now supports requesting binary image load information for processes in a trace file. Each image includes a path, UUID, name, load address and architecture. (76676504)
- Stores Inspector located in the Instruments Inspector now allows for copying example `xctrace export` command after invoking the shortcut menu on a listed store. (89078433)
- `xctrace export` now includes parsable description of backtraces recorded in an Instruments trace. Each frame inside the backtrace includes a VM address and a symbol name (if present). (95850764)
- The “File → Symbols” UI has been updated to make symbolication workflows more streamlined: - Better display/filtering of process and image lists
- More information about each loaded image, including UUIS, version, load address and load time.
- Easier resymbolication with an ‘Add Symbols’ button, allowing selection of multiple dSYMs at once. (97920704)
- Heaviest Stack Trace UI in the Extended Detail now allows for copying mangled names of symbols using shortcut menu. (98017107)
- Graph and Detail elements specified in the Instruments Package can now be disabled based on the value of a trace parameter. (101357705)
- The Heaviest Stack Trace UI has a new contextual menu for showing frames as a load address and binary offset. (102116922)
- os-signpost-interval-schema now exposes a way to bind a CLIPS variable to a duration field of a signpost interval and use it as part of other column definitions. (102447071)

###### Resolved Issues

- Fixed: Instruments’ launch time performance is now improved. Launching the application should be up to 3 times faster. (12219587)
- Fixed: Selecting ‘Open in Xcode’ from an Instruments Source Viewer now opens the selected file in an existing workspace. (76846286)
- Fixed: ‘Open in Xcode’ action of a Source Viewer now preserves line and text range selection when transitioning between Instruments and Xcode. (91005085)
- Fixed: Improved reliability of interaction with the find field when invoked on the detail view. (94526531)
- Fixed an issue where entering multiple filter tokens in a Call Tree view and selecting ‘All’ matching would still result in matching any of the specified tokens. (97454950)
- Fixed an issue where scrolling horizontally in a Call Tree view using trackpad wasn’t possible. (97752177)
- Fixed: Source View now automatically opens Disassembly View when no source code is available for a selected symbol. (99206757)
- Fixed: Performance of adding a new Instrument from the library to an existing trace document has been significantly improved. (100873173)
- Fixed an issue in the CPU Counters Instrument where `RETIRE_UOP` events wouldn’t be counted on Apple Silicon machines. (101330117)

##### Interface Builder

###### New Features

- The “Introduced Variations Based On:” inspector popup will now remember the last picked size class and variation settings. (98647372)
- The enabled property is configurable on UISearchBar through the attribute inspector. (101423711)

###### Resolved Issues

- Fixed: The Line Break Strategy can now be configured on a NS/UITextView paragraph style popup inspector and UILabel’s attributes inspector. (70369164)
- Fixed: The SF Symbol library search results have improved to include search terms besides the name of the symbol. For example, searching for “writing” will also show related “pencil” SF symbols. (94857888)
- Fixed an issue that prevented the Reveal in Editor button, in the custom class inspector, from revealing the class in the source code editor. (100136260)
- Fixed an issue that prevented XIBs containing only User Defined Runtime Attributes from loading at runtime. (100357502)
- Fixed: Xcodebuild supports a `-downloadPlatform <watchOS|tvOS>` argument to request downloading a single platform. (100869261)
- Fixed: Safe Area dimensions in landscape mode are now positioned correctly in the canvas. (101164646)
- Fixed an issue where frames sometimes shift when a storyboard is opened. (102221237)
- Fixed an issue with the resizing cursor not showing when attempting to resize a `NSViewController`. (102609072)

##### Localization

###### New Features

- You can now specify the default localization of an Xcode project. Configure it from the language list in the project editor’s Info tab. (4886288)

###### Resolved Issues

- Fixed an issue when exporting a project for localization, where referenced projects might not be exported. (91126400)

##### Playgrounds

###### Known Issues

- Manual execution mode for Xcode Playgrounds may fail. (104976410)

##### Signing and Distribution

###### Resolved Issues

- Fixed: Xcode automatic signing now creates managed provisioning profiles for Developer ID. This resolves an issue that caused Xcode to throw an error when cloud signing with a Developer ID certificate during the app distribution workflow. (90026719)
- Fixed: Resolved an issue when distributing apps that use Game Center. If necessary, Xcode automatic signing can now enable the Game Center feature on your app ID during distribution. (103426363)

##### Simulator

###### Resolved Issues

- Fixed: When simulating a user gesture in the iOS simulator, loading a WebView may cause a black box to appear on the entire screen. (107143140)

###### Known Issues

- Repeated Build & Run targeting iOS 16.1 and later simulator runtimes may sometimes result in a hung launch. (101990080)  Reboot the simulator device and reattempt the launch.

##### Source Control

###### Resolved Issues

- Fixed: Xcode’s Git integration now supports mailmap. Users who have changed their names or email addresses can set up a `.mailmap` file in their repository and Xcode now displays the correct canonical name on commits and branch history. (62682973)
- Fixed: Re-added support for perl compatible regular expressions to `git grep`. (101318680)
- Fixed: Addressed security vulnerabilities CVE-2022-23521 and CVE-2022-41903. (102376850)

###### Known Issues

- The branch history view may display an incomplete branch history in rare cases. (96024292)  Select a different branch, then, once again, select the desired branch.

##### Source Editor

###### New Features

- Improved code completion ranking for Swift. (98687334)

##### Storekit

###### New Features

- The [`StoreKit Test`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest) framework now supports testing SKAdNetwork 4.0. (91782868)

##### Swift

###### New Features

- The `@backDeployed(before:)` attribute may now be used to extend the availability of a function to OS releases prior to the introduction of that function as ABI. For example, suppose that `struct Temperature` was introduced in a macOS SDK framework in macOS 12. Later in macOS 13 the framework authors decided to add a `degreesFahrenheit` property as a convenience: ```swift
@available(macOS 12, *)
public struct Temperature {
  public var degreesCelsius: Double
  
  // ...
}

extension Temperature {
  @available(macOS 12, *)
  @backDeployed(before: macOS 13)
  public var degreesFahrenheit: Double {
    return (degreesCelsius * 9 / 5) + 32
  }
}
``` Adding the `@backDeployed` attribute to `degreesFahrenheit` enables the framework author to make this new declaration available to apps with a minimum deployment target of macOS 12, even though the ABI entry point for `degreesFahrenheit` is only present in macOS 13 and up. When a function with `@backDeployed` is called, the compiler wraps the invocation of the function in a thunk. The thunk checks whether the library entry point for the declaration is available at runtime, and invokes it if it is. Otherwise, a copy of the function that was emitted into the client is called instead. [`SE-0376`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0376-function-back-deployment.md) (105198323)
- Сollection downcasts in cast patterns are now supported. For example: ```swift
func collectionDowncast(_ arr: [Any]) {
  switch arr {
  case let ints as [Int]:
    // ...
  case is [Bool]:
    // ...
  }
}
``` (105198506)
- The API of `UnsafeMutableRawPointer`, `UnsafeMutableBufferPointer`, `UnsafeMutableRawBufferPointer` were improved, adding previously missing initialization (and deinitialization) methods, including more performant initialization from `Collection` types. For `UnsafeMutablePointer<T>` and `UnsafeMutableBufferPointer<T>`, method names containing the word “assign” were renamed to use the word “update”, and many more were added. Every multi-element initialization method of `UnsafeMutablePointer` and `UnsafeMutableBufferPointer` now has a corresponding “update” method. Slices of `UnsafeBufferPointer`, `UnsafeRawBufferPointer`, `UnsafeMutableBufferPointer` and `UnsafeMutableRawBufferPointer` now share the collection-like API of their base type. For example, given an initialized `b: UnsafeMutableBufferPointer<Int>`, the following lines are synonymous: ```swift
b.update(repeating: 0)
b[b.startIndex..<b.endIndex].update(repeating: 0)
``` [`SE-0370`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0370-pointer-family-initialization-improvements.md) (105198642)
- Implicit `self` is now permitted for `weak self` captures, after `self` is unwrapped. For example, the usage of implicit `self` below is permitted: ```swift
class ViewController {
  let button: Button

  func setup() {
      button.tapHandler = { [weak self] in
          guard let self else { return }
          dismiss() // refers to `self.dismiss()`
      }
  }

  func dismiss() { ... }
}
``` In Swift 5 language modes, implicit `self` is permitted for `weak self` captures in  closures even before `self` is unwrapped. For example, this code compiles successfully in Swift 5 language mode: ```swift
class ExampleClass {
  func makeArray() -> [String] {
    // `Array.map` takes a non-escaping closure:
    ["foo", "bar", "baaz"].map { [weak self] string in
      double(string) // implicitly refers to `self!.double(string)`
    }
  } 

  func double(_ string: String) -> String {
    string + string
  }
}
``` In Swift 6, the above code will no longer compile. `weak self` captures in non-escaping closures now have the same behavior as captures in escaping closures (as described in SE-0365). Code relying on the previous behavior will need to be updated to either unwrap `self` (e.g. by adding a `guard let self else return` statement), or to use a different capture method (e.g. using `[self]` or `[unowned self]` instead of `[weak self]`). [`SE-0365`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0365-implicit-self-weak-capture.md) (105198849)
- The compiler flag `-enable-upcoming-feature X` can now be used to enable a specific feature `X` that has been accepted by the evolution process, but whose introduction into the language is waiting for the next major version (e.g., version 6). The `X` is specified by any proposal that falls into this category: - `ConciseMagicFile` enables the new `#file` semantics in [`SE-0274`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0274-magic-file.md).
- `ForwardTrailingClosures` disables the “backward” scanning behavior of [`SE-0286`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0286-forward-scan-trailing-closures.md).
- `BareSlashRegexLiterals` enables the regex literal syntax of [`SE-0354`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0354-regex-literals.md). Features can be detected in source code with `#if hasFeature(X)`. [`SE-0362`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0362-piecemeal-future-features.md) (105198978)

###### Resolved Issues

- Fixed an occasional crash when suspending at an `await` in apps using Swift concurrency running on macOS 12.3 and earlier, on iOS 15.4 and earlier, watchOS 8.5 and earlier, and tvOS 15.4 and earlier. (101299662)
- Fixed: The Swift compiler may fail to build modules for XCFramework dependencies that were built with `BUILD_LIBRARY_FOR_DISTRIBUTION` enabled. These failures will occur when the XCFramework contains public Swift declarations that have `@MainActor` constraints implicitly added, such as subclasses of `UIView` or `NSView`. The Swift compiler expects those declarations to be marked `@available` for an operating system version where Swift concurrency is available. (105610970)

##### Swift Packages

###### New Features

- A proper diagnostic is shown instead of an ambiguous error when a tool needed by a plugin isn’t supported on the target platform. (91000836)
- Packages with duplicate product names are now allowed. Note this only applies to the command-line builds. (94744134)
- Implemented [`SE-0378`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0378-package-registry-auth.md), which adds support for token authentication for package registry requests. (99716571)
- Binary targets can now directly be vended as products without requiring the declaration of an additional source target. (101096803)
- SwiftPM now supports piecemeal adoption of upcoming Swift language improvements per [`SE-0362`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0362-piecemeal-future-features.md). (104718540)

###### Resolved Issues

- Fixed: Conditional target dependencies ([`SE-0273`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0273-swiftpm-conditional-target-dependencies.md)) in packages are now correctly applied to binary targets and leads to top-level targets being filtered out from builds of root packages. (85762201)
- Fixed: Removed implicit availability of `Foundation` from package manifests using tools-version 5.8 or later. An explicit import of Foundation is now required if APIs from Foundation are used in a manifest. (92879696)
- Fixed: When a pre-build command depends on tools that aren’t prebuilt binaries, it showed an ambiguous error message. The fix was added to show proper diagnostics. (94712361)
- Fixed: A proper diagnostic is shown instead of an ambiguous error when a plugin has a dependency on non-supported products or targets. (95117424)
- Fixed: Resolved an error that sometimes caused package resolution to fail with a message similar to: `An unknown error occurred. reference 'refs/remotes/origin/main' not found (-1)`. (100387832)
- Fixed: When package graph resolution fails, Xcode now shows a build failure rather than letting the build start and then fail with errors about missing build products. (101835157)
- Fixed: Warnings and errors associated with packages are now shown under the packages to which they apply in the package resolution log. (102879707)
- Fixed multiple bugs that could cause a “Unable to resolve build file: XCBCore.BuildFile” build error when using packages. (102912126)

###### Known Issues

- When a package build tool plugin generates a build command for a particular input file, that file is considered to have been handled by the plugin and isn’t passed to the build system. If the input file is a source code file (such as a Swift or Objective-C source file), it won’t be compiled into the product being built. (102789077)

##### Swiftui Previews

###### New Features

- `print` output now appears in the console for SwiftUI Previews by selecting “Preview” tab in the console. Currently output is limited to Swift’s `print` function. (96569171)

###### Resolved Issues

- Fixed: Previews can fail when previewing a file inside of a Swift package target that is the dependency of an executable target. (97630721)
- Fixed: Previews may fail in the Xcode canvas when previewing two files side-by-side when only one of them is in a Swift Package. (99296071)
- Fixed: Previews can fail when previewing inside of a target that is the dependency of a target where previewing is not supported such as an XPC service or static library. (99707713)
- Fixed: Previews could fail in Swift Packages with binary dependencies. (99936678)
- Fixed: Previews can fail when using Swift Concurrency in an app with a minimum deployment target of <= iOS 14.0. (99969698)
- Fixed: Some kinds of crashes of previews don’t appear in the canvas. (100586176)
- Fixed: Previewing files that exist both in a widget target and an application target can fail. (101221314)
- Fixed: Previews can fail when using opaque types as the generic parameter of another type in the return type of `body`. (101832285)
- Fixed: Previews can fail when previewing inside of apps that have an app identifier that differs from the bundle identifier. (102753115)

##### Testing

###### New Features

- Xcode now defaults to using a test plan for new projects. The test plan is marked as “Auto-created” and can be viewed and modified in the Test Plan Editor. To change an Auto-created Test Plan, a user will need to first save it to disk. This can be done by making a change in the Test Plan Editor, and then migrating the file to an on-disk representation with the on-screen prompts, or by explicitly saving the Auto-created Test Plan from within the Test Plan Editor. (97048381)
- The `timeout` argument of `XCTestCase.wait(for:timeout:enforceOrder:)` and related methods is now optional—if you don’t specify it, the function waits indefinitely (until the overall test times out.) To ensure reasonable execution time, set an appropriate value for the `executionTimeAllowance` property of the running `XCTestCase` instance (`self`). (100811826)

###### Resolved Issues

- Fixed: Errors thrown by `async` Swift test methods, as well as `async` `setUp` or `tearDown` methods, now show the source location where they were thrown when symbol information is present, and include a higher-fidelity description. (72813349)
- Fixed: If test timeouts are enabled in the test plan and a test observer is registered with the shared `XCTestObservationCenter`, the observer’s `-testCaseWillStart:` and `-testCaseDidFinish:` methods now count towards each test’s time allowance. This allows the harness to prevent hangs that could occur in the observer’s implementation of these methods. (78408785)
- Fixed: `XCTestCase.wait(for:timeout:enforceOrder:)` and related methods are now marked unavailable in concurrent Swift functions because they can cause a test to deadlock. Instead, you can use the new concurrency-safe `XCTestCase.fulfillment(of:timeout:enforceOrder:)` method. (91453026)
- Fixed: A test plan’s “Collect Diagnostics on Failure” setting now takes effect when tests are built using `xcodebuild build-for-testing` and run with `xcodebuild test-without-building`. (93053592)
- Fixed: Issues recorded in a later `setUp` or `tearDown` after an earlier `setUp` or `tearDown` used `XCTSkip` will no longer mark the test a failure. (93536791)
- Fixed: When an error is thrown during the execution of an `async` Swift test method or an `async` `setUp` or `tearDown` method, but is caught before returning from that method, XCTest avoids constructing a description of the error since doing so may be unsafe. (98847718)
- Fixed: Test targets contained in a test plan whose configurations have different sanitizers enabled (e.g. Address Sanitizer is enabled in one configuration, and Thread Sanitizer is enabled in another configuration) can now execute in parallel on macOS destinations (if the targets’ ‘Execute in Parallel’ checkboxes are checked). (99448030)
- Fixed: Result bundles downloaded from Xcode Cloud can now be linked back to their corresponding builds in the Xcode Test Report.  Users on Xcode 14.3 and later should be able to navigate to the build by right-clicking on the result bundle in the navigation panel and using the “Open in Xcode Cloud” option. (100152213)
- Fixed: A number of Swift code coverage bugs have been fixed. Most notably, code coverage should now correctly work in -O builds. (100327359)
- Fixed: `XCTKeyPathExpectation` now emits a warning when an asynchronous predicate function is used with a non-Sendable observed object. (102092338)

###### Known Issues

- When attempting to launch an application in a watchOS UI test under Xcode Cloud, the test may fail with an error message that the application `has not loaded accessibility`. (90334748)
- Adding an auto-created test plan as part of a Run, Profile, Analyze, or Archive action leads to a crash when the project file is re-opened. (90378346)  Delete the scheme that was modified within the xcshareddata directory.
- Swift files aren’t displaying code coverage data after running tests in the coverage report. (104935416)
- Manually adding, then removing a test plan, to a project that has an auto-created test plan causes the Test Navigator to display “No Test Plan” even though an auto-created test plan is actually backing the project. (105433014)  Close and re-open the project.
- Sometimes adding a test plan to a scheme results in the test plan not being listed within the scheme or test navigator on a subsequent project opening. (105455341)  Open and close the Scheme Editor to cause Xcode to persist changes to the Scheme’s contents to the .xcscheme file backing it.

##### Ui Testing

###### New Features

- You can now set a simulated location for your device to use in real time, or retrieve the simulated location that was previously set. (18825683)
- You can now open a URL using a specified application, or tell the device to open a URL using the default application for it. (21387710)
- You can now get or set the light or dark appearance mode of your device. (81016755)

###### Resolved Issues

- Fixed: Ensured orientation lock is disabled if the user requests the orientation to change during a UI test. (98693525)
- Fixed: Improvements have been made in auto-dismissal of single-button alerts. (102036701)

##### Xcode Cloud

###### Resolved Issues

- Fixed: Xcode Cloud workflows using Xcode 14.3 now correctly report build warnings and static analyzer issues encountered while building Xcode projects. (99978366)

###### Known Issues

- Connecting Slack may not complete successfully when using Xcode’s UI to connect. (106153362)  Connect Slack from Xcode Cloud’s web UI.

##### Xcode Previews

###### New Features

- When using Xcode Previews, any `print()` output will be logged to the debug console. (71080261)

## See Also

- [Xcode 14.3.1 Release Notes](xcode-14_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14.2 Release Notes](xcode-14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14.1 Release Notes](xcode-14_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14.0.1 Release Notes](xcode-14_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 14 Release Notes](xcode-14-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-14_3-release-notes)*