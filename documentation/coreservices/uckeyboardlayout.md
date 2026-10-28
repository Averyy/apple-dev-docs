# UCKeyboardLayout

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Provides header data for a `'uchr'` resource.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct UCKeyboardLayout
```

```c
typedef struct UCKeyboardLayout {
    ...
} UCKeyboardLayout;
```

## Overview

The Unicode keyboard-layout ( `'uchr'`) resource contains the data necessary to map virtual key codes to Unicode character codes for a given keyboard layout. The `'uchr'` format consists of a header information section and five key mapping data sections. The `UCKeyboardLayout` type is used in the `'uchr'` resource header. It specifies version and format information, offsets to the various subtables, and an array of `UCKeyboardTypeHeader` entries. 

You should use low-ASCII (0 - 0x7F) only for the KCHR/uchr resource names and you should use Unicode in the Info.plist file when you specify strings for the user-interface (UI).

## Topics

### Initializers
- [init()](./uckeyboardlayout/api-1447446-init.md)
- [init(keyLayoutHeaderFormat: UInt16, keyLayoutDataVersion: UInt16, keyLayoutFeatureInfoOffset: UInt32, keyboardTypeCount: UInt32, keyboardTypeList: UCKeyboardTypeHeader)](./uckeyboardlayout/api-1448404-init.md)
### Instance Properties
- [var keyLayoutDataVersion: UInt16](./uckeyboardlayout/api-1390626-keylayoutdataversion.md)
  An unsigned 16-bit integer identifying the version of the data in the resource, in binary code decimal format. For example, 0x0100 would equal version 1.0.
- [var keyLayoutFeatureInfoOffset: UInt32](./uckeyboardlayout/api-1390597-keylayoutfeatureinfooffset.md)
  An unsigned 32-bit integer providing an offset to a structure of type [`UCKeyLayoutFeatureInfo`](./uckeylayoutfeatureinfo.md), if such is used in the resource. May be 0 if no `UCKeyLayoutFeatureInfo` table is included in the resource.
- [var keyLayoutHeaderFormat: UInt16](./uckeyboardlayout/api-1390425-keylayoutheaderformat.md)
  An unsigned 16-bit integer identifying the format of the structure. Set to `kUCLayoutHeaderFormat`.
- [var keyboardTypeCount: UInt32](./uckeyboardlayout/api-1390448-keyboardtypecount.md)
  An unsigned 32-bit integer specifying the number of `UCKeyboardTypeHeader` structures in the `keyboardTypeList[]` field’s array.
- [var keyboardTypeList: UCKeyboardTypeHeader](./uckeyboardlayout/api-1390494-keyboardtypelist.md)
  A variable-length array containing structures of type `UCKeyboardTypeHeader`. Each `UCKeyboardTypeHeader` entry specifies a range of physical keyboard types and contains offsets to each of the key mapping sections to be used for that range of keyboard types. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeyboardlayout)*