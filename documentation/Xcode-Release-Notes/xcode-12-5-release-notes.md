# Xcode 12.5 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 12.5 includes SDKs for iOS 14.5, iPadOS 14.5, tvOS 14.5, watchOS 7.4, and macOS Big Sur 11.3. The Xcode 12.5 release supports on-device debugging for iOS 9 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 12.5 requires a Mac running macOS Big Sur 11 or later.

##### General

###### New Features

- You can create macOS File Provider extensions using the new File Provider Extension target template. (54054417)
- The Reveal Build Products Folder item in the Product menu opens Finder and selects the folder where Xcode builds the product. (72248847)

###### Resolved Issues

- Fixed an issue that could cause code completion, live issues, and other code-analysis features to produce incorrect results after you moved any of the source files of an open Xcode project. (57054858)
- Large workspaces now open faster. (70276306)
- Fixed an issue that could cause iOS 12.5, tvOS 14.5, watchOS 7.4, and earlier to set the minimum deployment target based on the app’s [`LSMinimumSystemVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/LSMinimumSystemVersion) instead of its [`MinimumOSVersion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/MinimumOSVersion). (76221112)

###### Deprecations

- Don’t use the iOS `MinimumOSVersion` information property list key to declare the minimum release of macOS in which your app runs. Use `LSMinimumSystemVersion` instead. (73890473) - Future releases of macOS ignore the `MinimumOSVersion` key in Mac apps, including apps built with Mac Catalyst.
- Future releases of macOS use the `LSMinimumSystemVersion` key in iOS apps built with Xcode 12.5 or later. If an iOS app doesn’t include an `LSMinimumSystemVersion` key, future releases of macOS compare the app’s `MinimumOSVersion` with the version of its Mac Catalyst runtime to determine compatibility.

##### Apple Clang Compiler

###### New Features

- libc++ no longer honors the `_LIBCPP_RAW_ITERATORS` macro. Use wrapped iterators instead. (63088925)
- Clang now infers the availability of `+new` from availability annotations on `-init` methods. Since `+new` calls `[[Foo alloc] init]`, `+new` isn’t available unless `+init` is available. (75884815)

##### Build System

###### New Features

- The build system no longer re-signs the hosting app target when building app-hosted test targets; instead it builds test targets before the app target’s sign task runs. This eliminates an extra `codesign` task, which speeds up builds for large apps with such test targets. (47322098)
- `xcodebuild` now supports the `-archive` flag when creating an XCFramework, providing a shorthand method for creating an XCFramework from one or more archives. (64725832) For example: ```None
xcodebuild -archive <archive_path1> -framework MyFramework.framework -archive <archive_path2> -framework MyFramework.framework -o <output_xcframework_path>
```

###### Resolved Issues

- Copy Files Build Phase now properly signs code for embedded frameworks with a framework version that isn’t “A”. (55701162) (FB7323980)
- You can now manually reorder schemes. (61456142)
- `xcodebuild` no longer double-escapes the output of `xcodebuild -showBuildSettings -json`. (63554669)
- Preprocess and Assemble single-file actions now work correctly when analyze-while-building is enabled, and no longer display an empty property list in the source editor. (70811963)
- Fixed a dependency cycle involving hosted test targets when Parallelize Build is disabled. Xcode no longer creates a cycle when the test target depends on another target in addition to the hosting target. (73210420)
- The build system no longer emits a “duplicate tasks” error when both an app and a test target link with the same XCFramework. (74362639) (FB9005738)

##### Code Completion

###### New Features

- Code completion is more reliable in expressions that contain errors, and in expressions that are ambiguous without additional context. (71378252) For example, given: ```swift
func test(a: Int, b: String) -> Int { ... }
func test(a: Int, b: Int) -> String { ... }
func test(a: (Int, Int) -> Int) -> Int { ... }
``` Invoking code completion after `test().prefix(3).` suggests members of String. Invoking code completion after `test(a: 2).` suggests members of Int and String. Invoking code completion after `$0.` in the following block suggests members of Int: ```swift
test {
  $0.
}
```

