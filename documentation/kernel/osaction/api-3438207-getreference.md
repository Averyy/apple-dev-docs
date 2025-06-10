# GetReference

**Framework**: Kernel  
**Kind**: instm

Returns a pointer to any additional memory allocated by the action object on your behalf.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
void * GetReference(void);
```

#### Return_value

A pointer to the additional storage you requested at creation time. This method returns `NULL` if you passed `0` to the `referenceSize` parameter of the [`Create`](osaction/3438206-create.md) method. It also returns `NULL` if the action object doesn't belong to the current process. 

#### Discussion

The action object zero-initializes the memory it allocates. Only the process that owns the action object may access the memory. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osaction/3438207-getreference)*