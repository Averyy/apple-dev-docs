# kIOUSBReserved1Err

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
#define kIOUSBReserved1Err
```

## Discussion

These errors are returned by the OHCI controller. The # in parenthesis (xx) corresponds to the OHCI Completion Code. For the following Completion codes, we return a generic IOKit error instead of a USB specific error. 

```occ
 
Completion Code         Error Returned              Description
9                       kIOReturnUnderrun           (Data Underrun) EP returned less data than max packet size
8                       kIOReturnOverrun            (Data Overrun) Packet too large or more data than buffer
5                       kIOReturnNotResponding      Device Not responding
4                       kIOUSBPipeStalled           Endpoint returned a STALL PID
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiousbreserved1err)*