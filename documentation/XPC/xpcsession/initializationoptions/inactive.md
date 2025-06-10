# inactive

**Framework**: XPC  
**Kind**: property

Indicates that the session isn’t activated during its creation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
static let inactive: XPCSession.InitializationOptions
```

#### Discussion

> ❗ **Important**:  If you create a session with this option, you must manually activate it by calling [`activate()`](xpcsession/activate().md).

## See Also

- [static let privileged: XPCSession.InitializationOptions](xpcsession/initializationoptions/privileged.md)
  Indicates that the Mach service is in the priviledged Mach bootstrap.
- [static let none: XPCSession.InitializationOptions](xpcsession/initializationoptions/none.md)
  Indicates that the listener uses a default configuration during creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/initializationoptions/inactive)*