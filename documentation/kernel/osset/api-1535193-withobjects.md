# withObjects

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

**Availability**:
- DriverKit 21.0+
- macOS 10.11.4+

## Declaration

*DriverKit*

```c
static OSSetPtr withObjects(const OSObject **values, uint32_t count, uint32_t capacity);
```

*macOS*

```c
static OSPtr<OSSet> withObjects(const OSObject *objects[], unsigned int count, unsigned int capacity);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osset/1535193-withobjects)*