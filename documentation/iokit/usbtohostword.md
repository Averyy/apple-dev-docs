# USBToHostWord

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define USBToHostWord
```

## Discussion

The USB API's use a convention of specifying parameters in the host order. The USB spec specifies that multi-byte items should be formatted in little endian order. The following macros allow one to translate multi-byte values from Host order to USB order and vice versa. There are separate macros for in-kernel use and for user space use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usbtohostword)*