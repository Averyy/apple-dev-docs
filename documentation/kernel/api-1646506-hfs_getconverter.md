# hfs_getconverter

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.12+

## Declaration

```c
int hfs_getconverter(u_int32_t encoding, hfs_to_unicode_func_t *get_unicode, unicode_to_hfs_func_t *get_hfsname);
```

## See Also

### Encodings
- [hfs_getencodingbias](./api-1646508-hfs_getencodingbias.md)
- [hfs_pickencoding](./api-1646509-hfs_pickencoding.md)
- [hfs_relconverter](./api-1646505-hfs_relconverter.md)
- [hfs_setencodingbias](./api-1646502-hfs_setencodingbias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1646506-hfs_getconverter)*