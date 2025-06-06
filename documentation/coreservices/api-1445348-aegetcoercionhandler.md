# AEGetCoercionHandler(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets the coercion handler for a specified descriptor type.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: UnsafeMutablePointer<AECoercionHandlerUPP?>!, _ handlerRefcon: UnsafeMutablePointer<SRefCon?>!, _ fromTypeIsDesc: UnsafeMutablePointer<DarwinBoolean>!, _ isSysHandler: Bool) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

Your application should not install a coercion handler in a system coercion handler dispatch table with the goal that the handler will get called when other applications perform coercions—this won’t work in macOS. For more information, see Writing and Installing Coercion Handlers in Apple Events Programming Guide.

In Mac OS 7.1 through 9.x and macOS version v10.2 and later, `AEGetCoercionHandler` returns `errAEHandlerNotInstalled` when there’s not an exact match, even if a wildcard handler is installed that could handle the coercion. macOS version v10.0.x and v10.1.x will return the wildcard handler.

## Parameters

- `fromType`: The descriptor type of the data coerced by the handler. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `toType`: The descriptor type of the resulting data. For a list of AppleScript’s predefined descriptor types, see  .
- `handler`: A universal procedure pointer. On return, a pointer to the specified handler, if a coercion table entry exists that exactly matches the values supplied in the parameters   and  . See  .
- `handlerRefcon`: A pointer to a reference constant. On return, the reference constant from the coercion table entry for the specified coercion handler. The Apple Event Manager passes this reference constant to the handler each time it calls the handler. The reference constant may have a value of 0.
- `fromTypeIsDesc`: A pointer to a Boolean value. The   function returns a value of   in this parameter if the coercion handler expects the data as a descriptor or  , if the coercion handler expects a pointer to the data.
- `isSysHandler`: Specifies the coercion table to get the handler from. Pass   to get the handler from the system coercion table or   to get the handler from your application’s coercion table. Use of the system coercion table is not recommended.

## See Also

- [func AEInstallCoercionHandler(DescType, DescType, AECoercionHandlerUPP!, SRefCon!, Bool, Bool) -> OSErr](1445548-aeinstallcoercionhandler.md)
  Installs a coercion handler in either the application or system coercion handler dispatch table.
- [func AERemoveCoercionHandler(DescType, DescType, AECoercionHandlerUPP!, Bool) -> OSErr](1441907-aeremovecoercionhandler.md)
  Removes a coercion handler from a coercion handler dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445348-aegetcoercionhandler)*