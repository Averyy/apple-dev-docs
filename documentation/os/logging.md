# Logging

**Framework**: os

Capture telemetry from your app for debugging and performance analysis using the unified logging system.

#### Overview

When debugging problems in your app, it’s helpful to record the exact sequence of events that occurred, along with supplemental data about those events. Log messages provide a continuous record of your app’s runtime behavior, and make it easier to identify problems that can’t be caught easily using other techniques. Specifically, you might use log messages:

- When you are unable to attach a debugger to the app, such as when you’re diagnosing problems on a user’s machine.
- When the problem is intermittent, and is difficult to catch in the debugger.
- When you want to get a general sense of your app’s behavior—for example, you want to know when certain tasks start and end.

The unified logging system provides a comprehensive and performant API to capture telemetry across all levels of the system. This system centralizes the storage of log data in memory and on disk, rather than writing that data to a text-based log file. You view log messages using the Console app, `log` command-line tool, or Xcode debug console. You can also access log messages programmatically using the [`OSLog`](https://developer.apple.com/documentation/OSLog) framework.

> ❗ **Important**:  The unified logging system is available in iOS 10.0 and later, macOS 10.12 and later, tvOS 10.0 and later, and watchOS 3.0 and later. This system supersedes the Apple System Logger (ASL) and Syslog APIs.

## Topics

### Essentials
- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md)
  Record useful debugging and analysis information, and include dynamic content in your messages.
- [Viewing Log Messages](viewing-log-messages.md)
  Use various tools to retrieve log information.
- [Customizing Logging Behavior While Debugging](customizing-logging-behavior-while-debugging.md)
  Control which log events are recorded.
### Log Messages
- [struct Logger](logger.md)
  An object for writing interpolated string messages to the unified logging system.
- [Message Argument Formatters](message-argument-formatters.md)
  Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.
- [struct OSLogType](oslogtype.md)
  The various log levels that the unified logging system provides.
### Measure Events
- [Recording Performance Data](recording-performance-data.md)
  Add signposts to record interesting time-based events.
- [struct OSSignposter](ossignposter.md)
  An object for measuring task performance using the unified logging system.
- [Legacy Signpost Symbols](legacy-signpost-symbols.md)
  Migrate your code away from using these legacy symbols.
- [struct OSSignpostType](ossignposttype.md)
  The different kinds of signpost.
- [typealias os_signpost_id_t](os_signpost_id_t.md)
  An identifier you use to distinguish between signposts that have the same name and destination log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logging)*