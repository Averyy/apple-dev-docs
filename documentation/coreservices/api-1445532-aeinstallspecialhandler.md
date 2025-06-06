# AEInstallSpecialHandler(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Installs a callback function in a special handler dispatch table.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEInstallSpecialHandler(_ functionClass: AEKeyword, _ handler: AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

An Apple event special handler dispatch table contains entries with a function class keyword, the address of the handler function that handles the Apple events indicated by the keyword, and a reference constant. Depending on which handlers you choose to install, a special handler dispatch table can have entries for any of the following:

-  a predispatch handler (an Apple event handler that the Apple Event Manager calls immediately before it dispatches an Apple event) 
-  up to one each of the callback functions described in [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager) these functions, such as an object comparison function and an object-counting function, can be installed with `AEInstallSpecialHandler` or with the [`AEInstallObjectAccessor(_:_:_:_:_:)`](1447905-aeinstallobjectaccessor.md) function 

See also [`AEGetSpecialHandler(_:_:_:)`](1444274-aegetspecialhandler.md) and [`AERemoveSpecialHandler(_:_:_:)`](1447960-aeremovespecialhandler.md). 

##### 1770210

Thread safe starting in OS X v10.2.

For Carbon applications running in Mac OS 8 or Mac OS 9, a handler in the system special handler dispatch table should reside in the system heap, where it may be available to other applications. If you put your system handler code in your application heap, be sure to use `AERemoveSpecialHandler` to remove the handler when your application quits. Otherwise, your handler will still have an entry in the system dispatch table with a pointer a handler that no longer exists. Another application may dispatch an Apple event that attempts to call your handler, leading to a system crash.

Your application should not install a handler in a system dispatch table with the goal that the handler will get called when other applications receive events—this won’t work in macOS.

## Parameters

- `functionClass`: See  .
- `handler`: A universal procedure pointer to the special handler to install. See  .
- `isSysHandler`: Specifies the special handler dispatch table to add the handler to. Pass   to add the handler to the system special handler dispatch table or   to add the handler to your application’s special handler dispatch table. Use of the system special handler dispatch table is not recommended.

## See Also

- [func AEGetSpecialHandler(AEKeyword, UnsafeMutablePointer<AEEventHandlerUPP?>!, Bool) -> OSErr](1444274-aegetspecialhandler.md)
  Gets a specified handler from a special handler dispatch table.
- [func AERemoveSpecialHandler(AEKeyword, AEEventHandlerUPP!, Bool) -> OSErr](1447960-aeremovespecialhandler.md)
  Removes a handler from a special handler dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445532-aeinstallspecialhandler)*