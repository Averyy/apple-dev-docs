# inactive

**Framework**: XPC  
**Kind**: property

Indicates that the listener isn’t activated during its creation.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
static let inactive: XPCListener.InitializationOptions
```

#### Discussion

> ❗ **Important**:  If you create a listener with this option, you must manually activate it by calling [`activate()`](xpclistener/activate().md).

## See Also

- [static let none: XPCListener.InitializationOptions](xpclistener/initializationoptions/none.md)
  Indicates that the listener uses a default configuration during creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener/initializationoptions/inactive)*