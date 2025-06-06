# AECoerceDesc(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Coerces the data in a descriptor to another descriptor type and creates a descriptor containing the newly coerced data.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AECoerceDesc(_ theAEDesc: UnsafePointer<AEDesc>!, _ toType: DescType, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145). If `AECoerceDesc` returns a nonzero result code, it returns a null descriptor record (a descriptor record of type `typeNull`, which does not contain any data) unless the Apple Event Manager is not available because of limited memory.

#### Discussion

See the Version Notes section for the [`AECoercePtr(_:_:_:_:_:)`](1441846-aecoerceptr.md) function for information on when to use descriptor-based versus pointer-based coercion handlers starting in OS X version 10.2.

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDesc`: A pointer to the descriptor containing the data to coerce. See  .
- `toType`: The desired descriptor type of the resulting descriptor. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `result`: A pointer to a descriptor. On successful return, a descriptor containing the coerced data and matching the descriptor type specified in  . On error, a null descriptor. If the function returns successfully, your application should call the   function to dispose of the resulting descriptor after it has finished using it.

## See Also

- [func AECoercePtr(DescType, UnsafeRawPointer!, Size, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](1441846-aecoerceptr.md)
  Coerces data to a desired descriptor type and creates a descriptor containing the newly coerced data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446519-aecoercedesc)*