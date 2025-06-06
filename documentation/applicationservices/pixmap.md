# PixMap

**Framework**: Application Services  
**Kind**: struct

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct PixMap
```

## Topics

### Initializers
- [init()](pixmap/1464317-init.md)
- [init(baseAddr: Ptr!, rowBytes: Int16, bounds: Rect, pmVersion: Int16, packType: Int16, packSize: Int32, hRes: Fixed, vRes: Fixed, pixelType: Int16, pixelSize: Int16, cmpCount: Int16, cmpSize: Int16, pixelFormat: OSType, pmTable: CTabHandle!, pmExt: UnsafeMutableRawPointer!)](pixmap/1461182-init.md)
### Instance Properties
- [var baseAddr: Ptr!](pixmap/1459096-baseaddr.md)
  For an onscreen pixel image, a pointer to the first byte of the image. For optimal performance, this should be a multiple of 4. The `baseAddr` field of the `PixMap` record for an offscreen graphics world contains a handle instead of a pointer. Your application should never directly access the `baseAddr` field of the `PixMap` record for an offscreen graphics world.
- [var bounds: Rect](pixmap/1460186-bounds.md)
  The boundary rectangle, which links the local coordinate system of a graphics port to QuickDraw's global coordinate system and defines the area of the bit image into which QuickDraw can draw. By default, the boundary rectangle is the entire main screen. Do not use the `value` of this field to determine the size of the screen; instead use the `value` of the `gdRect` field of the [`GDevice`](gdevice.md) structure for the screen.
- [var cmpCount: Int16](pixmap/1459843-cmpcount.md)
  The number of components used to represent a color for a pixel. With indexed pixels, each pixel is a single value representing an index in a color table, and therefore this field contains the value 1; the index is the single component. With direct pixels, each pixel contains three components (one integer each for the intensities of red, green, and blue) so this field contains the value 3.
- [var cmpSize: Int16](pixmap/1464685-cmpsize.md)
  The size in bits of each component for a pixel.
- [var hRes: Fixed](pixmap/1459752-hres.md)
  The horizontal resolution of the pixel image in pixels per inch. By default, this value is 0x00480000 (for 72 pixels per inch).
- [var packSize: Int32](pixmap/1463449-packsize.md)
  The size of the packed image in bytes. When the `packType` field contains the `value` 0, this field is always set to 0.
- [var packType: Int16](pixmap/1459316-packtype.md)
  The packing algorithm used to compress image data. Color QuickDraw currently supports a `packType` of 0, which means no packing, and values of 1 to 4 for packing direct pixels.
- [var pixelFormat: OSType](pixmap/1459241-pixelformat.md)
  The way the pixels are arranged; see `k4444YpCbCrA8PixelFormat`.
- [var pixelSize: Int16](pixmap/1460391-pixelsize.md)
  The number of bits used to represent a pixel. Indexed pixels can have sizes of 1, 2, 4, and 8 bits; direct pixel sizes are 16 and 32 bits.
- [var pixelType: Int16](pixmap/1463694-pixeltype.md)
  The storage format for a pixel image. Indexed pixels are indicated by a value of 0. Direct pixels are specified by a value of `RGBDirect`, or 16. In the `PixMap` record of the [`GDevice`](gdevice.md) structure for a direct device, this field is set to `RGBDirect` when the screen depth is set.
- [var pmExt: UnsafeMutableRawPointer!](pixmap/1462255-pmext.md)
  `Handle` to a PixMapExtension structure. Set to `NIL` if there is no extension.
- [var pmTable: CTabHandle!](pixmap/1459634-pmtable.md)
  Color map for this structure.
- [var pmVersion: Int16](pixmap/1460848-pmversion.md)
  The version number of Color QuickDraw that created this `PixMap` structure. The value of `pmVersion` is normally 0. If `pmVersion` is 4, Color QuickDraw treats the `PixMap` record's `baseAddr` field as 32-bit clean. All other flags are private. Most applications never need to set this field
- [var rowBytes: Int16](pixmap/1462797-rowbytes.md)
  The offset in bytes from one row of the image to the next. The value must be even, less than 0x4000, and for best performance it should be a multiple of 4. The high 2 bits of `rowBytes` are used as flags. If bit 15 =1, the data structure pointed to is a `PixMap` structure; otherwise it is a [`BitMap`](bitmap.md) structure.
- [var vRes: Fixed](pixmap/1459423-vres.md)
  The vertical resolution of the pixel image in pixels per inch. By default, this value is 0x00480000 (for 72 pixels per inch).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pixmap)*