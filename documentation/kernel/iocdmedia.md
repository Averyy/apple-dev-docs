# IOCDMedia

**Framework**: Kernel  
**Kind**: cl

The IOCDMedia class is a random-access disk device abstraction for CDs.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOCDMedia : IOMedia
```

#### Overview

The IOCDMedia class is a random-access disk device abstraction for CDs. It extends the IOMedia class by implementing special CD APIs, such as readCD, and publishing the TOC as a property of the IOCDMedia object.

## Topics

### Miscellaneous
- [getSpeed](iocdmedia/1811353-getspeed.md)
- [getTOC](iocdmedia/1811363-gettoc.md)
- [read](iocdmedia/1811376-read.md)
- [readCD()](iocdmedia/1811386-readcd.md)
- [readCD()](iocdmedia/1811393-readcd.md)
- [readDiscInfo](iocdmedia/1811402-readdiscinfo.md)
- [readISRC](iocdmedia/1811412-readisrc.md)
- [readMCN](iocdmedia/1811424-readmcn.md)
- [readTOC](iocdmedia/1811431-readtoc.md)
- [readTrackInfo](iocdmedia/1811438-readtrackinfo.md)
- [setSpeed](iocdmedia/1811448-setspeed.md)
### Instance Methods
- [- getMetaClass](iocdmedia/1581382-getmetaclass.md)
- [- getProvider](iocdmedia/1581367-getprovider.md)
- [- getSpeed](iocdmedia/1581380-getspeed.md)
- [- getTOC](iocdmedia/1581374-gettoc.md)
- [- matchPropertyTable](iocdmedia/1581384-matchpropertytable.md)
- [- read](iocdmedia/1581385-read.md)
- [- readCD](iocdmedia/1581373-readcd.md)
- [- readCD](iocdmedia/3516775-readcd.md)
- [- readDiscInfo](iocdmedia/1581378-readdiscinfo.md)
- [- readISRC](iocdmedia/1581376-readisrc.md)
- [- readMCN](iocdmedia/1581379-readmcn.md)
- [- readTOC](iocdmedia/1581377-readtoc.md)
- [- readTrackInfo](iocdmedia/1581365-readtrackinfo.md)
- [- setSpeed](iocdmedia/1581370-setspeed.md)
- [- write](iocdmedia/1581366-write.md)
- [- writeCD](iocdmedia/1581375-writecd.md)
- [- writeCD](iocdmedia/3516776-writecd.md)

## Relationships

### Inherits From
- [IOMedia](iomedia.md)

## See Also

- [IOBDMedia](iobdmedia.md)
  The IOBDMedia class is a random-access disk device abstraction for BDs.
- [IOMedia](iomedia.md)
  A random-access disk device abstraction.
- [IOCDMediaBSDClient](iocdmediabsdclient.md)
- [IOCDPartitionScheme](iocdpartitionscheme.md)
- [IODVDMedia](iodvdmedia.md)
  The IODVDMedia class is a random-access disk device abstraction for DVDs.
- [IODVDMediaBSDClient](iodvdmediabsdclient.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia)*