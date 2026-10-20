# copyinstr

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
int copyinstr(const user_addr_t uaddr, void *kaddr, size_t len, size_t *done);
```

## See Also

### copyio
- [copyin](./api-1441036-copyin.md)
- [copyout](./api-1441088-copyout.md)
- [copyoutstr](./api-1441047-copyoutstr.md)
- [copystr](./api-1441079-copystr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1441071-copyinstr)*