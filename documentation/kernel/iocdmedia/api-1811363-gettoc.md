# getTOC

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual CDTOC * getTOC();
```

#### Return_value

Returns a pointer to the TOC buffer (do not deallocate).

#### Overview

Get the full Table Of Contents.

All CDTOC fields passed across I/O Kit APIs are guaranteed to be binary-encoded (no BCD-encoded numbers are ever passed).

## See Also

- [getSpeed](iocdmedia/1811353-getspeed.md)
- [read](iocdmedia/1811376-read.md)
- [readCD()](iocdmedia/1811386-readcd.md)
- [readCD()](iocdmedia/1811393-readcd.md)
- [readDiscInfo](iocdmedia/1811402-readdiscinfo.md)
- [readISRC](iocdmedia/1811412-readisrc.md)
- [readMCN](iocdmedia/1811424-readmcn.md)
- [readTOC](iocdmedia/1811431-readtoc.md)
- [readTrackInfo](iocdmedia/1811438-readtrackinfo.md)
- [setSpeed](iocdmedia/1811448-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1811363-gettoc)*