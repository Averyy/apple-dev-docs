# IONetworkGetDataHandle

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Get the handle of a network data object with the given name.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn IONetworkGetDataHandle(io_connect_t conObject, const char *dataName, IONDHandle *dataHandleP);
```

## Return Value

kIOReturnSuccess on success, or an error code otherwise.

## Parameters

- `conObject`: The connection object.
- `dataName`: The name of the network data object.
- `dataHandleP`: Upon success, the handle is written to this address.

## See Also

### Miscellaneous
- [IONetworkClose](./api-1572704-ionetworkclose.md)
  Close the connection to an IONetworkInterface object.
- [IONetworkGetDataCapacity](./api-1572712-ionetworkgetdatacapacity.md)
  Get the capacity (in bytes) of a network data object.
- [IONetworkGetPacketFiltersMask](./api-1572711-ionetworkgetpacketfiltersmask.md)
  Get the packet filters for a given filter group.
- [IONetworkOpen](./api-1572709-ionetworkopen.md)
  Open a connection to an IONetworkInterface object. An IONetworkUserClient object is created to manage the connection.
- [IONetworkReadData](./api-1572706-ionetworkreaddata.md)
  Read the buffer of a network data object.
- [IONetworkResetData](./api-1572710-ionetworkresetdata.md)
  Fill the buffer of a network data object with zeroes.
- [IONetworkSetPacketFiltersMask](./api-1572703-ionetworksetpacketfiltersmask.md)
  Set the packet filters for a given filter group.
- [IONetworkWriteData](./api-1572707-ionetworkwritedata.md)
  Write to the buffer of a network data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1572708-ionetworkgetdatahandle)*