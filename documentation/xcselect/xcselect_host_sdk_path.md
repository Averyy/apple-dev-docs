# xcselect_host_sdk_path

**Framework**: xcselect  
**Kind**: func  
**Role**: Function

Returns the path to a version of the macOS SDK for building executables, libraries, and other content that run on the local Mac.

**Availability**:
- macOS 10.15+

## Declaration

```c
extern errno_t xcselect_host_sdk_path(xcselect_host_sdk_policy_t sdk_policy, char **path);
```

## Return Value

The return value is `0` if successful; otherwise, it returns `EINVAL` if the parameters are invalid or `ENOENT` if the function can’t find the SDK using the specified criteria.

## Parameters

- `path`: If successful, the path to the specified SDK version as a C string; otherwise, the value is unchanged.

  > ❗ **Important**:  If successful, this method allocates the C string from the heap and it’s your responsibility to free the string later using `free(3)`. See [Mac OS X Manual Page for free(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/free.3.html#//apple_ref/doc/man/3/free).


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcselect/xcselect_host_sdk_path)*