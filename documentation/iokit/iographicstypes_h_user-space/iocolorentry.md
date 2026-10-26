# IOColorEntry

**Framework**: IOKit  
**Kind**: tag

A structure defining one entry of a color lookup table.

## Declaration

```c
struct IOColorEntry {
   UInt16 index;
   IOColorComponent red;
   IOColorComponent green;
   IOColorComponent blue;
};
```

#### Overview

This structure is used by IOFramebuffer to define an entry of a color lookup table.

## Topics

### Fields
- [index](../iocolorentry/api-1505706-index.md)
  Number of pixels visible per row.
- [red](../iocolorentry/api-1505899-red.md)
  Value of red component 0-65535.
- [green](../iocolorentry/api-1505128-green.md)
  Value of green component 0-65535.
- [blue](../iocolorentry/api-1505830-blue.md)
  Value of blue component 0-65535.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iographicstypes_h_user-space/iocolorentry)*