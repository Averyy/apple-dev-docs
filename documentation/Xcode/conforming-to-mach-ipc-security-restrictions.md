# Conforming to Mach IPC security restrictions

**Framework**: Xcode

Avoid crashes and potentially insecure situations associated with Mach messages.

#### Overview

Mach ports represent low-level inter-process communication (IPC) capabilities on the system, and as such are a fundamental and powerful construct. An attacker who gains access to a Mach port for your app or extension potentially gains a lot of privileges they can use to attack your app and other resources on the system.

Higher-level IPC mechanisms, including the Mach Interface Generator (MIG) and [`XPC`](https://developer.apple.com/documentation/xpc), are designed to mitigate many of the security issues related to Mach IPC. Using Mach IPC traps directly doesn’t take advantage of these mitigations, and is very difficult to do correctly. Adopt the [`com.apple.security.hardened-process.platform-restrictions`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.platform-restrictions) entitlement in the Enhanced Security capability to turn potentially insecure misuse of Mach and VM APIs into crashes, and use the crash reports to diagnose and fix or remove the potentially insecure code.

##### Replace Mach Ipc Traps with Other Ipc Mechanisms

The easiest way to fix potentially insecure use of Mach IPC traps is to completely avoid using the API. Instead, use a different IPC mechanism that avoids the potentially insecure situations, for example, [`XPC`](https://developer.apple.com/documentation/xpc).

##### Diagnose Crashes Due to Additional Run Time Platform Restrictions

If your process has the [`com.apple.security.hardened-process.platform-restrictions`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.platform-restrictions) entitlement with a value of at least `1` and the system detects a potentially insecure use of Mach IPC, the system crashes your process. The crash report has an exception type of `EXC_GUARD`, and exception subtype of `GUARD_TYPE_MACH_PORT`. The exception message in the crash report is one of these values:

- **`REQUIRE_REPLY_PORT_SEMANTICS`**: The system detected a situation in which a malicious process can potentially divert or intercept a Mach message your process uses to communicate with a service that’s managed by `launchd`. Communicate with the service using XPC instead of Mach IPC traps.
- **`KOBJECT_REPLY_PORT_SEMANTICS`**: The system detected a situation in which a malicious process can potentially divert or intercept a Mach message your process uses to communicate with the kernel. Use functions in `libSystem` to access kernel capabilities, or use the kernel’s MIG interface to call kernel APIs.
- **`OOL_PORT_ARRAY`**: The system detected a situation in which your process uses an insecure descriptor layout with a MIG interface or Mach IPC trap. Replace your use of Mach messaging with XPC; alternatively, change your MIG interface so that it doesn’t send arrays of Mach ports.
- **`THREAD_SET_STATE`**: The system detected that your process calls [`thread_set_state`](https://developer.apple.com/documentation/kernel/1418827-thread_set_state) on one of its threads, in a potentially insecure way. This API provides full control over the state of any thread in your process, which an attacker can use to alter your process’s control flow. Don’t call `thread_set_state`. If you call `thread_set_state` in a Mach exception handler, rewrite your handler to use secure exception behavior. See `SET_EXCEPTION_BEHAVIOR`, below.
- **`SET_EXCEPTION_BEHAVIOR`**: The system detected that your processes sets exception ports on a process that uses an insecure Mach exception behavior. Exception behaviors including `EXCEPTION_DEFAULT` are insecure because they send receivers a task or thread port along with the exception message, which gives attackers who can intercept the exception message a way to control that task or thread. With additional run-time platform restrictions enabled, your process can only set exception ports on a process that uses the Mach exception behavior `EXCEPTION_IDENTITY_PROTECTED`, `EXCEPTION_STATE`, or `EXCEPTION_STATE_IDENTITY_PROTECTED`. Exception messages sent using these behaviors include a task identity token with the exception message, which you convert into a thread port by calling [`task_identity_token_get_task_port`](https://developer.apple.com/documentation/kernel/3727998-task_identity_token_get_task_por), which checks that your process has permission to use the thread port.
- **`ILLEGAL_MOVE`**: The system detected that your process moves a send right to its task or thread control port to another process. A *send right* is the permission for a process to send Mach messages to a Mach port. Giving the send right for a task or thread control port to another process gives the receiving process complete control over your process. Use the exception backtrace to identify the code responsible for sending the port’s send right to another process, and remove this code from your app.

## See Also

- [Verifying the origin of your XCFrameworks](verifying-the-origin-of-your-xcframeworks.md)
  Discover who signed a framework, and take action when that changes.
- [Enabling enhanced security for your app](enabling-enhanced-security-for-your-app.md)
  Detect out-of-bounds memory access, use of freed memory, and other potential vulnerabilities.
- [Creating enhanced security helper extensions](creating-enhanced-security-helper-extensions.md)
  Reduce opportunities for an attacker to target your app through its extensions.
- [Adopting type-aware memory allocation](adopting-type-aware-memory-allocation.md)
  Reduce the opportunities to treat pointers as data in your code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/conforming-to-mach-ipc-security-restrictions)*