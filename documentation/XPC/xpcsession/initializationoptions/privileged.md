# privileged

**Framework**: XPC  
**Kind**: property

Indicates that the Mach service is in the priviledged Mach bootstrap.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
static let privileged: XPCSession.InitializationOptions
```

#### Discussion

The Mach service typically accomplishes this by placing its `launchd.plist` in the `LaunchDaemons` directory.

## See Also

- [static let inactive: XPCSession.InitializationOptions](xpcsession/initializationoptions/inactive.md)
  Indicates that the session isn’t activated during its creation.
- [static let none: XPCSession.InitializationOptions](xpcsession/initializationoptions/none.md)
  Indicates that the listener uses a default configuration during creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/initializationoptions/privileged)*