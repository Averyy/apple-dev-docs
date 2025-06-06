# backtrace_unpack

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 12.3+

## Declaration

```swift
unsigned int backtrace_unpack(backtrace_pack_t packing, uintptr_t *dst, unsigned int dst_len, const uint8_t *src, size_t src_size);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3917661-backtrace_unpack)*