# EXC_CRASH (SIGKILL)

**Framework**: Xcode

The operating system terminated the process, often because a background task violated a requirement, device resources were limited, or the user force quit the app.

#### Overview

The crash report contains a `Termination Reason` field with a code that explains the reason for the crash. In the following example, that code is `0xdead10cc`:

```other
Exception Type:  EXC_CRASH (SIGKILL)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note:  EXC_CORPSE_NOTIFY
Termination Reason: Namespace RUNNINGBOARD, Code 0xdead10cc
```

The `Termination Reason` code is one of the following values:

- **`0x2182bad2` (`562215634`)**: The operating system terminated the app due to a background task failing to complete in time.
- **`0x2182bad3` (`562215635`)**: The operating system terminated the app due to a background URL session failing to complete in time.
- **`0x2182bad4` (`562215636`)**: The operating system terminated the app due to a background fetch failing to complete in time.
- **`0x8badf00d` (`2343432205`) — pronounced “ate bad food”**: The operating system’s watchdog terminated the app. See [`Addressing watchdog terminations`](addressing-watchdog-terminations.md).
- **`0xc00010ff` (`3221229823`) — pronounced “cool off”**: The operating system terminated the app due to a thermal event. This can be an issue with the particular device that this crash occurred on, or the environment it operated in. For tips on making your app run more efficiently, watch the [`iOS Performance and Power Optimization with Instruments`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2011/312/) WWDC session. To test your app’s response to thermal events, enable a thermal device condition as described in [`Test under adverse device conditions (iOS)`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev308429d42).
- **`0xdead10cc` (`3735883980`) — pronounced “dead lock”**: The operating system terminated the app because it held on to a file lock or SQLite database lock during suspension. Request additional background execution time on the main thread with [`beginBackgroundTask(withName:expirationHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplication/beginBackgroundTask(withName:expirationHandler:)). Make this request well before starting to write to the file in order to complete those operations and relinquish the lock before the app suspends. In an app extension, use [`beginActivity(options:reason:)`](https://developer.apple.com/documentation/Foundation/ProcessInfo/beginActivity(options:reason:)) to manage this work.
- **`0xbaadca11` (`3131951633`) — pronounced “bad call”**: The operating system terminated the app for failing to report a [`CallKit`](https://developer.apple.com/documentation/CallKit) call in response to a [`PushKit`](https://developer.apple.com/documentation/PushKit) notification.
- **`0xbad22222` (`3134333474`)**: The operating system terminated a VoIP application because it resumed too frequently.
- **`0xbaddd15c` (`3135099228`) — pronounced “bad disc”**: The operating system terminated the app to delete caches, in an attempt to reclaim disk space. Many factors contribute to low disk space. You may be able to help by minimizing what you write to disk and managing the entire life cycle of your files.
- **`0xc51bad01` (`3306925313`)**: watchOS terminated the app because it used too much CPU time while performing a background task. Optimize the code performing the background task to be more CPU efficient, or decrease the amount of work that the app performs while running in the background to resolve this crash.
- **`0xc51bad02` (`3306925314`)**: watchOS terminated the app because it failed to complete a background task within the allocated time. Decrease the amount of work that the app performs while running in the background to resolve this crash.
- **`0xc51bad03` (`3306925315`)**: watchOS terminated the app because it failed to complete a background task within the allocated time, but the system was sufficiently busy overall that the app might not have received much CPU time to perform the background task. Although you might be able to avoid the issue by reducing the amount of work your app performs in background tasks, `0xc51bad03` doesn’t indicate that the app did anything wrong. More likely, the app wasn’t able to complete its work because of overall system load.
- **`0xd00d2bad` (`3490524077`) — pronounced “dude, too bad”**: The operating system terminated the app due to excessive use of key system resources. You might be able to avoid the issue by reducing parallelization and ensuring that your app completes operations for preceding tasks before starting new tasks.

## See Also

- [EXC_ARITHMETIC](exc_arithmetic.md)
  An arithmetic problem terminated the process, often because of division by zero or a floating-point error.
- [EXC_BAD_ACCESS](exc_bad_access.md)
  A bad access to memory terminated the process.
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md)
  A bus error terminated the process, often because the process tried to access a misaligned or invalid address in memory, or due to a pointer authentication failure.
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md)
  A memory segmentation fault terminated the process, often because the process tried to access an invalid or out-of-bounds address in memory.
- [EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md)
  A trace trap or invalid CPU instruction interrupted the process, often because the process violated a requirement or timeout.
- [EXC_CRASH](exc_crash.md)
  The process crashed.
- [EXC_CRASH (SIGABRT)](sigabrt.md)
  The process terminated because it received an abort signal.
- [EXC_CRASH (SIGQUIT)](sigquit.md)
  Another processes terminated the process, often because the process violated a requirement or timeout.
- [EXC_CRASH (SIGSYS)](sigsys.md)
  A bad argument to a system call terminated the process.
- [EXC_CRASH (SIGTERM)](sigterm.md)
  A software termination signal terminated the process.
- [EXC_GUARD](exc_guard.md)
  The process violated a guarded resource protection, often related to file descriptors.
- [EXC_RESOURCE](exc_resource.md)
  The operating system stopped the process because the process exceeded a limit on resource consumption, like CPU time or memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/sigkill)*