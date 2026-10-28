# XPC_ACTIVITY_CHECK_IN

**Framework**: XPC  
**Kind**: var  
**Role**: Global Variable

A constant to check in with the system for a previously registered activity using the same identifier.

**Availability**:
- macOS 10.9+

## Declaration

```swift
let XPC_ACTIVITY_CHECK_IN: xpc_object_t
```

```c
extern xpc_object_t const XPC_ACTIVITY_CHECK_IN;
```

## Discussion

Pass this constant to [`xpc_activity_register(_:_:_:)`](./xpc_activity_register%28_,_,_%29.md) as the criteria dictionary to check in with the system for previously registered activity using the same identifier (for example, an activity from a launchd property list).

## See Also

### Registration
- [func xpc_activity_register(UnsafePointer<CChar>, xpc_object_t, xpc_activity_handler_t)](./xpc_activity_register%28_,_,_%29.md)
  Registers an activity with the system.
- [func xpc_activity_unregister(UnsafePointer<CChar>)](./xpc_activity_unregister%28_%29.md)
  Unregisters an activity with the specified identifier.
- [typealias xpc_activity_t](./xpc_activity_t.md)
  An XPC activity object.
- [typealias xpc_activity_handler_t](./xpc_activity_handler_t.md)
  A block to call when an XPC activity becomes eligible to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_check_in)*