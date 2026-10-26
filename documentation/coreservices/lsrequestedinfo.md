# LSRequestedInfo

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

The specification that controls which information to obtain about an item.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct LSRequestedInfo
```

```c
typedef enum LSRequestedInfo : OptionBits {
    ...
} LSRequestedInfo;
```

#### Overview

These flags are passed to the `LSCopyItemInfoForRef` and `LSCopyItemInfoForURL` functions to specify the type of information to be obtained in an item-information record; see [`LSItemInfoRecord`](./lsiteminforecord.md) for a description of this structure.

## Topics

### Creating an Item Information Request
- [init(rawValue: OptionBits)](./lsrequestedinfo/api-1443883-init.md)
### Constants
- [static var requestExtension: LSRequestedInfo](./lsrequestedinfo/api-1448601-requestextension.md)
  Requests the item’s filename extension.
- [static var requestTypeCreator: LSRequestedInfo](./lsrequestedinfo/api-1446509-requesttypecreator.md)
  Requests the item’s file type and creator signature.
- [static var requestBasicFlagsOnly: LSRequestedInfo](./lsrequestedinfo/api-1447145-requestbasicflagsonly.md)
  Requests all item-information flags that are not application-specific: that is, all except `kLSItemInfoIsNativeApp` through `kLSItemInfoAppIsScriptable`.
- [static var requestAppTypeFlags: LSRequestedInfo](./lsrequestedinfo/api-1442110-requestapptypeflags.md)
  Requests all application-specific item-information flags: that is, `kLSItemInfoIsNativeApp` through `kLSItemInfoAppIsScriptable`.
- [static var requestAllFlags: LSRequestedInfo](./lsrequestedinfo/api-1445356-requestallflags.md)
  Requests all item-information flags.
- [static var requestIconAndKind: LSRequestedInfo](./lsrequestedinfo/api-1447945-requesticonandkind.md)
  Not used.
- [static var requestExtensionFlagsOnly: LSRequestedInfo](./lsrequestedinfo/api-1445164-requestextensionflagsonly.md)
  Requests only the `kLSItemInfoExtensionIsHidden` item-information flag.
- [static var requestAllInfo: LSRequestedInfo](./lsrequestedinfo/api-1447901-requestallinfo.md)
  Requests all available item information.
- [kLSRequestExtension](./lsrequestedinfo/klsrequestextension.md)
  Requests the item’s filename extension.
- [kLSRequestTypeCreator](./lsrequestedinfo/klsrequesttypecreator.md)
  Requests the item’s file type and creator signature.
- [kLSRequestBasicFlagsOnly](./lsrequestedinfo/klsrequestbasicflagsonly.md)
  Requests all item-information flags that are not application-specific: that is, all except `kLSItemInfoIsNativeApp` through `kLSItemInfoAppIsScriptable`.
- [kLSRequestAppTypeFlags](./lsrequestedinfo/klsrequestapptypeflags.md)
  Requests all application-specific item-information flags: that is, `kLSItemInfoIsNativeApp` through `kLSItemInfoAppIsScriptable`.
- [kLSRequestAllFlags](./lsrequestedinfo/klsrequestallflags.md)
  Requests all item-information flags.
- [kLSRequestIconAndKind](./lsrequestedinfo/klsrequesticonandkind.md)
  Not used.
- [kLSRequestExtensionFlagsOnly](./lsrequestedinfo/klsrequestextensionflagsonly.md)
  Requests only the `kLSItemInfoExtensionIsHidden` item-information flag.
- [kLSRequestAllInfo](./lsrequestedinfo/klsrequestallinfo.md)
  Requests all available item information.

## Relationships

### Conforms To
- [OptionSet](../Swift/optionset.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lsrequestedinfo)*