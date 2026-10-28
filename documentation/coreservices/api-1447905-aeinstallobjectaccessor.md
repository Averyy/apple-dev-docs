# AEInstallObjectAccessor(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Adds or replaces an entry for an object accessor function to an object accessor dispatch table.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEInstallObjectAccessor(_ desiredClass: DescType, _ containerType: DescType, _ theAccessor: OSLAccessorUPP!, _ accessorRefcon: SRefCon!, _ isSysHandler: Bool) -> OSErr
```

```c
OSErr AEInstallObjectAccessor(DescType desiredClass, DescType containerType, OSLAccessorUPP theAccessor, SRefCon accessorRefcon, Boolean isSysHandler);
```

## Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

## Discussion

The `AEInstallObjectAccessor` function adds or replaces an entry to either the application or system object accessor dispatch table. 

### Version-Notes

In macOS, your application can not make an object callback function available to other applications by installing it in a system object accessor dispatch table.

If your Carbon application running in Mac OS 8 or OS 9 installs a system object accessor function in its application heap, rather than in the system heap, you must call [`AERemoveObjectAccessor(_:_:_:_:)`](./api-1442552-aeremoveobjectaccessor.md) to remove the function before your application terminates.

## Parameters

- `desiredClass`: The object type of the Apple event objects located by this accessor. See [`DescType`](./desctype.md).
- `containerType`: The type of the token whose objects are accessed by this accessor. (Token is defined in [`AEDisposeToken(_:)`](./api-1446783-aedisposetoken.md).) The accessor function finds objects in containers specified by tokens of this type. See [`DescType`](./desctype.md).
- `theAccessor`: A universal procedure pointer to the object accessor function to install. See [`OSLAccessorUPP`](./oslaccessorupp.md).
- `accessorRefcon`: A reference constant the Apple Event Manager passes to the object accessor function whenever it calls the function. If your object accessor function doesn’t require a reference constant, pass 0 for this parameter. To change the value of the reference constant, you must call `AEInstallObjectAccessor` again.
- `isSysHandler`: Specifies the object accessor dispatch table to add the entry to. Pass `TRUE` to add the entry to the system object accessor dispatch table or `FALSE` to add the entry to your application’s object accessor dispatch table. Use of the system object accessor dispatch table is not recommended. 

## See Also

### Getting, Calling, and Removing Object Accessor Functions
- [func AECallObjectAccessor(DescType, UnsafePointer<AEDesc>!, DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](./api-1447059-aecallobjectaccessor.md)
  Invokes the appropriate object accessor function for a specific desired type and container type. 
- [func AEGetObjectAccessor(DescType, DescType, UnsafeMutablePointer<OSLAccessorUPP?>!, UnsafeMutablePointer<SRefCon?>!, Bool) -> OSErr](./api-1449054-aegetobjectaccessor.md)
  Gets an object accessor function from an object accessor dispatch table. 
- [func AERemoveObjectAccessor(DescType, DescType, OSLAccessorUPP!, Bool) -> OSErr](./api-1442552-aeremoveobjectaccessor.md)
  Removes an object accessor function from an object accessor dispatch table. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447905-aeinstallobjectaccessor)*