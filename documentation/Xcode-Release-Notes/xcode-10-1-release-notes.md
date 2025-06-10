# Xcode 10.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 10.1 includes SDKs for iOS 12.1, watchOS 5.1, macOS 10.14.1, and tvOS 12.1. Xcode 10.1 supports on-device debugging for iOS 8 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 10.1 requires a Mac running macOS 10.13.6 or later.

##### General

###### New Features

- Support for arm64e (Preview)To try the developer preview of arm64e, select your iOS app target in the Project Editor, find its Architectures build setting, select the Other… option, and add arm64e to the list of architectures. For more information, see [`Preparing your app to work with pointer authentication`](https://developer.apple.com/documentation/Security/preparing-your-app-to-work-with-pointer-authentication). The App Store and TestFlight don’t accept submissions containing arm64e. Xcode will remove arm64e content from your app when you distribute from the Organizer window. (42296212)

###### Resolved Issues

- The navigation UI for Navigate > Open in… no longer displays individual tabs in a window as separate windows with one tab each. (31716375)
- The `xed` tool now uses the Xcode currently specified by `xcode-select` or the `DEVELOPER_DIR` environment variable. (7711481)

##### Apple Clang Compiler

###### Resolved Issues

- Changes to libunwind in iOS 12.1 beta 2 resolved an issue with a small number of apps running on iPhone XS and iPhone XS Max. (44361223)

##### Asset Catalog

###### Known Issues

- Apps that contain asset catalogs built using Xcode 10 or later with a deployment target of iOS 9.0, 9.1 or 9.2 produce content incompatible with the runtimes of those iOS versions when you’re using app thinning as part of exporting an archive for local or enterprise distribution. (46893768)

###### Resolved Issues

- Resolved an issue that affected app compatibility with iOS 9.0, 9.1, and 9.2 when distributing an app on the App Store. App asset catalogs built using Xcode 10 with a deployment target of iOS 9.0, 9.1 or 9.2 produce content incompatible with the runtimes of those iOS versions when distributed via the App Store. Rebuild and resubmit the app using Xcode 10.1 to resolve the issue. (44535967, 45723580, 45723189)
- The 40mm and 44mm wells for complications specify the correct icon sizes. (43069075, 43401397)

##### Build System

###### Resolved Issues

- The new build system supports On Demand Resources (ODR). (31508570)
- Fixed an issue where individual localized `.xib` files or storyboards associated with the base file wouldn’t be compiled into the product when using base localization for a `.xib` file or storyboard. (44437269)

##### Debugging

###### New Features

- The Breakpoint editor for Exception breakpoints now has an “ignore count” field. (21547530)

##### Devices

###### Resolved Issues

- Devices running iOS 12 or later take screenshots requested from the Devices window. (42873539)

##### Interface Builder

###### New Features

- Control-dragging in the canvas to add constraints now always includes all four directions, not just the ones closest to the direction of the drag. (43618031)

###### Resolved Issues

- Fixed an issue with Auto Layout incorrectly reporting issues when constraining views to [`UIScrollView`](https://developer.apple.com/documentation/UIKit/UIScrollView) subviews. (44457610)
- Improved canvas performance when switching between iPhone XS, iPhone XS Max, and iPhone XR with the device bar. (44605631)
- Fixed an issue that caused the layout of watch content in the Preview assistant editor to not match the Device Bar selection. (42563683)
- `@IBDesignable` views now build using the new build system when it’s enabled. (31433718)

##### Simulator

###### Known Issues

- If another process, such as `simctl`, shuts down a simulated device while Simulator is open, Simulator doesn’t reconnect to it properly when the device is next booted. If you have multiple versions of Xcode installed, you might experience this issue when running Simulator in those other versions. (44629720)  Quit and relaunch Simulator. To quit without shutting down all simulators, hold Option and choose Simulator > Quit Simulator…, then choose “Keep Running” in the dialog that appears.

##### Swift Compiler

###### Known Issues

- If you indirectly modify a property using a nonmutating setter that’s defined in a protocol or extension on a class instance, the Swift compiler might miscompile it by releasing the instance after the getter is invoked. This might cause the program to crash or have unpredictable behavior at runtime. (45274900) For example: ```swift
protocol SomeProtocol { }
class SomeClass: SomeProtocol { }
  
extension SomeProtocol {
    var someNonmutatingProperty: CGPoint {
        nonmutating set { _ = self }
        get { return .zero }
    }
}
  
// Might be miscompiled, deallocating SomeClass() too early.
SomeClass().someNonmutatingProperty.x = 42
```  Break the operation up into multiple statements so that the `get` and `set` operations occur in different statements: ```swift
let someObject = SomeClass()
// First get the nonmutating property value.
var temp = someObject.someNonmutatingProperty
temp.x = 42
// Then modify it.
someObject.someNonmutatingProperty = temp
```

###### Resolved Issues

- Playgrounds in Xcode no longer log messages about fields whose types fail to demangle at runtime. (44642942)
- Compilation now consistently reports the errors responsible for any failures. For example, previously, a message like “Command CompileSwiftSources failed with a nonzero exit code” could occur without an accompanying failure reason. (43033749, 44362180)
- Long file paths containing white space no longer cause build failures. (44142091)
- The [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) class’s [`init(for:)`](https://developer.apple.com/documentation/Foundation/Bundle/init(for:)) initializer now works consistently with Swift classes, including when not running on the latest operating system versions. (44489216)
- A `let` property of a generic class that has function type as an argument can now be passed successfully to another function or method. (41056468) ```swift
class A<B> {
    let function: (B) -> B
}
func takeFunction(_: (Int) -> Int) {}
  
func passFunction(from a: A<Int>) {
    takeFunction(a.function)
}
```
- Changes made to a captured value in a nested context is now reflected in the outer context. ([`SR-8398`](https://developer.apple.comhttps://bugs.swift.org/browse/SR-8398)) (42742744)
- A mutating method that returns `Self` on a value of protocol type can now successfully be invoked (43507711): ```swift
protocol Example {
    mutating func test() -> Self
}
  
func foo(x: inout Example) {
    _ = x.test() // No longer crashes the compiler sometimes.
}
```
- The compiler can now successfully form an array of heterogeneous class objects as an `AnyObject` array (42666956): ```swift
func f(_: [AnyObject])
  
f([NSObject.self, NSString.self])
```

##### Swift Standard Library

###### Resolved Issues

- The [`FixedWidthInteger`](https://developer.apple.com/documentation/Swift/FixedWidthInteger) protocol’s `unsafeAdding(_:)`, `unsafeSubtracting(_:)`, `unsafeDivided(by:)`, and `unsafeMultiplied(by:)` methods are now deprecated and will be removed in a future release.These methods produce undefined behavior in overflow conditions. In the case of arithmetic operations, use a combination of an assert and either the [`addingReportingOverflow(_:)`](https://developer.apple.com/documentation/Swift/FixedWidthInteger/addingReportingOverflow(_:)) method or the `&+` operator, both of which have well-defined results in cases of overflow. (43688685)

##### Source Control

###### Resolved Issues

- Organizational repositories now show up alongside personal repositories when cloning from GitLab.com or GitLab self-hosted accounts.

##### Testing

###### Known Issues

- Profiling tests does not behave correctly when test parallelization is enabled. (44836817)  Disable parallel testing while profiling by navigating to Product > Scheme > Edit Scheme… > Test > Info. Select the Options button next to your test target, and disable the “Execute in parallel” checkbox.

###### Resolved Issues

- UI tests in projects using the legacy build system now run on iPhone XS and iPhone XS Max. (44777186)
- If a UI test target app crashes during testing in Simulator, it’s now correctly reported as a test failure instead of either being incorrectly considered a successful test or displaying a failure message about “Application state unknown”. (44765263)
- Xcode 10.1 beta 2 and later support UI testing with devices running beta versions of iOS 12. (43796360)
- Fixed an issue where the [`testBundleDidFinish(_:)`](https://developer.apple.com/documentation/XCTest/XCTestObservation/testBundleDidFinish(_:)) method wouldn’t be called on an observer added to the shared [`XCTestObservationCenter`](https://developer.apple.com/documentation/XCTest/XCTestObservationCenter) instance if the observer was added at any point after testing had already started. (For example, after the [`testBundleWillStart(_:)`](https://developer.apple.com/documentation/XCTest/XCTestObservation/testBundleWillStart(_:)) method had been called on all the currently registered observers). (44340337)
- The [`XCUIElement`](https://developer.apple.com/documentation/XCTest/XCUIElement) class’s [`click()`](https://developer.apple.com/documentation/XCTest/XCUIElement/click()) and [`hover()`](https://developer.apple.com/documentation/XCTest/XCUIElement/hover()) methods now automatically scroll menus when the receiver is a menu item or subview of a menu item. (43510448)

## See Also

- [Xcode 10.3 Release Notes](xcode-10_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10.2.1 Release Notes](xcode-10_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10.2 Release Notes](xcode-10_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 10 Release Notes](xcode-10-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-10_1-release-notes)*