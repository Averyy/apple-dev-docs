# os_workgroup_testcancel

**Framework**: os  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the workgroup is canceled.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```c
extern bool os_workgroup_testcancel(os_workgroup_t wg);
```

## Return Value

`true` if the workgroup is canceled, or `false` if it is still active.

## Parameters

- `wg`: The workgroup you want to cancel.

## See Also

### Cancellation
- [os_workgroup_cancel](./os_workgroup_cancel.md)
  Cancels and invalidates the specified workgroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_testcancel)*