# IONetworkReadData

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Read the buffer of a network data object.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn IONetworkReadData(io_connect_t conObj, IONDHandle dataHandle, UInt8 *destBuf, UInt32 *inOutSizeP);
```

## Return Value

kIOReturnSuccess on success, or an error code otherwise.

## Parameters

- `conObj`: The connection object.
- `dataHandle`: The handle of a network data object.
- `destBuf`: The buffer where the data read shall be written to.
- `inOutSizeP`: Pointer to an integer that the caller must initialize to contain the size of the buffer. This function will overwrite it with the actual number of bytes written to the buffer.

## See Also

### Miscellaneous
- [IONetworkClose](./api-1572704-ionetworkclose.md)
  Close the connection to an IONetworkInterface object.
- [IONetworkGetDataCapacity](./api-1572712-ionetworkgetdatacapacity.md)
  Get the capacity (in bytes) of a network data object.
- [IONetworkGetDataHandle](./api-1572708-ionetworkgetdatahandle.md)
  Get the handle of a network data object with the given name.
- [IONetworkGetPacketFiltersMask](./api-1572711-ionetworkgetpacketfiltersmask.md)
  Get the packet filters for a given filter group.
- [IONetworkOpen](./api-1572709-ionetworkopen.md)
  Open a connection to an IONetworkInterface object. An IONetworkUserClient object is created to manage the connection.
- [IONetworkResetData](./api-1572710-ionetworkresetdata.md)
  Fill the buffer of a network data object with zeroes.
- [IONetworkSetPacketFiltersMask](./api-1572703-ionetworksetpacketfiltersmask.md)
  Set the packet filters for a given filter group.
- [IONetworkWriteData](./api-1572707-ionetworkwritedata.md)
  Write to the buffer of a network data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1572706-ionetworkreaddata)*