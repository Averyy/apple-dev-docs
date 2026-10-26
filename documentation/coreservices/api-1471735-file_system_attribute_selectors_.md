# File System Attribute Selectors for Mac OS 9

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability for the file system for features introduced in Mac OS 9.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltHasHFSPlusAPIs](./api-1471735-file_system_attribute_selectors_/gestalthashfsplusapis.md)
- [gestaltMustUseFCBAccessors](./api-1471735-file_system_attribute_selectors_/gestaltmustusefcbaccessors.md)
  If this bit is set in the `response` parameter, the File Manager no longer supports the low memory globals `FCBSPtr` and `FSFCBLen`. All access to file or fork control blocks must use the File System Manager utility functions instead. 
- [gestaltFSUsesPOSIXPathsForConversion](./api-1471735-file_system_attribute_selectors_/gestaltfsusesposixpathsforconversion.md)
- [gestaltFSSupportsExclusiveLocks](./api-1471735-file_system_attribute_selectors_/gestaltfssupportsexclusivelocks.md)
- [gestaltFSSupportsHardLinkDetection](./api-1471735-file_system_attribute_selectors_/gestaltfssupportshardlinkdetection.md)
- [gestaltFSAllowsConcurrentAsyncIO](./api-1471735-file_system_attribute_selectors_/gestaltfsallowsconcurrentasyncio.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471735-file_system_attribute_selectors_)*