# CSBackupIsItemExcluded(_:_:)

**Framework**: Core Services  
**Kind**: func

Returns a Boolean value indicating whether an item is currently excluded from the backup.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CSBackupIsItemExcluded(_ item: CFURL!, _ excludeByPath: UnsafeMutablePointer<DarwinBoolean>!) -> Bool
```

#### Return_value

`true` if the item or any of its ancestors are currently excluded from backup, `false` otherwise.

## Parameters

- `item`: The URL of the item.
- `excludeByPath`: If `true`, the item’s backup exclusion status applies to its location; if `false`, the item's backup exclusion status applies to itself, regardless of its location. See [`CSBackupSetItemExcluded(_:_:_:)`](1445043-csbackupsetitemexcluded.md) for more information. Can be `NULL`.

## See Also

- [func CSBackupSetItemExcluded(CFURL!, Bool, Bool) -> OSStatus](1445043-csbackupsetitemexcluded.md)
  Includes or excludes an item from the backup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1443602-csbackupisitemexcluded)*