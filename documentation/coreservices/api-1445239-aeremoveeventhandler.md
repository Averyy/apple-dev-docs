# AERemoveEventHandler(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Removes an event handler entry from an Apple event dispatch table.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AERemoveEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

Your application should not install a handler in a system dispatch table with the goal that the handler will get called when other applications receive events—this won’t work in macOS. For more information, see The System Dispatch Table in Apple Event Dispatching in Apple Events Programming Guide.

## Parameters

- `theAEEventClass`: The event class for the handler to remove. See  .
- `theAEEventID`: The event ID for the handler to remove. See  .
- `handler`: See  .
- `isSysHandler`: Specifies the Apple event dispatch table to remove the handler from. Pass   to remove the handler from the system dispatch table or   to remove the handler from your application’s dispatch table. See Version Notes for related information.

## See Also

- [func AEGetEventHandler(AEEventClass, AEEventID, UnsafeMutablePointer<AEEventHandlerUPP?>!, UnsafeMutablePointer<SRefCon?>!, Bool) -> OSErr](1445631-aegeteventhandler.md)
  Gets an event handler from an Apple event dispatch table.
- [func AEInstallEventHandler(AEEventClass, AEEventID, AEEventHandlerUPP!, SRefCon!, Bool) -> OSErr](1448596-aeinstalleventhandler.md)
  Adds an entry for an event handler to an Apple event dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445239-aeremoveeventhandler)*