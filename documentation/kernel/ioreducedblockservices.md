# IOReducedBlockServices

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOReducedBlockServices : IOBlockStorageDevice
```

## Topics

### Instance Methods
- [- attach](ioreducedblockservices/1535502-attach.md)
- [- detach](ioreducedblockservices/1535481-detach.md)
- [- doAsyncReadWrite](ioreducedblockservices/1535499-doasyncreadwrite.md)
- [- doAsyncReadWrite](ioreducedblockservices/3516741-doasyncreadwrite.md)
- [- doAsyncReadWrite](ioreducedblockservices/3516742-doasyncreadwrite.md)
- [- doEjectMedia](ioreducedblockservices/1535488-doejectmedia.md)
- [- doFormatMedia](ioreducedblockservices/1535503-doformatmedia.md)
- [- doGetFormatCapacities](ioreducedblockservices/1535504-dogetformatcapacities.md)
- [- doSynchronizeCache](ioreducedblockservices/1535490-dosynchronizecache.md)
- [- free](ioreducedblockservices/1535479-free.md)
- [- getAdditionalDeviceInfoString](ioreducedblockservices/1535508-getadditionaldeviceinfostring.md)
- [- getMetaClass](ioreducedblockservices/1535483-getmetaclass.md)
- [- getProductString](ioreducedblockservices/1535492-getproductstring.md)
- [- getRevisionString](ioreducedblockservices/1535487-getrevisionstring.md)
- [- getVendorString](ioreducedblockservices/1535473-getvendorstring.md)
- [- getWriteCacheState](ioreducedblockservices/1535477-getwritecachestate.md)
- [- message](ioreducedblockservices/1535485-message.md)
- [- reportBlockSize](ioreducedblockservices/1535471-reportblocksize.md)
- [- reportEjectability](ioreducedblockservices/1535486-reportejectability.md)
- [- reportMaxValidBlock](ioreducedblockservices/1535509-reportmaxvalidblock.md)
- [- reportMediaState](ioreducedblockservices/1535470-reportmediastate.md)
- [- reportRemovability](ioreducedblockservices/1535496-reportremovability.md)
- [- reportWriteProtection](ioreducedblockservices/1535506-reportwriteprotection.md)
- [- setWriteCacheState](ioreducedblockservices/1535497-setwritecachestate.md)
### Type Methods
- [+ AsyncReadWriteComplete](ioreducedblockservices/1535475-asyncreadwritecomplete.md)

## Relationships

### Inherits From
- [IOBlockStorageDevice](ioblockstoragedevice.md)

## See Also

- [IOSCSIPeripheralDeviceNub](ioscsiperipheraldevicenub.md)
- [IOSCSIPrimaryCommandsDevice](ioscsiprimarycommandsdevice.md)
- [IOSCSIProtocolServices](ioscsiprotocolservices.md)
  This class defines the public SCSI Protocol Services Layer API for any class that implements SCSI protocol services. A protocol services layer driver is responsible for taking incoming SCSITaskIdentifier objects and translating them to the native command type for the native protocol interface (e.g. SBP-2 ORB on FireWire).
- [IOSCSIProtocolInterface](ioscsiprotocolinterface.md)
  This class defines the public SCSI Protocol Layer API for any class that provides Protocol services or needs to provide the Protocol Service API for passing service requests to a Protocol Service driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioreducedblockservices)*