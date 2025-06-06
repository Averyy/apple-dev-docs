# OSAction

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.15+

## Declaration

```swift
class OSAction : OSObject, OSActionInterface
```

## Topics

### Instance Methods
- [- Aborted](osaction/3366002-aborted.md)
- [- Aborted_Impl](osaction/3366003-aborted_impl.md)
- [- Cancel](osaction/3438205-cancel.md)
  Cancels the execution of the action's callbacks. 
- [- Dispatch](osaction/3223366-dispatch.md)
- [- EndWait](../driverkit/osaction/endwait.md)
- [- GetReference](osaction/3438207-getreference.md)
  Returns a pointer to any additional memory allocated by the action object on your behalf.
- [- SetAbortedHandler](osaction/3438208-setabortedhandler.md)
  Install a handler for the system to call when no other processes reference the action object.
- [- Wait](../driverkit/osaction/wait.md)
- [- WillWait](../driverkit/osaction/willwait.md)
- [- free](osaction/3438209-free.md)
  Performs any final cleanup for the action object.
- [- getMetaClass](osaction/3223369-getmetaclass.md)
### Type Methods
- [+ Aborted_Invoke](osaction/3366004-aborted_invoke.md)
- [+ Create](osaction/3438206-create.md)
  Creates a new action object and configures it with your custom target object and callback method. 
- [+ CreateWithTypeName](osaction/3567113-createwithtypename.md)
- [+ CreateWithTypeName_Call](osaction/3567114-createwithtypename_call.md)
- [+ CreateWithTypeName_Impl](osaction/3567115-createwithtypename_impl.md)
- [+ CreateWithTypeName_Invoke](osaction/3567116-createwithtypename_invoke.md)
- [+ Create_Call](osaction/3223363-create_call.md)
- [+ Create_Impl](osaction/3223364-create_impl.md)
- [+ Create_Invoke](osaction/3223365-create_invoke.md)

## Relationships

### Inherits From
- [OSActionInterface](osactioninterface.md)
- [OSObject](osobject.md)

## See Also

- [OSActionInterface](osactioninterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osaction)*