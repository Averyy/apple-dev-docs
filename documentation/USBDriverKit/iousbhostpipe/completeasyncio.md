# CompleteAsyncIO

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Handles the completion of an asynchronous I/O request.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual void CompleteAsyncIO(OSAction *action, IOReturn status, uint32_t actualByteCount, uint64_t completionTimestamp);
```

#### Discussion

Implement a custom version of this method and use the [`TYPE`](../../DriverKit/type.md) macro to let the system know that your method conforms to this prototype.

## Parameters

- `action`: A pointer to the [`OSAction`](../../DriverKit/osaction.md) object of the request.
- `status`: The result of the operation.
- `actualByteCount`: The number of bytes that the operation actually transferred.
- `completionTimestamp`: The absolute time that the transfer completed.

## See Also

### Interacting with Bulk and Interrupt Endpoints
- [IO](./io.md)
  Performs a synchronous request on a bulk or interrupt endpoint.
- [AsyncIO](./asyncio.md)
  Enqueues an asynchronous request on a bulk or interrupt endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/completeasyncio)*