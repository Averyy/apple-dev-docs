# AECreateDescFromExternalPtr(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Creates a new descriptor that uses a memory buffer supplied by the caller.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AECreateDescFromExternalPtr(_ descriptorType: OSType, _ dataPtr: UnsafeRawPointer!, _ dataLength: Size, _ disposeCallback: AEDisposeExternalUPP!, _ disposeRefcon: SRefCon!, _ theDesc: UnsafeMutablePointer<AEDesc>!) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

This function is different than [`AECreateDesc(_:_:_:_:)`](1448535-aecreatedesc.md), in that it creates a descriptor that uses the data block provided by the caller “in place,” rather than allocate a block of memory and copy the data to it. This function can provide dramatically improved performance if you’re working with large chunks of data. It attempts to copy the descriptor to the address space of any recipient process using virtual memory APIs, avoiding an actual memory copy. For example, you might want to use this function to pass a large image in an Apple event.

You can use the [`AEGetDescDataRange(_:_:_:_:)`](1446560-aegetdescdatarange.md) function to access a specific section of a large block of data.

##### 1770173

Thread safe starting in OS X v10.2.

## Parameters

- `descriptorType`: The descriptor type for the new descriptor.
- `dataPtr`: The pointer that is passed in does not need to be aligned to any particular boundary, but is optimized to transfer data on a page boundary. You can get the current page size (4096 on all current macOS systems) with the   call. (Type  in a Terminal window for documentation.)
- `dataLength`: The length, in bytes, of the data for the new descriptor.
- `disposeCallback`: A universal procedure pointer to a dispose callback function of type  . Your callback function will be called when the block of memory provided by   is no longer needed by the Apple Event Manager. The function can be called at any time, including during creation of the descriptor.
- `disposeRefcon`: A reference constant the Apple Event Manager passes to the   function whenever it calls the function. If your dispose function doesn’t require a reference constant, pass 0 for this parameter. 
- `theDesc`: A pointer to a descriptor. On successful return, a descriptor that incorporates the data specified by the   parameter. On error, a null descriptor. If the function returns successfully, your application should call the   function to dispose of the resulting descriptor after it has finished using it.

## See Also

- [func AECreateDesc(DescType, UnsafeRawPointer!, Size, UnsafeMutablePointer<AEDesc>!) -> OSErr](1448535-aecreatedesc.md)
  Creates a new descriptor that incorporates the specified data.
- [func AEDuplicateDesc(UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](1442661-aeduplicatedesc.md)
  Creates a copy of a descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446239-aecreatedescfromexternalptr)*