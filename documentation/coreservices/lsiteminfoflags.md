# LSItemInfoFlags

**Framework**: Core Services  
**Kind**: struct

The specification that provides information about an item.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct LSItemInfoFlags
```

#### Overview

These flags are set in an item-information record to provide information about an item; see [`LSItemInfoRecord`](lsiteminforecord.md) for a description of this structure.

## Topics

### Creating Item Information Flags
- [init(rawValue: OptionBits)](lsiteminfoflags/1442051-init.md)
### Constants
- [static var isPlainFile: LSItemInfoFlags](lsiteminfoflags/1444223-isplainfile.md)
  Item is a data file (and not, for example, a directory, volume, or UNIX symbolic link).
- [static var isPackage: LSItemInfoFlags](lsiteminfoflags/1449324-ispackage.md)
  Item is a packaged directory.
- [static var isApplication: LSItemInfoFlags](lsiteminfoflags/1449811-isapplication.md)
  Item is a single-file or packaged application.
- [static var isContainer: LSItemInfoFlags](lsiteminfoflags/1443420-iscontainer.md)
  Item is a directory (includes packages) or volume.
- [static var isAliasFile: LSItemInfoFlags](lsiteminfoflags/1444478-isaliasfile.md)
  Item is an alias file (includes symbolic links).
- [static var isSymlink: LSItemInfoFlags](lsiteminfoflags/1446223-issymlink.md)
  Item is a UNIX symbolic link.
- [static var isInvisible: LSItemInfoFlags](lsiteminfoflags/1449065-isinvisible.md)
  Item is invisible, because either its name begins with a period or its `isInvisible` Finder flag is set.
- [static var isNativeApp: LSItemInfoFlags](lsiteminfoflags/1443624-isnativeapp.md)
  Item is an application that can run natively in macOS.
- [static var isClassicApp: LSItemInfoFlags](lsiteminfoflags/1449915-isclassicapp.md)
  Item is an application that cannot run natively and must be launched in the Classic emulation environment.
- [static var appPrefersNative: LSItemInfoFlags](lsiteminfoflags/1446535-appprefersnative.md)
  Item is an application that can run either natively or in the Classic emulation environment, but prefers to be launched natively. This flag is valid only when `kLSItemInfoIsNativeApp` is set.
- [static var appPrefersClassic: LSItemInfoFlags](lsiteminfoflags/1447454-appprefersclassic.md)
  Item is an application that can run either natively or in the Classic emulation environment, but prefers tobe launched in the Classic environment. This flag is valid only when `kLSItemInfoIsNativeApp` isset.
- [static var appIsScriptable: LSItemInfoFlags](lsiteminfoflags/1448463-appisscriptable.md)
  Item is an application that can be scripted.
- [static var isVolume: LSItemInfoFlags](lsiteminfoflags/1448330-isvolume.md)
  Item is the root directory of a volume or mount point.
- [static var extensionIsHidden: LSItemInfoFlags](lsiteminfoflags/1445838-extensionishidden.md)
  Item has a hidden filename extension.

## Relationships

### Conforms To
- [OptionSet](../swift/optionset.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lsiteminfoflags)*