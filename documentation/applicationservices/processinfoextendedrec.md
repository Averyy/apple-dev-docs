# ProcessInfoExtendedRec

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct ProcessInfoExtendedRec
```

```c
typedef struct ProcessInfoExtendedRec {
    ...
} ProcessInfoExtendedRec;
```

## Topics

### Initializers
- [init()](./processinfoextendedrec/api-1464665-init.md)
- [init(processInfoLength: UInt32, processName: StringPtr!, processNumber: ProcessSerialNumber, processType: UInt32, processSignature: OSType, processMode: UInt32, processLocation: Ptr!, processSize: UInt32, processFreeMem: UInt32, processLauncher: ProcessSerialNumber, processLaunchDate: UInt32, processActiveTime: UInt32, processAppRef: FSRefPtr!, processTempMemTotal: UInt32, processPurgeableTempMemTotal: UInt32)](./processinfoextendedrec/api-1462532-init.md)
### Instance Properties
- [var processActiveTime: UInt32](./processinfoextendedrec/api-1461059-processactivetime.md)
- [var processAppRef: FSRefPtr!](./processinfoextendedrec/api-1464388-processappref.md)
- [var processFreeMem: UInt32](./processinfoextendedrec/api-1458795-processfreemem.md)
- [var processInfoLength: UInt32](./processinfoextendedrec/api-1461721-processinfolength.md)
- [var processLaunchDate: UInt32](./processinfoextendedrec/api-1460999-processlaunchdate.md)
- [var processLauncher: ProcessSerialNumber](./processinfoextendedrec/api-1462399-processlauncher.md)
- [var processLocation: Ptr!](./processinfoextendedrec/api-1463684-processlocation.md)
- [var processMode: UInt32](./processinfoextendedrec/api-1462055-processmode.md)
- [var processName: StringPtr!](./processinfoextendedrec/api-1462598-processname.md)
- [var processNumber: ProcessSerialNumber](./processinfoextendedrec/api-1464114-processnumber.md)
- [var processPurgeableTempMemTotal: UInt32](./processinfoextendedrec/api-1458942-processpurgeabletempmemtotal.md)
- [var processSignature: OSType](./processinfoextendedrec/api-1461232-processsignature.md)
- [var processSize: UInt32](./processinfoextendedrec/api-1459964-processsize.md)
- [var processTempMemTotal: UInt32](./processinfoextendedrec/api-1459478-processtempmemtotal.md)
- [var processType: UInt32](./processinfoextendedrec/api-1459518-processtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/processinfoextendedrec)*