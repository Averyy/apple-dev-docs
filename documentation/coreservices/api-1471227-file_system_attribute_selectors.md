# File System Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability for the file system.

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
- [gestaltFSAttr](./api-1471227-file_system_attribute_selectors/gestaltfsattr.md)
  A selector you pass to the `Gestalt` function. If the Gestalt function returns `noErr`, the `response` parameter contains a 32-bit value specifying the features of the file system.
- [gestaltFullExtFSDispatching](./api-1471227-file_system_attribute_selectors/gestaltfullextfsdispatching.md)
- [gestaltHasFSSpecCalls](./api-1471227-file_system_attribute_selectors/gestalthasfsspeccalls.md)
  If this bit is set in the `response` parameter, the operating environment provides the file system specification (`FSSpec`) versions of the basic file-manipulation functions, as well as the `FSMakeFSSpec` function.
- [gestaltHasFileSystemManager](./api-1471227-file_system_attribute_selectors/gestalthasfilesystemmanager.md)
  If this bit is set in the `response` parameter, the File System Manager is present. See the *Guide to the File System Manager* for more information about the File System Manager. 
- [gestaltFSMDoesDynamicLoad](./api-1471227-file_system_attribute_selectors/gestaltfsmdoesdynamicload.md)
   If this bit is set in the `response` parameter, the File System Manager supports dynamic loading of external file system code resources.
- [gestaltFSSupports4GBVols](./api-1471227-file_system_attribute_selectors/gestaltfssupports4gbvols.md)
  If this bit is set in the `response` parameter, the file system supports 4 gigabyte volumes.
- [gestaltFSSupports2TBVols](./api-1471227-file_system_attribute_selectors/gestaltfssupports2tbvols.md)
  If this bit is set in the `response` parameter, the file system supports 2 terabyte volumes.
- [gestaltHasExtendedDiskInit](./api-1471227-file_system_attribute_selectors/gestalthasextendeddiskinit.md)
- [gestaltDTMgrSupportsFSM](./api-1471227-file_system_attribute_selectors/gestaltdtmgrsupportsfsm.md)
  If this bit is set in the `response` parameter, the desktop database supports File System Manager-based foreign file systems.
- [gestaltFSNoMFSVols](./api-1471227-file_system_attribute_selectors/gestaltfsnomfsvols.md)
  If this bit is set in the `response` parameter, the file system does not support MFS volumes. 
- [gestaltFSSupportsHFSPlusVols](./api-1471227-file_system_attribute_selectors/gestaltfssupportshfsplusvols.md)
  If this bit is set in the `response` parameter, the file system supports HFS Plus volumes. 
- [gestaltFSIncompatibleDFA82](./api-1471227-file_system_attribute_selectors/gestaltfsincompatibledfa82.md)
  If this bit is set in the `response` parameter, VCB and FCB structures are changed; DFA 8.2 is incompatible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471227-file_system_attribute_selectors)*