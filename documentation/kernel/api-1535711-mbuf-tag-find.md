# mbuf_tag_find

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_tag_find(mbuf_t mbuf, mbuf_tag_id_t module_id, mbuf_tag_type_t type, size_t *length, void **data_p);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Find the data associated with an mbuf tag.

## Parameters

- `mbuf`: The mbuf the tag is attached to.
- `module_id`: A module identifier returned by mbuf_tag_id_find.
- `type`: The 16 bit type of the tag to find.
- `length`: Upon success, the length of data will be store in *length.
- `data_p`: Upon successful return, *data_p will point to the buffer allocated for the mtag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535711-mbuf_tag_find)*