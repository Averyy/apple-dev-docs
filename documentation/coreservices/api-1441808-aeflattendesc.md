# AEFlattenDesc(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Flattens the specified descriptor and stores the data in the supplied buffer.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEFlattenDesc(_ theAEDesc: UnsafePointer<AEDesc>!, _ buffer: Ptr!, _ bufferSize: Size, _ actualSize: UnsafeMutablePointer<Size>!) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Flattening a descriptor serializes the data it contains. That is, it reduces a complex, possibly deeply nested structure to a series of bytes that can conveniently be stored. The descriptor can be reconstituted from the stored bytes with the [`AEUnflattenDesc(_:_:)`](1448997-aeunflattendesc.md) function.

Applications can be scriptable and work with Apple events without needing to flatten and unflatten descriptors. Flattening is a special-purpose capability that is useful in circumstances where it may be convenient to store data by saving and restoring a descriptor, rather than having to manually extract the data from it, store the data as a separate step, then manually recreate the descriptor (if necessary). For example, you might use flattening to store a preference setting received through an Apple event.

Flattening and unflattening should work without loss of data on descriptors that represent `AEDesc`, `AEList`, and `AERecord` structures. You can also use the process with `AppleEvent` descriptors. However, keep in mind that Apple events may contain attributes that are relevant only to a running process, and these attributes may not keep their meaning when the event is reconstituted.

Flattening and unflattening works across OS versions, including between Mac OS 9 and macOS.

Flattening is endian-neutral. That is, you can save flattened data on a machine that is either big-endian or little-endian, then retrieve and unflatten the data on either type of machine, without any special steps by your application.

##### 1770222

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDesc`: A pointer to the descriptor to be flattened. See  .
- `buffer`: A pointer to memory, allocated by the application, where the flattened data will be stored. See the   parameter for information on how large a buffer you should allocate.
- `bufferSize`: If   is too small,   returns   and doesn’t store any data in the buffer.
- `actualSize`: A pointer to a size variable. On return, the variable contains the actual size of the flattened data. You can specify   for this parameter if you do not care about the returned size.

## See Also

- [func AESizeOfFlattenedDesc(UnsafePointer<AEDesc>!) -> Size](1447305-aesizeofflatteneddesc.md)
  Returns the amount of buffer space needed to store the descriptor after flattening it.
- [func AEUnflattenDesc(UnsafeRawPointer!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](1448997-aeunflattendesc.md)
  Unflattens the data in the passed buffer and creates a descriptor from it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1441808-aeflattendesc)*