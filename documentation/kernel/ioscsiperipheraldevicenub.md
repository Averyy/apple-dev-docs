# IOSCSIPeripheralDeviceNub

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOSCSIPeripheralDeviceNub : IOSCSIProtocolServices
```

## Topics

### Instance Methods
- [- AbortCommand](ioscsiperipheraldevicenub/1569619-abortcommand.md)
- [- AbortSCSICommand](ioscsiperipheraldevicenub/1569638-abortscsicommand.md)
- [- AbortTask](ioscsiperipheraldevicenub/1569615-aborttask.md)
- [- AbortTaskSet](ioscsiperipheraldevicenub/1569627-aborttaskset.md)
- [- ClearACA](ioscsiperipheraldevicenub/1569617-clearaca.md)
- [- ClearTaskSet](ioscsiperipheraldevicenub/1569643-cleartaskset.md)
- [- ExecuteCommand](ioscsiperipheraldevicenub/1569647-executecommand.md)
- [- GatedWaitForTask](ioscsiperipheraldevicenub/1569628-gatedwaitfortask.md)
- [- HandleProtocolServiceFeature](ioscsiperipheraldevicenub/1569623-handleprotocolservicefeature.md)
- [- InterrogateDevice](ioscsiperipheraldevicenub/1569645-interrogatedevice.md)
- [- IsProtocolServiceSupported](ioscsiperipheraldevicenub/1569634-isprotocolservicesupported.md)
- [- LogicalUnitReset](ioscsiperipheraldevicenub/1569633-logicalunitreset.md)
- [- SendSCSICommand](ioscsiperipheraldevicenub/1569613-sendscsicommand.md)
- [- SendTask](ioscsiperipheraldevicenub/1569640-sendtask.md)
- [- TargetReset](ioscsiperipheraldevicenub/1569616-targetreset.md)
- [- TaskCompletion](ioscsiperipheraldevicenub/1569629-taskcompletion.md)
- [- free](ioscsiperipheraldevicenub/1569631-free.md)
- [- getMetaClass](ioscsiperipheraldevicenub/1569622-getmetaclass.md)
- [- init](ioscsiperipheraldevicenub/1569624-init.md)
- [- matchPropertyTable](ioscsiperipheraldevicenub/1569630-matchpropertytable.md)
- [- message](ioscsiperipheraldevicenub/1569636-message.md)
- [- setProperties](ioscsiperipheraldevicenub/4520031-setproperties.md)
- [- start](ioscsiperipheraldevicenub/1569646-start.md)
### Type Methods
- [+ TaskCallback](ioscsiperipheraldevicenub/1569632-taskcallback.md)
- [+ sCompareIOProperty](ioscsiperipheraldevicenub/1569611-scompareioproperty.md)
- [+ sWaitForTask](ioscsiperipheraldevicenub/1569614-swaitfortask.md)

## Relationships

### Inherits From
- [IOSCSIProtocolServices](ioscsiprotocolservices.md)

## See Also

- [IOReducedBlockServices](ioreducedblockservices.md)
- [IOSCSIPrimaryCommandsDevice](ioscsiprimarycommandsdevice.md)
- [IOSCSIProtocolServices](ioscsiprotocolservices.md)
  This class defines the public SCSI Protocol Services Layer API for any class that implements SCSI protocol services. A protocol services layer driver is responsible for taking incoming SCSITaskIdentifier objects and translating them to the native command type for the native protocol interface (e.g. SBP-2 ORB on FireWire).
- [IOSCSIProtocolInterface](ioscsiprotocolinterface.md)
  This class defines the public SCSI Protocol Layer API for any class that provides Protocol services or needs to provide the Protocol Service API for passing service requests to a Protocol Service driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiperipheraldevicenub)*