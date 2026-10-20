# agdcGTraceToken

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.14.4+

## Declaration

```c
void agdcGTraceToken(const IOFramebuffer *fb, const uint16_t line, const bool useController, const uint16_t fnID, const uint8_t fnType, const uint16_t tag1, const uint64_t arg1, const uint16_t tag2, const uint64_t arg2, const uint16_t tag3, const uint64_t arg3);
```

## See Also

### Framebuffer Utilities
- [VSLDisposeInterruptService](./api-1573084-vsldisposeinterruptservice.md)
- [VSLDoInterruptService](./api-1573107-vsldointerruptservice.md)
- [VSLNewInterruptService](./api-1573117-vslnewinterruptservice.md)
- [VSLPrepareCursorForHardwareCursor](./api-1573096-vslpreparecursorforhardwarecurso.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3123025-agdcgtracetoken)*