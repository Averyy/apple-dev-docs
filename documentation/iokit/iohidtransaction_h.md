# IOHIDTransaction.h

**Framework**: IOKit  
**Role**: API Collection

#### Overview

IOHIDTransaction defines an object used to manipulate multiple parsed items (IOHIDElement) contained within a Human Interface Device (HID) object. It is used to minimize device communication when interacting with feature and output type elements that are grouped by their report IDs. IOHIDTransaction is a CFType object and as such conforms to all the conventions expected such object.

This documentation assumes that you have a basic understanding of the material contained in [Introduction to Accessing Hardware From Applications](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Intro/AH_Intro.html#//apple_ref/doc/uid/TP40002714).

All of the information described in this document is contained in the header file `IOHIDTransaction.h` found at `/System/Library/Frameworks/IOKit.framework/Headers/hid/IOHIDTransaction.h`.

##### Included Headers

- <CoreFoundation/CoreFoundation.h>
- <IOKit/hid/IOHIDBase.h>

## Topics

### Miscellaneous
- [IOHIDTransactionAddElement](./api-1561679-iohidtransactionaddelement.md)
  Adds an element to the transaction @disussion To minimize device traffic it is important to add elements that share a common report type and report id.
- [IOHIDTransactionClear](./api-1561687-iohidtransactionclear.md)
  Clears element transaction values.
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
### Data Types
- [IOHIDTransactionRef](./iohidtransactionref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidtransaction_h)*