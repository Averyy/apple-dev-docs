# IOSCSIPeripheralDeviceNub

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOSCSIPeripheralDeviceNub : IOSCSIProtocolServices
```

## Topics

### Instance Methods
- [- AbortCommand](./ioscsiperipheraldevicenub/api-1569619-abortcommand.md)
- [- AbortSCSICommand](./ioscsiperipheraldevicenub/api-1569638-abortscsicommand.md)
- [- AbortTask](./ioscsiperipheraldevicenub/api-1569615-aborttask.md)
- [- AbortTaskSet](./ioscsiperipheraldevicenub/api-1569627-aborttaskset.md)
- [- ClearACA](./ioscsiperipheraldevicenub/api-1569617-clearaca.md)
- [- ClearTaskSet](./ioscsiperipheraldevicenub/api-1569643-cleartaskset.md)
- [- ExecuteCommand](./ioscsiperipheraldevicenub/api-1569647-executecommand.md)
- [- GatedWaitForTask](./ioscsiperipheraldevicenub/api-1569628-gatedwaitfortask.md)
- [- HandleProtocolServiceFeature](./ioscsiperipheraldevicenub/api-1569623-handleprotocolservicefeature.md)
- [- InterrogateDevice](./ioscsiperipheraldevicenub/api-1569645-interrogatedevice.md)
- [- IsProtocolServiceSupported](./ioscsiperipheraldevicenub/api-1569634-isprotocolservicesupported.md)
- [- LogicalUnitReset](./ioscsiperipheraldevicenub/api-1569633-logicalunitreset.md)
- [- SendSCSICommand](./ioscsiperipheraldevicenub/api-1569613-sendscsicommand.md)
- [- SendTask](./ioscsiperipheraldevicenub/api-1569640-sendtask.md)
- [- TargetReset](./ioscsiperipheraldevicenub/api-1569616-targetreset.md)
- [- TaskCompletion](./ioscsiperipheraldevicenub/api-1569629-taskcompletion.md)
- [- free](./ioscsiperipheraldevicenub/api-1569631-free.md)
- [- getMetaClass](./ioscsiperipheraldevicenub/api-1569622-getmetaclass.md)
- [- init](./ioscsiperipheraldevicenub/api-1569624-init.md)
- [- matchPropertyTable](./ioscsiperipheraldevicenub/api-1569630-matchpropertytable.md)
- [- message](./ioscsiperipheraldevicenub/api-1569636-message.md)
- [- setProperties](./ioscsiperipheraldevicenub/api-4520031-setproperties.md)
- [- start](./ioscsiperipheraldevicenub/api-1569646-start.md)
### Type Methods
- [+ TaskCallback](./ioscsiperipheraldevicenub/api-1569632-taskcallback.md)
- [+ sCompareIOProperty](./ioscsiperipheraldevicenub/api-1569611-scompareioproperty.md)
- [+ sWaitForTask](./ioscsiperipheraldevicenub/api-1569614-swaitfortask.md)

## Relationships

### Inherits From
- [IOSCSIProtocolServices](./ioscsiprotocolservices.md)

## See Also

### Base Types
- [IOReducedBlockServices](./ioreducedblockservices.md)
- [IOSCSIPrimaryCommandsDevice](./ioscsiprimarycommandsdevice.md)
- [IOSCSIProtocolServices](./ioscsiprotocolservices.md)
  This class defines the public SCSI Protocol Services Layer API for any class that implements SCSI protocol services. A protocol services layer driver is responsible for taking incoming SCSITaskIdentifier objects and translating them to the native command type for the native protocol interface (e.g. SBP-2 ORB on FireWire).
- [IOSCSIProtocolInterface](./ioscsiprotocolinterface.md)
  This class defines the public SCSI Protocol Layer API for any class that provides Protocol services or needs to provide the Protocol Service API for passing service requests to a Protocol Service driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiperipheraldevicenub)*