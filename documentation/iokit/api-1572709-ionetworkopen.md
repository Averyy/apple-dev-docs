# IONetworkOpen

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Open a connection to an IONetworkInterface object. An IONetworkUserClient object is created to manage the connection.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn IONetworkOpen(io_object_t obj, io_connect_t *con);
```

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
- [IONetworkReadData](./api-1572706-ionetworkreaddata.md)
  Read the buffer of a network data object.
- [IONetworkResetData](./api-1572710-ionetworkresetdata.md)
  Fill the buffer of a network data object with zeroes.
- [IONetworkSetPacketFiltersMask](./api-1572703-ionetworksetpacketfiltersmask.md)
  Set the packet filters for a given filter group.
- [IONetworkWriteData](./api-1572707-ionetworkwritedata.md)
  Write to the buffer of a network data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1572709-ionetworkopen)*