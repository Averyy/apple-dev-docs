# PMRetain(_:)

**Framework**: Application Services  
**Kind**: func

Retains a printing object by incrementing its reference count.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMRetain(_ object: PMObject?) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

You should retain a printing object when you receive it from elsewhere (that is, you did not create or copy it) and you want it to persist. If you retain a printing object, you are responsible for releasing it. (See `PMRelease`.) You can use the function `PMRetain` to increment a printing object’s reference count so that multiple threads or routines can use the object without the risk of another thread or routine deallocating the object.

## Parameters

- `object`: The printing object you want to retain.

## See Also

- [func PMRelease(PMObject?) -> OSStatus](1461402-pmrelease.md)
  Releases a printing object by decrementing its reference count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460190-pmretain)*