# AliasRecord

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Defines an alias record.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct AliasRecord {
    ...
} AliasRecord;
```

## Overview

The Alias Manager uses alias records to store information that allows it to locate an object in the file system. 

## Topics

### Fields
- [userType](./aliasrecord/api-1805870-usertype.md)
  A 4-byte field that can contain application-specific data. When an alias record is created, this field contains 0. Your application can use this field for its own purposes.
- [aliasSize](./aliasrecord/api-1805882-aliassize.md)
  The size, in bytes, assigned to the alias record at the time of its creation or updating. This is the total size of the record, including the `userType` and `aliasSize` fields, as well as the variable-length data that is private to the Alias Manager.
### Instance Properties
- [hidden](./aliasrecord/api-1444289-hidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aliasrecord)*