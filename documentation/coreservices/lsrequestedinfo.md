# LSRequestedInfo

**Framework**: Core Services  
**Kind**: struct

The specification that controls which information to obtain about an item.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct LSRequestedInfo
```

#### Overview

These flags are passed to the `LSCopyItemInfoForRef` and `LSCopyItemInfoForURL` functions to specify the type of information to be obtained in an item-information record; see [`LSItemInfoRecord`](lsiteminforecord.md) for a description of this structure.

## Topics

### Creating an Item Information Request
- [init(rawValue: OptionBits)](lsrequestedinfo/1443883-init.md)
### Constants
- [static var requestExtension: LSRequestedInfo](lsrequestedinfo/1448601-requestextension.md)
  Requests the item’s filename extension.
- [static var requestTypeCreator: LSRequestedInfo](lsrequestedinfo/1446509-requesttypecreator.md)
  Requests the item’s file type and creator signature.
- [static var requestBasicFlagsOnly: LSRequestedInfo](lsrequestedinfo/1447145-requestbasicflagsonly.md)
  Requests all item-information flags that are not application-specific: that is, all except `kLSItemInfoIsNativeApp` through `kLSItemInfoAppIsScriptable`.
- [static var requestAppTypeFlags: LSRequestedInfo](lsrequestedinfo/1442110-requestapptypeflags.md)
  Requests all application-specific item-information flags: that is, `kLSItemInfoIsNativeApp` through `kLSItemInfoAppIsScriptable`.
- [static var requestAllFlags: LSRequestedInfo](lsrequestedinfo/1445356-requestallflags.md)
  Requests all item-information flags.
- [static var requestIconAndKind: LSRequestedInfo](lsrequestedinfo/1447945-requesticonandkind.md)
  Not used.
- [static var requestExtensionFlagsOnly: LSRequestedInfo](lsrequestedinfo/1445164-requestextensionflagsonly.md)
  Requests only the `kLSItemInfoExtensionIsHidden` item-information flag.
- [static var requestAllInfo: LSRequestedInfo](lsrequestedinfo/1447901-requestallinfo.md)
  Requests all available item information.

## Relationships

### Conforms To
- [OptionSet](../swift/optionset.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lsrequestedinfo)*