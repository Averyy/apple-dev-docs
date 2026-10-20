# xpc_activity_handler_t

**Framework**: XPC  
**Kind**: typealias  
**Role**: Type Alias

A block to call when an XPC activity becomes eligible to run.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias xpc_activity_handler_t = (xpc_activity_t) -> Void
```

```c
typedef void (^)(NSObject<OS_xpc_object> *) xpc_activity_handler_t;
```

## See Also

### Registration
- [func xpc_activity_register(UnsafePointer<CChar>, xpc_object_t, xpc_activity_handler_t)](./xpc_activity_register%28_,_,_%29.md)
  Registers an activity with the system.
- [func xpc_activity_unregister(UnsafePointer<CChar>)](./xpc_activity_unregister%28_%29.md)
  Unregisters an activity with the specified identifier.
- [let XPC_ACTIVITY_CHECK_IN: xpc_object_t](./xpc_activity_check_in.md)
  A constant to check in with the system for a previously registered activity using the same identifier.
- [typealias xpc_activity_t](./xpc_activity_t.md)
  An XPC activity object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_handler_t)*