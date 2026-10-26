# IOHIDTransactionClear

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Clears element transaction values.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```c
void IOHIDTransactionClear(IOHIDTransactionRef transaction);
```

#### Discussion

In regards to kIOHIDTransactionDirectionTypeOutput direction, default element values will be preserved.

## Parameters

- `transaction`: IOHIDTransaction object to be modified.

## See Also

### Miscellaneous
- [IOHIDTransactionAddElement](./api-1561679-iohidtransactionaddelement.md)
  Adds an element to the transaction @disussion To minimize device traffic it is important to add elements that share a common report type and report id.
- [IOHIDTransactionCommit](./api-1561681-iohidtransactioncommit.md)
  Synchronously commits element transaction to the device.
- [IOHIDTransactionCommitWithCallback](./api-1561677-iohidtransactioncommitwithcallba.md)
  Commits element transaction to the device.
- [IOHIDTransactionContainsElement](./api-1561680-iohidtransactioncontainselement.md)
  Queries the transaction to determine if elemement has been added.
- [IOHIDTransactionCreate](./api-1561689-iohidtransactioncreate.md)
  Creates an IOHIDTransaction object for the specified device.
- [IOHIDTransactionGetDevice](./api-1561685-iohidtransactiongetdevice.md)
  Obtain the device associated with the transaction.
- [IOHIDTransactionGetDirection](./api-1561674-iohidtransactiongetdirection.md)
  Obtain the direction of the transaction.
- [IOHIDTransactionGetTypeID](./api-1561678-iohidtransactiongettypeid.md)
  Returns the type identifier of all IOHIDTransaction instances.
- [IOHIDTransactionGetValue](./api-1561683-iohidtransactiongetvalue.md)
  Obtains the value for a transaction element.
- [IOHIDTransactionRemoveElement](./api-1561686-iohidtransactionremoveelement.md)
  Removes an element to the transaction
- [IOHIDTransactionScheduleWithRunLoop](./api-1561675-iohidtransactionschedulewithrunl.md)
  Schedules transaction with run loop.
- [IOHIDTransactionSetDirection](./api-1561688-iohidtransactionsetdirection.md)
  Sets the direction of the transaction @disussion This method is useful for manipulating bi-direction (feature) elements such that you can set or get element values without creating an additional transaction object.
- [IOHIDTransactionSetValue](./api-1561676-iohidtransactionsetvalue.md)
  Sets the value for a transaction element.
- [IOHIDTransactionUnscheduleFromRunLoop](./api-1561682-iohidtransactionunschedulefromru.md)
  Unschedules transaction with run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1561687-iohidtransactionclear)*