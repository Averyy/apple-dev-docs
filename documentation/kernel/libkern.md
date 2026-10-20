# libkern

**Framework**: Kernel  
**Role**: API Collection

Access the runtime support and base classes of the kernel library.

## Topics

### Fundamentals
- [Data Types](./libkern/data_types.md)
  Create strings, numbers, collections, data objects, and the other standard types employed by drivers and kernel extensions.
- [Atomic Operations](./libkern/atomic_operations.md)
  Increment and decrement numbers, perform compare-and-swap operations, and manipulate other data atomically. 
- [Byte Order Utilities](./libkern/byte_order_utilities.md)
  Convert values between big-endian and little-endian formats. 
### Memory
- [OSMalloc](./api-1398447-osmalloc.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](./osmalloctag.md).
- [OSMalloc_Tagalloc](./api-1398437-osmalloc_tagalloc.md)
  Creates a tag for use with OSMalloc functions.
- [OSMalloc_Tagfree](./api-1398439-osmalloc_tagfree.md)
  Frees a tag used with OSMalloc functions.
- [OSMalloc_noblock](./api-1398431-osmalloc_noblock.md)
  Allocates a block of memory associated with a given [`OSMallocTag`](./osmalloctag.md), returning `NULL` if it would block.
- [OSMalloc_nowait](./api-1398445-osmalloc_nowait.md)
  Equivalent to [`OSMalloc_noblock`](./api-1398431-osmalloc_noblock.md).
- [OSFree](./api-1398441-osfree.md)
  Frees a block of memory allocated by [`OSMalloc`](./api-1398447-osmalloc.md).
- [bzero](./api-1579350-bzero.md)
- [bzero_phys](./api-1593364-bzero_phys.md)
### Compression
- [deflate](./api-1546831-deflate.md)
- [deflateBound](./api-1546926-deflatebound.md)
- [deflateCopy](./api-1546888-deflatecopy.md)
- [deflateEnd](./api-1546858-deflateend.md)
- [deflateInit2_](./api-1546915-deflateinit2.md)
- [deflateInit_](./api-1546868-deflateinit.md)
- [deflateParams](./api-1546901-deflateparams.md)
- [deflatePrime](./api-1546857-deflateprime.md)
- [deflateReset](./api-1546922-deflatereset.md)
- [deflateSetDictionary](./api-1546824-deflatesetdictionary.md)
- [deflateSetHeader](./api-1546907-deflatesetheader.md)
- [deflateTune](./api-1546910-deflatetune.md)
- [inflate](./api-1546920-inflate.md)
- [inflateBack](./api-1546870-inflateback.md)
- [inflateBackEnd](./api-1546827-inflatebackend.md)
- [inflateBackInit_](./api-1546837-inflatebackinit.md)
- [inflateCopy](./api-1546896-inflatecopy.md)
- [inflateEnd](./api-1546948-inflateend.md)
- [inflateGetHeader](./api-1546846-inflategetheader.md)
- [inflateInit2_](./api-1546903-inflateinit2.md)
- [inflateInit_](./api-1546829-inflateinit.md)
- [inflatePrime](./api-1546947-inflateprime.md)
- [inflateReset](./api-1546911-inflatereset.md)
- [inflateSetDictionary](./api-1546878-inflatesetdictionary.md)
- [inflateSync](./api-1546882-inflatesync.md)
- [inflateSyncPoint](./api-1546820-inflatesyncpoint.md)
- [compress](./api-1546928-compress.md)
- [compress2](./api-1546887-compress2.md)
- [compressBound](./api-1546819-compressbound.md)
- [adler32](./api-1546941-adler32.md)
- [adler32_combine](./api-1546886-adler32_combine.md)
### Cryptography
- [MD5_CTX](./md5_ctx.md)
- [MD5Final](./api-1537348-md5final.md)
- [MD5Init](./api-1537346-md5init.md)
- [MD5Update](./api-1537352-md5update.md)
### Non Quad Routines
- [fls](./api-2869617-fls.md)
- [flsll](./api-2869614-flsll.md)
- [ffs](./api-1441046-ffs.md)
- [ffsll](./api-2869615-ffsll.md)
### copyio
- [copyin](./api-1441036-copyin.md)
- [copyinstr](./api-1441071-copyinstr.md)
- [copyout](./api-1441088-copyout.md)
- [copyoutstr](./api-1441047-copyoutstr.md)
- [copystr](./api-1441079-copystr.md)

## See Also

### IOKit Drivers
- [IOKit Fundamentals](./iokit_fundamentals.md)
  Implement a driver for your custom hardware using a third-party kernel extension. 
- [Hardware Families](./hardware_families.md)
  Add support for specific hardware protocols such as USB, and for standard network, serial, audio, and graphics interfaces. 
- [Driver Support](./driver_support.md)
  Explore the device registry and access power-management utilities and other shared driver features. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/libkern)*