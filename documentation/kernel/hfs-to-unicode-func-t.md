# hfs_to_unicode_func_t

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.12+

## Declaration

```swift
typedef int (*hfs_to_unicode_func_t)(const uint8_t hfs_str[32], uint16_t *uni_str, u_int32_t maxCharLen, u_int32_t *usedCharLen);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/hfs_to_unicode_func_t)*