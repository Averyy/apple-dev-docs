# Xcode 16.3 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 16.3 includes SDKs for iOS 18.4, iPadOS 18.4, tvOS 18.4, watchOS 11.4, macOS Sequoia 15.4, and visionOS 2.4. The Xcode 16.3 release supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 7 and later, and visionOS. Xcode 16.3 requires a Mac running macOS Sequoia 15.2 or later.

##### General

###### Resolved Issues

- Fixed: Clipboard Viewer is not included with Additional Tools for Xcode 16.3 beta.  (142986262)
- Fixed: Using `LD_CLIENT_NAME` could cause a runtime crash where the debug dylib could not be found on some platforms. The workaround setting `ENABLE_DEBUG_DYLIB=NO` should no longer be necessary in this case.  (144577495)
- Fixed: The debugger variables view may have previously loaded unecessary child node content when pausing on a stack frame.  (147855714)

###### Known Issues

- Using the `-stack_size` linker flag for an app bundle target may fail. Set `ENABLE_DEBUG_DYLIB=NO` as a workaround.  (135877478) (FB15112909)
- Downloads of the Predictive Code Completion model may look like they have failed right after they have almost reached 100% completion.   (144245083)  Retry enabling Predictive Code Completion from Xcode Settings or restart your computer.

##### App Intents

###### Resolved Issues

- Fixed: OpenIntent required parameters incorrectly being marked as an error  (143909972)

##### Apple Clang Compiler

###### New Features

