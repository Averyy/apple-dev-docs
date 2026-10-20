# cdevsw_add_with_bdev

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```c
int cdevsw_add_with_bdev(int index, const struct cdevsw *csw, int bdev);
```

## See Also

### Block Device
- [bdevsw_add](./api-1457957-bdevsw_add.md)
- [bdevsw_isfree](./api-1457925-bdevsw_isfree.md)
- [bdevsw_remove](./api-1457943-bdevsw_remove.md)
- [cdevsw_add](./api-1457951-cdevsw_add.md)
- [cdevsw_isfree](./api-1457965-cdevsw_isfree.md)
- [cdevsw_remove](./api-1458013-cdevsw_remove.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1458015-cdevsw_add_with_bdev)*