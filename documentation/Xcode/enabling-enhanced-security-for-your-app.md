# Enabling enhanced security for your app

**Framework**: Xcode

Detect out-of-bounds memory access, use of freed memory, and other potential vulnerabilities.

#### Overview

People’s devices can contain a large amount of sensitive data that an attacker might want to use for malicious purposes. If your app contains any security vulnerabilities, an attacker may exploit the vulnerabilities to access or modify the data in your app, extension, App Clip, or device driver.

Adopt the Enhanced Security capability in your Xcode project to enable a collection of build settings and entitlements designed to mitigate certain common vulnerabilities in your app. Review the behavior of your app with these settings enabled, and fix any problems that Xcode and the system report.

> ❗ **Important**:  The Enhanced Security capability enables security checks that can impact the performance and stability of an app that isn’t designed and built with security in mind. Review your app’s threat model, and only adopt the Enhanced Security capability if the protections it enables align with your app’s security goals. Test your app thoroughly to ensure that you address all situations in which Enhanced Security mitigations could lead to your app crashing.

Enhanced Security compiler settings and runtime checks are available for apps and extensions built for iOS, iPadOS, macOS, and visionOS; App Clips in iOS; and DriverKit extensions in iPadOS and macOS. Additionally, you can create Enhanced Security helper extensions on iOS, iPadOS, and macOS to which the system provides further protections; for more information, see [`Creating enhanced security helper extensions`](creating-enhanced-security-helper-extensions.md).

##### Adopt the Enhanced Security Capability

Navigate to the Signing and Capabilities editor for your Xcode target, and click the Add Capability button. From the list of capabilities, select Enhanced Security. Xcode adds the following entitlements to your app’s provisioning profile:

- [`Enhanced Security`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.enhanced-security-version): Xcode sets the value to `1`.
- [`Hardened Process`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process): Xcode sets the value to `true`.
- [`Hardened Heap`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.hardened-heap): Xcode sets the value to `true`.
- [`Additional Runtime Platform Restrictions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.platform-restrictions): Xcode sets the value to `2`.
- [`Enable Read-Only Platform Memory`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.dyld-ro): Xcode sets the value to `true`.

When you add the Enhanced Security capability to your target, use the checkboxes in the Enhanced Security capability of the Signing and Capabilities editor to adopt specific hardening features. Additionally, click Enable Build Settings to add security-related build settings to all targets in your project, which turns on certain hardening features.

The sections below describe the individual entitlements and build settings that comprise Enhanced Security, and the steps you can take to adopt the hardening features in your code. Additionally, the sections describe how you can turn off any individual hardening setting, in case you need to do so while you prepare your code to support the additional protections.

##### Prepare Your App for Pointer Authentication

The Enhanced Security capability includes additional runtime platform restrictions, which Xcode enables by default for your app when you adopt the capability by setting the `ENABLE_POINTER_AUTHENTICATION` build setting to `Yes`. With these additional runtime platform restrictions enabled, Xcode builds your app for the `arm64e` architecture and enables .

When you enable pointer authentication, the system generates signature metadata for pointers that your app creates by allocating memory or constructing C++ objects. Then the system validates that the signatures are unchanged when your app accesses the memory addressed by those pointers. If the signature for a pointer isn’t valid, the system encounters an exception and crashes your app. Doing so helps to protect against an attacker overwriting memory in your app to compromise the app’s control flow.

To adopt pointer authentication, use the `__ptrauth` type qualifier to instruct the compiler to generate pointer authentication protection for variables in your code that store data and function pointers.

When a variable uses pointer authentication, the system throws an error if you overwrite its value with a raw pointer in your code, or copy its value to another variable that uses a different pointer authentication schema. If your app does either of these, the system encounters an exception and crashes your app. Instead, sign the pointer before storing it, re-signing it for a different use if necessary. For more information, see [`Improving control flow integrity with pointer authentication`](https://developer.apple.com/documentation/Apple-Silicon/improving-control-flow-integrity-with-pointer-authentication).

If you need to turn off pointer authentication for your target, uncheck the Authenticate Pointers checkbox in the Signing and Capabilities editor, or set the `ENABLE_POINTER_AUTHENTICATION` build setting to `No`.

##### Adopt Typed Allocator Support

When you adopt the Enhanced Security capability, Xcode configures build settings to enable the compiler’s typed allocator in C and C++ code. For more information on the typed allocator and the changes you need to make in your code if you use custom memory-allocator wrapper functions, see [`Adopting type-aware memory allocation`](adopting-type-aware-memory-allocation.md).

To turn off typed allocator support for your target, uncheck the Enable Typed Allocators checkbox in the Signing and Capabilities editor, or set the `CLANG_ENABLE_C_TYPED_ALLOCATOR_SUPPORT` build setting to `No` for C code, and the `CLANG_ENABLE_CPLUSPLUS_TYPED_ALLOCATOR_SUPPORT` build setting to `No` for C++ code.

##### Adopt Memory Integrity Enforcement

When you enable hardware memory tagging, each new memory allocation and any pointers to that memory include an embedded value called a . Accessing to memory through a pointer requires that the pointer’s tag matches the allocation’s tag. If the tags don’t match — for example, because of a use-after-free error or out-of-bounds access — the app crashes instead of performing the unsafe access.

To enable memory tagging, navigate to the Signing and Capabilities editor for your Xcode target. Enable the Enhanced Security capability, then, under Memory Safety, click Enable Hardware Memory Tagging. Xcode adds the [`Enable Hardware Memory Tagging`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.checked-allocations) entitlement to your app.

To enable additional diagnostics while debugging, navigate to the Scheme Editor and select the Run action, then select the Diagnostics pane and enable Hardware Memory Tagging.

When you enable memory tagging in Xcode, it also adds the [`Enable Soft Mode for Memory Tagging`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.checked-allocations.soft-mode) entitlement. This entitlement makes hardware memory tagging operate in , where the system produces a simulated crash instead of terminating the app if a pointer’s tag doesn’t match the memory allocation’s tag. You can review reports from simulated crashes to help you find memory issues and to help validate that your app doesn’t have memory corruption bugs that would result in crashes when soft mode is disabled. After you’re confident in the stability of your app, disable soft mode to protect your users. To disable soft mode, navigate to the Signing and Capabilities editor for your Xcode target, then, under Memory Safety, deselect Enable Soft Mode for Memory Tagging.

You can also enable the [`Memory Tag Pure Data`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.checked-allocations.enable-pure-data) and [`Prevent Receiving Tagged Memory`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.checked-allocations.no-tagged-receive) entitlements.

> **Note**:  This setting is available on iOS 26 and later on iPhone 17, iPhone 17 Pro, iPhone 17 Pro Max, or iPhone Air.

##### Initialize Stack Variables to Zero

When you enable the Enhanced Security capability for your target, Xcode sets the `CLANG_ENABLE_STACK_ZERO_INIT` build setting to `Yes`. This build setting configures the compiler to initialize automatic variables in your code with zeroes. Doing so helps to protect against particular types of use-after-free vulnerability, because your app zeroes out previous values in stack memory before it reuses them for other variables.

If you need to turn off zero-initialization of stack variables for your target, set the `CLANG_ENABLE_STACK_ZERO_INIT` build setting to `No`.

##### Address Security Related Compiler Warnings

When you enable the Enhanced Security capability for your target, Xcode configures some compiler warnings that help to identify potentially insecure code. These are:

Xcode additionally sets the `ENABLE_SECURITY_COMPILER_WARNINGS` target build setting to `Yes`. This turns on a collection of security-related compiler warnings that Xcode reports in the Issues navigator when you build the target. These additional warnings are:

If you need to turn off the additional compiler warnings that Enhanced Security configures for your target, set the `ENABLE_SECURITY_COMPILER_WARNINGS` build setting to `No`.

##### Adopt C++ Standard Library Hardening and Compiler Bounds Checking

When you enable the Enhanced Security capability for your target, Xcode sets the `ENABLE_CPLUSPLUS_BOUNDS_SAFE_BUFFERS` target build setting to `YES`. This enables a collection of safety checks in the C++ standard library. Specifically, it enables the  hardening mode.

In fast mode, the C++ standard library performs the following assertion checks in your code that uses standard library container types:

The standard library calculates these checks in constant time. If a hardening assertion fails (that is, if the check evaluates to `false`), the system encounters an exception and crashes your app.

To change the C++ standard library hardening mode for a single file in your project, define the `_LIBCPP_HARDENING_MODE` macro with one of the following values:

If you define the macro in code, you need to place the definition at the beginning of the file, before you include any standard library headers.

Additionally, setting `ENABLE_CPLUSPLUS_BOUNDS_SAFE_BUFFERS` to `Yes` adds compiler warnings on unsafe buffer usage in C++, configuring the compiler to treat these warnings as errors. The C++ compiler encounters an error if it detects that your code:

- Indexes an array, performs pointer arithmetic, or uses an unsafe C standard library function on a raw pointers
- Calls `operator[]()` on a smart pointer that refers to a list of objects
- Constructs a `std::span` object using the two-argument (pointer and size) constructor

To turn off C++ standard library hardening and compiler bounds checking for your target, set the `ENABLE_CPLUSPLUS_BOUNDS_SAFE_BUFFERS` build setting to `No`.

For more information on C++ standard library hardening, see [`Hardening Modes`](https://developer.apple.comhttps://libcxx.llvm.org/Hardening.html) in the LLVM documentation.

##### Adopt Additional Run Time Restrictions

When you enable the Enhanced Security capability for your target, Xcode adds the [`Additional Runtime Platform Restrictions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.platform-restrictions) entitlement to your app. This entitlement informs the system to perform additional checks on dynamic libraries your app or extension loads, and on Mach messages your app or extension receives from other processes.