- Clang now defines `TARGET_OS_*` conditionals as built-in macros based on the provided target triple. This extension can be disabled with the flag `-fno-define-target-os-macros`.  (111414452)
- You can now annotate C++ methods using API Notes.  (131387880)
- You can now annotate C++ classes declared within other classes using API Notes.  (132083354)
- - The default C++ language standard for the Apple Clang compiler is now C++14 with GNU language extensions. The following C++26 features have been implemented: - Unevaluated strings ([`P2361R6`](https://developer.apple.comhttps://wg21.link/P2361R6))
- `constexpr` cast from `void*`([`P2738R1`](https://developer.apple.comhttps://wg21.link/P2738R1))
- On the ignorability of standard attributes ([`P2552R3`](https://developer.apple.comhttps://wg21.link/P2552R3))
- User-generated `static_assert` messages ([`P2741R3`](https://developer.apple.comhttps://wg21.link/P2741R3))
- Placeholder variables with no name ([`P2169R4`](https://developer.apple.comhttps://wg21.link/P2169R4))
- Template parameter initialization ([`P2308R1`](https://developer.apple.comhttps://wg21.link/P2308R1))
- Remove Deprecated Arithmetic Conversion on Enumerations ([`P2864R2`](https://developer.apple.comhttps://wg21.link/P2864R2))
- Clarifying rules for brace elision in aggregate initialization ([`P3106R1`](https://developer.apple.comhttps://wg21.link/P3106R1))
- Pack Indexing ([`P2662R3`](https://developer.apple.comhttps://wg21.link/P2662R3))
- `= delete("should have a reason");` ([`P2573R2`](https://developer.apple.comhttps://wg21.link/P2573R2))
- Attributes for Structured Bindings ([`P0609R3`](https://developer.apple.comhttps://wg21.link/P0609R3))
- Disallow Binding a Returned Glvalue to a Temporary ([`P2748R5`](https://developer.apple.comhttps://wg21.link/P2748R5))
- Trivial infinite loops are not Undefined Behavior ([`P2809R3`](https://developer.apple.comhttps://wg21.link/P2809R3))
- Deleting a Pointer to an Incomplete Type Should be Ill-formed ([`P3144R2`](https://developer.apple.comhttps://wg21.link/P3144R2))
- Ordering of constraints involving fold expressions ([`P2963R3`](https://developer.apple.comhttps://wg21.link/P2963R3)) The following C++23 features have been implemented: - Deducing `this` ([`P0847R7`](https://developer.apple.comhttps://wg21.link/P0847R7))
- Change scope of lambda trailing-return-type ([`P2036R3`](https://developer.apple.comhttps://wg21.link/P2036R3))
- Relaxing some `constexpr` restrictions ([`P2448R2`](https://developer.apple.comhttps://wg21.link/P2448R2))
- A type trait to detect reference binding to temporary ([`P2255R2`](https://developer.apple.comhttps://wg21.link/P2255R2))
- Static and explicit object member functions with the same parameter-type-lists ([`P2797R0`](https://developer.apple.comhttps://wg21.link/P2797R0)) The following C++20 features have been implemented: - Class types as non-type template parameters ([`P0732R2`](https://developer.apple.comhttps://wg21.link/P0732R2))
- Immediate functions `(consteval)` ([`P1073R3`](https://developer.apple.comhttps://wg21.link/P1073R3))  (144371212)

###### Resolved Issues

- Fixed: In rare cases compiler generated code for Intel x86 processors may overwrite function parameters on the stack.  (143354182)

##### Build System

###### Resolved Issues

- Fixed: Validating embedded binaries like App Extensions and App Clips now uses less total memory.  (147873253)

##### C++ Standard Library

###### New Features

- The following C++26 features have been implemented: - Concatenation of `string`s and `string_view`s ([`P2591R5`](https://developer.apple.comhttps://wg21.link/P2591R5))
- Member `visit` ([`P2637R3`](https://developer.apple.comhttps://wg21.link/P2637R3))
- Printing Blank Lines with `println` ([`P3142R0`](https://developer.apple.comhttps://wg21.link/P3142R0))
- Interfacing `stringstreams` with `string_view` ([`P2495R3`](https://developer.apple.comhttps://wg21.link/P2495R3))
- Add `tuple` protocol to `complex` ([`P2819R2`](https://developer.apple.comhttps://wg21.link/P2819R2)) The following C++23 features have been implemented: - Pipe support for user-defined range adaptors ([`P2387R3`](https://developer.apple.comhttps://wg21.link/P2387R3))
- `out_ptr` - a scalable output pointer abstraction ([`P1132R8`](https://developer.apple.comhttps://wg21.link/P1132R8))
- `std::ranges::contains_subrange` (`std::ranges::contains` has been implemented in a previous release) ([`P2302R4`](https://developer.apple.comhttps://wg21.link/P2302R4))
- `ranges::find_last()`, `ranges::find_last_if()`, and `ranges::find_last_if_not()` ([`P1223R5`](https://developer.apple.comhttps://wg21.link/P1223R5))
- Poison Pills are Too Toxic ([`P2602R2`](https://developer.apple.comhttps://wg21.link/P2602R2)) The following C++20 features have been implemented: - The Mothership has Landed: Adding <=> to the Library ([`P1614R2`](https://developer.apple.comhttps://wg21.link/P1614R2))
- Symmetry for spaceship ([`P0905R1`](https://developer.apple.comhttps://wg21.link/P0905R1))
- `std::atomic_ref` ([`P0019R8`](https://developer.apple.comhttps://wg21.link/P0019R8))
- Add `wait`/`notify` to `atomic_ref<T>` ([`P1643R1`](https://developer.apple.comhttps://wg21.link/P1643R1))
- Missing `constexpr` in `std::optional` and `std::variant` ([`P2231R1`](https://developer.apple.comhttps://wg21.link/P2231R1)) Performance improvements: - The performance of growing `std::vector` has been improved for trivially relocatable types.
- Many types are considered trivially relocatable now, including `std::vector` and `std::string`.
- The performance of `std::ranges::fill` and `std::ranges::fill_n` has been improved for `std::vector<bool>::iterator`s, resulting in a performance increase of up to 1400x.
- The `std::mismatch` and `std::ranges::minmax` algorithms have been optimized for integral types, which can lead massive performance improvements (up to 100x).
- The `std::set_intersection` and `std::ranges::set_intersection` algorithms have been optimized to `O(log N)` instead of `O(N)` in certain best-case scenarios.
- `std::stable_sort` uses radix sort for integral types now, which can improve the performance up to 10x in the best case.  (144568843)

###### Deprecations

- The following items have been deprecated or removed: - Implemented the “Remove Deprecated `strstream`s From C++26” paper ([`P2867R2`](https://developer.apple.comhttps://wg21.link/P2867R2)). The `_LIBCPP_ENABLE_CXX26_REMOVED_STRSTREAM` macro has been added to restore the old behavior. This compatibility macro will be removed in a future release.
- Implemented the “Remove `wstring_convert` From C++26” paper ([`P2872R3`](https://developer.apple.comhttps://wg21.link/P2872R3)). The `_LIBCPP_ENABLE_CXX26_REMOVED_WSTRING_CONVERT` macro has been added to restore the old behavior. This compatibility macro will be removed in a future release.
- Implemented the “Disallow User Specialization of `allocator_traits`” paper ([`P2652R2`](https://developer.apple.comhttps://wg21.link/P2652R2)).
- The base template for `std::char_traits` has been removed. If you are using `std::char_traits` with types other than `char`, `wchar_t`, `char8_t`, `char16_t`, `char32_t` or a custom character type for which you specialized `std::char_traits`, your code will stop working. The Standard does not mandate that a base template is provided, and such a base template is bound to be incorrect for some types, which could previously cause unexpected behavior while going undetected.
- LWG3430 has been implemented which disallows implicit conversion of the source arguments to `std::filesystem::path` when constructing `std::basic_*fstream`. This effectively removes the possibility to directly construct a `std::basic_*fstream` from a `std::basic_string_view`, a input-iterator or a C-string, instead you can construct a temporary `std::basic_string`. This change has been applied to C++17 and later.
- libc++ no longer supports `std::allocator<const T>` and containers of `const`-qualified element type, such as `std::vector<const T>` and `std::list<const T>`. This used to be supported as an undocumented extension. If you were using `std::vector<const T>`, replace it with `std::vector<T>` instead. The `_LIBCPP_ENABLE_REMOVED_ALLOCATOR_CONST` macro can be defined to temporarily re-enable this extension. This compatibility macro will be removed in a future release. To assist with the clean-up process, consider running your code through Clang Tidy, with [`std-allocator-const`](https://developer.apple.comhttps://clang.llvm.org/extra/clang-tidy/checks/portability/std-allocator-const.html) enabled.
- libc++ no longer supports relational comparison for `std::chrono::weekday`. The relational comparison operators were provided as an undocumented extension. If you were using relational comparison on `std::chrono::weekday`, compare the results of `c_encoding()` or `iso_encoding()` instead. The `_LIBCPP_ENABLE_REMOVED_WEEKDAY_RELATIONAL_OPERATORS` macro can be defined to temporarily re-enable this extension. This compatibility macro will be removed in a future release.
- The C++20 synchronization library (`<barrier>`, `<latch>`, `std::atomic::wait`, etc.) has been deprecated in language modes prior to C++20. If you are using these features prior to C++20, please update to `-std=c++20`. In a future release, the synchronization library will become unavailable in language modes prior to C++20.
- The operators in the `rel_ops` namespace have been deprecated as a part of the paper P0768R1 “Library Support for the Spaceship (Comparison) Operator”.
- The `_LIBCPP_ENABLE_NARROWING_CONVERSIONS_IN_VARIANT` compatibility macro that changed the behavior for narrowing conversions in `std::variant` has been removed.
- The `_LIBCPP_ENABLE_CXX20_REMOVED_ALLOCATOR_MEMBERS` and `_LIBCPP_ENABLE_CXX20_REMOVED_ALLOCATOR_VOID_SPECIALIZATION` compatibility macros have been removed.
- The `_LIBCPP_ENABLE_CXX17_REMOVED_FEATURES` and `_LIBCPP_ENABLE_CXX20_REMOVED_FEATURES` compatibility macros have been removed.
- Several incidental transitive includes have been removed from libc++. If you see errors related to missing `std::` entities in your code after upgrading, ensure you have all required includes.  (144887966)

##### Carplay Simulator

###### New Features

- CarPlay Simulator allows you to go between simulated automaker backup camera UI and CarPlay via car button in CarPlay Simulator UI.  (125863514)

##### Debugging

###### New Features

- Rendering of LLDB and Swift REPL error diagnostics is improved. Inline diagnostics can now directly point to command input without echoing the command first.    (138057894)

###### Resolved Issues

- Fixed: Resolves a crash that sometimes occurs when fetching variables or running Swift expressions (more prevalent on macOS 15.4)  (137006656)
- Fixed: In some cases LLDB may not correctly handle breakpoints or symbolication of libraries loaded in simulator processes.  (144655033)

##### Developer Documentation Window

###### Known Issues

- Searching in the documentation viewer may start an indexing process which makes no progress. This may result in missing search results and increased CPU usage.  (147380194) (FB16926964)  Disable documentation indexing by setting the following preference: ```None
 defaults write com.apple.dt.Xcode IDEDocumentationSpotlightIndexDisable -bool YES
```

##### Devices

###### New Features

- Xcodebuild now has a command to prepare debug symbols for an device without needing to have run Xcode. Pass -prepareDeviceSupport and a -destination predicate to prepare an unlocked and attached device.  (124411614)

##### Distribution

###### Resolved Issues

- Fixed: The app store has began to enforce all app groups prefixed with ‘group.’ are registered in a provisioning profile. During distribution, Xcode will fail to sign with the correct profile if you have used this machine to distribute before. This issue still occurs even if you have set the `REGISTER_APP_GROUPS` build setting, which ensures your project contains the correct app groups.  (145875812)

##### Foundation

###### Resolved Issues

- Fixed: Foundation encoders/decoders user info dictionaries now require `Sendable` values. This may cause build errors even in the Swift 5 language mode in small edge cases where the userInfo property is set to a value like `init(myCustomInitializer:)` where the initializer is defined in an extension on `Dictionary` with a `Value == Any` constraint.  (113200224)
- Fixed: Passing Sendable Formatter subclasses across isolation boundaries in Swift may incorrectly cause compiler errors indicating that the type is not Sendable  (144869425)

##### Frameworks

###### Resolved Issues

- Fixed: Using the `ManagedApp` framework with the the iOS or visionOS SDK will fail to compile.  (145665850)

##### Gamekit

###### New Features

- GameKit provides social-gaming network features that you use to enhance engagement in your game. Starting in Xcode 16.3, you can update your game’s leaderboards and achievements locally in Xcode. Use Xcode to pull your existing configuration from App Store Connect. Once you’ve made changes, you can push updates to App Store connect. You can also test your leaderboards and achievements in Xcode by enabling Debug Mode. Update the progress for a leaderboard or achievement and the system sends an update to your app so you can verify that the leaderboard or achievement changed as expected in real time.   (110809856)

###### Resolved Issues

- Fixed: Adding a new leaderboard to an existing leaderboard set that already contains a leaderboard won’t function as expected.  (144418655)
- Fixed: Game Progress Manager is now compatible with macOS, iOS, iPadOS, tvOS and visionOS.  (145687441)

##### Instruments

###### New Features

- Call Trees now allow for listing all the samples aggregated to a node by context clicking on it and selecting ‘Show (Self) Samples’  (89381694)
- Instruments 16.3 includes a new Processor Trace Instrument which uses hardware-supported, low-overhead CPU execution tracing to accurately reconstruct execution of the program. This tool provides metrics like duration, number of cycles, and instructions retired for every function executed on the CPU. Timeline in Instruments presents execution flame graph, while detail views provide aggregate-level data like Call Tree or aggregated metrics (min, max, count, sum), divided by function. Traces can be recorded using the new Processor Trace template on supported devices: M4 Mac, M4 iPad, and iPhone 16/16 Pro. Tracing on the device requires additional configuration in the System Settings.  (131079807)
- Double clicking on an interval in the timeline while holding Option modifier will now filter and zoom-in to the interval location.  (140099146) (FB15872554)
- Clicking on a selected track will now expand it’s height to fit all the plots.  (143853314)

###### Resolved Issues

- Fixed: Gesture handling for timeline events has been simplified. Single click now selects an item, while double click sets the inspection range of a trace to interval location. Triple click gesture handling has been removed.  (91116149)
- Fixed: Threads are no longer named based on backtraces attributed to that thread. This improves performance of Instruments and ensures consistency of thread names with other tools.  (107272376)
- Fixed an issue where xctrace would crash when recording CPU Counters template containing unavailable PMU events.  (127001356) (FB13752225)
- Fixed an issue where Allocations Instrument would misattribute source location of an allocation in the disassembly view.  (127261727)
- Fixed: Improved collapsing behavior of the Heaviest Stack Trace by ensuring that prominent frames with source information are no longer hidden.  (136160536)
- Fixed: Source Viewer performance has been improved and will no longer be slower than the initial load of the Call Tree view.  (138136953)
- Fixed an issue where Call Tree view would occasionally cause application crashes.  (146034535)

###### Deprecations

- Removed support for profiling Notification Center Widget Extensions.  (138192293)

##### Interface Builder

###### Resolved Issues

- Fixed: iPhone 16e does not appear in the Interface Builder device bar.  (144352490)

##### Localization

###### New Features

- The String Catalog Editor now displays the number of strings in the file (or the number of strings that match the active filter).  (122523913)
- The String Catalog Editor now emits errors for more cases of contradictory format specifiers in varied strings.  (128285700)

###### Resolved Issues

- Fixed non-determinism in choosing string values when multiple targets share an InfoPlist.strings file. Additionally, more info plist keys may be extracted to `InfoPlist.xc/strings` files automatically. Keys such as `CFBundleDisplayName` will now be auto-extracted as “Don’t Translate” when they come from targets such as frameworks that typically do not display these values in the UI.  (116603462)
- Fixed: Format specifiers in String Catalog strings now have simplified rules for inferring argument numbers in order to avoid unexpected crashes at runtime. In most cases, the string “%@ has %lld books” is inferred to be equivalent to “%1$@ has %2$lld books”. In Xcode 16.3, this also applies to plural variations. An exception continues to be plural variations inside substitutions, which begin assigning implicit argument numbers starting with the substitution’s own assigned argument in the Attributes Inspector. To change behavior away from the default, use explicit argument numbers in strings (e.g. “%1$@ has %2$lld books”).  (128509959)
- Fixed: It is now a formal build error to place an xcstrings file inside an lproj directory. mul.lproj is an exception to this, since Xcode uses it to track String Catalogs associated with IB files in Base.lproj.  (133238564)
- Fixed: String Catalogs now remember sort order per editor.  (133752416) (FB14780987)
- Fixed: Xcode now remembers the preferred column order for String Catalogs.  (135439846) (FB15056367)
- Fixed: Jumping from strings in source code to entries in the String Catalog now also works for App Intent / Shortcut phrases.  (138472363)
- Fixed: Within buildable folders, .strings files are now properly grouped together with same-named Base-localized IB files and will share target membership.  (139114187)
- Fixed: Resolved various issues that could occur when localizable files are inside buildable folders.  (139114232)

##### Playgrounds

###### Resolved Issues

- Fixed: A playground that imports a module from a shared workspace may fail to run.  (143923367)

##### Predictive Code Completion

###### Resolved Issues

- Fixed: Expanded the amount of in-project context that will be used when providing suggestions for Predictive Code Completion.  (141363041)
- Fixed an issue that could cause some suggestions in Predictive Code Completion to contain unnecessary symbols or placeholder text.  (141952159)

##### Previews

###### Resolved Issues

- Fixed: In some project configurations, switching between Previews in different targets could show an error in the canvas that would not go away until a manual build was triggered.  (138953897)
- Fixed: Previews for a file in a static library or static package target could fail if they depended on a dynamic library or framework also built in the same project.  (140224924) (FB15892343)
- Fixed: `SWIFT_ENABLE_OPAQUE_TYPE_ERASURE` is now off by default for all debug builds. If you were previously turning it off in your project, you can remove that override. Previews now enables this selectively and recompiles the edited file with this setting only when running a preview.  (140442875)
- Fixed: Previews is only able to work for unoptimized builds compiled with `-Onone` and `SWIFT_COMPILATION_MODE=incremental`, which are the default for debug builds. Previews now provides better error messaging and instructions if you attempt to Preview in a file that is built with different settings.  (140803231)
- Fixed: Previews in static libraries that used `@availability` annotations would fail with a symbol not found error. This should now be resolved but if you continue to experience this please file a new feedback with fresh diagnostics since we’ve added new logging for triage.  (140898299) (FB16037528)
- Fixed: Previews offers two great benefits: a way to quickly see a configuration of a view without needing to build and run, and an execution environment for rapidly verifying changes.  ‘Automatically Refresh Previews’ provides the fastest execution environment. Disabling it will fall back to a slower execution environment that may work for your project configuration, while providing a speed benefit that should still be significantly faster overall than build and run. If disabling Automatically Refresh Previews resolves issues you experience in previews for your project configuration, please file a feedback with fresh previews diagnostics before and after toggling the setting. We’ve added new logging to help further triage issues.  (141724767)
- Fixed: In some project configurations on-device Previews could fail if you switched between files until you manually triggered a project rebuild.  (142443659)
- Fixed: In some project configurations Previews would show a blank canvas instead of a helpful error message if there were no previews found for this target. Remember to check that your preview is built for the run destination you are targeting if you use conditional compilation to hide previews. If you double checked your configuration and still believe the preview should be found, please file a feedback. If possible, also please include a simplified reproduction of the problem to help triage your specific setup. New diagnostics and logging have been added so fresh feedback will include important details.  (143507303)
- Fixed: As a general note, in addition to other correctness fixes in Xcode and our paired OS releases, diagnostics collection has been improved to help resolve remaining issues with the previews pipeline. If you have experienced timeouts or strange crashes in your code when using the new Previews execution engine, please see if your issues are resolved. If not, please file new feedback with fresh diagnostics to provide the latest information.  (143628687)

##### Realitykit

###### Resolved Issues

- Fixed: `EntityAction`, `ForceEffectProtocol`, and `RealityRenderer` methods that take closures are now marked as always executing on the main actor. Closures passed to `EntityAction` and `ForceEffectProtocol` are now marked as always executing on the main actor, and closures passed to `RealityRenderer` are now marked as executing without isolation.  (133462227)

##### Simulator

###### Resolved Issues

- Fixed: Simulator no longer discards key up events for keys when the command key is held.  (63086391) (FB7697257)
- Fixed: simctl now supports –json-fd and –json-output command line arguments for directing JSON output to a destination other than stdout.  (141441027)
- Fixed: In order to use iPhone 16e in the simulator with Xcode 16.2, download both the iPhone 16e, iPad Air (M3), and iPad (A16) Device Support and the iOS 18.3.1 Simulator Runtime from Xcode > Settings > Components.  iPhone 16e is not currently compatible with iOS 18.4 beta.  (143996070)
- Fixed: In order to use iPad Air (M3) or iPad (A16) in the simulator with Xcode 16.2, download both the iPhone 16e, iPad Air (M3), and iPad (A16) Device Support and the iOS 18.3.1 Simulator Runtime from Xcode > Settings > Components.  iPad Air (M3) and iPad (A16) are not currently compatible with iOS 18.4 beta 2.  (143996162)
- Fixed: Xcode and LLDB encounter a delay of 30 seconds or more when starting a debug session for a process in a Simulator device. The debug console may display a warning stating that LLDB is unable to read from the host’s in-memory shared cache. During this delay, the simulated app will remain invisible or unresponsive.  (145105465)
- Fixed: Simulator runtimes may complete download but not show as usable from Xcode.  (145242743)
- Fixed: Incorrect icons are used for recently released iPad hardware in Xcode’s run destination menu and devices window.  (145902433)

###### Known Issues

- The simulator runtime may be come unavailable when logging out and then back in, or if its disk image unmount gets cancelled. The workaround is to re-kick the coresimulator service with a reboot or by running: `pkill com.apple.CoreSimulator.CoreSimulatorService`  (136557160) (FB15246609)

##### Source Editor

###### New Features

- Editing JSON in Xcode now supports JSON5 syntax, including comments.  (117205049)

###### Resolved Issues

- Fixed an issue that sometimes caused horizontal scroll bars to be hidden from view when the Minimap was enabled.  (102106707)
- Fixed an issue where Code Completion may present a symbol as from the incorrect framework after using Jump to Definition.  (137079926)
- Fixed an issue where expanding short macros inside the Source Editor may crash Xcode.  (142656554)

##### Swift

###### Known Issues

- `DistributedActorSystem`, `DistributedTargetInvocationDecoder`, `DistributedTargetInvocationEncoder`, and `DistributedTargetInvocationResultHandler` may cause a compiler crash when conforming type is a class and is built in release mode.   (146101172)  Change conforming type to `struct` or make remoteCall, onReturn and other methods which use the SerializationRerquirement constraint `final`.

##### Swiftc++ Interoperability

###### New Features

- You can now call C++ functions that use `char8_t` type from Swift.  (39988329)
- You can now use Swift static variables from C++.  (115564118)
- You can now use Swift structs and enums declared within other Swift types from C++.  (118793469)
- C++ Standard Library Hardening now takes effect for Swift usages of C++ types such as `std::span`.  (126570011)
- Swift overlay for the C++ standard library is now available when targeting Mac Catalyst.  (126938813)
- C enums now automatically conform to Swift `Hashable` protocol.  (129713687)
- You can now conform C++ types to Swift protocols using the new `SwiftConformsTo:` API Notes attribute.  (131388824)
- You can now access Swift subscript operators with multiple parameters from C++.  (133539699)
- You can now initialize a C++ `std::map` or `std::unordered_map` from a Swift `Dictionary`.  (133691563)
- Mutable C++ containers such as `std::vector` now automatically conform to Swift `MutableCollecton`.  (134531554)
- C++ `std::string` now conforms to Swift `Comparable`.  (135184553)
- You can now annotate C++ functions and methods that return `SWIFT_SHARED_REFERENCE` types with `SWIFT_RETURNS_RETAINED` or `SWIFT_RETURNS_UNRETAINED` to explicitly define the ownership convention when called from Swift. The Swift compiler will now emit a warning for such C++ functions and methods that are not annotated with these ownership conventions.  (135306908)
- C++ `std::set` and `unordered_set` now conform to Swift `ExpressibleByArrayLiteral`.  (137126325)
- C++ `std::map` and `unordered_map` now conform to Swift `ExpressibleByDictionaryLiteral`.  (137126474)
- You can now initialize a Swift `String` from a C++ `std::string_view`.  (138417835)
- You can now annotate C++ functions and methods returning `SWIFT_SHARED_REFERENCE` types with `SWIFT_RETURNS_RETAINED` or `SWIFT_RETURNS_UNRETAINED` using the new `SwiftReturnOwnership:` API Notes attribute. Set its value to `retained` or `unretained`, respectively, to explicitly specify the ownership convention of the returned value.  (141007510)
- Compiler now produces an error when a public member of a C++ type and a private member of the type are imported into Swift with the same name. For example, a private field `name` and a method `getName()` annotated as SWIFT_COMPUTED_PROPERTY  will have a name conflict when they are imported into Swift and will result in an error. SWIFT_NAME attribute can be used to import them differently.  (144736093)

###### Resolved Issues

- Fixed: Xcode targets using Swift/C++ interoperability and having a deployment target of less than iOS 16 or tvOS 16 may not build for iOS or tvOS simulators.  (141232269)

##### Test Report

###### New Features

- The Test Report now displays XCUIElementQuery suggestions for UI elements selected using the Automation Explorer at a point of test failure.  (131473847)

##### Testing and Automation

###### New Features

- In Xcode when you are in a test context you are now able to query for your test plan name and scheme name in the environment with the keys `XCODE_TEST_PLAN_NAME` and `XCODE_SCHEME_NAME`.  (66632690)
- When a Swift Testing issue is recorded from an unknown context, such as a detached Task, the error message shown in Xcode now includes a description of the issue and the backtrace indicates where it occurred, for easier diagnosis.  (131564494)
- `xcodebuild` supports constraining the tests run through tests actions by tags. Use `-only-testing-tags` to include tests identified by a tags and `-skip-testing-tags` to omit tests identified by tags.  (132936523)
- The XCTest APIs related to UI automation testing have been moved to a new, standalone framework named XCUIAutomation. XCTest re-exports XCUIAutomation so `import XCTest` continues to import the APIs of both frameworks. You can use XCUIAutomation APIs from XCTest tests and any helper or utility functions they call.  (137059728)
- Swift Testing now includes Test Scoping Traits, a set of APIs for defining custom traits which can run code before or after tests or suites they’re applied to. For example, you can implement a trait which assigns a task local value for the duration of a test: ```swift
   struct MockAPICredentialsTrait: TestTrait, TestScoping {
     func provideScope(for test: Test, testCase: Test.Case?, performing function: @Sendable () async throws -> Void) async throws {
       let mockCredentials = APICredentials(apiKey: "...")
       try await APICredentials.$current.withValue(mockCredentials) {
         try await function()
       }
     }
   }
   
   extension Trait where Self == MockAPICredentialsTrait {
     static var mockAPICredentials: Self {
       Self()
     }
   }
   
   @Test(.mockAPICredentials)
   func example() {
     // ...validate API usage, referencing `APICredentials.current`...
   }
``` See the proposal [`SWT-0007`](https://developer.apple.comhttps://github.com/swiftlang/swift-testing/blob/main/Documentation/Proposals/0007-test-scoping-traits.md) for more details.  (138099506)
- `#expect(throws:)` and `#require(throws:)` now return the error that was thrown so that tests can inspect them further.  (138235250)
- Swift Testing now allows specifying a range of expected counts when calling `confirmation()`.  (138499457)
- When using a Swift.org toolchain, Xcode now prefers the copy of Swift Testing in that toolchain for building and running tests if one is available for the current platform.  (144709027) (FB16490332)

###### Resolved Issues

- Fixed: `XCTAttachment` does not support attaching directories on iOS, watchOS, tvOS, or visionOS.  (31157453)
- Fixed: Swift Testing and XCTest tests and suites written in Swift which are surrounded by `#if` conditions may not be shown in Xcode’s Test navigator or source editor.  (117387631)
- Fixes an issue with running parallel Tests on macOS run destinations where it never finishes.  (125369004)
- Fixed: The `xcodebuild` flags `-only-testing` and `-skip-testing` now accept identifiers for Swift Testing tests and suites.  (127329947)
- Fixed an issue when pressing up/down/left/right hardware keyboard buttons in text views.  (132717800) (FB14538574)
- Fixed: XCTest UI Recording has been enhanced to offer a more refined code generation process when capturing application events. This feature now also allows for recording any application, not just the application under development. XCTest UI Recording is available for all platforms except for visionOS.  (138064709)
- Fixed: If an error is thrown by the `prepare(for:)` method of a custom Swift Testing trait type, the test runner now records the error as an issue instead of crashing.  (140813092)
- Fixed: Resolved an issue where Swift Testing may produce spurious warnings when `try #require()` is used to cast a value of class type to another class.  (144624300)
- Fixed: Resolved an issue where XCTest UI Automation tests may fail on macOS if the test interruption handler is invoked during a test run.  (147359471)
- Fixed: XCTest UI Automation test results may not have UI element snapshot overlays as expected when viewing a test result in the Test Results UI.  (147527762)

###### Known Issues

- UI tests and unit testing using `USES_XCTRUNNER=YES` may see a UIKit warning about adopting scenes. This warning can be ignored.  (142567138)
- Test action may stall when running with debug executable and parallel testing enabled against the Mac run destinations.  (145872120)  Disable the Debug Executable in the Test Scheme.

##### Xcode Cloud

###### New Features

- You can now share environment variables across multiple workflows and use them in your custom build scripts. Learn about [`Shared Environment Variables`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/sharing-environment-variables-across-xcode-cloud-workflows).  (76150704)

##### Xcresulttool

###### New Features

- In Xcode 16, xcresulttool introduced new commands, including: `get test-results summary`, `get test-results tests`, `get test-results test-details`, `get test-results activities`, `get test-results insights`, `get build-results`, `get log`, `export attachments`, `and export metrics`. Please run `xcresulttool help <command> [<subcommand>]` to get more details for these commands as well as the output format. In Xcode 16.3 there are the following additions: - Command that outputs performance metrics in JSON format: `xcresulttool get test-results metrics --path <path> [--compact] [--test-id <test-id>]` A test identifier (`test-id`) can be used to specify a Test Case or a Test Suite. All the available metrics will be included if no `test-id` is provided.
- Command that outputs information about the available content in a .xcresult bundle, including code coverage, diagnostics, test results and logs: `xcresulttool get content-availability --path <path> [--compact]`
- Command that compares the content of two result bundles. Optional flags allow you to customize the outputted results: `xcresulttool compare <comparison-path> ... --baseline-path <baseline-path> [--summary] [--test-failures] [--tests] [--build-warnings] [--analyzer-issues]`
- All the commands that use `test-id` as an argument now accept both `testIdentifier` and `testIdentifierURL` values. Identifier URL (`testIdentifierURL`) is a recommended way of identification for Test Cases and Test Suites as it resolves identifier ambiguity across multiple testing targets.  (129712945)

###### Deprecations

- Some parts of `xcresulttool` API are deprecated and will be removed in the future. Upon removal they can be used with `--legacy` flag provided. Please use the new commands from above instead. List of deprecated commands: ```None
 xcresulttool get [object] --legacy --path <path> [--id <id>] [--version <version>] [--format <format>]
 xcresulttool export [object] --legacy --path <path> --output-path <output-path> [--id <id>] --type <type> [--version <version>]
 xcresulttool graph --legacy --path <path> [--id <id>] [--version <version>]
``` (144104308)

## See Also

- [Xcode 16.4 Release Notes](xcode-16_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16.2 Release Notes](xcode-16_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16.1 Release Notes](xcode-16_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16 Release Notes](xcode-16-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-16_3-release-notes)*