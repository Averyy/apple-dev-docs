# AERemoveObjectAccessor(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Removes an object accessor function from an object accessor dispatch table. 

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AERemoveObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ theAccessor: OSLAccessorUPP!, _ isSysHandler: Bool) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

In macOS, your application can not make an object callback function available to other applications by installing it in a system object accessor dispatch table.

## Parameters

- `desiredClass`: The object class of the Apple event objects located by the object accessor function to remove. Pass the value   to remove an object accessor function whose entry in an object accessor dispatch table specifies   as the object class. Pass the value   to remove an object accessor function whose entry in an object accessor dispatch table specifies   (a constant used to specify a property of any object class). Some other possible values are defined in  . See  .
- `containerType`: The descriptor type of the token that identifies the container for the objects located by the object accessor function to remove. (Token is defined in  .) Pass the value   to remove an object accessor function whose entry in an object accessor dispatch table specifies   as the descriptor type of the token used to specify the container type. See  .
- `theAccessor`: A universal procedure pointer to the special handler to remove. Although the   parameter is sufficient to identify the handler to remove, you can identify the handler explicitly as a safeguard. If you pass   for this parameter, the Apple Event Manager relies solely on the function class to identify the handler. A universal procedure pointer (UPP) to the object accessor function to remove. Although the parameters   and   are sufficient to identify the function to remove, you can identify the function explicitly by providing a UPP in this parameter. If you pass   for this parameter, the Apple Event Manager relies solely on the desired class and container type. See  .
- `isSysHandler`: Specifies the object accessor dispatch table to remove the object accessor function from. Pass   to remove the object accessor function from the system object accessor dispatch table or   to remove the object accessor function from your application’s object accessor dispatch table. Use of the system object accessor dispatch table is not recommended.

## See Also

- [func AECallObjectAccessor(DescType, UnsafePointer<AEDesc>!, DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](1447059-aecallobjectaccessor.md)
  Invokes the appropriate object accessor function for a specific desired type and container type. 
- [func AEGetObjectAccessor(DescType, DescType, UnsafeMutablePointer<OSLAccessorUPP?>!, UnsafeMutablePointer<SRefCon?>!, Bool) -> OSErr](1449054-aegetobjectaccessor.md)
  Gets an object accessor function from an object accessor dispatch table. 
- [func AEInstallObjectAccessor(DescType, DescType, OSLAccessorUPP!, SRefCon!, Bool) -> OSErr](1447905-aeinstallobjectaccessor.md)
  Adds or replaces an entry for an object accessor function to an object accessor dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442552-aeremoveobjectaccessor)*