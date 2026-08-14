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

- `theAEEventClass`: The event class for the handler to remove. See [`AEEventClass`](aeeventclass.md).
- `theAEEventID`: The event ID for the handler to remove. See [`AEEventID`](aeeventid.md).
- `handler`: A universal procedure pointer to the handler to remove. Although the parameters `theAEEventClass` and `theAEEventID` are sufficient to identify the handler, you can identify the handler explicitly as a safeguard. If you pass `NULL` for this parameter, the Apple Event Manager relies solely on the event class and event ID to identify the handler. If you use the `typeWildCard` constant for either or both of the event class and event ID parameters, `AERemoveEventHandler` will return an error unless an entry exists that specifies `typeWildCard` in exactly the same way. For example, if you specify `typeWildCard` in both the `theAEEventClass` parameter and the `theAEEventID` parameter, `AERemoveEventHandler` will not remove the first handler for any event class and event ID in the dispatch table; instead, it will only remove a handler if an entry exists that specifies type `typeWildCard` for both the event class and the event ID. For an explanation of wildcard values, see the Discussion section for [`AEInstallEventHandler(_:_:_:_:_:)`](1448596-aeinstalleventhandler.md). See [`AEEventHandlerUPP`](aeeventhandlerupp.md).
- `isSysHandler`: Specifies the Apple event dispatch table to remove the handler from. Pass `TRUE` to remove the handler from the system dispatch table or `FALSE` to remove the handler from your application’s dispatch table. See Version Notes for related information.

## See Also

- [func AEGetEventHandler(AEEventClass, AEEventID, UnsafeMutablePointer<AEEventHandlerUPP?>!, UnsafeMutablePointer<SRefCon?>!, Bool) -> OSErr](1445631-aegeteventhandler.md)
  Gets an event handler from an Apple event dispatch table.
- [func AEInstallEventHandler(AEEventClass, AEEventID, AEEventHandlerUPP!, SRefCon!, Bool) -> OSErr](1448596-aeinstalleventhandler.md)
  Adds an entry for an event handler to an Apple event dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445239-aeremoveeventhandler)*