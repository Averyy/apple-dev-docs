# CMVideoCardGammaTable

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMVideoCardGammaTable {
    ...
} CMVideoCardGammaTable;
```

#### Overview

The ColorSync Manager defines the `CMVideoCardGammaTable` data structure to specify video card gamma data in table format. You specify the number of channels, the number of entries per channel, and the size of each entry. The last field in the structure is an array of size one that serves as the start of the table data. The actual size of the array is equal to the number of channels times the number of entries times the size of each entry. 

## Topics

### Instance Properties
- [channels](./cmvideocardgammatable/api-1560665-channels.md)
  Number of gamma channels (1 or 3). If `channels` is set to 1 then the red, green, and blue lookup tables (LUTs) of the video card will be loaded with the same data. If `channels` is set to 3, then if the video card supports separate red, green, and blue LUTs, then the video card LUTs will be loaded with the data for the three channels from the `data` array.
- [data](./cmvideocardgammatable/api-1560268-data.md)
  Variable-sized array of data. The size of the data is equal to `channels``*``entryCount``*``entrySize`.
- [entryCount](./cmvideocardgammatable/api-1560714-entrycount.md)
  Number of entries per channel (1-based). The number of entries must be greater than or equal to 2.
- [entrySize](./cmvideocardgammatable/api-1560361-entrysize.md)
  Size in bytes of each entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmvideocardgammatable)*