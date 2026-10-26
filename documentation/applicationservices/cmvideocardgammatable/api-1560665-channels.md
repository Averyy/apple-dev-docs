# channels

**Framework**: Application Services  
**Kind**: structp  
**Role**: Instance Property

Number of gamma channels (1 or 3). If `channels` is set to 1 then the red, green, and blue lookup tables (LUTs) of the video card will be loaded with the same data. If `channels` is set to 3, then if the video card supports separate red, green, and blue LUTs, then the video card LUTs will be loaded with the data for the three channels from the `data` array.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
UInt16 channels;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmvideocardgammatable/1560665-channels)*