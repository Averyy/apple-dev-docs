# AERemoveCoercionHandler(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Removes a coercion handler from a coercion handler dispatch table.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AERemoveCoercionHandler(_ fromType: DescType, _ toType: DescType, _ handler: AECoercionHandlerUPP!, _ isSysHandler: Bool) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

Use of system coercion tables is not recommended. For more information, see Writing and Installing Coercion Handlers in Apple Events Programming Guide.

## Parameters

- `fromType`: The descriptor type of the data coerced by the handler. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `toType`: The descriptor type of the resulting data. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `handler`: A universal procedure pointer to the coercion handler to remove. Although the parameters   and   are sufficient to identify the handler, you can identify the handler explicitly as a safeguard. If you pass   for this parameter, the Apple Event Manager relies solely on the event class and event ID to identify the handler. See  .
- `isSysHandler`: Specifies the coercion table to remove the handler from. Pass   to remove the handler from the system coercion table or   to remove the handler from your application’s coercion table. Use of the system coercion table is not recommended.

## See Also

- [func AEGetCoercionHandler(DescType, DescType, UnsafeMutablePointer<AECoercionHandlerUPP?>!, UnsafeMutablePointer<SRefCon?>!, UnsafeMutablePointer<DarwinBoolean>!, Bool) -> OSErr](1445348-aegetcoercionhandler.md)
  Gets the coercion handler for a specified descriptor type.
- [func AEInstallCoercionHandler(DescType, DescType, AECoercionHandlerUPP!, SRefCon!, Bool, Bool) -> OSErr](1445548-aeinstallcoercionhandler.md)
  Installs a coercion handler in either the application or system coercion handler dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1441907-aeremovecoercionhandler)*