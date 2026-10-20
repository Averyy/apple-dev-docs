# LaunchParamBlockRec

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct LaunchParamBlockRec
```

```c
typedef struct LaunchParamBlockRec {
    ...
} LaunchParamBlockRec;
```

## Topics

### Initializers
- [init()](./launchparamblockrec/api-1460224-init.md)
- [init(reserved1: UInt32, reserved2: UInt16, launchBlockID: UInt16, launchEPBLength: UInt32, launchFileFlags: UInt16, launchControlFlags: LaunchFlags, launchAppRef: FSRefPtr!, launchProcessSN: ProcessSerialNumber, launchPreferredSize: UInt32, launchMinimumSize: UInt32, launchAvailableSize: UInt32, launchAppParameters: AppParametersPtr!)](./launchparamblockrec/api-1459112-init.md)
### Instance Properties
- [var launchAppParameters: AppParametersPtr!](./launchparamblockrec/api-1459942-launchappparameters.md)
- [var launchAppRef: FSRefPtr!](./launchparamblockrec/api-1460856-launchappref.md)
- [var launchAvailableSize: UInt32](./launchparamblockrec/api-1459169-launchavailablesize.md)
- [var launchBlockID: UInt16](./launchparamblockrec/api-1462452-launchblockid.md)
- [var launchControlFlags: LaunchFlags](./launchparamblockrec/api-1460826-launchcontrolflags.md)
- [var launchEPBLength: UInt32](./launchparamblockrec/api-1459313-launchepblength.md)
- [var launchFileFlags: UInt16](./launchparamblockrec/api-1462584-launchfileflags.md)
- [var launchMinimumSize: UInt32](./launchparamblockrec/api-1461626-launchminimumsize.md)
- [var launchPreferredSize: UInt32](./launchparamblockrec/api-1462310-launchpreferredsize.md)
- [var launchProcessSN: ProcessSerialNumber](./launchparamblockrec/api-1459263-launchprocesssn.md)
- [var reserved1: UInt32](./launchparamblockrec/api-1460726-reserved1.md)
- [var reserved2: UInt16](./launchparamblockrec/api-1461414-reserved2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/launchparamblockrec)*