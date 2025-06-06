# AEUnflattenDesc(_:_:)

**Framework**: Core Services  
**Kind**: func

Unflattens the data in the passed buffer and creates a descriptor from it.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```swift
func AEUnflattenDesc(_ buffer: UnsafeRawPointer!, _ result: UnsafeMutablePointer<AEDesc>!) -> OSStatus
```

#### Return_value

A result code. Returns `paramErr` if the flattened data in `buffer` is found to be invalid. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145) for other possible values.

#### Discussion

This function assumes the passed buffer contains valid flattened data, produced by a previous call to [`AEFlattenDesc(_:_:_:_:)`](1441808-aeflattendesc.md). See that function for a description of when you might want to flatten and unflatten descriptors, and of possible limitations.

Flattening and unflattening works across OS versions, including between Mac OS 9 and macOS.

Flattening is endian-neutral. That is, you can save flattened data on a machine that is either big-endian or little-endian, then retrieve and unflatten the data on either type of machine, without any special steps by your application.

##### 1770225

Thread safe starting in OS X v10.2.

## Parameters

- `buffer`: A pointer to memory, allocated by the application, that contains flattened data produced by a previous call to  .
- `result`: A null descriptor. On successful completion, points to a descriptor created from the flattened data. The caller is responsible for disposing of the descriptor.

## See Also

- [func AESizeOfFlattenedDesc(UnsafePointer<AEDesc>!) -> Size](1447305-aesizeofflatteneddesc.md)
  Returns the amount of buffer space needed to store the descriptor after flattening it.
- [func AEFlattenDesc(UnsafePointer<AEDesc>!, Ptr!, Size, UnsafeMutablePointer<Size>!) -> OSStatus](1441808-aeflattendesc.md)
  Flattens the specified descriptor and stores the data in the supplied buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448997-aeunflattendesc)*