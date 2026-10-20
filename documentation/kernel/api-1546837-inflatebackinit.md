# inflateBackInit_

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.6+

## Declaration

```c
int inflateBackInit_(z_streamp strm, int windowBits, unsigned char *window, const char *version, int stream_size);
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1546837-inflatebackinit)*