# kLSLaunchInClassic

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

A request that the system forces the app to launch in the Classic emulation environment.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

## Declaration

```c
kLSLaunchInClassic = 0x00040000
```

## See Also

### Deprecated Variables
- [kLSLaunchHasUntrustedContents](./klslaunchhasuntrustedcontents.md)
  A request that the system marks the launch items as untrustworthy. 
- [kLSLaunchNoParams](./klslaunchnoparams.md)
  A request that the system uses the app’s information property to determine the launch parameters.
- [kLSLaunchInhibitBGOnly](./klslaunchinhibitbgonly.md)
  A request that the system fails the launch if the app is background-only.
- [kLSLaunchStartClassic](./klslaunchstartclassic.md)
  A request that the system starts up the Classic emulation environment if the app requires it. If this flag is not set and the app requires the Classic environment, the launch fails.
- [kLSItemQuarantineProperties](../klsitemquarantineproperties.md)
- [kLSSharedFileListFavoriteItems](../klssharedfilelistfavoriteitems.md)
- [kLSSharedFileListFavoriteVolumes](../klssharedfilelistfavoritevolumes.md)
- [kLSSharedFileListGlobalLoginItems](../klssharedfilelistgloballoginitems.md)
- [kLSSharedFileListItemBeforeFirst](../klssharedfilelistitembeforefirst.md)
- [kLSSharedFileListItemHidden](../klssharedfilelistitemhidden.md)
- [kLSSharedFileListItemLast](../klssharedfilelistitemlast.md)
- [kLSSharedFileListLoginItemHidden](../klssharedfilelistloginitemhidden.md)
- [kLSSharedFileListRecentApplicationItems](../klssharedfilelistrecentapplicationitems.md)
- [kLSSharedFileListRecentDocumentItems](../klssharedfilelistrecentdocumentitems.md)
- [kLSSharedFileListRecentItemsMaxAmount](../klssharedfilelistrecentitemsmaxamount.md)
- [kLSSharedFileListRecentServerItems](../klssharedfilelistrecentserveritems.md)
- [kLSSharedFileListSessionLoginItems](../klssharedfilelistsessionloginitems.md)
- [kLSSharedFileListVolumesComputerVisible](../klssharedfilelistvolumescomputervisible.md)
- [kLSSharedFileListVolumesIDiskVisible](../klssharedfilelistvolumesidiskvisible.md)
- [kLSSharedFileListVolumesNetworkVisible](../klssharedfilelistvolumesnetworkvisible.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1645929-anonymous/klslaunchinclassic)*