# Cancel

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Cancels the execution of the action's callbacks. 

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```c
kern_return_t Cancel(OSActionCancelHandler handler);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md). 

#### Discussion

After cancellation, you can only free the action object. You cannot reactivate it. 

## Parameters

- `handler`: A handler block for the system to call after any in-flight callbacks finish executing. 

## See Also

### Ending the Action Early
- [- Aborted](../../DriverKit/osaction/aborted.md)
  Calls the abort handler of the action object. 
- [OSActionAbortedHandler](../../DriverKit/osactionabortedhandler.md)
  The block to call before aborting an action object.
- [OSActionCancelHandler](../../DriverKit/osactioncancelhandler.md)
  The block to call after the successful cancellation of the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osaction/3438205-cancel)*