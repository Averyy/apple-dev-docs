# MDItemCreateWithURL(_:_:)

**Framework**: Core Services  
**Kind**: func

Creates an MDItem object for a file at the specified file URL.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func MDItemCreateWithURL(_ allocator: CFAllocator!, _ url: CFURL!) -> MDItem!
```

#### Return_value

An `MDItem` object or `NULL` if there was a problem creating the object. 

#### Discussion

Returns a metadata item for the given URL.

##### 1675371

In macOS 10.5 and later MDItemRefs may or may not be uniqued. You should always use `CFEqual` for comparison. 

Prior to OS X v 10.5 items were guaranteed to be unique and == could or `CFEqual` could be used for the comparison.

## Parameters

- `allocator`: The   object to be used to allocate memory for the new object. Pass   or   to use the current default allocator.
- `url`: A file URL to the file from which to create the  . The file must exist.

## See Also

- [func MDItemCreate(CFAllocator!, CFString!) -> MDItem!](1426917-mditemcreate.md)
  Creates an MDItem object for a file at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1427034-mditemcreatewithurl)*