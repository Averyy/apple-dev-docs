# getCommand

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- DriverKit 21.0+
- macOS 10.11.4+

## Declaration

*DriverKit*

```cpp
virtual IOCommandPtr getCommand(bool blockForCommand);
```

*macOS*

```cpp
virtual OSPtr<IOCommand> getCommand(bool blockForCommand);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1560741-getcommand)*