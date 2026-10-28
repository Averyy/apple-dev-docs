# CMAppleProfileHeader

**Framework**: Application Services  
**Kind**: union  
**Role**: Union

Defines a data structure to provide access to both version 2.x and version 1.0 profiles, as specified by the International Color Consortium.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef union CMAppleProfileHeader {
    ...
} CMAppleProfileHeader;
```

## Discussion

The ColorSync Manager defines the `CMAppleProfileHeader` structure to provide access to both version 2.x and version 1.0 profiles, as specified by the International Color Consortium. To obtain a copy of the International Color Consortium Profile Format Specification, or to get other information about the ICC, visit the ICC Web site at [http://www.color.org/](http://www.color.org/).

## Topics

### Fields
- [cm2](./api-1560290-cmappleprofileheader/api-1560384-cm2.md)
  A current profile header. For a description of the ColorSync profile header, see [`CM2Header`](./cm2header.md). 
- [cm4](./api-1560290-cmappleprofileheader/api-1560107-cm4.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560290-cmappleprofileheader)*