# upl_abort_range

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.1+

## Declaration

```c
kern_return_t upl_abort_range(upl_t upl_object, upl_offset_t offset, upl_size_t size, integer_t abort_cond, boolean_t *empty);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1538505-upl_abort_range)*