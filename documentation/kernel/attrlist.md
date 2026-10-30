# attrlist

**Framework**: Kernel  
**Kind**: tag

A list of attributes associated with a file.

**Availability**:
- macOS 10.6+

## Declaration

```c
struct attrlist {
    ...
};
```

## Topics

### Working with List Metadata
- [bitmapcount](./attrlist/api-1555361-bitmapcount.md)
  The number of attribute bit sets in the list.
- [reserved](./attrlist/api-1555266-reserved.md)
  A reserved field used to maintain 4-byte alignment.
### Working with Attribute Groups
- [commonattr](./attrlist/api-1555342-commonattr.md)
  A group of common file attributes.
- [volattr](./attrlist/api-1555332-volattr.md)
  A group of volume attributes.
- [dirattr](./attrlist/api-1555218-dirattr.md)
  A group of directory attributes.
- [fileattr](./attrlist/api-1555275-fileattr.md)
  A group of file attributes.
- [forkattr](./attrlist/api-1555256-forkattr.md)
  A group of fork attributes.

## See Also

### Inspecting Event Properties
- [target](../EndpointSecurity/es_event_setattrlist_t/target.md)
  The source file of this event.
- [attrlist](../EndpointSecurity/es_event_setattrlist_t/attrlist.md)
  The attributes to set, such as volume, directory, file, and fork attributes.
- [reserved](../EndpointSecurity/es_event_setattrlist_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/attrlist)*