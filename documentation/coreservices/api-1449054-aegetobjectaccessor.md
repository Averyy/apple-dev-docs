# AEGetObjectAccessor(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets an object accessor function from an object accessor dispatch table. 

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ accessor: UnsafeMutablePointer<OSLAccessorUPP?>!, _ accessorRefcon: UnsafeMutablePointer<SRefCon?>!, _ isSysHandler: Bool) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Calling `AEGetObjectAccessor` does not remove the object accessor function from an object accessor dispatch table. 

##### 1770184

In macOS, your application can not make an object callback function available to other applications by installing it in a system object accessor dispatch table.

## Parameters

- `desiredClass`: The object class of the Apple event objects located by the object accessor function to get. Pass the value   to get an object accessor function whose entry in an object accessor dispatch table specifies   as the object class. Pass the value   to get an object accessor function whose entry in an object accessor dispatch table specifies   (a constant used to specify a property of any object class). Some other possible values are defined in  . See  .
- `containerType`: The descriptor type of the token that identifies the container for the objects located by the requested accessor function. (Token is defined in  .) Pass the value   to get an object accessor function whose entry in an object accessor dispatch table specifies   as the descriptor type of the token used to specify the container type. See  .
- `accessor`: A universal procedure pointer. On return, a pointer to the requested object accessor function, if an object accessor dispatch table entry exists that exactly matches the values supplied in the parameters   and  . See  .
- `accessorRefcon`: A pointer to a reference constant. On return, points to the reference constant from the object accessor dispatch table entry for the specified object accessor function. The reference constant may have a value of 0.
- `isSysHandler`: Specifies the object accessor dispatch table to get the object accessor function from. Pass   to get the object accessor function from the system object accessor dispatch table or   to get the object accessor function from your application’s object accessor dispatch table. Use of the system object accessor dispatch table is not recommended. 

## See Also

- [func AECallObjectAccessor(DescType, UnsafePointer<AEDesc>!, DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](1447059-aecallobjectaccessor.md)
  Invokes the appropriate object accessor function for a specific desired type and container type. 
- [func AEInstallObjectAccessor(DescType, DescType, OSLAccessorUPP!, SRefCon!, Bool) -> OSErr](1447905-aeinstallobjectaccessor.md)
  Adds or replaces an entry for an object accessor function to an object accessor dispatch table.
- [func AERemoveObjectAccessor(DescType, DescType, OSLAccessorUPP!, Bool) -> OSErr](1442552-aeremoveobjectaccessor.md)
  Removes an object accessor function from an object accessor dispatch table. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449054-aegetobjectaccessor)*