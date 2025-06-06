# Swift 5 Release Notes for Xcode 10.2

**Framework**: Xcode Release Notes

Update your code to use new language features and test your apps against changes.

#### Overview

Read these notes when you’re writing Swift apps in Xcode 10.2.

##### General

###### Swift 5 Runtime Support for Command Line Tools Package

- Starting with Xcode 10.2, Swift command-line tools require the Swift libraries in macOS. They’re included by default starting with macOS Mojave 10.14.4. In macOS Mojave 10.14.3 and earlier, there’s an optional package to provide these runtime support libraries for Swift command-line tools that you can download from [`More Downloads for Apple Developers`](https://developer.apple.comhttps://developer.apple.com/download/more/). If you installed the beta version of this package, replace it with the release version. This package is only needed for Swift command-line tools, not for apps with graphical user interfaces.

##### App Thinning

###### New Features

- Swift apps no longer include dynamically linked libraries for the Swift standard library and Swift SDK overlays in build variants for devices running iOS 12.2, watchOS 5.2, and tvOS 12.2. As a result, Swift apps can be smaller when they’re shipped in the App Store, deployed for testing using TestFlight, or thinned in an app archive for local development distribution. To see the difference in file sizes between an app that’s thinned for iOS 12.2 and an app that’s thinned for iOS 12.1 or earlier, set your app’s deployment target to iOS 12.1 or earlier, then create an archive of your app with the scheme set to Generic iOS Device. After building the archive, select Distribute App from the Archives organizer, then select Development distribution. Be sure to select a specific device—such as iPhone XS—in the App Thinning pull-down menu. When the distribution process completes, open the App Thinning Size Report in the newly created folder. The variant for iOS 12.2 will be smaller than the variant for iOS 12.1 and earlier. The exact size difference depends on the number of system frameworks your app uses. For information about app thinning, see [`What is app thinning?`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devbbdc5ce4f) in [`Xcode Help`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/). For information about app file sizes, see [`View builds and file sizes`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev3b56ce97c) in [`App Store Connect Help`](https://developer.apple.comhttps://help.apple.com/app-store-connect/).

##### Swift Language

###### New Features

- String literals can now be expressed using enhanced delimiters. A string literal with one or more number signs (`#`) before the opening quote treats backslashes and double-quote characters as literal unless they’re followed by the same number of number signs. Use enhanced delimiters to avoid cluttering string literals that contain many double-quote or backslash characters with extra escapes ([`SE-0200`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0200-raw-string-escaping.md)) (47725014): ```swift
print(#"<a href="\#(url)" title="Apple Developer">"#)

// Equivalent to:
print("<a href=\"\(url)\" title=\"Apple Developer\">")
```
- If you declare a type that has the same name as a type in the standard library, your type now shadows the type from the standard library.  (46767892) For example, if you declare a `Result` type in a module named `Foo`: ```swift
// Module `Foo`.

public enum Result<T> {
    case value(T)
    case error(Error)
}
``` Unqualified references to `Result` in any of your code that imports the `Foo` module will resolve to `Foo.Result`: ```swift
import Foo

func doSomething() -> Result<Int> { /* … */ }
``` To refer to the [`Result`](https://developer.apple.com/documentation/Swift/Result) type from the Swift standard library instead, qualify the access with the “`Swift.`” prefix. For example: ```swift
import Foo

func useStandardLibraryResult() -> Swift.Result<Int, Error> { /* … */ }
```
- The `@dynamicCallable` attribute lets you call named types like you call functions using a simple syntactic sugar. The primary use case is dynamic language interoperability. ([`SE-0216`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0216-dynamic-callable.md)) (47325423) For example: ```swift
@dynamicCallable struct ToyCallable {
    func dynamicallyCall(withArguments: [Int]) {}
    func dynamicallyCall(withKeywordArguments: KeyValuePairs<String, Int>) {}
}

let x = ToyCallable()

x(1, 2, 3)
// Desugars to `x.dynamicallyCall(withArguments: [1, 2, 3])`

x(label: 1, 2)
// Desugars to `x.dynamicallyCall(withKeywordArguments: ["label": 1, "": 2])`
```
- Key paths now support the identity keypath (`\.self`), a [`WritableKeyPath`](https://developer.apple.com/documentation/Swift/WritableKeyPath) that refers to its entire input value ([`SE-0227`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0227-identity-keypath.md)) (40538312): ```swift
let id = \Int.self

var x = 2
print(x[keyPath: id]) // Prints "2"
x[keyPath: id] = 3
print(x[keyPath: id]) // Prints "3"
```
- Prior to Swift 5, you could write an enumeration case that took variadic arguments: ```swift
enum X {
    case foo(bar: Int...)
}

func baz() -> X {
    return .foo(bar: 0, 1, 2, 3)
}
``` This was unsupported intentionally, and now generates an error. (46821582) Instead, change the enumeration case to take an array and explicitly pass an array in: ```swift
enum X {
    case foo(bar: [Int])
}

func baz() -> X {
    return .foo(bar: [0, 1, 2, 3])
}
```
- In Swift 5 mode, `try?` with an expression of an [`Optional`](https://developer.apple.com/documentation/Swift/Optional) type flattens the resulting optional, instead of returning a nested optional. ([`SE-0230`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0230-flatten-optional-try.md)) (47313584)
- If a type `T` conforms to one of the protocols in [`Initialization with Literals`](https://developer.apple.com/documentation/Swift/initialization-with-literals)—such as [`ExpressibleByIntegerLiteral`](https://developer.apple.com/documentation/Swift/ExpressibleByIntegerLiteral)—and  is a literal expression, then `T(``)` creates a literal of type `T` using the corresponding protocol, rather than calling an initializer of `T` with a value of the protocol’s default literal type. For example, expressions like `UInt64(0xffff_ffff_ffff_ffff)` are now valid, where previously they would overflow the default integer literal type of [`Int`](https://developer.apple.com/documentation/Swift/Int). ([`SE-0213`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0213-literal-init-via-coercion.md)) (17088188)
- String interpolation has improved performance, clarity, and efficiency. ([`SE-0228`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0228-fix-expressiblebystringinterpolation.md)) (43621912) The older `_ExpressibleByStringInterpolation` protocol is removed; if you have code that makes use of this protocol, you need to update it for the new design. You can use `#if` to conditionalize code between Swift 4.2 and Swift 5. For example: ```swift
#if compiler(<5)
extension MyType: _ExpressibleByStringInterpolation { /*...*/ }
#else
extension MyType: ExpressibleByStringInterpolation { /*...*/ }
#endif
```

##### Swift Standard Library

###### New Features

- The standard library now includes the [`Result`](https://developer.apple.com/documentation/Swift/Result) enumeration with [`Result.success(_:)`](https://developer.apple.com/documentation/Swift/Result/success(_:)) and [`Result.failure(_:)`](https://developer.apple.com/documentation/Swift/Result/failure(_:)) cases. Use [`Result`](https://developer.apple.com/documentation/Swift/Result) to manually propagate and handle errors in situations where `do-catch` statements and the `try` expression can’t be used, such as when you’re using asynchronous APIs that can fail. As part of this addition, the [`Error`](https://developer.apple.com/documentation/Swift/Error) protocol now conforms to itself, which makes working with errors in a generic context easier. ([`SE-0235`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0235-add-result.md)) (21200405)
- [`SIMD`](https://developer.apple.com/documentation/Swift/SIMD) types and basic operators are now defined in the standard library. The types provided by the [`SIMD`](https://developer.apple.com/documentation/Swift/SIMD) framework, like [`float2`](https://developer.apple.com/documentation/simd/float2) and [`float3`](https://developer.apple.com/documentation/simd/float3), are now type aliases of the new standard library types. SIMD types are generic over the scalar element type. For example, the old [`float3`](https://developer.apple.com/documentation/simd/float3) type is a type alias of `SIMD3<Float>`. Any type that conforms to the [`SIMDScalar`](https://developer.apple.com/documentation/Swift/SIMDScalar) protocol can be used as a scalar type for SIMD vectors, but effective vectorization depends on choosing a good data layout and having efficient subscript operations for the associated [`SIMDStorage`](https://developer.apple.com/documentation/Swift/SIMDStorage) types. Most existing code using `simd` types will continue to work with the new generic SIMD types, but there are a few changes to note.The new types add some new conformances; SIMD vectors are now [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable), [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable), and [`Codable`](https://developer.apple.com/documentation/Swift/Codable). This may allow you to delete some existing extensions that provide these conformances in your own code.The set of operators that are overloaded to provide vector-scalar arithmetic is greatly expanded. This makes it easier to write some things, but in some cases introduces ambiguity to the typechecker and may make it necessary to break apart some expressions or annotate with explicit types. Because the types are now generic rather than concrete, if you have defined your own protocols over the `simd` framework types, it may be necessary to refactor the conformances because a Swift generic type can’t have multiple conditional conformances to a protocol. This situation is relatively rare, but what you need to do in general is refactor code that looks like this: ```swift
protocol MyVectorProtocol { /* ... */ }

extension float2: MyVectorProtocol { /* ... */ }
extension double2: MyVectorProtocol { /* ... */ }
``` To use the following structure instead: ```swift
protocol MySIMDScalarProtocol: SIMDScalar { /* ... */ }

extension SIMD2 where Scalar: MySIMDScalarProtocol { /* ... */ }
// Or even:
protocol MySIMDScalarProtocol: SIMDScalar { /* ... */ }
extension SIMD where Scalar: MySIMDScalarProtocol { /* ... */ }
``` This change will frequently allow you to remove many redundant implementations, but it requires that you define any necessary implementation hooks that reference the concrete functions from the C headers on Darwin systems on the scalar type. ([`SE-0229`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0229-simd.md)) (17045503)
- [`Set`](https://developer.apple.com/documentation/Swift/Set) and [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary) now use a different hash seed for each newly created instance. As a consequence, the order of elements in equal sets and dictionaries is different much more often than in previous versions: ```swift
let a: Set<Int> = [1, 2, 3, 4, 5]

let b: Set<Int> = [1, 2, 3, 4, 5]
a == b  // true
print(a) // [1, 4, 3, 2, 5]
print(b) // [4, 2, 5, 1, 3]
``` Existing code that incorrectly assumes that two unrelated but equal sets or dictionaries would contain elements in the same order produces incorrect results more often in Swift 5. Although element ordering isn’t stable across distinct `Set` or `Dictionary` instances, the order doesn’t vary between multiple iterations over the same instance. Beyond emphasizing that these collections don’t guarantee consistent element ordering, this change also fixes a number of cases where bulk operations—such as [`union(_:)`](https://developer.apple.com/documentation/Swift/Set/union(_:))—exhibited quadratic performance. (44760778)
- To help prevent inconsistent hashing for Cocoa objects, the [`hashValue`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/hashValue) property on [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class) is no longer overridable. Overrides of [`hashValue`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/hashValue) were deprecated in Swift 4.2. To customize hashing in [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class) subclasses, override the [`hash`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/hash) property. The following example shows a sample implementation: ```swift
class Person: NSObject {
    let name: String

    init(name: String) {
        self.name = name
        super.init()
    }

    override func isEqual(_ other: Any?) -> Bool {
        guard let other = other as? Person else { return false }
        return other.name == self.name
    }

    override var hash: Int {
        var hasher = Hasher()
        hasher.combine(name)
        return hasher.finalize()
    }
}
``` Hashing and equality go hand in hand. If you override [`hash`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/hash), you also need to override [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)), and vice versa. (42623458)
- The [`DictionaryLiteral`](https://developer.apple.com/documentation/Swift/DictionaryLiteral) type is renamed [`KeyValuePairs`](https://developer.apple.com/documentation/Swift/KeyValuePairs). ([`SE-0214`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0214-DictionaryLiteral.md)) (23435865)
- Swift strings bridged into Objective-C code may now return a non-`nil` value from [`CFStringGetCStringPtr(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFStringGetCStringPtr(_:_:)) when appropriate, and the pointer returned from the `UTF8String` method is tied to the string’s lifetime rather than the innermost autorelease pool. Correct programs shouldn’t have any problems and may see significant speed-ups. However, it may cause previously untested code to run, which could expose latent bugs; for example, if there’s a check for a non-`nil` value, the branch may never have been taken prior to Swift 5. (26236614)
- The [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence) protocol no longer has a `SubSequence` associated type. Methods on [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence) that previously returned `SubSequence` now return concrete types. For example, [`suffix(_:)`](https://developer.apple.com/documentation/Swift/Sequence/suffix(_:)) now returns an [`Array`](https://developer.apple.com/documentation/Swift/Array).  (45761817) Extensions on [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence) that use `SubSequence` should be amended to either similarly use a concrete type, or be amended to be extensions on [`Collection`](https://developer.apple.com/documentation/Swift/Collection) instead, where [`SubSequence`](https://developer.apple.com/documentation/Swift/Collection/SubSequence) remains available. For example: ```swift
extension Sequence {
    func dropTwo() -> SubSequence {
        return self.dropFirst(2)
    }
}
``` Becomes: ```swift
extension Sequence {
   func dropTwo() -> DropFirstSequence<Self> {
        return self.dropFirst(2)
    }
}
``` Or: ```swift
extension Collection {
    func dropTwo() -> SubSequence {
        return self.dropFirst(2)
    }
}
```
- The [`String`](https://developer.apple.com/documentation/Swift/String) structure’s native encoding switched from UTF-16 to UTF-8, which may improve the relative performance of [`String.UTF8View`](https://developer.apple.com/documentation/Swift/String/UTF8View) compared to [`String.UTF16View`](https://developer.apple.com/documentation/Swift/String/UTF16View). Consider re-evaluating any code specifically tuned to use [`String.UTF16View`](https://developer.apple.com/documentation/Swift/String/UTF16View) for performance. (42339222)

###### Known Issues

- The `count(where:)` method on the [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence) protocol available in beta versions of Xcode 10.2 is now removed. (47549309)  Use [`reduce(_:_:)`](https://developer.apple.com/documentation/Swift/AnyCollection/reduce(_:_:)) to count occurrences matching a predicate efficiently: ```swift
let occurrences = sequence.reduce(0) { predicate($1) ? $0 + 1 : $0 }
```

###### Resolved Issues

- Setting the [`utf8`](https://developer.apple.com/documentation/Swift/String/utf8) property on a string now works as expected. (47864538)
- Passing a null [`UnsafeBufferPointer`](https://developer.apple.com/documentation/Swift/UnsafeBufferPointer)`<UInt8>` to the [`String`](https://developer.apple.com/documentation/Swift/String) structure’s [`init(decoding:as:)`](https://developer.apple.com/documentation/Swift/String/init(decoding:as:)) initializer now returns an empty string as expected. (47864610)

##### Swift Package Manager

###### New Features

- Targets can now declare some commonly used, target-specific build settings when using the Swift 5 `Package.swift` `tools-version`. The new settings can also be conditionalized based on platform and build configuration. The included build settings support Swift- and C-language defines, C language header search paths, linked libraries, and linked frameworks. ([`SE-0238`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0238-package-manager-build-settings.md)) (23270646)
- Packages can now customize the minimum deployment target setting for Apple platforms when using the Swift 5 `Package.swift` `tools-version`. Building a package emits an error if any of the package dependencies of the package specify a minimum deployment target greater than the package’s own minimum deployment target. ([`SE-0236`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0236-package-manager-platform-deployment-settings.md)) (28253354)
- A new dependency mirroring feature allows top-level packages to override dependency URLs. ([`SE-0219`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0219-package-manager-dependency-mirroring.md)) (42511642) Use the following command to set a mirror: ```shell
$ swift package config set-mirror \
--package-url <original URL> --mirror-url <mirror URL>
```
- The `swift test` command can generate code coverage data in a standard format suitable for consumption by other code coverage tools using the flag `--enable-code-coverage`. The generated code coverage data is available inside `/``/codecov`. (44567442)
- Swift 5 no longer supports the Swift 3 `Package.swift` `tools-version`. Packages still on the Swift 3 `Package.swift` `tools-version` should update to a newer `tools-version`. (41974124)
- Package manager operations for larger packages are now significantly faster. (35596212)
- The Swift Package Manager has a new `--disable-automatic-resolution` flag that forces the package resolution to fail when the `Package.resolved` entries are no longer compatible with the dependency versions specified in the `Package.swift` manifest file. This feature can be useful for a continuous integration system to check if a package’s `Package.resolved` is out of date. (45822895)
- The `swift run` command has a new `--repl` option that launches the Swift REPL with support for importing library targets of a package. This allows you to easily experiment with API from a package target without needing to build an executable that calls that API. (44889181)
- For more information about using the Swift Package Manager, visit [`Using the Package Manager`](https://developer.apple.comhttps://swift.org/getting-started/#using-the-package-manager) on [`swift.org`](https://developer.apple.comhttps://swift.org).

##### Swift Compiler

###### New Features

- To reduce the size taken up by Swift metadata, convenience initializers defined in Swift now only allocate an object ahead of time if they’re calling a designated initializer defined in Objective-C. In most cases, this has no effect on your app, but if your convenience initializer is called from Objective-C and doesn’t in turn delegate via `self.init` to an initializer exposed to Objective-C, the initial allocation from [`alloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571958-alloc) is released without any initializer being called. This can be problematic for users of the initializer that don’t expect any sort of object replacement to happen. One instance of this is with [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)): the implementation of [`NSKeyedUnarchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedUnarchiver) may behave incorrectly if it calls into Swift implementations of [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)) and the archived object graph contains cycles.To avoid this, ensure that convenience initializers that don’t support object replacement always delegate to initializers that are also exposed to Objective-C, either because they’re defined in Objective-C, or because they’re marked with `@objc`, or because they override initializers exposed to Objective-C, or because they satisfy requirements of an `@objc` protocol. (46823518)
- C types with an alignment greater than 16 bytes are no longer available in Swift. The Swift compiler never handled these types correctly. (31411216)
- In Swift 5 mode, the type of `self` in a convenience initializer of a nonfinal class is now the dynamic `Self` type, and not the concrete class type. (47323459)
- Exclusive memory access is now enforced at runtime by default in optimized (`-O` and `-Osize`) builds. Programs that violate exclusivity trap at runtime and produce a diagnostic message: “Simultaneous accesses to […], but modification requires exclusive access”. You can disable this using the command line flag `-enforce-exclusivity=unchecked`, but doing so may result in undefined behavior. Runtime violations of exclusivity typically result from simultaneous access of class properties or global variables—including variables in top-level code or variables captured by escaping closures. For more information, see [`Swift 5 Exclusivity Enforcement`](https://developer.apple.comhttps://swift.org/blog/swift-5-exclusivity/). ([`SR-7139`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-7139)) (37830912)
- Swift 3 mode has been removed. Supported values for the `-swift-version` flag are `4`, `4.2`, and `5`. (43101816)
- In Swift 5 mode, switches over enumerations that are declared in Objective-C or that come from system frameworks are required to handle —cases that might be added in the future, or that may be defined privately in an Objective-C implementation file. Formally, Objective-C allows storing any value in an enumeration as long as it fits in the underlying type. These unknown cases can be handled by using the new `@unknown default` case, which still provides warnings if any known cases are omitted from the switch. They can also be handled using a normal `default` case.If you’ve defined your own enumeration in Objective-C and you don’t need clients to handle unknown cases, you can use the `NS_CLOSED_ENUM` macro instead of `NS_ENUM`. The Swift compiler recognizes this and doesn’t require switches to have a default case.In Swift 4 and 4.2 modes, you can still use `@unknown default`. If you omit it and an unknown value is passed into the switch, the program traps at runtime, which is the same behavior as Swift 4.2 in Xcode 10.1. ([`SE-0192`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/master/proposals/0192-non-exhaustive-enums.md)) (39367045)
- Default arguments are now printed in SourceKit-generated interfaces for Swift modules, instead of just using a placeholder default. (18675831)
- `unowned` and `unowned(unsafe)` variables now support [`Optional`](https://developer.apple.com/documentation/Swift/Optional) types. (47326769)

###### Known Issues

- A key path literal that refers to a property in a protocol extension from another module may cause the compiler to crash. (48001932)  Avoid crossing the module boundary by defining a wrapper property in the local module, and reference the wrapper in the key path instead.
- The Swift compiler may crash during a build when the Thread Sanitizer is enabled. (48719789)  Disable Thread Sanitizer in the Scheme Editor’s Diagnostics tab.
- Linking against a static Swift library might create a binary with missing type metadata because the object files that define the metadata inside the static archive are mistakenly considered unused. (47598583) This can manifest as a Swift runtime error with a message such as: “failed to demangle superclass of `MyClass` from mangled name ”.  If you can rebuild the static library, try building it with whole module optimization enabled. Otherwise, add `-all_load` to the linker flags in the client binary to ensure all object files are linked into it.
- The expression `self.init()` is erroneously allowed in designated initializers in subclasses of [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) and [`UIView`](https://developer.apple.com/documentation/UIKit/UIView), even though `init()` is a convenience initializer on [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) and [`UIView`](https://developer.apple.com/documentation/UIKit/UIView). Using `self.init()` can result in stored properties being initialized more than once, which leads to memory leaks and other possible issues in your app. (SR-9836) (47734208)  Use `super.init(frame:)` instead.

###### Resolved Issues

- Swift command line projects won’t run on macOS 10.14.3 and earlier unless you install the Swift 5 Runtime Support for Command Line Tools package. Without that package, Swift command line projects crash on launch with “dyld: Library not loaded” errors. (46824656)
- Linking a Swift program directly from the command line with the `swiftc` compiler now results in output that runs without issue on macOS Mojave 10.14.4. (43616773)
- Compile time regressions in Xcode 10.2, as compared to Xcode 10.1, are now resolved in most cases. Some projects may continue to experience small regressions; file bug reports for cases you encounter. (47304789)
- The Swift compiler completes the “Merge swiftmodule” build step even if members of the [`UIAccessibility`](https://developer.apple.com/documentation/UIKit/UIAccessibility) structure or other types that contain `NS_ERROR_ENUM` nested types are referenced. (47152185)
- Single-element labeled tuple expressions, like `(label: 123)`, were allowed in some contexts but often resulted in surprising, inconsistent behavior that varied across compiler releases. They’re now completely disallowed. Single-element labeled , like `var x: (label: Int)`, were prohibited starting in Swift 3. ([`SR-0192`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-8109)) (41474370)
- If a key path literal refers to a property that’s defined in Objective-C or that’s defined with the `@objc` and `dynamic` modifiers in Swift, it now compiles successfully and generates the correct hash value or equality comparison with other key paths at runtime. (47184763)
- Extension binding now supports extensions of nested types which themselves are defined inside extensions. Previously this could fail with some declaration orders, producing spurious “undeclared type” errors. ([`SR-631`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-631)) (20337822)
- In Swift 5 mode, inferred associated types are no longer exposed publicly when a public type conforms to a non-public protocol. Instead, they get the minimum possible access to be visible from both the protocol and the conforming type. For source compatibility, Swift 4 and 4.2 modes continue to expose inferred associated types as publicly as the enclosing type unless the inferred associated type is itself less public than the conforming type. (46143405)
- In Swift 5 mode, a class method that returns `Self` can no longer be overridden with a method that returns a concrete class type that isn’t `final`. Such code isn’t type safe and needs to be updated. ([`SR-695`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-695)) (47322892) For example: ```swift
class Base {
    class func factory() -> Self { /*...*/ }
}

class Derived: Base {
    class override func factory() -> Derived { /*...*/ }
}
```
- In Swift 5 mode, attempting to declare a static property with the same name as a nested type is now always correctly rejected. Previously, it was possible to perform such a redeclaration in an extension of a generic type. ([`SR-7251`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-7251)) (47325738) For example: ```swift
struct Foo<T> {}

extension Foo {
    struct i {}

    // Error: Invalid redeclaration of 'i'.
    // (Prior to Swift 5, this didn't produce an error.)
    static var i: Int { return 0 }
}
```
- Designated initializers with variadic parameters are now correctly inherited in subclasses. (16331406)
- In Swift 5 mode, `@autoclosure` parameters can no longer be forwarded to `@autoclosure` arguments in another function call. Instead, you must explicitly call the function value with parentheses: `()`; the call itself is wrapped inside an implicit closure, guaranteeing the same behavior as in Swift 4 mode. ([`SR-5719`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-5719)) (37321597) For example: ```swift
func foo(_ fn: @autoclosure () -> Int) {}

func bar(_ fn: @autoclosure () -> Int) {
    foo(fn) // Incorrect, `fn` can't be forwarded and has to be called.
    foo(fn()) // OK
}
```
- Complex recursive type definitions involving classes and generics that would previously cause deadlocks at runtime are now fully supported. (38890298)
- In Swift 5 mode, when casting an optional value to a generic placeholder type, the compiler will be more conservative with the unwrapping of the value. The result of such a cast now more closely matches the result you would get in a nongeneric context. ([`SR-4248`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-4248)) (47326318) For example: ```swift
func forceCast<U>(_ value: Any?, to type: U.Type) -> U {
    return value as! U
}

let value: Any? = 42
print(forceCast(value, to: Any.self))
// Prints "Optional(42)"
// (Prior to Swift 5, this would print "42".)

print(value as! Any)
// Prints "Optional(42)"
```
- Protocols can now constrain their conforming types to those that subclass a given class. Two equivalent forms are supported: ```swift
protocol MyView: UIView { /*...*/ }

protocol MyView where Self: UIView { /*...*/ }
``` Swift 4.2 accepted the second form, but it wasn’t fully implemented and could sometimes crash at compile time or runtime. ([`SR-5581`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-5581)) (38077232)
- In Swift 5 mode, when setting a property from within its own `didSet` or `willSet` observer, the observer will now only avoid being recursively called if the property is set on `self` (either implicitly or explicitly). ([`SR-419`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-419)) (32334826) For example: ```swift
class Node {
    var children = [Node]()
    var depth: Int = 0 {
        didSet {
            if depth < 0 {
                // Won't recursively call didSet, because this is setting depth
                on self.
                depth = 0
            }

            // Will call didSet for each of the children,
            // as this isn't setting the property on self.
            // (Prior to Swift 5, this didn't trigger property
            // observers to be called again.)
            for child in children {
                child.depth = depth + 1
            }
        }
    }
}
```
- `#sourceLocation` is now honored when diagnostics are emitted in Xcode. That is, if your source uses `#sourceLocation` to map lines in a generated file back to the original source, diagnostics now show up in the original source file rather than in the generated file. (43647151)
- Using a generic type alias as the parameter or return type of an `@objc` method no longer results in the generation of an invalid Objective-C header. ([`SR-8697`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-8697)) (43347303)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/swift-5-release-notes-for-xcode-10_2)*