# AEInstallEventHandler(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Adds an entry for an event handler to an Apple event dispatch table.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEInstallEventHandler(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ handler: AEEventHandlerUPP!, _ handlerRefcon: SRefCon!, _ isSysHandler: Bool) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

The parameters `theAEEventClass` and `theAEEventID` specify the event class and event ID of the Apple events handled by the handler for this dispatch table entry. If there is already an entry in the specified dispatch table for the same event class and event ID, it is replaced. For these parameters, you must provide one of the following combinations:

- the event class and event ID of a single Apple event to dispatch to the handler (for example, an event class of `kAECoreSuite` and an event ID of `kAEDelete` so that a specific kind of `delete` event is dispatched to the handler) 
- the `typeWildCard` constant for `theAEEventClass` and an event ID for `theAEEventID`, which indicates that Apple events from all event classes whose event IDs match `theAEEventID` should be dispatched to the handler (for example, an event class of `typeWildCard` and an event ID of` kAEDelete` so that for all event classes, the `delete` event is dispatched to the handler) 
- an event class for `theAEEventClass` and the `typeWildCard` constant for `theAEEventID`, which indicates that all events from the specified event class should be dispatched to the handler (for example, an event class of `kAECoreSuite` and an event ID of` typeWildCard` so that all events for the core suite are dispatched to the handler) 
- the` typeWildCard` constant for both the `theAEEventClass` and `theAEEventID` parameters, which indicates that all Apple events should be dispatched to the handler

If you use the `typeWildCard` constant for either the `theAEEventClass` or the `theAEEventID` parameter (or for both parameters), the corresponding handler must return the error `errAEEventNotHandled` if it does not handle a particular event.

If an Apple event dispatch table contains one entry for an event class and a specific event ID, and also contains another entry that is identical except that it specifies a wildcard value for either the event class or the event ID, the Apple Event Manager dispatches the more specific entry. For example, if an Apple event dispatch table includes one entry that specifies the event class as `kAECoreSuite` and the event ID as `kAEDelete`, and another entry that specifies the event class as `kAECoreSuite` and the event ID as `typeWildCard`, the Apple Event Manager dispatches the Apple event handler associated with the entry that specifies the event ID as `kAEDelete`.

In addition to the Apple event handler dispatch tables, applications can add entries to special handler dispatch tables, as described in [`Managing Special Handler Dispatch Tables`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1652333). 

##### 1770205

Thread safe starting in OS X v10.2.

Your application should not install a handler in a system dispatch table with the goal that the handler will get called when other applications receive events—this won’t work in macOS. For more information, see The System Dispatch Table in Apple Event Dispatching in Apple Events Programming Guide.

## Parameters

- `theAEEventClass`: The event class for the Apple event or events to dispatch to this event handler. The Discussion section describes interactions between this parameter and the   parameter. See  .
- `theAEEventID`: The event ID for the Apple event or events to dispatch to this event handler. The Discussion section describes interactions between this parameter and the   parameter. See  .
- `handler`: A universal procedure pointer to the Apple event handler function to install. See  .
- `handlerRefcon`: A reference constant. The Apple Event Manager passes this value to the handler each time it calls it. If your handler doesn’t require a reference constant, pass 0 for this parameter.
- `isSysHandler`: Specifies the Apple event dispatch table to add the handler to. Pass   to add the handler to the system dispatch table or   to add the handler to your application’s dispatch table. See Version Notes for related information.

## See Also

- [func AEGetEventHandler(AEEventClass, AEEventID, UnsafeMutablePointer<AEEventHandlerUPP?>!, UnsafeMutablePointer<SRefCon?>!, Bool) -> OSErr](1445631-aegeteventhandler.md)
  Gets an event handler from an Apple event dispatch table.
- [func AERemoveEventHandler(AEEventClass, AEEventID, AEEventHandlerUPP!, Bool) -> OSErr](1445239-aeremoveeventhandler.md)
  Removes an event handler entry from an Apple event dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448596-aeinstalleventhandler)*