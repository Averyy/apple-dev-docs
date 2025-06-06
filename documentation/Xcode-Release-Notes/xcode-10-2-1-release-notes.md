# Xcode 10.2.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 10.2.1 includes SDKs for iOS 12.2, watchOS 5.2, macOS 10.14.4, and tvOS 12.2. Xcode 10.2.1 supports on-device debugging for iOS 8 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 10.2.1 requires a Mac running macOS 10.14.3 or later.

##### Apple Clang Compiler

###### Resolved Issues

- Simulator builds of watchOS projects that emit bitcode no longer fail with the error message: “GNU-style inline assembly is disabled.” (48903352)

##### Build System

###### Resolved Issues

- Resolved an issue that would produce a spurious “ignoring build task” warning when building localized Siri Intents. (49649474)

##### Lldb

###### Resolved Issues

- When importing Swift modules, LLDB now applies the `target.source-map` and the `DBGSourcePathRemapping` dictionary in the `.dSYM` bundle to the `-fmodule-map-file` option. This impacted alternative build systems that rely on path-remapping to access debug information. (49539481)

##### Localization

###### Resolved Issues

- Fixed a crash that could occur when modernizing localized content. (49575302)

##### Simulator

###### Known Issues

- Simulators for iOS 9.3 and earlier might fail to launch Swift apps with the message: “dyld: Library not loaded: /usr/lib/libauto.dylib”. (49326587)  Run the following command in Terminal for the relevant version of iOS: ```shell
sudo mkdir '/Library/Developer/CoreSimulator/Profiles/Runtimes/iOS 9.3.simruntime/Contents/Resources/RuntimeRoot/usr/lib/swift'
```

##### Swift Compiler

###### Known Issues

- In some cases, compilation may fail without emitting a specific error. (49303574)  Disable batch mode by adding the `SWIFT_ENABLE_BATCH_MODE` custom build setting and setting it to `NO`. If you’re invoking `swift` directly, include `-disable-batch-mode` on the command line.
- If you set the Reflection Metadata Level build setting to `None`, you might get a linker error about a missing nominal type descriptor when building a Swift project. (49710077)  Change the setting to `All`.
- Using an `@objc` designated initializer as a protocol witness always creates an instance of the base class, even if the protocol requirement is called on the metatype of a subclass. (49560721) For example, the following code should create an instance of `DerivedClass`, but actually creates an instance of `BaseClass`: ```swift
protocol Initable {
    init()
}

class BaseClass: NSObject, Initable {
    required override init() {
        super.init()
    }
}

class DerivedClass: BaseClass {}

let type: Initable.Type = DerivedClass.self
print(type.init())
```  Either declare the initializer as `@nonobjc`, or replace the protocol’s initializer requirement with a static method, as follows: ```swift
protocol Initable {
    static func construct() -> Self
}

class BaseClass: NSObject, Initable {
    required override init() {
        super.init()
    }

    static func construct() -> Self {
        return self.init()
    }
}

class DerivedClass: BaseClass {}
```

###### Resolved Issues

- A build time regression associated with Swift files that define a large number of types has been resolved. (49022293)
- The Swift compiler now applies the `-fdebug-prefix-map` to path names in Clang module import debug information records. (49539327)
- Indexing an invalid class that has circular inheritance during a debug build no longer hangs the compiler. ([`SR-10236`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-10236), 49539370)
- Resolved a memory usage issue associated with whole module optimization mode. (49586719)
- Resolved a build-time crash that occurred when the Thread Sanitizer was enabled. (49539420)
- Checking validity of the conditional requirements associated with constrained type extensions, such as when using synthesized protocol conformance code, now completes correctly. (49539169)
- When you declare enumerations that contain a single case with an associated value and multiple cases without an associated value, the compiler now properly distinguishes the cases without associated values. ([`SR-10221`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-10221), 49539226) ```swift
enum SomeEnum {
    case payloadCase(defaultUnknownInnerValue: Int),
    nonPayloadCase1,
    nonPayloadCase2

    var isNonPayloadCase1: Bool {
        switch self {
        case .nonPayloadCase1:
            return true
        default:
            return false
        }
    }
}
``` The compiler now properly distinguishes between .`nonPayloadCase1` and `.nonPayloadCase2`.

##### Swift Package Manager

###### Resolved Issues

- The `swift package generate-xcodeproj` command now handles submodules in the top-level package. (49535554)

## See Also

- [Xcode 10.3 Release Notes](xcode-10_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10.2 Release Notes](xcode-10_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10.1 Release Notes](xcode-10_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10 Release Notes](xcode-10-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-10_2_1-release-notes)*