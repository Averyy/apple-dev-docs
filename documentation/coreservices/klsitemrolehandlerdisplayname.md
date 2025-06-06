# kLSItemRoleHandlerDisplayName

**Framework**: Core Services  
**Kind**: data

The display name of the application that is set to handle this item, subject to the role mask.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10

## Declaration

```swift
let kLSItemRoleHandlerDisplayName: CFString!
```

#### Discussion

Instead of using this constant, resolve the desired role handler for the file, then use the URL resource property [`kCFURLLocalizedNameKey`](https://developer.apple.com/documentation/corefoundation/kcfurllocalizednamekey)/[`localizedNameKey`](https://developer.apple.com/documentation/foundation/urlresourcekey/localizednamekey) on the role handler's URL.

## See Also

- [let kLSItemContentType: CFString!](klsitemcontenttype.md)
  The item’s content type identifier, which is a uniform type identifier string.
- [let kLSItemFileType: CFString!](klsitemfiletype.md)
  The item’s file type.
- [let kLSItemFileCreator: CFString!](klsitemfilecreator.md)
  The item’s file creator.
- [let kLSItemExtension: CFString!](klsitemextension.md)
  The item’s filename extension.
- [let kLSItemDisplayName: CFString!](klsitemdisplayname.md)
  The item’s name to display to the user. The display name reflects localization and extension hiding that may be in effect.
- [let kLSItemDisplayKind: CFString!](klsitemdisplaykind.md)
  The localized kind string that describes the item’s type.
- [let kLSItemIsInvisible: CFString!](klsitemisinvisible.md)
  A Boolean value that indicates the item is hidden from users.
- [let kLSItemExtensionIsHidden: CFString!](klsitemextensionishidden.md)
  A Boolean value that indicates the item’s extension is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/klsitemrolehandlerdisplayname)*