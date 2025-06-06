# kLSItemExtension

**Framework**: Core Services  
**Kind**: data

The item’s filename extension.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10

## Declaration

```swift
let kLSItemExtension: CFString!
```

#### Discussion

Use [`CFURLCopyPathExtension(_:)`](https://developer.apple.com/documentation/corefoundation/cfurlcopypathextension(_:)) or [`pathExtension`](https://developer.apple.com/documentation/foundation/nsurl/pathextension) instead.

## See Also

- [let kLSItemContentType: CFString!](klsitemcontenttype.md)
  The item’s content type identifier, which is a uniform type identifier string.
- [let kLSItemFileType: CFString!](klsitemfiletype.md)
  The item’s file type.
- [let kLSItemFileCreator: CFString!](klsitemfilecreator.md)
  The item’s file creator.
- [let kLSItemDisplayName: CFString!](klsitemdisplayname.md)
  The item’s name to display to the user. The display name reflects localization and extension hiding that may be in effect.
- [let kLSItemDisplayKind: CFString!](klsitemdisplaykind.md)
  The localized kind string that describes the item’s type.
- [let kLSItemRoleHandlerDisplayName: CFString!](klsitemrolehandlerdisplayname.md)
  The display name of the application that is set to handle this item, subject to the role mask.
- [let kLSItemIsInvisible: CFString!](klsitemisinvisible.md)
  A Boolean value that indicates the item is hidden from users.
- [let kLSItemExtensionIsHidden: CFString!](klsitemextensionishidden.md)
  A Boolean value that indicates the item’s extension is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/klsitemextension)*