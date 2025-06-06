# Xcode 13.3 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 13.3 includes SDKs for iOS 15.4, iPadOS 15.4, tvOS 15.4, watchOS 8.5, and macOS Monterey 12.3. The Xcode 13.3 release supports on-device debugging for iOS 15.4, iPadOS 15.4, tvOS 15.4, watchOS 8.5 and later. Xcode 13.3 requires a Mac running macOS Monterey 12 or later.

##### App Store Integration

###### Resolved Issues

- Mitigated several Log4J 2 vulnerabilities by updating Log4J 2 jar files to version 2.17.1. See [`https://logging.apache.org/log4j/2.x/security.html`](https://developer.apple.comhttps://logging.apache.org/log4j/2.x/security.html). (86489820)

##### Apple Clang Compiler

###### New Features

- Several C++20 and C++2b papers have been implemented: - `using` declaration can now be used for enums, enum classes, and their members.
- The compiler can deduce the `size_t` and `ssize_t` types based on new literal suffixes (`uz`, `z`), for example `for (auto i = 0uz; i < vector.size(); ++i) {}`.
- If a lambda declaration takes no parameters, the open and close parentheses () can now be omitted in all contexts including mutable lambdas.
- Duplicate attributes are now allowed by the compiler.
- Any trailing whitespace after `\` is non-significant.
- Concatenations of string-literals with different encoding prefixes are now ill-formed, for example, `auto s = L"" U"";`. (89022082)

###### Resolved Issues

- Clang now follows the C++ standard’s `[intro.progress]` requirement. As a result, the compiler can remove infinite loops without side effects. Consider using `-fno-finite-loops` if your code has infinite loops without observable side effects that the compiler must preserve. (84717970)

###### Known Issues

- Exporting an app that uses Swift’s concurrency features from an archive with bitcode might fail when the app targets iOS 13.0 – iOS 14.7, watchOS 6.0 – watchOS 7.6, or tvOS 13.0 – 14.7. (89271047) : Either uncheck the box `Rebuild from bitcode` when exporting the app from an archive or disable bitcode (iOS only).
- Code that uses 16-byte (128-bit) atomic compare/exchange operations (for example with C++ `std::atomic::compare_exchange_*`) on ARM64 processors may corrupt the atomic variable if you do not use the return value. (88127379) : Assign the result to a `volatile` local variable.

##### Build System

###### New Features

- The build system and Swift compiler have a new mode that better utilizes available cores, resulting in faster builds for Swift projects. The mode is opt-in, and you can enable it globally with the following user default: ```shell
defaults write com.apple.dt.XCBuild EnableSwiftBuildSystemIntegration 1
``` Please report any issues with the new build system mode through Feedback Assistant. (87898478)

###### Resolved Issues

- Fixed a crash that occurred when building projects containing file paths with non-ASCII characters. (83694706)
- Xcode no longer passes `-stdlib=libstdc++` to Clang, because Clang no longer supports that library on Apple platforms. If your project defines the `CLANG_CXX_LIBRARY` build setting, remove it because it no longer does anything. (83768231)
- Building and uploading nonconsumable in-app purchase content for Apple to host is no longer supported. Existing content that’s hosted by Apple isn’t affected. To enable smaller app bundles, faster downloads, and richer app content, use on-demand resources to host your content on the App Store separately from the app bundle. For details, see [`On-Demand Resources Essentials`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/index.html). (84121695)
- Fixed an issue where the number of total build tasks in the status bar continued to increase when repeatedly rebuilding a project after a failed or canceled build. (42333715) (FB5714215)
- The Objective-C modernizer is now supported when using the new build system. (45011912) (FB5530174)
- Fixed: Xcode SwiftUI Previews occasionally fails with an error message about a modified `.h` file, such as “file `Header.h` has been modified since the module file `Module.pcm` was built: `mtime` changed.” (85938686)
- The build system no longer incorrectly reports a successful build when an input to a build task is missing. (86028889)
- Fixed: Apple Watch app targets may fail to build in the `ValidateEmbeddedBinary` step with the error message: “error: The value of CFBundleShortVersionString in your WatchKit app’s Info.plist (1.0) does not match the value in your companion app’s Info.plist ((null)). These values are required to match.” (89240826)

##### Debugging

###### New Features

- When compiling with optimizations turned off, the Swift compiler and Clang no longer eliminate redundant branch instructions on ARM64 targets. This improves debuggability by enabling more breakpoint locations, at the expense of producing slightly larger binaries when compiling with `-Onone`. (79515454)

###### Resolved Issues

- Fixed an issue where Playgrounds sometimes fails to execute when importing frameworks from the workspace by using the “Build active scheme” option. (85431564)

##### Devices

###### Resolved Issues

- Fixed: Activating an iOS and watchOS pair from the Devices and Simulator window causes Xcode to crash. (89262466)

##### Documentation

###### New Features

- Xcode can now build documentation from your Swift code in executable targets, like apps and command-line tools. (79155998) (FB9156246)

###### Resolved Issues

- Fixed an issue where symbol declarations unintentionally included access level modifiers like “public” and “open”. (85280786)

##### Instruments

###### New Features

- Improved the accuracy of leak scanning in Instruments, Xcode’s memory graph debugger, and the `leaks` command line. The system now scans object references inside multi-payload enum cases more accurately, allowing more precise memory leak analysis and the identification of strong, weak, and unowned reference types. (33836721)
- `xctrace` now has the ability to symbolicate previously captured trace files with user-specified dSYMs. Please see `man xctrace` or `xctrace help symbolicate` for details and syntax examples. For example: ```None
xctrace symbolicate --input input.trace --output symbolicated.trace --dsym SomeLibrary.dSYM
```

(47648946) (FB5647641)

- Instruments now has less of an effect on an application’s launch, making metrics gathered with the App Launch template more representative of its actual behavior. (62136401)
- `atos` now allows for symbolicating addresses in the form of binary offsets in cases where the `-offset` flag is provided or when no load address or slide is specified. For example: ```None
atos -arch arm64 -o Example.app/Contents/MacOS/Example 0x00fdae30
```

(75121237)

- Instruments removed the Console view from trace documents. To see output and errors during a trace, add the stdout/stderr instrument from the library. The new stdout/stderr instrument has improved performance and reliability, but it’s no longer active by default. (81732320)
- Instruments now displays run issues in a toolbar popover instead of displaying them in the detail area. In addition, run issues also appear in the ruler above the timeline to indicate when they occurred. (81732387)

###### Resolved Issues

- The find field in the Instruments detail area now properly synchronizes with find fields across the system. In addition, you can use Command-E on selected text in the extended detail view on the right to populate the detail area’s find field. (15486760) (FB5917381)
- Fixed a bug where the CPU Profiler instrument’s recordings didn’t start when targeting a Mac with Apple silicon. (84244734) (FB9703079)
- Fixed a UI issue where Instruments’ Packages preference tab incorrectly allowed for horizontal scrolling. (84359511) (FB9711254)

##### Linking

###### New Features

- The new chained fixups format is the default linking method when targeting macOS 11 or later, iOS 13.4 or later, watchOS 7.0 or later, and tvOS 14.0 or later. This new format results in smaller `LINKEDIT` segments in binaries. When targeting earlier operating system releases, the linker continues to generate the traditional opcode format in `LINKEDIT` for fixups, rebases, and binds. (85572905)

###### Resolved Issues

- Fixed: When profiling Rosetta 2 apps with Instruments or other tools, stack traces may include extra invalid unsymbolicated frames such as `0x3`. (87207828)

##### Localization

###### Resolved Issues

- Fixed an issue where Xcode duplicated keys in `.stringsdict` files alongside their corresponding `.strings` file key when exporting for localization. As part of this change, Xcode copies comments from `.strings` files to the resulting `.stringsdict` translation unit and marks the corresponding `.strings` unit as `translate="no"` in the exported XLIFF. (38238225)
- Fixed an issue where `genstrings` was unable to print diagnostics with Unicode characters. (85229466)
- Log and diagnostic messages now appear in the Report navigator when importing and exporting for localization. (18023462)
- You can now override build settings from the command-line tool when using `xcodebuild` to import and export localizations. (75221589)

##### Organizer

###### New Features

- Xcode now automatically sends you Smart Insights Notifications for your apps if you have 10 or fewer apps and if you haven’t previously subscribed to any apps. To activate this feature, click the Regressions item or any of the Metrics items in Organizer. (86535781)

###### Deprecations

- The `symbolicatecrash` script is deprecated. Instead, use the `atos` command-line tool. For more information about this tool, see [`Adding identifiable symbol names to a crash report`](https://developer.apple.com/documentation/Xcode/adding-identifiable-symbol-names-to-a-crash-report). (82929755)

##### Playgrounds

###### Resolved Issues

- Fixed: You may not be able to edit local network and ATS capability entries in Swift Playgrounds projects when running in macOS Big Sur 11. (89169927)

###### Known Issues

- Swift Playgrounds projects in Xcode may not launch unless a bundle ID is set in the project. (88832659) : Set a bundle ID in the Signing & Capabilities tab of the project editor.
- When you add a new Playground to an open workspace via the “File / New Playground …” menu, it may not open properly. (88929244) : Close and re-open the workspace. Or add a Playground using “File / New File …” instead.
- Adding a macOS capability to a Swift Playgrounds app project may cause the project to fail to load in Swift Playgrounds. : Remove any macOS capabilities.

##### Previews

###### Known Issues

- Previews may fail for a SwiftUI view that’s in a Mac Catalyst framework or package that isn’t also embedded within an app. (88895960) : To preview a SwiftUI view in Mac Catalyst, make sure the view’s framework or package is embedded in the app. Also make sure the active scheme contains both the app target and the view’s framework or package.
- Text fields in live previews for Mac Catalyst might not initially activate when you click on them. (89029611) : Try clicking again or Control-click in order to activate the text field.

##### Project Navigator

###### Resolved Issues

- Fixed an issue where some Xcode projects opened in a red “missing” state after Xcode crashed and reopened. (70526957) (FB8816939)
- Fixed: Xcode declares the wrong type identifier for GPX files (`com.topographix.gpx` instead of `com.topografix.gpx`). This can interrupt other applications that operate on `com.topografix.gpx` files. (86333977) (FB9804569)

##### Simulator

###### Known Issues

- Apps may terminate unexpectedly when running in a watchOS 5.3 simulator. (89453856)
- Debugging an app might fail the first time Simulator launches. (78621968) : Try debugging the App Extension again after Simulator launches. You may need to delete your iOS app from Simulator.

##### Source Control

###### New Features

- Xcode now supports using ED25519 public key signatures to perform git operations. You can select an existing ED25519 key from the Accounts tab in Xcode Preferences. (88897990)

###### Known Issues

- Multi-line comments containing parentheses may result in inaccurate diffs being displayed on the command-line and in the Code Review in Xcode’s source editor. (61163230)
- The Changes navigator’s pull request file list may not auto-refresh when you add commits to a branch with an associated pull request. (75502462) : Manually select commit from Pull Request Commit menu or relaunch Xcode.

##### Source Editor

###### New Features

- Code completion now suggests enum instances for `if case .`. (69842729)
- Code completion no longer auto-imports a module when completing a nonaccessible symbol. (85480026)

###### Resolved Issues

- Fixed an issue where “Add documentation” didn’t work on functions with generic parameters. (56540593)
- Fixed an issue that caused Xcode to hang when closing a project. (74228821)
- Fixed an issue with structured selection where Command-clicking on a function declaration in a protocol included the next function. (75201756)
- Fixed an issue that caused Xcode to hang when switching schemes. (75392935)
- Fixed an issue where code completion didn’t highlight or suggest initializers. (76405775)
- Fixed an issue where Xcode could hang in projects with a large amount of import statements. (76435758)
- Fixed issues with code completion, quick help, and jump-to-definition for property wrappers. (77622064)
- Fixed an issue where Xcode could hang when presenting code completion for the first time. (77651767)
- Fixed an issue where code completion auto-imported a module when naming a closure argument. (79307862) (FB9176668)
- Fixed an issue where code completion showed a `super.` snippet at invalid positions. (82176257)
- Fixed an issue where syntax highlighting displayed types as constants. (84007681)
- Fixed an issue where syntax highlighting became stale. (84307235)
- Fixed an issue where an optional type in a generic function caused indentation issues. (84931808) (FB9735705)
- Fixed an issue where code completion showed duplicate suggestions for the `for in...` or `switch...` snippet. (84965766) (FB9737092)
- Fixed an issue where code completion incorrectly showed “This completion is from a module that’s not imported.” (85479784)
- Fixed an issue where code completion showed duplicated tuple members. (85512121)
- Fixed an issue that caused Xcode to hang when opening a Swift package containing a large file with no extension. (85763867) (FB9781957)
- Fixed an issue where code completion inserted the wrong type placeholder. (86829101)
- Fixed an indentation issue for methods with keyword parameter labels spread across multiple lines. (87490908)
- Code completion no longer auto-imports test or app targets. (87585202)
- Fixed an issue where Source Editor didn’t syntax highlight custom attributes with arguments for wrapped properties. (87611350)
- Fixed a number of issues with the indentation of chained SwiftUI modifiers. (87612104)

##### Storekit

###### New Features

- Within StoreKit configuration files, you can now copy, paste, and duplicate products, subscription groups, subscription offers, and localizations. (63724339)
- You can now configure offers for codes in StoreKit configuration files when using StoreKit Testing in Xcode. You can redeem these offers when testing on devices running iOS 15.4 or later. (82929135)
- You can now toggle a new mode in StoreKit configuration files called Billing Retry on Renewal. This mode causes subscriptions to enter a simulated Billing Retry period when a subscription is set to renew. This mode works on devices and simulators running iOS 15.4, macOS Monterey 12.3, watchOS 8.5, or tvOS 15.4. (83938223)
- You can now test subscription price increases on devices or simulators running iOS 15.4, macOS Monterey 12.3, watchOS 8.5, and tvOS 15.4. You can test requesting and responding to price increase consent on a subscription transaction using the transaction manager. When testing subscription price increases on a device running iOS 15.4 or later, each request for price increase consent simulates calling the payment queue delegate method  [`paymentQueueShouldShowPriceConsent(_:)`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueueDelegate/paymentQueueShouldShowPriceConsent(_:)). (84318402)

###### Resolved Issues

- When opening the Find navigator’s results within a StoreKit configuration file, Xcode now opens the location of the configuration file where the results were found. (63911714)
- Fixed how StoreKit Testing displays multiple item selections in Xcode. (74015062) (FB8991179)
- Fixed an issue where the StoreKit Testing in Xcode editor didn’t horizontally scroll on small windows. (74015131) (FB8991182)

##### Swift 56

###### New Features

- Swift now allows existential types written with the `any` keyword. An existential type is a type that can hold a value of any type conforming to a specific protocol. The `any` keyword creates a syntactic distinction between existential types and protocol conformance constraints. The `any` keyword is an important syntactic indicator that you’re using an existential type, because there are fundamental limitations on the capabilities of these types, such as the inability to conform to protocols. For example: ```swift
protocol P {}
// generic syntax
func generic<T>(value: T) where T: P {
  ...
}
// existential syntax
func existential(value: any P) {
   ...
}
``` ([`SE-0335`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0335-existential-any.md), 88597544)
- You can now include type placeholders in type expressions and annotations. Type placeholders direct the compiler to set the type for that position according to the usual type inference rules. To use a type placeholder, enter an underscore (”_”) instead of the type name. ([`SE-0315`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0315-placeholder-types.md), 87734998) For example: ```None
// This is OK--the compiler can infer the key type as `Int`.
let dict: [_: String] = [0: "zero", 1: "one", 2: "two”]
```
- You can now write inverted availability conditions using the new `#unavailable` keyword. (87734695) For example: ```None
if #unavailable(iOS 15.0) {
    // Old functionality
} else {
    // iOS 15 functionality 
}
```
- The Swift compiler now accepts limited pointer type mismatches when directly calling functions imported from C as long as the C language allows those pointer types to alias. Consequently, any Swift `Unsafe[Mutable]Pointer<T>` or `Unsafe[Mutable]RawPointer` may be passed to C function arguments declared as `[signed|unsigned] char *`. Swift `Unsafe[Mutable]Pointer<T>` can also be passed to C function arguments with an integer type that differs from `T` only in its signedness. ([`SE-0324`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0324-c-lang-pointer-arg-conversion.md), 87735396) For example, after importing a C function declaration: ```None
long long decode_int64(const char *ptr_to_int64);
``` Swift can now directly pass a raw pointer as the function argument. For example: ```None
func decodeAsInt64(data: Data) -> Int64 {
    data.withUnsafeBytes { (bytes: UnsafeRawBufferPointer) in
        decode_int64(bytes.baseAddress!)
    }
}
```
- References to `Self` or so-called “`Self` requirements” in the type signatures of protocol members are now correctly detected in the parent of a nested type. As a result, you can’t declare these protocol members on protocols. (87735517) For example: ```None
struct Outer<T> {
  struct Inner {}
}

protocol P {}
extension P {
  func method(arg: Outer<Self>.Inner) {}
}

func test(p: P) {
  // error: 'method' has a 'Self' requirement and can’t be used on a value of
  // protocol type (use a generic constraint instead).
  _ = p.method
}
```
- Swift now provides an incremental migration path for data race safety. APIs can adopt concurrency without breaking clients that haven’t adopted concurrency. An existing declaration can introduce concurrency-related annotations (such as making its closure parameters `@Sendable`) and use the `@preconcurrency` attribute to maintain its behavior for clients who haven’t adopted concurrency: ```swift
// module A
@preconcurrency func runOnSeparateTask(_ workItem: @Sendable () -> Void)
// module B
import A
class MyCounter {
  var value = 0
}
func doesNotUseConcurrency(counter: MyCounter) {
  runOnSeparateTask {
    counter.value += 1 // no warning, because this code hasn't adopted concurrency
  }
}
func usesConcurrency(counter: MyCounter) async {
  runOnSeparateTask {
    counter.value += 1 // warning: capture of non-Sendable type 'MyCounter'
  }
}
``` You can enable warnings about data race safety within a module by setting the `-warn-concurrency` compiler option. When using a module that doesn’t provide `Sendable` annotations yet, you can suppress warnings for types from that module by marking the import with `@preconcurrency`: ```swift
/// module C
public struct Point {
  public var x, y: Double
}
// module D
@preconcurrency import C
func centerView(at location: Point) {
  Task {
    await mainView.center(at: location) // no warning about non-Sendable 'Point' because the @preconcurrency import suppresses it
  }
}
``` ([`SE-0337`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0337-support-incremental-migration-to-concurrency-checking.md), 88597842)
- The conformance of the unsafe pointer types (e.g., `UnsafePointer`, `UnsafeMutableBufferPointer`) to the `Sendable` protocols has been removed, because Swift can’t safely transfer pointers across task or actor boundaries. ([`SE-0331`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0331-remove-sendable-from-unsafepointer.md), 88598449)
- The standard library now provides the [`withUnsafeTemporaryAllocation(of:capacity:_:)`](https://developer.apple.com/documentation/Swift/withUnsafeTemporaryAllocation(of:capacity:_:)) and [`withUnsafeTemporaryAllocation(byteCount:alignment:_:)`](https://developer.apple.com/documentation/Swift/withUnsafeTemporaryAllocation(byteCount:alignment:_:)) functions. You can use these functions to cheaply allocate raw storage for a brief duration. The system allocates storage on the stack if possible. ([`SE-0322`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0322-temporary-buffers.md), 88598790)

###### Resolved Issues

- Apps that use back-deployed Swift Concurrency on operating systems prior to macOS 10.15, iOS 13, tvOS 13, or watchOS 6 no longer crash on launch. (87789769)
- As part of SE-327, in Swift 5 mode a warning is now emitted if the default-value expression of an instance-member property requires global-actor isolation. Previously, the isolation granted by the type checker matched the isolation of the property itself, but at runtime that isn’t guaranteed. In Swift 6, such default-value expressions become an error if they require isolation. For more details, see [`SE-327`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0327-actor-initializers.md#stored-property-isolation). (87620832) For example: ```None
@MainActor
func partyGenerator() -> [PartyMember] { fatalError("todo") }

class Party {
  @MainActor var members: [PartyMember] = partyGenerator()
  //                                      ^~~~~~~~~~~~~~~~
  // warning: expression requiring global actor 'MainActor' cannot
  //          appear in default-value expression of property 'members'
}
``` To fix this warning, move the expression into an initializer. ```None
func partyGenerator() -> [PartyMember] { fatalError("todo") }

class Party {
  @MainActor var members: [PartyMember]

  @MainActor init() {
    members = partyGenerator()
  }
}
```

###### Known Issues

- Applications linking to RealityKit with iOS 15 or macOS Monterey 12 SDKs fail to launch in previous operating systems. (79584511) : Add `OTHER_LDFLAGS = -weak_framework RealityFoundation` to your Xcode project settings to allow running RealityKit apps in older operating systems.

##### Swift Package Manager

###### New Features

- Swift Packages now support build tool plugins, as defined in [`SE-0303`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0303-swiftpm-extensible-build-tools.md) and [`SE-0325`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0325-swiftpm-additional-plugin-apis.md). This allows packages to define plugins that can specify tools that should run during a build operation, for example to generate source code. This is supported in both `swift` `package` and in Xcode’s support for packages. (79876749)
- The `swift` `package` command now supports command plugins, as defined in [`SE-0332`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0332-swiftpm-command-plugins.md). This allows Packages to define commands that can be invoked using the `swift` `package` command line to perform custom actions on the package. (82895553)

###### Resolved Issues

- Fixed: An error emitted by a build tool package plugin wasn’t being shown in the package log. (83715966)

###### Known Issues

- An error emitted by a build tool package plugin doesn’t prevent a build operation that relies on the outputs from the plugin from starting. This can cause build errors related to the missing files that the plugin would have produced. (87842335)

##### Swift Packages

###### Resolved Issues

- Fixed: Archiving an Xcode product that uses a build tool package plugin built from source failed with an error that the tool can’t be found. (88735684)

###### Known Issues

- Making changes to one or more packages in a workspace and then starting a build may cause Xcode to crash. (90286753) :  To avoid this issue, set the following user default in Terminal: ```None
defaults write com.apple.dt.Xcode XPMAvoidUpdatingUnchangedPackages No
```

##### Testing

###### New Features

- When running tests repeatedly, the test runner now prints the current iteration number to the console. (83848153)

###### Resolved Issues

- Fixed several issues with the `xccov` command-line tool. The `--file` argument is no longer required with the `view` command. If you don’t specify `--file`, the tool outputs all information from the specified archive rather than enumerating each file’s contents individually. `xccov` also now supports JSON output with the `--json` argument when viewing archives’ contents. (82004604)
- `xcodebuild` now supports an `.xctestproducts` bundle format for the `build-for-testing` and `test-without-building` actions. Using a bundle makes it easier to run tests, particularly when transporting tests between systems. Use the new `-testProductsPath` argument to set the path to the bundle. For example, performing a build with a command like: ```None
xcodebuild build-for-testing -project MyProject.xcodeproj -scheme App -testProductsPath ./App.xctestproducts
``` produces an App.xctestproducts bundle directory that you can then use to run tests with a command like: ```None
xcodebuild test-without-building -testProductPath ./App.xctestproducts -destination [...]
``` Use the `-testPlan` argument to specify the name of the test plan to build or run. (85612917)
- XCTest now supports resetting the authorization status of the “Local Network” protected resource during UI testing. (64828023) (FB7801261)

##### Xcode Cloud

###### Known Issues

- When configuring a project or workspace to use Xcode Cloud, the Default workflow may select the wrong scheme for the archive action. (78776640) : Edit the workflow and select the correct scheme.

## See Also

- [Xcode 13.4.1 Release Notes](xcode-13_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.4 Release Notes](xcode-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3.1 Release Notes](xcode-13_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2.1 Release Notes](xcode-13_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2 Release Notes](xcode-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.1 Release Notes](xcode-13_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13 Release Notes](xcode-13-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-13_3-release-notes)*