# os_signpost_id_make_with_pointer

**Framework**: os  
**Kind**: func  
**Role**: Function

Creates a signpost identifier that’s unique among signposts logging to the specified log, using a pointer value to generate the unique value.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```c
extern os_signpost_id_t os_signpost_id_make_with_pointer(os_log_t log, const void *ptr);
```

#### Discussion

Don’t use this function if the activity needs to cross process boundaries.

## See Also

### Creating a Signpost Identifier
- [os_signpost_id_generate](./os_signpost_id_generate.md)
  Creates a signpost identifier that’s unique among signposts logged to a specified log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_signpost_id_make_with_pointer)*