# LSItemInfoRecord

**Framework**: Core Services  
**Kind**: struct

The specification that contains requested information about an item.

**Availability**:
- Mac Catalyst 13.0+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.11

## Declaration

```swift
struct LSItemInfoRecord
```

#### Overview

This data type defines an item-information record used bythe `LSCopyItemInfoForRef` and `LSCopyItemInfoForURL` functionsto return requested information about an item.

## Topics

### Initializers
- [init()](lsiteminforecord/1445690-init.md)
- [init(flags: LSItemInfoFlags, filetype: OSType, creator: OSType, extension: Unmanaged<CFString>!)](lsiteminforecord/1448481-init.md)
### Instance Properties
- [var creator: OSType](lsiteminforecord/1441870-creator.md)
  The item’s creator signature.
- [var `extension`: Unmanaged<CFString>!](lsiteminforecord/1442123-extension.md)
  A Core Foundation string object specifying theitem’s filename extension; see the  inthe Core Foundation Reference Documentation for a description ofthe `CFStringRef` datatype.
- [var filetype: OSType](lsiteminforecord/1447384-filetype.md)
  The item’s file type.
- [var flags: LSItemInfoFlags](lsiteminforecord/1446281-flags.md)
  Item-information flags specifying informationabout the item; see [`LSItemInfoFlags`](lsiteminfoflags.md) for a description of these flags.

## See Also

- [struct LSApplicationParameters](lsapplicationparameters.md)
  The specification that defines the app, launch flags, and additional parameters that control how an app launches.
- [struct LSLaunchFSRefSpec](lslaunchfsrefspec.md)
  The specification that defines, by file-system reference, an app to launch, items to open, or both, along with related information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lsiteminforecord)*