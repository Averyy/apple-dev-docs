# Priority Constants for the AESend Function (Deprecated in macOS)

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify a value for the `sendPriority` parameter of the `AESend` function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kAENormalPriority](./api-1542840-priority_constants_for_the_aesen/kaenormalpriority.md)
  The Apple Event Manager posts the event at the end of the event queue of the server process and the server processes the Apple event as soon as it has the opportunity.
- [kAEHighPriority](./api-1542840-priority_constants_for_the_aesen/kaehighpriority.md)
  The Apple Event Manager posts the event at the beginning of the event queue of the server process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542840-priority_constants_for_the_aesen)*