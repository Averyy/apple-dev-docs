# CSBackupSetItemExcluded(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Includes or excludes an item from the backup.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CSBackupSetItemExcluded(_ item: CFURL!, _ exclude: Bool, _ excludeByPath: Bool) -> OSStatus
```

#### Return_value

A result code. Returns `noErr` if the item was successfully included or excluded from the backup.

#### Discussion

Backup skips files and folders marked for exclusion. If a folder is marked for exclusion, the folder and all its contents are excluded from the backup process. You can exclude specific paths that do not exist yet, but that you plan to create later, by passing the planned URL in `item` and passing `true` in `excludeByPath`. Note that if you pass `false` in `excludeByPath`, the URL must already exist. 

Your application can allow users to change the backup exclusion status of any file or folder to which it has write access. To change the backup exclusion status of a path, your application must be running with administrator privileges. 

## Parameters

- `item`: The URL of the file or folder to be included or excluded from the backup.
- `exclude`: Pass   to exclude this item from backup (Backup will not back up this item). Pass   to stop excluding this item (Backup will back up this item if the user so chooses).
- `excludeByPath`: Pass   to indicate that this item is excluded because of its location (its absolute path). Pass   to indicate that this item is excluded regardless of its location (and regardless of whether the user moves the item).

## See Also

- [func CSBackupIsItemExcluded(CFURL!, UnsafeMutablePointer<DarwinBoolean>!) -> Bool](1443602-csbackupisitemexcluded.md)
  Returns a Boolean value indicating whether an item is currently excluded from the backup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445043-csbackupsetitemexcluded)*