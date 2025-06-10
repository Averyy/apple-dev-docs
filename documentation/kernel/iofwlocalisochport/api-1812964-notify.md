# notify

**Framework**: Kernel  
**Kind**: instm

Informs hardware of a change to the DCL program.

## Declaration

```swift
virtual IOReturn notify( 
 IOFWDCLNotificationTypenotificationType, 
 DCLCommand **dclCommandList, 
 UInt32numDCLCommands );
```

#### Return_value

IOKit error code.

## Parameters

- `notificationType`: Type of change.
- `dclCommandList`: List of DCL commands that have been changed.
- `numDCLCommands`: Number of commands in list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwlocalisochport/1812964-notify)*