# withCapacity

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

**Availability**:
- DriverKit 21.0+
- macOS 12.0+

## Declaration

*DriverKit*

```c
static OSOrderedSetPtr withCapacity(uint32_t capacity, OSOrderBlock orderBlock);
```

*macOS*

```c
static OSPtr<OSOrderedSet> withCapacity(unsigned int capacity, OSOrderBlock orderBlock);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osorderedset/3753632-withcapacity)*