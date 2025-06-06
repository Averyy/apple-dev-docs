# AECreateDesc(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Creates a new descriptor that incorporates the specified data.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AECreateDesc(_ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

While it is possible to create an Apple event descriptor or a descriptor list or a descriptor with the `AECreateDesc` function (assuming you have access to the raw data for an Apple event, list, or descriptor), you typically create these structured objects with their specific creation routines—`AECreateAppleEvent`, `AECreateList`, or `AECreateDesc`. 

##### 1770172

Thread safe starting in OS X v10.2.

## Parameters

- `typeCode`: The descriptor type for the new descriptor. For a list of AppleScript’s predefined descriptor types, see  . See  .
- `dataPtr`: A pointer to the data for the new descriptor. This data is copied into a newly-allocated block of memory for the descriptor that is created. To minimize copying overhead, consider using  .
- `dataSize`: The length, in bytes, of the data for the new descriptor.
- `result`: A pointer to a descriptor. On successful return, a descriptor that incorporates the data specified by the   parameter. On error, a null descriptor. If the function returns successfully, your application should call the   function to dispose of the resulting descriptor after it has finished using it. See  .

## See Also

- [func AECreateDescFromExternalPtr(OSType, UnsafeRawPointer!, Size, AEDisposeExternalUPP!, SRefCon!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](1446239-aecreatedescfromexternalptr.md)
  Creates a new descriptor that uses a memory buffer supplied by the caller.
- [func AEDuplicateDesc(UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](1442661-aeduplicatedesc.md)
  Creates a copy of a descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448535-aecreatedesc)*