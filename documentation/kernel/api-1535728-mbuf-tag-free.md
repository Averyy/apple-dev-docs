# mbuf_tag_free

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
void mbuf_tag_free(mbuf_t mbuf, mbuf_tag_id_t module_id, mbuf_tag_type_t type);
```

#### Discussion

Frees a previously allocated mbuf tag.

## Parameters

- `mbuf`: The mbuf the tag was allocated on.
- `module_id`: The ID of the tag to free.
- `type`: The type of the tag to free.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535728-mbuf_tag_free)*