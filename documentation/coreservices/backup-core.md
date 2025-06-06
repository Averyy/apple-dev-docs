# Backup Core

**Framework**: Core Services

Access low-level details about file and folder settings used by the macOS Backup utility. 

#### Overview

Backup is a built-in, user-configurable backup solution that protects user data from accidental loss. You can use the Backup Core API  functionality to, for example, exclude temporary or otherwise unimportant folders and files created by your app from Backup, and to allow users to make backup decisions from within the context of your app.

## Topics

### Managing an Item’s Backup Exclusion Status
- [func CSBackupSetItemExcluded(CFURL!, Bool, Bool) -> OSStatus](1445043-csbackupsetitemexcluded.md)
  Includes or excludes an item from the backup.
- [func CSBackupIsItemExcluded(CFURL!, UnsafeMutablePointer<DarwinBoolean>!) -> Bool](1443602-csbackupisitemexcluded.md)
  Returns a Boolean value indicating whether an item is currently excluded from the backup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/backup_core)*