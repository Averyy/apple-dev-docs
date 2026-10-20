# IOCDMedia

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

The IOCDMedia class is a random-access disk device abstraction for CDs.

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOCDMedia : IOMedia
```

#### Overview

The IOCDMedia class is a random-access disk device abstraction for CDs. It extends the IOMedia class by implementing special CD APIs, such as readCD, and publishing the TOC as a property of the IOCDMedia object.

## Topics

### Miscellaneous
- [getSpeed](./iocdmedia/api-1811353-getspeed.md)
- [getTOC](./iocdmedia/api-1811363-gettoc.md)
- [read](./iocdmedia/api-1811376-read.md)
- [readCD()](./iocdmedia/api-1811386-readcd.md)
- [readCD()](./iocdmedia/api-1811393-readcd.md)
- [readDiscInfo](./iocdmedia/api-1811402-readdiscinfo.md)
- [readISRC](./iocdmedia/api-1811412-readisrc.md)
- [readMCN](./iocdmedia/api-1811424-readmcn.md)
- [readTOC](./iocdmedia/api-1811431-readtoc.md)
- [readTrackInfo](./iocdmedia/api-1811438-readtrackinfo.md)
- [setSpeed](./iocdmedia/api-1811448-setspeed.md)
### Instance Methods
- [- getMetaClass](./iocdmedia/api-1581382-getmetaclass.md)
- [- getProvider](./iocdmedia/api-1581367-getprovider.md)
- [- getSpeed](./iocdmedia/api-1581380-getspeed.md)
- [- getTOC](./iocdmedia/api-1581374-gettoc.md)
- [- matchPropertyTable](./iocdmedia/api-1581384-matchpropertytable.md)
- [- read](./iocdmedia/api-1581385-read.md)
- [- readCD](./iocdmedia/api-1581373-readcd.md)
- [- readCD](./iocdmedia/api-3516775-readcd.md)
- [- readDiscInfo](./iocdmedia/api-1581378-readdiscinfo.md)
- [- readISRC](./iocdmedia/api-1581376-readisrc.md)
- [- readMCN](./iocdmedia/api-1581379-readmcn.md)
- [- readTOC](./iocdmedia/api-1581377-readtoc.md)
- [- readTrackInfo](./iocdmedia/api-1581365-readtrackinfo.md)
- [- setSpeed](./iocdmedia/api-1581370-setspeed.md)
- [- write](./iocdmedia/api-1581366-write.md)
- [- writeCD](./iocdmedia/api-1581375-writecd.md)
- [- writeCD](./iocdmedia/api-3516776-writecd.md)

## Relationships

### Inherits From
- [IOMedia](./iomedia.md)

## See Also

### Data Storage
- [IOBDMedia](./iobdmedia.md)
  The IOBDMedia class is a random-access disk device abstraction for BDs.
- [IOMedia](./iomedia.md)
  A random-access disk device abstraction.
- [IOCDMediaBSDClient](./iocdmediabsdclient.md)
- [IOCDPartitionScheme](./iocdpartitionscheme.md)
- [IODVDMedia](./iodvdmedia.md)
  The IODVDMedia class is a random-access disk device abstraction for DVDs.
- [IODVDMediaBSDClient](./iodvdmediabsdclient.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia)*