###### Resolved Issues

- Code completion now returns suggestions more quickly inside large function bodies. (58687608)

##### Debugging

###### New Features

- When debugging C++ programs using libc++, LLDB now offers improved expression evaluation support for STL containers and algorithms. (19866497) - You can call member functions of STL containers, even if they are never called in the target program.
- LLDB can instantiate templated functions from the standard library. This includes algorithms such as `std::sort`, `std::count`, `std::count_if`, and so on.

###### Resolved Issues

- When debugging Swift code, Xcode’s variable view and the `v` (`frame variable`) command now display variables with resilient types including Foundation value types such as `URL`, `URLComponents`, `Notification`, `IndexPath`, `Decimal`, `Data`, `Date`, `Global`, `Measurement`, and `UUID`. (72101693)

###### Known Issues

- Xcode fails to launch apps when Nightstand Mode is enabled on Apple Watch. (61351690) : Disable Nightstand Mode on Apple Watch; Go to Settings > General > Nightstand Mode.

##### Instruments

###### New Features

- `<(start|end)-pattern>` elements in os-signpost-interval schema are now optional. This allows Custom Instruments to match signposts by name and other properties without needing to specify the expected message format. (43850670)
- Profiling XCTest with Instruments now automatically starts the recording, without a click on the record button. (50260328)
- Instruments can now import `os_log` and `os_signpost` data from the ktrace files that include logging-level data. (56037733)
- Custom Instruments can now specify statically defined sub-tracks without needing to be driven by table column data. (61367995)
- `xctrace export` now produces output in time-sorted order. (69804348)
- Table of Contents query for `xctrace` now exposes metadata information about the run. (71320853)

###### Resolved Issues

- Fixed an issue where `xctrace` wouldn’t pass a standard input to the launched process. (17842765)
- Launching an extension via Product > Profile in Xcode no longer causes Instruments to wait indefinitely for the process to start. (62275419) (FB7674284)
- Fixed a crash that sometimes occurred when you started recording after transferring a Metal app from Xcode to Instruments. (70655385) (FB8824932)
- Fixed an issue where plot elements wouldn’t draw using the color column specified in a point schema. (71680467) (FB8913696)

###### Known Issues

- In macOS 11.2 or earlier, `leaks` and other command line analysis tools fail or crash when run against processes built with Mac Catalyst and processes running in iOS 14.5 or later on simulated devices. (74690398)

##### Interface Builder

###### New Features

