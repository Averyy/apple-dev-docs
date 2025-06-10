# setLength

**Framework**: Kernel  
**Kind**: instm

Sets the length of the data in the buffer.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual void setLength(vm_size_t length);
```

#### Discussion

At creation time, the system sets the buffer’s length to its capacity. Use this method to indicate that there are fewer bytes in the buffer than the total overall capacity. For example, you might set the length to minimize the amount of data you transfer. This method doesn’t change the total capacity of the buffer. Changing the length of a buffer allows you to reuse a buffer for multiple transfers of different lengths. 

## Parameters

- `length`: The new length of the buffer. This value must be less than or equal to the capacity of the buffer. 

## See Also

- [- getCapacity](iobuffermemorydescriptor/1574844-getcapacity.md)
  Returns the number of bytes the buffer is capable of holding. 
- [- setDirection](iobuffermemorydescriptor/1574826-setdirection.md)
  Changes the direction associated with the buffer’s memory transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/1574850-setlength)*