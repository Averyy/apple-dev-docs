# UserInfo Dictionary Keys

**Framework**: UIKit

Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.

## Topics

### Constants
- [class let changedTypesAddedUserInfoKey: String](uipasteboard/changedtypesaddeduserinfokey.md)
  With the notification named [`changedNotification`](uipasteboard/changednotification.md), use this key to access the added representation types. These types are stored as an array in the notification’s `userInfo` dictionary.
- [class let changedTypesRemovedUserInfoKey: String](uipasteboard/changedtypesremoveduserinfokey.md)
  With the notification named [`changedNotification`](uipasteboard/changednotification.md), use this key to access the removed representation types. These types are stored as an array in the notification’s `userInfo` dictionary.

## See Also

- [UIPasteboard.Name](uipasteboard/name-swift.struct.md)
  Constants that identify the name of a pasteboard.
- [Pasteboard Names](pasteboard-names.md)
  Names identifying the system pasteboards.
- [UIPasteboard.OptionsKey](uipasteboard/optionskey.md)
  Options for describing pasteboard privacy.
- [Pasteboard Data Type Representations](pasteboard-data-type-representations.md)
  Pasteboard-item representation types, as for a given object value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/userinfo-dictionary-keys)*