- You can now configure a Module for custom classes in the inspector for [`NSObjectController`](https://developer.apple.com/documentation/AppKit/NSObjectController) and similar objects. (35971498)

###### Resolved Issues

- [`NSButton`](https://developer.apple.com/documentation/AppKit/NSButton)’s  “Image Only” Position setting now properly displays an image without a title at runtime. (16200971)
- Fixed an issue where the assistant editor wouldn’t display source code for a selected object’s custom Swift class if the class was annotated with `@objc`. (19623315)
- Fixed an issue where connect-to-source wouldn’t properly escape Swift keywords in Outlet and Action names. (22527929)
- Fixed an issue where Editor > Debug Selected Views failed to attach to `@IBDesignable` views for debugging. (45217745) (FB5645911)
- Added Dark Mode support for the connect-to-source bindings popover. (47583413) (FB5701084)
- Fixed iOS canvas appearance issues when importing project images with an unexpected scale. (63789933) (FB7719276)
- Fixed an issue where the assistant editor could open the wrong source file for a selected object’s custom class if duplicate class names existed in the project. (67362709)
- Fixed the canvas drifting when resizing the document outline. (67505701)
- Fixed an issue where selecting the custom color item from an inspector’s color pop-up menu wouldn’t open the system colors picker window. (69365980) (FB8727901)
- Selecting a view in the canvas and performing Select All (Command-A) no longer selects the view’s layout guides. (69518746)
- Fixed an issue where certain connect-to-source popover labels didn’t show up in Dark Mode. (69713404)
- Fixed an issue where the custom colors swatch in an inspector’s color properties displayed an incorrectly offset focus indicator. (72370447)

##### Localization

###### New Features

- You can now use Xcode to localize applications into all ISO 639 languages. (46806165) (FB5359472)
- You can now use workspaces to export a collection of projects for localization, generating a single localization catalog for all projects in the workspace. As part of this change, options to import and export for localization are now in the Product menu instead of  the Editor menu. You can also use `xcodebuild -importLocalizations` and `xcodebuild -exportLocalizations` with the `-workspace` option to export or import a workspace. (48548375)
- The new Localization Export Supported build setting lets you disable localization export for a specific target or project that doesn’t require localization. (66606145)

###### Resolved Issues

- Fixed an issue where the Application Language menu in the scheme editor doesn’t show all languages for which a project is localized. (28872507)
- `*-InfoPlist.strings` files are now renamed to `InfoPlist.strings` at build-time for bundles that require `Info.plist` localization. This is consistent with existing behavior that renames `Info.plist` files at build-time. (38686398)
- Exporting and importing for localization now produces an error if two files (ex: Main.strings and Main.storyboard) write translations to the same path. (39917359, 52412470) (FB6384066)
- Fixed an issue where exporting color sets for localization caused Xcode to crash. (63934393)
- Fixed an issue where new-style multiline Swift string literals weren’t properly extracted for localization. (64652467) (FB7742731)
- Localizable keys in `Info.plist` files are now only automatically extracted on localization export for Application and App Extension targets. (66871236)
- Fixed an issue where strings were replaced with their keys at localization export if the `.strings` file was outside the directory hierarchy of the Xcode project. (69835864) (FB8761502)

##### Playgrounds

###### New Features

- A Playground in an app’s project can now access symbols from the app target. New playgrounds you create have this option on by default. To enable this functionality in existing playground documents, turn on the Import App Types option in the File Inspector. (66357893)
- Inline results for deeply nested Swift arrays and structs now display more information in Xcode Playgrounds. (67344623)

###### Resolved Issues

- Fixed an issue that could cause Xcode to show “No editor” when opening a Playground. (56484197)

##### Previews

###### Resolved Issues

- The [`preferredColorScheme(_:)`](https://developer.apple.com/documentation/SwiftUI/View/preferredColorScheme(_:)) modifier now applies the theme to the nearest enclosing presentation, and its contained views. (62745457)

##### Signing and Distribution

###### Resolved Issues

- Resolved an issue that prevented exporting distribution certificates from Xcode due to a keyboard focus issue in the authentication window. (71011727) (FB8880845)
- Fixed an issue that caused OS X 10.11 and earlier to reject packages signed in macOS 11 or later. (71695608, 75599040)

###### Known Issues

- Xcode doesn’t build projects with a signing certificate on a smart card, or that is accessed via a [`CryptoTokenKit`](https://developer.apple.com/documentation/CryptoTokenKit) extension. (58266781) (FB7516556) : Instead of signing in Xcode or `xcodebuild`, run `codesign` in a post-build step.
- OS X 10.11 or earlier may reject code signatures added to universal binaries by Xcode 12.5 running in macOS 11.2 or earlier. (70724583) (FB8830007) : Specify `--digest-algorithm=sha1,sha256` to the `codesign` utility at signing time. In Xcode, specify this using the `OTHER_CODE_SIGN_FLAGS` build setting.
- If you embed a binary that contains an old code signature in your app, your app may fail to install and launch on devices running iOS 14.5 with the error message “The code signature version is no longer supported.” (77494287) To resolve this issue, first ensure that embedding the binary is necessary for your app to operate. If the binary is a static library, it’s not necessary to embed it. Stop embedding the binary in your app by following these steps: 1. Select your project in the Project Navigator.
2. Select your app’s target from the Targets list.
3. In the General tab, under the Frameworks, Libraries, and Embedded Content section; click the Embed pop-up menu next to your static library, and then choose Do Not Embed. If operating your app requires you to embed the binary, you can update its signature by following the instructions documented at [`Using the latest code signature format`](https://developer.apple.com/documentation/Xcode/using-the-latest-code-signature-format).

##### Simulator

###### New Features

- Simulator now supports recording video from within the app. Hold Option when clicking on the screenshot button in the toolbar (or press Command-R) to record a video. Click the red button to stop video recording. (63041314)
- Simulator can create animated GIFs from video recordings using the new Record Video feature. After recording a video, right-click on the video preview, then select Save as Animated GIF. To keep both the video file and the animated GIF, press and hold Option and select Save Copy as Animated GIF. You can adjust the dimensions and size of the generated GIFs in Simulator Preferences. (65089299)

###### Known Issues

- Siri isn’t available in simulated tvOS devices. (74261184, 75115292)
- Simulator may not respect the I/O > Keyboard > Use the Same Keyboard Language as macOS setting. (74897431)

##### Source Control

###### Resolved Issues

- Fixed an issue where some workspaces could fail to notice project file changes from source control operations until you quit and relaunched Xcode. (3920347)

###### Known Issues

- If you rename the default branch in your remote repository and don’t update `HEAD` to point to the renamed branch, source code operations may fail and Xcode may return an error -100. (76070146) : Use the `git` command line tool to re-point your `HEAD`; for example: ```None
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/<your_default_branch_name>
```

##### Storekit

###### New Features

- StoreKit Testing in Xcode now supports testing of non-renewing subscriptions. (59478394)
- The [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest) framework is now available on watchOS. (68152552)

##### Swift

###### New Features

- Incremental compilation is faster in many cases. When you change code within the body of a struct, class, enum, protocol, or extension, Swift now recompiles far fewer files in that module than before. (51230617)
- Implicit member expressions now support chains of member accesses. (57295228) For example, this code is now valid: ```swift
let milky: UIColor = .white.withAlphaComponent(0.5)
let milky2: UIColor = .init(named: "white")!.withAlphaComponent(0.5)
let milkyChance: UIColor? = .init(named: "white")?.withAlphaComponent(0.5)
``` As is the case with the existing implicit member expression syntax, the resulting type of the chain must be the same as the (implicit) base, so it isn’t well-formed to write `let cgMilky: CGColor = .white.withAlphaComponent(0.5).cgColor` (unless appropriate white and withAlphaComponent members were defined on CGColor.). Members of a “chain” can be properties, method calls, subscript accesses, force unwraps, or optional chaining question marks. Furthermore, the type of each member along the chain is permitted to differ (again, as long as the base of the chain matches the resulting type) meaning the following successfully typechecks: ```swift
struct Foo {
  static var foo = Foo()
  static var bar = Bar()

  var anotherFoo: Foo { Foo() }
  func getFoo() -> Foo { Foo() }
  var optionalFoo: Foo? { Foo() }
  subscript() -> Foo { Foo() }
}

struct Bar {
  var anotherFoo = Foo()
}

let _: Foo? = .bar.anotherFoo.getFoo().optionalFoo?.optionalFoo![]
```
- Swift includes more checks when bridging data from Objective-C. In particular, the runtime library aborts your program with a suitable error message if it detects a non-nullable pointer that contains a null value. (58650899)
- You can now use [`Float16`](https://developer.apple.com/documentation/Swift/Float16) in code running on Apple silicon. (61937297)
- Property wrappers are now supported on local variables. (73377111)
- Functions, subscripts, and initializers may now have more than one variadic parameter. When using variadic parameters, also label the parameter immediately following a variadic parameter. ([`SE-0284`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0284-multiple-variadic-parameters.md), 73676506) This makes declarations like the following valid: ```swift
func foo(_ a: Int..., b: Double...) { }

struct Bar {
  subscript(a: Int..., b b: Int...) -> [Int] { a + b }

  init(a: String..., b: Float...) { }
}
```
- Property wrappers now work in local contexts. (74192307) For example, this code is now valid: ```swift
@propertyWrapper
struct Wrapper<T> {
  var wrappedValue: T
}

func test() {
  @Wrapper var value = 10
}
```
- When you run `swift` with no arguments, it starts a REPL (Read-Eval-Print Loop) that uses LLDB. The Swift compiler no longer contains the integrated REPL for compiler developers (formerly accessible by running `swift -frontend -repl`). (74613702) The Swift compiler still supports running code as a script, for example: ```None
swift myScript.swift
```
- When compiling a type that conforms to a protocol via an extension, Swift takes into account the availability of the extension when forming generic types that use this protocol conformance. (74614358) For example, consider a `Box` type whose conformance to `Hashable` uses features only available on macOS 11: ```swift
public struct Box {}

@available(macOS 11, *)
extension Box : Hashable {
  func hash(into: inout Hasher) {
    // call some new API to hash the value...
  }
}

public func findBad(_: Set<Box>) -> Box {}
// warning: conformance of 'Box' to 'Hashable' is only available in macOS 11 or newer

@available(macOS 11, *)
public func findGood(_: Set<Box>) -> Box {} // OK
``` In the above code, it isn’t valid for `findBad()` to take a `Set<Box>` because `Set` requires that its element type conform to `Hashable`, but the conformance of `Box` to `Hashable` isn’t available before macOS 11. Note that using an unavailable protocol conformance is a warning, not an error, to avoid potential source compatibility issues. In prior releases, you could write code that made use of unavailable protocol conformances but worked anyway — if the optimizer had eliminated all runtime dispatch through this conformance, or the code in question was entirely unreachable at runtime. Protocol conformances can also be marked as completely unavailable or deprecated, by placing an appropriate `@available` attribute on the extension: ```swift
@available(*, unavailable, message: "Not supported anymore")
extension Box : Hashable {}

@available(*, deprecated, message: "Suggest using something else")
extension Box : Hashable {}
``` If a protocol conformance is defined on the type itself, it inherits availability from the type. You can move the protocol conformance to an extension if you need it to have narrower availability than the type.
- The `@available` attribute is no longer permitted on generic parameters, where it had no effect. (74614802) For example: ```swift
struct Bad<@available(macOS 11, *) T> {}
// error: '@available' attribute can't be applied to this declaration

struct Good<T> {} // equivalent
```
- Availability checking now rejects protocols that refine less available protocols. (74615650) Previously, this was accepted by the compiler but could result in linker errors or runtime crashes; for example: ```swift
@available(macOS 11, *)
protocol Base {}

protocol Bad : Base {}
// error: 'Base' is only available in macOS 11 or newer

@available(macOS 11, *)
protocol Good : Base {} // OK
```
- Protocol conformance checking now considers `where` clauses when evaluating if a `typealias` is a suitable witness for an associated type requirement. (74618612) The following code is now rejected: ```swift
protocol Holder {
  associatedtype Contents
}

struct Box<T> : Holder {}
// error: type 'Box<T>' doesn't conform to protocol 'Holder'

extension Box where T : Hashable {
  typealias Contents = T
}
``` In most cases, the compiler would either crash or produce surprising results when making use of a `typealias` with an unsatisfied `where` clause, but it is possible that some previously-working code is now rejected. In the above example, the conformance can be fixed in one of the following ways: - Make it conditional (move the `: Holder` from the definition of `Box` to the extension).
- Move the `typealias` from the extension to the type itself.
- Relax the `where` clause on the extension.

###### Resolved Issues

- Function overloading now works in local contexts, making the following valid: ```swift
func outer(x: Int, y: String) {
  func doIt(_: Int) {}
  func doIt(_: String) {}

  doIt(x)
  doIt(y)
}
``` In this code, the first `doIt(_:)` calls with an Int value, and the second with a String value. (29312676)
- Fixed an issue that occurred when you initialized a floating-point value — such as `Float` or `Double` — from a string representing a number outside the range for the given type. Swift now returns a value of positive or negative `0` or `.infinity` instead of `nil`. (36990878, 76728925) (FB9080490) - Input strings representing values greater than the maximum positive finite normal value now return a value of positive `.infinity`.
- Input strings representing values less than the maximum negative finite normal value now return a value of negative `.infinity`.
- Input strings representing values closer to 0 than to the minimum positive non-zero subnormal value now return a value of `+0`.
- Input strings representing values closer to 0 than to the maximum negative non-zero subnormal value now return a value of `-0`.
- The runtime and compiler support for Swift’s `is`, `as?`, and `as!` operators has been overhauled, providing more consistent and predictable behavior. (58991956)
- If your app (including loaded OS binaries) contains multiple redundant protocol conformances, Swift now uses the first one it finds in the first binary loaded (including in OS binaries). (72049977)
- Fixed a crash that occurred when setting a value using a [`ReferenceWritableKeyPath`](https://developer.apple.com/documentation/Swift/ReferenceWritableKeyPath) that was upcast to a [`WritableKeyPath`](https://developer.apple.com/documentation/Swift/WritableKeyPath). (74191390) (FB8999603)

###### Known Issues

- iOS Playgrounds may crash on initial execution. (70826934) : Re-execute the Playground.
- The compiler may generate incorrect code when you use an `enum` `case` with associated values to satisfy a protocol requirement. (72302307) For example: ```swift
protocol FileHandlerAction {
  static func setFileURL(_ fileURL: NSURL) -> Self
}

enum AppAction : FileHandlerAction {
  case setFileURL(NSURL)
}
``` : Provide a static method to satisfy the requirement: ```swift
enum AppAction : FileHandlerAction {
  case _setFileURL(NSURL)

  static func setFileURL(_ fileURL: NSURL) -> Self {
    return ._setFileURL(fileURL)
  }
}
```

###### Deprecations

- The Swift compiler emits a warning for the use of the `await` keyword as an unqualified identifier. Wrap `await` with back-ticks so Swift always treats it as an identifier, or fully qualify declarations named await. For example, add `self` anytime you reference an instance member named `await` from within the instance. ([`SE-0296`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0296-async-await.md), 67000350)

##### Swift Packages

###### New Features

- Swift packages that specify a 5.4 tools version can now explicitly declare targets as executable, which allows the use of the `@main` keyword in package code. ([`SE-0294`](https://developer.apple.comhttps://forums.swift.org/t/se-0294-declaring-executable-targets-in-package-manifests/42404), 47691185)
- The Swift Package Manager now builds package products and targets as dynamic frameworks automatically, if doing so avoids duplication of library code at runtime. (59931771) (FB7608638)
- Swift Package Manager caches package dependencies on a per-user basis, which reduces the amount of network traffic and increases performance of dependency resolution for subsequent uses of the same package. If needed, you can disable cache use in `xcodebuild` by using the new `-disablePackageRepositoryCache` flag. (72204929)

##### Testing

###### New Features

- XCTest now supports marking test failures as “expected.” Expected test failures don’t impact the overall pass/fail result of the suite containing the test. Xcode displays expected failures differently in the Test Navigator and Test Report, and highlights the line of code where the expected failure occurred along with an optional user description. Expected test failures provide a low-overhead tool for preserving the overall “green” state of a project’s test suite when there are failures which can’t be immediately resolved, ensuring that any new failures are clearly visible. In contrast to skipping a test with [`XCTSkip`](https://developer.apple.com/documentation/XCTest/XCTSkip-swift.struct), a test with an expected failure still runs, reporting any unexpected changes. (13408632) To mark a failure as expected, call the new [`XCTExpectFailure`](https://developer.apple.com/documentation/xctest/3726077-xctexpectfailure) API in a test before the code which produces the test failure, for example: ```swift
XCTExpectFailure("…")
// Perform test which currently fails
``` Additionally, the scope of the expected failure can be limited by enclosing the failing code in a closure: ```swift
// Arrange and act on the test subject

XCTExpectFailure("…") {
    XCTAssert(…) // Failing assertion
}

// Continue test with further assertions etc.
``` By default, if `XCTExpectFailure` is called but the test doesn’t record a failure, XCTest marks the test as having failed due to an “unmatched expected failure.” This can be suppressed for failures which occur non-deterministically, by passing `XCTExpectFailure` an `XCTExpectedFailure.Options` object as a parameter, with its `isStrict` property set to `false`: ```swift
let options = XCTExpectedFailure.Options()
options.isStrict = false
XCTExpectFailure("…", options: options)
// Perform test which sometimes fails
```
- Xcode now allows you to clean test results without having to re-open your workspace by selecting Clean Test Results from Xcode’s Product menu. (16527161)
- Xcode now supports XCTest unit and UI tests for watchOS apps. When creating a new watchOS app, check the Include tests checkbox to add a unit and UI test target to the newly created project. For an existing project, add a unit or UI test target via File > New > Target, and then add the test target to the Test action of the WatchKit App scheme. To run the tests, select a watch simulator or device from the run destinations menu in the toolbar, and then choose Product > Test. Note that testing is supported on watchOS 7.4 or later. (21395998)
- XCTest now automatically includes specialized subclasses of Swift generic test classes when running tests on macOS 11.3, iOS 14.5, tvOS 14.5, watchOS 7.4, or later OS versions. This allows you to use generics to improve reusability of test classes. (23493200)
- XCTest now includes [`XCTAssertIdentical(_:_:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTAssertIdentical(_:_:_:file:line:)) and [`XCTAssertNotIdentical(_:_:_:file:line:)`](https://developer.apple.com/documentation/XCTest/XCTAssertNotIdentical(_:_:_:file:line:)) APIs to assert whether two object instances are identical (the same instance) and are stricter than [`XCTAssertEqual`](https://developer.apple.com/documentation/XCTest/XCTAssertEqual) by using the `===` operator instead of `==` in Swift. (46137782)
- The code coverage report now shows the number of executable lines per file. (68808019)

###### Resolved Issues

- The `message` String parameter of `XCTSkip.init(_:file:line:)` no longer includes `@autoclosure` incorrectly. Unlike its conditional variants [`XCTSkipIf`](https://developer.apple.com/documentation/XCTest/XCTSkipIf) and [`XCTSkipUnless`](https://developer.apple.com/documentation/XCTest/XCTSkipUnless), XCTSkip’s initializer unconditionally evaluates its message string. (63827685)
- If a test times out (due to having Test Timeouts enabled in the active Test Plan), any content that the test emitted to standard out or standard error prior to the timeout is now included in the test log. (64591225)
- Xcode and `xcodebuild` now prevent the computer from sleeping while executing tests. (67493488)
- If code under test crashes, and Xcode is able to collect a crash report, the error message that Xcode generates in the Test Report and Test Log includes the crashing symbol, as well as the Application Specific Information field from the crash report. (69755517)
- Fixed an issue where methods on [`XCTOSSignpostMetric`](https://developer.apple.com/documentation/XCTest/XCTOSSignpostMetric) threw an exception on watchOS. (72552791)
- Xcode no longer incorrectly reports a name that starts with “<unknown>” for tests that the test code dynamically generates at runtime. (73767460)

###### Known Issues

- When running on a Mac with Apple silicon, Xcode doesn’t provide code coverage information for code in Swift packages. (71769076) (FB8919898)
- If you run lengthy uninterrupted CPU-bound computation in a test on Apple Watch devices, watchOS may terminate the test runner. (74301580) : Avoid performing heavy CPU-bound computation in your tests on Apple Watch devices.
- Xcode crashes when you attempt to view test results for an integration. (76126769) : Download the integration’s build logs and open the enclosed result bundle.

###### Deprecations

- Xcode no longer includes XCTest’s legacy Swift overlay library (`libswiftXCTest.dylib`). Use the library’s replacement, `libXCTestSwiftSupport.dylib`, instead. For frameworks that encounter build issues because of the removal of the legacy library, delete the framework and library search paths for `libswiftXCTest.dylib` and add the `ENABLE_TESTING_SEARCH_PATHS=YES` build setting. This setting automatically sets the target’s search paths so that it can locate the replacement XCTest library. (70365050)

## See Also

- [Xcode 12.5.1 Release Notes](xcode-12_5_1-release-notes.md)
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
- [Xcode 12 Release Notes](xcode-12-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-12_5-release-notes)*