If you use [`XPC`](https://developer.apple.com/documentation/XPC) for inter-process communication (IPC) and don’t use Mach IPC traps, or don’t have any explicit IPC mechanism in your app or extension, enabling additional run-time restrictions turns on protections that are unlikely to require you to make any code changes.

In apps and extensions that use Mach IPC traps, additional run-time restrictions turn potentially insecure situations into crashes to avoid giving an attacker privileged access to your process via Mach ports. For information on interpreting these crashes and changes to your code that avoid potentially insecure use of Mach messaging APIs, see [`Conforming to Mach IPC security restrictions`](conforming-to-mach-ipc-security-restrictions.md).

To turn off additional run-time restrictions for your target, uncheck the Enable Additional Runtime Platform Restrictions checkbox in the Signing and Capabilities editor.

##### Adopt Read Only Memory for Internal Platform State

When you enable the Enhanced Security capability for your target, Xcode adds the [`Enable Read-Only Platform Memory`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.dyld-ro) entitlement to your app. This entitlement informs the system to mark regions of memory in your process that the platform uses for its internal state as read-only.

In most situations, this additional protection doesn’t require you to make any changes. If your app modifies data in the protected regions — for example, it modifies the value of `const` data sections — the system crashes your app when you adopt this entitlement. To fix the crash, remove the code that modifies the read-only memory regions.

If you need to turn off read-only memory for the dynamic loader, uncheck the Enable Read-Only Platform Memory checkbox in the Signing and Capabilities editor.

##### Adopt Bounds Checking in C

Optionally, enable bounds checking for your target that complements the security features in Enhanced Security.

The `ENABLE_C_BOUNDS_SAFETY` build setting adds the `-fbounds-safety` flag to the compiler invocation when Xcode compiles C source files. This is an extension to the C programming language that prevents out-of-bounds memory access by enforcing bounds safety.

The compiler assumes that every pointer in your code that it compiles with the `-fbounds-safety` flag points to a single object, and emits an error if you attempt to perform pointer arithmetic using the pointer, or use a subscript to access an array element based on the pointer. To indicate that a pointer identifies a collection of objects of a given size, use one of these annotations:

If the pointer can potentially be `NULL`, add the suffix `_or_null` to the annotation name; for example, `__counted_by_or_null(N)`.

To indicate that a pointer identifies a collection of objects that has a particular sentinel value signifying the end — for example, a null-terminated string — use one of these annotations:

To indicate that a pointer refers to a value that you haven’t audited for bounds safety, add the `__unsafe_indexable` annotation.

For more information, see [`-fbounds-safety: Enforcing bounds safety for C`](https://developer.apple.comhttps://clang.llvm.org/docs/BoundsSafety.html) on the LLVM website.

To turn off bounds checking in C, set the value of the `ENABLE_C_BOUNDS_SAFETY` build setting to `No`.

## See Also

- [Verifying the origin of your XCFrameworks](verifying-the-origin-of-your-xcframeworks.md)
  Discover who signed a framework, and take action when that changes.
- [Creating enhanced security helper extensions](creating-enhanced-security-helper-extensions.md)
  Reduce opportunities for an attacker to target your app through its extensions.
- [Adopting type-aware memory allocation](adopting-type-aware-memory-allocation.md)
  Reduce the opportunities to treat pointers as data in your code.
- [Conforming to Mach IPC security restrictions](conforming-to-mach-ipc-security-restrictions.md)
  Avoid crashes and potentially insecure situations associated with Mach messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/enabling-enhanced-security-for-your-app)*