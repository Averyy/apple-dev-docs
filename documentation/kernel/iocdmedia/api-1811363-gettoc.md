# getTOC

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual CDTOC * getTOC();
```

#### Return Value

Returns a pointer to the TOC buffer (do not deallocate).

#### Overview

Get the full Table Of Contents.

All CDTOC fields passed across I/O Kit APIs are guaranteed to be binary-encoded (no BCD-encoded numbers are ever passed).

## See Also

### Miscellaneous
- [getSpeed](./api-1811353-getspeed.md)
- [read](./api-1811376-read.md)
- [readCD()](./api-1811386-readcd.md)
- [readCD()](./api-1811393-readcd.md)
- [readDiscInfo](./api-1811402-readdiscinfo.md)
- [readISRC](./api-1811412-readisrc.md)
- [readMCN](./api-1811424-readmcn.md)
- [readTOC](./api-1811431-readtoc.md)
- [readTrackInfo](./api-1811438-readtrackinfo.md)
- [setSpeed](./api-1811448-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1811363-gettoc)*