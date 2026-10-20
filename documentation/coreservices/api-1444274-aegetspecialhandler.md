# AEGetSpecialHandler(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets a specified handler from a special handler dispatch table.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetSpecialHandler(_ functionClass: AEKeyword, _ handler: UnsafeMutablePointer<AEEventHandlerUPP?>!, _ isSysHandler: Bool) -> OSErr
```

```c
OSErr AEGetSpecialHandler(AEKeyword functionClass, AEEventHandlerUPP *handler, Boolean isSysHandler);
```

#### Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

#### Discussion

See also [`AEInstallSpecialHandler(_:_:_:)`](./api-1445532-aeinstallspecialhandler.md) and [`AERemoveSpecialHandler(_:_:_:)`](./api-1447960-aeremovespecialhandler.md). 

##### Version-Notes

Thread safe starting in OS X v10.2.

In macOS, you should generally install all handlers in the application dispatch table. For Carbon applications running in Mac OS 8 or Mac OS 9, a special handler in the system dispatch table could reside in the system heap, where it would be available to other applications. However, this won’t work in macOS.

## Parameters

- `functionClass`: The keyword for the special handler to get. You can specify any of the constants described in [Special Handler Callback Constants](./apple_events/api-1572726-special_handler_callback_constan.md). See [`AEKeyword`](./aekeyword.md).
- `handler`: A universal procedure pointer. On return, a pointer to the specified special handler, if one exists that matches the value supplied in the `functionClass` parameter. See [`AEEventHandlerUPP`](./aeeventhandlerupp.md).
- `isSysHandler`: Specifies the special handler dispatch table to get the handler from. Pass `TRUE` to get the handler from the system special handler dispatch table or `FALSE` to get the handler from your application’s special handler dispatch table. Use of the system special handler dispatch table is not recommended.

## See Also

### Managing Special Handler Dispatch Tables
- [func AEInstallSpecialHandler(AEKeyword, AEEventHandlerUPP!, Bool) -> OSErr](./api-1445532-aeinstallspecialhandler.md)
  Installs a callback function in a special handler dispatch table.
- [func AERemoveSpecialHandler(AEKeyword, AEEventHandlerUPP!, Bool) -> OSErr](./api-1447960-aeremovespecialhandler.md)
  Removes a handler from a special handler dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444274-aegetspecialhandler)*