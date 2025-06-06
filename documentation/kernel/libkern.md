# libkern

**Framework**: Kernel

Access the runtime support and base classes of the kernel library.

## Topics

### Fundamentals
- [Data Types](libkern/data_types.md)
  Create strings, numbers, collections, data objects, and the other standard types employed by drivers and kernel extensions.
- [Atomic Operations](libkern/atomic_operations.md)
  Increment and decrement numbers, perform compare-and-swap operations, and manipulate other data atomically. 
- [Byte Order Utilities](libkern/byte_order_utilities.md)
  Convert values between big-endian and little-endian formats. 
### Memory
- [OSMalloc](1398447-osmalloc.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](osmalloctag.md).
- [OSMalloc_Tagalloc](1398437-osmalloc_tagalloc.md)
  Creates a tag for use with OSMalloc functions.
- [OSMalloc_Tagfree](1398439-osmalloc_tagfree.md)
  Frees a tag used with OSMalloc functions.
- [OSMalloc_noblock](1398431-osmalloc_noblock.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](osmalloctag.md), returning `NULL` if it would block.
- [OSMalloc_nowait](1398445-osmalloc_nowait.md)
  Equivalent to [`OSMalloc_noblock`](1398431-osmalloc_noblock.md).
- [OSFree](1398441-osfree.md)
  Frees a block of memory allocated by [`OSMalloc`](1398447-osmalloc.md).
- [bzero](1579350-bzero.md)
- [bzero_phys](1593364-bzero_phys.md)
### Compression
- [deflate](1546831-deflate.md)
- [deflateBound](1546926-deflatebound.md)
- [deflateCopy](1546888-deflatecopy.md)
- [deflateEnd](1546858-deflateend.md)
- [deflateInit2_](1546915-deflateinit2.md)
- [deflateInit_](1546868-deflateinit.md)
- [deflateParams](1546901-deflateparams.md)
- [deflatePrime](1546857-deflateprime.md)
- [deflateReset](1546922-deflatereset.md)
- [deflateSetDictionary](1546824-deflatesetdictionary.md)
- [deflateSetHeader](1546907-deflatesetheader.md)
- [deflateTune](1546910-deflatetune.md)
- [inflate](1546920-inflate.md)
- [inflateBack](1546870-inflateback.md)
- [inflateBackEnd](1546827-inflatebackend.md)
- [inflateBackInit_](1546837-inflatebackinit.md)
- [inflateCopy](1546896-inflatecopy.md)
- [inflateEnd](1546948-inflateend.md)
- [inflateGetHeader](1546846-inflategetheader.md)
- [inflateInit2_](1546903-inflateinit2.md)
- [inflateInit_](1546829-inflateinit.md)
- [inflatePrime](1546947-inflateprime.md)
- [inflateReset](1546911-inflatereset.md)
- [inflateSetDictionary](1546878-inflatesetdictionary.md)
- [inflateSync](1546882-inflatesync.md)
- [inflateSyncPoint](1546820-inflatesyncpoint.md)
- [compress](1546928-compress.md)
- [compress2](1546887-compress2.md)
- [compressBound](1546819-compressbound.md)
- [adler32](1546941-adler32.md)
- [adler32_combine](1546886-adler32_combine.md)
### Cryptography
- [MD5_CTX](md5_ctx.md)
- [MD5Final](1537348-md5final.md)
- [MD5Init](1537346-md5init.md)
- [MD5Update](1537352-md5update.md)
### Non Quad Routines
- [fls](2869617-fls.md)
- [flsll](2869614-flsll.md)
- [ffs](1441046-ffs.md)
- [ffsll](2869615-ffsll.md)
### copyio
- [copyin](1441036-copyin.md)
- [copyinstr](1441071-copyinstr.md)
- [copyout](1441088-copyout.md)
- [copyoutstr](1441047-copyoutstr.md)
- [copystr](1441079-copystr.md)

## See Also

- [IOKit Fundamentals](iokit_fundamentals.md)
  Implement a driver for your custom hardware using a third-party kernel extension. 
- [Hardware Families](hardware_families.md)
  Add support for specific hardware protocols such as USB, and for standard network, serial, audio, and graphics interfaces. 
- [Driver Support](driver_support.md)
  Explore the device registry and access power-management utilities and other shared driver features. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/libkern)*