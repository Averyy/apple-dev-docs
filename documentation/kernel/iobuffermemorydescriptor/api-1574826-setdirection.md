# setDirection

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Changes the direction associated with the buffer’s memory transfers.

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual void setDirection(IODirection direction);
```

## Parameters

- `direction`: The new direction of transfers. 

## See Also

### Configuring the Descriptor
- [- getCapacity](./api-1574844-getcapacity.md)
  Returns the number of bytes the buffer is capable of holding. 
- [- setLength](./api-1574850-setlength.md)
  Sets the length of the data in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/1574826-setdirection)*