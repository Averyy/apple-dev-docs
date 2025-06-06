# AEGetSpecialHandler(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets a specified handler from a special handler dispatch table.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetSpecialHandler(_ functionClass: AEKeyword, _ handler: UnsafeMutablePointer<AEEventHandlerUPP?>!, _ isSysHandler: Bool) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

See also [`AEInstallSpecialHandler(_:_:_:)`](1445532-aeinstallspecialhandler.md) and [`AERemoveSpecialHandler(_:_:_:)`](1447960-aeremovespecialhandler.md). 

##### 1770209

Thread safe starting in OS X v10.2.

In macOS, you should generally install all handlers in the application dispatch table. For Carbon applications running in Mac OS 8 or Mac OS 9, a special handler in the system dispatch table could reside in the system heap, where it would be available to other applications. However, this won’t work in macOS.

## Parameters

- `functionClass`: The keyword for the special handler to get. You can specify any of the constants described in  . See  .
- `handler`: A universal procedure pointer. On return, a pointer to the specified special handler, if one exists that matches the value supplied in the   parameter. See  .
- `isSysHandler`: Specifies the special handler dispatch table to get the handler from. Pass   to get the handler from the system special handler dispatch table or   to get the handler from your application’s special handler dispatch table. Use of the system special handler dispatch table is not recommended.

## See Also

- [func AEInstallSpecialHandler(AEKeyword, AEEventHandlerUPP!, Bool) -> OSErr](1445532-aeinstallspecialhandler.md)
  Installs a callback function in a special handler dispatch table.
- [func AERemoveSpecialHandler(AEKeyword, AEEventHandlerUPP!, Bool) -> OSErr](1447960-aeremovespecialhandler.md)
  Removes a handler from a special handler dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444274-aegetspecialhandler)*