# inactive

**Framework**: XPC  
**Kind**: property  
**Role**: Type Property

Indicates that the session isn’t activated during its creation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
static let inactive: XPCSession.InitializationOptions
```

#### Discussion

> ❗ **Important**:  If you create a session with this option, you must manually activate it by calling [`activate()`](../activate%28%29.md).

## See Also

### Session creation options
- [static let privileged: XPCSession.InitializationOptions](./privileged.md)
  Indicates that the Mach service is in the priviledged Mach bootstrap.
- [static let none: XPCSession.InitializationOptions](./none.md)
  Indicates that the listener uses a default configuration during creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/initializationoptions/inactive)*