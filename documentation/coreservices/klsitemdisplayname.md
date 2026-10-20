# kLSItemDisplayName

**Framework**: Core Services  
**Kind**: data  
**Role**: Global Variable

The item’s name to display to the user. The display name reflects localization and extension hiding that may be in effect.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10

## Declaration

```swift
let kLSItemDisplayName: CFString!
```

```c
const CFStringRef kLSItemDisplayName;
```

#### Discussion

Use [`LSCopyDisplayNameForURL(_:_:)`](./api-1446850-lscopydisplaynameforurl.md) or the URL resource property [`kCFURLLocalizedNameKey`](../CoreFoundation/kcfurllocalizednamekey.md)/[`localizedNameKey`](../Foundation/urlresourcekey/localizednamekey.md) instead.

## See Also

### Deprecated Constants
- [let kLSItemContentType: CFString!](./klsitemcontenttype.md)
  The item’s content type identifier, which is a uniform type identifier string.
- [let kLSItemFileType: CFString!](./klsitemfiletype.md)
  The item’s file type.
- [let kLSItemFileCreator: CFString!](./klsitemfilecreator.md)
  The item’s file creator.
- [let kLSItemExtension: CFString!](./klsitemextension.md)
  The item’s filename extension.
- [let kLSItemDisplayKind: CFString!](./klsitemdisplaykind.md)
  The localized kind string that describes the item’s type.
- [let kLSItemRoleHandlerDisplayName: CFString!](./klsitemrolehandlerdisplayname.md)
  The display name of the application that is set to handle this item, subject to the role mask.
- [let kLSItemIsInvisible: CFString!](./klsitemisinvisible.md)
  A Boolean value that indicates the item is hidden from users.
- [let kLSItemExtensionIsHidden: CFString!](./klsitemextensionishidden.md)
  A Boolean value that indicates the item’s extension is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/klsitemdisplayname)*