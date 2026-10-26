# Folder Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the Folder Manager.

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
- [gestaltFindFolderAttr](./api-1473089-folder_manager_attribute_selecto/gestaltfindfolderattr.md)
  The selector you pass to the `Gestalt` function to determine the  `FindFolder` function attributes.
- [gestaltFindFolderPresent](./api-1473089-folder_manager_attribute_selecto/gestaltfindfolderpresent.md)
- [gestaltFolderDescSupport](./api-1473089-folder_manager_attribute_selecto/gestaltfolderdescsupport.md)
  If this bit is set, the extended Folder Manager functionality supporting folder descriptors and routings is available. This bit is set for versions of the Mac OS starting with Mac OS 8.
- [gestaltFolderMgrFollowsAliasesWhenResolving](./api-1473089-folder_manager_attribute_selecto/gestaltfoldermgrfollowsaliaseswhenresolving.md)
- [gestaltFolderMgrSupportsExtendedCalls](./api-1473089-folder_manager_attribute_selecto/gestaltfoldermgrsupportsextendedcalls.md)
- [gestaltFolderMgrSupportsDomains](./api-1473089-folder_manager_attribute_selecto/gestaltfoldermgrsupportsdomains.md)
- [gestaltFolderMgrSupportsFSCalls](./api-1473089-folder_manager_attribute_selecto/gestaltfoldermgrsupportsfscalls.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1473089-folder_manager_attribute_selecto)*