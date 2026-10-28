# os_workgroup_join

**Framework**: os  
**Kind**: func  
**Role**: Function

Adds the current thread to the specified workgroup.

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
extern int os_workgroup_join(os_workgroup_t wg, os_workgroup_join_token_t token_out);
```

## Return Value

A value of `0` on success, or a nonzero error code that indicates why the function failed. Common error codes include `EINVAL` or `EALREADY`. For example, this method returns `EALREADY` if the thread already belongs to a workgroup. It returns `EINVAL` if the workgroup is already canceled.

## Discussion

When you call this function, the current thread must not belong to any workgroup. This function adds the thread to the specified workgroup and updates the `token_out` parameter. You may call this function safely from a real-time thread of your app.

> ❗ **Important**:  Save the `token_out` parameter so that you can remove the thread from the workgroup later. When removing a thread, the thread, workgroup, and token data must match the original values you specify for this function; if they don’t, the system aborts your process.

## Parameters

- `wg`: The workgroup to join.
- `token_out`: An empty token structure. This function fills the provided structure with information about the workgroup relationship. Save this structure so you can remove the thread from the workgroup later.

## See Also

### Thread Attachment
- [os_workgroup_leave](./os_workgroup_leave.md)
  Removes the current thread from the workgroup it previously joined.
- [os_workgroup_join_token_t](./os_workgroup_join_token_t.md)
  An opaque token that represents a connection between a thread and a workgroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_join)*