# AEGetEventHandler(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets an event handler from an Apple event dispatch table.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: UnsafeMutablePointer<AEEventHandlerUPP?>!, _ handlerRefcon: UnsafeMutablePointer<SRefCon?>!, _ isSysHandler: Bool) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

Your application should not install a handler in a system dispatch table with the goal that the handler will get called when other applications receive events—this won’t work in macOS. For more information, see The System Dispatch Table in Apple Event Dispatching in Apple Events Programming Guide.

In Mac OS 7.1 through 9.x and macOS version v10.2 and later, `AEGetEventHandler` returns `errAEHandlerNotInstalled` when there’s not an exact match, even if a wildcard handler is installed that could handle the event. macOS version v10.0.x and v10.1.x will return the wildcard handler.

## Parameters

- `theAEEventClass`: The event class for the desired handler. See  .
- `theAEEventID`: The event ID for the desired handler. See  .
- `handler`: See  .
- `handlerRefcon`: A pointer to a reference constant. On return, the reference constant from the dispatch table entry for the specified handler. The reference constant may have a value of 0.
- `isSysHandler`: Specifies the Apple event dispatch table to get the handler from. Pass   to get the handler from the system dispatch table or   to get the handler from your application’s dispatch table. See Version Notes for related information.

## See Also

- [func AEInstallEventHandler(AEEventClass, AEEventID, AEEventHandlerUPP!, SRefCon!, Bool) -> OSErr](1448596-aeinstalleventhandler.md)
  Adds an entry for an event handler to an Apple event dispatch table.
- [func AERemoveEventHandler(AEEventClass, AEEventID, AEEventHandlerUPP!, Bool) -> OSErr](1445239-aeremoveeventhandler.md)
  Removes an event handler entry from an Apple event dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445631-aegeteventhandler)*