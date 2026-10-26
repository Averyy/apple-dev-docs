# IONetworkGetPacketFiltersMask

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Get the packet filters for a given filter group.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn IONetworkGetPacketFiltersMask(io_connect_t connect, const io_name_t filterGroup, UInt32 *filtersMask, IOOptionBits options);
```

#### Return Value

An IOReturn error code.

#### Discussion

A network controller may support a number of packets filters that can accept or reject a type of packet seen on the network. A filter group identifies a set of related filters, such as all filters that will allow a packet to pass upstream based on the destination address encoded within the packet. This function allows an user-space program to get the filtering performed by a given filter group.

## Parameters

- `connect`: The connection object returned from IONetworkOpen().
- `filterGroup`: The name of the packet filter group.
- `filtersMask`: Pointer to the return value containing a mask of packet filters.
- `options`: kIONetworkSupportedPacketFilters may be set to fetch the filters that are supported by the hardware.

## See Also

### Miscellaneous
- [IONetworkClose](./api-1572704-ionetworkclose.md)
  Close the connection to an IONetworkInterface object.
- [IONetworkGetDataCapacity](./api-1572712-ionetworkgetdatacapacity.md)
  Get the capacity (in bytes) of a network data object.
- [IONetworkGetDataHandle](./api-1572708-ionetworkgetdatahandle.md)
  Get the handle of a network data object with the given name.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1572711-ionetworkgetpacketfiltersmask)*