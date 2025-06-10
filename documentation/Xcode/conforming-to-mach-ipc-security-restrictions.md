# Conforming to Mach IPC security restrictions

**Framework**: Xcode

Avoid crashes and potentially insecure situations associated with Mach messages.

#### Overview

Mach ports represent low-level inter-process communication (IPC) capabilities on the system, and as such are a fundamental and powerful construct. An attacker who gains access to a Mach port for your app or extension potentially gains a lot of privileges they can use to attack your app and other resources on the system.

Higher-level IPC mechanisms, including the Mach Interface Generator (MIG) and [`XPC`](https://developer.apple.com/documentation/XPC), are designed to mitigate many of the security issues related to Mach IPC. Using Mach IPC traps directly doesn’t take advantage of these mitigations, and is very difficult to do correctly. Adopt the [`Additional Runtime Platform Restrictions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.platform-restrictions) entitlement in the Enhanced Security capability to turn potentially insecure misuse of Mach and VM APIs into crashes, and use the crash reports to diagnose and fix or remove the potentially insecure code.

##### Replace Mach Ipc Traps with Other Ipc Mechanisms

The easiest way to fix potentially insecure use of Mach IPC traps is to completely avoid using the API. Instead, use a different IPC mechanism that avoids the potentially insecure situations, for example, [`XPC`](https://developer.apple.com/documentation/XPC).

##### Diagnose Crashes Due to Additional Run Time Platform Restrictions

If your process has the [`Additional Runtime Platform Restrictions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.platform-restrictions) entitlement with a value of at least `1` and the system detects a potentially insecure use of Mach IPC, the system crashes your process. The crash report has an exception type of `EXC_GUARD`, and exception subtype of `GUARD_TYPE_MACH_PORT`. The exception message in the crash report is one of these values:

## See Also

- [Verifying the origin of your XCFrameworks](verifying-the-origin-of-your-xcframeworks.md)
  Discover who signed a framework, and take action when that changes.
- [Enabling enhanced security for your app](enabling-enhanced-security-for-your-app.md)
  Detect out-of-bounds memory access, use of freed memory, and other potential vulnerabilities.
- [Creating extensions with enhanced security](creating-extensions-with-enhanced-security.md)
  Reduce opportunities for an attacker to target your app through its extensions.
- [Adopting type-aware memory allocation](adopting-type-aware-memory-allocation.md)
  Reduce the opportunities to treat pointers as data in your code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/conforming-to-mach-ipc-security-restrictions)*