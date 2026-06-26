# Xcode 26.5 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 26.5 includes Swift 6.3 and SDKs for iOS 26.5, iPadOS 26.5, tvOS 26.5, macOS 26.5, and visionOS 26.5. Xcode 26.5 supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 8 and later, and visionOS. Xcode 26.5 requires a Mac running macOS Tahoe 26.2 or later.

##### General

###### Known Issues

- When streaming stdout and stderr from multiple processes at the same time (eg: in parallel testing scenarios), the results may be significantly delayed.  (165098287)

##### Background Assets

###### Known Issues

- The system may incorrectly determine an app’s eligibility for development overrides in simulator environments.  (173742496) **Workaround:** Test your app on a physical device.

##### Coding Intelligence

###### New Features

- Messages can now be queued in the coding assistant.  (174563016)
- Agents can now ask clarifying questions to provide more accurate results.  (175182375)

###### Resolved Issues

- Fixed: An issue causing malformed data in RunSomeTests MCP tool call  (170415923)
- Fixed: Users interacting with Claude Code might receive an error message about their OAuth token being expired.  (175464325)

##### Instruments

###### Resolved Issues

- Fixed: Typing in the filter field at the bottom of the Symbols window would create a token for every character  (172423349)
- Fixed an issue where profiling using Metal System Trace with GPU Counters capture could cause memory footprint of Instruments to increase to tens of gigabytes.  (173195251)

##### Localization

###### Resolved Issues

- Fixed: Generated code for String Catalog symbol generation will no longer produce a compiler error for Packages that default to MainActor isolation.  (173302714) (FB22329375)

##### Security

###### Resolved Issues

- Fixed: Mac (Designed for iPad) apps with pointer authentication are now compatible with macOS Tahoe 26.5 and newer. Add `LSMinimumSystemVersion` with value `26.5` to your app’s Info.plist to ensure the app only runs on Tahoe 26.5 and newer.  (171174887)

##### Simulator

###### Resolved Issues

- Fixed: Pasteboard Synchronization within Simulator.app is currently not functioning.  (173403967) (FB22340739)

##### Storekit Testing in Xcode

###### New Features

- New billing plan APIs can be tested using [`StoreKit Testing in Xcode`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode). Configure a monthly with 12-month commitment billing plan for your auto-renewable subscriptions in the StoreKit Configuration, and simulate subscribing to the billing plan through the Transaction Manager in Xcode.  (168522699)

##### Swift

###### Known Issues

- When a closure with explicit captures is passed as an argument to a `nonisolated(nonsending)` parameter or converted to a `nonisolated(nonsending)` type, its isolation was inferred from the parent context instead of being directly set to `nonisolated(nonsending)`. The difference in isolation wasn’t observable by callers until Swift 6.3.2, which introduced a bug fix for an actor hop optimization that previously didn’t work when a `nonisolated(nonsending)` function value came from a parameter position. In particular, this affects projects that have enabled the `NonisolatedNonsendingByDefault` feature (via `ApproachableConcurrency` or directly). For example: ```swift
 @MainActor
 func compute(_ fn: nonisolated(nonsending) @Sendable () async -> Void) async {
   await fn()
 }
 
 func performComputation() async {
   let x: Int = 42
   await compute { [x] in // closure isolation is inferred to be @concurrent
     print(x)
   }
 }
``` In this example, the Swift compiler would no longer hop back to `@MainActor` after `await fn()` returns because `fn` is `nonisolated(nonsending)` and should have executed on `@MainActor` already, but because the closure isolation was incorrectly inferred to be `@concurrent`, any *synchronous* calls that follow `fn` one are going to be executed in a `@concurrent` isolation context instead of the `@MainActor` one.  (176582055) **Workaround:** There are multiple ways to work around this issue. ```None
  1. Remove explicit captures when values could be captured implicitly.

  The example from Description becomes:	
``` ```swift
 func performComputation() async {
   let x: Int = ...
   await compute {
     print(x)
   }
 }
``` 1. Convert a closure into a local function that is explicitly `nonisolated(nonsending)`: The example from Description becomes: ```swift
 func performComputation() async {
   let x: Int = ...
 
   @Sendable nonisolated(nonsending) func performAction() async {
     print(x)
   }
 
   await compute(performAction)
 }
```

##### Testing

###### Resolved Issues

- Fixed: Tests fail to run on iOS 15 simulators  (173337319) (FB22333623)

## See Also

- [Xcode 26.6 Release Notes](xcode-26_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.4.1 Release Notes](xcode-26_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.4 Release Notes](xcode-26_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.3 Release Notes](xcode-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.2 Release Notes](xcode-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.1.1 Release Notes](xcode-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.0.1 Release Notes](xcode-26_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26 Release Notes](xcode-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-26_5-release-notes)*