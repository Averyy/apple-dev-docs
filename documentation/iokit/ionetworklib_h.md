# IONetworkLib.h

**Framework**: IOKit  
**Role**: API Collection

## Overview

### Included Headers

- <IOKit/IOKitLib.h>
- <IOKit/network/IONetworkData.h>
- <IOKit/network/IONetworkMedium.h>
- <IOKit/network/IONetworkStats.h>
- <IOKit/network/IOEthernetStats.h>
- <IOKit/network/IONetworkUserClient.h>

## Topics

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
- [IONetworkReadData](./api-1572706-ionetworkreaddata.md)
  Read the buffer of a network data object.
- [IONetworkResetData](./api-1572710-ionetworkresetdata.md)
  Fill the buffer of a network data object with zeroes.
- [IONetworkSetPacketFiltersMask](./api-1572703-ionetworksetpacketfiltersmask.md)
  Set the packet filters for a given filter group.
- [IONetworkWriteData](./api-1572707-ionetworkwritedata.md)
  Write to the buffer of a network data object.
### Constants
- [IONetworkPacketFilterOptions](./api-1572705-ionetworkpacketfilteroptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ionetworklib_h)*