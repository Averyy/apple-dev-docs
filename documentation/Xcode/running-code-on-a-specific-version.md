# Running code on a specific platform or OS version

**Framework**: Xcode

Add conditional compilation markers around code that requires a particular family of devices or minimum operating system version to run.

#### Overview

When you invest time developing a new feature for an app, you want to get the maximum value out of the code you write. Creating a new project to support a new platform or operating system version adds unnecessary work, especially if most of your code stays the same. The best solution is to maintain one version of your app that runs on multiple platforms and operating system versions. To achieve this, compile code conditionally for the target platform, or use availability condition checks to run code based on operating system version.

##### Compile Code for a Specific Platform

Apple platforms support many of the same technologies, but some features might not be available on every platform. For example, features on iOS devices might not make sense on a macOS devices. To prevent code from compiling on an operating system that doesn’t support the corresponding feature, add a conditional compilation block to specify the target operating system.

```swift
/// Swift
/// `iOS` specifies the operating system for which this code compiles. 
/// Change `iOS` to specify another operating system.
#if os(iOS)
   // iOS code
#endif
```

```objc
/// Objective-C
/// `IOS` specifies the operating system for which this code compiles. 
/// Change `IOS` to specify another operating system. For the list of 
/// compilation macros, see the /usr/include/TargetConditionals.h 
/// header file in the appropriate SDK.
#if TARGET_OS_IOS
   // iOS code
#endif
```

You can also compile or prevent compiling for specific environments, such as Simulator or Mac Catalyst.

```swift
/// Swift
/// `simulator` specifies an environment to compile the code for. 
/// Change `simulator` to specify another environment, such as `macCatalyst`.
#if targetEnvironment(simulator)
    // code for Simulator
#endif

```

```objc
/// Objective-C
/// `SIMULATOR` specifies an environment this code depends on. 
/// Change `SIMULATOR` to specify another environment, such as `MACCATALYST`.
#if TARGET_OS_SIMULATOR
    // code for Simulator
#endif
```

If your Swift code relies on a specific Swift package or framework, you can check to see whether you can import the package or framework. This condition tests whether it’s possible to import a module, but doesn’t actually import it. This type of check has the advantage that your code uses the package or framework if a future version of the operating system makes it available.

```swift
/// Swift
/// `UIKit` specifies a module this code depends on. 
/// Change `UIKit` to specify another module.
#if canImport(UIKit)
    // code that requires UIKit
#endif
```

For more information on the compiler control statements and the platforms conditions they support, see [`Compiler Control Statements`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements/#Compiler-Control-Statements) in the Swift language documentation.

##### Require a Minimum Operating System Version for a Feature

Your app’s minimum deployment target defines the range of operating system versions your app supports. Rather than require the latest system software for each app update, target one or two older operating system versions to give people time to transition gradually. When you implement features found only in the most recent operating system version, wrap your code with availability markers.

- In Swift, use the `#available` compiler control statement to run code conditionally.
- In Objective-C, use the `@available` compiler directive to run code conditionally.

Platform names support both major and minor revision numbers for releases, as shown in the following example:

```swift
/// Swift
if #available(iOS 15.4.1, *) {
    // On iOS, this branch runs in versions 15.4.1 and greater. 
    // On any other OS, this branch runs in any version of that OS.
} else {
   // This branch runs in earlier iOS versions.
}
```

```objc
/// Objective-C
if (@available(iOS 15.4.1, *)) {
    // On iOS, this branch runs in versions 15.4.1 and greater. 
    // On any other OS, this branch runs in any version of that OS.
} else {
   // This branch runs in earlier iOS versions.
}
```

The `*` matches any other operating system. To specify versions for multiple operating systems, include multiple operating system names separated by commas.

```swift
// Swift
if #available(iOS 15, macOS 12, *) {
    // On iOS, this branch runs in iOS 15 or later.
    // On macOS, this branch runs in macOS 12 or later.
    // On any other OS, this branch will run in any version of that OS.
} else {
   // This branch runs in earlier iOS and macOS versions.
}
```

```objc
// Objective-C
if (@available(iOS 15, macOS 12, *)) {
    // On iOS, this branch runs in iOS 15 or later.
    // On macOS, this branch runs in macOS 12 or later.
    // On any other OS, this branch will run in any version of that OS.
} else {
   // This branch runs in earlier iOS and macOS versions.
}
```

For more information on the availability condition statement, see [`Availability Condition`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements/#Availability-Condition) in the Swift language documentation.

##### Annotate Declarations in Your Code

You can reduce the number of conditional runtime checks your app performs by factoring code with common requirements together and annotating your declarations.

- In Swift, use the `@available` attribute to indicate a declaration is available.
- In Objective-C, use the `API_AVAILABLE` macro to add availability information.

```swift
@available(iOS 15, macOS 12, *)
func newMethod() {
    // Use iOS 15 APIs.
}
```

```objc
@interface MyViewController : UIViewController
- (void) newMethod API_AVAILABLE(ios(15));
@end
```

With the above annotation in place, calling `newMethod` might still require a compiler control statement, but you remove the need to check again inside the body.

For more information about marking availability in Swift, see [`available`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes/#available).

## See Also

- [Customizing the build schemes for a project](customizing-the-build-schemes-for-a-project.md)
  Specify which targets to build, and customize the settings Xcode uses to build, run, test, and profile those targets.
- [Customizing the build phases of a target](customizing-the-build-phases-of-a-target.md)
  Specify the tasks to perform during a build, including the source files to compile, the scripts to run, and the resources to include in the final product.
- [Creating build rules for custom file types](creating-build-rules-for-custom-file-types.md)
  Tell Xcode how to build your project’s custom file types, and provide dependency information to optimize the build process for each file.
- [Running custom scripts during a build](running-custom-scripts-during-a-build.md)
  Execute custom shell scripts during the build process, and run tools or other commands that your project requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/running-code-on-a-specific-version)*