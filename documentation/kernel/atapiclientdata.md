# ATAPIClientData

**Framework**: Kernel  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 11.0+

## Declaration

```c
typedef struct ATAPIClientData {
    ...
} ATAPIClientData;
```

## Overview

This structure is stuffed into the refcon so we can associate which IOATACommand and SCSITaskIdentifier is completing.

## Topics

### Instance Properties
- [cmd](./atapiclientdata/api-1550957-cmd.md)
  IOATACommand for request.
- [scsiTask](./atapiclientdata/api-1550980-scsitask.md)
  SCSITaskIdentifier of request.
- [self](./atapiclientdata/api-1550940-self.md)
  Pointer to the object.

## See Also

### ATAPI
- [IOATAPIProtocolTransport](./ioatapiprotocoltransport.md)
  SCSI Protocol Driver Family for ATAPI Devices.
- [ATAPICmdPacket](./atapicmdpacket.md)
### Related Documentation
- [pseudoSymbol-1811777](pseudoSymbol-1811777)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/atapiclientdata)*