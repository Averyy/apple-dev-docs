# AECoercePtr(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Coerces data to a desired descriptor type and creates a descriptor containing the newly coerced data.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AECoercePtr(_ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size, _ toType: DescType, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Starting in OS X version 10.2, pointer-based coercion handlers are not called if the input type is “structured”—that is, if the type to be coerced is `typeAEList`, `typeAERecord`, or coerced `typeAERecord`. If you want to add a coercion handler for one of these types, it must be a descriptor-based handler. This does not mean you are required to use descriptor-based coercion handlers everywhere—for “flat” data types, such as `typeText`, pointer-based handlers are still fine.

Thread safe starting in OS X v10.2.

## Parameters

- `typeCode`: The descriptor type of the source data. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `dataPtr`: A pointer to the data to coerce.
- `dataSize`: The length, in bytes, of the data to coerce.
- `toType`: The desired descriptor type of the resulting descriptor. For a list of AppleScript’s predefined descriptor types, see  .
- `result`: A pointer to a descriptor. On successful return, a descriptor containing the coerced data and matching the descriptor type specified in  . On error, a null descriptor. If the function returns successfully, your application should call the   function to dispose of the resulting descriptor after it has finished using it. See  .

## See Also

- [func AECoerceDesc(UnsafePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](1446519-aecoercedesc.md)
  Coerces the data in a descriptor to another descriptor type and creates a descriptor containing the newly coerced data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1441846-aecoerceptr)*