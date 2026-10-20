# IOReducedBlockServices

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOReducedBlockServices : IOBlockStorageDevice
```

## Topics

### Instance Methods
- [- attach](./ioreducedblockservices/api-1535502-attach.md)
- [- detach](./ioreducedblockservices/api-1535481-detach.md)
- [- doAsyncReadWrite](./ioreducedblockservices/api-1535499-doasyncreadwrite.md)
- [- doAsyncReadWrite](./ioreducedblockservices/api-3516741-doasyncreadwrite.md)
- [- doAsyncReadWrite](./ioreducedblockservices/api-3516742-doasyncreadwrite.md)
- [- doEjectMedia](./ioreducedblockservices/api-1535488-doejectmedia.md)
- [- doFormatMedia](./ioreducedblockservices/api-1535503-doformatmedia.md)
- [- doGetFormatCapacities](./ioreducedblockservices/api-1535504-dogetformatcapacities.md)
- [- doSynchronizeCache](./ioreducedblockservices/api-1535490-dosynchronizecache.md)
- [- free](./ioreducedblockservices/api-1535479-free.md)
- [- getAdditionalDeviceInfoString](./ioreducedblockservices/api-1535508-getadditionaldeviceinfostring.md)
- [- getMetaClass](./ioreducedblockservices/api-1535483-getmetaclass.md)
- [- getProductString](./ioreducedblockservices/api-1535492-getproductstring.md)
- [- getRevisionString](./ioreducedblockservices/api-1535487-getrevisionstring.md)
- [- getVendorString](./ioreducedblockservices/api-1535473-getvendorstring.md)
- [- getWriteCacheState](./ioreducedblockservices/api-1535477-getwritecachestate.md)
- [- message](./ioreducedblockservices/api-1535485-message.md)
- [- reportBlockSize](./ioreducedblockservices/api-1535471-reportblocksize.md)
- [- reportEjectability](./ioreducedblockservices/api-1535486-reportejectability.md)
- [- reportMaxValidBlock](./ioreducedblockservices/api-1535509-reportmaxvalidblock.md)
- [- reportMediaState](./ioreducedblockservices/api-1535470-reportmediastate.md)
- [- reportRemovability](./ioreducedblockservices/api-1535496-reportremovability.md)
- [- reportWriteProtection](./ioreducedblockservices/api-1535506-reportwriteprotection.md)
- [- setWriteCacheState](./ioreducedblockservices/api-1535497-setwritecachestate.md)
### Type Methods
- [+ AsyncReadWriteComplete](./ioreducedblockservices/api-1535475-asyncreadwritecomplete.md)

## Relationships

### Inherits From
- [IOBlockStorageDevice](./ioblockstoragedevice.md)

## See Also

### Base Types
- [IOSCSIPeripheralDeviceNub](./ioscsiperipheraldevicenub.md)
- [IOSCSIPrimaryCommandsDevice](./ioscsiprimarycommandsdevice.md)
- [IOSCSIProtocolServices](./ioscsiprotocolservices.md)
  This class defines the public SCSI Protocol Services Layer API for any class that implements SCSI protocol services. A protocol services layer driver is responsible for taking incoming SCSITaskIdentifier objects and translating them to the native command type for the native protocol interface (e.g. SBP-2 ORB on FireWire).
- [IOSCSIProtocolInterface](./ioscsiprotocolinterface.md)
  This class defines the public SCSI Protocol Layer API for any class that provides Protocol services or needs to provide the Protocol Service API for passing service requests to a Protocol Service driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioreducedblockservices)*