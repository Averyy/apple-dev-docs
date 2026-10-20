# gatedGetCommand

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- DriverKit 21.0+
- macOS 10.11.4+

## Declaration

*DriverKit*

```cpp
virtual kern_return_t gatedGetCommand(IOCommand **command, bool blockForCommand);
```

*macOS*

```cpp
virtual IOReturn gatedGetCommand(IOCommand **command, bool blockForCommand);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1560742-gatedgetcommand)*