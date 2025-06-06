# AERemoveSpecialHandler(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Removes a handler from a special handler dispatch table.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AERemoveSpecialHandler(_ functionClass: AEKeyword, _ handler: AEEventHandlerUPP!, _ isSysHandler: Bool) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

See also [`AEInstallSpecialHandler(_:_:_:)`](1445532-aeinstallspecialhandler.md) and [`AEGetSpecialHandler(_:_:_:)`](1444274-aegetspecialhandler.md). 

##### 1770211

Thread safe starting in OS X v10.2.

Your application should not install a special handler in a system dispatch table with the goal that the handler will get called when other applications receive events—this won’t work in macOS.

In some previous versions of the Mac OS, applications might have reason to disable, within the application only, all Apple Event Manager functions that support Apple event objects—that is, all the functions available to an application as a result of linking the Object Support Library (OSL) and calling the [`AEObjectInit()`](1447372-aeobjectinit.md) function.

To disable the OSL, you should pass the keyword `keySelectProc` in the `functionClass` parameter, `NULL` in the `handler` parameter, and `FALSE` in the `isSysHandler` parameter. An application that expects its copy of the OSL to move after it is installed—for example, an application that keeps it in a stand-alone code resource—would need to disable the OSL. When an application calls `AEObjectInit` to initialize the OSL, the OSL installs the addresses of its functions as extensions to the pack. If those functions move, the addresses become invalid.

Once you have called the `AERemoveSpecialHandler` function to disable the OSL, subsequent calls by your application to any of the Apple Event Manager functions that support Apple event objects will return errors. To initialize the OSL after disabling it with the `AERemoveSpecialHandler` function, your application must call `AEObjectInit` again.

If you expect to initialize the OSL and disable it several times, you should call `AERemoveObjectAccessor` to remove your application’s object accessor functions from your application’s object accessor dispatch table before you call `AERemoveSpecialHandler`. 

## Parameters

- `functionClass`: The keyword for the special handler to remove. Pass one of the constants described in  . See  .
- `handler`: A universal procedure pointer to the special handler to remove. Although the   parameter is sufficient to identify the handler to remove, you can identify the handler explicitly as a safeguard. If you pass   for this parameter, the Apple Event Manager relies solely on the function class to identify the handler. See  .
- `isSysHandler`: Specifies the special handler dispatch table to remove the handler from. Pass   to remove the handler from the system special handler dispatch table or   to remove the handler from your application’s special handler dispatch table. Use of the system special handler dispatch table is not recommended.

## See Also

- [func AEGetSpecialHandler(AEKeyword, UnsafeMutablePointer<AEEventHandlerUPP?>!, Bool) -> OSErr](1444274-aegetspecialhandler.md)
  Gets a specified handler from a special handler dispatch table.
- [func AEInstallSpecialHandler(AEKeyword, AEEventHandlerUPP!, Bool) -> OSErr](1445532-aeinstallspecialhandler.md)
  Installs a callback function in a special handler dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447960-aeremovespecialhandler)*