# userType

**Framework**: Core Services  
**Kind**: structp

A 4-byte field that can contain application-specific data. When an alias record is created, this field contains 0. Your application can use this field for its own purposes.

## See Also

### Fields
- [aliasSize](./api-1805882-aliassize.md)
  The size, in bytes, assigned to the alias record at the time of its creation or updating. This is the total size of the record, including the `userType` and `aliasSize` fields, as well as the variable-length data that is private to the Alias Manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aliasrecord/1805870-usertype)*