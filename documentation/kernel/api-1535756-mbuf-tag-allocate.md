# mbuf_tag_allocate

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_tag_allocate(mbuf_t mbuf, mbuf_tag_id_t module_id, mbuf_tag_type_t type, size_t length, mbuf_how_t how, void **data_p);
```

#### Return_value

0 upon success otherwise the errno error.

#### Discussion

Allocate an mbuf tag. Mbuf tags allow various portions of the stack to tag mbufs with data that will travel with the mbuf through the stack.

Tags may only be added to mbufs with packet headers (MBUF_PKTHDR flag is set). Mbuf tags are freed when the mbuf is freed or when mbuf_tag_free is called.

## Parameters

- `mbuf`: The mbuf to attach this tag to.
- `module_id`: A module identifier returned by mbuf_tag_id_find.
- `type`: A 16 bit type value. For a given module_id, you can use a number of different tag types.
- `length`: The length, in bytes, to allocate for storage that will be associated with this tag on this mbuf.
- `how`: Indicate whether you want to block and wait for memory if memory is not immediately available.
- `data_p`: Upon successful return, *data_p will point to the buffer allocated for the mtag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535756-mbuf_tag_allocate)*