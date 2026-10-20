# OSAction

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.15+

## Declaration

```cpp
class OSAction : OSObject, OSActionInterface
```

## Topics

### Instance Methods
- [- Aborted](./osaction/api-3366002-aborted.md)
- [- Aborted_Impl](./osaction/api-3366003-aborted_impl.md)
- [- Cancel](./osaction/api-3438205-cancel.md)
  Cancels the execution of the action's callbacks. 
- [- Dispatch](./osaction/api-3223366-dispatch.md)
- [- EndWait](./osaction/api-3538555-endwait.md)
- [- GetReference](./osaction/api-3438207-getreference.md)
  Returns a pointer to any additional memory allocated by the action object on your behalf.
- [- SetAbortedHandler](./osaction/api-3438208-setabortedhandler.md)
  Install a handler for the system to call when no other processes reference the action object.
- [- Wait](./osaction/api-3538556-wait.md)
- [- WillWait](./osaction/api-3538557-willwait.md)
- [- free](./osaction/api-3438209-free.md)
  Performs any final cleanup for the action object.
- [- getMetaClass](./osaction/api-3223369-getmetaclass.md)
### Type Methods
- [+ Aborted_Invoke](./osaction/api-3366004-aborted_invoke.md)
- [+ Create](./osaction/api-3438206-create.md)
  Creates a new action object and configures it with your custom target object and callback method. 
- [+ CreateWithTypeName](./osaction/api-3567113-createwithtypename.md)
- [+ CreateWithTypeName_Call](./osaction/api-3567114-createwithtypename_call.md)
- [+ CreateWithTypeName_Impl](./osaction/api-3567115-createwithtypename_impl.md)
- [+ CreateWithTypeName_Invoke](./osaction/api-3567116-createwithtypename_invoke.md)
- [+ Create_Call](./osaction/api-3223363-create_call.md)
- [+ Create_Impl](./osaction/api-3223364-create_impl.md)
- [+ Create_Invoke](./osaction/api-3223365-create_invoke.md)

## Relationships

### Inherits From
- [OSActionInterface](./osactioninterface.md)
- [OSObject](./osobject.md)

## See Also

### Actions
- [OSActionInterface](./osactioninterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osaction)*