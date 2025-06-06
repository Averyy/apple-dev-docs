# AEInstallCoercionHandler(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Installs a coercion handler in either the application or system coercion handler dispatch table.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEInstallCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: AECoercionHandlerUPP!, _ handlerRefcon: SRefCon!, _ fromTypeIsDesc: Bool, _ isSysHandler: Bool) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Before using `AEInstallCoercionHandler` to install a handler for a particular descriptor type, you can use the [`AEGetCoercionHandler(_:_:_:_:_:_:)`](1445348-aegetcoercionhandler.md) function to determine whether the table already contains a coercion handler for that type. 

##### 1770208

See the Version Notes section for the [`AECoercePtr(_:_:_:_:_:)`](1441846-aecoerceptr.md) function for information on when to use descriptor-based versus pointer-based coercion handlers starting in OS X version 10.2.

Thread safe starting in OS X v10.2.

Your application should not install a coercion handler in a system coercion handler dispatch table with the goal that the handler will get called when other applications perform coercions—this won’t work in macOS. For more information, see Writing and Installing Coercion Handlers in Apple Events Programming Guide.

## Parameters

- `fromType`: The descriptor type of the data coerced by the handler. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `toType`:  If there was already an entry in the specified coercion handler table for the same source descriptor type and result descriptor type, the existing entry is replaced. See  .
- `handler`: A universal procedure pointer to the coercion handler function to install. See  .
- `handlerRefcon`: A reference constant. The Apple Event Manager passes this value to the handler each time it calls it. If your handler doesn’t require a reference constant, pass 0 for this parameter.
- `fromTypeIsDesc`: Specifies the form of the data to coerce. Pass   if the coercion handler expects the data as a descriptor or   if the coercion handler expects a pointer to the data. The Apple Event Manager can provide a pointer to data more efficiently than it can provide a descriptor, so all coercion functions should accept a pointer to data if possible.
- `isSysHandler`: Specifies the coercion table to add the handler to. Pass   to add the handler to the system coercion table or   to add the handler to your application’s coercion table. Use of the system coercion table is not recommended.

## See Also

- [func AEGetCoercionHandler(DescType, DescType, UnsafeMutablePointer<AECoercionHandlerUPP?>!, UnsafeMutablePointer<SRefCon?>!, UnsafeMutablePointer<DarwinBoolean>!, Bool) -> OSErr](1445348-aegetcoercionhandler.md)
  Gets the coercion handler for a specified descriptor type.
- [func AERemoveCoercionHandler(DescType, DescType, AECoercionHandlerUPP!, Bool) -> OSErr](1441907-aeremovecoercionhandler.md)
  Removes a coercion handler from a coercion handler dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445548-aeinstallcoercionhandler)*